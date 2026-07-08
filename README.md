# sw-metadata-bot-monitor-web

A website to display the results of running the sw metadata bot on different organizations

## Installation

### Option 1: Using uv (recommended)

```bash
uv sync
```

This creates/updates `.venv` and installs all project dependencies from `pyproject.toml`.

### Option 2: Using pip

```bash
python -m pip install --upgrade pip
python -m pip install "pystache>=0.6.8" "sw-metadata-bot>=0.4.1"
```

If you prefer isolated environments, create and activate a virtual environment first:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install "pystache>=0.6.8" "sw-metadata-bot>=0.4.1"
```

## Running Analysis and Updating the Dashboard

Use the helper script to run new analysis, submit issues and update the index.html:

```bash
make
```

The script now supports two modes automatically:

1. `uv` mode when both `uv` and `.venv/` are available
2. `pip` fallback mode when `uv` is not available or `.venv/` does not exist

In fallback mode, it installs required Python dependencies (`sw-metadata-bot`, `pystache`) with `pip` before running.

## Generating Only the Landing Page

If analysis output already exists, regenerate HTML pages with:

```bash
python generate_landing_page.py --config-file input/config.json
```

The generator reads snapshots from `outputs/<run_name>/<snapshot_tag>/run_report.json` and renders:

1. `index.html` for the latest snapshot
2. `history/report_<snapshot_tag>.html` for each available snapshot
