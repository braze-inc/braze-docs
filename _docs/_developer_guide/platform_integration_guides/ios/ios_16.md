---
nav_title: iOS 16 Upgrade Guide
article_title: iOS 16 Upgrade Guide
page_order: 9
platform: 
  - iOS
description: "This article covers iOS 16, SDK updates, and more."
---

# iOS 16 SDK upgrade guide

This guide describes relevant changes introduced in iOS 16 (2022) and the impact on your Braze iOS SDK integration. Refer to the [iOS 16 Release Notes][2] for a full migration guide.

{% alert note %}
iOS 16 is still in beta. Check back periodically as Apple APIs may change with future beta versions.<br>(Updated June 22, 2022)
{% endalert %}

## Changes in iOS 16

As of iOS 16 Beta 1, there were no functional changes in iOS 16 that affect your Braze SDK integration. This may change as Apple releases new beta versions of iOS 16, so check back here periodically.

### Safari Web Push {#safari-web-push}

Apple has announced two changes to their Web Push functionality.

#### Desktop Web Push (MacOS) {#macos-push}

Previously, Apple supported push notifications on MacOS (desktop) using their own Safari Push APIs.

Beginning in MacOS Ventura, [Safari will add support](https://webkit.org/blog/12824/news-from-wwdc-webkit-features-in-safari-16-beta/#web-push-for-macos) for Web Push APIs in addition to Safari Push. This is an existing cross-browser API standard used in other popular browsers.

If you're already sending Web Push for Safari through Braze, no change is needed.

#### Mobile Web Push (iOS and iPadOS) {#ios-push}

In 2023, Apple will be adding support for Web Push on iPhone and iPad devices through Safari. Previously, mobile and tablet devices did not support sending push notifications to Safari.

Braze will support this new iOS and iPadOS Web Push with no additional changes or upgrades required.

## Preparing for iOS 16 {#next-steps}

Based on the current iOS Beta, you will not need to upgrade your Braze iOS SDK. However, there are two other exciting updates:

1. Braze has launched a [new Swift SDK][3]. This brings improved performance, new features, and many improvements.

2. Our Braze Swift SDK will soon support a new ["no-code" push primer feature][7]!

[1]: https://github.com/Appboy/appboy-ios-sdk/blob/master/CHANGELOG.md
[3]: https://github.com/braze-inc/braze-swift-sdk
[2]: https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-16-release-notes
[7]: https://www.braze.com/docs/user_guide/message_building_by_channel/push/push_primer_messages/
