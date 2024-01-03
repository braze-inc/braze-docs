---
nav_title: YAML front matter 
page_order: 5
noindex: true
---

#  YAML front matter

> The following metadata and page types can be added to a page's YAML front matter.

## Metadata

### `nav_title`

- **Description:** This is the title of the article that will appear in the left navigation of the Docs site. Encapsulate in quotes.
- **Required?:** Yes, unless page is `hidden`.
- **Accepts Multiple Values?:** No.
- **Data Type:** String.
- **Available Values:** Any - the title of a page is up to you. We recommend less than 30 characters with spaces.

### `page_order`

- **Description:** This is the order in which the article will appear in the left navigation of the Docs site.
- **Required?:** Yes, unless page is hidden.
- **Accepts Multiple Values?:** No.
- **Data Type:** Integer.
- **Available Values:** Any number (including multiple decimals) between `1` and `100`. You can use `1.1`, `1.2`, `1.3`, etc. to order pages, as well.

### `hidden`

- **Description:** Whether the page will be visible in the left navigation bar. Setting this to `false` will cause the page not to appear in searches (both on-site or through online search providers).
- **Required?:** No.
- **Accepts Multiple Values?:** No.
- **Data Type:** Boolean.
- **Available Values:** You may choose between `true` and `false`.

### `config_only`

- **Description:** Whether a page will act as a page or as a category in the left navigation panel. Defaults to `false`.
- **Required?:** No.
- **Accepts Multiple Values?:** No.
- **Data Type:** Boolean.
- **Available Values:** You may choose between `true` and `false`.

### `permalink`

- **Description:** Sets the page's url. For example: `permalink: /this_page_name/` will set the page's URL to `https://www.braze.com/docs/this_page_name/`.
- **Required?:** No, unless page is `hidden`.
- **Accepts Multiple Values?:** No.
- **Data Type:** String.
- **Available Values:** Any - this URL is up to you. Encapsulate in slashes (`/`).

### `layout`

- **Description:** Sets specific features on the page that align with developed layouts. Defaults is a regular page.
- **Required?:** No.
- **Accepts Multiple Values?:** No.
- **Data Type:** String.
- **Available Values:** If you do not set this, it will default to a regular content page. You may choose between: `api_page`, `dev_guide`, `featured_video`, `featured`, `glossary_page`, `blank_config`, and `redirect`. There are others, but those are mostly for internal and config uses.

### `hide_toc`

- **Description:** Determines whether the Table of Contents on the right side of the page is included or not.
- **Required?:** No.
- **Accepts Multiple Values?:** No.
- **Data Type:** Boolean.
- **Available Values:** You may choose between `true` and `false`.

### `noindex`

- **Description:** Determines whether the article will show in Algolia and Google Searches. Defaults to `false` unless you have the `hidden` YAML tag set as `true`.
- **Required?:** No.
- **Accepts Multiple Values?:** No.
- **Data Type:** Boolean.
- **Available Values:** `true` or `false`.

### `description`

