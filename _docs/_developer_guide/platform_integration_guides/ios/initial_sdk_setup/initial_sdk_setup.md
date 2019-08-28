---
nav_title: Set Up
platform: iOS
page_order: 0
search_rank: 5
---

# Initial SDK Setup

{% alert important %}
The iOS SDK will add 1MB to 2MB to the the app IPA file, in addition to App File, and 30MB for the Framework.
{% endalert %}

{% include archive/apple/initial_setup.md platform="iOS" %}



[1]: http://cocoapods.org/
[2]: https://www.ruby-lang.org/en/installation/
[3]: http://guides.cocoapods.org/using/getting-started.html "CocoaPods Installation Directions"
[4]: http://guides.cocoapods.org/syntax/podfile.html
[5]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/headers/AppboyKitLibrary/Appboy.h#L32
[6]: https://dashboard-01.braze.com/app_settings/app_settings/ "App Settings"
[7]: https://github.com/Appboy/appboy-ios-sdk/blob/master/Example/Stopwatch/AppDelegate.m
[8]: {{ site.baseurl }}/developer_guide/platform_integration_guides/unity/ios/sdk_integration/#manual-sdk-integration
[12]: #appboy-podfiles-for-non-64-bit-apps
[13]: https://github.com/Appboy/appboy-ios-sdk/blob/master/HelloSwift/Podfile
[14]: https://github.com/Appboy/appboy-ios-sdk/blob/master/Example/Podfile "Example Podfile"
[15]: {% image_buster /assets/img_archive/podsworkspace.png %}
[17]: http://guides.cocoapods.org/using/getting-started.html#updating-cocoapods
[19]: https://developer.apple.com/library/ios/documentation/swift/conceptual/buildingcocoaapps/MixandMatch.html
[20]: {% image_buster /assets/img_archive/IDFAInBuildSetting.png %}
[21]: {{ site.baseurl }}/partners/technology_partners/
[22]: https://github.com/Appboy/appboy-ios-sdk/blob/master/Example/Stopwatch/SocialNetworkViewController.m
[25]: http://guides.cocoapods.org/using/troubleshooting.html "CocoaPods Troubleshooting Guide"
[27]: https://github.com/Appboy/appboy-ios-sdk/blob/master/CHANGELOG.md "iOS Changelog"
[28]: #apple-watch-sdk
[29]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/headers/AppboyKitLibrary/ABKIDFADelegate.h
[30]: https://github.com/Appboy/appboy-ios-sdk/blob/master/Example/Stopwatch/IDFADelegate.m
[31]: https://developer.apple.com/library/content/qa/qa1795/_index.html
