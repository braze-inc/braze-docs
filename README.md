# Welcome to Braze Docs!

This repository contains the source files for [Braze Docs](http://www.braze.com/docs), which hosts all user, developer, partner, and API documentation for the Braze customer engagement platform.

## Quick start

> For a more in-depth guide, see [Contributing](./CONTRIBUTING.md).

To build the docs locally, you'll need to install a Ruby version between `2.7.4` and `2.7.8`. In your terminal, open `braze-docs` and check which Ruby version is currently installed.

```bash
cd ~/braze-docs
ruby --version
```

If none of these Ruby versions are installed, use a [supported version manager](https://www.ruby-lang.org/en/documentation/installation/#managers) to install Ruby version `2.7.8`. For example, if you're using [rbenv](https://github.com/rbenv/rbenv), your input will be similar to the following:

```bash
rbenv install 2.7.8
```

Next, set the local Ruby version for `braze-docs`. For example, if you're using [rbenv](https://github.com/rbenv/rbenv), your input will be similar to the following:

```bash
rbenv local 2.7.8
```

Next, install project dependencies.

```bash
bundle install
```

To start your local docs server on localhost `http://127.0.0.1:4000`, run:

```bash
rake
```

To stop your server, reopen your terminal and press **Control**+**C**.

## Open-source license

Braze Docs is licensed under a Creative Commons public license. For more information, see [LICENSE](./LICENSE).

![Licence Icon](https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png)

## Code of conduct

At Braze, we expect respectful behavior from both administrators and contributors. For more information, see [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md).

[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-v1.4%20adopted-ff69b4.svg)](./CODE_OF_CONDUCT.md)
