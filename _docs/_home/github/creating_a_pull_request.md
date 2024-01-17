---
nav_title: Creating a pull request
page_order: 2
noindex: true
---

# Creating a Pull Request (PR)

> Learn how to create a Pull Request (PR) so you can review your working branch before requesting a review.

{% multi_lang_include contributing/prerequisites.md %}

## Creating a PR

If you're ready to create a PR, that means you've already [created a new branch]({{site.baseurl}}/home/github/creating_a_new_branch/) and you're finished making changes. In the terminal, checkout your previous branch.

```bash
git checkout BRANCH_NAME
```

Replace `BRANCH_NAME` with the branch name you created previously. Your output should be similar to the following:

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
$ git commit -m "Fixing a typo in the recommended software doc."
[fixing-typo-in-recommended-software 8b05e34] Fixing a typo in the metadata doc.
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

Next, go to the [Braze Docs GitHub repository](https://github.com/braze-inc/braze-docs), then select **Open pull request**.

![The Braze Docs GitHub repository with the "Open pull request" button highlighted.]()

In the PR description, you'll see Markdown comments similar to the following. Use these comments to help fill out your PR.

```markdown
<!-- This is a Markdown comment. -->
```

When you're finished, select the pull request dropdown, then select **Draft pull request**.

![The Braze Docs GitHub repository with the "Draft pull request" button highlighted.]()

