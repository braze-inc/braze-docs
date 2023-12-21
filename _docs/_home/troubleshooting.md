---
nav_title: Troubleshooting
page_order: 8
noindex: true
---

# Troubleshooting

> TODO:

## Cross-reference link returns 404

<!--
Link for context: https://github.com/braze-inc/braze-docs/pull/6647/files#r1427183418
-->

If a cross-reference link on your page (such as `{% raw %}[Braze Developer Guide]({{site.baseurl}}/developer_guide/home){% endraw %}`) leads to a 404 page, check the URL for the following string:

```plaintext
%7B%7Bsite.baseurl%7D%7D
```

A URL containing this string will look similar to the following:

```plaintext
https://www.braze.com/docs/user_guide/personalization_and_dynamic_content/connected_content/%7B%7Bsite.baseurl%7D%7D/user_guide/administrative/app_settings/message_activity_log_tab
```

If you find this string in the URL, one or more of your cross-reference links may be surrounded in Liquid raw tags. Move these tags, so they're only surrounding the Liquid content you're hoping to display as raw.

> TODO: Fix styling here.

{% raw %}
```plaintext
{/% raw %/}{/% endraw %/}
```
{% endraw %}

A cross-reference link surrounded by Liquid raw tags will look similar to the following:

{% raw %}
````plaintext
{/% raw %/}
If you'd like to leverage the Braze SDK in your app, see the [Braze Developer Guide]({{site.baseurl}}/developer_guide/home). You'll be able to do things like this:

```liquid
{% unless hide_nav %}
<div class="col-sm-12 col-md-3 col-lg-3 col-xl-2 d-print-none collapse d-md-block" id="nav_bar"  >
  <div id="nav_col" class="  ">
  {% include left_nav_menu.html %}
  </div>
</div>
{% endunless %}
```
{/% endraw %/}
````
{% endraw %}
