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

**Repository:** https://gitlab.in2p3.fr/escape2020/wp3/template_project_escape
**Analysis Date:** 2026-07-06
**sw-metadata-bot version:** 0.5.3
**RSMetacheck version:** 0.3.1

## 🔴 Pitfalls (2)

### [P012](https://w3id.org/rsmetacheck/catalog/#P012)
**Evidence:** P012 detected: metadata files downloadURL is outdated or invalid: https://gitlab.in2p3.fr/escape2020/wp3/template_project_escape/-/archive/v2.2/template_project_escape-v2.2.tar.gz

**Suggestion:** You need to update the downloadURL field (https://gitlab.in2p3.fr/escape2020/wp3/template_project_escape/-/archive/v2.2/template_project_escape-v2.2.tar.gz) to point to your latest release or current distribution source.

### [P014](https://w3id.org/rsmetacheck/catalog/#P014)
**Evidence:** P014 detected: metadata files Identifier uses bare DOI instead of full URL: '10.5281/zenodo.3884963'

**Suggestion:** You should include the full DOI URL form in your metadata (e.g., https://doi.org/10.5281/zenodo.3884963)

## ⚠️ Warnings (2)

### [W001](https://w3id.org/rsmetacheck/catalog/#W001)
**Evidence:** W001 detected: codemeta.json contains software requirements without versions: numpy, requests, pytest, pyyaml

**Suggestion:** Add version numbers to your dependencies. This provides stability for users and allows reproducibility across different environments.

### [W004](https://w3id.org/rsmetacheck/catalog/#W004)
**Evidence:** W004 detected: metadata files Programming languages without versions: Python, Bash

**Suggestion:** Include version numbers for each programming language used. Defining these helps ensure reproducibility and compatibility across systems.


---

This report was generated automatically by [sw-metadata-bot](https://github.com/SoftwareUnderstanding/sw-metadata-bot) on your main default branch.

If you're not interested in participating, please comment "unsubscribe" and we will remove your repository from our list.
If you would like the pitfalls and warnings to be fixed automatically, please comment "auto-fix" and we will prioritize adding this feature in future iterations.
