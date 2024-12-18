---
nav_title: 사용자 지정 속성 설정
article_title: iOS용 사용자 지정 속성 설정
platform: Swift
page_order: 3
description: "이 참조 문서에서는 Swift SDK의 커스텀 속성을 설정하는 방법을 보여줍니다."

---

# 사용자 지정 속성 설정

> Braze는 사용자에게 속성을 할당하는 방법을 제공합니다. 대시보드에서 이러한 속성에 따라 사용자를 필터링하고 세분화할 수 있습니다.

구현하기 전에 [이벤트 명명 규칙]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/)의 참고 사항과 함께 [모범 사례]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection)에서 커스텀 이벤트, 커스텀 속성 및 구매 이벤트가 제공하는 세분화 옵션 예제를 검토하세요.

## 기본 사용자 속성 할당하기

사용자 속성을 할당하려면 공유된 `ABKUser` 객체에 적절한 필드를 설정해야 합니다.

다음은 이름 속성 설정 예제입니다.

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.set(firstName: "first_name")
```

{% endtab %}
{% tab 목표-C %}

```objc
[AppDelegate.braze.user setFirstName:@"first_name"];
```

{% endtab %}
{% endtabs %}

`Braze.User` 객체에 다음 속성을 설정해야 합니다:

- `firstName`
- `lastName`
- `email`
- `dateOfBirth`
- `country`
- `language`
- `homeCity`
- `phone`
- `gender`

## 사용자 지정 사용자 속성 할당

기본 사용자 속성 외에도 Braze에서는 여러 가지 데이터 유형을 사용하여 커스텀 속성을 정의할 수 있습니다. 이러한 각 속성에서 지원할 수 있는 세분화 옵션에 대한 자세한 내용은 [사용자 데이터 수집]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/)을 참조하세요.

### 문자열 값이 있는 사용자 지정 속성

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.setCustomAttribute(key: "your_attribute_key", value: "your_attribute_value")
```

{% endtab %}
{% tab 목표-C %}

```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" stringValue:"your_attribute_value"];
```

{% endtab %}
{% endtabs %}

### 정수 값을 가진 사용자 지정 속성

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.setCustomAttribute(key: "your_attribute_key", value: yourIntegerValue)
```

{% endtab %}
{% tab 목표-C %}

```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" andIntegerValue:yourIntegerValue];
```

{% endtab %}
{% endtabs %}

### 이중 값을 가진 사용자 지정 속성

Braze는 데이터베이스 내에서 `float` 및 `double` 값을 동일하게 처리합니다.

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.setCustomAttribute(key: "your_attribute_key", value: yourDoubleValue)
```

{% endtab %}
{% tab 목표-C %}

```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" andDoubleValue:yourDoubleValue];
```

{% endtab %}
{% endtabs %}

### 부울 값이 있는 사용자 지정 속성

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.setCustomAttribute("your_attribute_key", value: yourBoolValue)
```

{% endtab %}
{% tab 목표-C %}

```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" andBOOLValue:yourBOOLValue];
```

{% endtab %}
{% endtabs %}

### 날짜 값이 있는 사용자 지정 속성

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.setCustomAttribute("your_attribute_key", dateValue:yourDateValue)
```

{% endtab %}
{% tab 목표-C %}

```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" andDateValue:yourDateValue];
```

{% endtab %}
{% endtabs %}

### 배열 값을 가진 사용자 정의 속성

[커스텀 속성 배열]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#arrays)의 최대 요소 개수 기본값은 25개입니다. 최대 요소 수를 초과하는 배열은 최대 요소 수를 포함하도록 잘립니다. 개별 배열의 최댓값은 최대 100개까지 늘릴 수 있습니다. 이 최대 한도를 늘리려면 고객 서비스 관리자에게 문의하세요. 


{% tabs %}
{% tab swift %}

```swift
// Setting a custom attribute with an array value
AppDelegate.braze?.user.setCustomAttributeArray(key: "array_name", array: ["value1",  "value2"])
// Adding to a custom attribute with an array value
AppDelegate.braze?.user.addToCustomAttributeArray(key: "array_name", value: "value3")
// Removing a value from an array type custom attribute
AppDelegate.braze?.user.removeFromCustomAttributeArray(key: "array_name", value: "value2")
```

