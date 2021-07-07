---
nav_title: iOS SDK Integration
permalink: "/ios_sdk/"
hidden: true
---

# Braze iOS SDK Integration Guide

> This iOS integration guide takes you on a step-by-step journey on setup best practices when first integrating the iOS SDK and its core components into your application. This guide will help you build a `BrazeManager.swift` helper file that will decouple any dependencies on the Braze iOS SDK from the rest of your production code, resulting in one `import AppboyUI` in your entire application. This approach limits issues that arise from excessive SDK imports, making it easier to track, debug, and alter code.

## Integration Overview

The following steps help you build a `BrazeManager` helper file that your production code calls into. This helper file will deal with all Braze-related dependencies by adding various extensions for the following integration topics listed below. Each topic will include horizontal tab steps and code snippets in both Swift and Objective-C. Please note that the Content Card and in-app message steps are not required for integration if you do not plan to utilize these channels in your application.

- [Create BrazeManager.swift](#create-brazemanagerswift)
- [Initialize SDK]()
- [Push Notifications](#push-notifications)
- [Access User Variables and Methods](#access-user-variables-and-methods)
- [Log Analytics](#log-analytics)
- [In-App Messages (Optional)](#in-app-messages)
- [Content Cards (Optional)](#content-cards)
- [Next Steps](#next-steps)

### Create BrazeManager.Swift

{% tabs local %}
{% tab Step 1: Create BrazeManager.swift %}

##### Create BrazeManager.swift
To build out your `BrazeManager.swift` file, create a new Swift file named _BrazeManager_ to add to your project at your desired location. Next, Replace `import Foundation` with `import AppboyUI` and then create a `BrazeManager` class that will be used to host all Braze-related methods and variables. 

{% alert note %}
- `BrazeManager` is an `NSObject` class and not a struct, so it can conform to ABK delegates such as the `ABKInAppMessageUIDelegate`.
- The `Brazemanager` is a singleton class by design to ensure that only one instance of this class will be used. This is done to provide a unified point of access to the object.
{% endalert %} 

1. Add a static variable named _shared_ that initializes the `BrazeManager` class. This is guaranteed to be lazily initiated only once.
2. Next, add a private constant variable named _apiKey_ and set it as the API key value from your app group in the Braze dashboard.
3. Add a private computed variable named _appboyOptions_, which will store configuration values for the SDK. It will be empty for now.

{% subtabs global %}
{% subtab Swift %}

```swift
class BrazeManager: NSObject {
  // 1
  static let shared = BrazeManager()
  
  // 2
  private let apikey = "YOUR-API-KEY"
  
  // 3
  private var appboyOptions[String:Any]{
    return [:]
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Initalize the SDK

{% tabs %}
{% tab Step 1: Initialize SDK from BrazeManager.swift %}

##### Initialize SDK from BrazeManager.swift
Next, you must initialize the SDK. This guide assumes you have already [integrated the SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/overview/) into your Xcode project. 

Add the `didFinishLaunching...` method from the `AppDelegate.swift` file sans return value in your `BrazeManager.swift` file. By creating a similar method in the `BrazeManager.swift` file, there will not be an `import AppboyUI` statement in your `AppDelegate.swift` file. 

Next, initialize the SDK using your newly declared `apiKey` and `appboyOptions` variables.

{% alert important %}
Initialization should be done in the main thread.
{% endalert %}

{% subtabs global %}
{% subtab Swift %}
```swift
func application(_ application: UIapplication, didFinishLaunchingWithOptions launchOptions:[UIApplication.LaunchOptionsKey:Any]?){
  Appboy.start(withAPIKey: apikey, in: applciation, withLaunchOptions: launchOptions, withAppboyOptions: appboyOptions)
}
```
{% endsubtab %}
{% subtab Objective-C %}

{% endsubtab %}
{% endsubtabs %}

{% endtab %}
{% tab Step 2: Handle Appboy Initalization %}

##### Handle Appboy Initialization in the AppDelegate.swift
Next, navigate back to the `AppDelegate.swift` file and add the following code snippet in the AppDelegate's `didFinishLaunching...` method to handle the Appboy initialization from the `BrazeManager.swift` helper file. Remember, there is no need to add an `import AppboyUI` statement in the `AppDelegate.swift`.

{% subtabs global %}
{% subtab Swift %}

```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions:
[UIApplication.LaunchOptionsKey: Any]?) -> Bool {
  // Override point for customization after application launch

  BrazeManager.shared.application(application, didFinishLaunchingWithOptions: launchOptions)

  return true
}
```
{% endsubtab %}
{% subtab Objective-C %}

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert checkpoint %}
Proceed to compile your code and run your application.<br><br>At this point, the SDK should be up and running. In your dashboard, observe that sessions are being logged before advancing any further.
{% endalert %}

### Push Notifications

{% tabs local %}
{% tab Step 1: Add Push Certificate %}

##### Add Push Certificate

Navigate to your existing app group in the Braze dashboard. Under __Push Notification Settings__ upload your push certificate file to your Braze dashboard and save it. <br><br>![Push Certificate]({% image_buster /assets/img/ios_sdk/ios_sdk2.png %}){: style="max-width:60%;"}

{% endtab %}
{% tab Step 2: Register for Notifications %}

##### Register for Push Notifications

Next, register for push notifications. This guide assumes you have [set up your push credentials correctly]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/) in your Apple developer portal and Xcode project. 

The code for registering push notifications will be added in the `didFinishLaunching...` method in the `BrazeManager.swift` file. Your initialization code should end up looking like the following:

1. Configure the contents for requesting authorization to interact with the user. These options are listed as an example.
2. Request authorization to send your users push notifications. The user's response to allow or deny push notifications is tracked in the form of the `granted` variable.
3. Forward the push authorization results to Braze after the user interacts with the notification prompt.
4. Initiate the registration process with APNs; this should be done in the main thread. If the registration succeeds, the app calls your `AppDelegate` object's `didRegisterForRemoteNotificationsWithDeviceToken` method. 

{% subtabs global %}
{% subtab Swift %}
```swift
func application(_ application: UIapplication, didFinishLaunchingWithOptions launchOptions:[UIApplication.LaunchOptionsKey:Any]?){
  Appboy.start(withAPIKey: apikey, in: applciation, withLaunchOptions: launchOptions, withAppboyOptions: appboyOptions)
  // 1 
  let options: UNAuthorizationOptions = [.alert, . sound, .bagde]

  // 2 
  UNUserNotificationCenter.current().requestAuthorization(option: options){ (granted, error) in
  // 3 
    Appboy.sharedInstance()?.pushAuthorization(fromUserNotificationCenter: granted)
  }
  
  // 4 
  UIApplications.shared.registerForRemoteNotificiations()
}
```
{% endsubtab %}
{% subtab Objective-C %}

{% endsubtab %}
{% endsubtabs %}

{% alert checkpoint %}
Proceed to compile your code and run your application.
- In your app, confirm that you are being prompted for push notifications before advancing any further.
- If you are not prompted, try deleting and re-installing the app to ensure the push notification prompt was not displayed previously.

Observe you are being prompted for push notifications before advancing any further.
{% endalert %}

{% endtab %}
{% tab Step 3: Forward Methods %}

##### Forward Push Notification Methods

Next, forward the system push notifications methods from `AppDelegate.swift` to `BrazeManager.swift` to be handled by the Braze iOS SDK.

###### Step 1: Create Extension for Push Notificiation Code

Create an extension for your push notification code in your `BrazeManager.swift` file so it reads in a more organized manner as to what purpose is being served in the helper file, like so:

1. Following the pattern of not including an `import AppboyUI` statement in your `AppDelegate`, we will handle the push notifications methods in the `BrazeManager.swift` file. User's device tokens will need to be passed to Braze from the `didRegisterForRemote...` method. Next, add the same method from the `AppDelegate` in your `BrazeManager` class.
2. Add the following line inside the method to register the device token to Braze. This is necessary for Braze to associate the token with the current device. 

{% subtabs global %}
{% subtab Swift %}

```swift
// MARK - Push Notifications
extension BrazeManager {
  // 1 
  func application(_ application: UIApplication,
didRegisterForRemoteNotificationsWithDeviceToken deviceToken: Data) {

  // 2 
  Appboy.sharedInstance().?registerDeviceToken(deviceToken)
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}

{% endsubtab %}
{% endsubtabs %}

###### Step 2: Support Remote Notifications
In the __Signing & Capabilities__ tab, add __Background Modes__ support and select __Remote notificiations__ to begin your support of remote notifications originating from Braze.<br><br>![Signing & Capabilities]({% image_buster /assets/img/ios_sdk/ios_sdk3.png %})

###### Step 3: Remote Notification Handling
The Braze SDK can handle remote notifications that originate from Braze. Forward remote notifications to Braze; the SDK will automatically ignore push notifications that do not originate from Braze. Add the following method to your `BrazeManager.swift` file in the push notification extension.

{% subtabs global %}
{% subtab Swift %}
```swift
func application(_ application: UIApplication, didReceiveRemoteNotification userInfo: [AnyHashable : Any], fetchCompletionHandler completionHandler: @escaping (UIBackgroundFetchResult) -> Void) {
  Appboy.sharedInstance()?.register(application, didReceiveRemoteNotification: userInfo, fetchCompletiionHandler: completionHandler)
}
```
{% endsubtab %}
{% subtab Objective-C %}

{% endsubtab %}
{% endsubtabs %}

###### Step 4: Forward Notification Responses

The Braze SDK can handle the response of push notifications that originate from Braze. Forward the response of the notifications to Braze; the SDK will automatically ignore responses from push notifications that do not originate from Braze. Add the following method to your `BrazeManager.swift` file:

{% subtabs global %}
{% subtab Swift %}

```swift
func userNotificationCenter(_ center: UNUserNotificationCenter, didReceive response: UNNotificationResponse, withCompletionHandler completionHandler: @escaping () -> Void) {
  Appboy.sharedInstance()?.userNotificationCenter(center, didReceive: response, withCompletionHandler: completionHandler)
}
```
{% endsubtab %}
{% subtab Objective-C %}

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert checkpoint %}
Proceed to Compile your code and run your application. <br><br>Try sending yourself a push notification from the Braze dashboard and observe that analytics are being logged from push notifications before advancing any further. 
{% endalert %}

### Access User Variables and Methods

{% tabs %}
{% tab Step 1: Create Extension %}

##### Create Extension

Next, you will want easy access to the `ABKUser` variables and methods. Creating an extension for your user code in your `Brazemanager.swift` file so it reads in a more organized manner as to what purpose is being served in the helper file, like so:

1. An `ABKUser` object represents a known or anonymous user in your iOS application. Add a computed variable to retrieve the `ABKUser`; this variable will be reused to retrieve variables about the user.
2. Query the user variable to easily access the `userId`. Among the other variables, the `ABKUser` object is responsible for (`firstName`, `lastName`, `phone`, `homeCity`, etc.)
3. Set the user by calling `changeUser()` with a corresponding `userId`.

{% subtabs global %}
{% subtab Swift %}

```swift
// Mark: User
extension BrazeManager {
  // 1
  var user: ABKUser?{
    return Appboy.sharedInstance()?.user
  }

  // 2 
  var userId: String?{
    return user?.userID
  }

  // 3
  func changeUser(_userId: String){
    Appboy.sharedInstance()?.changeUser(userId)
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert checkpoint %}
Proceed to compile your code and run your application.<br><br>Try identifying users from a successful sign-in/sign-up. Be sure you have a solid understanding of what is and what is not an appropriate user identifier. <br><br>In your dashboard, observe that the user identifier is logged before advancing any further.
{% endalert %} 

### Log Analytics

{% tabs local %}
{% tab Step 1: Create Extension %}

##### Create Extension for Analytics Code

Next, you must enable your production code to log crucial analytics metrics to Braze without the need for excessive `import AppboyUI` statements. The production code should call into the `BrazeManager` to log all analytics. 

Create an extension for your analytics code in your `Brazemanager.swift` file so it reads in a more organized manner as to what purpose is being served in the helper file, like so:

{% subtabs global %}
{% subtab Swift %}
```swift
//MARK: -Analytics
extension BrazeManager {

}
```
{% endsubtab %}
{% subtab Objective-C %}

{% endsubtab %}
{% endsubtabs %}

{% endtab %}
{% tab Step 2: Custom Events %}

##### Create Log Custom Event Method

Based on the following Braze SDK `logCustomEvent` method, create a matching method. 

__Braze `logCustomEvent` Reference Method__<br>
This is by design because only the `BrazeManager.swift` file can directly access the Braze iOS SDK methods. Therefore, by creating a matching method, the result is the same and is done without the need for any direct dependencies on the Braze iOS SDK in your production code.

```
open func logCustomEvent(_ eventName: String, withProperties properties: [AnyHashable : Any]?)
```

__Matching Method__<br>
Log custom events from the `Appboy` object to Braze. `Properties` is an optional parameter with a default value of nil. Custom events are not required to have properties but are required to have a name. 

{% subtabs global %}
{% subtab Swift %}
```swift
func logCustomEvent(_ eventName: String, withProperties properties: [AnyHashable: Any]? = nil){
  Appboy.sharedInstance()?.logCustomEvent(eventName, withProperties: properties)
}
```
{% endsubtab %}
{% subtab Objective-C %}

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Step 3: Custom Attributes %}

##### Create Log Custom Attributes Method 

The SDK can log numerous types as custom attributes. There is no need to create helper methods for each value type that can be set. Instead, only expose one method that can filter down to the appropriate value.

```
- (BOOL)setCustomAttributeWithKey:(NSString *)key andBOOLValue:(BOOL)value; 
- (BOOL)setCustomAttributeWithKey:(NSString *)key andIntegerValue:(NSIntenger)value; 
- (BOOL)setCustomAttributeWithKey:(NSString *)key andDoubleValue:(double)value; 
- (BOOL)setCustomAttributeWithKey:(NSString *)key andStringValue:(NSString *)value; 
- (BOOL)setCustomAttributeWithKey:(NSString *)key andDateValue:(NSDate *)value;
```

Custom attributes are logged from the `ABKUser` object. 

Create __one method__ that can encompass all of the available types that can be set for an attribute. Add this method in your `BrazeManager.swift` file in the analytics extension. This can be done by filtering through the valid custom attribute types and call the method associated with the matching type.

- The parameter `value` is a generic type that conforms to the `Equatable` protocol. This is explicitly done, so if the type is not what the Braze iOS SDK expects, there will be a compile-time error.
- The parameters `key` and `value` are optional parameters that will be conditionally unwrapped in the method. This is just one way to ensure non-nil values are being passed to the Braze iOS SDK.

{% subtabs global %}
{% subtab Swift %}

```swift
func setCustomAttributeWithKey<T: Equatable>(_ key: String?, andValue value: T?) {
  guard let key = key, let value = value else { return }
  switch value.self {
  case let value as Date:
    user?.setCustomAttributeWithKey(key, andDateValue: value)
  case let value as Bool:
    user?.setCustomAttributeWithKey(key, andBOOLValue: value)
  case let value as String:
    user?.setCustomAttributeWithKey(key, andStringValue: value)
  case let value as Double:
    user?.setCustomAttributeWithKey(key, andDoubleValue: value)
  case let value as Int:
    user?.setCustomAttributeWithKey(key, andIntegerValue: value)
  default:
   return
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Step 4: Purchases %}

##### Create Log Purchase Method

Next, based on the following Braze SDK `logPurchase` method, create a matching method. 

__Braze `logPurchase` Reference Method__<br>
This is by design because only the `BrazeManager.swift` file can directly access the Braze iOS SDK methods. Therefore, by creating a matching method, the result is the same and is done without the need for any direct dependencies on the Braze iOS SDK in your production code. 

```
open func logPurchase(_ productIdentifier: String, inCurrency currency: String, atPrice price: NSDecimalNumber, withoutQuantity quantity: UInt)
```
__Matching Method__<br>
Log purchases from the `Appboy` object to Braze. The SDK has multiple methods for logging purchases, and this is just one example. This method also handles creating the `NSDecimal` and `UInt` objects. How you want to handle that part is up to you, provided is just one example.

{% subtabs global %}
{% subtab Swift %}

```swift
func logPurchase(_ productIdentifier: String, inCurrency currency: String, atPrice price:
String, withQuantity quantity: Int) {

  Appboy.sharedInstance()?.logPurchase(productIdentifier, inCurrency: currency, atPrice: NSDecimalNumber(string: price), withQuantity: UInt(quantity))

}
```
{% endsubtab %}
{% subtab Objective-C %}

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert checkpoint %}
Proceed to compile your code and run your application. <br><br>Try logging custom events.<br><br>In your dashboard, observe that the custom events are logged before advancing any further. 
{% endalert %}

### In-App Messages

{% tabs local %}
{% tab Step 1: Conform to Delegate %}

{% alert important %}
The following in-app message section is not required for integration if you do not plan to utilize this channel in your application.
{% endalert %}

##### Conform to ABKInAppMessageUIDelegate

Next, enable your `BrazeManager.swift` file code to conform to the `ABKInAppMessageUIDelegate` to directly handle the associated methods. 

The code for conforming to the delegate will be added in the `didFinishLaunching...` methods in the `BrazeManager.swift` file. Your initialization code should end up looking like this:

{% subtabs global %}
{% subtab swift %}
```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) {
  Appboy.start(withApiKey: apiKey, in: application, withLaunchOptions: launchOptions, withAppboyOptions: appboyOptions)

  let options: UNAuthorizationOptions = [.alert, .sound, .badge]
  UNUserNotificationCenter.current().requestAuthorization(options: options) { (granted, error) in
    Appboy.sharedInstance()?.pushAuthorization(fromUserNotificationCenter: granted)
  }
  UIApplication.shared.registerForRemoteNotifications()

  Appboy.sharedInstance()?.inAppMessageController.inAppMessageUIController?.setInAppMessageUIDelegate?(self)
}
```
{% endsubtab %}
{% subtab Objective-C %}

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Step 2: Create Extension %}

##### Create Extension that Conforms to ABKInAppMessageUIDelegate
Next, create an extension that conforms to the `ABKInAppMessageUIDelegate`.

Add this snippet below the analytics section. Note that the `BrazeManager.swift` object is set as the delegate; this will be where the `BrazeManager.swift` file handles all the `ABKInAppMessageUIDelegate` methods. 

{% alert important %}
The `ABKInAppMessageUIDelegate` does not come with any required methods, but listed below is an example of one.
{% endalert %}

{% subtabs global %}
{% subtab Swift %}
```swift
// Mark: - ABKInAppMessage UI Delegate
extension AppboyManager: ABKInAppMessageUIDelegate{
  func inAppMessageViewControllerWith(_ inAppMessage: ABKInAppMessage) -> ABKInAppMessageViewController {
    switch inAppMessage {
    case is ABKInAppMessageSlideup:
      return ABKInAppMessageSlideupViewController(inAppMessage: inAppMessage)
    case is ABKInAppMessageModal:
      return ABKInAppMessageModalViewController(inAppMessage: inAppMessage)
    case is ABKInAppMessageFull:
      return ABKInAppMessageFullViewController(inAppMessage: inAppMessage)
    case is ABKInAppMessageHTML:
      return ABKInAppMessageHTMLViewController(inAppMessage: inAppMessage)
    default:
      return ABKInAppMessageViewController(inAppMessage: inAppMessage)
}
```
{% endsubtab %}
{% subtab Objective-C %}

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert checkpoint %}
Proceed to compile your code and run your application. <br><br>Try sending yourself an in-app message. <br><br>In the `Brazemanager.swift` file, set a breakpoint at the entry of the example _ABKInAppMessageUIDelegate_ method. Send yourself an in-app message and confirm the breakpoint is hit before advancing any further. 
{% endalert %}

### Content Cards

{% tabs %}
{% tab Step 1: Create Extension %}

{% alert important %}
The following Content Card section is not required for integration if you do not plan to utilize this channel in your application.
{% endalert %}

##### Create Extension

Enable your production code to display the Content Cards view controller without the need for unnecessary `import AppboyUI` statements. 

Create an extension for your Content Cards code in your `BrazeManager.swift` file, so it reads in a more organized manner as to what purpose is being served in the helper file, like so:

1. Display the `ABKContentCardsTableViewController`. An optional `navigationController` is the only parameter needed to present or push Braze's view controller.
2. Initialize an `ABKContentCardsTableViewController` object and optionally change the title. You must also add the initialized view controller to the navigation stack.

{% subtabs global %}
{% subtab Swift %}
```swift
// MARK: - Content Cards
extension Brazemanager {

  // 1 
  func displayContentCards(navigationController: UINavigationController?){
      
  // 2 
      let contentCardsVc = ABKContentCardsTableViewController()
      contentCardsVs.title = "Content Cards"
      navigationController?.pushViewController(contentCardsVc, animated: true)
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert checkpoint %}
Proceed to compile your code and run your application.<br><br>Try displaying the `ABKContentCardsTableViewController` in your application before advancing any further.
{% endalert %}

## Next Steps

Congratulations! You've completed this best practice integration guide! An example `BrazeManager` helper file can be found [here](https://github.com/braze-inc/braze-growth-shares-ios-demo-app/blob/master/Braze-Demo/BrazeManager.swift)

Now that you have decoupled any dependencies on the Braze iOS SDK from the rest of your production code check out some of our optional advanced implementation guides:
- [Advanced Push Notification Implementation Guide]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/implementation_guide/)
- [Advanced In-App Messages Implementation Guide]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/implementation_guide/)
- [Advanced Content Card Implementation Guide]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/content_cards/implementation_guide/)

[1]: {% image_buster /assets/img/ios_sdk/ios_sdk1.png %} 
[2]: {% image_buster /assets/img/ios_sdk/ios_sdk2.png %} 
[3]: {% image_buster /assets/img/ios_sdk/ios_sdk3.png %} 
[4]: {% image_buster /assets/img/ios_sdk/ios_sdk4.png %} 