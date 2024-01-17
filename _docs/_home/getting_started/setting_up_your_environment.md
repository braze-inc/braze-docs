---
nav_title: Setting up your environment
page_order: 1
noindex: true
---

# Setting up your environment

> Learn how to set up your local environment, so you can make complex or multi-document changes to Braze Docs. After it's set up, you'll be able to [build the docs locally]({{site.baseurl}}/home/getting_started/building_the_docs_locally/) and review your work an offline site preview.

{% alert tip %}
You only need to set up your environment a single time.
{% endalert %}

## Prerequisites

Before you start, you'll need to complete the following:

- [Download the recommended software]({{site.baseurl}}/home/getting_started/recommended_software/)
- [Create a GitHub account](https://github.com/join)
- Set up your GitHub SSH key on [macOS](https://docs.github.com/en/github-ae@latest/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent?platform=mac) or [Linux](https://docs.github.com/en/github-ae@latest/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent?platform=linux). If you're using [Windows Subsystem for Linux (WSL)](https://learn.microsoft.com/en-us/windows/wsl/install), use the Linux setup instructions.

## Step 1: Fork the repository

Open the [Braze Docs GitHub repository](https://github.com/braze-inc/braze-docs), then select **Fork**.

![The Braze Docs GitHub repository with the "Fork" button highlighted.]()

{% alert tip %}
For more information, see [**About forks**](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/about-forks).
{% endalert %}

Keep the default settings, then select **Create fork**.

![The Braze Docs GitHub repository with the "Create fork" button highlighted.]()

In your forked repository, select **Code** > **SSH** > <i class="fa-regular fa-clone"></i> **Copy**.

![An example forked repository with the "Code" dropdown open and the "Copy" icon highlighted.]()

In your terminal, open your home directory, then clone the Braze Docs repository.

```bash
cd ~
git clone git@github.com:braze-inc/braze-docs.git
```

## Step 2: Install Ruby 

To build the docs locally, you'll need Ruby version `2.7.4` installed. In the terminal, open `braze-docs` and check for Ruby version `2.7.4`.

```bash
cd ~/braze-docs
ruby --version
```

If this version isn't installed, use a [supported version manager](https://www.ruby-lang.org/en/documentation/installation/#managers) to install Ruby version `2.7.4`. For example, using [rbenv](https://github.com/rbenv/rbenv):

```bash
rbenv install 2.7.4
```

## Step 3: Install dependencies

Next, install the dependencies for Braze Docs. These are small programs used to generate your local Braze Docs site.

```bash
bundle install
```

## Step 4: Start a local server

To generate the Braze Docs site and run it in a local server, first checkout your git branch.

```bash
rake
```

By default, Braze Docs will be generated on localhost [`http://127.0.0.1:4000`](http://127.0.0.1:4000). To access the site, open the link in your browser.

To stop your local server, reopen the terminal and press <kbd>Control</kbd> + <kbd>C</kbd>.
