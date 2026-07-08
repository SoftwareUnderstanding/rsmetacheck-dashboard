import argparse
import datetime
import glob
import json
import os
from datetime import timezone

import pystache


def collect_dashboard_data(config: dict) -> tuple[list[dict], dict]:
    """Collect summary data from snapshot report_summary.json files."""
    outputs_config = config["outputs"]
    root_dir = outputs_config.get("root_dir") or outputs_config.get("output_root_dir")
    run_name = outputs_config["run_name"]
    snapshot_tag_format = outputs_config["snapshot_tag_format"]

    pattern = os.path.join(root_dir, run_name, "*", "report_summary.json")
    summary_points = []

    for summary_path in glob.glob(pattern):
        snapshot_tag = os.path.basename(os.path.dirname(summary_path))
        try:
            dt = datetime.datetime.strptime(snapshot_tag, snapshot_tag_format)
            label = dt.strftime("%b %d, %Y")
        except ValueError:
            label = snapshot_tag

        try:
            with open(summary_path, "r") as f:
                summary_data = json.load(f)
        except Exception:
            continue

        repository_count = summary_data.get("repository_count", 0)
        total_pitfalls = summary_data.get("total_pitfalls", 0)
        total_warnings = summary_data.get("total_warnings", 0)
        pitfalls_by_ids = summary_data.get("pitfalls_by_id", {})
        warnings_by_ids = summary_data.get("warnings_by_id", {})
        repo_issue_status: dict = summary_data.get("reason_codes_by_action", {})
        issues_created = summary_data.get("issues_created", 0)
        mean_pitfalls_per_repo = summary_data.get("pitfalls_per_repository", 0)
        mean_warnings_per_repo = summary_data.get("warnings_per_repository", 0)
        summary_points.append(
            {
                "snapshot_tag": snapshot_tag,
                "label": label,
                "path": summary_path,
                "repository_count": repository_count,
                "total_pitfalls": total_pitfalls,
                "total_warnings": total_warnings,
                "issues_created": issues_created,
                "pitfalls_by_ids": pitfalls_by_ids,
                "warnings_by_ids": warnings_by_ids,
                "repo_issue_status": repo_issue_status,
                "mean_pitfalls_per_repo": mean_pitfalls_per_repo,
                "mean_warnings_per_repo": mean_warnings_per_repo,
            }
        )

    summary_points.sort(key=lambda x: x["snapshot_tag"])

    totals = {
        "analysis_count": len(summary_points),
        "issues_created_total": sum(item["issues_created"] for item in summary_points),
        "total_pitfalls": sum(item["total_pitfalls"] for item in summary_points),
        "total_warnings": sum(item["total_warnings"] for item in summary_points),
    }
    return summary_points, totals


def argument_parser() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--config-file",
        default="input/config.json",
        help="Path to the bot config file (default: input/config.json)",
    )
    args = parser.parse_args()
    return args


def process_data(report_data: dict):
    """Enhance raw JSON data for the template."""
    repos = []
    for repo in report_data["records"]:
        name = repo["repo_url"].rstrip("/").split("/")[-1]

        try:
            analysis_date = datetime.datetime.fromisoformat(
                repo["analysis_date"].replace("Z", "+00:00")
            )
            analysis_date_formatted = analysis_date.strftime("%b %d, %Y")
        except Exception:
            analysis_date_formatted = repo["analysis_date"]

        has_issues = False
        has_pitfalls = False
        has_warnings = False

        if repo.get("pitfalls_ids"):
            has_issues = True
            has_pitfalls = True

        if repo.get("warnings_ids"):
            has_issues = True
            has_warnings = True

        repo_enhanced = repo.copy()
        repo_enhanced["repo_name"] = name
        repo_enhanced["analysis_date_formatted"] = analysis_date_formatted
        repo_enhanced["has_issues"] = has_issues
        repo_enhanced["has_pitfalls"] = has_pitfalls
        repo_enhanced["has_warnings"] = has_warnings

        repos.append(repo_enhanced)
    return repos


def scan_run_reports(config: dict) -> list[dict]:
    """Scan the outputs directory and return run_report snapshots sorted oldest-first.

    Each entry contains:
        snapshot_tag  — folder name used as tag (e.g. "20260408")
        label         — human-readable date string (e.g. "April 08, 2026")
        path          — path to run_report.json
    """
    outputs_config = config["outputs"]
    root_dir = outputs_config.get("root_dir") or outputs_config.get("output_root_dir")
    run_name = outputs_config["run_name"]
    snapshot_tag_format = outputs_config["snapshot_tag_format"]

    pattern = os.path.join(root_dir, run_name, "*", "run_report.json")
    snapshots = []
    for report_path in glob.glob(pattern):
        snapshot_tag = os.path.basename(os.path.dirname(report_path))
        try:
            dt = datetime.datetime.strptime(snapshot_tag, snapshot_tag_format)
            label = dt.strftime("%B %d, %Y")
        except ValueError:
            label = snapshot_tag
        snapshots.append(
            {"snapshot_tag": snapshot_tag, "label": label, "path": report_path}
        )

    snapshots.sort(key=lambda x: x["snapshot_tag"])
    return snapshots


