---
nav_title: Push analytics and custom event logging
article_title: Push analytics and custom event logging
page_order: 7.2
description: "Learn what push analytics Braze logs automatically, how to preserve native tracking with custom push handling, and how to log custom events or attributes from push payload data."
noindex: true
---

# Push analytics and custom event logging

> This page covers two distinct workflows: native push analytics (opens, influenced opens, and campaign reporting) and custom data logging (custom events and attributes) from push payloads. Use this guide to identify which workflow applies to your use case and follow the steps for your platform.

## Prerequisites

Before you start, complete the initial push notification integration for your platform:

- [Android push notifications]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android)
- [Swift push notifications]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift)
- [Web push notifications]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web)

## Native push analytics vs. custom event logging

These are two separate analytics workflows with different reporting surfaces.

| Analytics category | Description | Where it appears |
| --- | --- | --- |
| Native push analytics | Push metrics such as opens and influenced opens, tied to Braze push campaigns | Push campaign analytics, Currents message engagement events, Report Builder |
| Custom events and attributes | Analytics you define and log through SDK methods or the `/users/track` endpoint | User profiles, segmentation, action-based campaigns and Canvases, custom event analytics |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert important %}
Logging a custom event (such as `push_notification_opened`) is not the same as native Braze push open tracking. Custom events don't populate native push campaign open metrics or push attribution.
{% endalert %}

## What Braze logs automatically

When your SDK integration is configured, Braze automatically logs core channel interaction data, including push opens and influenced opens. No additional code is required for standard push analytics. For a full list of automatically collected data, see [SDK data collection]({{site.baseurl}}/user_guide/data/unification/user_data/sdk_data_collection/).

For more details, see the following:

- [SDK data collection]({{site.baseurl}}/user_guide/data/unification/user_data/sdk_data_collection/) for a full list of automatically collected and optional data.
- [Influenced opens]({{site.baseurl}}/user_guide/analytics/tracking/influenced_opens/) for how Braze calculates influenced opens.
- [Message engagement events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/) for downstream event schemas in Currents.

## Preserving native push analytics with custom push handling

You might use a custom push handler when you need to integrate multiple push providers, process additional payload data, or implement custom notification display logic. If you use a custom push handler, you must still pass push payloads to Braze SDK methods. This allows Braze to extract the embedded tracking data and log native push analytics (opens, influenced opens, and delivery metrics).

{% tabs %}
{% tab Android %}

