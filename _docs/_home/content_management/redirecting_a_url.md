---
nav_title: Redirecting a URL
page_order: 5
noindex: true
---

# Redirecting a URL

> Learn how to redirect URLs for pages on Braze Docs.

Page URLs always match the directory structure of the Braze Docs repository. When a Markdown file is renamed or moved to a different directory, the original URL will result in a 404 error if a redirect isn't set up.

![]()

By setting up URL redirects, you'll help prevent bookmarks from breaking for Braze Docs users.

{% multi_lang_include contributing/general_getting_started.md %}

## Setting up a page redirect

When redirecting an entire page, you can either set up the redirect using the global redirect file or the in-page YAML front matter.

{% tabs %}
{% tab global redirect (recommended) %}
Open your text editor, then find the page's Markdown file and move or rename the file as needed.

![]()

{% multi_lang_include contributing/alerts/tip_locating_a_file.md %}

Navigate to the `assets/js/` directory, then open the global redirect file: `broken_redirect_list.js`.

![]()

At the bottom of the file, set up your redirect on a newline.

```javascript
validurls['REDIRECT_FROM'] = 'REDIRECT_TO';
```

Replace the following:

| Placeholder     | Description                                                                                    |
|-----------------|------------------------------------------------------------------------------------------------|
| `REDIRECT_FROM` | The URL you want to redirect _from_ with `https://www.braze.com/` removed from the URL string. |
| `REDIRECT_TO`   | The URL you want to redirect _to_ with `https://www.braze.com/` removed from the URL string.   |

Your redirect should be similar to the following:

```javascript
validurls['/docs/user_guide/data_and_analytics/engagement_reports'] = '/docs/user_guide/data_and_analytics/your_reports/engagement_reports';
```
{% endtab %}
{% tab in-page redirect %}
When using an in-page redirect, you will _not_ rename the Markdown file. Instead, find the page's Markdown file and open it in your text editor.

![]()

{% multi_lang_include contributing/alerts/tip_locating_a_file.md %}

In the page's YAML front matter, set up your redirect.

```yaml
layout: redirect
redirect_to: NEW_URL
```

Replace `NEW_URL` with the new URL you want to redirect _to_ and remove `https://www.braze.com/` from the URL string. Your redirect should be similar to the following:

```yaml
---
nav_title: Getting started
article_title: Getting started with the Braze SDK
description: "If you're new to the Braze SDK, learn how to get started."
layout: redirect
redirect_to: /docs/developer_guide/getting_started/
---
```
{% endtab %}
{% endtabs %}

## Setting up a heading redirect

To redirect the URL for a page's heading, you'll use the `local_redirect` key within the page's YAML front matter. First, find the page's Markdown file, then open it in your text editor and rename the relevant heading.

![]()

{% multi_lang_include contributing/alerts/tip_locating_a_file.md %}

In the page's YAML front matter, set up the redirect.

```
local_redirect:
  OLD_HEADING: 'NEW_URL'
```

Replace the following:

| Placeholder       | Description                                                                                                                                   |
|-------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| `OLD_HEADING`     | The old heading in [Markdown syntax](https://www.markdownguide.org/basic-syntax/#an-example-putting-the-parts-together) with the `#` removed. |
| `NEW_HEADING_URL` | The new heading URL you want to redirect _to_ with `https://www.braze.com/` removed from the URL string.                                      |

Your redirect should be similar to the following:

```yaml
---
nav_title: Getting started
article_title: Getting started with the Braze SDK
description: "If you're new to the Braze SDK, learn how to get started."
local_redirect:
  building-from-source: '/docs/developer_guide/getting_started/#using-our-install-script'
```
