---
nav_title: Implementation Guide
platform: iOS
page_order: 7
description: ""
---

# Push Notification Implementation Guide

> This implementation guide covers the background needed on fundamental Push concepts, three use cases built by our team, accompanying code snippets, and guidance on logging analytics. Visit our Braze Demo Repository [here](https://github.com/braze-inc/braze-growth-shares-ios-demo-app)! Please note that this implementation guide is centered around a Swift implementation, but Objective-C snippets are provided for those interested.

## Notification Content Extensions

Push notifications while seemingly standard across different platforms, offer the immense capacity for customization past what is normally implemented in the default UI. When a push notification (abbreviated banner view) is 3D pressed or viewed using the banner options, content notification extensions enable a custom view of the expanded push notitfication. The customization options this extended view offer are quite expansive, offering similiar functionality to that you'd find in an in-app message. 

While implementing push in this way may be unfamiliar to some, one of our well-known features at Braze, [Push Stories]({{site.baseurl}}/user_guide/message_building_by_channel/push/advanced_push_options/push_stories/), are a prime example of what a custom view for notifcation content extension can look like!

## Use Case and Implementation Walkthrough

There are three push notifications content extension types provided. Each type has has a concept walkthrough, potential use cases, and a look into how Push notification variables may look and be used in the Braze dashboard:
- [Interactive Push Notification](#interactive-push-notification)
- [Personalized Push Notifications](#personalized-push-notifications)
- [Information Capture Push Notifications](#information-capture-push-notification)

### Interactive Push Notification

Push notifications can respond to user actions inside a content extension. As of iOS 12, content extensions now have the option of being interactive. 

Push notifications can be opened via 3D press or explicitly slecting "View." 3D press can be diasbled in the device settings.

#### Dashboard Configuration

Custom category is used to determine which view to be displaying in the content extension. Configured on the compose tab by toggling Notication Buttons. 

#### Other Use Cases

Gamification - GAP created this campaign with a custom HTML in-app message. This could be replicated in a push notification

### Personalized Push Notifications

Push notifications can display user-specific information incide a content extension. 

#### Dashboard Configuration

#### Handling Key-Value Pairs
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

### Information Capture Push Notification

Push notifications can capture user information incide a content extension.

#### Dashboard Configuration

#### Handling Buttom Actions

__Handling Push Notification Action Button Responses__<br>
Push notication action buttons are uniquely identified to handle responses from buttom presses accordingly.

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


Push notifcations can be automatically dismissed from an action button press.

#### Other Use Cases

User Input. Other ideas, SMS Capture, Complete Profile, Submit Feedback

## Logging vs. Analytics

Loggin analytics can only be done in real-time with the help of the customer;s server hitting Braze's API user/track endpoint. 

Requires userId parameter, which cannot be queried from Braze SDK.

### Saving Custom Event
__Saving Custom Events__<br>

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

1. Initialize a dictionary with event meta data
2. Initialize userDefaults to retrieve and store the event data
3. If there is an existing array, append new data to existing array and save
4. If there is not an existing array, save new array to userDefaults

### Sending Custom Events to Braze

After the SDK is initialized is the best time to log any saved analytics from a notification content extension

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

1. Loop through array of pending events
2. Loop through each key-value pair in pending event dictionary
3. Explicitly checking key for “Event Name” to set the value accordingly
4. Every other key-value will be added to the properties dictionary
5. Log individual custom event 
6. Remove all pending events from storage

### Saving Custom Attributes

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

1. Initialize a dictionary with attribute meta data
2. Initialize userDefaults to retrieve and store the attribute data
3. If there is an existing array, append new data to existing array and save
4. If there is not an existing array, save new array to userDefaults

### Sending Custom Attributes to Braze

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

1. Loop through array of pending attributes
2. Loop through each key-value pair in pending attributes dictionary
3. Log individual custom attribute with corresponding key and value
4. Remove all pending attributes from storage

### Saving User Attributes

Custom object that saves user attributes tied to a specific field  (firstName, lastName, email, phoneNumber, etc.)

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

1. Initialize an encoded UserAttribute object with corresponding type (email)
2. Initialize userDefaults to retrieve and store the event data
3. If there is an existing array, append new data to existing array and save
4. If there is not an existing array, save new array to userDefaults

### Sending User Attributes to Braze

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

1. Loop through array of pending attribute data
2. Initialize an encoded UserAttribute object from attribute data
3. Set specific user field based on the User Attribute type (email)
4. Remove all pending user attributes from storage