If you have a custom `FirebaseMessagingService`, call `BrazeFirebaseMessagingService.handleBrazeRemoteMessage(...)` inside your `onMessageReceived` method. Keep in mind that your `FirebaseMessagingService` subclass must finish execution within 9 seconds of invocation to avoid being [flagged or terminated](https://firebase.google.com/docs/cloud-messaging/android/receive) by the Android system.

```java
public class MyFirebaseMessagingService extends FirebaseMessagingService {
  @Override
  public void onMessageReceived(RemoteMessage remoteMessage) {
    super.onMessageReceived(remoteMessage);
    if (BrazeFirebaseMessagingService.handleBrazeRemoteMessage(this, remoteMessage)) {
      // Braze processed a Braze push payload.
    } else {
      // Non-Braze payload: pass to your other handlers.
    }
  }
}
```

For a full implementation example, see the [Braze Android SDK Firebase push sample app](https://github.com/braze-inc/braze-android-sdk/tree/master/samples/firebase-push).

{% endtab %}
{% tab Swift %}

In a manual push integration, forward background and user notification callbacks to Braze.

**Background notifications:**

```swift
if let braze = AppDelegate.braze, braze.notifications.handleBackgroundNotification(
  userInfo: userInfo,
  fetchCompletionHandler: completionHandler
) {
  return
}
completionHandler(.noData)
```

**User notification responses:**

```swift
if let braze = AppDelegate.braze, braze.notifications.handleUserNotification(
  response: response,
  withCompletionHandler: completionHandler
) {
  return
}
completionHandler()
```

**Foreground notifications:**

```swift
func userNotificationCenter(
  _ center: UNUserNotificationCenter,
  willPresent notification: UNNotification,
  withCompletionHandler completionHandler: @escaping (UNNotificationPresentationOptions) -> Void
) {
  if let braze = AppDelegate.braze {
    braze.notifications.handleForegroundNotification(notification: notification)
  }
  if #available(iOS 14.0, *) {
    completionHandler([.banner, .list, .sound])
  } else {
    completionHandler([.alert, .sound])
  }
}
```

For a full implementation example, see the [Braze Swift SDK manual push sample (`AppDelegate.swift`)](https://github.com/braze-inc/braze-swift-sdk/blob/main/Examples/Swift/Sources/PushNotifications-Manual/AppDelegate.swift).

{% endtab %}
{% tab Web %}

For web push, configure your service worker and SDK initialization as described in [Web push notifications]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web).

For more code samples, see the [Braze Web SDK repository](https://github.com/braze-inc/braze-web-sdk).

{% endtab %}
{% endtabs %}

## Logging custom data from push payloads

Use this section when you need to log additional data from push payload key-value pairs, such as custom events or attributes tied to your business logic.

For more information about custom events, see [Custom events]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_events/). To log custom events through SDK methods, see [Logging custom events]({{site.baseurl}}/developer_guide/analytics/logging_events/).

### Option A: Log with the `/users/track` endpoint

You can log analytics in real time by calling the [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) endpoint.

To identify the user profile, include `braze_id` in your push payload key-value pairs.

{% alert note %}
Passing `braze_id` only identifies the profile. You still need implementation logic that reads payload values and sends the `/users/track` request with the events or attributes you want to log.
{% endalert %}

### Option B: Log with SDK methods after app launch

You can also save payload data locally and log custom events and attributes through SDK methods after the app initializes. This approach is common in notification content extension flows where analytics data is persisted first and flushed on the next app launch.

{% alert important %}
Analytics aren't sent to Braze until the app launches. Depending on your dismissal settings, there can be a delay between when the user dismisses the notification and when the app opens and flushes analytics.
{% endalert %}

## Logging from a notification content extension (Swift)

The following steps cover how to save and send custom events, custom attributes, and user attributes from a Swift notification content extension.

### Step 1: Configure app groups in Xcode

In Xcode, add the `App Groups` capability to your main app target. Turn on **App Groups**, then click **+** to add a new group. Use your app's bundle ID to create the group identifier (for example, `group.com.company.appname.xyz`). Turn on **App Groups** for both your main app target and the content extension target.

![Xcode showing App Groups capability enabled for main app and notification extension]({% image_buster /assets/img/swift/push_story/add_app_groups.png %})

### Step 2: Choose what to log

Before you implement the snippets, choose which analytics category you want to log:

- **Custom events:** Actions users take (for example, completing a flow or tapping a specific UI element). Use custom events for action-based triggers, segmentation, and event analytics. For more information, see [Custom events]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_events/) and [Logging custom events]({{site.baseurl}}/developer_guide/analytics/logging_events/).
- **Custom attributes:** Profile fields you define (for example, `plan_tier` or `preferred_language`) and update over time. For more information, see [Custom attributes]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/) and [Setting user attributes]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/).
- **User attributes:** Standard profile fields (for example, email, first name, and phone number). In the sample code, these are represented by a typed `UserAttribute` model and then mapped to Braze user fields.

The helper files in this section (`RemoteStorage`, `UserAttribute`, and `EventName Dictionary`) are local utility files used by this sample implementation. They are not built-in SDK classes. They store payload-derived data in `UserDefaults`, define a typed model for pending user updates, and standardize event payload construction. For more information about local data storage behavior, see [Storage]({{site.baseurl}}/developer_guide/storage/?tab=swift).

{% alert note %}
The helper file examples in this section are iOS-specific (Swift and Objective-C). For Android and Web approaches to logging custom events and attributes, see [Logging custom events]({{site.baseurl}}/developer_guide/analytics/logging_events/) ([Android]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=android), [Web]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=web)) and [Setting user attributes]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/) ([Android]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?tab=android), [Web]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?tab=web)).
{% endalert %}

{% tabs local %}
{% tab Custom events %}

