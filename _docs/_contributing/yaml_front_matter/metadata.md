---
nav_title: Metadata
article_title: Metadata
description: "These are the metadata keys that can be added to a page's YAML front matter."
page_order: 0
noindex: true
---

#  Metadata

> These are the metadata keys that can be added to a page's YAML front matter. For more general information, see [About content management]({{site.baseurl}}/contributing/content_management/#pages).

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
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

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

The `article_title` key is used to set the page title for online search results and the end-user's browser tab. This key accepts any `string` value. For naming conventions, see the [Braze Docs Style Guide]({{site.baseurl}}/contributing/style_guide/).

{% tabs local %}
{% tab usage example %}
```markdown
---
article_title: Getting started with Braze Docs
---
```
{% endtab %}
{% endtabs %}

### `description`

The `description` key is used to set the page description in online search results. This key accepts any `string` value under 150 characters that's surrounded by double quotes.

{% tabs local %}
{% tab usage example %}
```markdown
---
description: "If you're new to Braze Docs, start with this step-by-step tutorial."
---
```
{% endtab %}
{% endtabs %}

### `nav_title`

The `nav_title` key is used to set the page title on the left-side navigation bar on Braze Docs. This key accepts any `string` less than 30 characters. If the [`hidden`](#hide-page-from-navigation) key is set to `true`, `nav_title` is not required.

{% tabs local %}
{% tab usage example %}
```markdown
---
nav_title: Getting started
---
```
{% endtab %}
{% endtabs %}

## Optional keys

### `alias`

The `alias` key is used to create an alternate URL path for a page. This is useful for providing a simpler static link that remains valid even if a file is moved or renamed. Unlike a [redirect]({{site.baseurl}}/contributing/content_management/redirecting_urls), the alias path loads the page directly without appending `?redirect` to the URL, which makes page loading faster.

In the following example, visiting `www.braze.com/docs/brazeai/liquid` will point to the real page path instead: `www.braze.com/docs/user_guide/brazeai/generative_ai/liquid`.

{% tabs local %}
{% tab usage example %}
```markdown
---
nav_title: Liquid Code
article_title: Generating Liquid code with BrazeAI
description: "Learn about the AI Liquid Assistant and how you can use it to generate Liquid snippets for your messaging."
alias: "/brazeai/liquid"
---
```
{% endtab %}
{% endtabs %}

{% alert important %}
Because the `alias` key must be unique across all URLs, it should only be used sparingly so it doesn't conflict with any existing or future URLs.
{% endalert %}

### `channel`

The `channel` key is used to set a page's related messaging channels. This key accepts one or more of the following `string` values as a list.

- `content cards`
- `email`
- `in-app messages`
- `news feed`
- `push`
- `sms`
- `webhooks`

{% tabs local %}
{% tab usage example %}
```markdown
---
channel:
  - email
  - news feed
---
```
{% endtab %}
{% endtabs %}

### `config_only`

The `config_only` key is used to hide a page's content without hiding it on left-side navigation bar. Use this key when [creating a section without a landing page]({{site.baseurl}}/contributing/content_management/sections?tab=without%20landing%20page#step-2-configure-your-section). This key accepts the boolean values `true` or `false`.

{% tabs local %}
{% tab usage example %}
```markdown
---
config_only: true
---
```
{% endtab %}
{% endtabs %}

### `hidden`

The `hidden` key is used to hide a page from the left-side navigation on Braze Docs. This key accepts the boolean values `true` or `false`.

{% tabs local %}
{% tab usage example %}
```markdown
---
hidden: true
---
```
{% endtab %}
{% endtabs %}

### `hide_toc`

The `hide_toc` key is used to hide the in-page table of contents (TOC) on the right side of the page. This key accepts the boolean values `true` or `false`.

{% tabs local %}
{% tab usage example %}
```markdown
---
hide_toc: true
---
```
{% endtab %}
{% endtabs %}

### `layout`

The `layout` key is used to set the layout for a page. If `layout` is not set, the `default` layout will be used. This key accepts any of the following `string` values. For a description and example of each layout, see [Page layouts]({{site.baseurl}}/contributing/yaml_front_matter/page_layouts/).

- `api_page`
- `dev_guide`
- `featured_video`
- `featured`
- `glossary_page`
- `blank_config`
- `redirect`

{% tabs local %}
{% tab usage example %}
```markdown
---
page_layout: glossary_page
---
```
{% endtab %}
{% endtabs %}

### `noindex`

The `noindex` key is used to hide a page from internal and external search results (such as Braze Docs and Google Search). This key accepts the boolean values `true` or `false`.

{% tabs local %}
{% tab usage example %}
```markdown
---
noindex: true
---
```
{% endtab %}
{% endtabs %}

### `page_order`

The `page_order` key is used to [order sections]({{site.baseurl}}/contributing/content_management/sections/#ordering-a-section) on the left-side navigation bar. This key accepts any non-negative number (such as `0`, `20`, or `5.5`).

{% tabs local %}
{% tab usage example %}
```markdown
---
page_order: 35.6
---
```
{% endtab %}
{% endtabs %}

### `page_type`

The `page_type` key is used to set formatting of a page. This key accepts any of the following `string` values.

- `glossary`
- `solution`
- `reference`
- `tutorial`
- `landing`
- `partner`
- `update`

For more information about each value, see [Page types]({{site.baseurl}}/contributing/yaml_front_matter/page_layouts/).

{% tabs local %}
{% tab usage example %}
```markdown
---
page_type: tutorial
---
```
{% endtab %}
{% endtabs %}

### `permalink`

The `permalink` key is used with the [`hidden`](#hide-page-from-navigation) key to override the default URL for a page on Braze Docs. The value assigned to `permalink` will be prepended with `https://www.braze.com/docs` before redirecting. This key accepts any `string` value meeting the following requirements.

- Characters are lowercase
- Words are separated by underscores (`_`)
- "Directories" are separated by forward slashes (`/`)
- All other special characters are removed

{% tabs local %}
{% tab usage example %}
```markdown
---
hidden: true
permalink: /support_contact/docs_team/
---
```
{% endtab %}
{% endtabs %}

### `platform`

The `platform` key is used to set the page's related platforms. This key accepts one or more [Braze SDKs]({{site.baseurl}}/developer_guide/home/) as a `string` value in a list.

{% tabs local %}
{% tab usage example %}
```markdown
---
platform:
  - iOS
  - Web
  - Android
---
```
{% endtab %}
{% endtabs %}

### `toc_headers`

By default, the table of contents (TOC) displays all heading levels. To show only specific heading levels, use the `toc_headers` key to explicitly list the desired levels. Any heading levels not listed will be hidden from the TOC.

This key accepts the following string values:

- `h1`
- `h2`
- `h3`
- `h4`

{% tabs local %}
{% tab usage example %}
```markdown
---
toc_headers: h2
---
```
{% endtab %}
{% endtabs %}

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

{% tabs local %}
{% tab usage example %}
```markdown
---
tool:
  - currents
  - segments
---
```
{% endtab %}
{% endtabs %}
