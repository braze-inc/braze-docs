---
nav_title: Page types
page_order: 5
noindex: true
---

# Page types

> These are the supported page type keys you can set in your page's YAML front matter.

{% alert important %}
Note that there can only be a single `page_type` value for page. A page cannot be both a `reference` and a `glossary`. The different page types exist to narrow the scope and purpose of each article.
{% endalert %}

## Page type keys

| Page Type <br> <br> Page Type Tag | Description | Available Templates |
| ------------- | ------------- | ------------- |
| Glossary Page <br> <br> `glossary`| Page provides a searchable description of certain terms or elements (metrics, words to know, API Endpoints, etc.) | [API or Code Glossary](../../_docs/_home/templates/api_glossary.md) <br> <br> [General Glossary](../../_docs/_home/templates/glossary_test_page.md)
| Solution Page <br> <br> `solution` | A troubleshooting or "options" article that walks users through a solution to an issue or through steps to resolving or narrowing down an issue. | [Help Article](../../_docs/_home/templates/help_article_template.md) <br> <br> [Solution Article](../../_docs/_home/templates/solution.md) |
| Reference Page <br> <br> `reference` | An article that explains a concept and contains specific information about technical processes and product content. (Canvas Steps, Segmentation, specific Product Features etc.). | [Reference Article with Video](../../_docs/_home/templates/reference_vide.md) <br> <br> [Reference Article](../../_docs/_home/templates/reference.md) |
| Tutorial Page <br> <br> `tutorial` | A general walk-through of an instructional concept. Should contain practical knowledge. Focuses on a single topic (like, how to create a campaign, how to create a Canvas, etc.) Goal or Task-Oriented Article that walks step-by-step through solving a specific issue (How to target specific users, how to segment based on location, etc.). | [Tutorial Article with Video](../../_docs/_home/templates/tutorial_video.md) <br> <br> [Tutorial Article](../../_docs/_home/templates/tutorial.md) <br> <br> [Use Case Article with Video](../../_docs/_home/templates/use_case_video.md) <br> <br> [Use Case Article](../../_docs/_home/templates/use_case.md) |
| Landing Page <br> <br> `landing` | Page provides a selection of options within a certain section, as well as a description or overview of said section. | [Single Section Landing Page using FA Icons](../../_docs/_home/templates/landing_single.md) <br> <br> [Single Section Landing Page using Images](../../_docs/_home/templates/landing_images.md) <br> <br> [Multi-Section Landing Page using FA Icons](../../_docs/_home/templates/landing_multiple.md) <br> <br> [Multi-Section Landing Page using Images](../../_docs/_home/templates/landing_multiple_images.md)
| Partner Page <br> <br> `partner` | A page that combines many of the preceding page types into a single page. These pages describe a partner, the benefits of that partner, how to integrate that partner, then how to use that integration and any best practices associated with that usage. | [Partner Page with Video](../../_docs/_home/templates/partner_page_template_video.md) <br> <br> [Partner Page](../../_docs/_home/templates/partner_page_template.md) |
| Updates and Release Notes <br> <br> `update` | A page that lists updates to a product or SDK in succession. A single update on a larger page or a page about a new feature would **not** count as an `update` page type. | See Release Notes Pages and SDK Changelogs pages. |

