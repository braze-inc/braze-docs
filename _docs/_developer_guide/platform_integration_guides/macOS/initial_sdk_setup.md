---
nav_title: Initial SDK Setup
platform: MacOS
page_order: 0
---

# Initial SDK Setup

As of version [3.32.0][1], the Braze SDK supports MacOS for apps using [Mac Catalyst][2], which allows iPad apps to be built for Mac.

{% alert note %}
To build your app with Mac Catalyst, please reference <a href="https://developer.apple.com/documentation/uikit/mac_catalyst">Apple's documentation here</a>.
{% endalert %}

To import the Braze SDK into your app, follow the instructions to use [Swift Package Manager][3]. Currently, the Braze SDK does not support Mac Catalyst when using Cocoapods or Carthage.

## Supported Features

Braze supports push notifications and location features when running on Mac Catalyst. To integrate push in your Catalyst app, follow the [iOS SDK instructions here][4]. For enabling automatic location collection, follow the [setup instructions here][5].

Please note that Push Stories and Geofences are not supported on MacOS.

[1]:https://github.com/Appboy/appboy-ios-sdk/releases/tag/3.32.0
[2]:https://developer.apple.com/mac-catalyst/
[3]:https://www.braze.com/docs/developer_guide/platform_integration_guides/ios/initial_sdk_setup/swift_package_manager/
[4]:https://www.braze.com/docs/developer_guide/platform_integration_guides/ios/push_notifications/integration/
[5]:https://www.braze.com/docs/developer_guide/platform_integration_guides/ios/analytics/location_tracking/