---
nav_title: Your first contribution
page_order: 2
noindex: true
---

# Your first contribution

> If you're new to docs-as-code or Braze Docs, start here to make your first contribution.

When you're finished with this tutorial, you'll be able to:

<i class="fa-solid fa-circle-check" style="color: #34a853;"></i> Navigate the Braze Docs GitHub repository<br>
<i class="fa-solid fa-circle-check" style="color: #34a853;"></i> Make changes using the GitHub website or your local environment<br>
<i class="fa-solid fa-circle-check" style="color: #34a853;"></i> Create pull-requests (PRs)<br>
<i class="fa-solid fa-circle-check" style="color: #34a853;"></i> Preview your changes in a test site<br>
<i class="fa-solid fa-circle-check" style="color: #34a853;"></i> Request a review from the Braze Docs team<br>

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

- **[`_docs`](https://github.com/braze-inc/braze-docs/tree/develop/_docs):** Contains all the written content for Braze Docs as text files written in Markdown. Text files are organized into directories and subdirectories that mirror the docs site, such as `_api` for the [API section](https://www.braze.com/docs/api/home) and `user_guide` for the [User Guide section](https://www.braze.com/docs/user_guide/introduction).
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

In the [Braze Docs GitHub repository](https://github.com/braze-inc/braze-docs), select **Fork**.

![]()

{% alert tip %}
For more information, see [**About forks**](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/about-forks).
{% endalert %}

Keep the default settings, then select **Create fork**.

![]()

In your forked repository, select **Code** > **SSH** > <i class="fa-regular fa-clone"></i> **Copy**.

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
`git status` displays the current status of your Git directory. If you're new to Git, you can run this command after every step to help visualize the Git workflow. For more information, see [`git status`](https://git-scm.com/docs/git-status).
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

Replace `BRANCH_NAME` with a short, non-space-separated description of your changes. The output is similar to the following:

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

Finally, push your changes to the Braze Docs GitHub repository, so you can [create your pull-request (PR)](#create-a-pull-request-pr) next.

```bash
git push -u origin BRANCH_NAME
```

Replace `BRANCH_NAME` with the name of your branch. The output is similar to the following:

```bash
$ git push -u origin fixing-typo-in-recommended-software
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

When you're finished, select **Commit changes,** so you can [create your pull-request (PR)](#create-a-pull-request-pr) next.

![]()

## Create a pull-request (PR)

On the home page for the [Braze Docs GitHub repository](https://github.com/braze-inc/braze-docs), select **Open pull request**.

![]()

In the PR description, you'll see Markdown comments similar to the following:

```markdown
<!-- This is a Markdown comment. -->
```

These comments will guide you through your PR description. When you're finished, select the pull request dropdown, then select **Draft pull request**.

![]()

## Preview your changes

In you're PR, you can preview your changes in a test environment that's identical to Braze Docs. A new site preview is automatically generated by **vercel bot** anytime changes are pushed to this PR. To open the site preview, select **View deployment**.

![]()

Double-check your work using the following Braze style guides:

- [Writing style guide]()
- [Images style guide]()
- [Alerts style guide]()

If you'd like to make additional changes, see [Make additional changes](). Otherwise, you can [request a review]() from the Braze Docs team.

## Request a review

If you're ready for a member of the Braze Docs team to review your work, select **Ready for review**.

![]()

Then, in the **Reviewers** section, select the **settings gear**, then add `@docs-team` as a reviewer.

![]()

If the docs team requests additional changes after their review, you'll be notified per your [GitHub notification settings](https://docs.github.com/en/account-and-profile/managing-subscriptions-and-notifications-on-github/setting-up-notifications/configuring-notifications). Otherwise, the docs team will approve and merge your changes.

Approved contributions will be deployed on the next Tuesday or Thursday. Be sure to check out [Braze Docs]() to see your hard work. Thanks for contributing!

## Optional: make additional changes

After you or a member of the Braze Docs team reviews your work, you may need to make additional changes to your PR. You can do so using your local environment or GitHub.

### Using your local environment

In your PR, select <i class="fa-regular fa-clone"></i> **Copy** next to your branch name.

![]()

In your text editor's terminal, checkout your branch and pull the latest updates from the remote branch in GitHub.

```branch
git checkout BRANCH_NAME && git pull
```

Replace `BRANCH_NAME` with the branch name you copied to your clipboard. The output is similar to the following:

```branch
$ git checkout -b fixing-typo-in-metadata  && git pull
Switched to branch 'fixing-typo-in-metadata'
Your branch is up to date with 'origin/fixing-typo-in-metadata'.
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

Finally, push your new changes to the remote branch on GitHub, then [request a review]().

```bash
git push
```

The output is similar to the following:

```bash
$ git push
Enumerating objects: 14, done.
...
To github.com:braze-inc/braze-docs.git
 * [new branch]      fixing-typo-in-recommended-software -> fixing-typo-in-recommended-software
branch 'fixing-typo-in-recommended-software' set up to track 'origin/fixing-typo-in-recommended-software'.
```

### Using GitHub

In your PR, select **Files Changes**.

![]()

Locate the file you'd like to update, then select <i class="fa-solid fa-ellipsis"></i> **Ellipsis** > **Edit file**.

![]()

When you're finished, select **Commit changes**.

![]()

Select **Commit directly to the BRANCH_NAME branch** > **Commit changes**, where `BRANCH_NAME` is the name of your branch.

![]()

When you're ready, [request a review]() next.
