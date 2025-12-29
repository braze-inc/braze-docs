---
nav_title: Jekyll collections
article_title: Jekyll Collections
description: "Learn how to create a Jekyll collection so you can add a new primary section on Braze Docs."
page_order: 6.2
---

# Jekyll collections

> Learn how to create a Jekyll collection to add a new primary section on Braze Docs. For more information, see [Jekyll Collections](https://jekyllrb.com/docs/collections/).

{% alert important %}
It's unlikely you'll need to create a new Jekyll collection for your content. If you're unsure where you should store your content, [create a GitHub issue](https://github.com/braze-inc/braze-docs/issues/new?assignees=&labels=issue&projects=&template=report_an_issue.md&title=).
{% endalert %}

{% multi_lang_include contributing/prerequisites.md %}

## Creating a Jekyll collection

### Step 1: Add a new collection

In `config.yml`, add a new Jekyll collection under the `collections` key.

```yaml
collections:
  COLLECTION_KEY:
    title: COLLECTION_TITLE
    output: true
    default_nav_url: COLLECTION_URL/
```

Replace the following:

| Placeholder              | Description                                       |
|-------------------|---------------------------------------------------|
| `COLLECTION_KEY`  | A single, unique word that represents your collection's name. Use lowercase letters only. |
| `COLLECTION_TITLE`| The name of your collection in title case.        |
| `COLLECTION_URL`  | The default URL for your collections landing page.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Your new collection should be similar to the following:

```yaml
collections:
  partners:
    title: Technology Partners
    output: true
    default_nav_url: home/
```

### Step 2: Set a default layout

In `config.yml`, set the default layout for your collection under the `defaults` key.

```yaml
-  
  scope:
    path: ""
    type: "COLLECTION_KEY"
  values:
    nav_level: 1
```

Replace `COLLECTION_KEY` with the key you [set up previously](#step-1-add-a-new-collection). For example:

```yaml
defaults:
  -
    scope:
      path: ""
      type: "partners"
    values:
      nav_level: 1
```

### Step 3: Create a landing page

In the `_docs` directory, create a new directory and add a new Markdown file named `home.md`.

```plaintext
braze-docs
└── _docs
    └── _COLLECTION_NAME
        └── home.md
```

Replace `_COLLECTION_NAME` with the name of your collection using lowercase letters and replacing spaces with underscores. For example:

```plaintext
braze-docs
└── _docs
    └── _technology_partners
        └── home.md
```

{% alert important %}
The directory name for a collection must start with an underscore.
{% endalert %}

### Step 4: Add additional content (optional)

Add additional sections and subsections for your new collection. For a full walkthrough, see [Creating a section]({{site.baseurl}}/contributing/content_management/sections/#creating-a-section).

```plaintext
braze-docs
└── _docs
    └── PRIMARY_SECTION
        └── SUBSECTION
            ├── NEW_DIRECTORY
            └── NEW_FILE.md
```

### Step 5: Set up a redirect file

In `braze-docs/_docs/_docs_pages`, create a new Markdown file for your collection.

```bash
COLLECTION_KEY.md
```

Replace `COLLECTION_KEY` with the key you [set up previously](#step-1-add-a-new-collection). For example:

```plaintext
braze-docs
└── _docs
    └── _docs_pages
        └── partners.md
```

In your Markdown file, add the following YAML front matter:

```markdown
---
config_only: true
noindex: true
layout: redirect
redirect_to: /docs/COLLECTION_KEY/home
permalink: COLLECTION_KEY/
---
```

Replace `COLLECTION_KEY` with the key you [set up previously](#step-1-add-a-new-collection). For example:

```markdown
---
config_only: true
noindex: true
layout: redirect
redirect_to: /docs/partners/home
permalink: partners/
---
```
