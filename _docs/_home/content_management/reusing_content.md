---
nav_title: Reusing content
page_order: 4
noindex: true
---

# Reusing content

> Learn how to reuse content across Braze Docs, so you can improve content consistency and reduce the time for content creation.

Content reuse in Jekyll is accomplished using includes. Includes are stored in the `_includes` directory as a regular Markdown file. Although, unlike the Markdown files in the `_docs` directory, these files don't need YAML front matter.

For general information about content reuse, see [About our framework]({{sitebase.url}}/docs/home/about_our_framework).

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

Next, reference our [style guide](https://docs.google.com/document/u/2/d/e/2PACX-1vTluyDFO3ZEV7V6VvhXE4As_hSFwmnFFdU9g6_TrAYTgH1QmbRoEDDdn5GzKAB9vdBbIdyiFdoaJcNk/pub) to add content to your page. Your page should look similar to the following:

{% raw %}
```markdown
## Prerequisites

Before you start, you'll need to complete the following:

- [Sign the contributors license agreement]({{site.baseurl}}/cla)
- [Review the Code of Conduct](https://github.com/braze-inc/braze-docs/blob/develop/CODE_OF_CONDUCT.md)
- [Set up your local environment]({{sitebase.url}}/docs/home/getting_started/setting_up_your_environment.md)
```
{% endraw %}

Anytime this [include is used](#using-an-include), the following will be rendered when Jekyll builds the site:

![The "Creating a new page" document with the "Prerequisites" include rendered.]()

{% multi_lang_include contributing/minis/creating_a_pull_request.md %}

## Using an include

In your text editor, open a Markdown file, then add the include you'd like to use.

{% raw %}
```plaintext
{% multi_lang_include PATH_TO_INCLUDE %}
```
{% endraw %}

Replace `PATH_TO_INCLUDE` with the relative path from inside the `_includes` directory. Your reference should look like the following:

_Example file tree:_

```bash
braze-docs
└── _includes
    ├── alerts
    ├── archive
    └── contributing
        └── prerequisites.md
```

_Example include:_

{% raw %}
```plaintext
{% multi_lang_include contributing/prerequisites.md %}
```
{% endraw %}

{% multi_lang_include contributing/minis/creating_a_pull_request.md %}
