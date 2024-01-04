---
nav_title: Page types
page_order: 1
noindex: true
---

#  Page types

> The following page types can be assigned to the [`page_type`]({{sitebase.url}}/docs/home/yaml_front_matter/metadata/#page-type) key in a page's YAML front matter. For more general information, see [About our framework]({{sitebase.url}}/docs/home/about_our_framework/#pages).

## Prerequisites

To use a page type, you'll need to add the [`page_type`]({{sitebase.url}}/docs/home/yaml_front_matter/metadata/#page-type) key to your YAML front matter:

```markdown
---
nav_title: Getting started
article_title: Getting started with Braze Docs
page_type: PAGE_TYPE_VALUE
---
```

Replace `PAGE_TYPE_VALUE` with one of the values from the following sections:

## Accepted values

### Glossary

- **Value:** `glossary`
- **Description:** Page provides a searchable description of certain terms or elements (metrics, words to know, API Endpoints, etc.)
- **Available Templates:**
    - [API or Code Glossary](../../_docs/_home/templates/api_glossary.md)
    - [General Glossary](../../_docs/_home/templates/glossary_test_page.md)

### Solution

- **Value:** `solution`
- **Description:** A troubleshooting or "options" article that walks users through a solution to an issue or through steps to resolving or narrowing down an issue.
- **Available Templates:**
    - [Help Article](../../_docs/_home/templates/help_article_template.md)
    - [Solution Article](../../_docs/_home/templates/solution.md)

### Reference

- **Value:** `reference`
- **Description:** An article that explains a concept and contains specific information about technical processes and product content. (Canvas Steps, Segmentation, specific Product Features etc.).
- **Available Templates:**
    - [Reference Article with Video](../../_docs/_home/templates/reference_vide.md)
    - [Reference Article](../../_docs/_home/templates/reference.md)

### Tutorial

- **Value:** `tutorial`
- **Description:** A general walk-through of an instructional concept. Should contain practical knowledge. Focuses on a single topic (like, how to create a campaign, how to create a Canvas, etc.) Goal or Task-Oriented Article that walks step-by-step through solving a specific issue (How to target specific users, how to segment based on location, etc.).
- **Available Templates:**
    - [Tutorial Article with Video](../../_docs/_home/templates/tutorial_video.md)
    - [Tutorial Article](../../_docs/_home/templates/tutorial.md)
    - [Use Case Article with Video](../../_docs/_home/templates/use_case_video.md)
    - [Use Case Article](../../_docs/_home/templates/use_case.md)

### Landing page

- **Value:** `landing`
- **Description:** Page provides a selection of options within a certain section, as well as a description or overview of said section.
- **Available Templates:**
    - [Single Section Landing Page using FA Icons](../../_docs/_home/templates/landing_single.md)
    - [Single Section Landing Page using Images](../../_docs/_home/templates/landing_images.md)
    - [Multi-Section Landing Page using FA Icons](../../_docs/_home/templates/landing_multiple.md)
    - [Multi-Section Landing Page using Images](../../_docs/_home/templates/landing_multiple_images.md)

### Partner

- **Value:** `partner`
- **Description:** A page that combines many of the preceding page types into a single page. These pages describe a partner, the benefits of that partner, how to integrate that partner, then how to use that integration and any best practices associated with that usage.
- **Available Templates:**
    - [Partner Page with Video](../../_docs/_home/templates/partner_page_template_video.md)
    - [Partner Page](../../_docs/_home/templates/partner_page_template.md)

### Updates and Release Notes

- **Value:** `update`
- **Description:** A page that lists updates to a product or SDK in succession. A single update on a larger page or a page about a new feature would **not** count as an `update` page type.
- **Available Templates:** See Release Notes Pages and SDK Changelogs pages.
