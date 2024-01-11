---
nav_title: Contributing to Braze Docs
page_order: 0
noindex: true
---

# Contributing to Braze Docs

> Thanks for contributing to Braze Docs! Every Tuesday and Thursday, we merge community contributions into the `master` branch and deploy them to Braze Docs. Use this guide to get your changes merged during our next deployment.

## Getting started

Before you start, you'll need to complete the following:

- [Sign the Contribution License Agreement (CLA)](https://www.braze.com/docs/cla)
- [Review the Code of Conduct](https://github.com/braze-inc/braze-docs/blob/develop/CODE_OF_CONDUCT.md)

## Making changes

For small, single-document changes, you can [make changes directly in GitHub]({{sitebase.url}}/docs/home/getting_started/your_first_contribution/?tab=github#make-a-change), like this:

![Editing a file directly in GitHub.]({% image_buster /assets/img/contributing/editing_directly_in_github.png %})

For complex or multi-document changes, you'll need to [set up your local environment]({{sitebase.url}}/docs/home/getting_started/setting_up_your_environment), then [make your changes using Git]({{sitebase.url}}/docs/home/getting_started/your_first_contribution/?tab=local%20environment#make-a-change), like this:

```bash
$ git push origin my-changes

Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 10 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 294 bytes | 294.00 KiB/s, done.
Total 3 (delta 1), reused 1 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
remote:
remote: Create a pull request for 'my-branch' on GitHub by visiting:
remote:      https://github.com/braze-inc/braze-docs/pull/new/my-branch
remote:
To github.com:braze-inc/braze-docs.git
 * [new branch]      my-branch -> my-branch
branch 'my-branch' set up to track 'origin/my-branch'.
```

## Creating a pull request

After making your changes, you'll [create a pull request (PR)]({{sitebase.url}}/docs/home/getting_started/your_first_contribution/#create-a-pull-request-pr). In your PR, you can add a summary, review your commit history, or [open a site preview]({{sitebase.url}}/docs/home/getting_started/your_first_contribution/#preview-your-changes).

![An example pull request (PR) on GitHub.]({% image_buster /assets/img/contributing/creating_a_pull_request.png %})

## Requesting a review

After finalizing your pull request (PR), you'll [submit your PR for review]({{sitebase.url}}/docs/home/getting_started/your_first_contribution/#request-a-review). A member of the Braze Docs team will review your work. If everything looks good, we'll merge your PR into the `develop` branch, and your changes will be deployed to Braze Docs on the next deployment day.

![A pull request (PR) recently merged into the 'develop' branch.]({% image_buster /assets/img/contributing/merging_a_pull_request.png %})
