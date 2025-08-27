---
nav_title: iOS 16 upgrade guide
article_title: iOS 16 Upgrade Guide
page_order: 7
platform: 
  - iOS
description: "This reference article covers iOS 16, how to upgrade, SDK updates, and more."
hidden: true
noindex: true
---

# iOS 16 SDK upgrade guide

> This guide describes relevant changes introduced in iOS 16 (2022) and the impact on your Braze iOS SDK integration. Refer to the [iOS 16 release notes](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-16-release-notes) for a full migration guide.

## Changes in iOS 16

### Safari Web Push {#safari-web-push}

Apple has announced two changes to their Web Push functionality.

#### Desktop Web Push (MacOS) {#macos-push}

Previously, Apple supported push notifications on macOS (desktop) using their own Safari push APIs.

Beginning in macOS Ventura (released October 24, 2022), [Safari has added support](https://webkit.org/blog/12824/news-from-wwdc-webkit-features-in-safari-16-beta/#web-push-for-macos) for Web Push APIs in addition to Safari push. This is an existing cross-browser API standard used in other popular browsers.

If you're already sending Web Push for Safari through Braze, no change is needed.

#### Mobile Web Push (iOS and iPadOS) {#ios-push}

Previously, Safari on iPhone and iPad did not support receiving push notifications.

In 2023, Apple will be adding support for Web Push on iPhone and iPad devices through Safari.

Braze will support this new iOS and iPadOS Web Push without requiring additional changes or upgrades.

## Preparing for iOS 16 {#next-steps}

While you do not need to upgrade your Braze iOS SDK for iOS 16, there are two other exciting updates:

1. Braze has launched a [new Swift SDK](https://github.com/braze-inc/braze-swift-sdk). This brings improved performance, new features, and many improvements.
2. Our Braze Swift SDK supports a new ["no-code" push primer feature]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/)!

