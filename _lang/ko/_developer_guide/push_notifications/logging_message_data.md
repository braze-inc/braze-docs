---
nav_title: 푸시 분석 및 커스텀 이벤트 로깅
article_title: 푸시 분석 및 커스텀 이벤트 로깅
page_order: 7.2
description: "Braze가 자동으로 기록하는 푸시 분석, 커스텀 푸시 처리 시 네이티브 추적을 유지하는 방법, 푸시 페이로드 데이터에서 커스텀 이벤트 또는 속성을 기록하는 방법을 알아보세요."
noindex: true
---

# 푸시 분석 및 커스텀 이벤트 로깅

> 이 페이지에서는 네이티브 푸시 분석(열기, 영향받은 열기, 캠페인 보고서)과 푸시 페이로드에서의 커스텀 데이터 로깅(커스텀 이벤트 및 속성) 워크플로를 다룹니다. 이 가이드를 통해 사용 사례에 해당하는 워크플로를 확인하고 플랫폼에 맞는 단계를 따르세요.

## 필수 조건

시작하기 전에 플랫폼에 대한 초기 푸시 알림 통합을 완료하세요:

- [Android 푸시 알림]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android)
- [Swift 푸시 알림]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift)
- [웹 푸시 알림]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web)

## 네이티브 푸시 분석 vs. 커스텀 이벤트 로깅

다음 워크플로는 각각 다른 보고 화면을 사용합니다.

| 분석 카테고리 | 설명 | 표시 위치 |
| --- | --- | --- |
| 네이티브 푸시 분석 | Braze 푸시 캠페인에 연결된 열기 및 영향받은 열기와 같은 푸시 측정기준 | 푸시 캠페인 분석, 커런츠 메시지 참여 이벤트, 보고서 빌더 |
| 커스텀 이벤트 및 속성 | SDK 메서드 또는 `/users/track` 엔드포인트를 통해 정의하고 기록하는 분석 | 고객 프로필, 세분화, 동작 기반 캠페인 및 캔버스, 커스텀 이벤트 분석 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert important %}
커스텀 이벤트(예: `push_notification_opened`)를 기록하는 것은 Braze의 네이티브 푸시 열기 추적과 동일하지 않습니다. 커스텀 이벤트는 네이티브 푸시 캠페인 열기 측정기준이나 푸시 기여도에 반영되지 않습니다.
{% endalert %}

## Braze가 자동으로 기록하는 항목

SDK 통합이 구성되면 Braze는 푸시 열기 및 영향받은 열기를 포함한 핵심 채널 상호작용 데이터를 자동으로 기록합니다. 표준 푸시 분석에는 추가 코드가 필요하지 않습니다. 자동으로 수집되는 데이터의 전체 목록은 [SDK 데이터 수집]({{site.baseurl}}/user_guide/data/unification/user_data/sdk_data_collection/)을 참조하세요.

자세한 내용은 다음을 참조하세요:

- [SDK 데이터 수집]({{site.baseurl}}/user_guide/data/unification/user_data/sdk_data_collection/) - 자동으로 수집되는 데이터와 선택적 데이터의 전체 목록.
- [영향받은 열기]({{site.baseurl}}/user_guide/analytics/tracking/influenced_opens/) - Braze가 영향받은 열기를 계산하는 방법.
- [메시지 참여 이벤트]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/) - 커런츠의 다운스트림 이벤트 스키마.

## 커스텀 푸시 처리 시 네이티브 푸시 분석 유지

여러 푸시 공급자를 통합하거나, 추가 페이로드 데이터를 처리하거나, 커스텀 알림 표시 로직을 구현해야 할 때 커스텀 푸시 핸들러를 사용할 수 있습니다. 커스텀 푸시 핸들러를 사용하는 경우에도 푸시 페이로드를 Braze SDK 메서드에 전달해야 합니다. 이를 통해 Braze가 내장된 추적 데이터를 추출하고 네이티브 푸시 분석(열기, 영향받은 열기, 전달 측정기준)을 기록할 수 있습니다.

{% tabs %}
{% tab Android %}

