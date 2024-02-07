---
nav_title: Pages
article: Pages
description: "Learn how to create, modify, and remove pages on Braze Docs."
page_order: 0
noindex: true
---

# Pages

> Learn how to create, modify, and remove pages on Braze Docs. To create or reorder a section instead, see [Sections]({{site.baseurl}}/contributing/content_management/sections/). For general information about pages, see [Content Management]({{site.baseurl}}/contributing/content_management/#pages).

{% multi_lang_include contributing/prerequisites.md %}

## Creating a page

### Step 1: Create a new file

Open the directory you'd like to add a new page to.

![A text editor with the file tree open.]()

{% alert tip %}
The repository file tree mirrors the Braze Docs site URL. For example, the [Catalogs]({{site.baseurl}}/api/endpoints/catalogs/) page in the API guide is located here: `_api/endpoints/catalogs/`.
{% endalert %}

Create a new Markdown file for your page.

```bash
PAGE_TITLE.md
```

Replace `PAGE_TITLE` with the title of your page, which should follow the [Braze Docs Style Guide]({{site.baseurl}}/contributing/style_guide/). Use all lowercase characters, remove special characters, and replace spaces with underscores (`_`). Your filename should be similar to the following:

- **Page title:** Setting up your development environment for C++
- **File name:** `setting_up_your_development_environment_for_cpp.md`

### Step 2: Add a layout

To use the default page layout, copy and paste the following into your Markdown file. For other layouts, see [Layouts]({{site.baseurl}}/contributing/yaml_front_matter/page_layouts/).

```markdown
---
nav_title: NAV_TITLE
article_title: ARTICLE_TITLE
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
| `NAV_TITLE`         | The title of your page as it will appear on the left-side navigation bar. In almost all cases, `nav_title` should exactly match `article_title`.                                 |
| `ARTICLE_TITLE`     | The title of your page. The `ARTICLE_TITLE` value in the metadata is used for search engine results, while the `ARTICLE_TITLE` value in Heading 1 is used for the title rendered on the page.                                               |
| `SHORT_DESCRIPTION` | A short, 1-2 sentence description of your page. The `SHORT_DESCRIPTION` value in YAML the metadata is used for search engine results, while the `SHORT_DESCRIPTION` value after Heading 1 is used for the description rendered on the page. |
| `HEADING`           | The title of your Heading 2 section.                                                                                                                                                                                                        |
| `CONTENT`           | The body paragraph for your Heading 2 section.                                                                                                                                                                                              |
{: .reset-td-br-1 .reset-td-br-2}

{% alert tip %}
This template is only to get you started&#8212;add [additional metadata]({{site.baseurl}}/contributing/yaml_front_matter/metadata/) and headings as needed.
{% endalert %}

## Writing content

Other than the Braze-specific syntax shown in this section, all content be written using [standard Markdown syntax](https://www.markdownguide.org/basic-syntax/).

### Cross-referencing

To reference a page hosted outside Braze Docs, use standard Markdown syntax.

{% raw %}
```markdown
[LINK_TEXT](FULL_URL)
```
{% endraw %}

To cross-reference a page hosted on Braze Docs, use the following Braze-specific syntax.

{% raw %}
```markdown
[LINK_TEXT]({{site.baseurl}}/SHORT_URL)
```
{% endraw %}

{% alert note %}
For a full walkthrough, see [Cross-referencing]({{site.baseurl}}/contributing/content_management/cross_referencing/).
{% endalert %}

### Adding images

To add images, place the image's PNG file inside the relevant location within `assets/img`, then use the following syntax:

{% raw %}
```markdown
![ALT_TEXT.]({% image_buster /assets/img/DIRECTORY/IMAGE.png %})
```
{% endraw %}

{% alert note %}
For a full walkthrough, see [Adding a new image]({{site.baseurl}}/contributing/content_management/images/).
{% endalert %}
