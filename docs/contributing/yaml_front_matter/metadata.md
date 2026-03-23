
#  Metadata

> These are the metadata keys that can be added to a page's YAML front matter. For more general information, see [About content management](../content_management.md#pages).

## Applying metadata

To apply metadata to your page, add Jekyll's front matter syntax to the beginning of your Markdown file.

```markdown
---
METADATA_KEY: METADATA_VALUE
---
```

Replace the following:

| Placeholder      | Description                                                                                                               |
|------------------|---------------------------------------------------------------------------------------------------------------------------|
| `METADATA_KEY`   | The key representing a supported metadata type. Replace with a [metadata key](#required-keys) from the following section. |
| `METADATA_VALUE` | The value assigned to the metadata key. Check a metadata key's supported values in the following section.                 |


Your page should be similar to the following:

```markdown
---
nav_title: Getting started
article_title: Getting started with Braze Docs
description: "If you're new to Braze Docs, start with this step-by-step tutorial."
---

# Getting started with Braze Docs

If you're new to Braze Docs or docs-as-code, start with our tutorial.
```

## Required keys

### `article_title`

The `article_title` key is used to set the page title for online search results and the end-user's browser tab. This key accepts any `string` value. For naming conventions, see the [Braze Docs Style Guide](../style_guide.md).

### usage example

```markdown
---
article_title: Getting started with Braze Docs
---
```



### `description`

The `description` key is used to set the page description in online search results. This key accepts any `string` value under 150 characters that's surrounded by double quotes.

### usage example

```markdown
---
description: "If you're new to Braze Docs, start with this step-by-step tutorial."
---
```



### `nav_title`

The `nav_title` key is used to set the page title on the left-side navigation bar on Braze Docs. This key accepts any `string` less than 30 characters. If the [`hidden`](#hide-page-from-navigation) key is set to `true`, `nav_title` is not required.

### usage example

```markdown
---
nav_title: Getting started
---
```



## Optional keys

### `alias`

The `alias` key is used to create an alternate URL path for a page. This is useful for providing a simpler static link that remains valid even if a file is moved or renamed. Unlike a [redirect](../content_management/redirecting_urls.md), the alias path loads the page directly without appending `?redirect` to the URL, which makes page loading faster.

In the following example, visiting `www.braze.com/docs/brazeai/liquid` will point to the real page path instead: `www.braze.com/docs/user_guide/brazeai/generative_ai/liquid`.

### usage example

```markdown
---
nav_title: Liquid Code
article_title: Generating Liquid code with BrazeAI
description: "Learn about the AI Liquid Assistant and how you can use it to generate Liquid snippets for your messaging."
alias: "/brazeai/liquid"
---
```



> **Important:**
> Because the `alias` key must be unique across all URLs, it should only be used sparingly so it doesn't conflict with any existing or future URLs.



### `channel`

The `channel` key is used to set a page's related messaging channels. This key accepts one or more of the following `string` values as a list.

- `content cards`
- `email`
- `in-app messages`
- `news feed`
- `push`
- `sms`
- `webhooks`

### usage example

```markdown
---
channel:
  - email
  - news feed
---
```



### `config_only`

The `config_only` key is used to hide a page's content without hiding it on left-side navigation bar. Use this key when [creating a section without a landing page](../content_management/sections.md#step-2-configure-your-section). This key accepts the boolean values `true` or `false`.

### usage example

```markdown
---
config_only: true
---
```



### `hidden`

The `hidden` key is used to hide a page from the left-side navigation on Braze Docs. This key accepts the boolean values `true` or `false`.

### usage example

```markdown
---
hidden: true
---
```



### `hide_toc`

The `hide_toc` key is used to hide the in-page table of contents (TOC) on the right side of the page. This key accepts the boolean values `true` or `false`.

### usage example

```markdown
---
hide_toc: true
---
```



### `layout`

The `layout` key is used to set the layout for a page. If `layout` is not set, the `default` layout will be used. This key accepts any of the following `string` values. For a description and example of each layout, see [Page layouts](page_layouts.md).

- `api_page`
- `dev_guide`
- `featured_video`
- `featured`
- `glossary_page`
- `blank_config`
- `redirect`

### usage example

```markdown
---
page_layout: glossary_page
---
```



### `noindex`

The `noindex` key is used to hide a page from internal and external search results (such as Braze Docs and Google Search). This key accepts the boolean values `true` or `false`.

### usage example

```markdown
---
noindex: true
---
```



### `page_order`

The `page_order` key is used to [order sections](../content_management/sections.md#ordering-a-section) on the left-side navigation bar. This key accepts any non-negative number (such as `0`, `20`, or `5.5`).

### usage example

```markdown
---
page_order: 35.6
---
```



### `page_type`

The `page_type` key is used to set formatting of a page. This key accepts any of the following `string` values.

- `glossary`
- `solution`
- `reference`
- `tutorial`
- `landing`
- `partner`
- `update`

For more information about each value, see [Page types](page_layouts.md).

### usage example

```markdown
---
page_type: tutorial
---
```



### `permalink`

The `permalink` key is used with the [`hidden`](#hide-page-from-navigation) key to override the default URL for a page on Braze Docs. The value assigned to `permalink` will be prepended with `https://www.braze.com/docs` before redirecting. This key accepts any `string` value meeting the following requirements.

- Characters are lowercase
- Words are separated by underscores (`_`)
- "Directories" are separated by forward slashes (`/`)
- All other special characters are removed

### usage example

```markdown
---
hidden: true
permalink: /support_contact/docs_team/
---
```



### `platform`

The `platform` key is used to set the page's related platforms. This key accepts one or more [Braze SDKs](https://www.braze.com/docs/developer_guide/home/) as a `string` value in a list.

### usage example

```markdown
---
platform:
  - iOS
  - Web
  - Android
---
```



### `toc_headers`

By default, the table of contents (TOC) displays all heading levels. To show only specific heading levels, use the `toc_headers` key to explicitly list the desired levels. Any heading levels not listed will be hidden from the TOC.

This key accepts the following string values:

- `h1`
- `h2`
- `h3`
- `h4`

### usage example

```markdown
---
toc_headers: h2
---
```



### `tool`

The `tool` key is used to set the page's related engagement tools. This key accepts one or more of the following `string` values as a list.

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

### usage example

```markdown
---
tool:
  - currents
  - segments
---
```


