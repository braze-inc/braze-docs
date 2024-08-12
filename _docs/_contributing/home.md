---
nav_title: Home
article: Contributing to Braze Docs
description: "Here's what you need to start contributing to Braze Docs!"
page_order: 0
search_tag: Contributing
---

# Contributing to Braze Docs

> Thanks for contributing to Braze Docs! Every Tuesday and Thursday, we merge community contributions and deploy them to Braze Docs. Use this guide to get your changes merged during our next deployment.

## Prerequisites

Some understanding of Git is required to contribute to Braze Docs. If you're new to Git and don't know where to start, see [Git Book: Getting Started](https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control). If you just need a refresher, see [Git and GitHub]({{site.baseurl}}/contributing/git_and_github/).

## Step 1: Sign the CLA

Everybody that contributes to Braze Docs must sign the [Contribution License Agreement (CLA)](https://www.braze.com/docs/cla). If you don't sign the CLA, the `@cla-bot` on GitHub will automatically block your pull request.

## Step 2: Set up your environment

Before you can make complex or multi-page changes to Braze Docs, you need to set up your local environment. However, small single-document changes can be completed [directly in GitHub]({{site.baseurl}}/contributing/your_first_contribution/?tab=github#step-2-make-a-change).

### Step 2.1: Get the required software

At a minimum, you need a terminal, a text editor, and a ruby version manager. If you're not sure where to start, see the following.

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
        <td>Git GUI</td>
        <td><a href="https://desktop.github.com/">GitHub Desktop</a></td>
        <td>A graphical user interface (GUI) you can use to run Git commands, instead of typing commands in the terminal.</td>
    </tr>    
    <tr>
        <td>Terminal</td>
        <td><a href="https://wezfurlong.org/wezterm/index.html">Wezterm</a></td>
        <td>A terminal emulator that allows you to run commands and interact with the Braze Docs repository from the commandline. If you're using a Windows operating system, you'll also need to install Windows Subsystem for Linux (WSL).</td>
    </tr>
    <tr>
        <td>Terminal extension</td>
        <td><a href="https://learn.microsoft.com/en-us/windows/wsl/install">Windows Subsystem for Linux (WSL)*</a></td>
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
        <td>A Ruby version manager that allows you to install and manage the required Ruby version for Braze Docs when you're setting up your local environment. To use a different Ruby version manager, see <a href="https://www.ruby-lang.org/en/documentation/installation/#managers">Ruby's supported version managers</a>.</td>
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
{: .reset-td-br-1 .reset-td-br-2}

{% alert note %}
As of writing, all software is free of cost. If you find that a product is no longer free, [please let us know](https://github.com/braze-inc/braze-docs/issues/new?assignees=&labels=issue&projects=&template=report_an_issue.md&title=).
{% endalert %}

### Step 2.2: Set up your GitHub account

Next, [create a GitHub account](https://github.com/join) and [set up your SSH key](https://docs.github.com/en/enterprise-cloud@latest/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent).

{% alert note %}
If you're using [WSL](https://learn.microsoft.com/en-us/windows/wsl/install), follow the Linux instructions to set up your SSH key.
{% endalert %}

### Step 2.3: Fork the repository

Open the [Braze Docs GitHub repository](https://github.com/braze-inc/braze-docs), then select **Fork**.

![The Braze Docs GitHub repository showing "Fork".]({% image_buster /assets/img/contributing/github/fork_the_repository.png %})

{% alert tip %}
For more information, see [GitHub: About forks](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/about-forks).
{% endalert %}

Keep the default settings, then select **Create fork**.

![The Braze Docs GitHub repository showing "Create fork".]({% image_buster /assets/img/contributing/github/create_a_new_fork.png %})

In your forked repository, select **Code** > **SSH** > <i class="fa-regular fa-clone"></i> **Copy**.

![An example forked repository with the "Code" dropdown open showing the "Copy" option.]({% image_buster /assets/img/contributing/github/clone_the_fork.png %}){: style="max-width:50%;"}

In your terminal, open your home directory, then clone the Braze Docs repository.

```bash
cd ~
git clone git@github.com:braze-inc/braze-docs.git
```

### Step 2.4: Install Ruby

To [generate a local site preview]({{site.baseurl}}/contributing/generating_a_preview/), you'll need Ruby version `3.3.0` installed. In the terminal, open `braze-docs` and check for Ruby version `3.3.0`.

```bash
cd ~/braze-docs
ruby --version
```

If this version isn't installed, use a [supported version manager](https://www.ruby-lang.org/en/documentation/installation/#managers) to install Ruby version `3.3.0`. For example, using [rbenv](https://github.com/rbenv/rbenv):

```bash
rbenv install 3.3.0
```

### Step 2.5: Install dependencies

Next, install the dependencies for Braze Docs. These are small programs used to generate your local Braze Docs site.

```bash
bundle install
```

## Next steps

If you're new to Git or docs-as-code, start with our tutorial: [Your first contribution]({{site.baseurl}}/contributing/your_first_contribution/). Otherwise, check out one of the following.

- [Content management]({{site.baseurl}}/contributing/content_management/)
- [YAML metadata]({{site.baseurl}}/contributing/yaml_front_matter/metadata/)
- [Generating a preview]({{site.baseurl}}/contributing/generating_a_preview/)
- [Style guides]({{site.baseurl}}/contributing/style_guide)
