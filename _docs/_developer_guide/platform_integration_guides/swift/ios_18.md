---
nav_title: iOS 18 Upgrade Guide
article_title: iOS 18 Upgrade Guide
page_order: 7
platform: 
  - iOS
description: "This article covers insights into the iOS 18 release to help you upgrade your SDK seamlessly."
---

# iOS 18 upgrade guide

> Curious about how Braze is preparing for the upcoming iOS release? This article summarizes our insights into the iOS 18 release to help you create a seamless experience for you and your users.


Apple's [WWDC](https://developer.apple.com/wwdc24/) took place June 9th - 11th 2024. Learn more about their announcements in our [blog post](https://www.braze.com/resources/articles/wwdc-announcements-bring-apple-intelligence-rcs-and-more-to-ios-18), or read on to learn how you can leverage iOS 18 with Braze.

## Changes in iOS 18

### Live Activities on Apple Watch

[Live Activities](https://www.braze.com/docs/developer_guide/platform_integration_guides/swift/live_activities/live_activities) will be supported on watchOS 11. No additional setup is required. However, Apple offers the option to customize the watch interface.

### Apple Vision Pro

The Vision Pro is now available in China, Japan, Singapore, Australia, Canada, France, Germany, and the UK. Check out our blog to see how [Braze supports visionOS](https://www.braze.com/resources/articles/building-braze-a-new-era-of-customer-engagement-braze-announces-visionos-support).

### iPhone notifications on macOS

Apple's new [iPhone mirroring](https://www.apple.com/newsroom/2024/06/macos-sequoia-takes-productivity-and-intelligence-on-mac-to-new-heights/) feature allows users to receive iPhone notifications on their macOS devices. Keep in mind, some media types, such as Push Story images and GIFs, are not supported, since they can't be rendered as a macOS notification.

### Apple Intelligence

[Apple Intelligence](https://developer.apple.com/documentation/Updates/Apple-Intelligence) is now available for devices on iOS 18.1 and later. For Braze, the most relevant feature is notification preview summaries, which uses on-device processing to collapse and generate text summaries for groups of related push notifications from a single app. Summaries can be expanded to view the original contents of each individual notification.

Keep in mind, this feature must be manually enabled by the user, meaning you won't have control over the specific behavior or content of your app's notification summary. However, this does not impact analytics or reporting features, such as push-click tracking.

![A sample screenshot of a push notification preview summary.]({% image_buster /assets/img/apple/apple_intelligence/notification_preview_summary.png %})
