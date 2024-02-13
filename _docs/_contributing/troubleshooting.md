---
nav_title: Troubleshooting
article: Troubleshooting
description: "Troubleshooting steps for common issues you may experience while contributing to Braze Docs."
page_order: 8
noindex: true
---

# Troubleshooting

> If you're having trouble contributing to Braze Docs, review these common issues first. If the issue you're experiencing isn't listed, [let us know](https://github.com/braze-inc/braze-docs/issues/new?assignees=&labels=issue&projects=&template=report_an_issue.md&title=) so we can add it here.

## Cross-reference link returns a 404

If a cross-reference link on your page (such as `{% raw %}[Braze Developer Guide]({{site.baseurl}}/developer_guide/home){% endraw %}`) returns a 404 page, check the URL for the following string.

```plaintext
%7B%7Bsite.baseurl%7D%7D
```

A URL containing this string will be similar to the following:

```plaintext
https://www.braze.com/docs/user_guide/personalization_and_dynamic_content/connected_content/%7B%7Bsite.baseurl%7D%7D/user_guide/administrative/app_settings/message_activity_log_tab
```

If you find this string in the URL, one or more of your cross-reference links are surrounded in the following [Liquid raw tag](https://shopify.dev/docs/api/liquid/tags/raw):

{% tabs local %}
{% tab liquid raw tag %}
<code>
&#123;% raw %} Example &#123;% endraw %}
</code>
{% endtab %}
{% endtabs %}

Move these tags so that they're only surrounding the Liquid content you want to display as raw.

{% tabs local %}
{% tab before %}
<code>
&#123;% raw %}
Learn how to use Liquid's <code>&#123;&#123; page_title }}</code> tag. For more information, see [Liquid tags]({{site.baseurl}}/contributing/liquid/).

&#123;% endraw %}
</code>
{% endtab %}

{% tab after %}
<code>
Learn how to Liquid's &#123;% raw %} &#123;&#123; page_title }} &#123;% endraw %} tag. For more information, see [Liquid tags]({{site.baseurl}}/contributing/liquid/).
</code>
{% endtab %}
{% endtabs %}
