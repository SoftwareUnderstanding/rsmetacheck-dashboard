You are part of the Software Understanding metadata quality initiative beta analysis. This initiative is meant to test the use of a bot to monitor the quality of metadata in software repositories.

This automated issue includes:
- Detected metadata pitfalls and warnings
- A suggested codemeta.json when no codemeta.json was detected
- Suggestions for fixing each issue

## Context

This analysis is performed by the [CodeMetaSoft](https://w3id.org/codemetasoft) project to help improve research software metadata quality.

This is a first initiative aimed at identifying and reporting metadata quality issues across research software repositories. 
At this stage, we only provide diagnostics and recommendations. 
In future iterations, we plan to propose automated fixes for the detected issues to further simplify the improvement process and reduce manual effort.
Feedbacks are welcome and will help us improve the tool and its recommendations.
[![Feedbacks](https://img.shields.io/badge/feedbacks-blue?style=for-the-badge)](https://github.com/SoftwareUnderstanding/sw-metadata-bot/issues/new?template=feedback.yml)

Each pitfall and warning is identified by a unique code (e.g. P001 for pitfalls, W004 for warnings) that corresponds to specific metadata quality issues.
You can find more details about these checks and how to address them in the [RSMetacheck catalog](https://softwareunderstanding.github.io/RsMetaCheck/).


# Metadata Quality Report

**Repository:** https://github.com/AMIGA-IAA/hcg-16
**Analysis Date:** 2026-07-06
**sw-metadata-bot version:** 0.5.3
**RSMetacheck version:** 0.3.1

## 🔴 Pitfalls (2)

### [P001](https://w3id.org/rsmetacheck/catalog/#P001)
**Evidence:** P001 detected: codemeta.json version '1.2.1' does not match release version '1.2.3'

**Suggestion:** Ensure the version in your metadata matches the latest official release (1.2.3). Keeping these synchronized avoids confusion for users and improves reproducibility.

### [P008](https://w3id.org/rsmetacheck/catalog/#P008)
**Evidence:** P008 detected: codemeta.json Software requirements contain invalid URLs: https://github.com/AMIGA-IAA/hcg-16/blob/master/conda-linux-64.lock

**Suggestion:** Verify and update any dependency links to ensure they lead to valid and accessible pages.

## ⚠️ Warnings (3)

### [W001](https://w3id.org/rsmetacheck/catalog/#W001)
**Evidence:** W001 detected: codemeta.json contains software requirements without versions: https://github.com/AMIGA-IAA/hcg-16/blob/master/conda-linux-64.lock

**Suggestion:** Add version numbers to your dependencies. This provides stability for users and allows reproducibility across different environments.

### [W002](https://w3id.org/rsmetacheck/catalog/#W002)
**Evidence:** W002 detected: metadata files dateModified '2021-09-28T00:00:00' is outdated compared to repository date '2023-06-14T17:26:23'

**Suggestion:** The data in the metadata file should be updated to be aligned with the date of the latest release (2023-06-14T17:26:23).

### [W004](https://w3id.org/rsmetacheck/catalog/#W004)
**Evidence:** W004 detected: metadata files Programming languages without versions: Python

**Suggestion:** Include version numbers for each programming language used. Defining these helps ensure reproducibility and compatibility across systems.


---

This report was generated automatically by [sw-metadata-bot](https://github.com/SoftwareUnderstanding/sw-metadata-bot) on your main default branch.

If you're not interested in participating, please comment "unsubscribe" and we will remove your repository from our list.
If you would like the pitfalls and warnings to be fixed automatically, please comment "auto-fix" and we will prioritize adding this feature in future iterations.
