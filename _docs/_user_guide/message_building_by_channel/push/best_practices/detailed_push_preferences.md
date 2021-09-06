---
nav_title: Detailed Push Preferences
article_title: Detailed Push Preferences
page_order: 1
page_type: reference
description: "This article covers best practices for creating detailed push preferences for your users."
channel: push

---

# Detailed Push Preferences

Push notifications should be treated with care to target users with timely and relevant notifications. Braze will collect useful device and usage information that can be used to target relevant segments. This should be supplemented with custom events and attributes specific to your app. Using that data you can carefully target messages to increase open rates and decrease instances of users disabling push.

![Circa Message Settings][15]

Additionally, you can create a settings page in your app that allows users to directly tell you which notifications they want to receive. This can be set as a boolean attribute in Braze that corresponds to the app setting status. For example, a news app could have subscription settings for the following:

- Breaking News
- Sports News
- Politics
- Business News

When the news app wants to create a campaign targeting only users interested in Politics, they simply add the 'Subscribes to Politics' attribute filter to the segment. When set to true, only users who subscribe to notifications will receive them.

![Example of Opt-In Prompts][14]

The general stats that you see for push enabled will relate to whether the user has approved notifications with the OS. If users disable notifications on iOS they'll be automatically removed from our system since Apple won't allow the push token to be sent. Android subscribes users to notifications by default.

Documentation for setting custom attributes:

- [iOS][4]
- [Android][5]
- [Windows Universal][6]
- [REST API][10]

[4]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/setting_custom_attributes/
[5]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_custom_attributes/#setting-custom-attributes
[6]: {{site.baseurl}}/developer_guide/platform_integration_guides/windows_universal/analytics/setting_custom_attributes/
[10]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-attributes-object-specification
[14]: {% image_buster /assets/img_archive/circa_push1.png %}
[15]: {% image_buster /assets/img_archive/circa_push2.png %}
[46]:{% image_buster /assets/img_archive/Push_Window8_Toast.png %}
[47]:{% image_buster /assets/img_archive/Push_Windows_Universal_Toast.png %}
