# Welcome to the Braze Docs wiki!

Thanks for contributing to Braze Docs! Every Tuesday and Thursday we merge community contributions into the `main` branch and deploy them to [Braze Docs](http://www.braze.com/docs). Follow this guide to get your changes merged next!

## Before you start

You'll need to complete the following before contributing:

- [Sign the Contribution License Agreement (CLA)](https://www.braze.com/docs/cla)
- [Review the Code of Conduct](./CODE_OF_CONDUCT.md)

## Making changes

For small, single-document changes, you can [make changes directly in GitHub](./first_time_contributors/making_changes_directly_in_github.md).

![Editing a file directly in GitHub.](./assets/img/contributing/editing_directly_in_github.png)

For complex or multi-document changes, you'll need to [set up your local environment](./first_time_contributors/setting_up_your_local_environment.md), then [make your changes locally](./first_time_contributors/making_changes_in_your_local_environment.md).

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

After making your changes, you'll [create a pull request (PR)](./github/creating_a_pull_request.md). In your PR, you can add a PR summary, check commit history, or [view your changes in a site preview](./github/viewing_your_site_preview.md).

![An example pull request (PR) on GitHub.](./assets/img/contributing/creating_a_pull_request.png)

## Submitting for review

After finalizing your pull request (PR), you'll [submit your PR for review](). Someone at Braze will review your work. If everything looks good, we'll merge your PR into the `develop` branch and your changes will be deployed to [Braze Docs](https://braze.com/docs) on the next Tuesday or Thursday.

![A pull request (PR) recently merged into the 'develop' branch.](./assets/img/contributing/merging_a_pull_request.png)
