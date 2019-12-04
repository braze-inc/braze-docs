---
nav_title: Docs Metadata
page_order: 0
---
# Docs Metadata

> This article walks through the options for adding metadata to Docs pages. We optimize our search based on page type and other bits of metadata, including: [yaml tags](#yaml-tags) and [page types](#page-types) (based on [templates]({{ site.baseurl }}/home/templates/)).

{% alert important %}

The [content tags](#content-tags) listed on this page are currently a work in progress and cannot be applied to pages without causing errors. Check back later for the final version, when these can be safely applied! Please note that you __can__ currently use the `platform` content tag.

{% endalert %}

## YAML Tags

These are independent. If you need to see additional optional YAML content based on "Layout", check out the [templates]({{ site.baseurl }}/home/templates/) and layouts (TBD) breakdowns.

### Configuration Tags

These will automatically change the layout or function of a page.

| YAML Content Tag | Description | Required? | Data Type | Available Values |
| ----------------- | ----------- | --------- | -------------------- |
| `nav_title` | This is the title of the article that will appear in the left navigation of the Docs site. Encapsulate in quotes. | Yes, unless page is `hidden`. | String. | Any - the title of a page is up to you. We recommend less than 30 characters with spaces. |
| `page_order` | This is the order in which the article will appear in the left navigation of the Docs site. | Yes, unless page is hidden. | Integer. | Any number (including multiple decimals) between `1` and `100`. You can use `1.1`, `1.2`, `1.3`, etc. to order pages, as well.|
| `hidden` | Notes whether or not the page will be visible in the left navigation bar. Setting this to `false` will cause the page not to appear in searches (both on-site or through online search providers). | No. | Boolean. | You may choose between `true` and `false`. |
| `config_only` | Whether or not a page will act as a page or as a category in the left navigation panel. Defaults to `false`. | No. |  Boolean. | You may choose between `true` and `false`. |
| `permalink` | Sets the page's url. For example: `permalink: /this_page_name/` will set the page's URL to `https://www.braze.com/docs/this_page_name/`. | No, unless page is `hidden`. | String. | Any - this url is up to you. Encapsulate in slashes (`/`). |
| `layout` | Sets specific features on the page that align with developed layouts. Defaults is a regular page. | No. | Sting. | If you do not set this, it will default to a regular content page. You may choose between: `api_page`, `dev_guide`, `featured_video`, `featured`, `glossary_page`, `blank_config`, and `redirect`. There are others, but those are mostly for internal and config uses. |
| `hide_toc` | Determines whether the Table of Contents on the right side of the page is included or not. | No. | Boolean. | You may choose between `true` and `false`. |

### Content Tags
These will assist in external and internal SEO, informing page content and formatting, and other content-based structure.

| YAML Content Tag | Description  | Required? | Exclusive or can multiple be used? | Data Type | Available Values |
| ----------------- | ----------- | --------- | ---------------------------------- | --------- | ---------------- |
| `description` | Description of the page that will show in online searches. Encapsulate in quotes. | Yes. | Exclusive up to 160 characters. | Sting. | Any - the page description of a page is up to you. We recommend less than 3 sentences.|
| `page_type` | Type of page, determined by page templates. Inform formatting and content. | Yes. | Exclusive; only one can be used per page. | String. | See [Page Types](#page-types) list below. |
| `platform` | Notes which platforms (iOS, Android, etc.) the article is associated with. | No, unless on a Dev Guide page.  | Multiple values can be used. | String. | Any of the platforms Braze integrates on: `iOS`, `Android`, `Web`, `API`, and any of the wrapper SDKs. |
| `channel` | Notes which messaging channels (push, in-app messages, etc.) the article is associated with. | No, unless the content mentions a specific channel or channels. | Multiple values can be used. | String. | Any of the messaging channels Braze sends to: `content cards`, `email`, `news feed`, `in-app messages`, `push`, `sms`, and `webhooks`.|
| `tool` | Notes which engagement tools (Canvas, Campaigns, etc.) the article is associated with. | Yes. | Multiple values can be used. | String. | Any of Braze's  tools: `dashboard`, `docs`, `canvas`, `campaigns`, `segments`, `templates`, `media`, `location`, `currents`, `reports`. |

### Sample YAML

The top of every markdown page should begin with a section of yaml to define the page.

```html
---
nav_title: "Docs Metadata"
page_order: 0

description: "This page walks through the options for adding metadata to Docs pages. We optimize our search based on page type and other bits of metadata. This is a great resource for contributors via our Github page."
page_type: reference
tool: 
  - docs
  - dashboard
---
```

## Page Types

To apply these, be sure your yaml parameter for page types is: `page_type:`

For example: `page_type: glossary`

| Page Type <br> <br> Page Type Tag | Description | Available Templates |
| ------------- | ------------- | ------------- |
| Glossary Page <br> <br> `glossary`| Page provides a searchable description of certain terms or elements (metrics, words to know, API Endpoints, etc.) | [API or Code Glossary]({{ site.baseurl }}/home/templates/api_glossary/) <br> <br> [General Glossary]({{ site.baseurl }}/home/templates/glossary_test_page/)
| Solution Page <br> <br> `solution` | A troubleshooting or "options" article that walks users through a solution to an issue or through steps to resolving or narrowing down an issue. | [Help Article]({{ site.baseurl }}/home/templates/help_article_template/) <br> <br> [Solution Article]({{ site.baseurl }}/home/templates/solution/) |
| Reference Page <br> <br> `reference` | An article that explains a concept and contains specific information about technical processes and product content. (Canvas Steps, Segmentation, specific Product Features etc.). | [Reference Article with Video]({{ site.baseurl }}/home/templates/reference_vide/) <br> <br> [Reference Article]({{ site.baseurl }}/home/templates/reference/) |
| Tutorial Page <br> <br> `tutorial` | A general walkthrough of an instructional concept. Should contain practical knowledge. Focuses on a single topic (like, how to create a campaign, how to create a canvas, etc.) Goal or Task-Oriented Article that walks step-by-step through solving a specific issue (How to target specific users, how to segment based on location, etc.). | [Tutorial Article with Video]({{ site.baseurl }}/home/templates/tutorial_video/) <br> <br> [Tutorial Article]({{ site.baseurl }}/home/templates/tutorial/) <br> <br> [Use Case Article with Video]({{ site.baseurl }}/home/templates/use_case_video/) <br> <br> [Use Case Article]({{ site.baseurl }}/home/templates/use_case/) |
| Landing Page <br> <br> `landing` | Page provides a selection of options within a certain section, as well as a description or overview of said section. | [Single Section Landing Page using FA Icons]({{ site.baseurl }}/home/templates/landing_single/) <br> <br> [Single Section Landing Page using Images]({{ site.baseurl }}/home/templates/landing_images/) <br> <br> [Multi-Section Landing Page using FA Icons]({{ site.baseurl }}/home/templates/landing_multiple/) <br> <br> [Multi-Section Landing Page using Images]({{ site.baseurl }}/home/templates/landing_multiple_images/)
| Partner Page <br> <br> `partner` | A page that combines many of the page types above into a single page. These pages describe a partner, the benefits of that partner, how to integrate that partner, then how to use that integration and any best practices associated with that usage. | [Partner Page with Video]({{ site.baseurl }}/home/templates/partner_page_template_video/) <br> <br> [Partner Page]({{ site.baseurl }}/home/templates/partner_page_template/) |

Potential Page Type: Best Practices