def build_history_links(
    snapshots: list[dict], history_dir: str = "history"
) -> list[dict]:
    """Convert a list of snapshots into navigation link dictionaries for the template."""
    links = []
    for snapshot in snapshots:
        html_filename = f"report_{snapshot['snapshot_tag']}.html"
        links.append(
            {
                "url": f"{history_dir}/{html_filename}",
                "label": snapshot["label"],
                "filename": html_filename,
                "snapshot_tag": snapshot["snapshot_tag"],
            }
        )
    return links


def main():
    HISTORY_DIR = "history"
    os.makedirs(HISTORY_DIR, exist_ok=True)

    args = argument_parser()
    with open(args.config_file, "r") as f:
        config = json.load(f)

    snapshots = scan_run_reports(config)
    if not snapshots:
        outputs_config = config["outputs"]
        root = os.path.join(
            outputs_config.get("root_dir") or outputs_config.get("output_root_dir"),
            outputs_config["run_name"],
        )
        print(f"No run_report.json files found under {root}/. Exiting.")
        return

    all_links = build_history_links(snapshots)
    root_links = [
        {"url": lk["url"], "label": lk["label"], "is_active": False} for lk in all_links
    ]

    with open("template.mustache", "r") as f:
        template = f.read()

    print("Regenerating historical HTMLs...")
    for snapshot, link in zip(snapshots, all_links):
        with open(snapshot["path"], "r") as f:
            snapshot_data = json.load(f)

        snapshot_repos = process_data(snapshot_data)

        page_links = [
            {
                "url": lk["filename"],
                "label": lk["label"],
                "is_active": lk["filename"] == link["filename"],
            }
            for lk in all_links
        ]

        template_data = {
            "date_stamp": snapshot["label"],
            "total_repos": len(snapshot_repos),
            "repos": snapshot_repos,
            "history_links": page_links,
            "base_path": "../",
            "is_current": False,
        }

        html = pystache.render(template, template_data)
        with open(os.path.join(HISTORY_DIR, link["filename"]), "w") as f:
            f.write(html)

    dashboard_points, dashboard_totals = collect_dashboard_data(config)
    dashboard_data_available = bool(dashboard_points)
    dashboard_data_json = json.dumps(dashboard_points)

    with open("dashboard_template.mustache", "r") as f:
        dashboard_template = f.read()

    dashboard_date = datetime.datetime.now(timezone.utc).strftime(
        "%B %d, %Y at %H:%M UTC"
    )
    dashboard_template_data = {
        "date_stamp": dashboard_date,
        "analysis_count": dashboard_totals["analysis_count"],
        "issues_created_total": dashboard_totals["issues_created_total"],
        "total_pitfalls": dashboard_totals["total_pitfalls"],
        "total_warnings": dashboard_totals["total_warnings"],
        "dashboard_data_available": dashboard_data_available,
        "dashboard_data_json": dashboard_data_json,
        "base_path": "",
        "history_links": root_links,
    }
    dashboard_html = pystache.render(dashboard_template, dashboard_template_data)
    with open("dashboard.html", "w") as f:
        f.write(dashboard_html)

    # Generate the current index.html from the most recent snapshot
    current_snapshot = snapshots[-1]
    with open(current_snapshot["path"], "r") as f:
        current_data = json.load(f)

    current_repos = process_data(current_data)

    generated_at_raw = current_data.get("run_metadata", {}).get("generated_at")
    if generated_at_raw:
        generated_at = datetime.datetime.fromisoformat(
            generated_at_raw.replace("Z", "+00:00")
        )
        date_stamp = generated_at.strftime("%B %d, %Y at %H:%M UTC")
    else:
        date_stamp = datetime.datetime.now(timezone.utc).strftime(
            "%B %d, %Y at %H:%M UTC"
        )

    template_data = {
        "date_stamp": date_stamp,
        "total_repos": len(current_repos),
        "repos": current_repos,
        "history_links": root_links,
        "base_path": "",
        "is_current": True,
    }

    html = pystache.render(template, template_data)
    with open("index.html", "w") as f:
        f.write(html)

    print("#### index.html and history were generated successfully ####")


if __name__ == "__main__":
    main()
