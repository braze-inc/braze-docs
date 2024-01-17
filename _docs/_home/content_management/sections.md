---
nav_title: Sections
page_order: 2
noindex: true
---

# Sections

> Learn how to create and order sections on Braze Docs. If you'd like to create, modify, or delete an individual page instead, see [Pages]({{site.baseurl}}/home/content_management/pages/). For general information about sections, see [About our framework]({{site.baseurl}}/home/about_our_framework).

{% multi_lang_include contributing/prerequisites.md %}

## Creating a section

When you create a new section, you have the option to create a section with or without a landing page.

- **With landing page:** Use this method if your section needs a dedicated overview, such as a landing page for a "Getting started" section listing prerequisites and outlining the user journey.
- **Without landing page:** Use this method if your section does not need a dedicated overview. Per the [Braze Docs Style Guide](https://docs.google.com/document/u/2/d/e/2PACX-1vTluyDFO3ZEV7V6VvhXE4As_hSFwmnFFdU9g6_TrAYTgH1QmbRoEDDdn5GzKAB9vdBbIdyiFdoaJcNk/pub#h.26dvs9p769cx), content should always be useful, so avoid adding a langing page if it offers little useful content.

{% tabs %}
{% tab with landing page %}
To create a section with a landing page, [create a new branch]({{site.baseurl}}/home/github/creating_a_new_branch/), then navigate to the relevant primary section or subsection and create a directory and Markdown file for your new section.

```plaintext
braze-docs
└── _docs
    └── PRIMARY_SECTION 
        └── SUBSECTION 
            ├── NEW_DIRECTORY 
            └── NEW_FILE.md
```

Replace the following:

| Placeholder       | Description                                                                                                                                                                                                                                                                                                                                                                             |
|-------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `PRIMARY_SECTION` | The name of the primary section your new content belongs to. For more information, see [Primary sections]({{site.baseurl}}/home/about_our_framework/#primary-sections).                                                                                                                                                                                                            |
| `SUBSECTION`      | If applicable, the name of the subsection your new content belongs to. For more information, see [Subsections]({{site.baseurl}}/home/about_our_framework/#subsections).                                                                                                                                                                                                            |
| `NEW_DIRECTORY`   | The name of your new section (be sure it adheres to the [Headings and Titles](https://docs.google.com/document/u/2/d/e/2PACX-1vTluyDFO3ZEV7V6VvhXE4As_hSFwmnFFdU9g6_TrAYTgH1QmbRoEDDdn5GzKAB9vdBbIdyiFdoaJcNk/pub#h.vs0awrl1ba2p) guideline). Use all lowercase characters, remove special characters, and replace spaces with underscores (`_`). This name must match `NEW_FILE`.      |
| `NEW_FILE`        | The name of your new section (be sure it adheres to the [Headings and Titles](https://docs.google.com/document/u/2/d/e/2PACX-1vTluyDFO3ZEV7V6VvhXE4As_hSFwmnFFdU9g6_TrAYTgH1QmbRoEDDdn5GzKAB9vdBbIdyiFdoaJcNk/pub#h.vs0awrl1ba2p) guideline). Use all lowercase characters, remove special characters, and replace spaces with underscores (`_`). This name must match `NEW_DIRECTORY`. |
{: .reset-td-br-1 .reset-td-br-2}

Your directory structure should look similar to the following:

```plaintext
braze-docs
└── _docs
    └── _developer_guide 
        └── platform_wide 
            ├── getting_started 
            └── getting_started.md
```

Open your new Markdown file and add the following template to use the default landing-page layout. For other layouts, see [Layouts]({{site.baseurl}}/home/examples/layouts).

```markdown
---
nav_title: NAV_TITLE
article_title: LANDING_PAGE_TITLE
description: SHORT_DESCRIPTION
---

# LANDING_PAGE_TITLE 

> SHORT_DESCRIPTION

## HEADING

CONTENT
```

Replace the following:

| Placeholder          | Description                                                                                                                                                                                                                                 |
|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `NAV_TITLE`          | The title of your page as it will appear on the left-side navigation bar. In most cases, `nav_title` should match `article_title`, however to save space, you may use a shorter _but still similar_ title.                                  |
| `LANDING_PAGE_TITLE` | The title of your landing page. The `LANDING_PAGE_TITLE` value in the metadata is used for search engine results, while the `LANDING_PAGE_TITLE` value in Heading 1 is used for the title rendered on the page.                             |
| `SHORT_DESCRIPTION`  | A short, 1-2 sentence description of your page. The `SHORT_DESCRIPTION` value in YAML the metadata is used for search engine results, while the `SHORT_DESCRIPTION` value after Heading 1 is used for the description rendered on the page. |
| `HEADING`            | The title of your Heading 2 section.                                                                                                                                                                                                        |
| `CONTENT`            | The body paragraph for your Heading 2 section.                                                                                                                                                                                              |
{: .reset-td-br-1 .reset-td-br-2}

{% alert tip %}
You may add additional metadata and headings as needed, this template is just to get you started. For the full list of supported YAML metadata, see [YAML front matter]({{site.baseurl}}/home/yaml_front_matter).
{% endalert %}

Next, open your new directory and create a Markdown file for each new page you want to add to your new section. Your directory structure should look similar to the following:

```plaintext
braze-docs
└── _docs
    └── _developer_guide 
        └── platform_wide 
            ├── getting_started 
            │    ├── integrating_the_sdk.md 
            │    └── setting_up_push_notifications.md
            └── getting_started.md
```

[Add content]({{site.baseurl}}/home/content_management/pages/#modifying-a-page) to each page as needed. When you're finished, continue to [Ordering a section](#ordering-a-section).
{% endtab %}

{% tab without landing page %}
To create a section without a landing page, create a [new branch]({{site.baseurl}}/home/github/creating_a_new_branch/), then navigate to the relevant primary section or subsection and create a directory and Markdown file for your new section.

```plaintext
braze-docs
└── _docs
    └── PRIMARY_SECTION 
        └── SUBSECTION 
            ├── NEW_DIRECTORY 
            └── NEW_FILE.md
```

Replace the following:

| Placeholder       | Description                                                                                                                                                                                                                                                                                                                                                                             |
|-------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `PRIMARY_SECTION` | The name of the primary section your new content belongs to. For more information, see [Primary sections]({{site.baseurl}}/home/about_our_framework/#primary-sections).                                                                                                                                                                                                            |
| `SUBSECTION`      | If applicable, the name of the subsection your new content belongs to. For more information, see [Subsections]({{site.baseurl}}/home/about_our_framework/#subsections).                                                                                                                                                                                                            |
| `NEW_DIRECTORY`   | The name of your new section (be sure it adheres to the [Headings and Titles](https://docs.google.com/document/u/2/d/e/2PACX-1vTluyDFO3ZEV7V6VvhXE4As_hSFwmnFFdU9g6_TrAYTgH1QmbRoEDDdn5GzKAB9vdBbIdyiFdoaJcNk/pub#h.vs0awrl1ba2p) guideline). Use all lowercase characters, remove special characters, and replace spaces with underscores (`_`). This name must match `NEW_FILE`.      |
| `NEW_FILE`        | The name of your new section (be sure it adheres to the [Headings and Titles](https://docs.google.com/document/u/2/d/e/2PACX-1vTluyDFO3ZEV7V6VvhXE4As_hSFwmnFFdU9g6_TrAYTgH1QmbRoEDDdn5GzKAB9vdBbIdyiFdoaJcNk/pub#h.vs0awrl1ba2p) guideline). Use all lowercase characters, remove special characters, and replace spaces with underscores (`_`). This name must match `NEW_DIRECTORY`. |
{: .reset-td-br-1 .reset-td-br-2}

Your directory structure should look similar to the following:

```plaintext
braze-docs
└── _docs
    └── _developer_guide 
        └── platform_wide 
            ├── getting_started 
            └── getting_started.md
```

Open your new Markdown file and add the following metadata to set your page's navigation title and disable the landing page:

```markdown
---
nav_title: NAV_TITLE
config_only: true
---
```

{% alert tip %}
You may add additional metadata and headings as needed, as this template is just to get you started. For the full list of supported YAML metadata, see [YAML front matter]({{site.baseurl}}/home/yaml_front_matter).
{% endalert %}

Replace `NAV_TITLE` with the title of your page as it will appear on the left-side navigation bar. Your page should look similar to the following:

```markdown
---
nav_title: Getting started
page_order: 2
noindex: true
config_only: true
---
```

Next, open your new directory and create a Markdown file for each new page you want to add to your new section. Your directory structure should look similar to the following:

```plaintext
braze-docs
└── _docs
    └── _developer_guide 
        └── platform_wide 
            ├── getting_started 
            │    ├── integrating_the_sdk.md 
            │    └── setting_up_push_notifications.md
            └── getting_started.md
```

[Add content]({{site.baseurl}}/home/content_management/pages/#modifying-a-page) to each page as needed. When you're finished, continue to [Ordering a section](#ordering-a-section).
{% endtab %}
{% endtabs %}

## Ordering a section

To order a section, first, [create a new branch]({{site.baseurl}}/home/github/creating_a_new_branch), then open one of the section's Markdown files in your text editor. Next, search for the `page_order` tag in your YAML metadata. If it doesn't exist, you can add it now.

The `page_order` tag represents a page's relative-order in a section on the left-side navigation bar and can be set to any non-negative number (such as `0`, `20`, or `5.5`). This means you'll need to know the `page_order` for each Markdown file in the current directory, but not any other directory (including subdirectories).

Set the `page_order` tag for each Markdown file in the currect directory to any non-negative number. Your file should look similar to the following:

```markdown
---
nav_title: Getting started
page_order: 2
noindex: true
config_only: true
---
```

{% multi_lang_include contributing/minis/creating_a_pull_request.md %}

