---
nav_title: "Message types"
article_title: Push message types
page_order: 3
page_type: reference
description: "This reference article lists the different types of push notifications you can send with Braze."
channel: push
---

# Push message types

> There are many types of push notifications you can use to interact with your customers. You can configure most of these settings in your push campaigns, but some require backend configurations as noted in the descriptions.

## Standard push

The all-encompassing push message. These appear on your user's device with a notification sound and message which slides in or appears in a notification bar or stack.

**Supported on:** Web, Android, iOS

For more information, see [Create a push message]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/).

## Web push

These push messages appear in web apps or browsers. They require permission to reach the customer. Web push does not work if the user is using a hidden browser.

**Supported on:** Web

For more information, see [Web push notifications]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/web/).

## Push primer campaigns

In-app message campaigns used to gain explicit push opt-in or opt-out signal from users. Through the primer, you can avoid sending notifications to users that are likely to turn off push through the device settings. For iOS, push campaigns are relevant as foreground push notifications (such as notifications that wake up the device) are not enabled until a user explicitly opts into iOS's native push prompt.

**Supported on:** Web, Android, iOS

For more information, see [Push primer in-app messages]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages/).

## Push Stories

Push Stories are immersive messages that take your user through a visual journey in the form of a carousel. These are available for mobile devices only.

**Supported on:** iOS, Android

For more information, see [Push stories]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/push_stories/).

## Push with action buttons

Push with action buttons are messages that let you provide options to your users and offer several calls to action.

**Supported on:** Web, Android, iOS

For more information, see [Push action buttons]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/push_action_buttons/).

## Rich push notifications

Rich push notifications are notifications with immersive images and creative content that can expand beyond an icon and call to action text.

**Supported on:** iOS, Android

For more information, see [Create rich notifications for iOS]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/rich_notifications/) or [Create rich notifications for Android]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android/rich_notifications/).

## Provisional push notifications for iOS

Introduced by Apple in iOS 12, provisional authorization automatically occurs on install for iOS apps, allowing brands to send silent notifications without displaying a push prompt to users. When the silent push is sent and viewed in the device's notification tray, users are given the option to allow or discontinue push notifications.

**Supported on:** iOS

For more information, see [iOS notification options]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/notification_options/#provisional-push).

## HTML push notifications

HTML push notifications are push messages that are hard coded in HTML and do not use the pre-set push templates that Braze provides. Having the option to create HTML push notifications allows your company to have full creative freedom and consistent branding when it comes to how you want these push messages to look.

**Supported on:** Android

## Notification IDs and channel IDs

Notification IDs and channel IDs let you replace or update push notifications already received, but not opened, by the user.

**Supported on:** iOS, Android

For more information, see [Notification channels]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android/notification_channels/) and [Advanced push campaign settings]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android/advanced_campaign_settings/).

## Background or silent push notifications {#background-push-notifications}

Push notifications that are not rendered on the device. Usually used to send packets of information down to the app for background processes and uninstall tracking. A background-enabled push token is required for a background or silent push to be sent.

**Supported on:** Web, Android, iOS

For more information, see [Silent push notifications]({{site.baseurl}}/developer_guide/push_notifications/silent/).

## Wearable push notifications

These push notifications allow brands to send messages directly to wearable devices like the Apple Watch.

**Supported on:** iOS
