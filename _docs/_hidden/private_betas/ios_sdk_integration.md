---
nav_title: iOS SDK Integration
permalink: "/ios_sdk/"
hidden: true
---

# Braze iOS SDK Integration Guide

> This iOS integration guide takes you on a step-by-step journey on setup best practices when first integrating the iOS SDK and its core components into your application. This guide will help you decouple any dependencies on the Braze iOS SDK from the rest of your production code.

{% alert note %}
Before building out your `BrazeManager.swift` file, make sure you have integrated the Braze iOS SDK. This integration guide is compatible with the following [CocoaPods integration]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/cocoapods/). 
{% endalert %}

## BrazeManager.swift

All Braze-related dependencies should be handled in the _BrazeManager.swift_ file your existing production code calls into. The _BrazeManager.swift_ file demonstrates how to decouple any dependencies on the Braze iOS SDK from the rest of your production code. The overall objective is to have only one import Appboy-iOS-SDK in your entire application.

### Create BrazeManager.swift

1. Create a new Swift file named BrazeManager to add to your project at your desired location. (Xcode -> New -> File)
2. Replace `import Foundation` with `import Appboy-iOS-SDK`.
3. Create the _BrazeManager_ class that will be used to host all Braze-related methods and variables. 
 
- _BrazeManager_ is an _NSObject_ class and not a struct, so it can conform to ABK delegates such as the _ABKInAppMessageUIDelegate_.
- The _BrazeManager_ object is a singleton by design to ensure that only one instance of this class will be used. This is done to provide a unified point of access to the object. 

{% tabs %}
{% tab Swift %}
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
1. Add a static variable named _shared_ that initializes the _BrazeManager_ class. This is guaranteed to be lazily initiated only once. <br><br>
2. Navigate back to your app group in the Braze dashboard, and copy the _API Key_ value. Next, add a private constant variable named _apiKey_ which will be used for your API Key. Replace "YOUR-API-KEY" with the value from your App Group in the Braze dashboard. The value must be a String object.<br><br>
3. Add a private computed variable named _appboyOptions_, which will be used to store configuration values for the SDK. It will be empty for now. The key must be a String object, and the value can be of any type.
{% endtab %}
{% tab Objective-C %}

{% endtab %}
{% endtabs %}

### Initialization

Add the following code snippet to your _BrazeManager.swift_ file to initialize your SDK. This should be done on the main thread. 

{% tabs %}
{% tab Swift %}
```swift
func application(_ application: UIapplication, didFinishLaunchingWithOptions launchOptions:[UIApplication.LaunchOptionsKey:Any]?){
  Appboy.start(withAPIKey: apikey, in: applciation, withLaunchOptions: launchOptions, withAppboyOptions: appboyOptions)

}
```
1. Add the _didFinishLaunching..._ method from the _AppDelegate.swift_ file sans return value in your BrazeManger.swift file. By creating a similar method in the _BrazeManager.swift_ file, there will not be an _import Appboy-iOS-SDK_ statement in your _AppDelegate.swift_ file.<br><br>
2. Initialize the SDK using your newly declared _apiKey_ and _appboyOptions_ variables
{% endtab %}
{% tab Objective-C %}

{% endtab %}
{% endtabs %}

Next, navigate back to the _AppDelegate.swift_ file and add the following in the AppDelegate's _didFinishLaunching..._ method to handle the Appboy initialization from the _BrazeManager_ helper file.

There is no need to add an _import Appboy-iOS-SDK_ statement in the _AppDelegate.swift_.

{% tabs %}
{% tab Swift %}

```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions:
[UIApplication.LaunchOptionsKey: Any]?) -> Bool {
  // Override point for customization after application launch

  BrazeManager.shared.application(application, didFinishLaunchingWithOptions: launchOptions)

  return true
```
{% endtab %}
{% tab Objective-C %}

{% endtab %}
{% endtabs %}

{% alert checkpoint %}
Proceed to compile your code and run your application.<br><br>At this point, the SDK should be up and running. In your dashboard, observe that sessions are being logged before advancing any further.
{% endalert %}

### Push Notifications

#### Add Push Certificate

