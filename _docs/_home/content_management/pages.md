---
nav_title: Pages
page_order: 0
noindex: true
---

# Pages

> Learn how to create, modify, and remove pages on Braze Docs. If you'd like to create a new section instead, see [Sections](../../../_docs/_home/content_management/managing_sections.md). For general information about pages, see [About our framework](../../../_docs/_home/about_our_framework.md#pages).

{% multi_lang_include contributing/prerequisites.md %}

## Creating a page

### Step 1: Create a new file

First, [create a new branch](../../../_docs/_home/github/creating_a_new_branch.md), then open the directory you'd like to add a new page to.

![A text editor with the file tree open.]()

{% alert tip %}
The repository file tree mirrors the Braze Docs site URL. For example, the [Catalogs]({{site.baseurl}}/api/endpoints/catalogs/) page in the API guide is located here: `_api/endpoints/catalogs/`.
{% endalert %}

Create a new Markdown file for your page.

```bash
PAGE_TITLE.md
```

Replace `PAGE_TITLE` with the title of your page (be sure it adheres to the [Headings and Titles](https://docs.google.com/document/u/2/d/e/2PACX-1vTluyDFO3ZEV7V6VvhXE4As_hSFwmnFFdU9g6_TrAYTgH1QmbRoEDDdn5GzKAB9vdBbIdyiFdoaJcNk/pub#h.vs0awrl1ba2p) guideline). Use all lowercase characters, remove special characters, and replace spaces with underscores (`_`). Your filename should be similar to the following:

- **Page title:** Setting up your development environment for C++
- **File name:** `setting_up_your_development_environment_for_cpp.md`

### Step 2: Add a layout

To use the default page layout, copy and paste the following into your Markdown file. For other layouts, see [Layouts](../../../_docs/_home/examples/layouts.md).

```markdown
---
nav_title: NAV_TITLE
article_tite: ARTICLE_TITLE
description: SHORT_DESCRIPTION
---

# ARTICLE_TITLE

> SHORT_DESCRIPTION

## HEADING

CONTENT
```

Replace the following:

| Placeholder         | Description                                                                                                                                                                                                                                 |
|---------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `NAV_TITLE`         | The title of your page as it will appear on the left-side navigation bar. In most cases, `nav_title` should match `article_title`, however to save space, you may use a shorter _but still similar_ title.                                  |
| `ARTICLE_TITLE`     | The title of your page. The `ARTICLE_TITLE` value in the metadata is used for search engine results, while the `ARTICLE_TITLE` value in Heading 1 is used for the title rendered on the page.                                               |
| `SHORT_DESCRIPTION` | A short, 1-2 sentence description of your page. The `SHORT_DESCRIPTION` value in YAML the metadata is used for search engine results, while the `SHORT_DESCRIPTION` value after Heading 1 is used for the description rendered on the page. |
| `HEADING`           | The title of your Heading 2 section.                                                                                                                                                                                                        |
| `CONTENT`           | The body paragraph for your Heading 2 section.                                                                                                                                                                                              |

You may add additional metadata and headings as needed, this template is just to get you started. For the full list of supported YAML metadata, see [Metadata](../../../_docs/_home/metadata.md).

When you're ready to add content to your new page, continue to [Modifying a page](#modifying-a-page).

## Modifying a page

Other than the Braze-specific syntax covered in this section, all page content should use [standard Markdown syntax](https://www.markdownguide.org/basic-syntax/). {% multi_lang_include contributing/minis/creating_a_pull_request.md %}

{% multi_lang_include contributing/minis/cross_referencing.md %}

{% multi_lang_include contributing/minis/adding_images.md %}

