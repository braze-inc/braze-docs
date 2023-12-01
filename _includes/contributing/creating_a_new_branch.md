## Creating a new branch

Get the latest changes from the Braze Docs repository, then create a new Git branch.

```bash
git checkout develop
git pull
git checkout -b BRANCH_NAME
```

Replace `BRANCH_NAME` with a short, non-space-separated description of your changes. The output is similar to the following:

```bash
$ git checkout -b fixing-typo-in-metadata
Switched to a new branch 'fixing-typo-in-metadata'
```

{% alert tip %}
If you're new to Git or docs-as-code, start with our tutorial: [Your first contribution]().
{% endalert %}