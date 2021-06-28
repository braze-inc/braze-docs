---
nav_title: iOS SDK Integration
permalink: "/ios_sdk/"
hidden: true
---

# Braze iOS SDK Integration Guide

> This iOS integration guide takes you on a step-by-step journey on setup best practices when first integrating the iOS SDK and its core components into your application. In addition, this guide will also help you decouple any dependencies on the Braze iOS SDK from the rest of your production code.

{% alert note %}
Before building out your `BrazeManager.swift` file, make sure you have integrated the Braze iOS SDK. This integration guide is compatible with the following [CocoaPods integration]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/cocoapods/). 
{% endalert %}

## BrazeManager.swift

All Braze-related dependencies should be handled in the _BrazeManager.swift_ file your existing production code calls into. The _BrazeManager.swift_ file demonstrates how to decouple any dependencies on the Braze iOS SDK from the rest of your production code. The overall objective is to have only one `import Appboy-iOS-SDK` in your entire application.

### Create BrazeManager.Swift
{% tabs local %}
{% tab Step 1: Create BrazeManager.Swift %}

##### Create BrazeManager.swift
To build out your BrazeManager.swift file, create a new Swift file named BrazeManager to add to your project at your desired location. Next, Replace `import Foundation` with `import Appboy-iOS-SDK` and then create the _BrazeManager_ class that will be used to host all Braze-related methods and variables. 

{% alert note %}
- _BrazeManager_ is an _NSObject_ class and not a struct, so it can conform to ABK delegates such as the _ABKInAppMessageUIDelegate_.
- The _BrazeManager_ object is a singleton by design to ensure that only one instance of this class will be used. This is done to provide a unified point of access to the object.
{% endalert %} 

1. Add a static variable named _shared_ that initializes the _BrazeManager_ class. This is guaranteed to be lazily initiated only once.
2. Navigate back to your app group in the Braze dashboard, and copy the _API Key_ value. Next, add a private constant variable named _apiKey_ used for your API Key. Finally, replace "YOUR-API-KEY" with the value from your App Group in the Braze dashboard. The value must be a String object.
3. Add a private computed variable named _appboyOptions_, which will store configuration values for the SDK. It will be empty for now. The key must be a String object, and the value can be of any type.

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
{% tab Step 2: Initalization %}

##### Initalize SDK from BrazeManager.swift

Add the _didFinishLaunching..._ method from the _AppDelegate.swift_ file sans return value in your BrazeManger.swift file. By creating a similar method in the _BrazeManager.swift_ file, there will not be an _import Appboy-iOS-SDK_ statement in your _AppDelegate.swift_ file. Next, initialize the SDK using your newly declared _apiKey_ and _appboyOptions_ variables; this should be done in the main thread.

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

##### Handle Appboy Initalization in AppDelegate

Next, navigate back to the _AppDelegate.swift_ file and add the following in the AppDelegate's _didFinishLaunching..._ method to handle the Appboy initialization from the _BrazeManager_ helper file.

There is no need to add an _import Appboy-iOS-SDK_ statement in the _AppDelegate.swift_.

{% subtabs global %}
{% subtab Swift %}

