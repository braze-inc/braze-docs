---
nav_title: Your first contribution
article_title: Your first contribution
page_order: 2
noindex: true
---

# Your first contribution

> If you're new to docs-as-code or Braze Docs, use this tutorial to learn how make your first contribution.

When you're finished with this tutorial, you'll be able to:

> TODO: replace checkmarks.

- [x] Navigate the Braze Docs GitHub repository
- [x] Make changes using the GitHub website or your local environment
- [x] Create pull-requests (PRs)
- [x] Preview your changes in a test site
- [x] Request a review from the Braze Docs team

## Before you start

You'll need to complete the following:

- [Sign the Contribution License Agreement (CLA)](https://www.braze.com/docs/cla)
- [Review the Code of Conduct](https://github.com/braze-inc/braze-docs/blob/develop/CODE_OF_CONDUCT.md)
- [Create a GitHub account](https://github.com/join)
- Optional: [Set up your local environment]()
- Optional: [Download the recommended software]()

## Explore the GitHub repository

The [Braze Docs GitHub repository](https://github.com/braze-inc/braze-docs) hosts the source files for Braze Docs.

![]()

As a contributor, you'll primarily work within the following directories:

- **[`_docs`](https://github.com/braze-inc/braze-docs/tree/develop/_docs):** Contains all the written content for Braze Docs as text files written in Markdown. Text files are orginized into directories and subdirectories that mirror the docs site, such as `_api` for the [API seciton](https://www.braze.com/docs/api/home) and `user_guide` for the [User Guide section](https://www.braze.com/docs/user_guide/introduction).
- **[`_includes`](https://github.com/braze-inc/braze-docs/tree/develop/_includes):** Contains text files that can be _reused_ in any file within `_docs`. Typically, includes are short, modular pieces of content that don't use standard formatting.
- **[`assets`](https://github.com/braze-inc/braze-docs/tree/develop/assets):** Contains all the images for Braze Docs. Any text file in `_docs` or `_includes` can link to this directory to display an image on its page.

For more information, see [Docs framework]().

## Make a change

Now that you're a little familiar with the docs repository, you're ready to start making changes. First, open [Braze Docs]() and find a simple change you'd like to make. Next, choose how you'd like to make your change:

- **(Recommended) [Using your local environment](#using-your-local-environment):** For complex or multi-document changes, you'll need to make changes from your local environment.
- **[Using GitHub](#using-github):** For small, single-document changes, you can make changes directly from the GitHub website.

{% alert warning %}
Before continuing, verify you've completed all tasks in the [Before you start](#before-you-start) section.
{% endalert %}

### Using your local environment

In the [Braze Docs GitHub repository](https://github.com/braze-inc/braze-docs), select **Code** > **SSH**, then copy the Git URL.

![]()

In your terminal, open your home directory, then clone the Braze Docs repository.

```bash
cd ~
git clone git@github.com:braze-inc/braze-docs.git
```

Most modern text editors (such as [VS Code](https://code.visualstudio.com/Download) and [Intellij IDEA](https://www.jetbrains.com/idea/download/)) offer an in-app terminal. Close your stand-alone terminal, then open the `braze-docs` directory and the in-app terminal in your text editor.

![]()

{% alert tip %}
If you're having trouble, feel free to use your stand-alone terminal instead.
{% endalert %}

In the terminal, check if you're in the `braze-docs` directory, then your Git status.

```bash
pwd
git status
```

{% alert tip %}
`git status` displays the current status of your Git directory. If you're new to Git, you can run this command after every step to help visualize the Git workflow. For more informaiton, see [`git status`](https://git-scm.com/docs/git-status).
{% endalert %}

In the docs repository, the `develop` branch reflects the most up-to-date version of Braze Docs. Checkout the `develop` branch and pull the latest updates into your local environment.

```bash
git checkout develop
git pull
```

When making changes to the docs, you'll always create a new branch. Use `git branch` along with the `-b` flag to create a new branch.

```branch
git checkout -b BRANCH_NAME
```

Replace `BRANCH_NAME` with a short, non-space-sperated description of your changes. The output is similar to the following:

```branch
$ git checkout -b fixing-typo-in-metadata
Switched to a new branch 'fixing-typo-in-metadata'
```

In your text editor, open the document you want to change, then make your changes using [Markdown formatting](). For help navigating the `braze-docs` repository, see [Directory structure]().

![]()

When you're finished, save your changes, then select the terminal and check your Git status. The output is similar to the following:

```bash
$ git status
On branch fixing-typo-in-metadata
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   _docs/_home/metadata.md

no changes added to commit (use "git add" and/or "git commit -a")
```

Use `git add` to tell Git which changes you want to stage for your commit. In the following example, there are two options:

- **Left side of pipe:** Add all of your changed files using `--all`.
- **Right side of pipe:** Add an individual file by replacing `PATH_TO_FILE` with the relative path to your changed file.

```bash
git add {--all|PATH_TO_FILE}
```

Use `git commit` with the `-m` flag to create your commit along with a short description (or message).

```bash
git commit -m "COMMIT_MESSAGE"
```

Replace `COMMIT_MESSAGE` with a short sentence describing your changes. The output is similar to the following:

```bash
$ git commit -m "Fixing a typo in the metadata doc."
[fixing-typo-in-recommended-software 8b05e34] Fixing a typo in the metadata doc.
 1 file changed, 1 insertion(+), 1 deletion(-)
```

Finally, push your changes to the Braze Docs GitHub repository so you can [create your pull-request (PR)](#create-a-pull-request-pr) next.

```bash
git push -u origin BRANCH_NAME
```

Replace `BRANCH_NAME` with the name of your branch. The output is similar to the following:

```bash
$ push -u origin fixing-typo-in-recommended-software
Enumerating objects: 14, done.
...
To github.com:braze-inc/braze-docs.git
 * [new branch]      fixing-typo-in-recommended-software -> fixing-typo-in-recommended-software
branch 'fixing-typo-in-recommended-software' set up to track 'origin/fixing-typo-in-recommended-software'.
```

### Using GitHub

In the [Braze Docs GitHub repository](https://github.com/braze-inc/braze-docs), select `_docs`.

![]()

Each page's URL on Braze Docs reflects the repository's directory structure. Use your page's URL to find its corresponding text file in the `_docs` directory. For more information see [Directory structure]().

For example, `braze.com/home/metadata/` can be found on the following page:

![]()

Select **Edit this file**, then make your changes using [Markdown formatting]().

![]()

When you're finished, select **Commit changes** so you can [create your pull-request (PR)](#create-a-pull-request-pr) next.

![]()

## Create a pull-request (PR)

> TODO

## Preview your changes

> TODO

## Request a review

> TODO
