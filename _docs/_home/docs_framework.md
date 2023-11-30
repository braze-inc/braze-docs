---
nav_title: Framework
page_order: 3
noindex: true
---

# Framework

> Learn about the various components that make up the Braze Docs framework.

## Managing the docs

Braze Docs is managed using docs-as-code, a method for managing documentation that mirrors the software development lifecycle by using a version control system. Braze Docs uses the Git version control system, which allows contributors to work on the same piece of documentation without overwriting each other's work.

{% alert note %}
For more information, see [About version control and Git](https://docs.github.com/en/get-started/using-git/about-git#about-version-control-and-git).
{% endalert %}

## Building the site

Braze Docs is built using Jekyll, a popular Static-Site Generator (SSG) that allows content files and design files to be stored in separate directories, such as `_docs` for content files and `assets` for design files. When the site is built, Jekyll intelligently merges each file and stores them as XML and HTML data in the `_site` directory.

{% alert note %}
For more information, see [Jekyll Directory Structure](https://jekyllrb.com/docs/structure/).
{% endalert %}

## Pages

Each page on Braze Docs is written in Markdown syntax and stored as a Markdown file using the `.md` file extension. At the top of each Markdown file, YAML front matter is used to add hidden metadata for each page.

```markdown
---
METADATA_KEY: METADATA_VALUE
---

# CONTENT
```

Replace the following:

- `METADATA_KEY`: The key for a supported metadata type. For more information, see [Metadata]().
- `METADATA_VALUE`: The value assigned to the metadata type's key. For more information, see [Metadata]().
- `CONTENT`: The page's content written in Markdown syntax.

For example:

_Input:_

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

_Output:_

![]()

## Content reuse

Jekyll offers the ability to reuse written content across the docs using the `include` tag. Includes are located in the `_includes` directory and can be written in Markdown or HTML syntax.

```markdown
{% raw %}{% multi_lang_include RELATIVE_PATH/FILE %}{% endraw %}
```

Replace the following:

- `RELATIVE_PATH`: (Optional) The relative path to the file from the `_includes` directory. This is only needed if you're including a file from a directory inside the `_includes` directory, such as `_includes/braze/upgrade_notice.md`.
- `FILE`: The name of the file including the file extension.

For example:

_Input:_

```markdown
# Getting started with Braze

Learn how you can get started with Braze.

{% raw %}{% multi_lang_include braze/upgrade_notice.md %}{% endraw %}
```

_Output:_

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

Replace `LAYOUT_VALUE` with the name of the layout file and the file extension removed. For example, to use the `api_glossary.html` layout, add the following to your YAML front matter:

_Input:_

```markdown
---
layout: api_glossary
---
```

_Output:_

![]()

{% alert note %}
For more information, see [Layouts]().
{% endalert %}

## Sections

> TODO: Something like "There are main sections and subsections... Primary are X and sub are Y."

### Primary sections

> TODO: improve/make better examples.

Articles are organized into section folders (i.e., `_docs/`), and each section folder is defined as a [Jekyll collection](http://jekyllrb.com/docs/collections/). Collections can be thought of as groupings of Jekyll posts that can be given their own unique properties.  Files within `_docs/` will mimic the url structure unless they have a permalinks config value or are `hidden` pages.

Each collection holds relevant articles. For example:

```plaintext
/_docs/_developer_guide/platform_integration_guides/ios/initial_sdk_setup/initial_sdk_setup.md
```

The live url will be based on the collections url. For example:

```plaintext
https://www.braze.com/docs/developer_guide/platform_integration_guides/ios/initial_sdk_setup/initial_sdk_setup/
```

### Subsections

Folders can be created to generate the navigation sidebar layout as desired. Navigation name will use the folder name. If a different folder name is desired, then on the same level as the folder, a config folder file of the same name can be created to determine the order.

In the previous example, there's an iOS folder:

```plaintext
└──_docs/
   └──_developer_guide/
      └──platform_integration_guides/
         ├──ios/
         └──ios.md
```

To label this folder "iOS" in the navigation sidebar, we'll add the following metadata to `ios.md`:

```yaml
---
nav_title: iOS
config_only: true
layout: blank_config
page_order: 1
---
```
