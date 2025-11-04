---
nav_title: Visionos support
article_title: visionOS support
page_order: 7.2
platform: 
  - iOS
description: "This article covers the features supported on visionOS."
---

# visionOS support

> Starting with [Braze Swift SDK 8.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#800), you can leverage Braze with [visionOS](https://developer.apple.com/visionos/), Apple's spacial-computing platform for the Apple Vision Pro. For a sample visionOS app using Braze, see [Sample Apps]({{site.baseurl}}/developer_guide/references/?tab=swift).

## Fully supported features

Most features available on iOS are also available on visionOS, including:

- Analytics (sessions, custom events, purchases, etc.)
- In-App Messaging (data models and UI)
- Content Cards (data models and UI)
- Push Notifications (user-visible with action buttons and silent notifications)
- Feature Flags
- Location Analytics

## Partially supported features

Some features are only partially supported on visionOS, but Apple is likely to address these in the future:

- Rich Push Notifications
  - Images are supported.
  - GIFs and videos display the preview thumbnail, but cannot be played.
  - Audio playback is not supported.
- Push Stories
  - Scrolling and selecting the Push Story page is supported.
  - Navigating between Push Story pages using **Next** is not supported.

## Unsupported features

- Geofences Monitoring is not supported. Apple has not made the Core Location APIs for region monitoring available on visionOS.
- Live Activities are not supported. Currently, ActivityKit is only available on iOS and iPadOS.
