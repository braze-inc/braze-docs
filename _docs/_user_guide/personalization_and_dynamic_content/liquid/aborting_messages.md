---
nav_title: Aborting Messages
page_order: 7
description: "Messages may now be aborted within conditional statements. In this reference article, we list some examples use cases for this functionality."
---

# Aborting Messages
Optionally, you can also now abort messages within conditionals. Here are some examples of how this feature can be used in marketing campaigns:

**Aborting message if "Number Games Attended" = 0:**

For example, let’s say that you did not want to send the above message to customers who had not attended a game:

![liquid abort message][15]

This message will only send to customers who are known to have attended a game.

**Messaging English speaking customers only:**

You can message English speaking customers only by creating an "if" statement that'll match when a customer's language is English and an else statement that'll abort the message for anyone who does not speak English or does not have a language on their profile.

{% raw %}
```liquid

{% if ${language} == 'en' %}
Send this message in English!
{% else %}
{% abort_message() %}
{% endif %}
```

By default Braze will log a generic error message to your Developer Console log:

```text
{% abort_message %} called
```

You can also have the abort_message log something to your Developer Console log by including a string inside the parentheses:

```liquid
{% abort_message('language was nil') %}
```
{% endraw %}

![developer_console][26]

[1]: http://docs.shopify.com/themes/liquid-documentation/basics
[2]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/
[3]: http://docs.shopify.com/themes/liquid-documentation/filters
[5]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types
[6]: #conditional-messaging-logic-tags
[7]: https://docs.shopify.com/themes/liquid-documentation/tags
[12]: https://docs.shopify.com/themes/liquid-documentation/filters
[4]: {% image_buster /assets/img_archive/personalized_firstname_.png %}
[8]: http://docs.shopify.com/themes/liquid-documentation/tags/control-flow-tags "Control Flow Tags"
[9]: #connected-content
[11]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/
[15]: {% image_buster /assets/img_archive/liquid_abort.png %}
[16]: #manipulating-message-content-filters
[17]: #conditional-logic
[18]: #aborting-messages
[19]: https://docs.shopify.com/themes/liquid/filters/math-filters
[20]: https://docs.shopify.com/themes/liquid/filters/string-filters
[21]: https://docs.shopify.com/themes/liquid/filters/string-filters#capitalize
[22]: https://docs.shopify.com/themes/liquid/filters/array-filters
[23]: https://docs.shopify.com/themes/liquid/filters/array-filters#first
[24]: https://docs.shopify.com/themes/liquid/filters/additional-filters#date
[25]: https://docs.shopify.com/themes/liquid/basics/operators
[26]: {% image_buster /assets/img_archive/developer_console.png %}
[27]: #adding-personalizable-attributes-objects
[30]: #variable-tags
[31]:https://docs.shopify.com/themes/liquid/tags/variable-tags
[32]:https://docs.shopify.com/themes/liquid/tags/iteration-tags
[34]:{% image_buster /assets/img_archive/personalized_iflogic_.png %}
[37]:#accounting-for-null-attribute-values
[38]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/
[39]: #most-recently-used-device-information
[40]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/#optional-idfa-collection
[41]: https://dashboard-01.braze.com/app_settings/app_settings/custom_attributes
[42]: https://dashboard-01.braze.com/app_settings/app_settings/custom_events
[43]: {{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions
[44]: {% image_buster /assets/img_archive/insert_liquid_var_arrow.png %}
[45]: {% image_buster /assets/img_archive/insert_var_shot.png %}
[46]: #targeted-device-information
