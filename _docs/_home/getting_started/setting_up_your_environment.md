---
nav_title: Setting up your environment
article_title: Setting up your environment
page_order: 1
noindex: true
---

# Setting up your environment

> TODO

## Before you start

You'll need to complete the following:

- [Download the recommended software]()
- [Create a GitHub account](https://github.com/join)
- Set up your GitHub SSH key:
  - [macOS](https://docs.github.com/en/github-ae@latest/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent?platform=mac)
  - [Windows](https://docs.github.com/en/github-ae@latest/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent?platform=windows)
  - [Linux](https://docs.github.com/en/github-ae@latest/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent?platform=linux)

## Install Ruby version `2.7.4`

To build the docs locally, you'll need Ruby version `2.7.4` installed. In the terminal, open `braze-docs` and check for Ruby version `2.7.4`.

```bash
cd ~/braze-docs
ruby --version
```

If it's not, use a [supported version manager](https://www.ruby-lang.org/en/documentation/installation/#managers) to install Ruby version `2.7.4`. For example, using [rbenv](https://github.com/rbenv/rbenv):

```bash
rbenv install 2.7.4
```

## Install Braze Docs dependencies

Next, install project dependencies.

```bash
./bundle install
```

## Starting the local server

To start your local docs server on localhost `http://127.0.0.1:4000`, run:

```bash
./rake
```

## Stopping the local server

To stop your server, reopen the terminal and press **Control**+**C**.
