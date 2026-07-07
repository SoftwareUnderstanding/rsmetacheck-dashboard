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

**Repository:** https://github.com/SoftwareUnderstanding/SOMEF-Vider
**Analysis Date:** 2026-07-03
**sw-metadata-bot version:** 0.5.2
**RSMetacheck version:** 0.3.1

## 🔴 Pitfalls (1)

### [P017](https://w3id.org/rsmetacheck/catalog/#P017)
**Evidence:** P017 detected: codemeta.json version '0.0.2' does not match version '0.1.0' in package.json

**Suggestion:** You need to synchronize all version references across metadata and build configuration files. (Repository matches github API: https://github.com/SoftwareUnderstanding/SOMEF-Vider)

## ⚠️ Warnings (1)

### [W002](https://w3id.org/rsmetacheck/catalog/#W002)
**Evidence:** W002 detected: metadata files dateModified '2026-03-19T00:00:00' is outdated compared to repository date '2026-05-18T10:17:45'

**Suggestion:** The data in the metadata file should be updated to be aligned with the date of the latest release (2026-05-18T10:17:45).


---

This report was generated automatically by [sw-metadata-bot](https://github.com/SoftwareUnderstanding/sw-metadata-bot) on your main default branch.

If you're not interested in participating, please comment "unsubscribe" and we will remove your repository from our list.
If you would like the pitfalls and warnings to be fixed automatically, please comment "auto-fix" and we will prioritize adding this feature in future iterations.
