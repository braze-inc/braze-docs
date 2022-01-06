---
nav_title: Other SDK Customizations
article_title: Other SDK Customizations for iOS
platform: iOS
description: "This document covers SDK customizations such as Log Level, IDFA Collection, and other customizations."
page_order: 3

---

# Other SDK customizations

## Braze Log Level

The default log level for the Braze iOS SDK is Minimal, or `8` in the chart below. This level suppresses most logging so that no sensitive information is logged in a production released application.

See the following list of available log levels:

### Log Levels

| Level    | Description |
|----------|-------------|
| 0        | Verbose. All log information will be logged to the iOS console.  |
| 1        | Debug. Debug and higher log information will be logged to the iOS console.  |
| 2        | Warning. Warning and higher log information will be logged to the iOS console.  |
| 4        | Error. Error and and higher log information will be logged to the iOS console.  |
| 8        | Minimal. Minimal information will be logged to the iOS console. The SDK's default setting. |
{: .reset-td-br-1 .reset-td-br-2}

### Verbose Logging

You can configure log level to any available value. However, setting log level to Verbose, or `0`, can be very useful for debugging issues with your integration. This level is only intended to be used in development environments and should not be set in a released application.

### Setting Log Level

Log level can be assigned either at compile time or at runtime:

{% tabs local %}
{% tab Compile Time %}

#### Setting Log Level at compile time

Add a dictionary named `Braze` to your `Info.plist` file. Inside the `Braze` Dictionary, add the `LogLevel` String subentry and set the value to `0`. 

{% alert note %}
Prior to Braze iOS SDK v4.0.2, the dictionary key `Appboy` must be used in place of `Braze`.
{% endalert %} 

Example `Info.plist` contents:

```
<key>Braze</key>
<dict>
	<key>LogLevel</key>
	<string>0</string>
</dict>
```

{% endtab %}
{% tab Runtime %}

#### Setting Log Level at runtime

Add the `ABKLogLevelKey` inside the `appboyOptions` parameter passed to `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:`. Set its value to the integer `0`.

{% subtabs %}
{% subtab OBJECTIVE-C %}

```objc
NSMutableDictionary *appboyOptions = [NSMutableDictionary dictionary];
appboyOptions[ABKLogLevelKey] = @(0);
[Appboy startWithApiKey:@"YOUR-API-KEY"
          inApplication:application
      withLaunchOptions:launchOptions
      withAppboyOptions:appboyOptions];
```

{% endsubtab %}
{% subtab swift %}

```swift
let appboyOptions: [AnyHashable: Any] = [
  ABKLogLevelKey : 0
]
Appboy.start(withApiKey: "YOUR-API-KEY", in:application, withLaunchOptions:launchOptions, withAppboyOptions:appboyOptions)
```

{% endsubtab %}
{% endsubtabs %}

{% alert note %}
Log level can only be set at runtime with Braze iOS SDK v4.4.0 or newer. If using an earlier version of the SDK, set log level at compile time instead.
{% endalert %} 

{% endtab %}
{% endtabs %}

## Optional IDFA collection

IDFA Collection is optional within the Braze SDK and disabled by default. IDFA Collection is only required within Braze if you intend to utilize our [install attribution integrations][21]. If you opt to store your IDFA, we will store it free of charge so you may take advantage of these options immediately upon release without additional development work.

As a result, we recommend continuing to collect the IDFA if you meet any of the following criteria:

- You are attributing app installation to a previously served advertisement
- You are attributing an action within the application to a previously served advertisement

### iOS 14 AppTrackingTransparency
In the future, Apple will require a new permission prompt in order to collect IDFA. For now, prompting for IDFA permission with `AppTrackingTransparency` is not required, but you should be prepared for a future iOS release from Apple which will require user opt-in.

When the `AppTrackingTransparency` prompt is required, in addition to implementing Braze's `ABKIDFADelegate` protocol, your application will need to request authorization using Apple's `ATTrackingManager` in the App Tracking Transparency framework. For more information, please reference this [Braze iOS 14 guide]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/ios_14/#idfa-and-app-tracking-transparency), [Apple's Overview](https://developer.apple.com/app-store/user-privacy-and-data-use/), and [Apple's Developer Documentation](https://developer.apple.com/documentation/apptrackingtransparency). In iOS 14, collecting IDFA will require building with Xcode 12.

The prompt for App Tracking Transparency authorization also requires an `Info.plist` entry to explain your usage of the identifier:

```
<key>NSUserTrackingUsageDescription</key>
<string>To retarget ads and build a global profile to better serve you things you would like.</string>
```

### Implementing IDFA collection

Follow these steps to implement IDFA Collection:

##### Step 1: Implement ABKIDFADelegate

Create a class that conforms to the [`ABKIDFADelegate`][29] protocol.

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
#import "IDFADelegate.h"
#import <AdSupport/ASIdentifierManager.h>
#import <AppTrackingTransparency/AppTrackingTransparency.h>

@implementation IDFADelegate

- (NSString *)advertisingIdentifierString {
  return [[[ASIdentifierManager sharedManager] advertisingIdentifier] UUIDString];
}

- (BOOL)isAdvertisingTrackingEnabledOrATTAuthorized {
  if (@available(iOS 14, *)) {
    return [ATTrackingManager trackingAuthorizationStatus] == ATTrackingManagerAuthorizationStatusAuthorized;
  }
  return [[ASIdentifierManager sharedManager] isAdvertisingTrackingEnabled];
}

@end
```

{% endtab %}
{% tab swift %}

```swift
import Appboy_iOS_SDK
import AdSupport
import AppTrackingTransparency

class IDFADelegate: NSObject, ABKIDFADelegate {
   func advertisingIdentifierString() -> String {
    return ASIdentifierManager.shared().advertisingIdentifier.uuidString
  }

  func isAdvertisingTrackingEnabledOrATTAuthorized() -> Bool {
    if #available(iOS 14, *) {
      return ATTrackingManager.trackingAuthorizationStatus ==  ATTrackingManager.AuthorizationStatus.authorized
    }
    return ASIdentifierManager.shared().isAdvertisingTrackingEnabled
  }
}
```
{% endtab %}
{% endtabs %}

##### Step 2: Set the delegate during Braze initialization

In the `appboyOptions` dictionary passed to `startWithApiKey:inApplication:withAppboyOptions:`, set the `ABKIDFADelegateKey` key to an instance of your `ABKIDFADelegate` conforming class.

## Approximate iOS SDK size {#ios-sdk-size}

The approximate iOS SDK framework file size is 30MB and the approximate .ipa (addition to app file) size is between 1MB and 2MB.

Braze measures the size of our iOS SDK by observing the SDK's effect on `.ipa` size, per [Apple's recommendations on app sizing][31]. If you are calculating the iOS SDK's size addition to your application, we recommend following the steps under ["Getting an App Size Report"][31] to compare the size difference in your `.ipa` before and after integrating the Braze iOS SDK. When comparing sizes from the App Thinning Size Report, we also recommend looking at app sizes for thinned `.ipa` files, as universal `.ipa` files will be larger than the binaries downloaded from the App Store and installed onto user devices.

> If you are integrating via CocoaPods with `use_frameworks!`, set `Enable Bitcode = NO` in target's Build Settings for accurate sizing.


[21]: {{site.baseurl}}/partners/advertising_technologies/attribution/adjust/
[29]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKIDFADelegate.h
[31]: https://developer.apple.com/library/content/qa/qa1795/_index.html
