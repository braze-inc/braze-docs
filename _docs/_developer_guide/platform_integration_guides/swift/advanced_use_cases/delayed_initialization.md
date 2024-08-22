---
nav_title: Delayed Initialization
article_title: Delayed initialization for the Braze Swift SDK
platform: Swift
page_order: 6
description: "This article covers how to implement the Swift SDK delayed initialization to preserve push notification handling when the SDK is initialized asynchronously."

---

# Delayed initialization for the Braze Swift SDK

> Learn how to initialize your Braze Swift SDK asynchronously while ensuring push notification handling is preserved. This can be useful when you need to set up other services before initializing the SDK, such as fetching configuration data from a server, or waiting for user consent.

## Setting up delayed initialization

### Step 1: Preparing the SDK for delayed initialization

By default, push notifications received and clicked while your application is in the terminated state cannot be processed before the SDK is initialized. Since the version [10.1.0](https://github.com/braze-inc/braze-swift-sdk/releases/tag/10.1.0) of the Braze Swift SDK, we offer a new static helper method to handle this scenario: [Braze.prepareForDelayedInitialization(pushAutomation:)](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/preparefordelayedinitialization(pushautomation:)).

This method prepares the SDK for delayed initialization by setting up the push automation system. All push notifications originating from Braze will be captured, queued, and processed by the SDK once it is initialized. This method must be called as early as possible in your application lifecycle, in or before the `application(_:didFinishLaunchingWithOptions:)` method of your `AppDelegate`.

{% alert note %}
Non-Braze push notifications will not be captured by the SDK and will be handled by the system delegate methods as usual.
{% endalert %}

{% tabs %}
{% tab Swift (UIKit) %}
```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
  // Prepare the SDK for delayed initialization
  Braze.prepareForDelayedInitialization()

  // ... Additional non-Braze setup code

  return true
}
```
{% endtab %}

{% tab Swift (SwiftUI) %}
SwiftUI applications require implementing the [@UIApplicationDelegateAdaptor](https://developer.apple.com/documentation/swiftui/uiapplicationdelegateadaptor) property wrapper to call the `prepareForDelayedInitialization()` method.

```swift
@main
struct MyApp: App {
  @UIApplicationDelegateAdaptor var appDelegate: AppDelegate

  var body: some Scene {
    WindowGroup {
      ContentView()
    }
  }
}

class AppDelegate: NSObject, UIApplicationDelegate {
  
  func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]? = nil) -> Bool {
    // Prepare the SDK for delayed initialization
    Braze.prepareForDelayedInitialization()

    // ... Additional non-Braze setup code

    return true
  }
  
}
```
{% endtab %}

{% tab Objective-C %}
```objc
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  // Prepare the SDK for delayed initialization
  [Braze prepareForDelayedInitialization];
  
  // ... Additional non-Braze setup code

  return YES;
}

```
{% endtab %}
{% endtabs %}

{% alert note %}
[Braze.prepareForDelayedInitialization(pushAutomation:)](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/preparefordelayedinitialization(pushautomation:)) takes an optional `pushAutomation` parameter that represents the automation configuration for push notifications. See [Braze.Configuration.Push.Automation](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/push-swift.class/automation-swift.class) for more information. When this parameter is `nil`, all automation features are enabled except requesting authorization at launch.
{% endalert %}

### Step 2: Initializing the Braze SDK

Once the SDK is prepared for delayed initialization, you can initialize the SDK asynchronously at a later time. The SDK will process all queued push notifications events once it is initialized.

To do so, simply follow the standard initialization process described in the [Completing the integration]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/completing_integration/) documentation page.

## Considerations

By using `Braze.prepareForDelayedInitialization(pushAutomation:)`, the SDK will automatically be configured to use the push notification automation features. Any system delegate methods that handle push notifications will not be called for push notifications originating from Braze.

Actions resulting from the user clicking on Braze push notifications will only be processed by the SDK once it is initialized. For instance, if the user clicks on a push notification that opens a deep link, the deep link will be opened only after the `Braze` instance is initialized.

If you need to perform additional processing on Braze push notifications, please refer to the [Subscribing to push notifications updates]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#subscribing-to-push-notifications-updates). You must implement the subscription handler right after initializing the SDK to receive updates for push notifications that were previously enqueued.
