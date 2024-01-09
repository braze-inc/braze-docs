---
nav_title: Creating a new branch
page_order: 0
noindex: true
---

# Creating a new branch

> Learn how to create a new Git branch in your local environment. If you're new to Git or docs-as-code, start with our tutorial instead: [Your first contribution]({{site.baseurl}}/docs/home/getting_started/your_first_contribution/).

{% multi_lang_include contributing/prerequisites.md %}

## Creating a branch

In your terminal, open the Braze Docs repository.

```bash
cd ~/PATH/braze-docs
```

Replace `PATH` with the file path to the `braze-docs` directory you downloaded when you [set up your environment]({{site.baseurl}}/home/getting_started/setting_up_your_environment/). Your terminal command should be similar to the following:

```bash
cd ~/open-source/braze/braze-docs
```

Checkout the `develop` branch and download the latest updates.

```bash
git checkout develop
git pull
```

Create a new branch.

```bash
git checkout -b BRANCH_NAME
```

Replace `BRANCH_NAME` with a short, non-space-separated description of your branch's changes. Your output should be similar to the following:

```bash
$ git checkout -b fixing-typo-in-metadata
Switched to a new branch 'fixing-typo-in-metadata'
```

