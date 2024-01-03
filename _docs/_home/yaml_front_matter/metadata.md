---
nav_title: Metadata 
page_order: 0
noindex: true
---

#  Metadata

> The following metadata keys can be added to a page's YAML front matter. For more general information, see [About our framework]({{sitebase.url}}/docs/home/about_our_framework/#pages).

## Prerequisites

To add metadata to a Markdown file, you'll need to add Jekyll's front matter syntax to the beginning of your file:

```markdown
---
METADATA_KEY: METADATA_VALUE
---

# Getting started with Braze Docs

If you're new to Braze Docs or docs-as-code, start with our tutorial.
```

Replace the following:

| Placeholder      | Description                                                                                                               |
|------------------|---------------------------------------------------------------------------------------------------------------------------|
| `METADATA_KEY`   | The key representing a supported metadata type. Replace with a [metadata key](#metadata-keys) from the following section. |
| `METADATA_VALUE` | The value assigned to the metadata key. Check a metadata key's supported values in the following section.                 |

## Supported keys

### Channel

The messaging channel a page is related to.

- **Key:** `channel`
- **Required?:** No, unless the content mentions a specific channel or channels.
- **Accepts Multiple Values?:** Multiple values can be used.
- **Data Type:** `string`
- **Available Values:** Any of the messaging channels Braze sends to: `content cards`, `email`, `news feed`, `in-app messages`, `push`, `sms`, and `webhooks`.

**Usage example:**

```markdown
---
channel: email, news feed
---
```

### Description

- **Key:** `description`
- **Description:** Description of the page that will show in online searches. Encapsulate in quotes.
- **Required?:** Yes.
- **Accepts Multiple Values?:** No.
- **Data Type:** `string`
- **Available Values:** Any - the page description of a page is up to you. We recommend less than 3 sentences. Template: `This {page_type} {lists, describes, walks you through} {topic or task} for {platform and/or channel} using {tool}.` Though the exact phrasing can vary, it must include at least the page type, what the page aims to do (as in, it will "walk you through how to perform noted task" or "teach you how to read a certain report" or "describe the requirements of a certain Partner integration". Example: `This glossary lists all of the terms you need to know while onboarding with Braze and preparing for the Integration Phase.` Or `This reference article describes the different kinds of Canvas Steps and how they affect iOS or Android push campaigns.` Or even `This solutions article will walk you through a custom integration.`

### Engagement tool

- **Key:** `tool`
- **Description:** Notes which engagement tools (Canvas, campaigns, etc.) the article is associated with.
- **Required?:** Yes.
- **Accepts Multiple Values?:** Multiple values can be used.
- **Data Type:** `string`
- **Available Values:** Any of the following Braze  tools: `dashboard`, `docs`, `canvas`, `campaigns`, `segments`, `templates`, `media`, `location`, `currents`, `reports`.

### Hide page

- **Key:** `hidden`
- **Description:** Whether the page will be visible in the left navigation bar. Setting this to `false` will cause the page not to appear in searches (both on-site or through online search providers).
- **Required?:** No.
- **Accepts Multiple Values?:** No.
- **Data Type:** `boolean`
- **Available Values:** You may choose between `true` and `false`.

### Hide page (content only)

- **Key:** `config_only`
- **Description:** Whether a page will act as a page or as a category in the left navigation panel. Defaults to `false`.
- **Required?:** No.
- **Accepts Multiple Values?:** No.
- **Data Type:** `boolean`
- **Available Values:** You may choose between `true` and `false`.

### Hide page (search only)

- **Key:** `noindex`
- **Description:** Determines whether the article will show in Algolia and Google Searches. Defaults to `false` unless you have the `hidden` YAML tag set as `true`.
- **Required?:** No.
- **Accepts Multiple Values?:** No.
- **Data Type:** `boolean`
- **Available Values:** `true` or `false`.

### Hide table of contents

- **Key:** `hide_toc`
- **Description:** Determines whether the Table of Contents on the right side of the page is included or not.
- **Required?:** No.
- **Accepts Multiple Values?:** No.
- **Data Type:** `boolean`
- **Available Values:** You may choose between `true` and `false`.

### Navigation title

- **Key:** `nav_title`
- **Description:** This is the title of the article that will appear in the left navigation of the Docs site. Encapsulate in quotes.
- **Required?:** Yes, unless page is `hidden`.
- **Accepts Multiple Values?:** No.
- **Data Type:** `string`
- **Available Values:** Any - the title of a page is up to you. We recommend less than 30 characters with spaces.

### Override default URL

- **Key:** `permalink`
- **Description:** Sets the page's url. For example: `permalink: /this_page_name/` will set the page's URL to `https://www.braze.com/docs/this_page_name/`.
- **Required?:** No, unless page is `hidden`.
- **Accepts Multiple Values?:** No.
- **Data Type:** `string`
- **Available Values:** Any - this URL is up to you. Encapsulate in slashes (`/`).

### Page layout

- **Key:** `layout`
- **Description:** Sets specific features on the page that align with developed layouts. Defaults is a regular page.
- **Required?:** No.
- **Accepts Multiple Values?:** No.
- **Data Type:** `string`
- **Available Values:** If you do not set this, it will default to a regular content page. You may choose between: `api_page`, `dev_guide`, `featured_video`, `featured`, `glossary_page`, `blank_config`, and `redirect`. There are others, but those are mostly for internal and config uses.

### Page order

- **Key:** `page_order`
- **Description:** This is the order in which the article will appear in the left navigation of the Docs site.
- **Required?:** Yes, unless page is hidden.
- **Accepts Multiple Values?:** No.
- **Data Type:** `integer`
- **Available Values:** Any number (including multiple decimals) between `1` and `100`. You can use `1.1`, `1.2`, `1.3`, etc. to order pages, as well.

### Page type

- **Key:** `page_type`
- **Description:** Type of page, determined by page templates. Inform formatting and content.
- **Required?:** Yes.
- **Accepts Multiple Values?:** No.
- **Data Type:** `string`
- **Available Values:** See [Page Types](#page-types).

### Platform

- **Key:** `platform`
- **Description:** Notes which platforms (iOS, Android, etc.) the article is associated with.
- **Required?:** No, unless on a Dev Guide page.
- **Accepts Multiple Values?:** Multiple values can be used.
- **Data Type:** `string`
- **Available Values:** Any of the platforms Braze integrates on: `iOS`, `Android`, `Web`, `API`, and any of the wrapper SDKs.
