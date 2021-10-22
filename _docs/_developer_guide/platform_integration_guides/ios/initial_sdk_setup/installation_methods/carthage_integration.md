---
nav_title: Carthage Integration
article_title: Carthage Integration for iOS
platform: iOS
page_order: 1
description: "This reference article shows how to integrate the Braze SDK using Carthage for iOS."

---

# Carthage integration

Starting from version 3.24.0 of the SDK, you can integrate the Braze SDK using Carthage by including the following in your `Cartfile`:
```
binary "https://raw.githubusercontent.com/Appboy/appboy-ios-sdk/master/appboy_ios_sdk_full.json"
```

You can integrate earlier versions of the SDK by including the following in your `Cartfile`:
```
github "Appboy/Appboy-iOS-SDK" "<BRAZE_IOS_SDK_VERSION>"
```

Make sure to replace `<BRAZE_IOS_SDK_VERSION>` with the latest version of the Braze iOS SDK in "x.y.z" format. Release versions are available [here](https://github.com/Appboy/appboy-ios-sdk/releases).

For further instructions using Carthage, please refer to their [user guide][9] on Github.

Once you've synced the Braze SDK release artifacts (we support Carthage via a zip of release artifacts attached to our Github releases), integrate the `Appboy_iOS_SDK.framework` and `SDWebImage.framework` into your project.

## Next steps

Follow the instructions for [Completing the Integration]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/completing_integration/).

## Dependency-free integration
If you want to use SDWebImage in your project along with the Braze SDK, you can install a thin version of the Braze Carthage framework. To do so, include the following lines in your Cartfile:

```
binary "https://raw.githubusercontent.com/Appboy/appboy-ios-sdk/master/appboy_ios_sdk.json"
github "SDWebImage/SDWebImage"
```

## Core only integration
If you want to use the Core SDK without any UI components, you can install the core version of the Braze Carthage framework by including the following line in your Cartfile:

```
binary "https://raw.githubusercontent.com/Appboy/appboy-ios-sdk/master/appboy_ios_sdk_core.json"
```

[9]: https://github.com/Carthage/Carthage#if-youre-building-for-ios-tvos-or-watchos
