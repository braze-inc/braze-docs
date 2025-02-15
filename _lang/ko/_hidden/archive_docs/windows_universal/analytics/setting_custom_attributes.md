---
nav_title: 사용자 지정 속성 설정
article_title: Windows 유니버설용 사용자 지정 속성 설정
platform: Windows Universal
page_order: 3
description: "이 참조 문서에서는 Windows 유니버설 플랫폼에서 커스텀 속성을 설정하는 방법에 대해 설명합니다."
hidden: true
---

# 사용자 지정 속성 설정
{% multi_lang_include archive/windows_deprecation.md %}

Braze는 사용자에게 속성을 할당하는 방법을 제공합니다. 대시보드에서 이러한 속성에 따라 사용자를 필터링하고 세분화할 수 있습니다.

구현하기 전에 커스텀 이벤트, 커스텀 속성 및 구매 이벤트가 제공하는 세분화 옵션의 예시를 [모범 사례][7]에서 검토하세요.

사용자 속성은 현재 `IAppboyUser` 에 할당할 수 있습니다. 현재 `IAppboyUser`에 대한 참조를 얻으려면 `Appboy.SharedInstance.AppboyUser`를 호출합니다

## 기본 사용자 속성 할당하기

다음 속성을 `IAppboyUser` 의 속성으로 정의해야 합니다:

- `FirstName`
- `LastName`
- `Email`
- `Gender`
- `DateOfBirth`
- `Country`
- `HomeCity`
- `PhoneNumber`

**구현 예시**

```csharp
Appboy.SharedInstance.AppboyUser.FirstName = "User's First Name"
```

## 사용자 지정 사용자 속성 할당

기본 사용자 속성 외에도 Braze에서는 다양한 데이터 유형을 사용하여 사용자 지정 속성을 정의할 수 있습니다. 세분화 옵션과 이러한 각 속성이 사용자에게 미치는 영향에 대한 자세한 내용은 [모범 사례를]({{site.baseurl}}/developer_guide/platform_integration_guides/windows_universal/analytics/setting_user_ids/#user-id-integration-best-practices-and-notes) 참조하세요.

### 사용자 지정 속성 값 설정

{% tabs %}
{% tab 부울 %}
```csharp
bool SetCustomAttribute(STRING_KEY, BOOL_VALUE);
```
{% endtab %}
{% tab 정수 %}
```csharp
bool SetCustomAttribute(STRING_KEY, INT_VALUE);
```
{% endtab %}
{% tab 더블 또는 플로트 %}
```csharp
bool SetCustomAttribute(STRING_KEY, DOUBLE_VALUE);
```
Braze는 데이터베이스 내에서 FLOAT와 DOUBLE 값을 정확히 동일하게 취급합니다.
{% endtab %}
{% tab 문자열 %}
```csharp
bool SetCustomAttribute(STRING_KEY, "STRING_VALUE");
```
{% endtab %}
{% tab Long %}
```csharp
bool SetCustomAttribute(STRING_KEY, LONG_VALUE);
```
{% endtab %}
{% tab 날짜 %}
```csharp
bool SetCustomAttribute(STRING_KEY, "DATE_VALUE");
```
>  Braze에 전달된 날짜는 [ISO 8601][2] 형식, e.g `2013-07-16T19:20:30+01:00` 또는 `yyyy-MM-dd'T'HH:mm:ss:SSSZ` 형식 e.g `2016-12-14T13:32:31.601-0800`이어야 합니다
{% endtab %}
{% tab 배열 %}
```csharp
// Setting a custom attribute with an array value
Appboy.SharedInstance.EventLogger.SetCustomAttributeArray("custom_attribute_array_test", testSetArray);
// Adding to a custom attribute with an array value
Appboy.SharedInstance.EventLogger.AddToCustomAttributeArray("custom_attribute_array_test", testAddString);
// Removing a value from an array type custom attribute
Appboy.SharedInstance.EventLogger.RemoveFromCustomAttributeArray("custom_attribute_array_test", testRemString);
```
{% endtab %}
{% endtabs %}

### 사용자 지정 속성 늘리기/줄이기

이 코드는 증분 사용자 지정 속성의 예시입니다. 커스텀 속성의 값을 양수 또는 음수의 정수 값만큼 증가시킬 수 있습니다.

```csharp
bool IncrementCustomAttribute(STRING_KEY, INCREMENT_INTEGER_VALUE);
```

### 사용자 지정 속성 설정 해제하기

사용자 지정 속성은 다음 방법을 사용하여 설정 해제할 수도 있습니다:

```csharp
bool UnsetCustomAttribute(STRING_KEY);
```

### REST API를 통해 사용자 지정 속성 설정하기

REST API를 사용하여 사용자 속성을 설정할 수도 있습니다. 자세한 내용은 [사용자 API][4] 설명서를 참조하세요.

### 사용자 지정 속성 값 제한

커스텀 속성 값의 최대 길이는 255자이며, 이보다 긴 값은 잘립니다.

## 알림 구독 상태 관리하기

사용자에 대한 구독(이메일 또는 푸시)을 설정하려면 `IAppboyUser` 의 속성으로 다음과 같은 구독 상태를 설정할 수 있습니다. Braze의 구독 상태는 이메일과 푸시 모두에 대해 세 가지 상태가 있습니다.

| 구독 상태 | 정의 |
| ------------------- | ---------- |
| `OptedIn` | 구독하고 명시적으로 동의한 경우 |
| `Subscribed` | 구독 중이지만 명시적으로 옵트인하지 않은 경우 |
| `UnSubscribed` | 구독 취소 및/또는 명시적 수신 거부 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

- `EmailNotificationSubscriptionType`
  - 유효한 이메일 주소가 수신되면 자동으로 `Subscribed` 로 설정되지만, 명시적인 옵트인 프로세스를 설정하고 사용자의 명시적인 동의를 받은 후 이 값을 `OptedIn` 으로 설정하는 것이 좋습니다.
- `PushNotificationSubscriptionType`
  - 사용자는 유효한 푸시 등록 시 자동으로 `Subscribed`로 설정되지만, 명시적인 옵트인 프로세스를 설정하고 사용자의 명시적인 동의를 받은 후 이 값을 `OptedIn`으로 설정하는 것이 좋습니다.

>  이러한 유형은 `AppboyPlatform.PCL.Models.NotificationSubscriptionType`에 해당합니다. 자세한 내용은 [사용자 구독 관리하기를][10] 참조하세요.

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/windows_universal/analytics/setting_user_ids/#user-id-integration-best-practices--notes
[2]: http://en.wikipedia.org/wiki/ISO_8601
[4]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
[7]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection
[10]: {{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions
