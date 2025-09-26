---
nav_title: Git and GitHub
article_title: Git and GitHub
description: "Learn how to use Git and GitHub, so you can contribute to Braze Docs."
page_order: 6
noindex: true
---

# Git and GitHub

> Learn how to use Git and GitHub, so you can contribute to Braze Docs. Approved contributions will be deployed on the following Tuesday or Thursday. Be sure to check out Braze Docs so you can celebrate your hard work. Thanks for contributing!

{% alert tip %}
If you're new to Git or the command-line, start with our tutorial instead: [Your first contribution]({{site.baseurl}}/contributing/your_first_contribution/).
{% endalert %}

{% multi_lang_include contributing/prerequisites.md %}

## Getting the latest changes {#latest}

To update your local environment with the latest changes from the [Braze Docs repository](https://github.com/braze-inc/braze-docs), pull the `develop` branch.

```bash
git checkout develop
git pull
```

## Creating a branch {#create-branch}

To create a new branch, use Git's `checkout` command with the `-b` flag.

```bash
git checkout -b BRANCH_NAME
```

Replace `BRANCH_NAME` with a short, non-space-separated description of your branch's changes. Your output should be similar to the following:

```bash
$ git checkout -b fixing-typo-in-metadata
Switched to a new branch 'fixing-typo-in-metadata'
```

## Creating a pull request {#create-pr}

To create a pull request (PR) for the [branch you created previously](#create-branch), add your changes and stage a commit. Replace `COMMIT_MESSAGE` with a short sentence describing your changes.

```bash
git add --all
git commit -m "COMMIT_MESSAGE"
```

Your output should be similar to the following:

```bash
$ git commit -m "Fixing a typo in the recommended software doc
[fixing-typo-in-recommended-software 8b05e34] Fixing a typo in the metadata doc.
 1 file changed, 1 insertion(+), 1 deletion(-)
```

Push your changes to the Braze Docs GitHub repository. Replace `BRANCH_NAME` with the name of your branch.

{% tabs local %}
{% tab forked repository %}
If you [previously forked the Braze Docs repository]({{site.baseurl}}/contributing/home/#step-3-fork-the-repository), use `upstream` as your remote. External contributors typically fork the repository.

```bash
git push -u upstream BRANCH_NAME
```
{% endtab %}

{% tab cloned repository %}
If you previously cloned the Braze Docs repository, use `origin` as your remote. Internal contributors typically clone the repository.

```bash
git push -u origin BRANCH_NAME
```
{% endtab %}
{% endtabs %}

The output is similar to the following:

```bash
$ git push -u upstream fixing-typo-in-recommended-software
Enumerating objects: 14, done.
...
To github.com:braze-inc/braze-docs.git
 * [new branch]      fixing-typo-in-recommended-software -> fixing-typo-in-recommended-software
branch 'fixing-typo-in-recommended-software' set up to track 'origin/fixing-typo-in-recommended-software'.
```

Go to the [Braze Docs GitHub repository](https://github.com/braze-inc/braze-docs), then select **Compare & pull request**.

![The Braze Docs GitHub repository showing "Open pull request".]({% image_buster /assets/img/contributing/github/compare_and_pull_request.png %})

In the PR description, you'll see Markdown comments similar to the following. Use these comments to help fill out your PR.

```markdown
<!-- This is a Markdown comment. -->
```

When you're finished, select the pull request dropdown, then select **Draft pull request**.

![The Braze Docs GitHub repository showing "Draft pull request".]({% image_buster /assets/img/contributing/github/draft_pull_request.png %}){: style="max-width:65%;"}

## Allowing changes to pull requests {#allow-changes}

In GitHub, go to the [PR you previously created](#create-pr), then check **Allow edits and access to secrets from maintainers**. This will let the Braze Docs team make style or formatting changes to your content.

![A Pull Request showing the allow edits from maintainers checkbox.]({% image_buster /assets/img/contributing/github/allow_maintainers_to_edit.png %}){: style="max-width:50%;"}

## Requesting a review {#request-review}

To request a PR review from a member of the Braze Docs team, go to the [PR you previously created](#create-pr) and select **Ready for review**.

![An example pull request with the "Ready for review" button highlighted.]({% image_buster /assets/img/contributing/github/ready_for_review.png %}){: style="max-width:75%;"}

Select **Reviewers**, then type `braze-inc/docs-team` and select the team name. Press <kbd>Esc</kbd> or click out of the dropdown to confirm your selection.

![An example pull request with "docs-team" added as the reviewer.]({% image_buster /assets/img/contributing/github/add_docs_team_as_reviewers.png %}){: style="max-width:55%;"}

If the Braze Docs team requests additional changes after their review, you'll be notified per your [GitHub notification settings](https://docs.github.com/en/account-and-profile/managing-subscriptions-and-notifications-on-github/setting-up-notifications/configuring-notifications). If no changes are required, the team will approve and merge your changes.

Approved contributions will be deployed on the following Tuesday or Thursday. Be sure to check out Braze Docs so you can celebrate your hard work. Thanks for contributing!
