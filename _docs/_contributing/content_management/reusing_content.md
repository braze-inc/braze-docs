---
nav_title: Reusing Content
article: Reusing content
description: "Learn how to reuse content across Braze Docs, so you can improve content consistency and reduce the time for content creation."
page_order: 5
noindex: true
---

# Reusing content

> Learn how to reuse content across Braze Docs, so you can improve content consistency and reduce the time for content creation. For general information about content reuse, see [Content Management]({{site.baseurl}}/contributing/content_management/#content-reuse).

Content reuse in Jekyll is accomplished using includes. Includes are stored in the `_includes` directory as a regular Markdown file. Although, unlike the Markdown files in the `_docs` directory, these files don't need YAML front matter.

{% multi_lang_include contributing/prerequisites.md %}

## Creating an include

While include files can be stored anywhere in the `_includes` directory, it's best to keep related content together using subdirectories. First, create a new Markdown file with a `.md` extension. Your file tree should like similar to the following:

```bash
braze-docs
└── _includes
    ├── alerts
    ├── archive
    └── contributing
        └── prerequisites.md
```

Next, add content to your page. If you plan on adding your include to a page that already has YAML front matter, do not add front matter to your include. Your page should look similar to the following:

{% raw %}
```markdown
## Prerequisites

Before you start, you'll need to complete the following:

- [Sign the contributors license agreement]({{site.baseurl}}/cla)
- [Review the Code of Conduct](https://github.com/braze-inc/braze-docs/blob/develop/CODE_OF_CONDUCT.md)
- [Set up your local environment]({{site.baseurl}}/home/getting_started/setting_up_your_environment.md)
```
{% endraw %}

{% alert tip %}
For a full walkthrough on adding content to your page, see [Pages]({{site.baseurl}}/contributing/content_management/pages/#writing-content)
{% endalert %}

Anytime the above [include is referenced](#referencing-an-include), the following will be rendered when Jekyll builds the site:

![The "Creating a new page" document with the "Prerequisites" include rendered.]()

## Referencing an include

Open a Markdown file and reference an include using the following syntax: 

{% raw %}
```plaintext
{% multi_lang_include PATH_TO_INCLUDE %}
```
{% endraw %}

Replace `PATH_TO_INCLUDE` with the relative path from inside the `_includes` directory. For example, given the following file tree:

```bash
braze-docs
└── _includes
    ├── alerts
    ├── archive
    └── contributing
        └── prerequisites.md
```

The reference would be similar to the following:

{% raw %}
```plaintext
{% multi_lang_include contributing/prerequisites.md %}
```
{% endraw %}