커스텀 `FirebaseMessagingService`가 있는 경우, `onMessageReceived` 메서드 내에서 `BrazeFirebaseMessagingService.handleBrazeRemoteMessage(...)`를 호출하세요. `FirebaseMessagingService` 서브클래스는 Android 시스템에 의해 [플래그 지정되거나 종료](https://firebase.google.com/docs/cloud-messaging/android/receive)되지 않도록 호출 후 9초 이내에 실행을 완료해야 합니다.

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

전체 구현 예제는 [Braze Android SDK Firebase 푸시 샘플 앱](https://github.com/braze-inc/braze-android-sdk/tree/master/samples/firebase-push)을 참조하세요.

{% endtab %}
{% tab Swift %}

수동 푸시 통합에서는 백그라운드 및 사용자 알림 콜백을 Braze에 전달합니다.

**백그라운드 알림:**

```swift
if let braze = AppDelegate.braze, braze.notifications.handleBackgroundNotification(
  userInfo: userInfo,
  fetchCompletionHandler: completionHandler
) {
  return
}
completionHandler(.noData)
```

**사용자 알림 응답:**

```swift
if let braze = AppDelegate.braze, braze.notifications.handleUserNotification(
  response: response,
  withCompletionHandler: completionHandler
) {
  return
}
completionHandler()
```

**포그라운드 알림:**

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

전체 구현 예제는 [Braze Swift SDK 수동 푸시 샘플(`AppDelegate.swift`)](https://github.com/braze-inc/braze-swift-sdk/blob/main/Examples/Swift/Sources/PushNotifications-Manual/AppDelegate.swift)을 참조하세요.

{% endtab %}
{% tab Web %}

웹 푸시의 경우, [웹 푸시 알림]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web)에 설명된 대로 서비스 워커와 SDK 초기화를 구성하세요.

더 많은 코드 샘플은 [Braze Web SDK 리포지토리](https://github.com/braze-inc/braze-web-sdk)를 참조하세요.

{% endtab %}
{% endtabs %}

## 푸시 페이로드에서 커스텀 데이터 로깅

비즈니스 로직에 연결된 커스텀 이벤트나 속성과 같이 푸시 페이로드 키-값 페어에서 추가 데이터를 기록해야 할 때 이 섹션을 사용하세요.

커스텀 이벤트에 대한 자세한 내용은 [커스텀 이벤트]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_events/)를 참조하세요. SDK 메서드를 통해 커스텀 이벤트를 기록하려면 [커스텀 이벤트 로깅]({{site.baseurl}}/developer_guide/analytics/logging_events/)을 참조하세요.

### 옵션 A: `/users/track` 엔드포인트로 기록

[`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) 엔드포인트를 호출하여 실시간으로 분석을 기록할 수 있습니다.

고객 프로필을 식별하려면 푸시 페이로드 키-값 페어에 `braze_id`를 포함하세요.

{% alert note %}
`braze_id`를 전달하면 프로필만 식별됩니다. 페이로드 값을 읽고 기록하려는 이벤트 또는 속성과 함께 `/users/track` 요청을 보내는 구현 로직이 별도로 필요합니다.
{% endalert %}

### 옵션 B: 앱 실행 후 SDK 메서드로 기록

페이로드 데이터를 로컬에 저장한 후 앱이 초기화된 후 SDK 메서드를 통해 커스텀 이벤트와 속성을 기록할 수도 있습니다. 이 접근 방식은 분석 데이터를 먼저 저장한 후 다음 앱 실행 시 전송하는 알림 콘텐츠 확장 플로우에서 일반적으로 사용됩니다.

{% alert important %}
앱이 실행될 때까지 분석이 Braze로 전송되지 않습니다. 해제 설정에 따라 사용자가 알림을 해제하는 시점과 앱이 열리고 분석을 전송하는 시점 사이에 지연이 발생할 수 있습니다.
{% endalert %}

## 알림 콘텐츠 확장에서 로깅(Swift)

다음 단계에서는 Swift 알림 콘텐츠 확장에서 커스텀 이벤트, 커스텀 속성 및 사용자 속성을 저장하고 전송하는 방법을 다룹니다.

### 1단계: Xcode에서 앱 그룹 구성

Xcode에서 메인 앱 타겟에 `App Groups` 기능을 추가합니다. **App Groups**를 켜고 **+**를 클릭하여 새 그룹을 추가합니다. 앱의 번들 ID를 사용하여 그룹 식별자를 생성합니다(예: `group.com.company.appname.xyz`). 메인 앱 타겟과 콘텐츠 확장 타겟 모두에서 **App Groups**를 켭니다.

![메인 앱과 알림 확장에 대해 App Groups 기능이 활성화된 Xcode]({% image_buster /assets/img/swift/push_story/add_app_groups.png %})

### 2단계: 기록할 항목 선택

스니펫을 구현하기 전에 기록할 분석 카테고리를 선택하세요:

- **커스텀 이벤트:** 사용자가 수행하는 동작(예: 플로우 완료 또는 특정 UI 요소 탭). 동작 기반 트리거, 세분화 및 이벤트 분석에 커스텀 이벤트를 사용합니다. 자세한 내용은 [커스텀 이벤트]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_events/) 및 [커스텀 이벤트 로깅]({{site.baseurl}}/developer_guide/analytics/logging_events/)을 참조하세요.
- **커스텀 속성:** 정의하고 시간이 지남에 따라 업데이트하는 프로필 필드(예: `plan_tier` 또는 `preferred_language`). 자세한 내용은 [커스텀 속성]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/) 및 [사용자 속성 설정]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/)을 참조하세요.
- **사용자 속성:** 표준 프로필 필드(예: 이메일, 이름, 전화번호). 샘플 코드에서는 타입이 지정된 `UserAttribute` 모델로 표현된 후 Braze 사용자 필드에 매핑됩니다.

이 섹션의 헬퍼 파일(`RemoteStorage`, `UserAttribute`, `EventName Dictionary`)은 이 샘플 구현에서 사용하는 로컬 유틸리티 파일입니다. 내장 SDK 클래스가 아닙니다. 페이로드에서 파생된 데이터를 `UserDefaults`에 저장하고, 보류 중인 사용자 업데이트를 위한 타입 모델을 정의하며, 이벤트 페이로드 구성을 표준화합니다. 로컬 데이터 저장 동작에 대한 자세한 내용은 [스토리지]({{site.baseurl}}/developer_guide/storage/?tab=swift)를 참조하세요.

{% alert note %}
이 섹션의 헬퍼 파일 예제는 iOS 전용(Swift 및 Objective-C)입니다. Android 및 웹에서 커스텀 이벤트와 속성을 기록하는 방법은 [커스텀 이벤트 로깅]({{site.baseurl}}/developer_guide/analytics/logging_events/)([Android]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=android), [Web]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=web)) 및 [사용자 속성 설정]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/)([Android]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?tab=android), [Web]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?tab=web))을 참조하세요.
{% endalert %}

{% tabs local %}
{% tab Custom events %}

#### 커스텀 이벤트 저장

사전을 빌드하고, 메타데이터를 채우고, 헬퍼 파일로 저장하여 분석 페이로드를 생성합니다.

1. 이벤트 메타데이터로 사전을 초기화합니다.
2. 이벤트 데이터를 검색하고 저장하기 위해 `userDefaults`를 초기화합니다.
3. 기존 배열이 있으면 추가하고 저장합니다.
4. 배열이 없으면 새 배열을 저장합니다.

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

#### Braze에 커스텀 이벤트 전송

SDK 초기화 직후에 저장된 분석을 기록합니다.

1. 보류 중인 이벤트를 순회합니다.
2. 각 이벤트의 키-값 페어를 순회합니다.
3. `event_name` 키를 확인합니다.
4. 나머지 키-값 페어를 `properties` 사전에 추가합니다.
5. 각 커스텀 이벤트를 기록합니다.
6. 스토리지에서 보류 중인 이벤트를 제거합니다.

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

#### 커스텀 속성 저장

분석 사전을 처음부터 생성한 후 저장합니다.

1. 속성 메타데이터로 사전을 초기화합니다.
2. 속성 데이터를 검색하고 저장하기 위해 `userDefaults`를 초기화합니다.
3. 기존 배열이 있으면 추가하고 저장합니다.
4. 배열이 없으면 새 배열을 저장합니다.

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

#### Braze에 커스텀 속성 전송

SDK 초기화 직후에 저장된 분석을 기록합니다.

1. 보류 중인 속성을 순회합니다.
2. 각 키-값 페어를 순회합니다.
3. 각 커스텀 속성 키와 값을 기록합니다.
4. 스토리지에서 보류 중인 속성을 제거합니다.

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

#### 사용자 속성 저장

사용자 속성을 저장할 때 업데이트되는 사용자 필드(`email`, `first_name`, `phone_number` 등)를 캡처하는 커스텀 오브젝트를 생성합니다. 이 오브젝트는 `UserDefaults`를 통해 저장 및 검색할 수 있어야 합니다. 예제는 **헬퍼 파일** 탭의 `UserAttribute` 헬퍼 파일을 참조하세요.

1. 해당 타입으로 인코딩된 `UserAttribute` 오브젝트를 초기화합니다.
2. 데이터를 검색하고 저장하기 위해 `userDefaults`를 초기화합니다.
3. 기존 배열이 있으면 추가하고 저장합니다.
4. 배열이 없으면 새 배열을 저장합니다.

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

#### Braze에 사용자 속성 전송

SDK 초기화 직후에 저장된 분석을 기록합니다.

1. `pendingAttributes` 데이터를 순회합니다.
2. 각 `UserAttribute`를 디코딩합니다.
3. 속성 타입에 따라 사용자 필드를 설정합니다.
4. 스토리지에서 보류 중인 사용자 속성을 제거합니다.

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

#### RemoteStorage 헬퍼 파일

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

#### UserAttribute 헬퍼 파일

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

#### EventName 사전 헬퍼 파일

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

## 결과 분석

분석 카테고리에 맞는 보고 화면을 사용하세요:

| 분석 카테고리 | Braze에서 확인하는 위치 |
| --- | --- |
| 네이티브 푸시 분석 | 캠페인 수준의 푸시 열기 측정기준을 보려면 푸시 캠페인의 **캠페인 분석** 페이지로 이동합니다. 측정기준 정의는 [영향받은 열기]({{site.baseurl}}/user_guide/analytics/tracking/influenced_opens/)를 참조하세요. 커스텀 분석 뷰를 구축하려면 **분석** > **보고서 빌더(신규)**로 이동합니다. 탐색 단계는 [보고서 빌더]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/)를 참조하세요. 웨어하우스 수준의 이벤트 스키마는 [메시지 참여 이벤트]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/)를 참조하세요. |
| 커스텀 이벤트 및 속성 | 커스텀 이벤트 트렌드를 보려면 **분석** > **커스텀 이벤트 보고서**로 이동합니다. 자세한 내용은 [커스텀 이벤트]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_events/)를 참조하세요. 사용자 수준의 값을 검사하려면 **사용자 검색** 페이지로 이동하여 프로필을 엽니다. 단계는 [고객 프로필]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/)을 참조하세요. 이러한 값으로 오디언스를 필터링하려면 **오디언스** > **세그먼트**로 이동합니다. 탐색 단계는 [세그먼트 생성]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/) 및 [세분화 필터]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/)의 필터 옵션을 참조하세요. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

커스텀 보고서 생성에 대해서는 [보고서 빌더]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/)를 참조하세요.

## 관련 참조

- [푸시 알림]({{site.baseurl}}/developer_guide/push_notifications/)
- [커스텀 이벤트 로깅]({{site.baseurl}}/developer_guide/analytics/logging_events/)
- [커스텀 이벤트]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_events/)
- [사용자 추적 엔드포인트(`/users/track`)]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)
- [Braze Android SDK 리포지토리](https://github.com/braze-inc/braze-android-sdk)
- [Braze Swift SDK 리포지토리](https://github.com/braze-inc/braze-swift-sdk)
- [Braze Web SDK 리포지토리](https://github.com/braze-inc/braze-web-sdk)