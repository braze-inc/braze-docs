---
nav_title: Creating a new branch
page_order: 0
noindex: true
---

# Creating a new branch

> Learn how to create a new Git branch in your local environment. If you're new to Git or docs-as-code, start with our tutorial instead: [Your first contribution]().

{% multi_lang_include contributing/general_getting_started.md %}

## Creating a new branch

Get the latest changes from the Braze Docs repository, then create a new Git branch.

```bash
git checkout develop
git pull
git checkout -b BRANCH_NAME
```

Replace `BRANCH_NAME` with a short, non-space-separated description of your changes. The output is similar to the following:

```bash
$ git checkout -b fixing-typo-in-metadata
Switched to a new branch 'fixing-typo-in-metadata'
```
