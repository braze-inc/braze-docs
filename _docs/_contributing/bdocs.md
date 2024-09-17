---
nav_title: bdocs
article_title: bdocs
description: "Learn how to use `bdocs`, the Braze-Docs CLI tool, that helps you replace links, generate redirect URLs, generate deployment text, and more."
---

# bdocs

> Learn how to use `bdocs`, the Braze-Docs CLI tool, that helps you replace links, generate redirect URLs, generate deployment text, and more.

{% multi_lang_include contributing/prerequisites.md %}

## Quick start

To see the list of each command and a short definition, run:

```terminal
./bdocs
```

The following will be output to your terminal:

```terminal
bdocs is a CLI tool for executing Braze Docs scripts.

USUAGE:
  ./bdocs [option]

OPTIONS:
  deploy       Create the deploy body text for weekly deployments
  release      Create the release body text for monthly releases
  transform    Transform reference links to inline links on 1 or more pages
  clean        Remove reference links that are not being used on 1 or more pages
  redirects    List the old URLs for all new redirects in this branch
  help         Display this help message and exit
```

## Copying to your clipboard

If you're on MacOS, you can copy the output of a command directly to your clipboard by using the following command:

```terminal
./bdocs COMMAND | pbcopy
```

The `|` means to "pipe" (or send) the output of the first command to the next command. `pbcopy` means to write the output to your clipboard instead of the terminal. By combining these commands together, you are sending the output from `bdocs` to `pbcopy` using a pipe!

## List of commands

## deploy

`deploy` generates the PR body text for the Docs Team's weekly deployments by comparing which PRs have been merged into `develop`, but not `master`, then listing them in the proper Markdown format.

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

## release

`release` generates the PR body text for the Docs Team's monthly releases by comparing which PRs have been merged into `master` since the last release, then listing them in the proper Markdown format.

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
...
```
{% endtab %}
{% endtabs %}

## transform

Reference-style links are not supported within Liquid `{% raw %}{% tab %}{% endraw %}` tags. `transform` removes all the reference-style links on a file and replaces them with [in-line links]({{site.baseurl}}/contributing/content_management/cross_referencing)--whether it be a normal URL, a `{% raw %}{{site.baseurl}}{% endraw %}`, an image, or other link. `transform` can take a single file or an entire directory as an argument.

{% alert note %}
By default, after you run `transform`, `bdocs` will ask if you want to run `clean` next.
{% endalert %}

{% tabs local %}
{% tab usage example %}
{% subtabs local %}
{% subtab single file %}
```terminal
$ ./bdocs transform _docs/_user_guide/onboarding_faq.md
```

Heres a page:

```
content...
```
{% endsubtab %}

{% subtab directory %}
```terminal
$ ./bdocs transform _docs/_user_guide/*
```

Page 1:

```
content...
```

Page 2:

```
content...
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## clean

`clean` removes any unused reference links from the bottom of a Markdown file. It can take a single file or an entire directory as an argument.

{% alert note %}
By default, after you run `transform`, `bdocs` will ask if you want to run `clean` next.
{% endalert %}

{% tabs local %}
{% tab usage example %}
{% subtabs local %}
{% subtab single file %}
```terminal
$ ./bdocs clean _docs/_user_guide/onboarding_faq.md
```

Heres a page:

```
content...
```
{% endsubtab %}

{% subtab directory %}
```terminal
$ ./bdocs clean _docs/_user_guide/*
```

Page 1:

```
content...
```

Page 2:

```
content...
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## redirects

`redirects` checks if any new redirects has been added to [`broken_redirect_list.js`](https://github.com/braze-inc/braze-docs/blob/develop/assets/js/broken_redirect_list.js), then lists all of the old URLs using a base URL of your choice.

{% tabs local %}
{% tab usage example %}
The following example uses the [Sage AI rebrand PR](https://github.com/braze-inc/braze-docs/pull/8040).

```terminal
$ git checkout bd-3442
$ ./bdocs redirects

Which base URL would you like to use? Note: You can use a local or deployment base URL.

$ https://braze-docs-gtcavota9-braze.vercel.app/

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
https://braze-docs-gtcavota9-braze.vercel.app/docs/user_guide/sage_ai/predictive_suite/predictive_events/messaging_users/
https://braze-docs-gtcavota9-braze.vercel.app/docs/user_guide/sage_ai/intelligence/
https://braze-docs-gtcavota9-braze.vercel.app/docs/user_guide/sage_ai/intelligence/intelligent_channel/
https://braze-docs-gtcavota9-braze.vercel.app/docs/user_guide/sage_ai/intelligence/intelligent_selection/
https://braze-docs-gtcavota9-braze.vercel.app/docs/user_guide/sage_ai/intelligence/intelligent_timing/
https://braze-docs-gtcavota9-braze.vercel.app/docs/user_guide/sage_ai/intelligence/faqs
https://braze-docs-gtcavota9-braze.vercel.app/docs/user_guide/sage_ai/recommendations/
https://braze-docs-gtcavota9-braze.vercel.app/docs/user_guide/sage_ai/recommendations/about_item_recommendations/
https://braze-docs-gtcavota9-braze.vercel.app/docs/user_guide/sage_ai/recommendations/ai_item_recommendations/
https://braze-docs-gtcavota9-braze.vercel.app/docs/user_guide/sage_ai/recommendations/rules_based_recommendations/
https://braze-docs-gtcavota9-braze.vercel.app/docs/user_guide/sage_ai/generative_ai
https://braze-docs-gtcavota9-braze.vercel.app/docs/user_guide/sage_ai/generative_ai/ai_copywriting/
https://braze-docs-gtcavota9-braze.vercel.app/docs/user_guide/sage_ai/generative_ai/ai_copywriting/brand_guidelines/
https://braze-docs-gtcavota9-braze.vercel.app/docs/user_guide/sage_ai/generative_ai/ai_liquid/
https://braze-docs-gtcavota9-braze.vercel.app/docs/user_guide/sage_ai/generative_ai/ai_content_qa/
```
{% endtab %}
{% endtabs %}

{% alert tip %}
If you're using VS Code, hold **CMD** while right-clicking a link to open it into your default browser. Because these are the old links, they should all redirect to the new URL specified in the redirect file. If it doesn't, there's an issue with the redirect.
{% endalert %}