- **Description:** Description of the page that will show in online searches. Encapsulate in quotes.
- **Required?:** Yes.
- **Accepts Multiple Values?:** No.
- **Data Type:** String.
- **Available Values:** Any - the page description of a page is up to you. We recommend less than 3 sentences. Template: `This {page_type} {lists, describes, walks you through} {topic or task} for {platform and/or channel} using {tool}.` Though the exact phrasing can vary, it must include at least the page type, what the page aims to do (as in, it will "walk you through how to perform noted task" or "teach you how to read a certain report" or "describe the requirements of a certain Partner integration". Example: `This glossary lists all of the terms you need to know while onboarding with Braze and preparing for the Integration Phase.` Or `This reference article describes the different kinds of Canvas Steps and how they affect iOS or Android push campaigns.` Or even `This solutions article will walk you through a custom integration.`

### `page_type`

- **Description:** Type of page, determined by page templates. Inform formatting and content.
- **Required?:** Yes.
- **Accepts Multiple Values?:** No.
- **Data Type:** String.
- **Available Values:** See [Page Types](#page-types).

### `platform`

- **Description:** Notes which platforms (iOS, Android, etc.) the article is associated with.
- **Required?:** No, unless on a Dev Guide page.
- **Accepts Multiple Values?:** Multiple values can be used.
- **Data Type:** String.
- **Available Values:** Any of the platforms Braze integrates on: `iOS`, `Android`, `Web`, `API`, and any of the wrapper SDKs.

### `channel`

- **Description:** Notes which messaging channels (push, in-app messages, etc.) the article is associated with.
- **Required?:** No, unless the content mentions a specific channel or channels.
- **Accepts Multiple Values?:** Multiple values can be used.
- **Data Type:** String.
- **Available Values:** Any of the messaging channels Braze sends to: `content cards`, `email`, `news feed`, `in-app messages`, `push`, `sms`, and `webhooks`.

### `tool`

- **Description:** Notes which engagement tools (Canvas, campaigns, etc.) the article is associated with.
- **Required?:** Yes.
- **Accepts Multiple Values?:** Multiple values can be used.
- **Data Type:** String.
- **Available Values:** Any of the following Braze  tools: `dashboard`, `docs`, `canvas`, `campaigns`, `segments`, `templates`, `media`, `location`, `currents`, `reports`.

## Page types 

{% alert important %}
Note that there can only be a single `page_type` value for page. A page cannot be both a `reference` and a `glossary`. The different page types exist to narrow the scope and purpose of each article.
{% endalert %}

### Glossary Page

- **Key:** `glossary`
- **Description:** Page provides a searchable description of certain terms or elements (metrics, words to know, API Endpoints, etc.)
- **Available Templates:**
    - [API or Code Glossary](../../_docs/_home/templates/api_glossary.md)
    - [General Glossary](../../_docs/_home/templates/glossary_test_page.md)

### Solution Page

- **Key:** `solution`
- **Description:** A troubleshooting or "options" article that walks users through a solution to an issue or through steps to resolving or narrowing down an issue.
- **Available Templates:**
    - [Help Article](../../_docs/_home/templates/help_article_template.md)
    - [Solution Article](../../_docs/_home/templates/solution.md)

### Reference Page

- **Key:** `reference`
- **Description:** An article that explains a concept and contains specific information about technical processes and product content. (Canvas Steps, Segmentation, specific Product Features etc.).
- **Available Templates:**
    - [Reference Article with Video](../../_docs/_home/templates/reference_vide.md)
    - [Reference Article](../../_docs/_home/templates/reference.md)

### Tutorial Page

- **Key:** `tutorial`
- **Description:** A general walk-through of an instructional concept. Should contain practical knowledge. Focuses on a single topic (like, how to create a campaign, how to create a Canvas, etc.) Goal or Task-Oriented Article that walks step-by-step through solving a specific issue (How to target specific users, how to segment based on location, etc.).
- **Available Templates:**
    - [Tutorial Article with Video](../../_docs/_home/templates/tutorial_video.md)
    - [Tutorial Article](../../_docs/_home/templates/tutorial.md)
    - [Use Case Article with Video](../../_docs/_home/templates/use_case_video.md)
    - [Use Case Article](../../_docs/_home/templates/use_case.md)

### Landing Page

- **Key:** `landing`
- **Description:** Page provides a selection of options within a certain section, as well as a description or overview of said section.
- **Available Templates:**
    - [Single Section Landing Page using FA Icons](../../_docs/_home/templates/landing_single.md)
    - [Single Section Landing Page using Images](../../_docs/_home/templates/landing_images.md)
    - [Multi-Section Landing Page using FA Icons](../../_docs/_home/templates/landing_multiple.md)
    - [Multi-Section Landing Page using Images](../../_docs/_home/templates/landing_multiple_images.md)

### Partner Page

- **Key:** `partner`
- **Description:** A page that combines many of the preceding page types into a single page. These pages describe a partner, the benefits of that partner, how to integrate that partner, then how to use that integration and any best practices associated with that usage.
- **Available Templates:**
    - [Partner Page with Video](../../_docs/_home/templates/partner_page_template_video.md)
    - [Partner Page](../../_docs/_home/templates/partner_page_template.md)

### Updates and Release Notes

- **Key:** `update`
- **Description:** A page that lists updates to a product or SDK in succession. A single update on a larger page or a page about a new feature would **not** count as an `update` page type.
- **Available Templates:** See Release Notes Pages and SDK Changelogs pages.