#### Saving custom events

Create the analytics payload by building a dictionary, populating metadata, and saving it with the helper file.

1. Initialize a dictionary with event metadata.
2. Initialize `userDefaults` to retrieve and store event data.
3. If an existing array is found, append and save.
4. If no array exists, save a new array.

{% subtabs global %}
{% subtab Swift %}
```swift
func saveCustomEvent(with properties: [String: Any]? = nil) {
  // 1
  let customEventDictionary = Dictionary(eventName: "YOUR-EVENT-NAME", properties: properties)
  
  // 2
  let remoteStorage = RemoteStorage(storageType: .suite)
  
  // 3
  if var pendingEvents = remoteStorage.retrieve(forKey: .pendingCustomEvents) as? [[String: Any]] {
    pendingEvents.append(contentsOf: [customEventDictionary])
    remoteStorage.store(pendingEvents, forKey: .pendingCustomEvents)
  } else {
    // 4
    remoteStorage.store([customEventDictionary], forKey: .pendingCustomEvents)
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)saveCustomEvent:(NSDictionary<NSString *, id> *)properties {
  // 1
  NSDictionary<NSString *, id> *customEventDictionary = [[NSDictionary alloc] initWithEventName:@"YOUR-EVENT-NAME" properties:properties];
  
  // 2
  RemoteStorage *remoteStorage = [[RemoteStorage alloc] initWithStorageType:StorageTypeSuite];
  NSMutableArray *pendingEvents = [[remoteStorage retrieveForKey:RemoteStorageKeyPendingCustomEvents] mutableCopy];
  
  // 3
  if (pendingEvents) {
    [pendingEvents addObject:customEventDictionary];
    [remoteStorage store:pendingEvents forKey:RemoteStorageKeyPendingCustomEvents];
  } else {
    // 4
    [remoteStorage store:@[ customEventDictionary ] forKey:RemoteStorageKeyPendingCustomEvents];
  }
}
```
{% endsubtab %}
{% endsubtabs %}

#### Sending custom events to Braze

Log saved analytics right after SDK initialization.

1. Loop through pending events.
2. Loop through key-value pairs in each event.
3. Check for the `event_name` key.
4. Add remaining key-value pairs to the `properties` dictionary.
5. Log each custom event.
6. Remove pending events from storage.

{% subtabs global %}
{% subtab Swift %}
```swift
func logPendingCustomEventsIfNecessary() {
  let remoteStorage = RemoteStorage(storageType: .suite)
  guard let pendingEvents = remoteStorage.retrieve(forKey: .pendingCustomEvents) as? [[String: Any]] else { return }
  
  // 1
  for event in pendingEvents {
    var eventName: String?
    var properties: [AnyHashable: Any] = [:]
    
    // 2
    for (key, value) in event {
      if key == "event_name" {
        // 3
        if let eventNameValue = value as? String {
          eventName = eventNameValue
        } else {
          print("Invalid type for event_name key")
        }
      } else {
        // 4
        properties[key] = value
      }
    }
    // 5
    if let eventName = eventName {
      AppDelegate.braze?.logCustomEvent(name: eventName, properties: properties)
    }
  }
  
  // 6
  remoteStorage.removeObject(forKey: .pendingCustomEvents)
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)logPendingEventsIfNecessary {
  RemoteStorage *remoteStorage = [[RemoteStorage alloc] initWithStorageType:StorageTypeSuite];
  NSArray *pendingEvents = [remoteStorage retrieveForKey:RemoteStorageKeyPendingCustomEvents];
  
  // 1
  for (NSDictionary<NSString *, id> *event in pendingEvents) {
    NSString *eventName = nil;
    NSMutableDictionary *properties = [NSMutableDictionary dictionary];
    
    // 2
    for (NSString* key in event) {
      if ([key isEqualToString:@"event_name"]) {
        // 3
        if ([[event objectForKey:key] isKindOfClass:[NSString class]]) {
          eventName = [event objectForKey:key];
        } else {
          NSLog(@"Invalid type for event_name key");
        }
      } else {
        // 4
        properties[key] = event[key];
      }
    }
    // 5
    if (eventName != nil) {
      [AppDelegate.braze logCustomEvent:eventName properties:properties];
    }
  }
  
  // 6
  [remoteStorage removeObjectForKey:RemoteStorageKeyPendingCustomEvents];
}
```
{% endsubtab %}
{% endsubtabs %}

