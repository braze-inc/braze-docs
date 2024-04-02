---
nav_title: visionOS
article_title: visionOS
page_order: 7.2
platform: 
  - iOS
description: "visionOS support"
---

# visionOS

With the release of the Apple Vision Pro, Apple has introduced a new platform called visionOS. Starting with the Braze Swift SDK [8.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#800), visionOS is supported as a first class platform.

> Please refer to our [sample apps]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/sample_apps/) for working examples of visionOS integration.

## Supported Features

Most of the features available on iOS are supported on visionOS. This includes:
- Analytics (sessions, custom events, purchases, etc.)
- In-App Messaging (data models and UI)
- Content Cards (data models and UI)
- Push Notifications
- Feature Flags
- Location Analytics

## Partially Supported Features

The following features are partially supported on visionOS:
- Rich Push Notifications
  - Images display as expected
  - GIFs and videos display the preview thumbnail, it is not currently possible to play the media
  - Audio playback is not supported
- Push Stories
  - The _Next_ button to navigate between Push Story pages is not working as intended
  - Scrolling and clicking on the Push Story page works as expected

We expect that future visionOS updates will address these limitations.

## Unsupported Features

Currently, Geofences Monitoring is not supported. The geofences related CoreLocation APIs are not made available by Apple on visionOS.

