---
nav_title: Your first contribution
article_title: Your first contribution
description: "If you're new to docs-as-code or Braze Docs, start with this step-by-step tutorial."
page_order: 1
noindex: true
---

# Your first contribution

> If you're new to docs-as-code or Braze Docs, start with this step-by-step tutorial. If you're an experienced contributor, see [About content management]({{site.baseurl}}/contributing/content_management/) instead.

When you're finished with this tutorial, you'll be able to:

- Navigate the Braze Docs GitHub repository
- Make changes using the GitHub website or your local environment
- Create pull requests (PRs)
- Preview your changes in a test site
- Request a review from the Braze Docs team

{% multi_lang_include contributing/prerequisites.md %}

## Making your first contribution

### Step 1: Explore the GitHub repository

The [Braze Docs GitHub repository](https://github.com/braze-inc/braze-docs) hosts the source files for Braze Docs. Take a few minutes to explore the repository, even if you don't understand everything yet. Over time, you'll become more familiar.

![The Braze Docs GitHub repository homepage.]({% image_buster /assets/img/contributing/github/home_page.png %})

### Step 2: Make a change

Now that you're a little familiar with the docs repository, you're ready to start making changes. First, open [Braze Docs]({{site.baseurl}}) and find a simple change you'd like to make.

You'll make your change using the [same method you chose previously]({{site.baseurl}}/contributing/home#step-4-choose-how-to-contribute):

|Method           |Use Case                              |Additional Requirements                                                                                              |
|-----------------|--------------------------------------|--------------------------------------------------------------------------------------------------------------------|
|GitHub website   |For small, single-document changes.   |No additional requirements needed. With this method, you're ready to start contributing!|
|Local environment|For complex or multi-document changes.|Before you can use this method, you'll need to [set up your local environment]({{site.baseurl}}/contributing/local_environment).|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

{% tabs %}
{% tab github %}
#### Step 2.1: Find the page on GitHub

In the [Braze Docs GitHub repository](https://github.com/braze-inc/braze-docs), select `_docs`.

![The Braze Docs GitHub repository homepage with the '_docs' folder highlighted in the file tree.]({% image_buster /assets/img/contributing/github/select_docs_directory.png %})

Each page's URL on Braze Docs reflects the repository's directory structure. Use your page's URL to find its corresponding Markdown file in the `_docs` directory. For example, the Markdown file for `braze.com/contributing/home` can be found in `_docs` > `_contributing` > `home.md`.

![The home page for the "Contributing" section on Braze Docs.]({% image_buster /assets/img/contributing/github/example_file_path.png %})

#### Step 2.2: Edit the file

Select **Edit this file**, then make your changes using [Markdown formatting](https://www.markdownguide.org/basic-syntax/).

![An example page on Braze Docs showing "Edit this file".]({% image_buster /assets/img/contributing/github/edit_from_directory.png %})

When you're finished, select **Commit changes**.

![The Braze Docs GitHub repository showing "Commit changes" after editing a file.]({% image_buster /assets/img/contributing/github/commit_changes.png %})

#### Step 2.3: Propose your changes

In the next window, choose **Create a new branch for this commit and start a pull request**. If you choose the first option, your changes will not be sent to the correct location, so double-check that the correct option is selected before continuing.

After confirming, select **Propose changes**.

![The "Propose changes" window after selecting "Commit changes" in GitHub.]({% image_buster /assets/img/contributing/github/propose_changes.png %}){: style="max-width:65%;"}

In the next window, select **compare across forks**.

![The "Comparing changes" window with "compare across forks" highlighted.]({% image_buster /assets/img/contributing/github/compare_across_forks.png %})

From the base repository dropdown, choose **braze-inc/braze-docs**, then select **Create pull request**. You'll learn how to fill out the draft in the next step.

![The "Comparing changes" window with "braze-inc/braze-docs" highlighted in the base repository dropdown list.]({% image_buster /assets/img/contributing/github/choose_base_repository.png %})

{% alert important %}
If `braze-inc/braze-docs` is missing from the list of available base branches, there may be an issue with the origin of your forked repository. For detailed information, see [Troubleshooting]({{site.baseurl}}/contributing/troubleshooting/#missing-base-repository).
{% endalert %}
{% endtab %}

{% tab local environment %}
#### Step 2.1: Get the latest changes

Most modern text editors (such as [VS Code](https://code.visualstudio.com/Download) and [Intellij IDEA](https://www.jetbrains.com/idea/download/)) offer an in-app terminal for running commands and interacting with your project files. Open your text editor, then open your text editor's in-app terminal.

![Intellij IDEA with the in-app terminal open.]({% image_buster /assets/img/contributing/text_editor_with_terminal.png %})

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

#### Step 2.2: Create a new branch

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

#### Step 2.3: Edit the file

In your text editor, open the document you want to change, then make your changes using [Markdown formatting](https://www.markdownguide.org/basic-syntax/).

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

#### Step 2.4: Push your changes

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
git push -u upstream BRANCH_NAME
```

Replace `BRANCH_NAME` with the name of your branch. The output is similar to the following:

```bash
$ git push -u upstream fixing-typo-in-recommended-software
Enumerating objects: 14, done.
...
To github.com:braze-inc/braze-docs.git
 * [new branch]      fixing-typo-in-recommended-software -> fixing-typo-in-recommended-software
branch 'fixing-typo-in-recommended-software' set up to track 'origin/fixing-typo-in-recommended-software'.
```

#### Step 2.5: Create your pull request

Go back to the [repository homepage](https://github.com/braze-inc/braze-docs) and select **Compare & pull request**. You'll learn how to fill out the draft in the next step.

![The Braze Docs GitHub repository homepage showing "Open pull request".]({% image_buster /assets/img/contributing/github/compare_and_pull_request.png %})
{% endtab %}
{% endtabs %}

### Step 3: Fill out your pull request (PR)

In the PR description, you'll see Markdown comments similar to the following:

```markdown
<!-- This is a Markdown comment. -->
```

These comments will guide you through your PR description. When you're finished, select the pull request dropdown, then select **Draft pull request**.

![An example pull request showing "Draft pull request".]({% image_buster /assets/img/contributing/github/draft_pull_request.png %}){: style="max-width:65%;"}

Finally, check **Allow edits and access to secrets from maintainers**. This will let the Braze Docs team make style or formatting changes to your content during their review later.

![A Pull Request showing the allow edits from maintainers checkbox.]({% image_buster /assets/img/contributing/github/allow_maintainers_to_edit.png %}){: style="max-width:50%;"}

### Step 4: Review your work

Create your content by following the [Braze Docs Style Guide]({{sitebase.url}}/contributing/style_guide/) and reviewing your work in a site preview. If you need to make additional changes, see [Make additional changes](#step-6-make-additional-changes-optional). Otherwise, you can [request a review](#step-5-request-a-review) from the Braze Docs team.

{% tabs %}
{% tab github %}
In a PR comment, tag `@braze-inc/docs-team` to request a site preview.

![An example comment tagging the Braze Docs team to request a site preview.]({% image_buster /assets/img/contributing/github/tag_docs_team_in_comment.png %}){: style="max-width:83%;"}

To open the site preview, select **View deployment**.

![An example pull request showing the "View deployment" button generated by the Vercel bot.]({% image_buster /assets/img/contributing/github/view_deployment.png %})

{% endtab %}

{% tab local environment %}
In the terminal, use the `rake` command start a local server.

```bash
cd ~/braze-docs
rake
```

The output will be similar to the following:

```bash
== Sinatra (v3.0.4) has taken the stage on 4000 for development with backup from Puma
Puma starting in single mode...
* Puma version: 6.3.1 (ruby 3.2.2-p225) ("Mugi No Toki Itaru")
*  Min threads: 8
*  Max threads: 32
*  Environment: development
*          PID: 16158
* Listening on http://127.0.0.1:4000
...
```

By default, your site preview will be generated on localhost [`http://127.0.0.1:4000`](http://127.0.0.1:4000). To open your site preview, open the link in your web browser.

![An example site preview running in a web browser.]({% image_buster /assets/img/contributing/styling_examples/home.png %})

To stop your local server, reopen the terminal and press <kbd>Control</kbd> + <kbd>C</kbd>.

{% alert tip %}
For a full walkthrough, see [Generating a preview]({{site.baseurl}}/contributing/generating_a_preview/)
{% endalert %}
{% endtab %}
{% endtabs %}

### Step 5: Request a review

If you're ready for a member of the Braze Docs team to review your work, select **Ready for review**.

![An example pull request showing "Ready for review".]({% image_buster /assets/img/contributing/github/ready_for_review.png %}){: style="max-width:75%;"}

In the **Reviewers** field, type `braze-inc/docs-team`. Select the team name and press <kbd>Esc</kbd> or click out of the dropdown to confirm your selection.

![An example pull request with "docs-team" added as the reviewer.]({% image_buster /assets/img/contributing/github/add_docs_team_as_reviewers.png %}){: style="max-width:55%;"}

If the docs team requests additional changes after their review, you'll be notified per your [GitHub notification settings](https://docs.github.com/en/account-and-profile/managing-subscriptions-and-notifications-on-github/setting-up-notifications/configuring-notifications). Otherwise, the docs team will approve and merge your changes.

Approved contributions will be deployed on the next Tuesday or Thursday. Be sure to check out Braze Docs to see your hard work. Thanks for contributing!

### Step 6: Make additional changes (optional)

After you or a member of the Braze Docs team reviews your work, you may need to make additional changes to your PR. You can do so using your local environment or GitHub.

{% tabs %}
{% tab github %}
In your PR, select **Files changed**, then locate the file you'd like to update and select <i class="fa-solid fa-ellipsis"></i> **Show options** > **Edit file**.

![The "Files changed" section in an example pull request showing "Edit file".]({% image_buster /assets/img/contributing/github/edit_from_pr.png %})

When you're finished, select **Commit changes**.

![A file from an example pull request showing "Commit changes" after editing.]({% image_buster /assets/img/contributing/github/commit_changes.png %})

Select **Commit directly to the BRANCH_NAME branch** > **Commit changes**, where `BRANCH_NAME` is the name of your branch.

![The "Commit changes" option after choosing "Commit directly to BRANCH_NAME branch.]({% image_buster /assets/img/contributing/github/confirm_committed_changes.png %}){: style="max-width:65%;"}

When you're finished, [request a review](#step-5-request-a-review).
{% endtab %}

{% tab local environment %}
In your PR, select <i class="fa-regular fa-clone"></i> **Copy** next to your branch name.

![An example pull request with the "Copy" icon shown next to the branch name.]({% image_buster /assets/img/contributing/github/clone_the_fork.png %})

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
