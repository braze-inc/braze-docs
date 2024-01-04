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

## Prerequisites

Before you start, you'll need to complete the following:

- [Sign the Contribution License Agreement (CLA)](https://www.braze.com/docs/cla)
- [Review the Code of Conduct](https://github.com/braze-inc/braze-docs/blob/develop/CODE_OF_CONDUCT.md)
- [Create a GitHub account](https://github.com/join)
- Optional: [Set up your local environment]()
- Optional: [Download the recommended software]()

## Explore the GitHub repository

The [Braze Docs GitHub repository](https://github.com/braze-inc/braze-docs) hosts the source files for Braze Docs.

![The Braze Docs GitHub repository homepage.]()

For more information, see [Docs framework]().

## Make a change

Now that you're a little familiar with the docs repository, you're ready to start making changes. First, open [Braze Docs]() and find a simple change you'd like to make. Next, choose how you'd like to make your change:

- **Using GitHub (Basic):** For small, single-document changes, you can make changes directly from the GitHub website.
- **Using your local environment (Advanced):** For complex or multi-document changes, you'll need to make changes from your local environment. If you're a documentation guru, this is the recommended method.

{% alert important %}
Before continuing, verify you've completed all [prerequisite tasks](#prerequisites).
{% endalert %}

{% tabs %}
{% tab github %}
In the [Braze Docs GitHub repository](https://github.com/braze-inc/braze-docs), select `_docs`.

![The Braze Docs GitHub repository homepage with the '_docs' folder highlighted in the file tree.]()

Each page's URL on Braze Docs reflects the repository's directory structure. Use your page's URL to find its corresponding text file in the `_docs` directory. For more information see [Directory structure]().

For example, `braze.com/home/yaml_front_matter/` can be found on the following page:

![The "YAML front matter" page in the "Contributing" section on Braze Docs.]()

Select **Edit this file**, then make your changes using [Markdown formatting]().

![An example page on Braze Docs with the "Edit this file" button highlighted.]()

When you're finished, select **Commit changes**.

![The Braze Docs GitHub repository with the "Commit changes" button highlighted after editing a file.]()
{% endtab %}
{% tab local environment %}
Most modern text editors (such as [VS Code](https://code.visualstudio.com/Download) and [Intellij IDEA](https://www.jetbrains.com/idea/download/)) offer an in-app terminal for running commands and interacting with your project files. Open your text editor, then open your text editor's in-app terminal.

![Intellij IDEA with the in-app terminal open.]()

{% alert tip %}
If you're having trouble, feel free to use your stand-alone terminal instead.
{% endalert %}

In the terminal, open the `braze-docs` directory.

```bash
cd ~/PATH_TO_REPOSITORY
```

Replace `PATH_TO_REPOSITORY` with the location you saved the `braze-docs` repository when you [set up your environment]({{sitebase.url}}/home/getting_started/setting_up_your_environment/). Your command should be similar to the following:

```bash
cd ~/braze/braze-docs
```

Check if you're in the `braze-docs` directory, then check your Git status.

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

```bash
git checkout -b BRANCH_NAME
```

Replace `BRANCH_NAME` with a short, non-space-separated description of your changes. Your command should be similar to the following:

```bash
$ git checkout -b fixing-typo-in-metadata
Switched to a new branch 'fixing-typo-in-metadata'
```

In your text editor, open the document you want to change, then make your changes using [Markdown formatting](). For help navigating the `braze-docs` repository, see [Directory structure]().

![A text editor with an example document open.]()

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

Use `git add` to tell Git which changes you want to stage for your commit. The following command shows two options:

- **Left side of pipe:** Add all of your changed files using `--all`.
- **Right side of pipe:** Add an individual file by replacing `PATH_TO_FILE` with the relative path to your changed file.

```bash
git add {--all|PATH_TO_FILE}
```

Use `git commit` with the `-m` flag to create your commit along with a short description (or message).

```bash
git commit -m "COMMIT_MESSAGE"
```

Replace `COMMIT_MESSAGE` with a short sentence describing your changes. Your command should be similar to the following:

```bash
$ git commit -m "Fixing a typo in the recommended software doc."
[fixing-typo-in-recommended-software 8b05e34] Fixing a typo in the recommended software doc.
 1 file changed, 1 insertion(+), 1 deletion(-)
```

Finally, push your changes to the Braze Docs GitHub repository.

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
{% endtab %}
{% endtabs %}

## Create a pull-request (PR)

On the homepage for the [Braze Docs GitHub repository](https://github.com/braze-inc/braze-docs), select **Open pull request**.

![The Braze Docs GitHub repository homepage with the "Open pull request" button highlighted.]()

In the PR description, you'll see Markdown comments similar to the following:

```markdown
<!-- This is a Markdown comment. -->
```

These comments will guide you through your PR description. When you're finished, select the pull request dropdown, then select **Draft pull request**.

![An example pull request with the "Draft pull request" button highlighted.]()

## Preview your changes

In your PR, you can preview your changes in a test environment that's identical to Braze Docs. A new site preview is automatically generated by **vercel bot** anytime someone pushes to this PR. To open the site preview, select **View deployment**.

![An example pull request with the "View deployment" button highlighted next to the Vercel bot.]()

Double-check your work using the following Braze style guides:

- [Writing style guide]({{sitebase.url}}/docs/home/style_guides/writing/)
- [Images style guide]({{sitebase.url}}/docs/home/style_guides/images/)
- [Alerts style guide]({{sitebase.url}}/docs/home/style_guides/alerts/)

If you'd like to make additional changes, see [Make additional changes](). Otherwise, you can [request a review]() from the Braze Docs team.

## Request a review

If you're ready for a member of the Braze Docs team to review your work, select **Ready for review**.

![An example pull request with the "Ready for review" button highlighted.]()

Then, in the **Reviewers** section, select the **settings gear**, then add `@docs-team` as a reviewer.

![An example pull request with the "@docs-team" added as the reviewer.]()

If the docs team requests additional changes after their review, you'll be notified per your [GitHub notification settings](https://docs.github.com/en/account-and-profile/managing-subscriptions-and-notifications-on-github/setting-up-notifications/configuring-notifications). Otherwise, the docs team will approve and merge your changes.

Approved contributions will be deployed on the next Tuesday or Thursday. Be sure to check out [Braze Docs]() to see your hard work. Thanks for contributing!

## Optional: Make additional changes

After you or a member of the Braze Docs team reviews your work, you may need to make additional changes to your PR. You can do so using your local environment or GitHub.

{% tabs %}
{% tab local environment %}
In your PR, select <i class="fa-regular fa-clone"></i> **Copy** next to your branch name.

![An example pull request with the "Copy" icon highlighted next to the branch name.]()

In your text editor's terminal, checkout your branch and pull the latest updates from the remote branch in GitHub.

```bash
git checkout BRANCH_NAME && git pull
```

Replace `BRANCH_NAME` with the branch name you copied to your clipboard. The output is similar to the following:

```bash
$ git checkout fixing-typo-in-metadata  && git pull
Switched to branch 'fixing-typo-in-metadata'
Your branch is up to date with 'origin/fixing-typo-in-metadata'.
```

In your text editor, open the document you want to change, then make your changes using [Markdown formatting](). For help navigating the `braze-docs` repository, see [Directory structure]().

![A text editor with an example document open.]()

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
$ git commit -m "Fixing a typo in the recommended software doc."
[fixing-typo-in-recommended-software 8b05e34] Fixing a typo in the recommended software doc.
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
{% endtab %}
{% tab github %}
In your PR, select **Files Changed**.

![An example pull request with the "Files Changes" tab highlighted.]()

Locate the file you'd like to update, then select <i class="fa-solid fa-ellipsis"></i> **Ellipsis** > **Edit file**.

![The "Filed" section in an example pull request with the "Edit file" button highlighted.]()

When you're finished, select **Commit changes**.

![A file from an example pull request with the "Commit changes" button highlighted after editing.]()

Select **Commit directly to the BRANCH_NAME branch** > **Commit changes**, where `BRANCH_NAME` is the name of your branch.

![The "Commit changes" button highlighted after choosing "Commit directly to BRANCH_NAME branch."]()

When you're ready, [request a review]() next.
{% endtab %}
{% endtabs %}

