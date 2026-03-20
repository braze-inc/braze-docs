---
nav_title: Set custom attributes
article_title: iOS용 커스텀 속성 설정
platform: iOS
page_order: 3
description: "이 참조 문서에서는 iOS 애플리케이션에서 커스텀 속성을 설정하는 방법을 보여줍니다."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# iOS용 커스텀 속성 설정

Braze는 사용자에게 속성을 할당하는 방법을 제공합니다. 대시보드에서 이러한 속성에 따라 사용자를 필터링하고 세분화할 수 있습니다.

구현하기 전에 [모범 사례]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection)에서 커스텀 이벤트, 커스텀 속성 및 구매 이벤트가 제공하는 세분화 옵션 예제와 [이벤트 명명 규칙]({{site.baseurl}}/user_guide/data/custom_data/event_naming_conventions/)에 대한 참고 사항을 검토하세요.

## 기본 사용자 속성 할당하기

사용자 속성을 할당하려면 공유된 `ABKUser` 오브젝트에 적절한 필드를 설정해야 합니다.

다음은 이름 속성 설정 예제입니다.

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[Appboy sharedInstance].user.firstName = @"first_name";
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.firstName = "first_name"
```

{% endtab %}
{% endtabs %}

`ABKUser` 오브젝트에 다음 속성을 설정해야 합니다:

- `firstName`
- `lastName`
- `email`
- `dateOfBirth`
- `country`
- `language`
- `homeCity`
- `phone`
- `userID`
- `gender`

## 커스텀 사용자 속성 할당하기

기본 사용자 속성 외에도 Braze에서는 여러 가지 데이터 유형을 사용하여 커스텀 속성을 정의할 수 있습니다. 이러한 각 속성에서 지원하는 세분화 옵션에 대한 자세한 내용은 [사용자 데이터 수집]({{site.baseurl}}/developer_guide/analytics/)을 참조하세요.

### 문자열 값이 있는 커스텀 속성

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].user setCustomAttributeWithKey:@"your_attribute_key" andStringValue:"your_attribute_value"];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.setCustomAttributeWithKey("your_attribute_key", andStringValue: "your_attribute_value")
```

{% endtab %}
{% endtabs %}

### 정수 값이 있는 커스텀 속성

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].user setCustomAttributeWithKey:@"your_attribute_key" andIntegerValue:yourIntegerValue];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.setCustomAttributeWithKey("your_attribute_key", andIntegerValue: yourIntegerValue)
```

{% endtab %}
{% endtabs %}

### double 값이 있는 커스텀 속성

Braze는 데이터베이스 내에서 `float` 및 `double` 값을 동일하게 처리합니다.

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].user setCustomAttributeWithKey:@"your_attribute_key" andDoubleValue:yourDoubleValue];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.setCustomAttributeWithKey("your_attribute_key", andDoubleValue: yourDoubleValue)
```

{% endtab %}
{% endtabs %}

### 부울 값이 있는 커스텀 속성

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].user setCustomAttributeWithKey:@"your_attribute_key" andBOOLValue:yourBOOLValue];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.setCustomAttributeWithKey("your_attribute_key", andBOOLValue: yourBoolValue)
```

{% endtab %}
{% endtabs %}

### 날짜 값이 있는 커스텀 속성

이 방법을 통해 Braze에 전달되는 날짜는 [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) 형식(예: `2013-07-16T19:20:30+01:00`) 또는 `yyyy-MM-dd'T'HH:mm:ss:SSSZ` 형식(`2016-12-14T13:32:31.601-0800`)이어야 합니다.

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].user setCustomAttributeWithKey:@"your_attribute_key" andDateValue:yourDateValue];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.setCustomAttributeWithKey("your_attribute_key", andDateValue:yourDateValue)
```

{% endtab %}
{% endtabs %}

### 배열 값이 있는 커스텀 속성

배열의 기본 및 최대 요소 개수는 500개입니다. Braze 대시보드의 **데이터 설정** > **커스텀 속성**에서 배열의 최대 요소 개수를 업데이트할 수 있습니다. 최대 요소 개수를 초과하는 배열은 최대 요소 개수만큼 잘립니다.


{% tabs %}
{% tab OBJECTIVE-C %}