{% endtab %}
{% tab Custom attributes %}

#### Saving custom attributes

Create the analytics dictionary from scratch, then persist it.

1. Initialize a dictionary with attribute metadata.
2. Initialize `userDefaults` to retrieve and store attribute data.
3. If an existing array is found, append and save.
4. If no array exists, save a new array.

{% subtabs global %}
{% subtab Swift %}
```swift
func saveCustomAttribute() {
  // 1
  let customAttributeDictionary: [String: Any] = ["YOUR-CUSTOM-ATTRIBUTE-KEY": "YOUR-CUSTOM-ATTRIBUTE-VALUE"]
  
  // 2
  let remoteStorage = RemoteStorage(storageType: .suite)
  
  // 3
  if var pendingAttributes = remoteStorage.retrieve(forKey: .pendingCustomAttributes) as? [[String: Any]] {
    pendingAttributes.append(contentsOf: [customAttributeDictionary])
    remoteStorage.store(pendingAttributes, forKey: .pendingCustomAttributes)
  } else {
    // 4
    remoteStorage.store([customAttributeDictionary], forKey: .pendingCustomAttributes)
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)saveCustomAttribute {
  // 1
  NSDictionary<NSString *, id> *customAttributeDictionary = @{ @"YOUR-CUSTOM-ATTRIBUTE-KEY": @"YOUR-CUSTOM-ATTRIBUTE-VALUE" };
  
  // 2
  RemoteStorage *remoteStorage = [[RemoteStorage alloc] initWithStorageType:StorageTypeSuite];
  NSMutableArray *pendingAttributes = [[remoteStorage retrieveForKey:RemoteStorageKeyPendingCustomAttributes] mutableCopy];
  
  // 3
  if (pendingAttributes) {
    [pendingAttributes addObject:customAttributeDictionary];
    [remoteStorage store:pendingAttributes forKey:RemoteStorageKeyPendingCustomAttributes];
  } else {
    // 4
    [remoteStorage store:@[ customAttributeDictionary ] forKey:RemoteStorageKeyPendingCustomAttributes];
  }
}
```
{% endsubtab %}
{% endsubtabs %}

#### Sending custom attributes to Braze

Log saved analytics right after SDK initialization.

1. Loop through pending attributes.
2. Loop through each key-value pair.
3. Log each custom attribute key and value.
4. Remove pending attributes from storage.

{% subtabs global %}
{% subtab Swift %}
```swift
func logPendingCustomAttributesIfNecessary() {
  let remoteStorage = RemoteStorage(storageType: .suite)
  guard let pendingAttributes = remoteStorage.retrieve(forKey: .pendingCustomAttributes) as? [[String: Any]] else { return }
     
  // 1
  pendingAttributes.forEach { setCustomAttributesWith(keysAndValues: $0) }
  
  // 4
  remoteStorage.removeObject(forKey: .pendingCustomAttributes)
}
   
func setCustomAttributesWith(keysAndValues: [String: Any]) {
  // 2
  for (key, value) in keysAndValues {
    // 3
    if let value = value as? [String] {
      setCustomAttributeArrayWithKey(key, andValue: value)
    } else {
      setCustomAttributeWithKey(key, andValue: value)
    }
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)logPendingCustomAttributesIfNecessary {
  RemoteStorage *remoteStorage = [[RemoteStorage alloc] initWithStorageType:StorageTypeSuite];
  NSArray *pendingAttributes = [remoteStorage retrieveForKey:RemoteStorageKeyPendingCustomAttributes];
   
  // 1
  for (NSDictionary<NSString*, id> *attribute in pendingAttributes) {
    [self setCustomAttributeWith:attribute];
  }
  
  // 4
  [remoteStorage removeObjectForKey:RemoteStorageKeyPendingCustomAttributes];
}
 
- (void)setCustomAttributeWith:(NSDictionary<NSString *, id> *)keysAndValues {
  // 2
  for (NSString *key in keysAndValues) {
    // 3
    [self setCustomAttributeWith:key andValue:[keysAndValues objectForKey:key]];
  }
}
```
{% endsubtab %}
{% endsubtabs %}

