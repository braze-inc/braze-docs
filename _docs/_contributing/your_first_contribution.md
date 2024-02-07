---
nav_title: Your First Contribution
article: Your first contribution
description: "If you're new to docs-as-code or Braze Docs, start with this step-by-step tutorial."
page_order: 1
noindex: true
---

# Your first contribution

> If you're new to docs-as-code or Braze Docs, start with this step-by-step tutorial. If you're an experienced contributor, see [Content Management]({{site.baseurl}}/contributing/content_management/) instead.

When you're finished with this tutorial, you'll be able to:

- Navigate the Braze Docs GitHub repository
- Make changes using the GitHub website or your local environment
- Create pull-requests (PRs)
- Preview your changes in a test site
- Request a review from the Braze Docs team

{% multi_lang_include contributing/prerequisites.md %}

## Step 1: Explore the GitHub repository

The [Braze Docs GitHub repository](https://github.com/braze-inc/braze-docs) hosts the source files for Braze Docs. Take a few minutes to explore the repository, even if you don't understand everything yet. Over time, you'll become more familiar.

![The Braze Docs GitHub repository homepage.]()

## Step 2: Make a change

Now that you're a little familiar with the docs repository, you're ready to start making changes. First, open Braze Docs and find a simple change you'd like to make. Next, choose how you'd like to make your change:

- **Using GitHub (Basic):** For small, single-document changes, you can make changes directly from the GitHub website.
- **Using your local environment (Advanced):** For complex or multi-document changes, you'll need to make changes from your local environment. If you're a documentation guru, this is the recommended method.

{% alert warning %}
Before continuing, verify you've completed all [prerequisites](#prerequisites).
{% endalert %}

{% tabs %}
{% tab github %}
In the [Braze Docs GitHub repository](https://github.com/braze-inc/braze-docs), select `_docs`.

![The Braze Docs GitHub repository homepage with the '_docs' folder highlighted in the file tree.]()

Each page's URL on Braze Docs reflects the repository's directory structure. Use your page's URL to find its corresponding text file in the `_docs` directory. For example, `braze.com/home/yaml_front_matter/` can be found on the following page.

![The "YAML front matter" page in the "Contributing" section on Braze Docs.]()

Select **Edit this file**, then make your changes using [Markdown formatting](https://www.markdownguide.org/basic-syntax/).

![An example page on Braze Docs with the "Edit this file" button highlighted.]()

When you're finished, select **Commit changes**.

![The Braze Docs GitHub repository with the "Commit changes" button highlighted after editing a file.]()
{% endtab %}

{% tab local environment %}
Most modern text editors (such as [VS Code](https://code.visualstudio.com/Download) and [Intellij IDEA](https://www.jetbrains.com/idea/download/)) offer an in-app terminal for running commands and interacting with your project files. Open your text editor, then open your text editor's in-app terminal.

![Intellij IDEA with the in-app terminal open.]()

{% alert tip %}
If you're having trouble, you can use a stand-alone terminal instead.
{% endalert %}

In the terminal, open the `braze-docs` directory.

```bash
cd ~/PATH_TO_REPOSITORY
```

Replace `PATH_TO_REPOSITORY` with the location you saved the `braze-docs` repository when you [set up your environment]({{site.baseurl}}/contributing/home/#step-2-set-up-your-environment). Your command should be similar to the following:

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

In the docs repository, the `develop` branch reflects the most up-to-date version of Braze Docs. Check out the `develop` branch and pull the latest updates into your local environment.

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

In your text editor, open the document you want to change, then make your changes using [Markdown formatting](https://www.markdownguide.org/basic-syntax/).

![A text editor with an example document open.]()

{% multi_lang_include contributing/alerts/tip_locating_a_file.md %}

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
$ git commit -m "Fixing a typo in the recommended software doc"
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

## Step 3: Create a pull-request (PR)

On the homepage for the [Braze Docs GitHub repository](https://github.com/braze-inc/braze-docs), select **Open pull request**.

![The Braze Docs GitHub repository homepage with the "Open pull request" button highlighted.]()

In the PR description, you'll see Markdown comments similar to the following:

```markdown
<!-- This is a Markdown comment. -->
```

These comments will guide you through your PR description. When you're finished, select the pull request dropdown, then select **Draft pull request**.

![An example pull request with the "Draft pull request" button highlighted.]()

## Step 4: Preview your changes

In your PR, you can preview your changes in a test environment that's identical to Braze Docs. In most cases, **Vercel bot** will generate a new site preview anytime someone pushes to this PR. To open the site preview, select **View deployment**.

![An example pull request with the "View deployment" button highlighted next to the Vercel bot.]()

{% alert note %}
If **vercel bot** isn't generating a site preview, tag `@docs-team` for help.
{% endalert %}

Use the [Braze Docs Style Guide]({{sitebase.url}}/contributing/style_guide/) to review your work. If you need to make additional changes, see [Make additional changes](#step-6-make-additional-changes-optional). Otherwise, you can [request a review](#step-5-request-a-review) from the Braze Docs team.

## Step 5: Request a review

If you're ready for a member of the Braze Docs team to review your work, select **Ready for review**.

![An example pull request with the "Ready for review" button highlighted.]()

Next, in the **Reviewers** section, select the gear icon, then add `@docs-team` as a reviewer.

![An example pull request with the "@docs-team" added as the reviewer.]()

If the docs team requests additional changes after their review, you'll be notified per your [GitHub notification settings](https://docs.github.com/en/account-and-profile/managing-subscriptions-and-notifications-on-github/setting-up-notifications/configuring-notifications). Otherwise, the docs team will approve and merge your changes.

Approved contributions will be deployed on the next Tuesday or Thursday. Be sure to check out Braze Docs to see your hard work. Thanks for contributing!

## Step 6: Make additional changes (optional)

After you or a member of the Braze Docs team reviews your work, you may need to make additional changes to your PR. You can do so using your local environment or GitHub.

{% tabs %}
{% tab github %}
In your PR, select **Files Changed**.

![An example pull request with the "Files Changes" tab highlighted.]()

Locate the file you'd like to update, then select <i class="fa-solid fa-ellipsis"></i> **Show options** > **Edit file**.

![The "Filed" section in an example pull request with the "Edit file" button highlighted.]()

When you're finished, select **Commit changes**.

![A file from an example pull request with the "Commit changes" button highlighted after editing.]()

Select **Commit directly to the BRANCH_NAME branch** > **Commit changes**, where `BRANCH_NAME` is the name of your branch.

![The "Commit changes" button highlighted after choosing "Commit directly to BRANCH_NAME branch.]()

When you're ready, you can [request a review](#step-5-request-a-review).
{% endtab %}

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

In your text editor, open the document you want to change, then repeat the repeat the steps you completed earlier during [Step 2: Make a change](#step-2-make-a-change).
{% endtab %}
{% endtabs %}
