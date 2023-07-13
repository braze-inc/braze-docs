---
nav_title: Detailed Push Preferences
article_title: Detailed Push Preferences
page_order: 1.5
page_type: reference
description: "This article covers best practices for creating detailed push preferences for your users."
channel: push

---

# Detailed push preferences

> Push notifications should be treated with care to target users with timely and relevant notifications. Braze will collect useful device and usage information that can be used to target relevant segments. This should be supplemented with custom events and attributes specific to your app. Using that data, you can carefully target messages to increase open rates and decrease instances of users disabling push.

## Create a notifications settings page

You can create a settings page in your app that allows users to directly tell you which notifications they want to receive. This can be set as a boolean attribute in Braze that corresponds to the app setting status. For example, a news app could have subscription settings for breaking news, sports news, or politics.

When the news app wants to create a campaign targeting only users interested in Politics, they simply add the 'Subscribes to Politics' attribute filter to the segment. When set to true, only users who subscribe to notifications will receive them.

## Obtain user permission

The general stats that you see for push enabled will relate to whether the user has approved notifications with their OS. If users disable notifications on iOS, they'll be automatically removed from our system since Apple won't allow the push token to be sent. 

Android 13 and up requires permission be obtained before push notifications can be shown. Older versions of Android will subscribe users to notifications by default.

## Set custom attributes

Refer to the following articles for setting custom attributes based on your platform:
- [iOS][4]
- [Android][5]
- [REST API][10]

[4]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_custom_attributes/
[5]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_custom_attributes/#setting-custom-attributes
[10]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-attributes-object-specification
[46]:{% image_buster /assets/img_archive/Push_Window8_Toast.png %}
[47]:{% image_buster /assets/img_archive/Push_Windows_Universal_Toast.png %}