Go back to your existing app group in the Braze dashboard. Under __Push Notification Settings__ upload your push certificate file to your Braze dashboard and save it. <br><br>![Push Certificate][2]{: style="max-width:60%;"}

#### Register for Push Notifications

Next, you must register for push notifications. This guide assumes you have set up your push credentials correctly in your Apple developer portal and Xcode project. 

The code for registering push notifications will be added in the _didFinishLaunching..._ method in the _BrazeManager.swift_ file. Your initialization code should end up looking like this:

{% tabs %}
{% tab Swift %}
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
1. Configure the contents for requesting authorization to interact with the user. These options are listed as an example.<br><br>
2. Request authorization to send your users push notifications. The user's response to allow or deny push notifications is tracked in the form of the _granted_ variable.<br><br>
3. Forward the push authorization results to Braze after the user interacts with the notification prompt.<br><br>
4. Initiate the registration process with APNs. If the registration succeeds, the app calls your _AppDelegate's_ object's _didRegisterForRemoteNotificationsWithDeviceToken_ method. 
{% endtab %}
{% tab Objective-C %}

{% endtab %}
{% endtabs %}

{% alert checkpoint %}
Proceed to compile your code and run your application.
- In your app, confirm that you are being prompted for push notifications before advancing any further.
- If you are not prompted, try deleting and re-installing the app to ensure the push notification prompt was not displayed previously.
{% endalert %}

#### Forward Push Notification Methods

Next, you must forward the system push notifications methods from _AppDelegate.swift_ to _BrazeManager.swift_ to be handled by the Braze iOS SDK.

##### Step 1: Create Extension for Push Notificiation Code

This step is optional, but creating an extension for your push notification code in your _BrazeManager.swift_ file reads in a more organized manner as to what purpose is being served in the helper file, like so:

{% tabs %}
{% tab Swift %}
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
1. Following the pattern of not including an _import Appboy-iOS-SDK_ statement in your _AppDelegate_, we will handle the push notifications methods in the _BrazeManager.swift_ file. User's device tokens will need to be passed to Braze from the _didRegisterForRemote..._ method. Add the same method from the _AppDelegate_ in your _BrazeManager_ class.<br><br>
2. Add the following line inside the method to register the device token to Braze. This is necessary for Braze to associate the token with the current device. 
{% endtab %}
{% tab Objective-C %}

{% endtab %}
{% endtabs %}

##### Step 2: Support Remote Notifications
In the _Signing & Capabilities_ tab, add _Background Modes_ support and select _Remote notificiations_ to begin your support of remote notifications originating from Braze.<br><br>![Signing & Capabilities][3]

##### Step 3: Remote Notification Handling
The Braze SDK can handle remote notifications that originate from Braze. Add the following method to your _BrazeManager.swift_ file in the push notification extension:

{% tabs %}
{% tab Swift %}
```swift
func application(_ application: UIApplication, didReceiveRemoteNotification userInfo: [AnyHashable : Any], fetchCompletionHandler completionHandler: @escaping (UIBackgroundFetchResult) -> Void) {
  Appboy.sharedInstance()?.register(application, didReceiveRemoteNotification: userInfo, fetchCompletiionHandler: completionHandler)
}
```
1. Forward remote notifications to Braze. The SDK will automatically ignore push notifications that do not originate from Braze.
{% endtab %}
{% tab Objective-C %}

{% endtab %}
{% endtabs %}

##### Step 4: Forward Notification Responses

The Braze SDK can handle the response of push notifications that originate from Braze. Add the following method to your _BrazeManager.swift_ file:

{% tabs %}
{% tab Swift %}
```swift
func userNotificationCenter(_ center: UNUserNotificationCenter, didReceive response: UNNotificationResponse, withCompletionHandler completionHandler: @escaping () -> Void) {
  Appboy.sharedInstance()?.userNotificationCenter(center, didReceive: response, withCompletionHandler: completionHandler)
}
```
1. Forward the response of the notifications to Braze. The SDK will automatically ignore responses from push notifications that do not originate from Braze.
{% endtab %}
{% tab Objective-C %}

{% endtab %}
{% endtabs %}

{% alert checkpoint %}
Proceed to Compile your code and run your application. <br><br>Try sending yourself a push notification from the Braze dashboard and observe that analytics are being logged from push notifications before advancing any further. 
{% endalert %}