```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions:
[UIApplication.LaunchOptionsKey: Any]?) -> Bool {
  // Override point for customization after application launch

  BrazeManager.shared.application(application, didFinishLaunchingWithOptions: launchOptions)

  return true
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
{% tab Step 1: Push Certificate %}

##### Add Push Certificate

Go back to your existing app group in the Braze dashboard. Under __Push Notification Settings__ upload your push certificate file to your Braze dashboard and save it. <br><br>![Push Certificate]({% image_buster /assets/img/ios_sdk/ios_sdk2.png %}){: style="max-width:60%;"}

{% endtab %}
{% tab Step 2: Register %}

##### Register for Push Notifications

Next, you must register for push notifications. This guide assumes you have [set up your push credentials correctly]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/) in your Apple developer portal and Xcode project. 

The code for registering push notifications will be added in the _didFinishLaunching..._ method in the _BrazeManager.swift_ file. Your initialization code should end up looking like this:

1. Configure the contents for requesting authorization to interact with the user. These options are listed as an example.
2. Request authorization to send your users push notifications. The user's response to allow or deny push notifications is tracked in the form of the _granted_ variable.
3. Forward the push authorization results to Braze after the user interacts with the notification prompt.
4. Initiate the registration process with APNs. If the registration succeeds, the app calls your _AppDelegate's_ object's _didRegisterForRemoteNotificationsWithDeviceToken_ method. 

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
{% endalert %}

{% endtab %}
{% tab Step 3: Forward Methods %}

##### Forward Push Notification Methods

Next, you must forward the system push notifications methods from _AppDelegate.swift_ to _BrazeManager.swift_ to be handled by the Braze iOS SDK.

###### Step 1: Create Extension for Push Notificiation Code

This step is optional, but creating an extension for your push notification code in your _BrazeManager.swift_ file reads in a more organized manner as to what purpose is being served in the helper file, like so:

1. Following the pattern of not including an _import Appboy-iOS-SDK_ statement in your _AppDelegate_, we will handle the push notifications methods in the _BrazeManager.swift_ file. User's device tokens will need to be passed to Braze from the _didRegisterForRemote..._ method. Next, add the same method from the _AppDelegate_ in your _BrazeManager_ class.
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
In the _Signing & Capabilities_ tab, add _Background Modes_ support and select _Remote notificiations_ to begin your support of remote notifications originating from Braze.<br><br>![Signing & Capabilities]({% image_buster /assets/img/ios_sdk/ios_sdk3.png %})

###### Step 3: Remote Notification Handling
The Braze SDK can handle remote notifications that originate from Braze. Forward remote notifications to Braze. The SDK will automatically ignore push notifications that do not originate from Braze. Add the following method to your _BrazeManager.swift_ file in the push notification extension.

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

The Braze SDK can handle the response of push notifications that originate from Braze. Forward the response of the notifications to Braze. The SDK will automatically ignore responses from push notifications that do not originate from Braze. Add the following method to your _BrazeManager.swift_ file:

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

Next, you will want easy access to the _ABKUser_ variables and methods. This step is optional, but creating an extension for your user code in your _Brazemanager.swift_ file reads in a more organized manner as to what purpose is being served in the helper file, like so:

1. An ABKUser object represents a known or anonymous user in your iOS application. Add a computed variable to retrieve the _ABKUser_; this variable will be reused to retrieve variables about the user. The _ABKUser_ object itself is _&#95;Nonnull_, but the computed value is optional due to the nullability of the _sharedInstance()_.
2. Query the user variable to easily access the _userId_. Among the other variables, the _ABKUser_ object is responsible for (firstName, lastName, phone, homeCity, etc.)
3. Set the user by calling _changeUser()_ with a corresponding _userId_.

{% tabs local %}
{% tab Swift %}

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
{% endtab %}
{% tab Objective-C %}

{% endtab %}
{% endtabs %}

{% alert checkpoint %}
Proceed to compile your code and run your application.<br><br>Try identifying users from a successful sign-in/sign-up. Be sure you have a solid understanding of what is and what is not an appropriate user identifier. <br><br>In your dashboard, observe that the user identifier is logged before advancing any further.
{% endalert %} 

### Log Analytics

Next, you must enable your production code to log crucial analytics metrics to Braze without the need for excessive _import Appboy-iOS-SDK_ statements. Without an _import Appboy-iOS-SDK_ statement, the production code should call into the _BrazeManager_ to log all analytics. 

{% tabs local %}
{% tab Step 1: Log Custom Event %}

##### Create Extension for Analytics Code

This step is optional, but creating an extension for your analytics code in your _Brazemanager.swift_ file reads in a more organized manner as to what purpose is being served in the helper file, like so:

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

##### Create Log Custom Event Method

Create a method that matches the Braze SDK's _logCustomEvent_ method: 
```
open func logCustomEvent(_ eventName: String, withProperties properties: [AnyHashable : Any]?)
```

This is by design because only the _BrazeManager.swift_ file can directly access the Braze iOS SDK methods. Therefore, by creating a matching method, the result is the same and is done without the need for any direct dependencies on the Braze iOS SDK in your production code.

Log custom events from the _Appboy_ object to Braze. _Properties_ is an optional parameter with a default value of nil. Custom events are not required to have properties but are required to have a name. 

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
{% tab Step 2: Log Analytics %}

##### Create Log Analytics Method 

The SDK can log numerous types as custom attributes. There is no need to create helper methods for each value type that can be set. Instead, only expose one method that can filter down to the appropriate value.

{% subtabs global %}
{% subtab Swift %}
```swift
- (BOOL)setCustomAttributeWithKey:(NSString *)key andBOOLValue:(BOOL)value; 
- (BOOL)setCustomAttributeWithKey:(NSString *)key andIntegerValue:(NSIntenger)value; 
- (BOOL)setCustomAttributeWithKey:(NSString *)key andDoubleValue:(double)value; 
- (BOOL)setCustomAttributeWithKey:(NSString *)key andStringValue:(NSString *)value; 
- (BOOL)setCustomAttributeWithKey:(NSString *)key andDateValue:(NSDate *)value;
```
{% endsubtab %}
{% subtab Objective-C %}

{% endsubtab %}
{% endsubtabs %}

Custom attributes are logged from the ABKUser object. 

Create __one method__ that can encompass all of the available types that can be set for an attribute. Add this method in your _BrazeManager.swift_ file in the analytics extension.

Filter through the valid custom attribute types and call the method associated with the matching type.

The parameter _value_ is a generic type that conforms to the _Equatable_ protocol. This is explicitly done, so if the type is not what the Braze iOS SDK expects, there will be a compile-time error.

The parameters _key_ and _value_ are optional parameters that will be conditionally unwrapped in the method. This is just one way to ensure non-nil values are being passed to the Braze iOS SDK.

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
{% tab Setp 3: Log Purchase %}

##### Create Log Purchase Method

Next, create a method that matches the Braze SDK's _logPurchase_ method: 
```
open func logPurchase(_ productIdentifier: String, inCurrency currency: String, atPrice price: NSDecimalNumber, withoutQuantity quantity: UInt)
```

This is by design because only the _BrazeManager.swift_ file can directly access the Braze iOS SDK methods. Therefore, by creating a matching method, the result is the same and is done without the need for any direct dependencies on the Braze iOS SDK in your production code. 

Log purchases from the _Appboy_ object to Braze. The SDK has multiple methods for logging purchases, and this is just one example. This method also handles creating the _NSDecimal_ and _UInt_ object. How you want to handle that part is up to you, provided is just one example.

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

##### Conform to ABKInAppMessageUIDelegate
Next, enable your _BrazeManager.swift_ file code to conform to the _ABKInAppMessageUIDelegate_ to directly handle the associated methods. 

The code for conforming to the delegate will be added in the _didFinishLaunching..._ methods in the _BrazeManager.swift_ file. Your initialization code should end up looking like this:

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
Next, create an extension that conforms to the ABKInAppMessageUIDelegate.

Add this snippet below the analytics section. Note that the _BrazeManager.swift_ object is set as the delegate; this will be where the _BrazeManager.swift_ file handles all the _ABKInAppMessageUIDelegate_ methods. 

The _ABKInAppMessageUIDelegate_ does not come with any required methods, but listed below is an example of one.

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
Proceed to compile your code and run your application. <br><br>Try sending yourself an in-app message. <br><br>In the _Brazemanager.swift_ file, set a breakpoint at the entry of the example _ABKInAppMessageUIDelegate_ method. Send yourself an in-app message and confirm the breakpoint is hit before advancing any further. 
{% endalert %}

### Content Cards Extension

Next, enable your production code to display the Content Cards view controller without the need for unnecessary _import Appboy-iOS-SDK_ statements. 

This step is optional, but creating an extension for your Content Cards code in your _BrazeManager.swift_ file reads in a more organized manner as to what purpose is being served in the helper file, like so:

1. Display the _ABKContentCardsTableViewController_. An optional _navigationController_ is the only parameter needed to present or push Braze's view controller.
2. Initialize an _ABKContentCardsTableViewController_ object and optionally change the title. You must also add the initialized view controller to the navigation stack.

{% tabs local %}
{% tab Swift %}
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
{% endtab %}
{% tab Objective-C %}

{% endtab %}
{% endtabs %}

{% alert checkpoint %}
Proceed to compile your code and run your application.<br><br>Try displaying the _ABKContentCardsTableViewController_ in your application.
{% endalert %}

## Next Steps

Congratulations! You've completed this best practice integration guide! Now that you have decoupled any dependencies on the Braze iOS SDK from the rest of your production code check out some of our optional advanced implementation guides:
- [Advanced Push Notification Implementation Guide]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/implementation_guide/)
- [Advanced In-App Messages Implementation Guide]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/implementation_guide/)
- [Advanced Content Card Implementation Guide]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/content_cards/implementation_guide/)

[1]: {% image_buster /assets/img/ios_sdk/ios_sdk1.png %} 
[2]: {% image_buster /assets/img/ios_sdk/ios_sdk2.png %} 
[3]: {% image_buster /assets/img/ios_sdk/ios_sdk3.png %} 
[4]: {% image_buster /assets/img/ios_sdk/ios_sdk4.png %} 