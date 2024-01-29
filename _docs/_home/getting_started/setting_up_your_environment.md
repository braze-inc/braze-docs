---
nav_title: Setting up your environment
page_order: 1
noindex: true
---

# Setting up your environment

> Learn how to set up your local environment, so you can make complex or multi-document changes to Braze Docs. You'll only need to do set up your environment once. Once you're finished, you can [build the docs locally]({{site.baseurl}}/home/getting_started/building_the_docs_locally/) to preview your work while you write. 

## Prerequisites

Before you start, you'll need to [create a GitHub account](https://github.com/join) and [set up your SSH key](https://docs.github.com/en/enterprise-cloud@latest/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent).

{% alert note %}
If you're using [Windows Subsystem for Linux (WSL)](https://learn.microsoft.com/en-us/windows/wsl/install), set up your SSH key using the Linux setup instructions.
{% endalert %}

## Step 1: Download the minimum software

At a minimum, you'll need the following:

- A terminal
- A text editor
- A ruby version manager

If you're not sure which specific products to choose, here's our recommendations: 

<style>
table td {
    word-break: break-word;
}
</style>
<table>
<thead>
    <tr>
        <th>Type</th>
        <th>Product</th>
        <th>Description</th>
    </tr>
</thead>
<tbody>
    <tr>
        <td>Terminal</td>
        <td><a href="https://wezfurlong.org/wezterm/index.html">Wezterm</a></td>
        <td>A terminal emulator that allows you to run commands and interact with the Braze Docs repository from the commandline. If you're using a Windows operating system, you'll also need to install Windows Subsystem for Linux (WSL).</td>
    </tr>
    <tr>
        <td>Terminal extension</td>
        <td><a href="https://learn.microsoft.com/en-us/windows/wsl/install">Windows Subsystem for Linux (WSL)</a> *</td>
        <td>WSL lets you install a Linux subsystem and run Unix-like commands on your Windows operating system. If you're contributing from a Windows operating system, we recommend installing WSL, so you can use any Unix-like command mentioned in the docs.<br><br><em>* Only available for Windows.</em></td>
    </tr>
    <tr>
        <td>Package manager</td>
        <td><a href="https://brew.sh/">Homebrew</a></td>
        <td>A package manager that allows you to install and manage the various command-line interface (CLI) tools used for contributing to Braze Docs.</td>
    </tr>
    <tr>
        <td>Ruby version manager</td>
        <td><a href="https://github.com/rbenv/rbenv#using-package-managers">rbenv</a></td>
        <td>A Ruby version manager that allows you to install and manage the required Ruby version for Braze Docs when you're setting up your local environment. If you'd like to use a different Ruby version manager, see <a href="https://www.ruby-lang.org/en/documentation/installation/#managers">Ruby's supported version managers</a>.</td>
    </tr>
    <tr>
        <td>GitHub UI tool</td>
        <td><a href="https://desktop.github.com/">GitHub Desktop</a></td>
        <td>Many of our recommendations for advanced contributors assume you will be using your terminal to handle Git workflows. If you prefer to simplify things, you can use GitHub Desktop to provide a UI for steps like checking out branches, making commits, and opening pull requests.</td>
    </tr>    
    <tr>
        <td>Text editor</td>
        <td><a href="https://code.visualstudio.com/download">Visual Studio Code (VS Code)</a></td>
        <td>A full-featured text editor by Microsoft that allows you to edit any file in the Braze Docs repository. To improve your experience, be sure to install the following plugins:
            <ul>
                <li><a href="https://marketplace.visualstudio.com/items?itemName=sissel.shopify-liquid">Liquid + Jekyll Linter</a></li>
                <li><a href="https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint">Markdown Linter</a></li>
                <li><a href="https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker">Spellchecker</a></li>
            </ul>
        </td>
    </tr>
    <tr>
        <td>Text editor</td>
        <td><a href="https://www.jetbrains.com/idea/download/">Intellij's IDEA Community Edition</a></td>
        <td>A full-featured text editor by Intellij that allows you to edit any file in the Braze Docs repository. To improve your experience, be sure to install the following plugins:
            <ul>
                <li><a href="https://plugins.jetbrains.com/plugin/7793-markdown">Markdown Linter</a></li>
                <li><a href="https://plugins.jetbrains.com/plugin/12175-grazie-lite">Spellchecker</a></li>
            </ul>
        </td>
    </tr>
</tbody>
</table>

{% alert note %}
As of writing, all software is free of cost. If you find that a product is no longer free, [please let us know](https://github.com/braze-inc/braze-docs/issues/new?assignees=&labels=issue&projects=&template=report_an_issue.md&title=).
{% endalert %}

## Step 2: Fork the repository

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

## Step 3: Install Ruby 

To build the docs locally, you'll need Ruby version `2.7.4` installed. In the terminal, open `braze-docs` and check for Ruby version `2.7.4`.

```bash
cd ~/braze-docs
ruby --version
```

If this version isn't installed, use a [supported version manager](https://www.ruby-lang.org/en/documentation/installation/#managers) to install Ruby version `2.7.4`. For example, using [rbenv](https://github.com/rbenv/rbenv):

```bash
rbenv install 2.7.4
```

## Step 4: Install dependencies

Next, install the dependencies for Braze Docs. These are small programs used to generate your local Braze Docs site.

```bash
bundle install
```

## Step 5: Start a local server

To generate the Braze Docs site and run it in a local server, first checkout your git branch.

```bash
rake
```

By default, Braze Docs will be generated on localhost [`http://127.0.0.1:4000`](http://127.0.0.1:4000). To access the site, open the link in your browser.

To stop your local server, reopen the terminal and press <kbd>Control</kbd> + <kbd>C</kbd>.