### Access User Variables and Methods

Next, you will want easy access the _ABKUser_ variables and methods. This step is optional, but creating an extension for your user code in your _Brazemanager.swift_ file reads in a more organized manner as to what purpose is being served in the helper file, like so:

{% tabs %}
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
1. An ABKUser object represents a known or anonymous user in your iOS application. Add a computed variable to retrieve the _ABKUser_; this variable will be reused to retrieve variables about the user. The _ABKUser_ object itself is _&#95;Nonnull_, but the computed value is optional due to the nullability of the _sharedInstance()_.<br><br>
2. Query the user variable to easily access the _userId_, among the other variables the _ABKUser_ object is responsible for (firstName, lastName, phone, homeCity, etc.)<br><br>
3. Set the user by calling _changeUser()_ with a corresponding _userId_.
{% endtab %}
{% tab Objective-C %}

{% endtab %}
{% endtabs %}

{% alert checkpoint %}
Proceed to compile your code and run your application.<br><br>Try identifying users from a successful sign-in/sign-up. Be sure you have a solid understanding of what is and what is not an appropriate user identifier. <br><br>In your dashboard, observe that the user identifier is logged before advancing any further.
{% endalert %} 

### Log Analytics

Next, you must enable your production code to log crucial analytics metrics to Braze without the need for excessive _import Appboy-iOS-SDK_ statements. Without an _import Appboy-iOS-SDK_ statement, the production code should call into the _BrazeManager_ to log all analytics. 

This step is optional, but creating an extension for your analytics code in your _Brazemanager.swift_ file reads in a more organized manner as to what purpose is being served in the helper file, like so:

```swift
//MARK: -Analytics
extension BrazeManager {

}
```

Create a method that matches the Braze SDK's _logCustomEvent_ method: 
```swift
open func logCustomEvent(_ eventName: String, withProperties properties: [AnyHashable : Any]?)
```

This is by design because only the _BrazeManager.swift_ file can directly access the Braze iOS SDK methods. By creating a matching method, the result is the same and is done without the need for any direct dependencies on the BrazeiOS SDK in your production code.

{% tabs %}
{% tab Swift %}
```swift
func logCustomEvent(_ eventName: String, withProperties properties: [AnyHashable: Any]? = nil){
  Appboy.sharedInstance()?.logCustomEvent(eventName, withProperties: properties)
}
```
1. Log custom events from the _Appboy_ object to Braze. _Properties_ is an optional parameter with a default value of nil. Custom events are not required to have properties but are required to have a name. 
{% endtab %}
{% tab Objective-C %}

{% endtab %}
{% endtabs %}

The SDK can log numerous types as custom attributes. There is no need to create helper methods for each value type that can be set. Only expose one method that can filter down to the appropriate value.

```swift
- (BOOL)setCustomAttributeWithKey:(NSString *)key andBOOLValue:(BOOL)value; 
- (BOOL)setCustomAttributeWithKey:(NSString *)key andIntegerValue:(NSIntenger)value; 
- (BOOL)setCustomAttributeWithKey:(NSString *)key andDoubleValue:(double)value; 
- (BOOL)setCustomAttributeWithKey:(NSString *)key andStringValue:(NSString *)value; 
- (BOOL)setCustomAttributeWithKey:(NSString *)key andDateValue:(NSDate *)value;
```

Custom attributes are logged from the ABKUser object. 

Create __one method__ that can encompass all of the available types that can be set for an attribute. Add this method in your _BrazeManager.swift_ file in the analytics extension.

{% tabs %}
{% tab Swift %}
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
The parameter _value_ is a generic type that conforms to the _Equatable_ protocol. This is explicitly done, so if the type is not what the Braze iOS SDK expects, there will be a compile-time error.

The parameters _key_ and _value_ are optional parameters that will be conditionally unwrapped in the method. This is just one way to ensure non-nil values are being passed to the Braze iOS SDK.

Filter through the valid custom attribute types and call the method associated with the matching type.
{% endtab %}
{% tab Objective-C %}

{% endtab %}
{% endtabs %}

Next, create a method that matches the Braze SDK's _logPurchase_ method: 
```swift
open func logPurchase(_ productIdentifier: String, inCurrency currency: String, atPrice price: NSDecimalNumber, withoutQuantity quantity: UInt)
```

