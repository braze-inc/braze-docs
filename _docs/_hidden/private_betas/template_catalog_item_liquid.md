---
nav_title: Templating Catalog Items Including Liquid
article_title: Templating Catalog Items Including Liquid
permalink: "/templating_catalog_items_liquid/"
description: "Learn how to template catalog items that include Liquid."
page_type: reference
hidden: true
---

# Templating catalog items including Liquid

 Similar to [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content), the `:rerender` flag must be included in the Liquid tag to render its Liquid content. Note that the `:rerender` flag is only one level deep, meaning it won't apply to any nested Liquid tag calls.

 {% alert important %}
 Templating catalog items that include Liquid is in early access. Reach out to your Braze account manager if you're interested in participating in the early access.
 {% endalert %}

If a catalog item contains user profile fields (within a Liquid personalization tag), these values must be defined earlier in the message via Liquid before the templating in order to render the Liquid properly. If `:rerender` flag is not provided, it will render the raw Liquid content.

For example, if a catalog named "Messages" has an item with this Liquid:

![][15]{: style="max-width:80%;"}<br>

To render the following Liquid content:

{% raw %}
```liquid
Hi ${first_name}

{% catalog_items Messages greet_msg :rerender %}
{{ items[0].Welcome_Message }}
```
{% endraw %}

This will display as the following:

{% raw %}
```
Hi Peter,

Welcome to our store, Peter!
```
{% endraw %}

{% alert note %}
Catalog Liquid tags can't be used recursively inside catalogs.
{% endalert %}

[15]: {% image_buster /assets/img_archive/catalog_liquid_templating.png %}
