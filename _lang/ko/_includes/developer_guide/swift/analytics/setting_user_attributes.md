{% multi_lang_include developer_guide/prerequisites/swift.md %}

## 기본 사용자 속성

### Supported attributes

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

### 기본 속성 설정

기본 사용자 속성을 설정하려면 공유 `Braze.User` 객체의 적절한 필드를 설정하십시오. 다음은 이름 속성 설정 예제입니다.

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.set(firstName: "Alex")
```

{% endtab %}
{% tab objective-c %}

```objc
[AppDelegate.braze.user setFirstName:@"Alex"];
```

{% endtab %}
{% endtabs %}

### 기본 속성 해제

기본 사용자 속성을 해제하려면 관련 메서드에 `nil`을 전달하십시오.

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.set(firstName: nil)
```

{% endtab %}
{% tab objective-c %}

```objc
[AppDelegate.braze.user setFirstName:nil];
```

{% endtab %}
{% endtabs %}

## 사용자 지정 사용자 속성

기본 사용자 속성 외에도 Braze는 여러 가지 데이터 유형을 사용하여 커스텀 속성을 정의할 수 있도록 허용합니다. 각 속성의 세분화 옵션에 대한 자세한 내용은 [사용자 데이터 수집]({{site.baseurl}}/developer_guide/analytics/)을 참조하십시오.

{% alert important %}
커스텀 속성 값의 최대 길이는 255자이며, 이보다 긴 값은 잘립니다. 자세한 내용은 [`Braze.User`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class)를 참조하십시오.
{% endalert %}

### 사용자 지정 속성 설정

{% tabs local %}
{% tab 문자열 %}
`string` 값으로 커스텀 속성을 설정하려면:

{% subtabs %}
{% subtab swift %}
```swift
AppDelegate.braze?.user.setCustomAttribute(key: "your_attribute_key", value: "your_attribute_value")
```
{% endsubtab %}

{% subtab objective-c %}
```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" stringValue:"your_attribute_value"];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab 정수 %}
`integer` 값으로 커스텀 속성을 설정하려면:

{% subtabs %}
{% subtab swift %}
```swift
AppDelegate.braze?.user.setCustomAttribute(key: "your_attribute_key", value: yourIntegerValue)
```
{% endsubtab %}

{% subtab objective-c %}
```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" andIntegerValue:yourIntegerValue];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab 부동 소수점 %}
Braze는 데이터베이스 내에서 `float` 및 `double` 값을 동일하게 처리합니다. 배정밀도 값으로 커스텀 속성을 설정하려면:

{% subtabs %}
{% subtab swift %}
```swift
AppDelegate.braze?.user.setCustomAttribute(key: "your_attribute_key", value: yourDoubleValue)
```
{% endsubtab %}

{% subtab objective-c %}
```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" andDoubleValue:yourDoubleValue];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab 부울 %}
`boolean` 값으로 커스텀 속성을 설정하려면:

{% subtabs %}
{% subtab swift %}
```swift
AppDelegate.braze?.user.setCustomAttribute("your_attribute_key", value: yourBoolValue)
```
{% endsubtab %}

{% subtab objective-c %}
```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" andBOOLValue:yourBOOLValue];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab 날짜 %}
`date` 값으로 커스텀 속성을 설정하려면:

{% subtabs %}
{% subtab swift %}
```swift
AppDelegate.braze?.user.setCustomAttribute("your_attribute_key", dateValue:yourDateValue)
```
{% endsubtab %}

