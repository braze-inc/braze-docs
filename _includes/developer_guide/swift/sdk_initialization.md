{% multi_lang_include developer_guide/prerequisites/swift.md %}

## Using delayed initialization

You can initialize your Braze Swift SDK asynchronously while ensuring push notification handling is preserved. This can be useful when you need to set up other services before initializing the SDK, such as fetching configuration data from a server, or waiting for user consent.

### Considerations

When you use `Braze.prepareForDelayedInitialization(pushAutomation:)`, you are configuring the SDK to automatically use push notification automation features. Any system delegate methods that handle push notifications will not be called for push notifications originating from Braze.

The SDK will only process a Braze push notification and the resulting action **after** the SDK is initialized. For example, if a user taps a push notification that opens a deep link, the deep link will only open after the `Braze` instance is initialized.

If you need to perform additional processing on Braze push notifications, see [Subscribing to push notifications updates]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#subscribing-to-push-notifications-updates). Keep in mind, to receive updates for push notifications that were previously enqueued, you must implement the subscription handler directly after initializing the SDK.

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

## Using Google Tag Manager

The Braze Swift SDK can be initialized and controlled by tags configured within Google Tag Manager.

In the following example, a music streaming app wants to log different events as users listen to songs. Using Google Tag Manager for iOS, they can control which of the Braze third-party vendors receive this event and create tags specific to Braze.

### Step 1: Create a trigger for custom events

Custom events are logged with `actionType` set to `logEvent`. In this example, the Braze custom tag provider is expecting the custom event name to be set using `eventName`.

First, create a trigger that looks for an `eventName` that equals `played song`.

![A custom trigger in Google Tag Manager set to trigger for some events when "eventName" equals "played song".]({% image_buster /assets/img/android_google_tag_manager/gtm_android_trigger.png %})

