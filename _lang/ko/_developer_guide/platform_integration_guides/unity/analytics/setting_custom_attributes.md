---
nav_title: 사용자 지정 속성 설정
article_title: Unity용 커스텀 속성 설정
platform: 
  - Unity
  - iOS
  - Android
page_order: 2
description: "이 참조 문서에서는 Unity 플랫폼에서 커스텀 속성을 설정하고 해제하는 방법을 다룹니다."

---

# 사용자 지정 속성 설정

> Braze는 사용자에게 속성을 할당하는 방법을 제공합니다. 대시보드에서 이러한 속성에 따라 사용자를 필터링하고 세분화할 수 있습니다.

구현하기 전에 [모범 사례][1]에서 커스텀 이벤트, 커스텀 속성 및 구매 이벤트가 제공하는 세분화 옵션의 예제를 검토하세요.

## 기본 사용자 속성 할당하기

사용자 속성을 할당하려면 BrazeBinding 객체에서 적절한 메서드를 호출해야 합니다. 다음은 이 메서드를 사용하여 호출할 수 있는 기본 제공 속성 목록입니다.

### 이름
`AppboyBinding.SetUserFirstName("first name");`

### 성
`AppboyBinding.SetUserLastName("last name");`

### 사용자 이메일
`AppboyBinding.SetUserEmail("email@email.com");`

>  Braze를 통해 이메일을 보내지 않더라도 이메일 주소를 설정하는 것은 여전히 유용합니다. 이메일을 사용하면 개별 사용자 프로필을 쉽게 검색하고 문제 발생 시 문제를 해결할 수 있습니다.

### 성별
`AppboyBinding.SetUserGender(Appboy.Models.Gender);`

### 생년월일
`AppboyBinding.SetUserDateOfBirth("year(int)", "month(int)", "day(int)");`

### 사용자 국가
`AppboyBinding.SetUserCountry("country name");`

### 사용자 거주 구/군/시
`AppboyBinding.SetUserHomeCity("city name");`

### 사용자 이메일 구독
`AppboyBinding.SetUserEmailNotificationSubscriptionType(AppboyNotificationSubscriptionType);`

### 사용자 푸시 구독
`AppboyBinding.SetUserPushNotificationSubscriptionType(AppboyNotificationSubscriptionType);`

### 사용자 전화번호
`AppboyBinding.SetUserPhoneNumber("phone number");`

## 사용자 지정 사용자 속성 할당

기본 사용자 속성 외에도 Braze에서는 여러 가지 데이터 유형을 사용하여 커스텀 속성을 정의할 수 있습니다.
이러한 각 속성을 통해 제공되는 세분화 옵션에 대한 자세한 내용은 이 섹션의 ['모범 사례' 설명서][1]를 참조하세요.

### 사용자 지정 속성 값 설정

{% tabs %}
{% tab 부울 값 %}

```csharp
AppboyBinding.SetCustomUserAttribute("custom boolean attribute key", 'boolean value');
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
{% tab 문자열 %}

```csharp
AppboyBinding.SetCustomUserAttribute("custom string attribute key", "string custom attribute");
```

{% endtab %}
{% tab 날짜 %}

```csharp
AppboyBinding.SetCustomUserAttributeToNow("custom date attribute key");
```

```csharp
AppboyBinding.SetCustomUserAttributeToSecondsFromEpoch("custom date attribute key", 'integer value');
```

>  Braze에 전달된 날짜는 [ISO 8601][2] 형식, e.g `2013-07-16T19:20:30+01:00` 또는 `yyyy-MM-dd'T'HH:mm:ss:SSSZ` 형식 e.g `2016-12-14T13:32:31.601-0800`이어야 합니다

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
{% endtabs
%}
### 사용자 지정 속성 설정 해제하기

사용자 지정 속성은 다음 방법을 사용하여 설정 해제할 수도 있습니다:

```csharp
AppboyBinding.UnsetCustomUserAttribute("custom attribute key");
```

## REST API를 통해 사용자 지정 속성 설정하기
REST API를 사용하여 사용자 속성을 설정할 수도 있습니다. 그러려면 [사용자 API 설명서를][3] 참조하세요.

## 사용자 지정 속성 값 제한
커스텀 속성 값의 최대 길이는 255자이며, 이보다 긴 값은 잘립니다.

## 사용자 구독 설정하기

사용자에 대한 가입(이메일 또는 푸시)을 설정하려면 각각     
`AppboyBinding.SetUserEmailNotificationSubscriptionType()` 또는 `AppboyBinding.SetPushNotificationSubscriptionType()` 함수를 호출합니다. 이 두 함수는 `Appboy.Models.AppboyNotificationSubscriptionType` 매개변수를 인수로 사용합니다. 이 유형에는 세 가지 상태가 있습니다:

| 구독 상태 | 정의 |
| ------------------- | ---------- |
| `OPTED_IN` | 가입 상태, 명시적으로 옵트인 |
| `SUBSCRIBED` | 가입 상태, 명시적으로 옵트인하지 않음 |
| `UNSUBSCRIBED` | 구독 취소 및/또는 명시적 수신 거부 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

>  Windows에서 사용자에게 푸시 알림을 보내기 위해 명시적으로 옵트인할 필요는 없습니다. 사용자가 푸시에 등록되면 기본적으로 `OPTED_IN` 대신 `SUBSCRIBED`로 설정됩니다. 자세한 내용은 설명서에서 [가입 및 명시적 옵트인 구현][10]을 참조하세요.

- `EmailNotificationSubscriptionType`
  - 사용자는 유효한 이메일 주소를 수신하면 자동으로 `SUBSCRIBED` 로 설정됩니다. 그러나 명시적인 옵트인 프로세스를 설정하고 사용자의 명시적인 동의를 받은 후 이 값을 `OPTED_IN`으로 설정하는 것이 좋습니다. 자세한 내용은 [사용자 구독 변경][8] 문서를 참조하세요.
- `PushNotificationSubscriptionType`
  - 사용자는 유효한 푸시 등록 시 자동으로 `SUBSCRIBED` 로 설정됩니다. 그러나 명시적인 옵트인 프로세스를 설정하고 사용자의 명시적인 동의를 받은 후 이 값을 `OPTED_IN`으로 설정하는 것이 좋습니다. 자세한 내용은 [사용자 구독 변경][8] 문서를 참조하세요.

>  이러한 유형은 `Appboy.Models.AppboyNotificationSubscriptionType`에 해당합니다.

## 코드 예제

### 이메일 구독:

```csharp
AppboyBinding.SetUserEmailNotificationSubscriptionType(AppboyNotificationSubscriptionType.OPTED_IN);
```

### 푸시 알림 구독:

```csharp
AppboyBinding.SetUserPushNotificationSubscriptionType(AppboyNotificationSubscriptionType.OPTED_IN);
```

[1]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection
[2]: http://en.wikipedia.org/wiki/ISO_8601
[3]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
[8]: {{site.baseurl}}/user_guide/administrative/manage_your_users/managing_user_subscriptions/#changing-subscriptions
[10]: {{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions
