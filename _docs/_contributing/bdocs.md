---
nav_title: About bdocs wrapper
article_title: About bdocs wrapper
description: "Learn how to use bdocs, the Braze-Docs CLI tool, that helps you replace links, generate redirect URLs, generate deployment text, and more."
page_order: 8.5
---

# About `bdocs` wrapper

> [`bdocs`](https://github.com/braze-inc/braze-docs/blob/develop/bdocs) is a wrapper script located in the root of the Braze Docs repository that helps you replace links, generate redirect URLs, create deployment descriptions, and more.

{% multi_lang_include contributing/prerequisites.md %}

## Using `bdocs`

To run a command, use the following syntax. Replace `COMMAND` with one of the [available commands](#list-of-commands).

```bash
./bdocs COMMAND
```

To see the list of commands in your terminal, use the `help` command:

```bash
$ ./bdocs help

bdocs is a CLI tool for executing Braze Docs scripts.

USAGE:
  ./bdocs [option]

OPTIONS:
  deploy         Create the deploy body text for weekly deployments
  release        Create the release body text for monthly releases
  tlinks         Transform reference links to inline links on 1 or more pages
  rlinks         Remove unused reference links on 1 or more pages
  ulinks         Update old links using newest redirect on 1 or more pages
  mredirects     Make redirects for all renamed files in this branch
  fblinks        Finds broken links throughout the docs site
  lredirects     Test new redirects by listing old URLs in this branch
  syntax         Print all unique Markdown syntax supported by Braze Docs
  help           Display this help message and exit
```

## Copying to your clipboard

If you're on MacOS, you can copy the output of `bdocs` directly to your clipboard by using the following command. The `|` means to "pipe" (or send) the output of the first command to the next command. `pbcopy` means to write the output to your clipboard instead of the terminal. By combining these commands, you're sending the output from `bdocs` to `pbcopy` using a pipe.

```bash
./bdocs COMMAND | pbcopy
```

## List of commands

### `deploy`

This command creates the pull request description for weekly deployments by comparing which pull requests have been merged into `develop` but not `main` and then listing them in the proper Markdown format.

{% tabs local %}
{% tab usage example %}
```bash
$ ./bdocs deploy

- [#6980](https://github.com/braze-inc/braze-docs/pull/6980) - Update index.md
- [#6981](https://github.com/braze-inc/braze-docs/pull/6981) - Update ab_test_projection.md
- [#6983](https://github.com/braze-inc/braze-docs/pull/6983) - Add Show archived content
```
{% endtab %}
{% endtabs %}

### `release`

This command creates the pull request description for monthly releases by comparing which pull requests have been merged into `main` since the last release and then listing them in the proper Markdown format.

{% tabs local %}
{% tab usage example %}
```bash
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

{% alert note %}
After you run `tlinks`, [`rlinks`](#rlinks) will be automatically run against the same file or directory.
{% endalert %}

{% tabs local %}
{% tab usage example %}
#### Example command

```bash
./bdocs tlinks _docs/_user_guide/onboarding_faq.md
```

#### Example page: Before

{% raw %}
```markdown
Before continuing, [create your SSH token][2]. When you're finished, see [Step 2: Uploading your token][5].

[2]: {{site.baseurl}}/developer_guide/platform_wide/sdk_authentication/
[5]: https://www.apple.com/swift#step-2-uploading-your-token
```
{% endraw %}

#### Example page: After

{% raw %}
```markdown
Before continuing, [create your SSH token]({{site.baseurl}}/developer_guide/authentication/). When you're finished, see [Step 2: Uploading your token](https://www.apple.com/swift#step-2-uploading-your-token).

[2]: {{site.baseurl}}/developer_guide/platform_wide/sdk_authentication/
[5]: https://www.apple.com/swift#step-2-uploading-your-token
```
{% endraw %}
{% endtab %}
{% endtabs %}

### `rlinks`

`rlinks` (short for "remove links") removes any unused reference links from the bottom of a Markdown file. This command takes a single file or an entire directory as an argument.

{% alert note %}
After you run `tlinks`, `rlinks` will be automatically run against the same file or directory.
{% endalert %}

{% tabs local %}
{% tab usage example %}
#### Example command

```bash
./bdocs rlinks _docs/_user_guide/onboarding_faq.md
```

#### Example page: Before

{% raw %}
```markdown
Before continuing, [create your SSH token]({{site.baseurl}}/developer_guide/authentication/). When you're finished, see [Step 2: Uploading your token](https://www.apple.com/swift#step-2-uploading-your-token).

[2]: {{site.baseurl}}/developer_guide/platform_wide/sdk_authentication/
[5]: https://www.apple.com/swift#step-2-uploading-your-token
```
{% endraw %}

#### Example page: After

{% raw %}
```markdown
Before continuing, [create your SSH token]({{site.baseurl}}/developer_guide/authentication/). When you're finished, see [Step 2: Uploading your token](https://www.apple.com/swift#step-2-uploading-your-token).

```
{% endraw %}
{% endtab %}
{% endtabs %}

### `ulinks`

`ulinks` (short for "update links") takes a file or directory and updates any old links listed on [`broken_redirect_list.js`](https://github.com/braze-inc/braze-docs/blob/develop/assets/js/broken_redirect_list.js) with the newest possible link. For example, if link `one` redirects to link `two`, and link `two` redirects to link `three`, `ulinks` will replace both link `one` and link `two` with link `three`. This command only updates links starting with {% raw %}`{{site.baseurl}}`{% endraw %}.

{% tabs local %}
{% tab usage example %}
#### Example command

```bash
$ ./bdocs ulinks _docs/_developer_guide/content_cards/creating_custom_content_cards.md
Made 1 replacements in _docs/_developer_guide/content_cards/creating_custom_content_cards.md
Total replacements made: 1
```

#### Example page: Before

{% raw %}
```markdown
Learn how to [log analytics]({{site.baseurl}}/developer_guides/android/content_cards/logging_analytics/) for your custom Content Cards.
```
{% endraw %}

#### Example page: After

{% raw %}
```markdown
Learn how to [log analytics]({{site.baseurl}}/developer_guides/content_cards/analytics/) for your custom Content Cards.
```
{% endraw %}
{% endtab %}
{% endtabs %}

#### Why you should update old links

Ideally, redirects added to [`assets/js/broken_redirect_list.js`](https://github.com/braze-inc/braze-docs/blob/develop/assets/js/broken_redirect_list.js) should only be used to:

- Redirect traffic from outside of Braze Docs to the correct content (such as those coming from Stack Overflow, [Braze Learning](https://learning.braze.com/), the [Braze Blog](https://www.braze.com/resources/articles), and similar).
- Prevent existing bookmarks from breaking.

It should not be used to redirect URLs on an existing Braze Docs page to another existing Braze Docs page. Instead, these URLs should be updated with the newest possible link. We want to avoid cases in which someone reading an existing Braze Docs page clicks a link and is redirected from one page, to another page, to another page, and so on. `ulinks` helps solves this issue, improving the end-user experience.

### `mredirects`

`mredirects` (short for "make redirects") checks for renamed files committed in the current branch, then creates [URL redirects]({{site.baseurl}}/contributing/content_management/redirecting_urls/) in `assets/js/broken_redirect_list.js` for each renamed file.

Because it relies on `git diff` to check for renamed files, redirects are only created for committed files in the following scenarios:

|Scenario|Example|
|--------|-------|
|The file was renamed.|Renaming `developer_guide.md` to `dev_references.md`|
|A directory in a file's path was renamed.| Renaming `_docs/developer_guide/home.md` to `_docs/dev_reference/home.md`|
|The file was moved to a new directory.|Moving `_docs/developer_guide/home.md` into `_docs/developer_guide/getting_started/`|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% tabs local %}
{% tab usage example %}
#### Example command

```bash
$ ./bdocs mredirects                           
Redirects created successfully!
```

#### Example redirect file

```js
validurls['/docs/partners/message_personalization/dynamic_content/niftyimages'] = '/docs/partners/message_personalization/dynamic_content/visual_and_interactive_content/niftyimages';
validurls['/docs/partners/message_personalization/dynamic_content/movable_ink'] = '/docs/partners/message_personalization/dynamic_content/visual_and_interactive_content/movable_ink';
validurls['/docs/partners/message_personalization/dynamic_content/offerfit'] = '/docs/partners/message_personalization/dynamic_content/content_optimization_testing/offerfit';
validurls['/docs/partners/message_personalization/dynamic_content/stylitics'] = '/docs/partners/message_personalization/dynamic_content/visual_and_interactive_content/stylitics';
validurls['/docs/partners/data_and_infrastructure_agility/customer_data_platform/jebbit'] = '/docs/partners/additional_channels_and_extensions/extensions/surveys/jebbit';
validurls['/docs/partners/message_personalization/dynamic_content/judo/'] = '/docs/partners/message_personalization/dynamic_content/visual_and_interactive_content/judo/';
```
{% endtab %}
{% endtabs %}

### `fblinks`

`fblinks` (short for "find broken links") checks each file in the `_docs` directory for links that lead to a 404 page. Each broken link is written to a `.csv` file that you can import to Google Sheets.

#### Requirements

To use `fblinks`, you'll need to install the dependencies using `yarn`. This only needs to be done a single time. To install dependencies, run:

```bash
cd ~/braze-docs
brew install node yarn
yarn install
```

{% tabs local %}
{% tab usage example %}
#### Example command

```bash
$ ./bdocs fblinks                           
59 broken links were found. The full list can be found at:
  /Users/Alex.Lee/braze-docs/scripts/temp/broken-links.csv
```

{% alert tip %}
If you're using VS Code, hold <kbd>Command</kbd>, then <kbd>Left-Click</kbd> the link to open the CSV file in a new tab.
{% endalert %}

#### Example CSV file

```plaintext
File,Broken Link,Path to Broken Link
/Users/Alex.Lee/braze-docs/_docs/_api/api_limits.md,/docs/api/endpoints/email/bounce/remove,/Users/Alex.Lee/braze-docs/_docs/_api/endpoints/email/bounce/remove.md
/Users/Alex.Lee/braze-docs/_docs/_api/endpoints/messaging.md,/docs/docs/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/,/Users/Alex.Lee/braze-docs/_docs/_docs/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery.md
/Users/Alex.Lee/braze-docs/_docs/_contributing/bdocs.md,/docs/resources/articles,/Users/Alex.Lee/braze-docs/_docs/_resources/articles.md
```
{% endtab %}
{% endtabs %}

### `lredirects`

`lredirects` (short for "list redirects") checks if any new redirects have been added to [`broken_redirect_list.js`](https://github.com/braze-inc/braze-docs/blob/develop/assets/js/broken_redirect_list.js), then lists all of the old URLs using a base URL of your choice. For more general information, see [Redirecting URLs]({{site.baseurl}}/contributing/content_management/redirecting_urls).

{% alert tip %}
If you're using VS Code, hold <kbd>Command</kbd>, then <kbd>Left-Click</kbd> a link to open it in your default browser. Because these are the old links, they should all redirect to the new URL specified in the redirect file. If it doesn't, there's an issue with the redirect.
{% endalert %}

{% tabs local %}
{% tab usage example %}
The following example uses the [Sage AI rebrand PR](https://github.com/braze-inc/braze-docs/pull/8040).

```bash
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

### `syntax`

`syntax` prints all the unique Braze Docs syntax to the terminal. Keep in mind, this doesn't include any standard Markdown syntax, only _unique_ syntax. This is helpful for two reasons:

1. You no longer need to leave your text-editor to verify the syntax of a unique Braze Markdown implementation.
2. Even if you're offline, you can easily review the unique Braze Docs syntax&#8212;making it easier when working on airplane mode.

{% tabs local %}
{% tab usage example %}
{% raw %}
<pre style="font-family: 'Roboto Mono', monospace; font-size: 14px; line-height: 16px; background-color: #f4f4f7; color: #666666; padding: 10px; overflow-x: auto; white-space: pre; word-break: inherit; word-wrap: inherit; min-height: 36px;">
$ ./bdocs syntax
This is all of the unique Markdown syntax supported by Braze Docs.

ALERTS
  {% alert TYPE %}
  {% endalert %}

IMAGE LINK
  ![ALT_TEXT.]({% image_buster /assets/img/DIRECTORY/IMAGE.png %})

IMAGE RESIZING
  {: style="max-width:NUMBER%;"}

INCLUDES
  {% multi_lang_include PATH_TO_INCLUDE %}

LIQUID RAW TAGS
  &#123;% raw %}&#123;% endraw %}

TABS
  {% tabs %}
  {% tab NAME %}
  {% endtab %}
  {% endtabs %}

SUBTABS
  {% subtabs %}
  {% subtab NAME %}
  {% endsubtab %}
  {% endsubtabs %}

TABLE WORD-BREAK
  {: .reset-td-br-NUM .reset-td-br-NUM .reset-td-br-NUM .reset-td-br-NUM role="presentation"}
</pre>
{% endraw %}
{% endtab %}
{% endtabs %}