{% subtab objective-c %}
```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" andDateValue:yourDateValue];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab 배열 %}
[커스텀 속성 배열]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#arrays)의 최대 요소 개수 기본값은 25개입니다. 최대 요소 수를 초과하는 배열은 최대 요소 수를 포함하도록 잘립니다. 개별 배열의 최댓값은 최대 100개까지 늘릴 수 있습니다. 이 최대 한도를 늘리려면 고객 서비스 관리자에게 문의하세요.

`array` 값으로 커스텀 속성을 설정하려면:

{% subtabs %}
{% subtab swift %}
```swift
// Setting a custom attribute with an array value
AppDelegate.braze?.user.setCustomAttributeArray(key: "array_name", array: ["value1",  "value2"])
// Adding to a custom attribute with an array value
AppDelegate.braze?.user.addToCustomAttributeArray(key: "array_name", value: "value3")
// Removing a value from an array type custom attribute
AppDelegate.braze?.user.removeFromCustomAttributeArray(key: "array_name", value: "value2")
```
{% endsubtab %}

{% subtab objective-c %}
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
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### 커스텀 속성 증가 또는 감소

이 코드는 증분 사용자 지정 속성의 예시입니다. 사용자 정의 속성의 값을 `integer` 또는 `long` 값으로 증가시킬 수 있습니다:

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.incrementCustomUserAttribute(key: "your_attribute_key", by: incrementIntegerValue)
```

{% endtab %}
{% tab objective-c %}

```objc
[AppDelegate.braze.user incrementCustomUserAttribute:@"your_attribute_key" by:incrementIntegerValue];
```

{% endtab %}
{% endtabs %}

### 사용자 정의 속성 해제

{% tabs %}
{% tab swift %}
사용자 정의 속성을 해제하려면 관련 속성 키를 `unsetCustomAttribute` 메서드에 전달하십시오.

```swift
AppDelegate.braze?.user.unsetCustomAttribute(key: "your_attribute_key")
```

{% endtab %}
{% tab objective-c %}
사용자 정의 속성을 해제하려면 관련 속성 키를 `unsetCustomAttributeWithKey` 메서드에 전달하십시오.

```objc
[AppDelegate.braze.user unsetCustomAttributeWithKey:@"your_attribute_key"];
```

{% endtab %}
{% endtabs %}

### 사용자 정의 속성 중첩

사용자 정의 속성 내에 속성을 중첩할 수도 있습니다. 다음 예제에서는 중첩된 속성을 가진 `favorite_book` 객체가 사용자 프로필의 사용자 정의 속성으로 설정됩니다. 자세한 내용은 [중첩된 사용자 정의 속성]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support)을 참조하십시오.

{% tabs %}
{% tab swift %}
```swift
let favoriteBook: [String: Any?] = [
  "title": "The Hobbit",
  "author": "J.R.R. Tolkien",
  "publishing_date": "1937"
]

braze.user.setCustomAttribute(key: "favorite_book", dictionary: favoriteBook)
```
{% endtab %}

{% tab objective-c %}
```objc
NSDictionary *favoriteBook = @{
  @"title": @"The Hobbit",
  @"author": @"J.R.R. Tolkien",
  @"publishing_date": @"1937"
};

[AppDelegate.braze.user setCustomAttributeWithKey:@"favorite_book" dictionary:favoriteBook];
```
{% endtab %}
{% endtabs %}

### REST API 사용

REST API를 사용하여 사용자 속성을 설정하거나 해제할 수도 있습니다. 자세한 정보는 [사용자 데이터 엔드포인트]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data)를 참조하십시오.

## 사용자 구독 설정

사용자에 대한 가입(이메일 또는 푸시)을 설정하려면 각각 `set(emailSubscriptionState:)` 또는 `set(pushNotificationSubscriptionState:)` 함수를 호출합니다. 이 두 함수 모두 열거형 `Braze.User.SubscriptionState` 을 인자로 받습니다. 이 유형에는 세 가지 상태가 있습니다:

| 구독 상태 | 정의 |
| ------------------- | ---------- |
| `optedIn` | 구독하고 명시적으로 동의한 경우 |
| `subscribed` | 구독 중이지만 명시적으로 옵트인하지 않은 경우 |
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
{% tab objective-c %}

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
{% tab objective-c %}

```objc
[AppDelegate.braze.user setPushNotificationSubscriptionState: BRZUserSubscriptionState]
```

{% endtab %}
{% endtabs %}

자세한 내용은 [사용자 구독 관리하기를]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/) 참조하세요.
