---
nav_title: Completing the integration
article_title: Complete the iOS SDK Integration
platform: iOS
description: "This reference article shows how to finish integrating the Braze SDK after installing it via one of the integration options."
page_order: 2

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Complete the integration

Before following these steps, make sure you have integrated the SDK using either [Carthage]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/carthage_integration/), [CocoaPods]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/cocoapods/), [Swift Package Manager]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/swift_package_manager/), or a [manual]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/manual_integration_options/) integration.

## Step 1: Update your app delegate

{% tabs %}
{% tab OBJECTIVE-C %}

If you are integrating the Braze SDK with CocoaPods, Carthage, or with a [dynamic manual integration]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/manual_integration_options/), add the following line of code to your `AppDelegate.m` file:

```objc
#import "Appboy-iOS-SDK/AppboyKit.h"
```

If you are integrating with Swift Package Manager or with a [static manual integration]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/manual_integration_options/), use this line instead:

```objc
#import "AppboyKit.h"
```

Next, within your `AppDelegate.m` file, add the following snippet within your `application:didFinishLaunchingWithOptions:` method:

```objc
[Appboy startWithApiKey:@"YOUR-APP-IDENTIFIER-API-KEY"
          inApplication:application
      withLaunchOptions:launchOptions];
```

Update `YOUR-APP-IDENTIFIER-API-KEY` with the correct value from your **Manage Settings** page. Check out our [API documentation]({{site.baseurl}}/api/api_key/#the-app-identifier-api-key) for more information on where to find your app identifier API key.

{% endtab %}
{% tab swift %}

If you are integrating the Braze SDK with CocoaPods, Carthage, or with a [dynamic manual integration]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/manual_integration_options/), add the following line of code to your `AppDelegate.swift` file:

```swift
import Appboy_iOS_SDK
```

If you are integrating with Swift Package Manager or with a [static manual integration]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/manual_integration_options/), use this line instead:

```swift
import AppboyKit
```
Refer to the [Apple developer docs](https://developer.apple.com/library/ios/documentation/swift/conceptual/buildingcocoaapps/MixandMatch.html) for more information on using Objective-C code in Swift projects.

Next, in `AppDelegate.swift`, add following snippet to your `application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool`:

```swift
Appboy.start(withApiKey: "YOUR-APP-IDENTIFIER-API-KEY", in:application, withLaunchOptions:launchOptions)
```

Update `YOUR-APP-IDENTIFIER-API-KEY` with the correct value from your **Manage Settings** page. Check out our [API documentation]({{site.baseurl}}/api/api_key/#the-app-identifier-api-key) for more information on where to find your app identifier API key.

{% endtab %}
{% endtabs %}

{% alert note %}
The `sharedInstance` singleton will be nil before `startWithApiKey:` is called, as that is a prerequisite to using any Braze functionality.
{% endalert %}

{% alert warning %}
Be sure to initialize Braze in your application's main thread. Initializing asynchronously can lead to broken functionality.
{% endalert %}


## Step 2: Specify your data cluster

{% alert note %}
Note that as of December 2019, custom endpoints are no longer given out. If you have a pre-existing custom endpoint, you may continue to use it. For more details, refer to our <a href="{{site.baseurl}}/api/basics/#endpoints">list of available endpoints</a>.
{% endalert %}

### Compile-time endpoint configuration (recommended)

If given a pre-existing custom endpoint:
- Starting with Braze iOS SDK v3.0.2, you can set a custom endpoint using the `Info.plist` file. Add the `Braze` dictionary to your `Info.plist` file. Inside the `Braze` dictionary, add the `Endpoint` string subentry and set the value to your custom endpoint URL's authority (for example, `sdk.iad-01.braze.com`, not `https://sdk.iad-01.braze.com`). Note that before Braze iOS SDK v4.0.2, the dictionary key `Appboy` must be used in place of `Braze`.

Your Braze representative should have already advised you of the [correct endpoint]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/).

### Runtime endpoint configuration

If given a pre-existing custom endpoint:
- Starting with Braze iOS SDK v3.17.0+, you can override set your endpoint via the `ABKEndpointKey` inside the `appboyOptions` parameter passed to `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:`. Set the value to your custom endpoint URL's authority (for example, `sdk.iad-01.braze.com`, not `https://sdk.iad-01.braze.com`).

## SDK integration complete

Braze should now be collecting data from your application, and your basic integration should be complete. See the following articles to enable [custom event tracking]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=swift), [push messaging]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration/), and the complete suite of Braze features.

## Customizing Braze on startup

If you wish to customize Braze on startup, you can instead use the Braze initialization method `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:` and pass in an optional `NSDictionary` of Braze startup keys.
{% tabs %}
{% tab OBJECTIVE-C %}

In your `AppDelegate.m` file, within your `application:didFinishLaunchingWithOptions:` method, add the following Braze method:

```objc
[Appboy startWithApiKey:@"YOUR-APP-IDENTIFIER-API-KEY"
          inApplication:application
      withLaunchOptions:launchOptions
      withAppboyOptions:appboyOptions];
```

Note that this method would replace the `startWithApiKey:inApplication:withLaunchOptions:` initialization method.

{% endtab %}
{% tab swift %}

In `AppDelegate.swift`, within your `application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool` method, add the following Braze method where `appboyOptions` is a `Dictionary` of startup configuration values:

```swift
Appboy.start(withApiKey: "YOUR-APP-IDENTIFIER-API-KEY",
                 in:application,
                 withLaunchOptions:launchOptions,
                 withAppboyOptions:appboyOptions)
```

Note that this method would replace the `startWithApiKey:inApplication:withLaunchOptions:` initialization method.

{% endtab %}
{% endtabs %}

This method is called with the following parameters:

- `YOUR-APP-IDENTIFIER-API-KEY` – Your [app identifier]({{site.baseurl}}/api/api_key/#the-app-identifier-api-key) API key from the Braze dashboard.
- `application` – The current app.
- `launchOptions` – The options `NSDictionary` that you get from `application:didFinishLaunchingWithOptions:`.
- `appboyOptions` – An optional `NSDictionary` with startup configuration values for Braze.

See [Appboy.h](https://github.com/braze-inc/braze-ios-sdk/blob/master/AppboyKit/include/Appboy.h) for a list of Braze startup keys.

## Appboy.sharedInstance() and Swift nullability
Differing somewhat from common practice, the `Appboy.sharedInstance()` singleton is optional. This is because `sharedInstance` is `nil` before `startWithApiKey:` is called, and there are some non-standard but not-invalid implementations in which a delayed initialization can be used.

If you call `startWithApiKey:` in your `didFinishLaunchingWithOptions:` delegate before any access to Appboy's `sharedInstance` (the standard implementation), you can use optional chaining, like `Appboy.sharedInstance()?.changeUser("testUser")`, to avoid cumbersome checks. This will have parity with an Objective-C implementation that assumed a non-null `sharedInstance`.

## Additional resources

Full [iOS class documentation](http://appboy.github.io/appboy-ios-sdk/docs/annotated.html) is available to provide additional guidance on any SDK methods.

