---
nav_title: iOS 15 upgrade guide
article_title: iOS 15 SDK Upgrade Guide
page_order: 7
platform: iOS
description: "This reference article covers the new iOS 15 OS updates, required SDK updates, and new features."
hidden: true
noindex: true
---

# iOS 15 SDK upgrade guide

> This guide outlines changes introduced in iOS 15 (WWDC21) and the required upgrade steps for your Braze iOS SDK integration. For a complete list of new iOS 15 updates, see Apple's [iOS 15 release notes](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-15-release-notes).


## Transparency changes to UI navigations

As part of our annual testing of iOS betas, we have identified a change made by Apple which causes certain UI navigation bars to appear transparent instead of opaque. This will be visible on iOS 15 when using the Braze default UI for Content Cards, or when web deep links are opened inside your app instead of in a separate browser app.

To avoid this visual change in iOS 15, we strongly recommend you upgrade to the [Braze iOS SDK v4.3.2](https://github.com/Appboy/appboy-ios-sdk/releases/tag/4.3.2) as soon as possible, before users begin to upgrade their phone to the new iOS 15 operating system.

## New notification settings {#notification-settings}

iOS 15 introduced new notification features to help users stay focused and avoid frequent interruptions throughout the day. We're excited to offer support for these new features. These features do not require any additional SDK upgrades and will only be applied to users on iOS 15 devices.

### Focus modes {#focus-mode}

iOS 15 users can now create "Focus Modes"—custom profiles used to determine which notifications they want to break through their focus and display prominently.

![]({% image_buster /assets/img/ios/ios15-notification-settings.png %}){: style="float:right;max-width:25%;margin-left:15px;border:0"}

### Interruption levels {#interruption-levels}

In iOS 15, push notifications can be sent with one of four interruption levels:

* **Passive** (new) - No sound, no vibration, no screen waking, no break through of focus settings.
* **Active** (default) - Allows sound, vibration, screen waking, no break through of focus settings.
* **Time-Sensitive** (new) - Allows sound, vibration, screen waking, can break through system controls if allowed.
* **Critical** - Allows sound, vibration, screen waking, can break through system controls, and bypass ringer switch.

See [iOS notification options]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/#interruption-level) to learn more about how to set this option in iOS Push.

### Notification summary {#notification-summary}

![]({% image_buster /assets/img/ios/ios15-notification-summary.png %}){: style="float:right;max-width:25%;margin-left:15px;border:0"}

In iOS 15, users can (optionally) choose certain times throughout the day to receive a summary of notifications. Notifications that don't require immediate attention (such as sent as "Passive" or while the user is in Focus Mode) will be grouped to prevent constant interruptions throughout the day.

For each notification you send, you'll soon be able to specify a "relevance score" to control which notification should appear at the top of the summary.

See [iOS Notification Options]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/#relevance-score) to learn more about how to set a notification's "relevance score".

## Location buttons {#location-buttons}

iOS 15 introduces a new, convenient way for users to temporarily grant location access within an app. 

The new location button builds off the existing "Allow Once" permission without repeatedly prompting users who click multiple times in the same session.

For more information, watch Apple's [Meet the Location Button](https://developer.apple.com/videos/play/wwdc2021/10102/) video from this year's Worldwide Developer Conference (WWDC).

{% alert tip %}
This feature gives you an extra chance to prompt users for permission! Users who have previously declined location permissions before iOS 15 will be shown a prompt when clicking the location button as an opportunity to reset the permission from the declined state one last time.
{% endalert %}

### Using location buttons with Braze

No additional integration is required when using location buttons with Braze. Your app should continue passing a user's location (once they've granted permission) as usual.

According to Apple, for users who have already shared background location access, the "While Using App" option will continue to grant that level of permission after they upgrade to iOS 15.

## Apple mail {#mail}

This year, Apple has announced many updates to email tracking and privacy. For more information, check out our [blog post](https://www.braze.com/resources/articles/9-ways-email-marketers-can-respond-to-apples-mail-privacy-protection-feature).

## Safari IP address location

In iOS 15, users will be able to configure Safari to anonymize or generalize the location determined from their IP addresses. Keep this in mind when using location-based targeting or segmentation.

