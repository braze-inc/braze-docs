---
nav_title: Setting up your environment
page_order: 1
noindex: true
---

# Setting up your environment

> Learn how to set up your local environment, so you can make complex or multi-document changes to Braze Docs. Optionally, for small single-document changes, you can [make changes directly in GitHub]().

## Prerequisites

Before you start, you'll need to complete the following:

- [Download the recommended software]()
- [Create a GitHub account](https://github.com/join)
- Set up your GitHub SSH key:
  - [macOS](https://docs.github.com/en/github-ae@latest/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent?platform=mac)
  - [Windows](https://docs.github.com/en/github-ae@latest/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent?platform=windows)
  - [Linux](https://docs.github.com/en/github-ae@latest/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent?platform=linux)

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

If it's not, use a [supported version manager](https://www.ruby-lang.org/en/documentation/installation/#managers) to install Ruby version `2.7.4`. For example, using [rbenv](https://github.com/rbenv/rbenv):

```bash
rbenv install 2.7.4
```

## Step 3: Install dependencies

Next, install project dependencies.

```bash
bundle install
```

## Step 4: Start a local server

To start your local docs server on localhost `http://127.0.0.1:4000`, run:

```bash
rake
```

To stop your server, reopen the terminal and press **Control**+**C**.

