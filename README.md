# Welcome to Braze Docs!

This repository contains the source files for [Braze Docs](http://www.braze.com/docs), which hosts all user, developer, partner, and API documentation for the Braze customer engagement platform.

If you'd like to help improve the docs, you can:

- [Report an issue](https://github.com/braze-inc/braze-docs/issues/new?assignees=&labels=issue&projects=&template=report_an_issue.md&title=)
- [Request a feature](https://github.com/braze-inc/braze-docs/issues/new?assignees=&labels=enhancement&projects=&template=request_a_feature.md&title=)
- [Contribute](https://www.braze.com/docs/contributing/home)

## Quick start

> **Note:** For a full walkthrough, see [Contributing to Braze Docs](https://www.braze.com/docs/contributing/home/).

To build the docs locally, you'll need Ruby version `3.3.0` installed. In the terminal, open `braze-docs` and check for Ruby version `3.3.0`.

```bash
cd ~/braze-docs
ruby --version
```

If this version isn't installed, use a [supported version manager](https://www.ruby-lang.org/en/documentation/installation/#managers) to install it. For example, using [rbenv](https://github.com/rbenv/rbenv):

```bash
rbenv install 3.3.0
```

Next, install project dependencies.

```bash
bundle install
```

To start your local docs server on localhost `http://127.0.0.1:4000`, run:

```bash
# for 'en' language:
rake

# for other langauges:
rake es
rake fr
rake ja
rake ko
rake pt_br
```

To stop your server, reopen the terminal and press **Control**+**C**.

## About `bdocs` wrapper

[`bdocs`](https://github.com/braze-inc/braze-docs/blob/develop/bdocs) is a wrapper script located in the root of this repository that helps you replace links, generate redirect URLs, create deployment descriptions, and more. For an in-depth walkthrough, see [`bdocs` wrapper](https://www.braze.com/docs/contributing/bdocs/). To get started quickly, run the following command to see a list of available commands:

```terminal
./bdocs
```

## Creative Commons license

Braze Docs is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. For more information, see [LICENSE](./LICENSE).

![Licence Icon](https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png)

## Code of conduct

At Braze, we expect respectful behavior from both administrators and contributors. For more information, see [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md).

[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-v1.4%20adopted-ff69b4.svg)](CODE_OF_CONDUCT.md)