```objc
// Setting a custom attribute with an array value
[[Appboy sharedInstance].user setCustomAttributeArrayWithKey:@"array_name" array:@[@"value1",  @"value2"]];
// Adding to a custom attribute with an array value
[[Appboy sharedInstance].user addToCustomAttributeArrayWithKey:@"array_name" value:@"value3"];
// Removing a value from an array type custom attribute
[[Appboy sharedInstance].user removeFromCustomAttributeArrayWithKey:@"array_name" value:@"value2"];
// Removing an entire array and key
[[Appboy sharedInstance].user setCustomAttributeArrayWithKey:@"array_name" array:nil];
```

{% endtab %}
{% tab swift %}

```swift
// Setting a custom attribute with an array value
Appboy.sharedInstance()?.user.setCustomAttributeArrayWithKey("array_name", array: ["value1",  "value2"])
// Adding to a custom attribute with an array value
Appboy.sharedInstance()?.user.addToCustomAttributeArrayWithKey("array_name", value: "value3")
// Removing a value from an array type custom attribute
Appboy.sharedInstance()?.user.removeFromCustomAttributeArrayWithKey("array_name", value: "value2")
```

{% endtab %}
{% endtabs %}

### 커스텀 속성 설정 해제하기

커스텀 속성은 다음 방법을 사용하여 설정 해제할 수도 있습니다:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].user unsetCustomAttributeWithKey:@"your_attribute_key"];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.unsetCustomAttributeWithKey("your_attribute_key")
```

{% endtab %}
{% endtabs %}

### 커스텀 속성 증가/감소시키기

이 코드는 증분 커스텀 속성의 예시입니다. 커스텀 속성의 값을 양의 정수나 음의 정수 또는 long 값만큼 증가시킬 수 있습니다.

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].user incrementCustomUserAttribute:@"your_attribute_key" by:incrementIntegerValue];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.incrementCustomUserAttribute("your_attribute_key", by: incrementIntegerValue)
```

{% endtab %}
{% endtabs %}

### REST API를 통해 커스텀 속성 설정하기

REST API를 사용하여 사용자 속성을 설정할 수도 있습니다. 자세한 내용은 [사용자 API 설명서]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data)를 참조하세요.

### 커스텀 속성 값 제한

커스텀 속성 값의 최대 길이는 255자이며, 이보다 긴 값은 잘립니다.

#### 추가 정보

- 자세한 내용은 [`ABKUser.h` 파일](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h)에서 확인할 수 있습니다.
- 자세한 내용은 [`ABKUser` 설명서](http://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_user.html)를 참조하세요.

## 사용자 구독 설정하기

사용자에 대한 구독(이메일 또는 푸시)을 설정하려면 각각 `setEmailNotificationSubscriptionType` 또는 `setPushNotificationSubscriptionType` 함수를 호출합니다. 이 두 함수 모두 열거형 `ABKNotificationSubscriptionType`을 인수로 받습니다. 이 유형에는 세 가지 상태가 있습니다:

| 구독 상태 | 정의 |
| ------------------- | ---------- |
| `ABKOptedin` | 구독하고 명시적으로 옵트인한 경우 |
| `ABKSubscribed` | 구독 중이지만 명시적으로 옵트인하지 않은 경우 |
| `ABKUnsubscribed` | 구독 취소 및/또는 명시적으로 수신 거부한 경우 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

앱에서 푸시 알림을 보낼 수 있도록 권한을 부여한 사용자의 기본 상태는 `ABKOptedin`입니다. iOS에서는 명시적인 옵트인이 필요하기 때문입니다.

유효한 이메일 주소가 수신되면 자동으로 `ABKSubscribed`로 설정되지만, 명시적인 옵트인 프로세스를 설정하고 사용자의 명시적인 동의를 받은 후 이 값을 `OptedIn`으로 설정하는 것이 좋습니다. 자세한 내용은 [사용자 구독 관리하기]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/)를 참조하세요.

### 이메일 구독 설정하기

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].user setEmailNotificationSubscriptionType: ABKNotificationSubscriptionType]
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.setEmailNotificationSubscriptionType(ABKNotificationSubscriptionType)
```

{% endtab %}
{% endtabs %}

### 푸시 알림 구독 설정하기

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].user setPushNotificationSubscriptionType: ABKNotificationSubscriptionType]
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.setPushNotificationSubscriptionType(ABKNotificationSubscriptionType)
```

{% endtab %}
{% endtabs %}

자세한 내용은 [사용자 구독 관리하기]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/)를 참조하세요.