{% endtab %}
{% tab User attributes %}

#### Saving user attributes

When saving user attributes, create a custom object to capture which user field is being updated (`email`, `first_name`, `phone_number`, and so on). The object should be compatible with storing and retrieving via `UserDefaults`. See the `UserAttribute` helper file in the **Helper files** tab for one example.

1. Initialize an encoded `UserAttribute` object with the corresponding type.
2. Initialize `userDefaults` to retrieve and store the data.
3. If an existing array is found, append and save.
4. If no array exists, save a new array.

{% subtabs global %}
{% subtab Swift %}
```swift
func saveUserAttribute() {
  // 1
  guard let data = try? PropertyListEncoder().encode(UserAttribute.email("USER-ATTRIBUTE-VALUE")) else { return }
  
  // 2
  let remoteStorage = RemoteStorage(storageType: .suite)
  
  // 3
  if var pendingAttributes = remoteStorage.retrieve(forKey: .pendingUserAttributes) as? [Data] {
    pendingAttributes.append(contentsOf: [data])
    remoteStorage.store(pendingAttributes, forKey: .pendingUserAttributes)
  } else {
    // 4
    remoteStorage.store([data], forKey: .pendingUserAttributes)
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)saveUserAttribute {
  // 1
  UserAttribute *userAttribute = [[UserAttribute alloc] initWithUserField:@"USER-ATTRIBUTE-VALUE" attributeType:UserAttributeTypeEmail];
   
  NSError *error;
  NSData *data = [NSKeyedArchiver archivedDataWithRootObject:userAttribute requiringSecureCoding:YES error:&error];
  
  if (error != nil) {
    // log error
  }
  // 2
  RemoteStorage *remoteStorage = [[RemoteStorage alloc] initWithStorageType:StorageTypeSuite];
  NSMutableArray *pendingAttributes = [[remoteStorage retrieveForKey:RemoteStorageKeyPendingUserAttributes] mutableCopy];
  
  // 3
  if (pendingAttributes) {
    [pendingAttributes addObject:data];
    [remoteStorage store:pendingAttributes forKey:RemoteStorageKeyPendingUserAttributes];
  } else {
    // 4
    [remoteStorage store:@[data] forKey:RemoteStorageKeyPendingUserAttributes];
  }
}
```
{% endsubtab %}
{% endsubtabs %}

#### Sending user attributes to Braze

Log saved analytics right after SDK initialization.

1. Loop through `pendingAttributes` data.
2. Decode each `UserAttribute`.
3. Set user fields based on attribute type.
4. Remove pending user attributes from storage.

{% subtabs global %}
{% subtab Swift %}
```swift
func logPendingUserAttributesIfNecessary() {
  let remoteStorage = RemoteStorage(storageType: .suite)
  guard let pendingAttributes = remoteStorage.retrieve(forKey: .pendingUserAttributes) as? [Data] else { return }
  
  // 1
  for attributeData in pendingAttributes {
    // 2
    guard let userAttribute = try? PropertyListDecoder().decode(UserAttribute.self, from: attributeData) else { continue }
    
    // 3
    switch userAttribute {
    case .email(let email):
      AppDelegate.braze?.user.set(email: email)
    }
  }
  // 4
  remoteStorage.removeObject(forKey: .pendingUserAttributes)
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)logPendingUserAttributesIfNecessary {
  RemoteStorage *remoteStorage = [[RemoteStorage alloc] initWithStorageType:StorageTypeSuite];
  NSArray *pendingAttributes = [remoteStorage retrieveForKey:RemoteStorageKeyPendingUserAttributes];
  
  // 1
  for (NSData *attributeData in pendingAttributes) {
    NSError *error;
    
    // 2
    UserAttribute *userAttribute = [NSKeyedUnarchiver unarchivedObjectOfClass:[UserAttribute class] fromData:attributeData error:&error];
    
    if (error != nil) {
      // log error
    }
    
    // 3
    if (userAttribute) {
      switch (userAttribute.attributeType) {
        case UserAttributeTypeEmail:
          [self user].email = userAttribute.userField;
          break;
      }
    }
  }
  // 4
  [remoteStorage removeObjectForKey:RemoteStorageKeyPendingUserAttributes];
}
```
{% endsubtab %}
{% endsubtabs %}

