---
nav_title: Pages
article_title: Managing Pages
description: "Learn how to create, modify, and remove pages on Braze Docs."
page_order: 0
noindex: true
---

# Managing pages

> Learn how to create, modify, and remove pages on Braze Docs. To create or reorder a section instead, see [Sections]({{site.baseurl}}/contributing/content_management/sections/). For general information about pages, see [About content management]({{site.baseurl}}/contributing/content_management/#pages).

{% multi_lang_include contributing/prerequisites.md %}

## Creating a page

### Step 1: Create a new file

Open the relevant directory, then create a new Markdown file for your page.

```bash
PAGE_TITLE.md
```

Replace `PAGE_TITLE` with the title of your page, which should follow the [Braze Docs Style Guide]({{site.baseurl}}/contributing/style_guide/). Use all lowercase characters, remove special characters, and replace spaces with underscores (`_`). Your filename should be similar to the following:

- **Page title:** Setting up your development environment for C++
- **File name:** `setting_up_your_development_environment_for_cpp.md`

{% multi_lang_include contributing/alerts/tip_locating_a_file.md %}

### Step 2: Add a template

Copy and paste one of the following templates into your Markdown file, and then customize it. For more information, see [Templates]({{site.baseurl}}/contributing/content_types/).

{% tabs local %}
{% tab Basic template %}

{% multi_lang_include contributing/templates/basic.md %}
{% endtab %}

{% tab Technology partner template %}
{% multi_lang_include contributing/templates/technology_partner.md %}
{% endtab %}
{% endtabs %}

![Diagram showing the components of a page, such as breadcrumbs, article title, description, and table of contents.]({% image_buster /assets/img/contributing/article_anatomy.png %})
<sup>*The [Creating a Content Card]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/) page uses the [how-to guide]({{site.baseurl}}/contributing/content_types/#how-to-guides) and [reference]({{site.baseurl}}/contributing/content_types/#references) templates.*</sup>

## Writing content

Other than the Braze-specific syntax covered in this section, all content be written using [standard Markdown syntax](https://www.markdownguide.org/basic-syntax/).

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

To add images, place the image's PNG file inside the relevant location within `assets/img`, then use the following syntax.

{% raw %}
```markdown
![ALT_TEXT.]({% image_buster /assets/img/DIRECTORY/IMAGE.png %})
```
{% endraw %}

{% alert note %}
For a full walkthrough, see [Adding a new image]({{site.baseurl}}/contributing/content_management/images/).
{% endalert %}
