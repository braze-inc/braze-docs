---
nav_title: Redirecting URLs
article: Redirecting URLs
description: "Learn how to redirect URLs for pages and page headings on Braze Docs."
page_order: 5
noindex: true
---

# Redirecting URLs

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
After you move or rename the relevant Markdown file, navigate to the `assets/js/` directory and open the global redirect file.

```bash
braze-docs
└── assets
    └── js
        └── broken_redirect_list.js
```

At the of the file, create a redirect on a new line using the following syntax:

```javascript
validurls['REDIRECT_FROM'] = 'REDIRECT_TO';
```

Replace the following:

| Placeholder     | Description                                                                                    |
|-----------------|------------------------------------------------------------------------------------------------|
| `REDIRECT_FROM` | The URL you want to redirect _from_ with `https://www.braze.com/` removed from the URL string. |
| `REDIRECT_TO`   | The URL you want to redirect _to_ with `https://www.braze.com/` removed from the URL string.   |
{: .reset-td-br-1 .reset-td-br-2}

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
{: .reset-td-br-1 .reset-td-br-2}

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
