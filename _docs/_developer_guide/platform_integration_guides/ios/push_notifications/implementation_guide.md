---
nav_title: Implementation Guide
platform: iOS
page_order: 7
description: ""
---

# Push Notification Implementation Guide

> This implementation guide covers how to leverage push notification content extensions to get the most out of your push messages. Also included are three use cases built by our team, accompanying code snippets, and guidance on logging analytics. Visit our Braze Demo Repository [here](https://github.com/braze-inc/braze-growth-shares-ios-demo-app)! Please note that this implementation guide is centered around a Swift implementation, but Objective-C snippets are provided for those interested.

## Notification Content Extensions

Push notifications while seemingly standard across different platforms offer immense customization options past what is normally implemented in the default UI. When a push notification is 3D pressed, long pressed or, "viewed" through the banner options, content notification extensions enable a custom view of the expanded push notification. The customization options this extended view offer are quite expansive, offering similar functionality to that you'd find in an in-app message.

While implementing push in this way may be unfamiliar to some, one of our well-known features at Braze, [Push Stories]({{site.baseurl}}/user_guide/message_building_by_channel/push/advanced_push_options/push_stories/), are a prime example of what a custom view for notification content extension can look like!

## Use Case and Implementation Walkthrough

There are three push notifications content extension types provided. Each type has a concept walkthrough, potential use cases, and a look into how Push notification variables may look and be used in the Braze dashboard:
- [Interactive Push Notification](#interactive-push-notification)
- [Personalized Push Notifications](#personalized-push-notifications)
- [Information Capture Push Notifications](#information-capture-push-notification)

### Interactive Push Notification

Push notifications can respond to user actions inside a content extension. As of iOS 12, content extensions now have the option of being interactive! This interactivity offers many possibilities to get your users engaged in your push notification and your service. 

Push notifications can be opened in three different ways: 
- A 3D press (hard press) on the push banner
- A long press on the push banner
- Swiping the banner to the right and selecting "View"

3D presses can be disabled in a device's accessibility settings so it's important to note other ways users can access your push content.  
#### Dashboard Configuration

To set up a custom view in the dashboard you must notify Braze you would like to use a custom category, register the category, and then toggle notification buttons on. While notifications buttons aren't directly used, they are required to signal which view to be displayed in the content extension. The given pre-registered custom iOS category is then checked against the code. Lastly, since pushes with content extensions aren't always apparent, we recommend including a call to action to get your user to make the most of their push experience.

In the code, we have an `UNNotificationExtensionCategory` with the strong "match_game". The value given here must match what is set in the Braze dashboard. Lastly, you must also enable user interactions by toggling the `UNNotificationExtensionUserInteractionEnabled` attribute. After this, your touch is enabled. 

Interested in implementing this in your push notifications? Take a look at the [logging and analytics section](#logging-vs-analytics) to get a better understanding of how the flow of data should look. 

The example shown below is a custom HTML in-app message. It can be replicated in a push notification content extension, where the user taps it. You can actually do in-app message communications in a push. 

### Personalized Push Notifications

Push notifications can display user-specific information inside a content extension. The example to the right shows a notification of a Braze LAB user who has completed a Braze session and is now encouraged to hold this notification to check their progress. The information provided here is detailed and user-specific and can be fired off as a session is completed or specific user action is taken.

#### Dashboard Configuration

To set up a personalized push in the dashboard, you must register the specific category you would like to display, and then within the key-value pairs, using standard Liquid, set up the appropriate user attributes you would like to display. We can personalize these views based on the specific user attributes of a specific user profile.  

#### Handling Key-Value Pairs

The method below, `didReceive` is called when the content extension has received a notification. The key-value pairs provided in the dashboard are represented in the code through the use of a `userInfo` dictionary. This information is then parsed and sent to the push notification.

__Parsing Key-Value Pairs from Push Notifications__<br>

{% tabs %}
{% tab Swift %}
``` swift 
func didReceive(_ notification: UNNotification) {
  let userInfo = notification.request.content.userInfo
     
  guard let value = userInfo["YOUR-KEY-VALUE-PAIR"] as? String,
        let otherValue = userInfo["YOUR-OTHER-KEY-VALUE-PAIR"] as? String,
  else { fatalError("Key-Value Pairs are incorrect.")}
 
  ...
}
```
{% endtab %}
{% tab Objective-C %}
```objc
- (void)didReceiveNotification:(nonnull UNNotification *)notification {
  NSDictionary *userInfo = notification.request.content.userInfo;
   
  if ([userInfo objectForKey:@"YOUR-KEY-VALUE-PAIR"] && [userInfo objectForKey:@"YOUR-OTHER-KEY-VALUE-PAIR"]) {
 
  ...
 
  } else {
    [NSException raise:NSGenericException format:@"Key-Value Pairs are incorrect"];
  }
}
```
{% endtab %}
{% endtabs %}

#### Other Use Cases

The ideas for progress-based and user-focused push content extensions are endless, some examples could be adding the option to share your progress across different platforms, achievement unlocked, punch cards, or even onboarding checklists. 

### Information Capture Push Notification

Push notifications can capture user information inside a content extension, allowing you to push the limits of what is possible with a push. Examining the flow shown below, the view is able to respond to state changes. Those state change components are represented in each image. 

1. User receives a push, and push is opened and prompts the user for information. 
2. Information is given, if valid, the register button is shown.
3. Confirmation view is displayed.
4. Push is dismissed. 

Not that the information requested here can be a wide range of things, it doesn't have to be email specific.

#### Dashboard Configuration

To set up information capture push in the dashboard, you must register and set your custom category, and provide whatever key-value pairs are needed. As seen in the example, you may also include an image in your push. To do this, you must set the notification style to Rich Notification and include a rich push image as you normally would. 

#### Handling Buttom Actions

Each action button is uniquely identified, so in the code, we are checking if our response identifier is equal to our registerIndentifier and that's how we know the user clicked register. And then on your backend, save this event and attribute, and lastly dismiss the notification. 

__Handling Push Notification Action Button Responses__<br>
Push notification action buttons are uniquely identified to handle responses from button presses accordingly.

{% tabs %}
{% tab Swift %}
``` swift 
func didReceive(_ response: UNNotificationResponse, completionHandler completion: @escaping (UNNotificationContentExtensionResponseOption) -> Void) {
  if response.actionIdentifier == "YOUR-REGISTER-IDENTIFIER" {
    completion(.dismiss)
  } else {
    completion(.doNotDismiss)
  }
}
```
{% endtab %}
{% tab Objective-C %}
```objc
- (void)didReceiveNotificationResponse:(UNNotificationResponse *)response completionHandler:(void (^)(UNNotificationContentExtensionResponseOption))completion {
  if ([response.actionIdentifier  isEqual: @"YOUR-REGISTER-IDENTIFIER"]) {
    completion(UNNotificationContentExtensionResponseOptionDismiss);
  } else {
    completion(UNNotificationContentExtensionResponseOptionDoNotDismiss);
  }
}
```
{% endtab %}
{% endtabs %}

##### Dismissing Pushes

Push notifications can be automatically dismissed from an action button press and there exist three pre-built push dismissal options to choose from:

1. completion(.dismiss) - Dismisses the notification
2. completion(.doNotDismiss) - Notification stays open
3. completion(.dismissAndForward) - Push dismisses and the user gets forwarded into the application.

#### Other Use Cases

Requesting user input through push notifications is an exciting opportunity that many companies do not take advantage of. In these push messages, you can not only request basic information like name, email, or number, but you could also prompt users to complete a user profile if unfinished, or even to submit feedback. 

## Logging vs. Analytics

### Logging with the Braze API

Logging analytics can only be done in real-time with the help of the customer's server hitting Braze's API user/track endpoint. If you would like to log analytics with the API, it requires the userId parameter, which cannot be queried from Braze SDK.

### Logging Manually 

Logging manually will require you to create, save, and retrieve analytics, this requires some custom developer work on your end. The code snippets shown below will help address this. 

It's also important to note that analytics are not sent to Braze until the mobile application is subsequently launched. This means that, depending on your dismissal settings, there often exists an indeterminate period of time between when a push notification is dismissed and the mobile app is launched and the analytics are retrieved. While this time buffer may not affect all use cases, users should consider the impact and if necessary, adjust their user journey to include opening the application to address this concern. 

### Code Snippets

#### Saving Custom Event

To save custom events you must create the analytics from scratch. This is done by creating a dictionary with metadata and saving the data through the use of a helper file.

{% tabs %}
{% tab Swift %}
``` swift 
func saveCustomEvent(with properties: [String: Any]? = nil) {
  let customEventDictionary = Dictionary(eventName: "YOUR-EVENT-NAME", properties: properties)
  let remoteStorage = RemoteStorage(storageType: .suite)
     
  if var pendingEvents = remoteStorage.retrieve(forKey: .pendingCustomEvents) as? [[String: Any]] {
    pendingEvents.append(contentsOf: [customEventDictionary])
    remoteStorage.store(pendingEvents, forKey: .pendingCustomEvents)
  } else {
    remoteStorage.store([customEventDictionary], forKey: .pendingCustomEvents)
  }
}
```
{% endtab %}
{% tab Objective-C %}
```objc
- (void)saveCustomEvent:(NSDictionary<NSString *, id> *)properties {
  NSDictionary<NSString *, id> *customEventDictionary = [[NSDictionary alloc] initWithEventName:@"YOUR-EVENT-NAME" properties:properties];
 
  RemoteStorage *remoteStorage = [[RemoteStorage alloc] initWithStorageType:StorageTypeSuite];
  NSMutableArray *pendingEvents = [[remoteStorage retrieveForKey:RemoteStorageKeyPendingCustomEvents] mutableCopy];
   
  if (pendingEvents) {
    [pendingEvents addObject:customEventDictionary];
    [remoteStorage store:pendingEvents forKey:RemoteStorageKeyPendingCustomAttributes];
  } else {
    [remoteStorage store:@[ customEventDictionary ] forKey:RemoteStorageKeyPendingCustomAttributes];
  }
}
```
{% endtab %}
{% endtabs %}

1. Initialize a dictionary with event metadata
2. Initialize userDefaults to retrieve and store the event data
3. If there is an existing array, append new data to the existing array and save
4. If there is not an existing array, save the new array to userDefaults

{% details Remote Storage Helper File %}
{% tabs %}
{% tab Swift %}
```swift
enum RemoteStorageKey: String, CaseIterable {
   
  // MARK: - Notification Content Extension Analytics
  case pendingCustomEvents = "pending_custom_events"
  case pendingCustomAttributes = "pending_custom_attributes"
  case pendingUserAttributes = "pending_user_attributes"
}
 
enum RemoteStorageType {
  case standard
  case suite
}
 
class RemoteStorage: NSObject {
  private var storageType: RemoteStorageType = .standard
  private lazy var defaults: UserDefaults = {
    switch storageType {
    case .standard:
      return .standard
    case .suite:
      return UserDefaults(suiteName: "YOUR-APP=GROUP")!
    }
  }()
   
  init(storageType: RemoteStorageType = .standard) {
    self.storageType = storageType
  }
   
  func store(_ value: Any, forKey key: RemoteStorageKey) {
    defaults.set(value, forKey: key.rawValue)
  }
   
  func retrieve(forKey key: RemoteStorageKey) -> Any? {
    return defaults.object(forKey: key.rawValue)
  }
   
  func removeObject(forKey key: RemoteStorageKey) {
    defaults.removeObject(forKey: key.rawValue)
  }
   
  func resetStorageKeys() {
    for key in RemoteStorageKey.allCases {
      defaults.removeObject(forKey: key.rawValue)
    }
  }
}
```
{% endtab %}
{% tab Objective-C %}
```objc
@interface RemoteStorage ()
 
@property (nonatomic) StorageType storageType;
@property (nonatomic, strong) NSUserDefaults *defaults;
 
@end
 
@implementation RemoteStorage
 
- (id)initWithStorageType:(StorageType)storageType {
  if (self = [super init]) {
    self.storageType = storageType;
  }
  return self;
}
 
- (void)store:(id)value forKey:(RemoteStorageKey)key {
  [[self defaults] setValue:value forKey:[self rawValueForKey:key]];
}
 
- (id)retrieveForKey:(RemoteStorageKey)key {
  return [[self defaults] objectForKey:[self rawValueForKey:key]];
}
 
- (void)removeObjectForKey:(RemoteStorageKey)key {
  [[self defaults] removeObjectForKey:[self rawValueForKey:key]];
}
 
- (void)resetStorageKeys {
  [[self defaults] removeObjectForKey:[self rawValueForKey:RemoteStorageKeyPendingCustomEvents]];
  [[self defaults] removeObjectForKey:[self rawValueForKey:RemoteStorageKeyPendingCustomAttributes]];
  [[self defaults] removeObjectForKey:[self rawValueForKey:RemoteStorageKeyPendingUserAttributes]];
}
 
- (NSUserDefaults *)defaults {
  if (!self.defaults) {
    switch (self.storageType) {
      case StorageTypeStandard:
        return [NSUserDefaults standardUserDefaults];
        break;
      case StorageTypeSuite:
        return [[NSUserDefaults alloc] initWithSuiteName:@"YOUR-SUITE-NAME"];
    }
  } else {
    return self.defaults;
  }
}
 
- (NSString*)rawValueForKey:(RemoteStorageKey)remoteStorageKey {
    switch(remoteStorageKey) {
    case RemoteStorageKeyPendingCustomEvents:
      return @"pending_custom_events";
    case RemoteStorageKeyPendingCustomAttributes:
      return @"pending_custom_attributes";
    case RemoteStorageKeyPendingUserAttributes:
      return @"pending_user_attributes";
    default:
      [NSException raise:NSGenericException format:@"Unexpected FormatType."];
  }
}
```
{% endtab %}
{% endtabs %}
{% enddetails %}

#### Sending Custom Events to Braze

After the SDK is initialized is the best time to log any saved analytics from a notification content extension. This can be done by, looping through the pending events, checking for the "Event Name" key, setting the appropriate values in Braze, and then clearing the storage for the next time this function is needed.

{% tabs %}
{% tab Swift %}
``` swift 
func logPendingCustomEventsIfNecessary() {
  let remoteStorage = RemoteStorage(storageType: .suite)
  guard let pendingEvents = remoteStorage.retrieve(forKey: .pendingCustomEvents) as? [[String: Any]] else { return }
     
  for event in pendingEvents {
    var eventName: String?
    var properties: [AnyHashable: Any] = [:]
    for (key, value) in event {
      if key == PushNotificationKey.eventName.rawValue {
        if let eventNameValue = value as? String {
          eventName = eventNameValue
        } else {
          print("Invalid type for event_name key")
        }
      } else {
        properties[key] = value
      }
    }
       
    if let eventName = eventName {
      logCustomEvent(eventName, withProperties: properties)
    }
  }
     
  remoteStorage.removeObject(forKey: .pendingCustomEvents)
}
```
{% endtab %}
{% tab Objective-C %}
```objc
- (void)logPendingEventsIfNecessary {
  RemoteStorage *remoteStorage = [[RemoteStorage alloc] initWithStorageType:StorageTypeSuite];
  NSArray *pendingEvents = [remoteStorage retrieveForKey:RemoteStorageKeyPendingCustomEvents];
   
  for (NSDictionary<NSString *, id> *event in pendingEvents) {
    NSString *eventName = nil;
    NSMutableDictionary *properties = [NSMutableDictionary dictionary];
     
    for(NSString* key in event) {
      if ([key isEqual: @"event_name"]) {
        if ([[event objectForKey:key] isKindOfClass:[NSString class]]) {
          eventName = [event objectForKey:key];
        } else {
          NSLog(@"Invalid type for event_name key");
        }
      } else {
        [properties setValue:[event objectForKey:key] forKey:key];
      }
    }
     
    if (eventName != nil) {
      [[Appboy sharednstance] logCustomEvent:eventName withProperties:properties];
    }
  }
   
  [remoteStorage removeObjectForKey:RemoteStorageKeyPendingCustomEvents];
}
```
{% endtab %}
{% endtabs %}

1. Loop through the array of pending events
2. Loop through each key-value pair in the pending event dictionary
3. Explicitly checking key for “Event Name” to set the value accordingly
4. Every other key-value will be added to the properties dictionary
5. Log individual custom event 
6. Remove all pending events from storage

#### Saving Custom Attributes

To save custom attributes you must create the analytics from scratch. This is done by creating a dictionary with metadata and saving the data through the use of a helper file.

__Saving Custom Attributes__<br>

{% tabs %}
{% tab Swift %}
``` swift 
func saveCustomAttribute() {
  let customAttributeDictionary: [String: Any] = ["YOUR-CUSTOM-ATTRIBUTE-KEY": "YOUR-CUSTOM-ATTRIBUTE-VALUE"]
  let remoteStorage = RemoteStorage(storageType: .suite)
     
  if var pendingAttributes = remoteStorage.retrieve(forKey: .pendingCustomAttributes) as? [[String: Any]] {
    pendingAttributes.append(contentsOf: [customAttributeDictionary])
    remoteStorage.store(pendingAttributes, forKey: .pendingCustomAttributes)
  } else {
    remoteStorage.store([customAttributeDictionary], forKey: .pendingCustomAttributes)
  }
}
```
{% endtab %}
{% tab Objective-C %}
``` objc
- (void)saveCustomAttribute {
  NSDictionary<NSString *, id> *customAttributeDictionary = @{ @"YOUR-CUSTOM-ATTRIBUTE-KEY": @"YOUR-CUSTOM-ATTRIBUTE-VALUE" };
   
  RemoteStorage *remoteStorage = [[RemoteStorage alloc] initWithStorageType:StorageTypeSuite];
  NSMutableArray *pendingAttributes = [[remoteStorage retrieveForKey:RemoteStorageKeyPendingCustomAttributes] mutableCopy];
   
  if (pendingAttributes) {
    [pendingAttributes addObject:customAttributeDictionary];
    [remoteStorage store:pendingAttributes forKey:RemoteStorageKeyPendingCustomAttributes];
  } else {
    [remoteStorage store:@[ customAttributeDictionary ] forKey:RemoteStorageKeyPendingCustomAttributes];
  }
}
```
{% endtab %}
{% endtabs %}

1. Initialize a dictionary with attribute metadata
2. Initialize userDefaults to retrieve and store the attribute data
3. If there is an existing array, append new data to the existing array and save
4. If there is not an existing array, save the new array to userDefaults

#### Sending Custom Attributes to Braze

After the SDK is initialized is the best time to log any saved analytics from a notification content extension. This can be done by looping through the pending attributes, setting the appropriate custom attribute in Braze, and then clearing the storage for the next time this function is needed.

{% tabs %}
{% tab Swift %}
``` swift 
func logPendingCustomAttributesIfNecessary() {
  let remoteStorage = RemoteStorage(storageType: .suite)
  guard let pendingAttributes = remoteStorage.retrieve(forKey: .pendingCustomAttributes) as? [[String: Any]] else { return }
     
  pendingAttributes.forEach { setCustomAttributesWith(keysAndValues: $0) }
     
  remoteStorage.removeObject(forKey: .pendingCustomAttributes)
}
   
func setCustomAttributesWith(keysAndValues: [String: Any]) {
  for (key, value) in keysAndValues {
    if let value = value as? [String] {
      setCustomAttributeArrayWithKey(key, andValue: value)
    } else {
      setCustomAttributeWithKey(key, andValue: value)
    }
  }
}
```
{% endtab %}
{% tab Objective-C %}
```objc
func logPendingCustomAttributesIfNecessary() {
  let remoteStorage = RemoteStorage(storageType: .suite)
  guard let pendingAttributes = remoteStorage.retrieve(forKey: .pendingCustomAttributes) as? [[String: Any]] else { return }
     
  pendingAttributes.forEach { setCustomAttributesWith(keysAndValues: $0) }
     
  remoteStorage.removeObject(forKey: .pendingCustomAttributes)
}
   
func setCustomAttributesWith(keysAndValues: [String: Any]) {
  for (key, value) in keysAndValues {
    if let value = value as? [String] {
      setCustomAttributeArrayWithKey(key, andValue: value)
    } else {
      setCustomAttributeWithKey(key, andValue: value)
    }
  }
}
```
{% endtab %}
{% endtabs %}

1. Loop through the array of pending attributes
2. Loop through each key-value pair in the pending attributes dictionary
3. Log individual custom attribute with corresponding key and value
4. Remove all pending attributes from storage

#### Saving User Attributes

When saving custom attributes, you can't save a custom object, the object must be converted to a UserAttribute data object and then initialize with a correct type. Next, store the necessary user attributes. Because we don't want to loop through everything, we take advantage of the enum to help identify where the data should be stored without looping through the data unnecessarily.

{% tabs %}
{% tab Swift %}
``` swift 
func saveUserAttribute() {
  guard let data = try? PropertyListEncoder().encode(UserAttribute.userAttributeType("USER-ATTRIBUTE-VALUE")) else { return }
         
  let remoteStorage = RemoteStorage(storageType: .suite)
     
  if var pendingAttributes = remoteStorage.retrieve(forKey: .pendingUserAttributes) as? [Data] {
    pendingAttributes.append(contentsOf: [data])
    remoteStorage.store(pendingAttributes, forKey: .pendingUserAttributes)
  } else {
    remoteStorage.store([data], forKey: .pendingUserAttributes)
  }
}
```
{% endtab %}
{% tab Objective-C %}
```objc
func saveUserAttribute() {
  guard let data = try? PropertyListEncoder().encode(UserAttribute.userAttributeType("USER-ATTRIBUTE-VALUE")) else { return }
         
  let remoteStorage = RemoteStorage(storageType: .suite)
     
  if var pendingAttributes = remoteStorage.retrieve(forKey: .pendingUserAttributes) as? [Data] {
    pendingAttributes.append(contentsOf: [data])
    remoteStorage.store(pendingAttributes, forKey: .pendingUserAttributes)
  } else {
    remoteStorage.store([data], forKey: .pendingUserAttributes)
  }
}
```
{% endtab %}
{% endtabs %}

1. Initialize an encoded UserAttribute object with the corresponding type (email)
2. Initialize userDefaults to retrieve and store the event data
3. If there is an existing array, append new data to the existing array and save
4. If there is not an existing array, save the new array to userDefaults

{% details UserAttribute Helper File %}
{% tabs %}
{% tab Swift %}
```swift
enum UserAttribute: Hashable {
  case email(String?)
}
 
// MARK: - Codable
extension UserAttribute: Codable {
  private enum CodingKeys: String, CodingKey {
    case email
  }
   
  func encode(to encoder: Encoder) throws {
    var values = encoder.container(keyedBy: CodingKeys.self)
     
    switch self {
    case .email(let email):
      try values.encode(email, forKey: .email)
    }
  }
   
  init(from decoder: Decoder) throws {
    let values = try decoder.container(keyedBy: CodingKeys.self)
     
    let email = try values.decode(String.self, forKey: .email)
    self = .email(email)
  }
}
```
{% endtab %}
{% tab Objective-C %}
```objc
@implementation UserAttribute
 
- (id)initWithUserField:(NSString *)userField attributeType:(UserAttributeType)attributeType {
  if (self = [super init]) {
    self.userField = userField;
    self.attributeType = attributeType;
  }
  return self;
}
 
- (void)encodeWithCoder:(NSCoder *)encoder {
  [encoder encodeObject:self.userField forKey:@"userField"];
  [encoder encodeInteger:self.attributeType forKey:@"attributeType"];
}
 
- (id)initWithCoder:(NSCoder *)decoder {
  if (self = [super init]) {
    self.userField = [decoder decodeObjectForKey:@"userField"];
     
    NSInteger attributeRawValue = [decoder decodeIntegerForKey:@"attributeType"];
    self.attributeType = (UserAttributeType) attributeRawValue;
  }
  return self;
}
 
@end
```
{% endtab %}
{% endtabs %}

{% enddetails %}

#### Sending User Attributes to Braze

After the SDK is initialized is the best time to log any saved analytics from a notification content extension. This can be done by looping through the pending attributes, setting the appropriate custom attribute in Braze, and then clearing the storage for the next time this function is needed.

{% tabs %}
{% tab Swift %}
``` swift 
func logPendingUserAttributesIfNecessary() {
  let remoteStorage = RemoteStorage(storageType: .suite)
  guard let pendingAttributes = remoteStorage.retrieve(forKey: .pendingUserAttributes) as? [Data] else { return }
     
  for attributeData in pendingAttributes {
    guard let userAttribute = try? PropertyListDecoder().decode(UserAttribute.self, from: attributeData) else { continue }
       
    switch userAttribute {
    case .email(let email):
      user?.email = email
    }
  }
     
  remoteStorage.removeObject(forKey: .pendingUserAttributes)
}
```
{% endtab %}
{% tab Objective-C %}
```objc
func logPendingUserAttributesIfNecessary() {
  let remoteStorage = RemoteStorage(storageType: .suite)
  guard let pendingAttributes = remoteStorage.retrieve(forKey: .pendingUserAttributes) as? [Data] else { return }
     
  for attributeData in pendingAttributes {
    guard let userAttribute = try? PropertyListDecoder().decode(UserAttribute.self, from: attributeData) else { continue }
       
    switch userAttribute {
    case .email(let email):
      user?.email = email
    }
  }
     
  remoteStorage.removeObject(forKey: .pendingUserAttributes)
}
```
{% endtab %}
{% endtabs %}

1. Loop through the array of pending attribute data
2. Initialize an encoded UserAttribute object from attribute data
3. Set specific user field based on the User Attribute type (email)
4. Remove all pending user attributes from storage

[1]: {% image_buster /assets/img/push_implementation_guide/push1.png %}
