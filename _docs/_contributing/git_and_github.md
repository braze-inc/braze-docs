---
nav_title: Git and GitHub
article: Git and GitHub
description: "Learn how to use Git and GitHub, so you can contribute to Braze Docs."
page_order: 6
noindex: true
---

# Git and GitHub

> Learn how to use Git and GitHub, so you can contribute to Braze Docs.

{% alert tip %}
If you're new to Git or the command-line, start with our tutorial instead: [Your first contribution]({{site.baseurl}}/contributing/your_first_contribution/).
{% endalert %}

{% multi_lang_include contributing/prerequisites.md %}

## Creating a branch

To create a new Git branch, first checkout the `develop` branch and update your local environment.

```bash
git checkout develop
git pull
```

Create a new Git branch using Git's `checkout` command. 

```bash
git checkout -b BRANCH_NAME
```

Replace `BRANCH_NAME` with a short, non-space-separated description of your branch's changes. Your output should be similar to the following:

```bash
$ git checkout -b fixing-typo-in-metadata
Switched to a new branch 'fixing-typo-in-metadata'
```

## Creating a pull request

To create a pull request (PR), first checkout your branch. 

```bash
git checkout BRANCH_NAME
```

Replace `BRANCH_NAME` with the name of your branch [you created previously](#creating-a-branch). Your output should be similar to the following:

```bash
$ git checkout fixing-typo-in-metadata
Switched to branch 'fixing-typo-in-metadata'
```

Add your changes and stage your commit.

```bash
git add --all
git commit -m "COMMIT_MESSAGE"
```

Replace `COMMIT_MESSAGE` with a short sentence describing your changes. Your output should be similar to the following:

```bash
$ git commit -m "Fixing a typo in the recommended software doc
[fixing-typo-in-recommended-software 8b05e34] Fixing a typo in the metadata doc.
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

Next, go to the [Braze Docs GitHub repository](https://github.com/braze-inc/braze-docs), then select **Compare & pull request**.

![The Braze Docs GitHub repository showing "Open pull request".]({% image_buster /assets/img/contributing/github/compare_and_pull_request.png %})

In the PR description, you'll see Markdown comments similar to the following. Use these comments to help fill out your PR.

```markdown
<!-- This is a Markdown comment. -->
```

When you're finished, select the pull request dropdown, then select **Draft pull request**.

![The Braze Docs GitHub repository showing "Draft pull request".]({% image_buster /assets/img/contributing/github/draft_pull_request.png %}){: style="max-width:65%;"}

## Allowing changes to pull requests

In GitHub, go to the Braze Docs repository page and select **Pull requests**.

![Braze Docs repository page with navigation menu containing Pull requests.]({% image_buster /assets/img/contributing/github/menu_pull_requests.png %})

Open the relevant pull request, then check **Allow edits and access to secrets from maintainers**. This will let the Braze Docs team make style or formatting changes to your content.

![A Pull Request showing the allow edits from maintainers checkbox.]({% image_buster /assets/img/contributing/github/allow_maintainers_to_edit.png %}){: style="max-width:50%;"}

## Requesting a review

To request a PR review from a member of the Braze Docs team, open the [PR you previously created](#creating-a-pull-request) and select **Ready for review**.

![An example pull request with the "Ready for review" button highlighted.]({% image_buster /assets/img/contributing/github/ready_for_review.png %}){: style="max-width:75%;"}

**Reviewers** and type `braze-inc/docs-team`. Select the team name and press <kbd>Esc</kbd> or click out of the dropdown to confirm your selection.

![An example pull request with "docs-team" added as the reviewer.]({% image_buster /assets/img/contributing/github/add_docs_team_as_reviewers.png %}){: style="max-width:55%;"}

If the Braze Docs team requests additional changes after their review, you'll be notified per your [GitHub notification settings](https://docs.github.com/en/account-and-profile/managing-subscriptions-and-notifications-on-github/setting-up-notifications/configuring-notifications). If no changes are required, the team will approve and merge your changes.

Approved contributions will be deployed on the following Tuesday or Thursday. Be sure to check out Braze Docs so you can celebrate your hard work. Thanks for contributing!
