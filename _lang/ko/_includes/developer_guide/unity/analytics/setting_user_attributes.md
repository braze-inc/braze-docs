{% multi_lang_include developer_guide/prerequisites/unity.md %}

## 기본 사용자 속성

사용자 속성을 설정하려면 `BrazeBinding` 객체에서 적절한 메서드를 호출해야 합니다. 다음은 이 메서드를 사용하여 호출할 수 있는 기본 제공 속성 목록입니다.

| 속성                 | 코드 샘플 |
|---------------------------|-------------|
| 이름                | `AppboyBinding.SetUserFirstName("first name");` |
| 성                 | `AppboyBinding.SetUserLastName("last name");` |
| 사용자 이메일                | `AppboyBinding.SetUserEmail("email@email.com");` |
| 성별                    | `AppboyBinding.SetUserGender(Appboy.Models.Gender);` |
| 생년월일                | `AppboyBinding.SetUserDateOfBirth("year(int)", "month(int)", "day(int)");` |
| 사용자 국가              | `AppboyBinding.SetUserCountry("country name");` |
| 사용자 거주 구/군/시            | `AppboyBinding.SetUserHomeCity("city name");` |
| 사용자 이메일 구독   | `AppboyBinding.SetUserEmailNotificationSubscriptionType(AppboyNotificationSubscriptionType);` |
| 사용자 푸시 구독    | `AppboyBinding.SetUserPushNotificationSubscriptionType(AppboyNotificationSubscriptionType);` |
| 사용자 전화번호         | `AppboyBinding.SetUserPhoneNumber("phone number");` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## 사용자 지정 사용자 속성

기본 사용자 속성 외에도 Braze는 여러 가지 데이터 유형을 사용하여 커스텀 속성을 정의할 수 있도록 허용합니다. 각 속성의 세분화 옵션에 대한 자세한 내용은 [사용자 데이터 수집]({{site.baseurl}}/developer_guide/analytics)을 참조하십시오.

### 사용자 지정 속성 설정

{% tabs %}
{% tab 문자열 %}

```csharp
AppboyBinding.SetCustomUserAttribute("custom string attribute key", "string custom attribute");
```

{% endtab %}

{% tab 정수 %}

```csharp
// Set Integer Attribute
AppboyBinding.SetCustomUserAttribute("custom int attribute key", 'integer value');
// Increment Integer Attribute
AppboyBinding.IncrementCustomUserAttribute("key", increment(int))
```
{% endtab %}

{% tab Double %}

```csharp
AppboyBinding.SetCustomUserAttribute("custom double attribute key", 'double value');
```

{% endtab %}

{% tab 부울 %}

```csharp
AppboyBinding.SetCustomUserAttribute("custom boolean attribute key", 'boolean value');
```
{% endtab %}

{% tab 날짜 %}

```csharp
AppboyBinding.SetCustomUserAttributeToNow("custom date attribute key");
```

```csharp
AppboyBinding.SetCustomUserAttributeToSecondsFromEpoch("custom date attribute key", 'integer value');
```

{% alert note %}
Braze에 전달된 날짜는 [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) 형식(예: `2013-07-16T19:20:30+01:00`) 또는 `yyyy-MM-dd'T'HH:mm:ss:SSSZ` 형식(예: `2016-12-14T13:32:31.601-0800`)이어야 합니다.
{% endalert %}

{% endtab %}

{% tab 배열 %}

```csharp
// Setting An Array
AppboyBinding.SetCustomUserAttributeArray("key", array(List), sizeOfTheArray(int))
// Adding to an Array
AppboyBinding.AddToCustomUserAttributeArray("key", "Attribute")
// Removing an item from an Array
AppboyBinding.RemoveFromCustomUserAttributeArray("key", "Attribute")
```
{% endtab %}
{% endtabs %}

{% alert important %}
커스텀 속성 값의 최대 길이는 255자이며, 이보다 긴 값은 잘립니다.
{% endalert %}

### 커스텀 속성 해제

커스텀 사용자 속성을 해제하려면 다음 메서드를 사용하십시오:

```csharp
AppboyBinding.UnsetCustomUserAttribute("custom attribute key");
```

### REST API 사용

사용자 속성을 설정하거나 해제하기 위해 REST API를 사용할 수도 있습니다. 자세한 내용은 [사용자 데이터 엔드포인트]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data)을 참조하십시오.

## 사용자 구독 설정

사용자를 위한 이메일 또는 푸시 구독을 설정하려면 다음 함수 중 하나를 호출하십시오.

```csharp
// Email notifications
AppboyBinding.SetUserEmailNotificationSubscriptionType()

// Push notifications
AppboyBinding.SetPushNotificationSubscriptionType()`
```

두 함수 모두 `Appboy.Models.AppboyNotificationSubscriptionType`을 인수로 사용하며, 세 가지 다른 상태가 있습니다:

| 구독 상태 | 정의 |
| ------------------- | ---------- |
| `OPTED_IN` | 구독하고 명시적으로 동의한 경우 |
| `SUBSCRIBED` | 구독 중이지만 명시적으로 옵트인하지 않은 경우 |
| `UNSUBSCRIBED` | 구독 취소 및/또는 명시적 수신 거부 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Windows에서 사용자에게 푸시 알림을 보내기 위해 명시적으로 옵트인할 필요는 없습니다. 사용자가 푸시에 등록되면 기본적으로 `OPTED_IN` 대신 `SUBSCRIBED`로 설정됩니다. 자세한 내용은 설명서에서 [가입 및 명시적 옵트인 구현]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions)을 참조하세요.
{% endalert %}

| 구독 유형                        | 설명 |
|------------------------------------------|-------------|
| `EmailNotificationSubscriptionType`      | 사용자는 유효한 이메일 주소를 수신하면 자동으로 `SUBSCRIBED` 로 설정됩니다. 그러나 명시적인 옵트인 프로세스를 설정하고 사용자의 명시적인 동의를 받은 후 이 값을 `OPTED_IN`으로 설정하는 것이 좋습니다. 자세한 내용은 [사용자 구독 변경]({{site.baseurl}}/user_guide/administrative/manage_your_users/managing_user_subscriptions/#changing-subscriptions) 문서를 참조하세요. |
| `PushNotificationSubscriptionType`       | 사용자는 유효한 푸시 등록 시 자동으로 `SUBSCRIBED` 로 설정됩니다. 그러나 명시적인 옵트인 프로세스를 설정하고 사용자의 명시적인 동의를 받은 후 이 값을 `OPTED_IN`으로 설정하는 것이 좋습니다. 자세한 내용은 [사용자 구독 변경]({{site.baseurl}}/user_guide/administrative/manage_your_users/managing_user_subscriptions/#changing-subscriptions) 문서를 참조하세요. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
이러한 유형은 `Appboy.Models.AppboyNotificationSubscriptionType`에 해당합니다.
{% endalert %}

### 이메일 구독 설정

```csharp
AppboyBinding.SetUserEmailNotificationSubscriptionType(AppboyNotificationSubscriptionType.OPTED_IN);
```

### 푸시 알림 구독 설정하기

```csharp
AppboyBinding.SetUserPushNotificationSubscriptionType(AppboyNotificationSubscriptionType.OPTED_IN);
```