{% endtab %}
{% tab Helper files %}

#### RemoteStorage helper file

{% subtabs global %}
{% subtab Swift %}
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
      // Use the App Group identifier you created in Step 1.
      return UserDefaults(suiteName: "group.com.company.appname.xyz")!
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
{% endsubtab %}
{% subtab Objective-C %}
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
  if (!_defaults) {
    switch (self.storageType) {
      case StorageTypeStandard:
        _defaults = [NSUserDefaults standardUserDefaults];
        break;
      case StorageTypeSuite:
        _defaults = [[NSUserDefaults alloc] initWithSuiteName:@"group.com.company.appname.xyz"];
        break;
    }
  }
  return _defaults;
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
{% endsubtab %}
{% endsubtabs %}

#### UserAttribute helper file

{% subtabs global %}
{% subtab Swift %}
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
      try values.encodeIfPresent(email, forKey: .email)
    }
  }
   
  init(from decoder: Decoder) throws {
    let values = try decoder.container(keyedBy: CodingKeys.self)
     
    let email = try values.decodeIfPresent(String.self, forKey: .email)
    self = .email(email)
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
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
{% endsubtab %}
{% endsubtabs %}

#### EventName dictionary helper file

{% subtabs global %}
{% subtab Swift %}
```swift
extension Dictionary where Key == String, Value == Any {
  init(eventName: String, properties: [String: Any]? = nil) {
    self.init()
    self[PushNotificationKey.eventName.rawValue] = eventName
     
    if let properties = properties {
      for (key, value) in properties {
        self[key] = value
      }
    }
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
@implementation NSMutableDictionary (Helper)

+ (instancetype)dictionaryWithEventName:(NSString *)eventName
                              properties:(NSDictionary *)properties {
  NSMutableDictionary *dict = [NSMutableDictionary dictionary];
  dict[@"event_name"] = eventName;

  if (properties) {
    for (id key in properties) {
      dict[key] = properties[key];
    }
  }

  return dict;
}
 
@end
```
{% endsubtab %}
{% endsubtabs %}

{% endtab %}
{% endtabs %}

## Analyzing results

Use the reporting surface that matches the analytics category:

| Analytics category | Where to view in Braze |
| --- | --- |
| Native push analytics | To view campaign-level push open metrics, navigate to your push campaign's **Campaign Analytics** page. For metric definitions, see [Influenced opens]({{site.baseurl}}/user_guide/analytics/tracking/influenced_opens/). To build custom analytics views, navigate to **Analytics** > **Report Builder (New)**. For navigation steps, see [Report Builder]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/). For warehouse-level event schemas, see [Message engagement events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/). |
| Custom events and attributes | To view custom event trends, navigate to **Analytics** > **Custom Events Report**. For details, see [Custom events]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_events/). To inspect user-level values, navigate to the **Search Users** page and open a profile. For steps, see [User profiles]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/). To filter audiences by these values, navigate to **Audience** > **Segments**. For navigation steps, see [Create a segment]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/) and filter options in [Segmentation filters]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

For custom report creation, see [Report Builder]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/).

## Related references

- [Push notifications]({{site.baseurl}}/developer_guide/push_notifications/)
- [Logging custom events]({{site.baseurl}}/developer_guide/analytics/logging_events/)
- [Custom events]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_events/)
- [Track users endpoint (`/users/track`)]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)
- [Braze Android SDK repository](https://github.com/braze-inc/braze-android-sdk)
- [Braze Swift SDK repository](https://github.com/braze-inc/braze-swift-sdk)
- [Braze Web SDK repository](https://github.com/braze-inc/braze-web-sdk)
