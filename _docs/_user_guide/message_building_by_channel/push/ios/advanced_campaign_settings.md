---
nav_title: "Advanced Push Campaign Settings"
article_title: Advanced Push Campaign Settings
page_type: reference
page_order: 6
description: "This reference article covers several advanced push campaign setting such as alert options, flags, sounds, expiry, and more."
platform: iOS
channel:
  - push
tool:
  - Campaigns

---

# Advanced push campaign settings

> This reference article covers several advanced push campaign settings such as alert options, flags, sounds, expiry and more.

When creating push engagement, on the **Compose** step, you can select the <i class="fas fa-cog"></i> cog icon to view the advanced settings for your message.

![][1]

## Alert options

By selecting the checkbox here, you will notice a dropdown menu of key-values available for adjusting how the notification will appear on devices.

## Adding content-available flag

The `content-available` flag instructs devices to download new content in the background. Most commonly, this can be checked on should you be interested in sending [silent notifications][2].

## Adding mutable-content flag

The `mutable-content` flag enables advanced receiver customizations in iOS 10+ devices. This flag will automatically be sent when composing a [rich notification][3], regardless of the value of this checkbox.

## Sounds

Here, you can enter a path to a sound file in your app bundle to specify a sound to be played when the push message is received. If the specified sound file does not exist or should the keyword "default" be entered, Braze will use the default device alert sound.

## Collapse ID
Specify a Collapse ID to coalesce similar notifications. If you send multiple notifications with the same Collapse ID, the device will only show the most recently received notification. For more information, refer to Apple's [documentation][4].

## Expiry

Selecting **Expiry** will offer the option to set an expiration time for your message. should a user's device lose connectivity, Braze will continue to try and send the message until the specified time. If this is not set, the platform will default to an expiration of 30 days. Note that push notifications that expire before delivery are not considered as failed and will not be recorded as a bounce.

[1]: {% image_buster /assets/img_archive/ios_advanced_settings.gif %}
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/silent_push_notifications/
[3]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/#ios-10-rich-notifications
[4]: https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1
