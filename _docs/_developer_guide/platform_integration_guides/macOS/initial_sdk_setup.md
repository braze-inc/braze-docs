---
nav_title: Initial SDK Setup
platform: MacOS
page_order: 0
---

As of version [3.32.0][1], the Braze SDK offers MacOS support for apps using [Mac Catalyst][2], which allows iPad apps to be built for Mac.

{% alert note %}
To build your app with Mac Catalyst, please reference [Apple's documentation here][3].
{% endalert %}

# Initial SDK Setup

To import the Braze SDK into your app, follow the instructions to use [Swift Package Manager][4]. Currently, the Braze SDK does not support Mac Catalyst when using Cocoapods or Carthage.

To add push notifications to your Catalyst app, follow our normal [iOS SDK instructions here][5]. For enabling automatic location collection, follow the [setup instructions here][6].

Please note that the Geofences feature and Push Stories are not supported when building with Mac Catalyst.

[1]:https://github.com/Appboy/appboy-ios-sdk/releases/tag/3.32.0
[2]:https://developer.apple.com/mac-catalyst/
[3]:https://developer.apple.com/documentation/uikit/mac_catalyst
[4]:https://www.braze.com/docs/developer_guide/platform_integration_guides/ios/initial_sdk_setup/swift_package_manager/
[5]:https://www.braze.com/docs/developer_guide/platform_integration_guides/ios/push_notifications/integration/
[6]:https://www.braze.com/docs/developer_guide/platform_integration_guides/ios/analytics/location_tracking/