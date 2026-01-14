---
nav_title: Redirect URLs
article_title: Redirect URLs
description: "Learn how to redirect URLs for pages and page headings on Braze Docs."
page_order: 5
noindex: true
---

# Redirect URLs

> Learn how to redirect URLs for pages and page headings on Braze Docs. For general information about URLs, see [About content management]({{site.baseurl}}/contributing/content_management/#urls).

Page URLs always match the directory structure of the Braze Docs repository. When a Markdown file is renamed or moved to a different directory, the original URL will result in a 404 error if a redirect isn't set up.

![Example of a 404 page on Braze Docs.]({% image_buster /assets/img/contributing/styling_examples/404.png %})

By setting up URL redirects, you'll help prevent user bookmarks from breaking.

{% multi_lang_include contributing/prerequisites.md %}

## Redirecting a page

You can choose to redirect a page's URL to the Braze Docs home page or a new location.

{% tabs local %}
{% tab home page %}
Open the relevant Markdown file and add the following key-value pair to the YAML front matter. If there's already a `layout` key, replace the existing key with the new one.

```markdown
---
layout: blank_config
---
```

Your YAML front matter should be similar to the following:

```markdown
---
nav_title: Customization Guides
config_only: true
layout: blank_config
page_order: 3
---
```
{% endtab %}

{% tab new location %}
Move or rename the relevant Markdown file, then navigate to the `assets/js/` directory and open the global redirect file.

```bash
braze-docs
└── assets
    └── js
        └── broken_redirect_list.js
```

{% alert tip %}
If you don't plan on moving or renaming the file, you can also set up the redirect directly in your file's YAML front matter with [`layout: redirect`]({{site.baseur}}/contributing/yaml_front_matter/page_layouts/#redirect), instead of creating a new one in the global redirect file.
{% endalert %}

At the of the file, create a redirect on a new line using the following syntax:

```javascript
validurls['REDIRECT_FROM'] = 'REDIRECT_TO';
```

Replace the following:

| Placeholder     | Description                                                                                    |
|-----------------|------------------------------------------------------------------------------------------------|
| `REDIRECT_FROM` | The URL you want to redirect _from_ with `https://www.braze.com/` removed from the URL string. |
| `REDIRECT_TO`   | The URL you want to redirect _to_ with `https://www.braze.com/` removed from the URL string.   |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% multi_lang_include contributing/alerts/warning_urls_must_be_lowercase.md %}

Your redirect should be similar to the following:

```javascript
validurls['/docs/user_guide/data_and_analytics/engagement_reports'] = '/docs/user_guide/data_and_analytics/your_reports/engagement_reports';
```
{% endtab %}
{% endtabs %}

## Redirecting a heading

To redirect the URL for an in-page heading, you'll use the `local_redirect` key within the page's YAML front matter. First, move or rename the relevant Markdown file, the use the following syntax in the page's YAML front matter:

```
local_redirect:
  OLD_HEADING: 'NEW_HEADING_URL'
```

Replace the following:

| Placeholder       | Description                                                                                                                                   |
|-------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| `OLD_HEADING`     | The old heading in [Markdown syntax](https://www.markdownguide.org/basic-syntax/#an-example-putting-the-parts-together) with the `#` removed. |
| `NEW_HEADING_URL` | The new heading URL you want to redirect _to_ with `https://www.braze.com/` removed from the URL string.                                      |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% multi_lang_include contributing/alerts/warning_urls_must_be_lowercase.md %}

Your redirect should be similar to the following:

```yaml
---
nav_title: Getting started
article_title: Getting started with the Braze SDK
description: "If you're new to the Braze SDK, learn how to get started."
local_redirect:
  building-from-source: '/docs/developer_guide/getting_started/#using-our-install-script'
```

## Testing redirects

You can use [`bdocs`]({{site.baseurl}}/contributing/bdocs) to lists all of the old URLs you set up using a base URL of your choice.

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

{% alert tip %}
If you're using VS Code, hold **CMD** while right-clicking a link to open it in your default browser. Because these are the old links, they should all redirect to the new URL specified in the redirect file. If it doesn't, there's an issue with the redirect.
{% endalert %}

## Troubleshooting

{% multi_lang_include contributing/troubleshooting/redirects.md %}
