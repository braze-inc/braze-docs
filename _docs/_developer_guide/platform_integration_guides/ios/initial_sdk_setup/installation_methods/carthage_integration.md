---
nav_title: Carthage Integration
article_title: Carthage Integration for iOS
platform: iOS
page_order: 1
description: "This reference article shows how to integrate the Braze SDK using Carthage for iOS."

---

# Carthage Integration

Starting from version 4.4.0, the Braze SDK supports XCFrameworks when integrating via Carthage. To import the full SDK, include these lines in your `Cartfile`:
```
binary "https://raw.githubusercontent.com/Appboy/appboy-ios-sdk/master/appboy_ios_sdk.json"
github "SDWebImage/SDWebImage"
```

Please reference the [Carthage quick start guide][1] for more detailed instructions about importing the SDK. When migrating from version `4.3.4` of the Braze SDK or before, follow the [Carthage migration guide for XCFrameworks][2].

For platform-specific usage of Carthage, refer to their [user guide][3] on Github.

### Previous versions

For versions `3.34.0` through `4.3.4`, simply include this one line in your `Cartfile`:
```
binary "https://raw.githubusercontent.com/Appboy/appboy-ios-sdk/master/appboy_ios_sdk_full.json"
```

You can integrate earlier versions of the SDK by including the following in your `Cartfile`:
```
github "Appboy/Appboy-iOS-SDK" "<BRAZE_IOS_SDK_VERSION>"
```

> Make sure to replace `<BRAZE_IOS_SDK_VERSION>` with the appropriate version of the Braze iOS SDK in "x.y.z" format. Release versions are available [here][4].

## Next Steps

Follow the instructions for [Completing the Integration][5].

## Dependency-Free Integration
If you want to use the Braze SDK without the `SDWebImage` dependency, install a thin version of the Braze Carthage framework. To do so, include the following line in your Cartfile:

```
binary "https://raw.githubusercontent.com/Appboy/appboy-ios-sdk/master/appboy_ios_sdk.json"
```

## Core Only Integration
If you want to use the Core SDK without any UI components, install the core version of the Braze Carthage framework by including the following line in your Cartfile:

```
binary "https://raw.githubusercontent.com/Appboy/appboy-ios-sdk/master/appboy_ios_sdk_core.json"
```

[1]: https://github.com/Carthage/Carthage#quick-start
[2]: https://github.com/Carthage/Carthage#migrating-a-project-from-framework-bundles-to-xcframeworks
[3]: https://github.com/Carthage/Carthage#if-youre-building-for-ios-tvos-or-watchos
[4]: https://github.com/Appboy/appboy-ios-sdk/releases
[5]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/completing_integration/