Next, create a new Tag (also known as a "Function Call") and enter the class path of your [custom tag provider](#adding-ios-google-tag-provider) described later in this article. This tag will be triggered when you log the `played song` event. Because `eventName` is set to `played song` it will be used as custom event name that's logged to Braze.

{% alert important %}
When sending a custom event, set `actionType` to `logEvent`, and set a value for `eventName` so Braze receives the correct event name and action to take.
{% endalert %}

![A tag in Google Tag Manager with classpath and key-value pair fields. This tag is set to trigger with the previously created "played song" trigger.]({% image_buster /assets/img/android_google_tag_manager/gtm_android_function_call_tag.png %})

You can also include additional key-value pair arguments to the tag, which will be sent as custom event properties to Braze. `eventName` and `actionType` will not be ignored for custom event properties. In the following example tag, pass in `genre`, which was defined using a tag variable in Google Tag Manager and sourced from the custom event logged in the app.

The `genre` event property is sent to Google Tag Manager as a "Firebase - Event Parameter" variable since Google Tag Manager for iOS uses Firebase as the data layer.

![A variable in Google Tag Manager where "genre" is added as an event parameter for the "Braze - Played Song Event" tag.]({% image_buster /assets/img/android_google_tag_manager/gtm_android_eventname_variable.png %})

When a user plays a song in the app, log an event through Firebase and Google Tag Manager using the Firebase analytics event name that matches the tag's trigger name, `played song`:

{% tabs %}
{% tab SWIFT %}

```swift
let parameters: [String: Any] = ["genre": "pop",
                                 "number of times listened": 42]
Analytics.logEvent("played song", parameters: parameters)
```

{% endtab %}
{% tab OBJECTIVE-C %}

```obj-c
NSDictionary *parameters = @{@"genre" : @"pop",
                             @"number of times listened" : @42};
[FIRAnalytics logEventWithName:@"played song" parameters:parameters];
```

{% endtab %}
{% endtabs %}

### Step 2: Log custom attributes

Custom attributes are set via an `actionType` set to `customAttribute`. The Braze custom tag provider is expecting the custom attribute key-value to be set via `customAttributeKey` and `customAttributeValue`:

{% tabs %}
{% tab SWIFT %}
```swift
let parameters: [String: Any] = ["customAttributeKey": "favoriteSong",
                                 "customAttributeValue": "Private Eyes"]
FIRAnalytics.logEvent(withName:"customAttribute", parameters: parameters)
```
{% endtab %}
{% tab OBJECTIVE-C %}

```obj-c
NSDictionary *parameters = @{@"customAttributeKey" : @"favoriteSong",
                             @"customAttributeValue" : @"Private Eyes"};
[FIRAnalytics logEventWithName:@"customAttribute" parameters:parameters];
```

{% endtab %}

{% endtabs %}

### Step 3: Call `changeUser()`

Calls to `changeUser()` are made via an `actionType` set to `changeUser`. The Braze custom tag provider is expecting the Braze user ID to be set via an `externalUserId` key-value pair within your tag:

{% tabs %}
{% tab SWIFT %}
```swift
let parameters: [String: Any] = ["externalUserId": "favorite userId"]
Analytics.logEvent(withName:"changeUser", parameters: parameters)
```
{% endtab %}
{% tab OBJECTIVE-C %}

```obj-c
NSDictionary *parameters = @{@"externalUserId" : userId};
[FIRAnalytics logEventWithName:@"changeUser" parameters:parameters];
```

{% endtab %}

{% endtabs %}

### Step 4: Add a custom tag provider {#adding-ios-google-tag-provider}

With the tags and triggers set up, you will also need to implement Google Tag Manager in your iOS app which can be found in Google's [documentation](https://developers.google.com/tag-manager/ios/v5/).

After Google Tag Manager is installed in your app, add a custom tag provider to call Braze SDK methods based on the tags you've configured within Google Tag Manager.

Be sure to note the "Class Path" to the file - this is what you'll enter when setting up a tag in the [Google Tag Manager](https://tagmanager.google.com/) console.

This example highlights one of many ways you can structure your custom tag provider. Specifically, it shows how to determine which Braze SDK method to call based on the `actionType` key-value pair sent from the GTM Tag. This example assumes you've assigned the Braze instance as a variable in the AppDelegate.

The `actionType` supported in this example are `logEvent`, `customAttribute`, and `changeUser`, but you may prefer to change how your tag provider handles data from Google Tag Manager.
{% tabs %}
{% tab SWIFT %}

Add the following code to your `BrazeGTMTagManager.swift` file.
```swift
import FirebaseAnalytics
import GoogleTagManager
import BrazeKit

let ActionTypeKey: String = "actionType"

// Custom Events
let LogEventAction: String = "logEvent"
let LogEventName: String = "eventName"

// Custom Attributes
let CustomAttributeAction: String = "customAttribute"
let CustomAttributeKey: String = "customAttributeKey"
let CustomAttributeValueKey: String = "customAttributeValue"

// Change User
let ChangeUserAction: String = "changeUser"
let ChangeUserExternalUserId: String = "externalUserId"

@objc(BrazeGTMTagManager)
final class BrazeGTMTagManager : NSObject, TAGCustomFunction {
  @objc func execute(withParameters parameters: [AnyHashable : Any]!) -> NSObject! {
    var parameters: [String : Any] = parameters as! [String : Any]
    guard let actionType: String = parameters[ActionTypeKey] as? String else {
      print("There is no Braze action type key in this call. Doing nothing.")
      return nil
    }
    parameters.removeValue(forKey: ActionTypeKey)
    if actionType == LogEventAction {
      logEvent(parameters: parameters)
    } else if actionType == CustomAttributeAction {
      logCustomAttribute(parameters: parameters)
    } else if actionType == ChangeUserAction {
      changeUser(parameters: parameters)
    }
    return nil
  }
  
  func logEvent(parameters: [String : Any]) {
    var parameters: [String : Any] = parameters
    guard let eventName: String = parameters[LogEventName] as? String else { return }
    parameters.removeValue(forKey: LogEventName)
    AppDelegate.braze?.logCustomEvent(name: eventName, properties: parameters)
  }
  
  func logCustomAttribute(parameters: [String: Any]) {
    guard let customAttributeKey = parameters[CustomAttributeKey] as? String else { return }
    let customAttributeValue = parameters[CustomAttributeValueKey]
    
    if let customAttributeValue = customAttributeValue as? String {
      AppDelegate.braze?.user.setCustomAttribute(key: customAttributeKey, value: customAttributeValue)
    } else if let customAttributeValue = customAttributeValue as? Date {
      AppDelegate.braze?.user.setCustomAttribute(key: customAttributeKey, value: customAttributeValue)
    } else if let customAttributeValue = customAttributeValue as? Double {
      AppDelegate.braze?.user.setCustomAttribute(key: customAttributeKey, value: customAttributeValue)
    } else if let customAttributeValue = customAttributeValue as? Bool {
      AppDelegate.braze?.user.setCustomAttribute(key: customAttributeKey, value: customAttributeValue)
    } else if let customAttributeValue = customAttributeValue as? Int {
      AppDelegate.braze?.user.setCustomAttribute(key: customAttributeKey, value: customAttributeValue)
    } else if let customAttibuteValue = customAttributeValue as? [String] {
      AppDelegate.braze?.user.setCustomAttributeArray(key: customAttributeKey, array: customAttibuteValue)
    }
  }
  
  func changeUser(parameters: [String: Any]) {
    guard let userId = parameters[ChangeUserExternalUserId] as? String else { return }
    AppDelegate.braze?.changeUser(userId: userId)
  }
}
```
{% endtab %}
{% tab OBJECTIVE-C %}
Add the following code to your `BrazeGTMTagManager.h` file:

```obj-c
@import Firebase;
@import GoogleTagManager;

@interface BrazeGTMTagManager : NSObject <TAGCustomFunction>

@end
```

And add the following code to your `BrazeGTMTagManager.m` file:

```obj-c
#import <Foundation/Foundation.h>
#import "BrazeGTMTagManager.h"
#import "BrazeKit"
#import "AppDelegate.h"

static NSString *const ActionTypeKey = @"actionType";

// Custom Events
static NSString *const LogEventAction = @"logEvent";
static NSString *const LogEventEventName = @"eventName";

// Custom Attributes
static NSString *const CustomAttributeAction = @"customAttribute";
static NSString *const CustomAttributeKey = @"customAttributeKey";
static NSString *const CustomAttributeValueKey = @"customAttributeValue";

// Change User
static NSString *const ChangeUserAction = @"changeUser";
static NSString *const ChangeUserExternalUserId = @"externalUserId";

@implementation BrazeGTMTagManager

- (NSObject *)executeWithParameters:(NSDictionary *)parameters {
  NSMutableDictionary *mutableParameters = [parameters mutableCopy];
  
  NSString *actionType = mutableParameters[ActionTypeKey];
  if (!actionType) {
    NSLog(@"There is no Braze action type key in this call. Doing nothing.", nil);
    return nil;
  }
  
  [mutableParameters removeObjectForKey:ActionTypeKey];
  
  if ([actionType isEqualToString:LogEventAction]) {
    [self logEvent:mutableParameters];
  } else if ([actionType isEqualToString:CustomAttributeAction]) {
    [self logCustomAttribute:mutableParameters];
  } else if ([actionType isEqualToString:ChangeUserAction]) {
    [self changeUser:mutableParameters];
  } else {
    NSLog(@"Invalid action type. Doing nothing.");
  }
  return nil;
}

- (void)logEvent:(NSMutableDictionary *)parameters {
  NSString *eventName = parameters[LogEventEventName];
  [parameters removeObjectForKey:LogEventEventName];
  [AppDelegate.braze logCustomEvent:eventName
                         properties:parameters];
}

- (void)logCustomAttribute:(NSMutableDictionary *)parameters {
  NSString *customAttributeKey = parameters[CustomAttributeKey];
  id customAttributeValue = parameters[CustomAttributeValueKey];
  
  if ([customAttributeValue isKindOfClass:[NSString class]]) {
    [AppDelegate.braze logCustomEvent:customAttributeKey
                           properties:parameters];
  } else if ([customAttributeValue isKindOfClass:[NSDate class]]) {
    [AppDelegate.braze.user setCustomAttributeWithKey:customAttributeKey
                                            dateValue:customAttributeValue];
  } else if ([customAttributeValue isKindOfClass:[NSNumber class]]) {
    if (strcmp([customAttributeValue objCType], [@(YES) objCType]) == 0) {
      [AppDelegate.braze.user setCustomAttributeWithKey:customAttributeKey
                                              boolValue:[(NSNumber *)customAttributeValue boolValue]];
    } else if (strcmp([customAttributeValue objCType], @encode(short)) == 0 ||
               strcmp([customAttributeValue objCType], @encode(int)) == 0 ||
               strcmp([customAttributeValue objCType], @encode(long)) == 0) {
      [AppDelegate.braze.user setCustomAttributeWithKey:customAttributeKey
                                               intValue:[(NSNumber *)customAttributeValue integerValue]];
    } else if (strcmp([customAttributeValue objCType], @encode(float)) == 0 ||
               strcmp([customAttributeValue objCType], @encode(double)) == 0) {
      [AppDelegate.braze.user setCustomAttributeWithKey:customAttributeKey
                                            doubleValue:[(NSNumber *)customAttributeValue doubleValue]];
    } else {
      NSLog(@"Could not map NSNumber value to Braze custom attribute:%@", customAttributeValue);
    }
  } else if ([customAttributeValue isKindOfClass:[NSArray class]]) {
    [AppDelegate.braze.user setCustomAttributeArrayWithKey:customAttributeKey
                                                     array:customAttributeValue];
  }
}

- (void)changeUser:(NSMutableDictionary *)parameters {
  NSString *userId = parameters[ChangeUserExternalUserId];
  [AppDelegate.braze changeUser:userId];
}

@end
```
{% endtab %}
{% endtabs %}
