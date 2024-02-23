---
nav_title: Jekyll Collections
article_title: Jekyll collections
description: "Learn how to create a Jekyll collection, so you can add a new primary section on Braze Docs."
page_order: 6
---

# Jekyll collections

> Learn how to create a Jekyll collection, so you can add a new primary section on Braze Docs.

{% alert important %}
It's unlikely you'll need to create a new Jekyll collection. If you're having trouble deciding where your content should go, [create a GitHub issue](https://github.com/braze-inc/braze-docs/issues/new?assignees=&labels=issue&projects=&template=report_an_issue.md&title=) instead.
{% endalert %}

{% multi_lang_include contributing/prerequisites.md %}

## Creating a Jekyll collection

### Step 1: Add a new collection

In `config.yml`, under `collections`:

```yaml
contributing:
    output: true
    default_nav_url: COLLECTION_NAME/
```

Replace... Example:

```yaml
collections:
  home:
    title: Documentation
    output: true
    default_nav_url: ''
    page_order: 1
  contributing:
    output: true
    default_nav_url: contributing/
```

### Step 2: Set a default layout

In `config.yml`, under `defaults`:

```yaml
scope:
  path: ""
  type: "COLLECTION_NAME"
values:
  nav_level: 1
```

<!-- Add alert for a link to additional supported values -->

Replace... Example:

```yaml
defaults:
  -
    scope:
      path: ""
    values:
      layout: "documents"
      default_nav_url: home/
      search_rank: 0
      toc_minheaders: 2
      toc_headers: "h2, h3"
  -
    scope:
      path: ""
      type: "home"
    values:
      nav_level: 1
  -
    scope:
      path: ""
      type: "contributing"
    values:
      nav_level: 1
```

### Step 3: Create a landing page

In the `_docs` directory, create a new directory.

```bash
_COLLECTION_NAME
```

Replace... Example:

```bash
TREE
```

Create a new Markdown file for your landing page named `home.md`. Example:

```bash
TREE
```

### Step 4: Add additional content

Add additional subsections and subsections for your new collection.

<!-- Link / include content from pages / sections -->

### Step 5: Set up a redirect file

Go to `_docs` > `_docs_pages` and create a new Markdown file.

```bash
COLLECTION_NAME.md
```

Replace... Example:

```bash
contributing.md
```

In your Markdown file...

```markdown
---
config_only: true
noindex: true
layout: redirect
redirect_to: /docs/COLLECTION_NAME/home
permalink: COLLECTION_NAME/
---
```

Replace... Example:

```markdown
---
config_only: true
noindex: true
layout: redirect
redirect_to: /docs/contributing/home
permalink: contributing/
---
```