{% endtab %}
{% tab 목표-C %}

```objc
// Setting a custom attribute with an array value
[AppDelegate.braze.user setCustomAttributeArrayWithKey:@"array_name" array:@[@"value1",  @"value2"]];
// Adding to a custom attribute with an array value
[AppDelegate.braze.user addToCustomAttributeArrayWithKey:@"array_name" value:@"value3"];
// Removing a value from an array type custom attribute
[AppDelegate.braze.user removeFromCustomAttributeArrayWithKey:@"array_name" value:@"value2"];
// Removing an entire array and key
[AppDelegate.braze.user setCustomAttributeArrayWithKey:@"array_name" array:nil];
```

{% endtab %}
{% endtabs %}

### 사용자 지정 속성 설정 해제하기

사용자 지정 속성은 다음 방법을 사용하여 설정 해제할 수도 있습니다:

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.unsetCustomAttribute(key: "your_attribute_key")
```

{% endtab %}
{% tab 목표-C %}

```objc
[AppDelegate.braze.user unsetCustomAttributeWithKey:@"your_attribute_key"];
```

{% endtab %}
{% endtabs %}

### 사용자 지정 속성 늘리기/줄이기

이 코드는 증분 사용자 지정 속성의 예시입니다. 커스텀 속성의 값을 양의 정수나 음의 정수 또는 long 값만큼 증가시킬 수 있습니다.

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.incrementCustomUserAttribute(key: "your_attribute_key", by: incrementIntegerValue)
```

{% endtab %}
{% tab 목표-C %}

```objc
[AppDelegate.braze.user incrementCustomUserAttribute:@"your_attribute_key" by:incrementIntegerValue];
```

{% endtab %}
{% endtabs %}

### REST API를 통해 사용자 지정 속성 설정하기

REST API를 사용하여 사용자 속성을 설정할 수도 있습니다. 자세한 내용은 [사용자 API 설명서를]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data) 참조하세요.

### 사용자 지정 속성 값 제한

커스텀 속성 값의 최대 길이는 255자이며, 이보다 긴 값은 잘립니다.

#### 추가 정보

- 자세한 내용은 [`Braze.User` 설명서](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class)를 참조하세요.

## 사용자 구독 설정하기

사용자에 대한 가입(이메일 또는 푸시)을 설정하려면 각각 `set(emailSubscriptionState:)` 또는 `set(pushNotificationSubscriptionState:)` 함수를 호출합니다. 이 두 함수 모두 열거형 `Braze.User.SubscriptionState` 을 인자로 받습니다. 이 유형에는 세 가지 상태가 있습니다:

| 구독 상태 | 정의 |
| ------------------- | ---------- |
| `optedIn` | 가입 상태, 명시적으로 옵트인 |
| `subscribed` | 가입 상태, 명시적으로 옵트인하지 않음 |
| `unsubscribed` | 구독 취소 및/또는 명시적 수신 거부 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

앱에서 푸시 알림을 보낼 수 있도록 권한을 부여한 사용자의 기본 상태는 `optedIn`입니다. iOS에서는 명시적인 옵트인이 필요하기 때문입니다.

유효한 이메일 주소가 수신되면 `subscribed` 으로 자동 설정되지만, 명시적인 옵트인 프로세스를 설정하고 사용자의 명시적인 동의를 받은 후 이 값을 `optedIn` 으로 설정하는 것이 좋습니다. 자세한 내용은 [사용자 구독 관리하기를]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/) 참조하세요.

### 이메일 구독 설정

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.set(emailSubscriptionState: Braze.User.SubscriptionState)
```

{% endtab %}
{% tab 목표-C %}

```objc
[AppDelegate.braze.user setEmailSubscriptionState: BRZUserSubscriptionState]
```

{% endtab %}
{% endtabs %}

### 푸시 알림 구독 설정하기

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.set(pushNotificationSubscriptionState: Braze.User.SubscriptionState)
```

{% endtab %}
{% tab 목표-C %}

```objc
[AppDelegate.braze.user setPushNotificationSubscriptionState: BRZUserSubscriptionState]
```

{% endtab %}
{% endtabs %}

자세한 내용은 [사용자 구독 관리하기를]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/) 참조하세요.

