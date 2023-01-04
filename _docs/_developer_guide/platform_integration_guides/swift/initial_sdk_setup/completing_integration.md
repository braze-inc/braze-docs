---
nav_title: Completing the Integration
article_title: Completing the iOS SDK Integration
platform: Swift
description: "This reference article shows how to finish integrating the Braze SDK after installing it via one of the integration options."
page_order: 2

---

# Completing the integration

Before following these steps, make sure you have integrated the SDK using either [CocoaPods]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/installation_methods/cocoapods/) or [Swift Package Manager]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/installation_methods/swift_package_manager/).

## Update your app delegate

{% tabs %}
{% tab OBJECTIVE-C %}

Add the following line of code to your `AppDelegate.m` file:

```objc
@import BrazeKit;
```

Next, add a static variable to your `AppDelegate.m` file to keep a reference to the Braze instance throughout your application's lifetime:

```objc
static Braze *_braze;

@implementation AppDelegate
+ (Braze *)braze {
  return _braze;
}

+ (void)setBraze:(Braze *)braze {
  _braze = braze;
}
@end
```

Finally, within your `AppDelegate.m` file, add the following snippet within your `application:didFinishLaunchingWithOptions:` method:

```objc
BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:"YOUR-APP-IDENTIFIER-API-KEY"
                                                                  endpoint:"YOUR-BRAZE-ENDPOINT"];
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
AppDelegate.braze = braze;
```

Update `YOUR-APP-IDENTIFIER-API-KEY` and `YOUR-BRAZE-ENDPOINT` with the correct value from your **Manage Settings** page. Check out our [API documentation]({{site.baseurl}}/api/api_key/#the-app-identifier-api-key) for more information on where to find your app identifier API key.

{% endtab %}
{% tab swift %}

Add the following line of code to your `AppDelegate.swift` file to import the features included in the Braze Swift SDK:

```swift
import BrazeKit
```

Refer to the [Apple developer docs](https://developer.apple.com/library/ios/documentation/swift/conceptual/buildingcocoaapps/MixandMatch.html) for more information on using Objective-C code in Swift projects.

Next, add a static property to your `AppDelegate` class to keep a strong reference to the Braze instance throughout your application's lifetime:

```swift
class AppDelegate: UIResponder, UIApplicationDelegate {
  static var braze: Braze? = nil
}
```

Finally, in `AppDelegate.swift`, add the following snippet to your `application:didFinishLaunchingWithOptions:` method:

```swift
let configuration = Braze.Configuration(
    apiKey: "YOUR-APP-IDENTIFIER-API-KEY",
    endpoint: "YOUR-BRAZE-ENDPOINT"
)
let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```

Update `YOUR-APP-IDENTIFIER-API-KEY` and `YOUR-BRAZE-ENDPOINT` with the correct value from your **Manage Settings** page. Check out our [API documentation]({{site.baseurl}}/api/api_key/#the-app-identifier-api-key) for more information on where to find your app identifier API key.

{% endtab %}
{% endtabs %}

{% alert warning %}
Be sure to initialize Braze in your application's main thread. Initializing asynchronously can lead to broken functionality.
{% endalert %}

## SDK integration complete

Braze should now be collecting data from your application, and your basic integration should be complete. See the following articles to enable [custom event tracking]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/tracking_custom_events/), [push messaging]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/), and the complete suite of Braze features.

## Additional resources

Full [iOS class documentation][1] is available to provide additional guidance on any SDK methods.

[1]: https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/ "full iOS class documentation"
