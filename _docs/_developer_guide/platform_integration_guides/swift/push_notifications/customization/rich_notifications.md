---
nav_title: Rich Notifications
article_title: Rich Push Notifications for iOS
platform: Swift
page_order: 5
description: "This article covers implementing rich push notifications in your iOS application."
channel:
  - push

---

# Rich push notifications for iOS

Rich notifications are push notifications with images, GIFs, and video. To enable this functionality, you must create a notification service extension&mdash;a type of extension that enables modification of a push payload before it is displayed. Refer to Apple's [`UNNotificationAttachment`][28] for a list of supported file types and sizes.

## Creating a service extension

To create a [notification service extension][23], navigate to **File > New > Target** in Xcode and select **Notification Service Extension**.

![][26]{: style="max-width:90%"}

Ensure that **Embed In Application** is set to embed the extension in your application.

## Setting up the notification service extension

A notification service extension is its own binary that is bundled with your app. It must be set up in the [Apple Developer Portal][27] with its own app ID and provisioning profile.

The notification service extension's bundle ID must be distinct from your main app target's bundle ID. For example, if your app's bundle ID is `com.company.appname`, you can use `com.company.appname.AppNameServiceExtension` for your service extension.

### Examples

For a step-by-step guide on integrating rich push notifications with `BrazeNotificationService`, refer to our [tutorial](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications).

To see a sample, refer to the usage in [`NotificationService`][1] of our Examples app.

## Creating a rich notification in your dashboard

Your Marketing team can also create rich notifications from the dashboard. Create a push notification through the push composer and simply attach an image or GIF, or provide a URL that hosts an image, GIF, or video. Note that assets are downloaded on the receipt of push notifications, so you should plan for large, synchronous spikes in requests if you are hosting your content.

[1]: https://github.com/braze-inc/braze-swift-sdk/blob/main/Examples/Swift/Sources/PushNotificationsServiceExtension/NotificationService.swift
[23]: https://developer.apple.com/reference/usernotifications/unnotificationserviceextension
[26]: {% image_buster /assets/img_archive/ios10_se_at.png %}
[27]: https://developer.apple.com
[28]: https://developer.apple.com/reference/usernotifications/unnotificationattachment
