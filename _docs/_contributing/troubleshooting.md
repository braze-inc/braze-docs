---
nav_title: Troubleshooting
article: Troubleshooting
description: "Troubleshooting steps for common issues you may experience while contributing to Braze Docs."
page_order: 9
noindex: true
---

# Troubleshooting

> If you're having trouble contributing to Braze Docs, review these common issues first. If the issue you're experiencing isn't listed, [let us know](https://github.com/braze-inc/braze-docs/issues/new?assignees=&labels=issue&projects=&template=report_an_issue.md&title=) so we can add it here.

## Redirect isn't working

If a [redirect you set up]({{site.baseurl}}/contributing/content_management/redirecting_urls/) in the global redirect file (`assets/js/broken_redirect_list.js`) isn't working, double-check your URL string for any uppercase characters. If you find any, convert them to lowercase (even if the corresponding filename in the `_docs` directory contains uppercase characters).

{% tabs local %}
{% tab before %}
```javascript
validurls['/docs/hidden/WIP_Partnerships/WIP_Guidelines'] = '/docs/contributing/home/';
```
{% endtab %}

{% tab after %}
```javascript
validurls['/docs/hidden/wip_partnerships/wip_guidelines'] = '/docs/contributing/home/';
```
{% endtab %}
{% endtabs %}

## Cross-reference link returns a 404

If a [cross-reference link]({{site.baseurl}}/contributing/content_management/cross_referencing/) on your page (such as `{% raw %}[Braze Developer Guide]({{site.baseurl}}/developer_guide/home){% endraw %}`) returns a 404 page, check the URL for the following string.

```plaintext
%7B%7Bsite.baseurl%7D%7D
```

A URL containing this string will be similar to the following:

```plaintext
https://www.braze.com/docs/user_guide/personalization_and_dynamic_content/connected_content/%7B%7Bsite.baseurl%7D%7D/user_guide/administrative/app_settings/message_activity_log_tab
```

If you find this string in the URL, one or more of your cross-reference links are surrounded in [Liquid raw tags](https://shopify.dev/docs/api/liquid/tags/raw).

{% tabs local %}
{% tab Liquid raw tag %}
<code>
&#123;% raw %} &#123;% endraw %}
</code>
{% endtab %}
{% endtabs %}

Move these tags so that they're only surrounding the Liquid content you want to display as raw.

{% tabs local %}
{% tab before %}
<code>
&#123;% raw %} Learn how to use Liquid's <code>&#123;&#123; page_title }} tag. For more information, see [Liquid tags](&#123;&#123;site.baseurl}}/contributing/liquid/). &#123;% endraw %}
</code>
{% endtab %}

{% tab after %}
<code>
Learn how to use Liquid's &#123;% raw %} &#123;&#123; page_title }} &#123;% endraw %} tag. For more information, see [Liquid tags](&#123;&#123;site.baseurl}}/contributing/liquid/).
</code>
{% endtab %}
{% endtabs %}
