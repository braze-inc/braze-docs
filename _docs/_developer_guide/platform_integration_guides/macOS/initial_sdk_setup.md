---
nav_title: Initial SDK Setup
article_title: Initial SDK Setup for MacOS
platform: MacOS
page_order: 0
page_type: reference
description: "This page provides resources for initial SDK setup steps on macOS."

---

# Initial SDK setup

As of version [3.32.0][1], the Braze SDK supports macOS for apps using [Mac Catalyst][2] when integrating through Swift Package Manager. Currently, the SDK does not support Mac Catalyst when using Cocoapods or Carthage.

{% alert note %}
To build your app with Mac Catalyst, reference <a href="https://developer.apple.com/documentation/uikit/mac_catalyst">Apple's documentation</a>.
{% endalert %}

Once your app supports Catalyst, follow [these instructions to use Swift Package Manager][3] to import the Braze SDK into your app.

## Supported features

Braze supports [push notifications][4], [Content Cards][7], [in-app messages][5], and [automatic location collection][5] when running on Mac Catalyst.

Please note that Push Stories, rich push, and geofences are not supported on macOS.

[1]:https://github.com/Appboy/appboy-ios-sdk/releases/tag/3.32.0
[2]:https://developer.apple.com/mac-catalyst/
[3]:{{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/installation_methods/swift_package_manager/
[4]:{{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/
[5]:{{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/location_tracking/
[6]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/overview/
[7]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/content_cards/data_model/
