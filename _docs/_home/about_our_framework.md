---
nav_title: About our framework
page_order: 3
noindex: true
---

# About our framework

> Learn about the various components that make up the Braze Docs framework.

## Managing the docs

Braze Docs is managed using docs-as-code, a method for managing documentation that mirrors the software development lifecycle by using a version control system. Braze Docs uses the Git version control system, which allows contributors to work on the same piece of documentation without overwriting each other's work. For more information, see [About version control and Git](https://docs.github.com/en/get-started/using-git/about-git#about-version-control-and-git).

![The Braze Docs repository's home page on GitHub.]()

## Building the site

Braze Docs is built using Jekyll, a popular Static-Site Generator (SSG) that allows content files and design files to be stored in separate directories, such as `_docs` for content files and `assets` for design files. When the site is built, Jekyll intelligently merges each file and stores them as XML and HTML data in the `_site` directory. For more information, see [Jekyll Directory Structure](https://jekyllrb.com/docs/structure/).

![The home page for Braze Docs.]()

## Pages

Each page on Braze Docs is written in Markdown syntax and stored as a Markdown file using the `.md` file extension. At the top of each Markdown file, YAML front matter is used to add hidden metadata for each page.

```markdown
---
METADATA_KEY: METADATA_VALUE
---

# CONTENT
```

Replace the following:

| Placeholder      | Description                                                                             |
|------------------|-----------------------------------------------------------------------------------------|
| `METADATA_KEY`   | The key representing a supported metadata type. For more information, see [Metadata](). |
| `METADATA_VALUE` | The value assigned to the metadata type's key. For more information, see [Metadata]().  |
| `CONTENT`        | The page's content written in Markdown syntax.                                          |

_Example input:_

```markdown
---
nav_title: Getting started
layout: default
page_order: 5
---

# Getting started with Braze

Learn how you can get started with Braze.

## Step 1: Create an account
```

_Example output:_

![]()

{% alert note %}
For a full walkthrough, see [Managing pages]().
{% endalert %}

## Images

> TODO: add overview for images.

{% alert note %}
For a full walkthrough, see [Managing images]().
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

_Example input:_

```markdown
# Getting started with Braze

Learn how you can get started with Braze.

{% raw %}{% multi_lang_include braze/upgrade_notice.md %}{% endraw %}
```

_Example output:_

![]()

{% alert note %}
For a full walkthrough, see [Reusing content]().
{% endalert %}

## Layouts

By default, Jekyll uses the `default.html` layout in the `_layouts` directory to build each page on Braze Docs. However, different layouts can be used by assigning the layout to the `layout:` key in the YAML front matter.

```markdown
---
layout: LAYOUT_VALUE
---
```

Replace `LAYOUT_VALUE` with the name of the layout file and the file extension removed.

_Example file tree:_

```plaintext
braze-docs
├── _build
├── _config.yml
├── _data
├── _docs
├── _includes
│   └── api_glossary.html
├── _lang
├── _layouts
├── _plugins
├── _site
├── assets
├── config
├── public
├── scripts
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE
└── README.md
```

_Example input:_

```markdown
---
layout: api_glossary
---
```

_Example output:_

![]()

{% alert note %}
For more information, see [Layouts]().
{% endalert %}

## Sections

Braze Docs is organized into [primary sections]() and [subsections](). Choose a section to learn more.

{% alert note %}
For a full walkthrough, see [Managing sections]().
{% endalert %}

### Primary sections

The primary sections on Braze Docs are:

- [Braze Docs Home](https://www.braze.com/docs)
- [User Guide](https://www.braze.com/docs/user_guide/introduction)
- [Developer Guide](https://www.braze.com/docs/developer_guide/home)
- [Braze API Guide](https://www.braze.com/docs/api/home)
- [Technology Partners](https://www.braze.com/docs/partners/home)
- [Braze Help](https://www.braze.com/docs/help/home)

These primary sections can be accessed on the site header from any page on Braze Docs.

![]()

Each primary section is built using [Jekyll collections](https://jekyllrb.com/docs/collections/), which allows related content to be grouped together for easy management. Keep in mind, while all primary sections are collections, not all collections are primary sections. You can find the full list of Braze Docs collections in the Jekyll configuration file, `_config.yml`:

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
    ├── _developer_guide
    ├── _docs_pages
    ├── _help
    ├── _hidden
    ├── _home
    ├── _partners
    └── _user_guide
```

The landing page for each primary section is a standard Markdown file with the `page_order:` key set to `0`.

_Example input:_

```markdown
---
page_order: 0
layout: dev_guide
guide_top_header: "Braze Developer Guide"
guide_top_text: "This is where developers can find all the integrations available with Braze.<br>For additional resources and to join the Braze developer community, visit the <a href='https://www.braze.com/dev-portal'>Braze developer portal</a>."
article_title: Braze Developer Guide
description: "This landing page is where developers can find all the integrations available with Braze."
---
```

_Example output:_

![]()

### Subsections

All primary sections on Braze Docs contain one or more subsection, each representing an expandable item on the left-side navigation.

![]()

Unlike primary sections, subsections can be configured with or _without_ a landing page. Subsections without landing pages are helpful for organizing related content together while minimizing the number of non-useful pages in Braze Docs. Whether a subsection is configured with or without a landing page, all subsections represent both a directory _and_ Markdown file in the repository. See the following example:

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

In the `_primary_section` directory, `subsection_a` is **not** configured with a landing page, while `subsection_b` is configured with a landing page. In the following example, `subsection_a.md` has `config_only:` set to `true`, which prevents this page from being rendered as a landing page:

_Example input:_

```markdown
---
nav_title: Subsection A
page_order: 0
config_only: true
---
```

_Example output:_

![]()

However, `subsection_b.md` doesn't use the `config_only:` key, so this page _is_ rendered as a landing page:

_Example input:_

```markdown
---
nav_title: Subsection B
page_order: 0
---
```

_Example output:_

![]()

{% alert note %}
While a subsection with `config_only:` set to `true` is not rendered as a page, the subsection's directory name is still used in the URLs for pages in that subsection. For more information, see [URLs]().
{% endalert %}

## URLs

URLs on Braze Docs always match the directory structure within the docs repository. 

_Example file tree:_

```plaintext
braze-docs
└── _docs
    └── _primary_section
        └── subsection_a
            └── page_a.md
```

_Example URL:_

```plaintext
https://www.braze.com/docs/primary_section/subsection_a/page_a
```

This includes URLs for pages located in a [subsection]() with `config_only:` set to `true`. Even though `config_only` subsections aren't rendered as pages, the subsection's directory name is still used in the URLs for pages in that directory. See the following example:

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

The URLs for `subsection_a/page_a.md` and `subsection_a/page_b.md` will contain `subsection_a` even though `subsection_a.md` is not configured as a landing page.

_Example `subsection_a.md`:_

```markdown
---
nav_title: Subsection A
page_order: 0
config_only: true
---
```

_Example URLs for Subsection A:_

```plaintext
https://www.braze.com/docs/primary_section/subsection_a/page_a
https://www.braze.com/docs/primary_section/subsection_a/page_b
```

While this is similar for `subsection_b`, in addition to `subsection_b/page_a.md` and `subsection_b/page_b.md` receiving unique URLS, `subsection_b.md` also receives a unique URL since it's configured as a landing page.

_Example `subsection_b.md`:_

```markdown
---
nav_title: Subsection B
page_order: 0
---
```

_Example URLs for Subsection B:_

```plaintext
https://www.braze.com/docs/primary_section/subsection_b
https://www.braze.com/docs/primary_section/subsection_b/page_a
https://www.braze.com/docs/primary_section/subsection_b/page_b
```
