---
nav_title: Metadata 
page_order: 0
noindex: true
---

#  Metadata

> The following metadata keys can be added to a page's YAML front matter. For more general information, see [About our framework]({{site.baseurl}}/home/about_our_framework/#pages).

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
| `METADATA_KEY`   | The key representing a supported metadata type. Replace with a [metadata key](#required-keys) from the following section. |
| `METADATA_VALUE` | The value assigned to the metadata key. Check a metadata key's supported values in the following section.                 |
{: .reset-td-br-1 .reset-td-br-2}

## Required keys

### Article title

The `article_title` key is used to set the page title for online search results and the end-user's browser tab. This key accepts any `string` value. For style guidelines, see [Naming Conventions](https://docs.google.com/document/u/2/d/e/2PACX-1vTluyDFO3ZEV7V6VvhXE4As_hSFwmnFFdU9g6_TrAYTgH1QmbRoEDDdn5GzKAB9vdBbIdyiFdoaJcNk/pub#h.n0sf2nl43bpo).

**Usage example:**

```markdown
---
article_title: Getting started with Braze Docs
---
```

### Description

The `description` key is used to set the page description in online search results. This key accepts any `string` value under 150 characters that's surrounded by double quotes.

**Usage example:**

```markdown
---
description: "If you're new to Braze Docs, start with this step-by-step tutorial."
---
```

### Navigation title

The `nav_title` key is used to set the page title on the left-side navigation bar on Braze Docs. This key accepts any `string` less than 30 characters. If the [`hidden`](#hide-page) key is set to `true`, `nav_title` is not required.

**Usage example:**

```markdown
---
nav_title: Getting started
---
```

## Optional keys

### Engagement tool

The `tool` key is used to set the page's related engagement tool(s). This key accepts one or more of the following `string` values as a list:

- `dashboard`
- `docs`
- `canvas`
- `campaigns`
- `currents`
- `location`
- `media`
- `reports`
- `segments`
- `templates`

**Usage example:**

```markdown
---
tool:
  - currents
  - segments
---
```

### Hide from navigation {#hide-page}

The `hidden` key is used to hide a page from the left-side navigation on Braze Docs. This key accepts the boolean values `true` or `false`.

**Usage example:**

```markdown
---
hidden: true
---
```

### Hide from search

The `noindex` key is used to hide a page from internal and external search results (such as Braze Docs and Google Search). This key accepts the boolean values `true` or `false`.

**Usage example:**

```markdown
---
noindex: true
---
```

### Hide table of contents

The `hide_toc` key is used to hide the in-page Table of Contents (toc) on the right side of the page. This key accepts the boolean values `true` or `false`.

**Usage example:**

```markdown
---
hide_toc: true
---
```

### Messaging channel

The `channel` key is used to set a page's related messaging channel(s). This key accepts one or more of the following `string` values as a list:

- `content cards`
- `email`
- `in-app messages`
- `news feed`
- `push`
- `sms`
- `webhooks`

**Usage example:**

```markdown
---
channel:
  - email
  - news feed
---
```

### Navigation only

The `config_only` key is used to hide a page's content without hiding it on left-side navigation bar. Use this key when [creating a section without a landing page]({{site.baseurl}}/home/content_management/sections/?tab=without%20landing%20page#creating-a-section). This key accepts the boolean values `true` or `false`.

**Usage example:**

```markdown
---
config_only: true
---
```

### Override default URL

The `permalink` key is used with the [`hidden`](#hide-from-navigation) key to override the default URL for a page on Braze Docs. The value assigned to `permalink` will be prepended with `https://www.braze.com/docs` before redirecting. This key accepts any `string` value meeting the following requirements:

- Characters are lowercase
- Words are separated by underscores (`_`)
- "Directories" are separated by backslashes (`/`)
- All other special characters are removed

**Usage example:**

```markdown
---
hidden: true
permalink: /support_contact/docs_team/
---
```

### Page layout

The `layout` key is used to set the layout for a page. If `layout` is not set, the `default` layout will be used. This key accepts any of the following `string` values:

- `api_page`
- `dev_guide`
- `featured_video`
- `featured`
- `glossary_page`
- `blank_config`
- `redirect`

For more information about each value, see [Page layouts]({{site.baseurl}}/home/yaml_front_matter/page_layouts/).

**Usage example:**

```markdown
---
page_layout: glossary_page
---
```

### Page order

The `page_order` key is used to [order sections]({{site.baseurl}}/home/content_management/sections/#ordering-a-section) on the left-side navigation bar. This key accepts any non-negative number (such as `0`, `20`, or `5.5`).

**Usage example:**

```markdown
---
page_order: 35.6
---
```

### Page type

The `page_type` key is used to set formatting of a page. This key accepts any of the following `string` values:

- `glossary`
- `solution`
- `reference`
- `tutorial`
- `landing`
- `partner`
- `update`

For more information about each value, see [Page types]({{site.baseurl}}/home/yaml_front_matter/page_types/).

**Usage example:**

```markdown
---
page_type: tutorial
---
```

### Platform

The `platform` key is used to set the page's related platform(s). This key accepts one or more [Braze SDKs]({{site.baseurl}}/developer_guide/home/) as a `string` value in a list.

**Usage example:**

```markdown
---
platform:
  - iOS
  - Web
  - Android
---
```
