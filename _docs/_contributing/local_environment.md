---
nav_title: Setting up environment
article_title: Setting up your local Braze Docs environment
description: "Learn how to set up your local Braze Docs environment, so you can make complex or multi-page changes."
page_order: 0.1 
noindex: true
---

# Setting up your local environment

> Learn how to set up your local Braze Docs environment, so you can make complex or multi-page changes.

{% multi_lang_include contributing/prerequisites.md %}

## Setting up your local environment

### Step 1: Get the required software

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
        <td>Tool manager</td>
        <td><a href="https://asdf-vm.com/guide/getting-started.html">asdf</a></td>
        <td>A tool manager for installing and switching between multiple versions of Node.js. You can install this <a href="#install-dependencies">during set up later</a>.</td>
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
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
As of writing, all software is free of cost. If you find that a product is no longer free, [please let us know](https://github.com/braze-inc/braze-docs/issues/new?assignees=&labels=issue&projects=&template=report_an_issue.md&title=).
{% endalert %}

### Step 2: Create an SSH key

Next, [create an SSH key](https://docs.github.com/en/enterprise-cloud@latest/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent) for your GitHub account. Note that if you're using [WSL](https://learn.microsoft.com/en-us/windows/wsl/install), be sure to follow the Linux instructions to create your SSH key.

### Step 3: Clone your forked repository

{% alert important %}
Double-check that you [forked the repository]({{site.baseurl}}/contributing/home/#step-3-fork-the-repository), before trying to clone it locally.
{% endalert %}

In GitHub, open your forked repository, then select **Code** > **SSH** > <i class="fa-regular fa-clone"></i> **Copy**.

![An example forked repository with the "Code" dropdown open showing the "Copy" option.]({% image_buster /assets/img/contributing/github/clone_the_fork.png %}){: style="max-width:50%;"}

In your terminal, open your home directory, then clone the Braze Docs repository.

```bash
cd ~
git clone git@github.com:braze-inc/braze-docs.git
```

### Step 4: Add a remote for `braze-inc/braze-docs`

To ensure that your changes are pushed to the official Braze Docs repository, instead of your fork, you'll need to set up a new remote in Git.

```bash
cd ~/braze-docs
git remote add upstream git@github.com:braze-inc/braze-docs.git
```

To verify that your new `upstream` remote was added successfully, list your remotes using the `remote` command's `-v` option.

```bash
$ git remote -v
origin    git@github.com:internetisaiah/braze-docs.git (fetch)
origin    git@github.com:internetisaiah/braze-docs.git (push)
upstream  git@github.com:braze-inc/braze-docs.git (fetch)
upstream  git@github.com:braze-inc/braze-docs.git (push)
```

### Step 5: Install Ruby

To [generate a local site preview]({{site.baseurl}}/contributing/generating_a_preview/), you'll need Ruby version `3.3.0` installed. In the terminal, open `braze-docs` and check for Ruby version `3.3.0`.

```bash
cd ~/braze-docs
ruby --version
```

If this version isn't installed, use a [supported version manager](https://www.ruby-lang.org/en/documentation/installation/#managers) to install Ruby version `3.3.0`. For example, using [rbenv](https://github.com/rbenv/rbenv):

```bash
rbenv install 3.3.0
```

### Step 6: Install dependencies {#install-dependencies}

If you have multiple versions of Node.js installed, use `asdf` for version management.

```bash
brew install asdf
```

Next, install the dependencies for Braze Docs. These are small programs used to generate your local Braze Docs site.

```bash
bundle install && asdf install
```

### Step 7: Start your local server

To verify your installation and start your local docs server on localhost `http://127.0.0.1:4000`, run:

```bash
# for 'en' language:
rake

# for other languages:
rake es
rake fr
rake ja
rake ko
rake pt_br
```

To stop your server, reopen the terminal and press **Control+C**.

## Next steps

If you're new to Git or docs-as-code, start with our tutorial: [Your first contribution]({{site.baseurl}}/contributing/your_first_contribution/). Otherwise, check out one of the following.

- [Content management]({{site.baseurl}}/contributing/content_management/)
- [YAML metadata]({{site.baseurl}}/contributing/yaml_front_matter/metadata/)
- [Generating a preview]({{site.baseurl}}/contributing/generating_a_preview/)
- [Style guides]({{site.baseurl}}/contributing/style_guide)
