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

**Repository:** https://gitlab.in2p3.fr/christopher.eckner/mlfermilatdwarfs/
**Analysis Date:** 2026-07-03
**sw-metadata-bot version:** 0.5.2
**RSMetacheck version:** 0.3.1

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
    "name": "MIT License",
    "url": "https://spdx.org/licenses/MIT",
    "identifier": "https://spdx.org/licenses/MIT"
  },
  "codeRepository": "https://gitlab.in2p3.fr/christopher.eckner/mlfermilatdwarfs/",
  "issueTracker": "https://gitlab.in2p3.fr/christopher.eckner/mlfermilatdwarfs//issues",
  "copyrightHolder": "ECKNER Christopher",
  "copyrightYear": "2021",
  "downloadUrl": "https://gitlab.in2p3.fr/christopher.eckner/mlfermilatdwarfs/-/branches",
  "keywords": [
    "gamma-ray astronomy",
    "particle physics",
    "indirect dark matter searches"
  ],
  "programmingLanguage": [
    "Python"
  ],
  "softwareRequirements": [
    {
      "name": "numpy",
      "@type": "SoftwareApplication",
      "version": ">=1.19"
    },
    {
      "name": "scipy",
      "@type": "SoftwareApplication",
      "version": ">=1.6.2"
    },
    {
      "name": "iminuit",
      "@type": "SoftwareApplication",
      "version": "<=1.5.4"
    },
    {
      "name": "astropy",
      "@type": "SoftwareApplication",
      "version": ">=4.1"
    },
    {
      "name": "scikit-learn",
      "@type": "SoftwareApplication",
      "version": ">=0.24"
    }
  ],
  "continuousIntegration": "https://gitlab.in2p3.fr/christopher.eckner/mlfermilatdwarfs/-/blob/master/.gitlab-ci.yml",
  "releaseNotes": "First stable release.",
  "softwareVersion": "v1.0",
  "datePublished": "2021-10-22",
  "buildInstructions": [
    "https://gitlab.in2p3.fr/christopher.eckner/mlfermilatdwarfs/-/blob/master/README.md"
  ],
  "author": [
    {
      "@type": "Person",
      "email": "calore@lapth.cnrs.fr, serpico@lapth.cnrs.fr, b.zaldivar.m@csic.es",
      "name": "calore@lapth.cnrs.fr, serpico@lapth.cnrs.fr, b.zaldivar.m@csic.es"
    }
  ],
  "readme": "https://gitlab.in2p3.fr/christopher.eckner/mlfermilatdwarfs/-/blob/master/README.md",
  "description": [
    "It is a <tt>python</tt> code to derive data-driven upper limits on the thermally averaged, velocity-weighted pair-annihilation cross-section (velocity-independent; $s$-wave) of a user-defined particle dark matter model using the expected differential gamma-ray spectrum of pair-annihilation events (provided by the user) as well as 10 years of Fermi-LAT data from observations of the Milky Way\u00b4s dwarf spheroidal galaxies. \n"
  ]
}
```


---

This report was generated automatically by [sw-metadata-bot](https://github.com/SoftwareUnderstanding/sw-metadata-bot) on your main default branch.

If you're not interested in participating, please comment "unsubscribe" and we will remove your repository from our list.
If you would like the pitfalls and warnings to be fixed automatically, please comment "auto-fix" and we will prioritize adding this feature in future iterations.
