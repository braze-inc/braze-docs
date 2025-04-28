---
nav_title: Upgrading to iOS 18
article_title: Upgrading to iOS 18
page_order: 7.1
platform: 
  - iOS
description: "This article covers insights into the iOS 18 release to help you upgrade your SDK seamlessly."
---

# Upgrading to iOS 18

> Curious about how Braze is preparing for the upcoming iOS release? This article summarizes our insights into the iOS 18 release to help you create a seamless experience for you and your users.

Apple's [WWDC](https://developer.apple.com/wwdc24/) took place June 9th - 11th 2024. Learn more about their announcements in our [blog post](https://www.braze.com/resources/articles/wwdc-announcements-bring-apple-intelligence-rcs-and-more-to-ios-18), or read on to learn how you can leverage iOS 18 with Braze.

## Changes in iOS 18

### Live Activities on Apple Watch

[Live Activities](https://www.braze.com/docs/developer_guide/push_notifications/live_notifications/?sdktab=swift) will be supported on watchOS 11. No additional setup is required. However, Apple offers the option to customize the watch interface.

### Apple Vision Pro

The Vision Pro is now available in China, Japan, Singapore, Australia, Canada, France, Germany, and the UK. Check out our blog to see how [Braze supports visionOS](https://www.braze.com/resources/articles/building-braze-a-new-era-of-customer-engagement-braze-announces-visionos-support).

### iPhone notifications on macOS

Apple's new [iPhone mirroring](https://www.apple.com/newsroom/2024/06/macos-sequoia-takes-productivity-and-intelligence-on-mac-to-new-heights/) feature allows users to receive iPhone notifications on their macOS devices. Keep in mind, some media types, such as Push Story images and GIFs, are not supported, since they can't be rendered as a macOS notification.

### Apple Intelligence

[Apple Intelligence](https://developer.apple.com/documentation/Updates/Apple-Intelligence) is now available for devices running iOS 18.1 and later.

As a Braze user, the most important new feature for you to be aware of are [notification summaries](https://support.apple.com/en-us/108781), which uses on-device processing to automatically group and generate text summaries for related push notifications sent from a single app. End-users can tap to expand a summary and view each push notification as they were originally sent.

Due to how these summaries are generated, you won't have control over their specific behavior or the generated text. However, this will not impact any analytics or reporting features, such as push-click tracking.

![A sample screenshot of a push notification preview summary.]({% image_buster /assets/img/apple/apple_intelligence/notification_preview_summary.png %})
