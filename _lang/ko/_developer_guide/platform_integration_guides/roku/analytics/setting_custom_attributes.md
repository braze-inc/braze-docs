---
nav_title: 사용자 지정 속성 설정
article_title: Roku에 대한 사용자 지정 속성 설정
platform: Roku
page_order: 4
page_type: reference
description: "이 참조 문서에서는 Braze SDK를 통해 사용자에게 Roku의 커스텀 속성을 할당하는 방법을 설명합니다."

---

# 사용자 지정 속성 설정

> Braze는 사용자에게 속성을 할당하는 방법을 제공합니다. 대시보드에서 이러한 속성에 따라 사용자를 필터링하고 세분화할 수 있습니다.

구현하기 전에 [모범 사례]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection)에서 커스텀 이벤트, 사용자 속성 및 구매 이벤트가 제공하는 세분화 옵션의 예제를 검토하세요. 또한 [이벤트 이름 지정 규칙]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/)을 숙지하는 것이 좋습니다.

## 기본 사용자 속성 할당하기

사용자 속성은 현재 활성 상태인 사용자에게 할당됩니다. 다음과 같은 기본 필드를 설정할 수 있습니다:

- `FirstName`
- `LastName`
- `Email`
- `Gender`
- `DateOfBirth`
- `Country`
- `Language`
- `HomeCity`
- `PhoneNumber`

**구현 예시**<br>코드에서 이름을 설정하는 방식은 다음과 같습니다:

```brightscript
m.Braze.setFirstName("User's First Name")
```

## 사용자 지정 사용자 속성 할당

기본 사용자 속성 외에도 Braze에서는 여러 가지 데이터 유형을 사용하여 커스텀 속성을 정의할 수 있습니다.

### 사용자 지정 속성 값 설정
{% tabs %}
{% tab 부울 %}
```brightscript
m.Braze.setCustomAttribute("boolAttribute", true)
```
{% endtab %}
{% tab 정수 %}
```brightscript
m.Braze.setCustomAttribute("intAttribute", 5)
```
{% endtab %}
{% tab 플로트 또는 더블 %}
```brightscript
m.Braze.setCustomAttribute("floatAttribute", 3.5)
```
Braze는 데이터베이스 내에서 FLOAT와 DOUBLE 값을 정확히 동일하게 취급합니다.
{% endtab %}
{% tab 문자열 %}
```brightscript
m.Braze.setCustomAttribute("stringAttribute", "stringValue")
```
{% endtab %}
{% tab 날짜 %}
```brightscript
dateAttribute = CreateObject("roDateTime")
dateAttribute.fromISO8601String("1992-11-29 00:00:00.000")
m.Braze.setCustomAttribute("dateAttribute", dateAttribute)
```
{% endtab %}
{% tab 배열 %}
```brightscript
stringArray = createObject("roArray", 3, true)
stringArray.Push("string1")
stringArray.Push("string2")
stringArray.Push("string3")
m.Braze.setCustomAttribute("arrayAttribute", stringArray)
```
{% endtab %}
{% endtabs %}

### 사용자 지정 속성 늘리기/줄이기

이 코드는 증분 사용자 지정 속성의 예시입니다. 커스텀 속성의 값을 양의 정수 또는 음의 정수 값만큼 증가시킬 수 있습니다.

```brightscript
m.Braze.incrementCustomUserAttribute("intAttribute", 3)
```

### 사용자 지정 속성 설정 해제하기

사용자 지정 속성은 다음 방법을 사용하여 설정 해제할 수도 있습니다:

```brightscript
m.Braze.unsetCustomAttribute("attributeName")
```

### REST API를 통해 사용자 지정 속성 설정하기

REST API를 사용하여 사용자 속성을 설정할 수도 있습니다. 자세한 내용은 [사용자 API]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data) 설명서를 참조하세요.

### 사용자 지정 속성 값 제한

사용자 지정 속성 값의 최대 길이는 255자입니다.

## 이메일 구독 상태 관리

SDK를 통해 프로그래밍 방식으로 사용자의 이메일 가입 상태를 다음과 같이 설정할 수 있습니다.

| 구독 상태 | 정의 |
| ------------------- | ---------- |
| `OptedIn` | 가입 상태, 명시적으로 옵트인 |
| `Subscribed` | 가입 상태, 명시적으로 옵트인하지 않음 |
| `UnSubscribed` | 구독 취소 및/또는 명시적 수신 거부 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

>  이러한 유형은 `BrazeConstants().SUBSCRIPTION_STATES`에 해당합니다.

이메일 구독 상태를 설정하는 방법은 `setEmailSubscriptionState()` 입니다. 유효한 이메일 주소가 수신되면 자동으로 `Subscribed` 로 설정되지만, 명시적인 옵트인 프로세스를 설정하고 사용자의 명시적인 동의를 받은 후 이 값을 `OptedIn` 으로 설정하는 것이 좋습니다. 자세한 내용은 [사용자 가입 관리]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions)를 참조하세요.

사용 예시:
```brightscript
m.Braze.setEmailSubscriptionState(BrazeConstants().SUBSCRIPTION_STATES.OPTED_IN)
```

