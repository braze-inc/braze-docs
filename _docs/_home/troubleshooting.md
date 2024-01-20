---
nav_title: Troubleshooting
page_order: 9
noindex: true
---

# Troubleshooting

> If you're having trouble contributing to Braze Docs, review these common issues first. If the issue you're experiencing isn't listed, [let us know](https://github.com/braze-inc/braze-docs/issues/new?assignees=&labels=issue&projects=&template=report_an_issue.md&title=), so we can add it here.

## Cross-reference link returns 404

If a cross-reference link on your page (such as `{% raw %}[Braze Developer Guide]({{site.baseurl}}/developer_guide/home){% endraw %}`) leads to a 404 page, check the URL for the following string:

```plaintext
%7B%7Bsite.baseurl%7D%7D
```

A URL containing this string will look similar to the following:

```plaintext
https://www.braze.com/docs/user_guide/personalization_and_dynamic_content/connected_content/%7B%7Bsite.baseurl%7D%7D/user_guide/administrative/app_settings/message_activity_log_tab
```

If you find this string in the URL, one or more of your cross-reference links are surrounded in [Liquid raw tags](https://shopify.dev/docs/api/liquid/tags/raw). Move these tags, so they're only surrounding the Liquid content you're want to display as raw.

![An image of Liquid's raw tag. An image is used here to prevent Liquid from linting the example.]()

A cross-reference link surrounded by Liquid raw tags will look similar to the following:

![An image of Liquid's raw tag used in an example code block. An image is used here to prevent Liquid from linting the example.]()
