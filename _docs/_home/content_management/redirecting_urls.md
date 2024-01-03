---
nav_title: Redirecting URLs
page_order: 5
noindex: true
---

# Redirecting URLs

> Learn how to redirect URLs for pages and page headings on Braze Docs.

Page URLs always match the directory structure of the Braze Docs repository. When a Markdown file is renamed or moved to a different directory, the original URL will result in a 404 error if a redirect isn't set up.

![Example of a 404 page on Braze Docs.]()

By setting up URL redirects, you'll help prevent bookmarks from breaking for Braze Docs users.

{% multi_lang_include contributing/prerequisites.md %}

## Redirecting a page

To redirect the URL for an entire page, you'll use our global redirect file. First, [create a new branch](../../github/creating_a_new_branch.md), then find the page's Markdown file and move or rename the file.

![A text editor with the file tree open on the left side.]()

{% multi_lang_include contributing/alerts/tip_locating_a_file.md %}

Navigate to the `assets/js/` directory, then open the global redirect file: `broken_redirect_list.js`. At the bottom of the file, set up your redirect on a newline.

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

{% multi_lang_include contributing/minis/creating_a_pull_request.md %}

## Redirecting a heading

To redirect the URL for an in-page heading, you'll use the `local_redirect` key within the page's YAML front matter. First, [create a new branch](../../github/creating_a_new_branch.md), then open the page's markdown file and rename the relevant heading.

![A text editor with the file tree open on the left side.]()

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

{% multi_lang_include contributing/minis/creating_a_pull_request.md %}

