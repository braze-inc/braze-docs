---
nav_title: Delayed Initialization
article_title: Delayed initialization for the Braze Swift SDK
platform: Swift
page_order: 6
description: "This article covers how to implement the Swift SDK delayed initialization to preserve push notification handling when the SDK is initialized asynchronously."

---

# Delayed initialization

> Learn how to initialize your Braze Swift SDK asynchronously while ensuring push notification handling is preserved. This can be useful when you need to set up other services before initializing the SDK, such as fetching configuration data from a server, or waiting for user consent.

{% multi_lang_include developer_guide/prerequisites/swift.md %}

## Considerations

When you use `Braze.prepareForDelayedInitialization(pushAutomation:)`, you are configuring the SDK to automatically use push notification automation features. Any system delegate methods that handle push notifications will not be called for push notifications originating from Braze.

The SDK will only process a Braze push notification and the resulting action **after** the SDK is initialized. For example, if a user taps a push notification that opens a deep link, the deep link will only open after the `Braze` instance is initialized.

If you need to perform additional processing on Braze push notifications, see [Subscribing to push notifications updates]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#subscribing-to-push-notifications-updates). Keep in mind, to receive updates for push notifications that were previously enqueued, you must implement the subscription handler directly after initializing the SDK.

## Setting up delayed initialization

### Step 1: Prepare the SDK

By default, if an end-user opens your push notification while your app is in a terminated state, the push notification cannot be processed before the SDK is initialized.

Starting with [Braze Swift SDK version 10.1.0](https://github.com/braze-inc/braze-swift-sdk/releases/tag/10.1.0) and later, you can handle this using the static helper method: [Braze.prepareForDelayedInitialization(pushAutomation:)](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/preparefordelayedinitialization(pushautomation:)). This method will prepare the SDK for delayed initialization by setting up the push automation system.

Before the SDK is initialized, all push notifications originating from Braze will be captured and queued. After the SDK is initialized, those push notifications will be processed by the SDK. This method must be called as early as possible in your application lifecycle, either in or before the `application(_:didFinishLaunchingWithOptions:)` method of your `AppDelegate`.

{% alert note %}
The Swift SDK does not capture non-Braze push notifications&#8212;these will continue to be handled by the system delegate methods.
{% endalert %}

{% tabs %}
{% tab Swift %}
{% subtabs local %}
{% subtab UIKit %}
```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
  // Prepare the SDK for delayed initialization
  Braze.prepareForDelayedInitialization()

  // ... Additional non-Braze setup code

  return true
}
```
{% endsubtab %}

{% subtab SwiftUI %}
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
{% endsubtab %}
{% endsubtabs %}
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
[Braze.prepareForDelayedInitialization(pushAutomation:)](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/preparefordelayedinitialization(pushautomation:)) takes an optional `pushAutomation` parameter that represents the automation configuration for push notifications. When [Braze.Configuration.Push.Automation](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/push-swift.class/automation-swift.class) is `nil`, all automation features are enabled, other than requesting authorization at launch.
{% endalert %}

### Step 2: Initialize the SDK

After you've prepared the SDK for delayed initialization, you can initialize the SDK asynchronously at any time in the future. Then the SDK will process all queued push notifications events originating from Braze.

To initialize the Braze SDK, follow the [standard Swift SDK initialization process]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/sdk_integration/#step-2-update-your-app-delegate).
