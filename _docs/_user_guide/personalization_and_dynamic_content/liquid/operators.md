---
nav_title: Operators
page_order: 3
---

# Operators

Liquid supports many [operators][25] that can be used in your conditional statements.

|   Syntax| Operator Description|
|---------|-----------|
| ==  | equals        |
| !=  | does not equal|
|  >  | greater than  |
| <   | less than     |
| >=| greater than or equal to|
| <= | less than or equal to |
| or | condition A or condition B|
| and | condition A and condition B|
| contains | checks to see if a string or string array contains a string|

## Operator Examples

Here are some examples of how these operators could be helpful for your marketing campaigns:

**Total Revenue - sending messages based on an integer custom attribute for "Total Revenue":**

![total revenue][13]

In this example, if a customer’s "Total Revenue" custom attribute is greater than zero, they will get the message:

```
We appreciate your business! Use our coupon SAVE10 for an extra 10% off your next purchase.
```
If a customer’s "Total Revenue" custom attribute does not exist or is equal to 0, they will get the following message:

```
Make your first purchase today! Use our coupon SAVE10 for an extra 10% off
```

**Games Attended - sending messages that differ based on an integer attribute, "Number Games Attended":**

![games liquid][14]

In this example, if you have attended one game, you get the following message:

```
Loved that sport game? Get 10% off your second one with code SAVE10
```

If you have attended more than one game, you get:

```
Love sports games? Get 10% your next one with code SAVE10
```
If you haven’t attended any games, or that custom attribute doesn’t exist on your profile, you’d get the following message:

```
Attend your first game! 10% off with code SAVE10
```

[1]: http://docs.shopify.com/themes/liquid-documentation/basics
[2]: {{ site.baseurl }}/user_guide/data_and_analytics/custom_data/custom_attributes/
[3]: http://docs.shopify.com/themes/liquid-documentation/filters
[5]: {{ site.baseurl }}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types
[6]: #conditional-messaging-logic-tags
[7]: https://docs.shopify.com/themes/liquid-documentation/tags
[12]: https://docs.shopify.com/themes/liquid-documentation/filters
[4]: {% image_buster /assets/img_archive/personalized_firstname_.png %}
[8]: http://docs.shopify.com/themes/liquid-documentation/tags/control-flow-tags "Control Flow Tags"
[9]: #connected-content
[11]: {{ site.baseurl }}/user_guide/data_and_analytics/custom_data/custom_events/
[13]: {% image_buster /assets/img_archive/total_revenue_ios.png %}
[14]: {% image_buster /assets/img_archive/games_liquid.png %}
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
[29]: {% image_buster /assets/img_archive/MemberSince.png %}
[30]: #variable-tags
[31]:https://docs.shopify.com/themes/liquid/tags/variable-tags
[32]:https://docs.shopify.com/themes/liquid/tags/iteration-tags
[33]:{% image_buster /assets/img_archive/SupportedAttributes.png %}
[34]:{% image_buster /assets/img_archive/personalized_iflogic_.png %}
[36]:{% image_buster /assets/img_archive/value_null.png %}
[37]:#accounting-for-null-attribute-values
[38]: {{ site.baseurl }}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/
[39]: #most-recently-used-device-information
[40]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/#optional-idfa-collection
[41]: https://dashboard-01.braze.com/app_settings/app_settings/custom_attributes
[42]: https://dashboard-01.braze.com/app_settings/app_settings/custom_events
[43]: {{ site.baseurl }}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions
[44]: {% image_buster /assets/img_archive/insert_liquid_var_arrow.png %}
[45]: {% image_buster /assets/img_archive/insert_var_shot.png %}
[46]: #targeted-device-information
