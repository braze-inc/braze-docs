---
nav_title: Initial SDK Setup
platform: MacOS
page_order: 0
---

The Braze SDK offers MacOS support using [Mac Catalyst][1], which allows you to build iPad apps for Mac.

{% alert note %}
To build your app with Mac Catalyst, please reference [Apple's documentation here][2].
{% endalert %}

# Initial SDK Setup

{ WIP }

To import the Braze SDK into your app, follow the instructions to use [Swift Package Manager][3] or [Cocoapods][4]. Mac Catalyst is not supported when using Carthage to import the SDK.

^ Cocoapods will only work once we add Cocoapods+XCFramework (4.0.0-beta) - make a TODO once we add support later


[1]:https://developer.apple.com/mac-catalyst/
[2]:https://developer.apple.com/documentation/uikit/mac_catalyst
[3]:https://www.braze.com/docs/developer_guide/platform_integration_guides/ios/initial_sdk_setup/swift_package_manager/
