---
nav_title: Redirecting URLs
article_title: Redirecting URLs
page_order: 4
noindex: true
---

# Redirecting URLs

> Learn how to redirect broken or outdated URLs for Braze Docs.

## Redirecting a deleted page

To redirect a page that was deleted from the [`_docs` directory](https://github.com/braze-inc/braze-docs/tree/develop/_docs), you'll set up the redirect in [`broken_redirect_list.js`](https://github.com/Appboy/braze-docs/blob/develop/assets/js/broken_redirect_list.js). 

In the terminal, open `braze-docs`, then open `assets/js/broken_redirect_list.js` in a text editor. For example:

```bash
cd ~/braze-docs
nano ./assets/js/broken_redirect_list.js
```

At the bottom of the file, add the following line.

```javascript
validurls['<redirect-from>'] = '<redirect-to>';
```

Replace `<redirect-from>` with path you want to redirect _from_ and `<redirect-to>` with the path you want to redirect _to_. For example:

```javascript
validurls['/docs/user_guide/data_and_analytics/engagement_reports/#engagement-reports'] = '/docs/user_guide/data_and_analytics/your_reports/engagement_reports/#engagement-reports';
```

When you're finished, save your changes and [create a pull request](../_github/creating_a_pull_request.md).

## Redirecting an existing page

### Redirecting the entire page

To redirect an entire page currently located in the [`_docs` directory](https://github.com/braze-inc/braze-docs/tree/develop/_docs), you'll reassign the `layout` tag in the page's YAML front matter.

In the terminal, open `braze-docs`, then open page's Markdown file in a text editor. For example:

```bash
cd ~/braze-docs
nano ./_docs/_user_guide/data_and_analytics/custom_data/custom_attributes/array_of_objects.md
```

In the page's YAML front matter, add the following lines.

```yaml
layout: redirect
redirect_to: <new-url-path>
```

Replace `<new-url-path>` with the URL path you want to redirect _to_. For example:

```yaml
---
nav_title: Android and FireOS
config_only: true
noindex: true
layout: redirect
redirect_to: /docs/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/
page_order: 0.1
---
```

When you're finished, save your changes and [create a pull request](../_github/creating_a_pull_request.md).

### Redirecting a page heading

To redirect a heading on a page currently located in the [`_docs` directory](https://github.com/braze-inc/braze-docs/tree/develop/_docs), you'll add the `local_redirect` tag to the page's YAML front matter. 

In the terminal, open `braze-docs`, then open page's Markdown file in a text editor. For example:

```bash
cd ~/braze-docs
nano ./_docs/_user_guide/data_and_analytics/custom_data/custom_attributes/array_of_objects.md
```

In the page's YAML front matter, add the following lines.

```
local_redirect:
  <old-heading>: '<new-url-path>'
```

Replace `<hold-heading>` with the old heading path and `<new-url-path>` with the _full_ URL path including the heading. For example:

```yaml
nav_title: Integration
article_title: Push Integration for iOS
platform: iOS
page_order: 0
description: "This reference article covers how to integrate push notifications in your iOS application."
channel:
  - push
search_rank: 5

local_redirect:
  creating-a-service-extension: '/docs/developer_guide/platform_integration_guides/ios/push_notifications/rich/#creating-a-service-extension'
```

When you're finished, save your changes and [create a pull request](../_github/creating_a_pull_request.md).
