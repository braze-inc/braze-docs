<img src="assets/Braze_Primary_Icon_PURPLE.png" width="65" height="65" alt="Braze icon" align="left"/>

Welcome to Braze Docs!
===

[![Static Badge](https://img.shields.io/badge/License-Creative_Commons-lightgrey)](/LICENSE.md)
[![X (formerly Twitter) Follow](https://img.shields.io/twitter/follow/braze)](https://x.com/braze)

[Releases](https://github.com/braze-inc/braze-docs/releases) · [Deployments](https://github.com/braze-inc/braze-docs/deployments)

This repository contains the source files for [Braze Docs](http://www.braze.com/docs), which hosts all user, developer, partner, and API documentation for the Braze customer engagement platform.

If you'd like to help improve the docs, you can:

- [Submit a request](https://www.braze.com/docs/request) or ask in [#ask-docs](https://braze.enterprise.slack.com/archives/C0D10FTGQ) on Slack
- [Contribute](.github/CONTRIBUTING.md) (see [docs/contributing/README.md](docs/contributing/README.md) for the full handbook)

## Quick start

> [!TIP]
> For a full walkthrough, see [Contributing to Braze Docs](docs/contributing/README.md).

To build the docs locally, you'll need Ruby version `3.3.0` installed. In the terminal, open `braze-docs` and check for Ruby version `3.3.0`.

```bash
cd ~/braze-docs
ruby --version
```

If this version isn't installed, use a [supported version manager](https://www.ruby-lang.org/en/documentation/installation/#managers) to install it. For example, using [rbenv](https://github.com/rbenv/rbenv):

```bash
rbenv install 3.3.0
```

If you have multiple versions of Node.js installed, use `asdf` for version management.

```bash
brew install asdf
```

Next, install project dependencies.

```bash
bundle install && asdf install
```

To start your local docs server on localhost `http://127.0.0.1:4000`, run the following command. To stop your server, reopen the terminal and press **Control**+**C**.

```bash
# for 'en' language:
rake

# for other languages:
rake de
rake es
rake fr
rake ja
rake ko
rake pt_br

# to render content in '{% markdown_embed %}' tags:
MARKDOWN_API=true rake

# to render tiles on partner landing pages:
PARTNER_API=true rake

# to render both APIs:
MARKDOWN_API=true PARTNER_API=true rake
```

> [!NOTE]
> Prepending `MARKDOWN_API=true` to your rake command lets you preview content within a `{% markdown_embed %}` tag, such as the content on the [Developer Guide: Changelogs](https://www.braze.com/docs/developer_guide/changelogs/) page. Prepending `PARTNER_API=true` lets you render the tiles on a partner landing page, such as [Technology Partners](https://www.braze.com/docs/partners/home/).

## About `bdocs` wrapper

[`bdocs`](https://github.com/braze-inc/braze-docs/blob/develop/bdocs) is a wrapper script located in the root of this repository that helps you replace links, generate redirect URLs, create deployment descriptions, and more. For an in-depth walkthrough, see [`bdocs` wrapper](docs/contributing/bdocs.md). To get started quickly, run the following command to see a list of available commands:

```terminal
./bdocs
```

## Creative Commons license

Braze Docs is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. For more information, see [LICENSE](./LICENSE).

![Licence Icon](https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png)

## Code of conduct

At Braze, we expect respectful behavior from both administrators and contributors. For more information, see [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md).

[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-v1.4%20adopted-ff69b4.svg)](CODE_OF_CONDUCT.md)
