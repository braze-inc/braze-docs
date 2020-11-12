---
nav_title: SDK Migration from Airship to Braze
permalink: /sdk_migration_guide_airship/
hidden: true
page_type: reference
---

# Migrating SDKs from Airship to Braze (iOS)

> At Braze, we understand that moving to an entirely new platform and SDK can be daunting, but with the following migration guide, straightforward code-level examples, and impressive feature set the Braze platform brings to the table, we don't think you'll mind. Listed below, we have included the Braze equivalent to many key Airship features as well as "rip-and-replace" code snippets to make your migration quick, simple, and painless. 

## Beyond the Code
### Token Management
Airship uses their own Airship tokens, while Braze uses Apple's device token for iOS.

__Braze Perspective:__<br>
We ensure customers can keep track of communication with their users such as push notifications when in the process of migrating from Airship to Braze (Hard cutover to 100% Braze, 50% Airship 50% Braze, etc.).

To migrate tokens from Airship to Braze, we recommend [migrating tokens via API]({{site.baseurl}}/help/help_articles/push/push_token_migration/#migration-via-api). The documentation linked contains specific steps, as well as an example payload, but the overall process is as follows:

1. Import the tokens via the [/users/track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) endpoint. For large batch imports, we have resources available to help expedite the process. Please reach out to your COM or SA for more details!
2. If the token already exists in Braze it will be ignored, otherwise an anonymous profile will be generated.
3. QA the push integration. Ensure that the steps to [configure Push]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/ios/push_notifications/#step-1-configure-the-apple-developer-settings) have been completed. 

### Mobile Wallet
Airship uses their own mobile wallet integration, while Braze uses a Passkit integration. <br>Visit this [implementation guide]({{site.baseurl}}/partners/additional_channels/mobile_wallet/passkit/) to learn how to integrate Passkit into Braze.

## Campaign Channel Configuration
At a high level, Braze is a truly unique tool in the customer engagement space. Because of our extensive customization options and growing feature set, campaigns migrated into Braze often benefit from replanning and rethinking to leverage these tools - and our campaign planning framework (reach out to your COM or SA for more details) is purpose-built for just that.

### Segmentation
Airship allows campaigns to target users, while Braze offers multiple segmentation filters to provide a rich user experience for your customers.

### Push Notifications
Airship uses only one push channel for iOS & Android, while Braze requires separate channels (one for iOS, one for Android).

__Braze Perspective:__<br>
We recognize the key differences between the two push platforms and leverage them in the Braze dashboard.

## Code Rip and Replace
### Installation
#### Airship
```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) {
     
    UAirship.takeOff(UAConfig.default())
     
    // Location
    UALocation.shared()?.isLocationUpdatesEnabled = true
    UALocation.shared().isBackgroundLocationUpdatesAllowed = true
     
    // Push Notifications
    UAirship.push()?.notificationOptions = [.alert, .badge, .sound]
    UAirship.push()?.userPushNotificationsEnabled = true
    UAirship.push()?.pushNotificationDelegate = self
     
    // In-App Messages
    UAInAppAutomation.shared()?.inAppMessageManager.delegate = self
    UAInAppAutomation.shared()?.inAppMessageManager.displayInterval = 30
}
```
#### Braze 
```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) {
         
    Appboy.start(withApiKey: apiKey, in: application, withLaunchOptions: launchOptions, withAppboyOptions: appboyOptions)
     
    // Location
    locationManager.requestAlwaysAuthorization()
     
    // Push Notifications
    let options: UNAuthorizationOptions = [.alert, .sound, .badge]
    UNUserNotificationCenter.current().requestAuthorization(options: options) { (granted, error) in
      Appboy.sharedInstance()?.pushAuthorization(fromUserNotificationCenter: granted)
    }
    UIApplication.shared.registerForRemoteNotifications()
     
    // In-App Messages
    Appboy.sharedInstance()?.inAppMessageController.inAppMessageUIController?.setInAppMessageUIDelegate?(self)
}
```

### Getting and Setting User ID
#### Airship
```swift
extension AirshipManager {
  var userId: String? {
    return UAirship.namedUser()?.identifier
   }
     
  func setUser(_ userId: String) {
    UAirship.namedUser()?.identifier = userId
  }
}
```
#### Braze
```swift
extension AppboyManager {
  var userId: String? {
     return Appboy.sharedInstance()?.user.userID
  }
     
  func changeUser(_ userId: String) {
    Appboy.sharedInstance()?.changeUser(userId)
  }
}
```
### Handling Push Notifications
#### Airship
```swift
extension AirshipManager: UAPushNotificationDelegate {
  func receivedBackgroundNotification(_ notificationContent: UANotificationContent, completionHandler: @escaping (UIBackgroundFetchResult) -> Void) {
    // Background content-available notification
    completionHandler(.noData)
  }
   
  func receivedForegroundNotification(_ notificationContent: UANotificationContent, completionHandler: @escaping () -> Void) {
    // Foreground notification
    completionHandler()
  }
   
  func receivedNotificationResponse(_ notificationResponse: UANotificationResponse, completionHandler: @escaping () -> Void) {
    // Notification response
    completionHandler()
  }
}
```
#### Braze
```swift
extension AppboyManager {
  func application(_ application: UIApplication, didRegisterForRemoteNotificationsWithDeviceToken deviceToken: Data) {
    Appboy.sharedInstance()?.registerDeviceToken(deviceToken)
  }
   
  func application(_ application: UIApplication, didReceiveRemoteNotification userInfo: [AnyHashable : Any], fetchCompletionHandler completionHandler: @escaping (UIBackgroundFetchResult) -> Void) {
    Appboy.sharedInstance()?.register(application, didReceiveRemoteNotification: userInfo, fetchCompletionHandler: completionHandler)
  }
   
  func userNotificationCenter(_ center: UNUserNotificationCenter, didReceive response: UNNotificationResponse, withCompletionHandler completionHandler: @escaping () -> Void) {
    Appboy.sharedInstance()?.userNotificationCenter(center, didReceive: response, withCompletionHandler: completionHandler)
  }
}
```
### Analytics
#### Airship
```swift
extension AirshipManager {
  func trackEvent(with name: String, value: NSDecimalNumber? = nil, eventProperties: [String: Any]? = nil) {
    let event = UACustomEvent(name: name, value: value)
     
    if let eventProperties = eventProperties {
      event.properties = eventProperties
    }
 
    event.track()
  }
   
  func applyMutationsWithValue(_ value: String, forAttribute attribute: String) {
    let mutations = UAAttributeMutations()
    mutations.setString(value, forAttribute: attribute)
    UAirship.namedUser().apply(mutations)
  }
}
```
#### Braze 
```swift
extension AppboyManager {
  func logCustomEvent(_ eventName: String, withProperties properties: [AnyHashable: Any]? = nil) {
    Appboy.sharedInstance()?.logCustomEvent(eventName, withProperties: properties)
  }
   
  func setCustomAttributeWithKey(_ key: String, andStringValue value: String) {
    Appboy.sharedInstance()?.user.setCustomAttributeWithKey(key, andStringValue: value)
  }
   
  func logPurchase(productIdentifier: String, inCurrency currency: String, atPrice price: String, withQuanitity quanity: Int) {
    Appboy.sharedInstance()?.logPurchase(productIdentifier, inCurrency: currency, atPrice: NSDecimalNumber(string: price), withQuantity: UInt(quanity))
  }
}
```
### Handling In-App Messages
#### Airship
```swift

extension AirshipManager: UAInAppMessagingDelegate {
  func extend(_ message: UAInAppMessage) -> UAInAppMessage {
      // Can be used to modify the message before it is displayed
      return message
  }
 
  func messageWillBeDisplayed(_ message: UAInAppMessage, scheduleID: String) {
    // Message displayed
  }
 
  func messageFinishedDisplaying(_ message: UAInAppMessage, scheduleID: String, resolution: UAInAppMessageResolution) {
      // Message finished
  }
}
```
#### Braze
```swift
extension AppboyManager: ABKInAppMessageControllerDelegate {
  func before(inAppMessageDisplayed inAppMessage: ABKInAppMessage) -> ABKInAppMessageDisplayChoice {
    // This delegate method defines whether the in-app message will be displayed now, displayed later, or discarded.
    return .displayInAppMessageNow
  }
   
  func beforeControlMessageImpressionLogged(_ inAppMessage: ABKInAppMessage) -> ABKInAppMessageDisplayChoice {
    // This delegate method defines the timing of when the control in-app message impression event should be logged: now, later, or discarded.
    return .displayInAppMessageNow
  }
}
 
extension AppboyManager: ABKInAppMessageUIDelegate {
  func on(inAppMessageDismissed inAppMessage: ABKInAppMessage) {
    // Use this method to perform any custom logic that should execute after the in-app message has been dismissed
  }
   
  func on(inAppMessageClicked inAppMessage: ABKInAppMessage) -> Bool {
    // This delegate method is fired when the user clicks on a slide-up in-app message or a modal/full in-app message without button(s) on it.
    return true
  }
   
  func on(inAppMessageButtonClicked inAppMessage: ABKInAppMessageImmersive, button: ABKInAppMessageButton) -> Bool {
    // This delegate method is fired whenever the user clicks a button on the in-app message.
    return true
  }
   
  func on(inAppMessageHTMLButtonClicked inAppMessage: ABKInAppMessageHTMLBase, clickedURL: URL?, buttonID buttonId: String) -> Bool {
    // This delegate method is fired whenever the user clicks a link on the HTML in-app message.
    return true
  }
}
```
### Content Cards / Message Center
#### Airship
```swift
extension AirshipManager {
  func displayMessageCenter() {
    UAMessageCenter.shared()?.defaultUI.title = "My Message Center"
     
    let style = UAMessageCenterStyle()
    style.navigationBarColor = .black
    style.titleColor = .white
    style.tintColor = .white
     
    UAMessageCenter.shared()?.defaultUI.messageCenterStyle = style
    UAMessageCenter.shared()?.display()
  }
}
```
#### Braze 
```swift
extension AppboyManager {
  func displayContentCards(navigationController: UINavigationController?) {
    let contentCardsVc = ABKContentCardsTableViewController()
    contentCardsVc.title = "My Message Center"
    contentCardsVc.disableUnreadIndicator = true
    navigationController?.pushViewController(contentCardsVc, animated: true)
  }
}
```
