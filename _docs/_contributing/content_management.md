---
nav_title: Manage content
article_title: Manage Content
description: "This is an overview of how content is managed on Braze Docs."
page_order: 2 
noindex: true
---

# About content management

> This is an overview for how content is managed on Braze Docs. To learn more about a specific topic, choose the dedicated topic page in the navigation.

## Methodology

Braze Docs is managed using docs-as-code, a method for managing documentation that mirrors the software development lifecycle by using a version control system. Braze Docs uses the Git version control system, which allows contributors to work on the same piece of documentation without overwriting each other's work. For more information, view [About version control and Git](https://docs.github.com/en/get-started/using-git/about-git#about-version-control-and-git).

![The Braze Docs repository's home page on GitHub.]({% image_buster /assets/img/contributing/github/home_page.png %})

## Site generator 

Braze Docs is built using Jekyll, a popular static-site generator that allows content files and design files to be stored in separate directories, such as `_docs` for content files and `assets` for design files. When the site is built, Jekyll intelligently merges each file and stores them as XML and HTML data in the `_site` directory. For more information, see [Jekyll Directory Structure](https://jekyllrb.com/docs/structure/).

![The home page for Braze Docs.]({% image_buster /assets/img/contributing/styling_examples/home.png %})

As a contributor, you'll primarily work within the following directories.

| Directory                                                                     | Description                                                                                                                                                                                                                                                                                                                       |
|-------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [`_docs`](https://github.com/braze-inc/braze-docs/tree/develop/_docs)         | Contains all the written content for Braze Docs as text files written in Markdown. Text files are organized into directories and subdirectories mirroring the docs site, such as `_api` for the [API section]({{site.baseurl}}/api/home) and `user_guide` for the [User Guide section]({{site.baseurl}}/user_guide/introduction). |
| [`_includes`](https://github.com/braze-inc/braze-docs/tree/develop/_includes) | Contains text files (called "includes") that can be reused in any file within the `_docs` directory. Typically, includes are short, modular pieces of content that don't use standard formatting. The files stored in this location are important for [content reuse](#content-reuse).                                            |
| [`assets`](https://github.com/braze-inc/braze-docs/tree/develop/assets)       | Contains all the images for Braze Docs. Any text file in the `_docs` or `_includes` directory can link to this directory to display an image on its page.                                                                                                                                                                         |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
For a full walkthrough, see [Generating a preview]({{site.baseurl}}/contributing/generating_a_preview/).
{% endalert %}

## Pages

Each page on Braze Docs is written in Markdown syntax and stored as a Markdown file using the `.md` file extension. At the top of each Markdown file, YAML front matter is used to add hidden metadata for each page.

```markdown
---
METADATA_KEY: METADATA_VALUE
---

# CONTENT
```

Replace the following.

| Placeholder      | Description                                                                                                                              |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| `METADATA_KEY`   | The key representing a supported metadata type. For more information, see [Metadata]({{site.baseurl}}/contributing/yaml_front_matter/metadata/). |
| `METADATA_VALUE` | The value assigned to the metadata type's key. For more information, see [Metadata]({{site.baseurl}}/contributing/yaml_front_matter/metadata/).  |
| `CONTENT`        | The page's content written in Markdown syntax.                                                                                           |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% tabs local %}
{% tab example input %}
```markdown
---
nav_title: Contributing to Braze Docs
article_title: Contributing to Braze Docs
description: "Here's what you need to start contributing to Braze Docs!"
page_order: 0
search_tag: Contributing
---

# Contributing to Braze Docs

> Thanks for contributing to Braze Docs! Every Tuesday and Thursday, we merge community contributions and deploy them to Braze Docs. Use this guide to get your changes merged during our next deployment.
```
{% endtab %}

{% tab example output %}
![Example page on Braze Docs.]({% image_buster /assets/img/contributing/styling_examples/page.png %})
{% endtab %}
{% endtabs %}

{% alert tip %}
For a full walkthrough, see [Creating a page]({{site.baseurl}}/contributing/content_management/pages/#creating-a-page).
{% endalert %}

## Images

Images are stored as PNG files inside `assets/img`. The structure of the `img` directory does not need to match the structure of Braze Docs; however, it's best to group related images together into subdirectories.

Each image can be linked to one or more pages using the following syntax.

{% raw %}
```markdown
![ALT_TEXT.]({% image_buster /assets/img/DIRECTORY/IMAGE.png %})
```
{% endraw %}

Replace the following.

| Placeholder | Description                                                                                                             |
|-------------|-------------------------------------------------------------------------------------------------------------------------|
| `ALT_TEXT`  | The alt text for the image. This is required to make Braze Docs equally accessible for those using screen readers. |
| `IMAGE`     | The relative path to your image starting from the `img` directory.                                                      |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Your in-line image should be similar to the following:

{% raw %}
```markdown
![The form for creating a new pull request on GitHub.]({% image_buster /assets/img/contributing/getting_started/github_pull_request.png %})
```
{% endraw %}

{% alert tip %}
For a full walkthrough, see [Adding a new image]({{site.baseurl}}/contributing/content_management/images/#adding-a-new-image).
{% endalert %}

## Sections

Braze Docs is organized into [primary sections](#primary-sections) and [subsections](#subsections).

### Primary sections

The primary sections on Braze Docs are:

- [Braze Docs Home]({{site.baseurl}})
- [User Guide]({{site.baseurl}}/user_guide/introduction)
- [Developer Guide]({{site.baseurl}}/developer_guide/home)
- [Braze API Guide]({{site.baseurl}}/api/home)
- [Technology Partners]({{site.baseurl}}/partners/home)
- [Braze Help]({{site.baseurl}}/help/home)
- [Contributing to Braze Docs]({{site.baseurl}}/contributing/home/)

Other than **Contributing to Braze Docs**, these primary sections can be accessed on the site header from any page on Braze Docs.

![The primary sections as shown on the site header on Braze Docs.]({% image_buster /assets/img/contributing/styling_examples/header.png %})

Each primary section is built using [Jekyll collections](https://jekyllrb.com/docs/collections/), which allows related content to be grouped together for easy management. Keep in mind, while all primary sections are collections, not all collections are primary sections. You can find the full list of Braze Docs collections in the Jekyll configuration file, `_config.yml`.

```yaml
collections:
  home:
    title: Documentation
    output: true
    default_nav_url: ''
    page_order: 1
  user_guide:
    title: User Guide
    output: true
    default_nav_url: introduction/
    page_order: 2
  developer_guide:
    title: Developer Guide
    output: true
    default_nav_url: home/
    page_order: 3
  api:
    title: API
    output: true
    default_nav_url: home/
    page_order: 4
  partners:
    title: Technology Partners
    output: true
    default_nav_url: home/
    page_order: 5
  help:
    title: Help
    output: true
    default_nav_url: home/
    page_order: 6
  contributing:
    output: true
    default_nav_url: contributing/
  hidden: # Hidden pages not directly linked via navigation
    title: Braze
    output: true
    hidden: true
  docs_pages: # Site specific pages. ie main redirects and search
    title: Braze
    output: true
    hidden: true
```

Each collection listed represents a directory within the `_docs` directory.

```plaintext
braze-docs
└── _docs
    ├── _api
    ├── _contributing
    ├── _developer_guide
    ├── _docs_pages
    ├── _help
    ├── _hidden
    ├── _home
    ├── _partners
    └── _user_guide
```

The landing page for each primary section is a standard Markdown file with the `page_order:` key set to `0`.

{% tabs local %}
{% tab example input %}
```markdown
---
page_order: 0
nav_title: Home
article_title: Braze User Guide
layout: user_guide
user_top_header: "Braze User Guide"
---
```
{% endtab %}

{% tab example output %}
![An example landing page on Braze Docs.]({% image_buster /assets/img/contributing/styling_examples/primary_section.png %})
{% endtab %}
{% endtabs %}

### Subsections

All primary sections on Braze Docs contain one or more subsection, each representing an expandable item on the left-side navigation.

Unlike primary sections, subsections can be configured with or without a landing page. Subsections without landing pages are helpful for organizing related content together while minimizing the number of non-useful pages in Braze Docs. Whether a subsection is configured with or without a landing page, all subsections represent both a directory and Markdown file in the repository. For an example, see the following.

```plaintext
braze-docs
└── _docs
    └── _primary_section
        ├── subsection_a
        │   ├── page_a.md
        │   └── page_b.md
        ├── subsection_b
        │   ├── page_a.md
        │   └── page_b.md
        ├── subsection_a.md # not configured as a landing page
        └── subsection_b.md # configured as a landing page  
```

{% alert tip %}
For a full walkthrough, see [Creating a section]({{site.baseurl}}/contributing/content_management/sections/#creating-a-section).
{% endalert %}

In the `_primary_section` directory, `subsection_a` is not configured with a landing page, while `subsection_b` is configured with a landing page. In the following example, `subsection_a.md` has `config_only:` set to `true`, which prevents this page from being rendered as a landing page.

{% tabs local %}
{% tab example input %}
```markdown
---
nav_title: Subsection A
page_order: 0
config_only: true
---
```
{% endtab %}

{% tab example output %}
![The left-side navigation on Braze Docs, showing an example of an expanded section without a landing page.]({% image_buster /assets/img/contributing/styling_examples/subsection_config_only.png %})
{% endtab %}
{% endtabs %}

However, `subsection_b.md` doesn't use the `config_only:` key, so this page _is_ rendered as a landing page.

{% tabs local %}
{% tab example input %}
```markdown
---
nav_title: Subsection B
page_order: 0
---
```
{% endtab %}

{% tab example output %}
![The left-side navigation on Braze Docs, showing an example of an expanded section with a landing page.]({% image_buster /assets/img/contributing/styling_examples/subsection_landing_page.png %})
{% endtab %}
{% endtabs %}

{% alert note %}
While a subsection with `config_only:` set to `true` is not rendered as a page, the subsection's directory name is still used in the URLs for pages in that subsection. For more information, see [URLs](#urls).
{% endalert %}

## Cross-references

A cross-reference is when one page on Braze Docs links to another page on Braze Docs. Due to certain site requirements, Braze Docs doesn't support [standard Markdown syntax](https://www.markdownguide.org/basic-syntax/) for cross-reference links, so we created one using Liquid.

{% raw %}
```markdown
[LINK_TEXT]({{site.baseurl}}/SHORT_URL)
```
{% endraw %}

Replace the following:

| Placeholder | Description                                        |
|-------------|----------------------------------------------------|
| `LINK_TEXT` | The page title or related action.                  |
| `SHORT_URL` | The page URL with `https://www.braze.com` removed. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Your cross-reference link should be similar to the following:

{% raw %}
```markdown
Before continuing, [create your SSH token]({{site.baseurl}}/dev_guide/auth).
```
{% endraw %}

{% alert tip %}
For a full walkthrough, see [Cross-referencing]({{site.baseurl}}/contributing/content_management/cross_referencing/).
{% endalert %}

## Content reuse

Jekyll offers the ability to reuse written content across the docs using the `include` tag. Includes are located in the `_includes` directory and can be written in Markdown or HTML syntax.

```markdown
{% raw %}{% multi_lang_include RELATIVE_PATH/FILE %}{% endraw %}
```

Replace the following:

| Placeholder     | Description                                                                                                                                                                                                             |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `RELATIVE_PATH` | (Optional) The relative path to the file from the `_includes` directory. This is only needed if you're including a file from a directory inside the `_includes` directory, such as `_includes/braze/upgrade_notice.md`. |
| `FILE`          | The name of the file including the file extension.                                                                                                                                                                      |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% tabs local %}
{% tab example input %}
{% raw %}
```markdown
# Pages

> Learn how to create, modify, and remove pages on Braze Docs.

{% multi_lang_include contributing/prerequisites.md %}
```
{% endraw %}
{% endtab %}

{% tab example output %}
![Content reuse example on Braze Docs.]({% image_buster /assets/img/contributing/styling_examples/includes.png %})
{% endtab %}
{% endtabs %}

{% alert tip %}
For a full walkthrough, see [Reusing content]({{site.baseurl}}/contributing/content_management/reusing_content).
{% endalert %}

## Layouts

By default, Jekyll uses the `default.html` layout in the `_layouts` directory to build each page on Braze Docs. However, different layouts can be used by assigning the layout to the `layout:` key in the YAML front matter.

```markdown
---
layout: LAYOUT_VALUE
---
```

Replace `LAYOUT_VALUE` with the name of the layout file and the file extension removed.

{% tabs local %}
{% tab example input %}
**File tree**

```plaintext
braze-docs
└── _layouts
    └── api_page.html
```

**In-page metadata**

```markdown
---
layout: api_page
---
```
{% endtab %}

{% tab example output %}
![API glossary layout example on Braze Docs.]({% image_buster /assets/img/contributing/styling_examples/layouts/api_page.png %})
{% endtab %}
{% endtabs %}

{% alert tip %}
For more information, see [Page layouts]({{site.baseurl}}/contributing/yaml_front_matter/page_layouts).
{% endalert %}

## URLs

URLs on Braze Docs always match the directory structure within the docs repository. Given the following example file tree, the URL for `page_a.md` would be `https://www.braze.com/docs/primary_section/subsection_a/page_a`.

```plaintext
braze-docs
└── _docs
    └── _primary_section
        └── subsection_a
            └── page_a.md
```

This includes URLs for pages located in a [subsection](#subsections) with `config_only:` set to `true`. Even though `config_only` subsections aren't rendered as pages, the subsection's directory name is still used to generate the URLs for pages in that directory. For an example, see the following.

```plaintext
braze-docs
└── _docs
    └── _primary_section
        ├── subsection_a
        │   ├── page_a.md
        │   └── page_b.md
        ├── subsection_b
        │   ├── page_a.md
        │   └── page_b.md
        ├── subsection_a.md # not configured as a landing page
        └── subsection_b.md # configured as a landing page  
```

{% tabs local %}
{% tab subsection a %}

**Example landing page**

```markdown
---
nav_title: Subsection A
page_order: 1 
config_only: true
---
```

Since `subsection_a.md` is configured as a landing page, only `page_a.md` and `page_b.md` will receive a unique URL. `subsection_b.md` will **not** receive any URL.

**Example URLs**

```plaintext
Subsection A URL: N/A
Page A URL: https://www.braze.com/docs/primary_section/subsection_a/page_a
Page B URL: https://www.braze.com/docs/primary_section/subsection_a/page_b
```
{% endtab %}
{% tab subsection b %}
**Example landing page**

```markdown
---
nav_title: Subsection B
page_order: 2 
---
```

Since `subsection_b.md` is configured as a landing page, `page_a.md`, `page_b.md`, and `subsection_b.md` will receive a unique URL.

**Example URLs**

```plaintext
Subesction B URL: https://www.braze.com/docs/primary_section/subsection_b
Page A URL: https://www.braze.com/docs/primary_section/subsection_b/page_a
Page B URL: https://www.braze.com/docs/primary_section/subsection_b/page_b
```
{% endtab %}
{% endtabs %}
