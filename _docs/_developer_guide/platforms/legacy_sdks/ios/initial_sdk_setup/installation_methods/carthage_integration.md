---
nav_title: Carthage
article_title: Carthage Integration for iOS
platform: iOS
page_order: 1
description: "This reference article shows how to integrate the Braze SDK using Carthage for iOS."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Carthage integration

## Import the SDK

Starting from version `4.4.0`, the Braze SDK supports XCFrameworks when integrating via Carthage. To import the full SDK, include these lines in your `Cartfile`:
```
binary "https://raw.githubusercontent.com/Appboy/appboy-ios-sdk/master/appboy_ios_sdk.json"
github "SDWebImage/SDWebImage"
```

Reference the [Carthage quick start guide](https://github.com/Carthage/Carthage#quick-start) for more instructions about importing the SDK.

When migrating from a version prior to `4.4.0`, follow the [Carthage migration guide for XCFrameworks](https://github.com/Carthage/Carthage#migrating-a-project-from-framework-bundles-to-xcframeworks).

{% alert note %}
For more details around the syntax of the `Cartfile` or features such as version pinning, visit the [Carthage documentation](https://github.com/Carthage/Carthage/blob/master/Documentation/Artifacts.md#cartfile). 
For platform-specific usage of Carthage, refer to their [user guide](https://github.com/Carthage/Carthage#if-youre-building-for-ios-tvos-or-watchos).
{% endalert %}

### Previous versions

For versions `3.24.0` through `4.3.4`, include the following in your `Cartfile`:
```
binary "https://raw.githubusercontent.com/Appboy/appboy-ios-sdk/master/appboy_ios_sdk_full.json"
```

To import versions prior to `3.24.0`, include the following in your `Cartfile`:
```
github "Appboy/Appboy-iOS-SDK" "<BRAZE_IOS_SDK_VERSION>"
```

Make sure to replace `<BRAZE_IOS_SDK_VERSION>` with the [appropriate version](https://github.com/Appboy/appboy-ios-sdk/releases) of the Braze iOS SDK in "x.y.z" format.

## Next steps

Follow the instructions for [completing the integration]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/completing_integration/).

## Core only integration

If you want to use the Core SDK without any UI components or dependencies, install the core version of the Braze Carthage framework by including the following line in your `Cartfile`:

```
binary "https://raw.githubusercontent.com/Appboy/appboy-ios-sdk/master/appboy_ios_sdk_core.json"
```

