---
nav_title: Building the docs locally
page_order: 2
noindex: true
---

# Building the docs locally

> Learn how to build the docs locally, so you can preview the changes in your Git branch before creating a Pull Request (PR).

## Prerequisites

To build the docs locally, you'll need to [set up your environment]({{site.baseurl}}/home/getting_started/setting_up_your_environment/). You only need to complete this process once.

## Starting a local server

### Step 1: Checkout a branch

In your terminal, [get the latest updates from `develop`]({{site.baseurl}}/home/github/getting_the_latest_updates/), then check out a branch.

```bash
git checkout BRANCH_NAME
```

Replace `BRANCH_NAME` with one of your branches or another person's branch you're reviewing. Your command should be similar to the following:

```bash
git checkout BD-2346-fixing-typo-swift
```

### Step 2: Start a local server

When you start a local server, the files in your [current branch](#step-1-checkout-a-branch) are used to you build a local preview of Braze Docs. To start a local server using your current branch, run the following command in your `braze-docs` directory:

```bash
rake
```

The output will be similar to the following:

```bash
== Sinatra (v3.0.4) has taken the stage on 4000 for development with backup from Puma
Puma starting in single mode...
* Puma version: 6.3.1 (ruby 2.7.8-p225) ("Mugi No Toki Itaru")
*  Min threads: 8
*  Max threads: 32
*  Environment: development
*          PID: 16158
* Listening on http://127.0.0.1:4000
...
```

### Step 3: Open your site preview

By default, your site preview will be generated on localhost [`http://127.0.0.1:4000`](http://127.0.0.1:4000). To open your site preview, open the link in your web browser.

![An example site preview running in a web browser.]()

### Step 4: Stop your local server

To stop your local server, reopen the terminal and press <kbd>Control</kbd> + <kbd>C</kbd>.

## Updating the site preview

In most cases, your site preview will update automatically when you make changes to the files in `braze-docs`. When this happens, your terminal will output a message similar to the following:

```bash
Asset Pipeline: Processing 'javascript_asset_tag' manifest 'global'
Asset Pipeline: Saved 'global-128fd02b54e35ea79fcb21ea460fac06.js' to '/Users/alex-lee/braze-docs/_site/assets'
                    ...done in 1.940883 seconds.
```

To see these updates in your browser, refresh the page.

{% alert tip %}
You can refresh the current page in your browser by pressing <kbd>Command</kbd> + <kbd>R</kbd> on macOS or <kbd>Control</kbd> + <kbd>R</kbd> on Windows.
{% endalert %}

However, there are cases where your site preview will **not** be automatically updated, such as when:

- File or directory names are changed
- New files or directories are added
- Content changes to files in the `_includes` directory

To see these updates, you'll need to [stop your local server](#step-4-stop-your-local-server) and [start it again](#step-2-start-a-local-server).
