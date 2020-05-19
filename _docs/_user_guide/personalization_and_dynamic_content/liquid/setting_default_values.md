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
