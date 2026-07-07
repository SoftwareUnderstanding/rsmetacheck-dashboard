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

**Repository:** https://github.com/SoftwareUnderstanding/software_types
**Analysis Date:** 2026-07-06
**sw-metadata-bot version:** 0.5.3
**RSMetacheck version:** 0.2.1

## 🔴 Pitfalls (1)

### [P002](https://w3id.org/rsmetacheck/catalog/#P002)
**Evidence:** P002 detected: LICENSE file contains unreplaced template placeholders

**Suggestion:** Update the copyright section with accurate names, organizations, and the current year. Personalizing this section ensures clarity and legal accuracy.

## 📄 Missing codemeta.json

No root `codemeta.json` file was detected in the repository. A generated suggestion is provided below.

```json
{
  "@context": "https://w3id.org/codemeta/3.0",
  "@type": [
    "SoftwareSourceCode",
    "SoftwareApplication"
  ],
  "license": {
    "name": "Apache License 2.0",
    "url": "https://raw.githubusercontent.com/SoftwareUnderstanding/software_types/main/LICENSE",
    "identifier": "https://spdx.org/licenses/Apache-2.0"
  },
  "codeRepository": "https://github.com/SoftwareUnderstanding/software_types",
  "issueTracker": "https://github.com/SoftwareUnderstanding/software_types/issues",
  "dateCreated": "2022-02-03",
  "dateModified": "2025-12-09",
  "downloadUrl": "https://github.com/SoftwareUnderstanding/software_types/releases",
  "name": "software_types",
  "author": [
    {
      "@type": "Organization",
      "identifier": "SoftwareUnderstanding",
      "@id": "https://github.com/SoftwareUnderstanding"
    }
  ],
  "readme": "https://raw.githubusercontent.com/SoftwareUnderstanding/software_types/main/README.md",
  "description": [
    "Schema.org profile for software types"
  ]
}
```


---

This report was generated automatically by [sw-metadata-bot](https://github.com/SoftwareUnderstanding/sw-metadata-bot) on your main default branch.

If you're not interested in participating, please comment "unsubscribe" and we will remove your repository from our list.
If you would like the pitfalls and warnings to be fixed automatically, please comment "auto-fix" and we will prioritize adding this feature in future iterations.
