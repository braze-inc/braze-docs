---
nav_title: About bdocs Wrapper
article_title: About `bdocs` Wrapper
description: "Learn how to use `bdocs`, the Braze-Docs CLI tool, that helps you replace links, generate redirect URLs, generate deployment text, and more."
page_order: 8.5
---

# About `bdocs` wrapper

> [`bdocs`](https://github.com/braze-inc/braze-docs/blob/develop/bdocs) is a wrapper script located in the root of the Braze Docs repository that helps you replace links, generate redirect URLs, create deployment descriptions, and more.

{% multi_lang_include contributing/prerequisites.md %}

## Using `bdocs`

To run a command, use the following syntax. Replace `COMMAND` with one of the [available commands](#list-of-commands).

```terminal
./bdocs COMMAND
```

To see the list of commands in your terminal, use the `help` command:

```terminal
$ ./bdocs help

bdocs is a CLI tool for executing Braze Docs scripts.

USAGE:
  ./bdocs [option]

OPTIONS:
  deploy       Create the deploy body text for weekly deployments
  release      Create the release body text for monthly releases
  tlinks       Transform reference links to inline links on 1 or more pages
  rlinks       Remove reference links that are not being used on 1 or more pages
  redirects    List the old URLs for all new redirects in this branch
  help         Display this help message and exit
```



## Copying to your clipboard

If you're on MacOS, you can copy the output of a command directly to your clipboard by using the following command. The `|` means to "pipe" (or send) the output of the first command to the next command. `pbcopy` means to write the output to your clipboard instead of the terminal. By combining these commands, you're sending the output from `bdocs` to `pbcopy` using a pipe.

```terminal
./bdocs COMMAND | pbcopy
```

## List of commands

### `deploy`

This command creates the pull request description for weekly deployments by comparing which pull requests have been merged into `develop` (but not `master`) and then listing them in the proper Markdown format.

{% tabs local %}
{% tab usage example %}
```terminal
$ ./bdocs deploy

- [#6980](https://github.com/braze-inc/braze-docs/pull/6980) - Update index.md
- [#6981](https://github.com/braze-inc/braze-docs/pull/6981) - Update ab_test_projection.md
- [#6983](https://github.com/braze-inc/braze-docs/pull/6983) - Add Show archived content
```
{% endtab %}
{% endtabs %}

### `release`

This command creates the pull request description for monthly releases by comparing which pull requests have been merged into `master` since the last release and then listing them in the proper Markdown format.

{% tabs local %}
{% tab usage example %}
```terminal
$ ./bdocs release

## Deploy - September 17, 2024

- https://github.com/braze-inc/braze-docs/pull/8104 - Deploy - September 17, 2024
- https://github.com/braze-inc/braze-docs/pull/8039 - Add Trending item recommendations
- https://github.com/braze-inc/braze-docs/pull/8073 - Add dynamic images to WhatsApp
- https://github.com/braze-inc/braze-docs/pull/8069 - Response messages GA

## Leftover deploy - September 12, 2024

- https://github.com/braze-inc/braze-docs/pull/8045 - Add list of security events that are reported
- https://github.com/braze-inc/braze-docs/pull/8047 - -2 Add sentence to security event report download
- https://github.com/braze-inc/braze-docs/pull/8048 - SessionM Partnership Doc
- https://github.com/braze-inc/braze-docs/pull/8051 - File file_storage_integrations.md committed.
```
{% endtab %}
{% endtabs %}

### `tlinks`

Reference-style links are not supported within Liquid `{% raw %}{% tab %}{% endraw %}` tags. `tlinks` (short for "transform links") transforms all the reference-style links on a file into [in-line links]({{site.baseurl}}/contributing/content_management/cross_referencing)&#8212;whether it be a normal URL, a `{% raw %}{{site.baseurl}}{% endraw %}`, an image, or other link. This command takes a single file or an entire directory as an argument.

{% alert tip %}
After you run `tlinks`, you'll be asked if you'd like to run [`rlinks`](#rlinks) next.
{% endalert %}

{% tabs local %}
{% tab usage example %}
#### Example command

```terminal
./bdocs tlinks _docs/_user_guide/onboarding_faq.md
```

#### Example page: before

{% raw %}
```markdown
Before continuing, [create your SSH token][2]. When you're finished, see [Step 2: Uploading your token][5].

[2]: {{site.baseurl}}/developer_guide/platform_wide/sdk_authentication/
[5]: https://www.apple.com/swift#step-2-uploading-your-token
```
{% endraw %}

#### Example page: after

{% raw %}
```markdown
Before continuing, [create your SSH token]({{site.baseurl}}/developer_guide/platform_wide/sdk_authentication/). When you're finished, see [Step 2: Uploading your token](https://www.apple.com/swift#step-2-uploading-your-token).

[2]: {{site.baseurl}}/developer_guide/platform_wide/sdk_authentication/
[5]: https://www.apple.com/swift#step-2-uploading-your-token
```
{% endraw %}
{% endtab %}
{% endtabs %}

### `rlinks`

`rlinks` (short for "remove links") removes any unused reference links from the bottom of a Markdown file. This command takes a single file or an entire directory as an argument.

{% alert note %}
After you run `tlinks`, you'll be asked if you'd like to run `rlinks` next.
{% endalert %}

{% tabs local %}
{% tab usage example %}
#### Example command

```terminal
./bdocs rlinks _docs/_user_guide/onboarding_faq.md
```

#### Example page: before

{% raw %}
```markdown
Before continuing, [create your SSH token]({{site.baseurl}}/developer_guide/platform_wide/sdk_authentication/). When you're finished, see [Step 2: Uploading your token](https://www.apple.com/swift#step-2-uploading-your-token).

[2]: {{site.baseurl}}/developer_guide/platform_wide/sdk_authentication/
[5]: https://www.apple.com/swift#step-2-uploading-your-token
```
{% endraw %}

#### Example Page: After

{% raw %}
```markdown
Before continuing, [create your SSH token]({{site.baseurl}}/developer_guide/platform_wide/sdk_authentication/). When you're finished, see [Step 2: Uploading your token](https://www.apple.com/swift#step-2-uploading-your-token).

```
{% endraw %}
{% endtab %}
{% endtabs %}

### `redirects`

This command checks if any new redirects have been added to [`broken_redirect_list.js`](https://github.com/braze-inc/braze-docs/blob/develop/assets/js/broken_redirect_list.js), then lists all of the old URLs using a base URL of your choice.

{% alert tip %}
If you're using VS Code, hold **CMD** while right-clicking a link to open it in your default browser. Because these are the old links, they should all redirect to the new URL specified in the redirect file. If it doesn't, there's an issue with the redirect.
{% endalert %}

{% tabs local %}
{% tab usage example %}
The following example uses the [Sage AI rebrand PR](https://github.com/braze-inc/braze-docs/pull/8040).

```terminal
$ git checkout bd-3442
$ ./bdocs redirects https://braze-docs-gtcavota9-braze.vercel.app/

https://braze-docs-gtcavota9-braze.vercel.app/docs/user_guide/sage_ai/
https://braze-docs-gtcavota9-braze.vercel.app/docs/user_guide/sage_ai/predictive_suite/
https://braze-docs-gtcavota9-braze.vercel.app/docs/user_guide/sage_ai/predictive_suite/predictive_churn
https://braze-docs-gtcavota9-braze.vercel.app/docs/user_guide/sage_ai/predictive_suite/predictive_churn/creating_a_churn_prediction/
https://braze-docs-gtcavota9-braze.vercel.app/docs/user_guide/sage_ai/predictive_suite/predictive_churn/prediction_analytics/
https://braze-docs-gtcavota9-braze.vercel.app/docs/user_guide/sage_ai/predictive_suite/predictive_churn/prediction_analytics/prediction_quality/
https://braze-docs-gtcavota9-braze.vercel.app/docs/user_guide/sage_ai/predictive_suite/predictive_churn/messaging_users/
https://braze-docs-gtcavota9-braze.vercel.app/docs/user_guide/sage_ai/predictive_suite/predictive_churn/prediction_faq/
https://braze-docs-gtcavota9-braze.vercel.app/docs/user_guide/sage_ai/predictive_suite/predictive_events/
https://braze-docs-gtcavota9-braze.vercel.app/docs/user_guide/sage_ai/predictive_suite/predictive_events/creating_an_event_prediction/
https://braze-docs-gtcavota9-braze.vercel.app/docs/user_guide/sage_ai/predictive_suite/predictive_events/prediction_analytics/
```
{% endtab %}
{% endtabs %}
