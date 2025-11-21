---
nav_title: Advanced settings
article_title: Advanced Push Settings
platform: iOS
page_order: 5
description: "This reference article covers advanced iOS push notification settings such as alert options, sounds, expiry, and more."
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Advanced settings

When creating a push campaign, on the compose step, select **Settings** to view the advanced settings available.

![]({% image_buster /assets/img_archive/ios_advanced_settings.png %})

## Extracting data from push key-value pairs

Braze allows you to send custom-defined string key-value pairs, known as `extras`, along with a push notification to your application. Extras can be defined via the dashboard or API and will be available as key-value pairs within the `notification` dictionary passed to your push delegate implementations.

## Alert options

Check the **Alert Options** checkbox to see a dropdown of key-values available to adjust how the notification appears on devices.

## Adding content-available flag

Check the **Add Content-Available Flag** checkbox to instruct devices to download new content in the background. Most commonly, this can be checked if you are interested in sending [silent notifications]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/silent_push_notifications/).

## Adding mutable-content flag

Check the **Add Mutable-Content Flag** checkbox to enable advanced receiver customization in iOS 10+ devices. This flag will automatically be sent when composing a [rich notification]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/customization/rich_notifications/), regardless of the value of this checkbox.

## Update app badge count

Enter the number that you want to update your badge count to, or use Liquid syntax to set your custom conditions. You may also update your badge count manually through your application's `applicationIconBadgeNumber` property or the push notification payload. To read more, refer to our dedicated [Badge count]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/customization/badges/) article.

## Sounds

Here you can enter a path to a sound file in your app bundle to specify a sound to be played when the push message is received. If the specified sound file does not exist or should the keyword "default" be entered, Braze will use the default device alert sound. For more on customization, refer to our dedicated [Custom sounds]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/customization/custom_sounds/) article.

## Collapse ID

Specify a collapse ID to coalesce similar notifications. If you send multiple notifications with the same collapse ID, the device will only show the most recently received notification. Refer to Apple's documentation on [coalesced notifications](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1).

## Expiry

Checking the **Expiry** checkbox will allow setting an expiration time for your message. Should a user's device lose connectivity, Braze will continue to try and send the message until the specified time. If this is not set, the platform will default to an expiration of 30 days. Note that push notifications that expire before delivery are not considered failed and will not be recorded as a bounce.

