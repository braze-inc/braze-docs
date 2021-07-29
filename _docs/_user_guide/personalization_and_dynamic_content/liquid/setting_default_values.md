---
nav_title: Setting Default Values
page_order: 5
description: "Set default fallback values for any personalization attribute that you use in your messages."
---

# Setting Default Values

{% raw %}

Set default fallback values for any personalization attribute that you use in your messages. Default values can be added by specifying a [Liquid Filter][3] (use `|` to distinguish the filter inline, as shown below) with the name "default."

```
| default: 'Insert Your Desired Default Here'
```

If a default value is not provided and the field is missing or not set on the user, the field will be blank in the message.

The example below shows the correct syntax for adding a default value. In this case, the words "Valued User" will replace the attribute `{{ ${first_name} }}` if a user's `first_name` field is blank or unavailable.

```liquid
Hi {{ ${first_name} | default: 'Valued User' }}, thanks for using the App!
```

To a user named Janet Doe, the message would appear to the user as either:

```
Hi Janet, thanks for using the App!
```

Or...

```
Hi Valued User, thanks for using the App!
```

{% endraw %}

[3]: http://docs.shopify.com/themes/liquid-documentation/filters
[31]:https://docs.shopify.com/themes/liquid/tags/variable-tags
[32]:https://docs.shopify.com/themes/liquid/tags/iteration-tags
[34]:{% image_buster /assets/img_archive/personalized_iflogic_.png %}
[37]:#accounting-for-null-attribute-values
