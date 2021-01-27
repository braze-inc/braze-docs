---
nav_title: Using Liquid
page_order: 0
description: "Liquid can elevate the personalization in your messages to impressive heights. Liquid tags act as placeholders in your messages that can pull in consented information from your user's account and enable personalization and relevant messaging practices."
---

# Liquid Usage Use Cases & Overview

{% raw %}

If you include the following text in your message: `{{${first_name}}}`, the appropriate value from the user will be interpolated when the message is sent. If you would like to use the value of a custom attribute, you must add the namespace "custom_attribute" to the variable. For example, to use a custom attribute named "zip code", you would include `{{custom_attribute.${zip code}}}` in your message.

The following values can be substituted into a message, depending on their availability:

- [Basic User Information][1] (e.g. `first_name`, `last_name`, `email_address`)
- [Custom Attributes][2]
- [Custom Event Properties][11]
- [Most Recently Used Device Information][39]
- [Target Device Information][40]

You can also pull content directly from a web server via Braze's [Connected Content][9] feature.
{% endraw %}

{% alert important %}
Braze currently supports Liquid up to and including __Liquid 3 from Shopify__. We do not currently support Liquid 4 and beyond.
{% endalert %}

## Using Liquid

{% raw %}

Once you know the [Liquid tags available][1], using Liquid can elevate the personalization in your messages to impressive heights. Liquid tags act as placeholders in your messages that can pull in consented information from your user's account and enable personalization and relevant messaging practices. In the block below, you can see that a dual usage of a Liquid tag to call the user's first name, as well as a default tag in the event that a user would not have their first name registered.

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

### Inserting Tags

You can insert tags by typing `{{` in any message, which will trigger an auto-completion feature that will continue to update as you type. You can even select a variable from the options that appear as you type.

If you're using a custom tag, you can copy and paste the tag into whatever message you desire.

{% endraw %}

{% alert note %}

If you choose to use Liquid in your Email messages, be sure to: 
1. Insert it using the HTML editor as opposed to the classic editor. The Classic Editor may parse the Liquid as plaintext.
2. Place Liquid code within the `<body>` tag only. Placing it outside this tag may cause inconsistent rendering upon delivery. 

{% endalert %}

{% raw %}


### Pre-Formatted Variables

You can insert pre-formatted variables with defaults through the "Insert Personalization Attribute" modal located on the top-right of any templated text field.

![Modal buttons][44]

The modal will insert Liquid with your specified default value at the point that your cursor was. The insertion point is also specified via the preview box, which has the before and after text. If a block of text is highlighted, the highlighted text will be replaced.

![Modal][45]

{% endraw %}



[1]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/
[2]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/
[9]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/
[11]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/
[39]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/#most-recently-used-device-information
[40]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/#targeted-device-information
[44]: {% image_buster /assets/img_archive/insert_liquid_var_arrow.png %}
[45]: {% image_buster /assets/img_archive/insert_var_shot.png %}
