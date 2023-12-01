---
nav_title: Creating a new page
page_order: 0
noindex: true
---

# Creating a new page

> Learn how to create a new page for Braze Docs. If you're looking to create a new section instead, see [Managing sections](). For general information about pages, see [About our framework]().

{% multi_lang_include contributing/general_getting_started.md %}

## Creating a new branch

THIS.

## Creating a new page

In your text editor, select the `_docs` directory, then open the directory for the relevant [Jekyll collection]().

```plaintext
_docs
├── _api
├── _developer_guide
├── _docs_pages
├── _help
├── _hidden
├── _home
├── _partners
└── _user_guide
```

Find the directory for the section you'd like to add your new page to. For example, to add a new page to the [Getting Started]({{site.baseurl}}developer_guide/platform_wide/getting_started) section in the [Developer Guide]({{site.baseurl}}developer_guide/home), go to:

```plaintext
_docs
├── _api
├── _developer_guide
│   └── platform_wide
│       └── getting_started
├── _docs_pages
├── _help
├── _hidden
├── _home
├── _partners
└── _user_guide
```

{% alert tip %}
URLs on Braze Docs always match the directory structure within the docs repository. Use a page or section's URL to help find your way around.
{% endalert %}

Next, create a new Markdown file for your page.

```plaintext
PAGE_TITLE.md
```

Replace `PAGE_TITLE` with the title of your page (be sure it adheres to the [Headings and Titles](https://docs.google.com/document/u/2/d/e/2PACX-1vTluyDFO3ZEV7V6VvhXE4As_hSFwmnFFdU9g6_TrAYTgH1QmbRoEDDdn5GzKAB9vdBbIdyiFdoaJcNk/pub#h.vs0awrl1ba2p) guideline). Use all lowercase characters, remove special characters, and replace spaces with underscores (`_`). Your filename should be similar to the following:

- **Page title:** Setting up your development environment for C++
- **File name:** `setting_up_your_development_environment_for_cpp.md`

If you plan on using the default page layout, use the template below to get started. Otherwise, you can find more specific layouts in [Layouts]().

```markdown
---
nav_title: NAV_TITLE
page_order: ORDER_NUMBER
---

# IN_PAGE_TITLE

> SHORT_DESCRIPTION

## HEADING

CONTENT
```

Replace the following:

- `NAV_TITLE`: THIS
- `ORDER_NUMBER`: THIS
- `IN_PAGE_TITLE`: THIS
- `SHORT_DESCRIPTION`: THIS
- `HEADING`: THIS
- `CONTENT`: THIS

{% alert note %}
For the full list of supported YAML metadata, see [Metadata]().
{% endalert %}

When you're finished 