This is by design because only the _BrazeManager.swift_ file can directly access the Braze iOS SDK methods. By creating a matching method, the result is the same and is done without the need for any direct dependencies on the Braze iOS SDK in your production code. 

{% tabs %}
{% tab Swift %}
```swift
func logPurchase(_ productIdentifier: String, inCurrency currency: String, atPrice price:
String, withQuantity quantity: Int) {

  Appboy.sharedInstance()?.logPurchase(productIdentifier, inCurrency: currency, atPrice: NSDecimalNumber(string: price), withQuantity: UInt(quantity))

}
```
1. Log purchases from the _Appboy_ object to Braze. The SDK has multiple methods for logging purchases, and this is just one example. This method also handles creating the _NSDecimal_ and _UInt_ object. How you want to handle that part is up to you, provided is just one example.
{% endtab %}
{% tab Objective-C %}

{% endtab %}
{% endtabs %}

{% alert checkpoint %}
Proceed to compile your code and run your application. <br><br>Try logging custom events.<br><br>In your dashboard, observe that the custom events are logged before advancing any further. 
{% endalert %}

### In-App Messages
Next, enable your _BrazeManager.swift_ file code to conform to the _ABKInAppMessageUIDelegate_ to directly handle the associated methods. 

The code for conforming to the delegate will be added in the _didFinishLaunching..._ methods in the _BrazeManager.swift_ file. Your initialization code should end up looking like this:

{% tabs %}
{% tab Swift %}
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
{% endtab %}
{% tab Objective-C %}

{% endtab %}
{% endtabs %}

Next, create an extension that conforms to the ABKInAppMessageUIDelegate.

Add this snippet below the analytics section. Note that the _BrazeManager.swift_ object is set as the delegate; this will be where the _BrazeManager.swift_ file handles all the _ABKInAppMessageUIDelegate_ methods. 

The _ABKInAppMessageUIDelegate_ does not come with any required methods, but listed above is an example of one.

{% tabs %}
{% tab Swift %}
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
{% endtab %}
{% tab Objective-C %}

{% endtab %}
{% endtabs %}

{% alert checkpoint %}
Proceed to compile your code and run your application. <br><br>Try sending yourself an in-app message. <br><br>In the _Brazemanager.swift_ file, set a breakpoint at the entry of the example _ABKInAppMessageUIDelegate_ method. Send yourself an in-app message and confirm the breakpoint is hit before advancing any further. 
{% endalert %}

### Content Cards Extension

Next, enable your production code to display the Content Cards view controller without the need for unnecessary _import Appboy-iOS-SDK_ statements. 

This step is optional, but creating an extension for your Content Cards code in your _BrazeManager.swift_ file reads in a more organized manner as to what purpose is being served in the helper file, like so:

{% tabs %}
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
1. Display the _ABKContentCardsTableViewController_. An optional _navigationController_ is the only parameter needed to present or push Braze's view controller.<br><br>
2. Initialize an _ABKContentCardsTableViewController_ object and optionally change the title. You must also add the initialized view controller to the navigation stack.
{% endtab %}
{% tab Objective-C %}

{% endtab %}
{% endtabs %}

{% alert checkpoint %}
Proceed to compile your code and run your application.<br><br>Try displaying the _ABKContentCardsTableViewController_ in your application.
{% endalert %}

## Next Steps

Congratulations! You've completed this best practice integration guide! Now that you have decoupled any dependencies on the Braze iOS SDK from the rest of your production code, check out some of our optional advanced implementation guides:
- [Advanced Push Notification Implementation Guide]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/implementation_guide/)
- [Advanced In-App Messages Implementation Guide]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/implementation_guide/)
- [Advanced Content Card Implementation Guide]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/content_cards/implementation_guide/)

[1]: {% image_buster /assets/img/ios_sdk/ios_sdk1.png %} 
[2]: {% image_buster /assets/img/ios_sdk/ios_sdk2.png %} 
[3]: {% image_buster /assets/img/ios_sdk/ios_sdk3.png %} 
[4]: {% image_buster /assets/img/ios_sdk/ios_sdk4.png %} 