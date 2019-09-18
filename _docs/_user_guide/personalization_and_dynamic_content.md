---
nav_title: Personalization & Dynamic Content
page_order: 6
user_top_header: "Personalized Messaging"
user_top_text: "Braze allows you to personalize your campaigns by inserting user-specific information, such as the user's name, into messages."

user_featured_title: "Available Messaging Channels"
user_featured_list:
- name: Liquid
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/
  fa_icon:
- name: Connected Content
  link: /docs/user_guide/personalization_and_dynamic_content/connected_content/
  fa_icon:
- name: Deep-Linking to In-App Content
  link: /docs/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/
  fa_icon:

user_menu_title: "More Articles"

user_menu_list:

- name: Key-Value Pairs
  link: /docs/user_guide/personalization_and_dynamic_content/key_value_pairs/
  fa_icon:
- name: Key-Value Pairs
  link: /docs/user_guide/personalization_and_dynamic_content/key_value_pairs/
  fa_icon:
- name: Emoji Messaging
  link: /docs/user_guide/personalization_and_dynamic_content/emoji_messaging/
  fa_icon:
- name: Content Blocks
  link: /docs/user_guide/engagement_tools/templates_and_media/content_blocks/
  fa_icon:
---

Campaign messages support templated messaging using the Liquid templating language. Detailed documentation of Liquid syntax and usage is available [here][1].

For more on Dynamic Personalization with Liquid, check out our [detailed, guided LAB course](https://lab.braze.com/dynamic-personalization-with-liquid)!

Liquid templating language supports the use of objects, tags and filters.

[Objects][27] allow you to insert personalizable attributes into your messages.

[Tags][6] allow you to execute programming logic in your messages. For example, you can use tags to include intelligent logic, such as "if" statements, in your campaigns.

[Filters][16] allow you to reformat personalizable attributes and dynamic content. For example, you could convert a timestamp, such as *2016-09-07 08:43:50 UTC* into a date such as *September 7th, 2016*.

[1]: http://docs.shopify.com/themes/liquid-documentation/basics
[2]: {{ site.baseurl }}/user_guide/data_and_analytics/custom_data/custom_attributes/
[3]: http://docs.shopify.com/themes/liquid-documentation/filters
[5]: {{ site.baseurl }}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types
[6]: {{ site.baseurl }}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/
[7]: https://docs.shopify.com/themes/liquid-documentation/tags
[12]: https://docs.shopify.com/themes/liquid-documentation/filters
[4]: {% image_buster /assets/img_archive/personalized_firstname_.png %}
[8]: http://docs.shopify.com/themes/liquid-documentation/tags/control-flow-tags "Control Flow Tags"
[9]: #connected-content
[11]: {{ site.baseurl }}/user_guide/data_and_analytics/custom_data/custom_events/
[13]: {% image_buster /assets/img_archive/total_revenue_ios.png %}
[14]: {% image_buster /assets/img_archive/games_liquid.png %}
[15]: {% image_buster /assets/img_archive/liquid_abort.png %}
[16]: {{ site.baseurl }}/user_guide/personalization_and_dynamic_content/liquid/filters/
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
[27]: {{ site.baseurl }}/user_guide/personalization_and_dynamic_content/liquid/overview/
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
