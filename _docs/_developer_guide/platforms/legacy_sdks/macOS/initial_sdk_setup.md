---
nav_title: Initial SDK setup
article_title: Initial SDK Setup for MacOS
platform: MacOS
page_order: 0
page_type: reference
description: "This reference article provides resources for initial integration of the Braze SDK on macOS."
search_rank: 1
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Initial SDK setup

> This reference article covers how to install the Braze SDK for MacOS. 

As of version [3.32.0](https://github.com/Appboy/appboy-ios-sdk/releases/tag/3.32.0), the Braze SDK supports macOS for apps using [Mac Catalyst](https://developer.apple.com/mac-catalyst/) when integrating through Swift Package Manager. Currently, the SDK does not support Mac Catalyst when using CocoaPods or Carthage.

{% alert note %}
To build your app with Mac Catalyst, reference <a href="https://developer.apple.com/documentation/uikit/mac_catalyst">Apple's documentation</a>.
{% endalert %}

Once your app supports Catalyst, follow [these instructions to use Swift Package Manager]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/sdk_integration/?tab=swift%20package%20manager/) to import the Braze SDK into your app.

## Supported features

Braze supports [push notifications]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift), [Content Cards]({{site.baseurl}}/developer_guide/platforms/swift/content_cards/#content-cards-data-model), [in-app messages]({{site.baseurl}}/developer_guide/analytics/tracking_location/?sdktab=swift), and [automatic location collection]({{site.baseurl}}/developer_guide/analytics/tracking_location/?sdktab=swift) when running on Mac Catalyst.

Note that Push Stories, rich push, and geofences are not supported on macOS.

[1]:https://github.com/Appboy/appboy-ios-sdk/releases/tag/3.32.0
[2]:https://developer.apple.com/mac-catalyst/
