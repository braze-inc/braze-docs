---
nav_title: Carthage Integration
platform: iOS
page_order: 0
search_rank: 5
---

# Carthage Integration
You can integrate the Braze SDK using Carthage by including the following in your `Cartfile`:

```
github "Appboy/Appboy-iOS-SDK" "3.15.0"
```

For further instructions using Carthage, please refer to their [user guide][9] on Github.

Once you've synced the Braze SDK release artifacts (we support Carthage via a zip of release artifacts attached to our Github releases), integrate the `Appboy_iOS_SDK.framework` and `SDWebImage.framework` into your project. Then, in your Application delegate do:


{% tabs %}
{% tab OBJECTIVE-C %}

```objc
#import <Appboy_iOS_SDK/AppboyKit.h>

...

// In `application:didFinishLaunchingWithOptions:`
[Appboy startWithApiKey:@"YOUR-API-KEY"
         inApplication:application
         withLaunchOptions:launchOptions];
```

{% endtab %}
{% tab swift %}

```swift
import Appboy_iOS_SDK

...

// In `application:didFinishLaunchingWithOptions:`
Appboy.start(withApiKey: "YOUR-API-KEY",
              in:application,
              withLaunchOptions:launchOptions)
```

{% endtab %}
{% endtabs %}

## Dependency-Free Integration
If you want to use SDWebImage in your project along with the Braze SDK, you can install a thin version of the Braze Carthage framework. To do so, include the following lines in your Cartfile:

```
binary "https://raw.githubusercontent.com/Appboy/appboy-ios-sdk/master/appboy_ios_sdk.json"
github "rs/SDWebImage"
```

## Core Only Integration
If you want to use the Core SDK without any UI components, you can install the core version of the Braze Carthage framework by including the following line in your Cartfile:

```
binary "https://raw.githubusercontent.com/Appboy/appboy-ios-sdk/master/appboy_ios_sdk_core.json"
```

[1]: http://cocoapods.org/
[2]: https://www.ruby-lang.org/en/installation/
[3]: http://guides.cocoapods.org/using/getting-started.html "CocoaPods Installation Directions"
[4]: http://guides.cocoapods.org/syntax/podfile.html
[5]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/headers/AppboyKitLibrary/Appboy.h#L32
[6]: https://dashboard-01.braze.com/app_settings/app_settings/ "App Settings"
[7]: https://github.com/Appboy/appboy-ios-sdk/blob/master/Example/Stopwatch/AppDelegate.m
[8]: {{ site.baseurl }}/developer_guide/platform_integration_guides/unity/ios/sdk_integration/#manual-sdk-
[9]: https://github.com/Carthage/Carthage#if-youre-building-for-ios-tvos-or-watchos
[12]: #appboy-podfiles-for-non-64-bit-apps
[13]: https://github.com/Appboy/appboy-ios-sdk/blob/master/HelloSwift/Podfile
[14]: https://github.com/Appboy/appboy-ios-sdk/blob/master/Example/Podfile "Example Podfile"
[15]: {% image_buster /assets/img_archive/podsworkspace.png %}
[17]: http://guides.cocoapods.org/using/getting-started.html#updating-cocoapods
[19]: https://developer.apple.com/library/ios/documentation/swift/conceptual/buildingcocoaapps/MixandMatch.html
[20]: {% image_buster /assets/img_archive/IDFAInBuildSetting.png %}
[21]: {{ site.baseurl }}/partners/technology_partners/
[25]: http://guides.cocoapods.org/using/troubleshooting.html "CocoaPods Troubleshooting Guide"
[27]: https://github.com/Appboy/appboy-ios-sdk/blob/master/CHANGELOG.md "iOS Changelog"
[28]: #apple-watch-sdk
[29]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/headers/AppboyKitLibrary/ABKIDFADelegate.h
[30]: https://github.com/Appboy/appboy-ios-sdk/blob/master/Example/Stopwatch/IDFADelegate.m
[31]: https://developer.apple.com/library/content/qa/qa1795/_index.html
