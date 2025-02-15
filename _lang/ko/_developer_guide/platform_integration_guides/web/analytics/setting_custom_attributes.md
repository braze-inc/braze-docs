---
nav_title: 사용자 지정 속성 설정
article_title: 웹용 사용자 지정 속성 설정
platform: Web
page_order: 3
description: "이 참조 문서에서는 웹에 대한 커스텀 속성을 할당하고 설정하는 방법을 다룹니다."

---

# 사용자 지정 속성 설정

> Braze는 사용자에게 속성을 할당하는 방법을 제공합니다. 대시보드에서 이러한 속성에 따라 사용자를 필터링하고 세분화할 수 있습니다.

구현하기 전에 [모범 사례]({{site.baseurl}}/developer_guide/platform_wide/getting_started/analytics_overview/#best-practices)에서 커스텀 이벤트, 커스텀 속성 및 구매 이벤트가 제공하는 세분화 옵션의 예제를 검토하세요.

사용자에게 속성을 할당하려면 `braze.getUser()` 메서드를 호출하여 앱의 현재 사용자에 대한 참조를 가져옵니다. 현재 사용자에 대한 참조가 있으면 메서드를 호출하여 미리 정의된 속성이나 커스텀 속성을 설정할 수 있습니다.

## 미리 정의된 사용자 속성 할당하기

Braze는 [`User` 클래스](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html) 내에서 다음 사용자 속성을 설정하기 위해 미리 정의된 메서드를 제공합니다:

- 이름
- 성
- 언어
- 국가
- 생년월일
- 이메일
- 성별
- 출생지
- 전화번호

### 구현 예시

#### 이름 설정

```javascript
braze.getUser().setFirstName("SomeFirstName");
```

#### 성별 설정

```javascript
braze.getUser().setGender(braze.User.Genders.FEMALE);
```

#### 생년월일 설정

```javascript
braze.getUser().setDateOfBirth(2000, 12, 25);
```

## 사용자 지정 사용자 속성 할당

Braze는 사전 정의된 사용자 속성 메서드 외에도 애플리케이션의 데이터를 추적할 수 있는 [커스텀 속성]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types)도 제공합니다. 

커스텀 속성에 대한 전체 메서드 사양은 여기 [JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html)에서 확인할 수 있습니다.

### 사용자 지정 속성 길이

커스텀 속성 키 및 값의 최대 길이는 255자입니다. 유효한 커스텀 속성 값에 대한 자세한 내용은 [전체 기술 설명서](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html)를 참조하세요.

### 구현 예시

#### 문자열 값으로 사용자 지정 속성 설정하기
```javascript
braze.getUser().setCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  YOUR_STRING_VALUE
);
```

#### 정수 값으로 사용자 정의 속성 설정하기
```javascript
braze.getUser().setCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  YOUR_INT_VALUE
);

// Integer attributes may also be incremented using code like the following
braze.getUser().incrementCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  THE_INTEGER_VALUE_BY_WHICH_YOU_WANT_TO_INCREMENT_THE_ATTRIBUTE
);
```

#### 날짜 값으로 사용자 지정 속성 설정하기
```javascript
braze.getUser().setCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  YOUR_DATE_VALUE
);

// This method will assign the current time to a custom attribute at the time the method is called
braze.getUser().setCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  new Date()
);

// This method will assign the date specified by secondsFromEpoch to a custom attribute
braze.getUser().setCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  new Date(secondsFromEpoch * 1000)
);
```
>  이 메서드를 통해 Braze에 전달되는 날짜는 JavaScript 날짜 객체여야 합니다.

#### 배열 값으로 사용자 정의 속성 설정하기

커스텀 속성 배열의 최대 요소 개수 기본값은 25개입니다. 개별 배열은 Braze 대시보드의 **데이터 설정** > **커스텀 속성**에서 최대 100개로 늘릴 수 있습니다. 이 최대치를 늘리려면 고객 서비스 관리자에게 문의하세요. 최대 요소 수를 초과하는 [배열은]({{site.baseurl}}/developer_guide/platform_wide/getting_started/analytics_overview/#arrays) 최대 요소 수를 포함하도록 잘립니다.

```javascript
braze.getUser().setCustomUserAttribute(YOUR_ATTRIBUTE_KEY_STRING, YOUR_ARRAY_OF_STRINGS);

// Adding a new element to a custom attribute with an array value
braze.getUser().addToCustomAttributeArray(YOUR_ATTRIBUTE_KEY_STRING, "new string");

// Removing an element from a custom attribute with an array value
braze.getUser().removeFromCustomAttributeArray(YOUR_ATTRIBUTE_KEY_STRING, "value to be removed");
```

### 사용자 지정 속성 설정 해제하기

커스텀 속성은 값을 `null`로 설정하여 해제할 수 있습니다.

```javascript
braze.getUser().setCustomUserAttribute(YOUR_ATTRIBUTE_KEY_STRING, null);
```

### REST API를 통해 사용자 지정 속성 설정하기

REST API를 사용하여 사용자 속성을 설정할 수도 있습니다. 자세한 내용은 [사용자 API]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data) 설명서를 참조하세요.

## 사용자 구독 설정하기

사용자에 대한 가입(이메일 또는 푸시)을 설정하려면 각각 `setEmailNotificationSubscriptionType()` 또는 `setPushNotificationSubscriptionType()` 함수를 호출합니다. 이 두 함수는 `enum` 유형 `braze.User.NotificationSubscriptionTypes`를 인수로 사용합니다. 이 유형에는 세 가지 상태가 있습니다:

| 구독 상태 | 정의 |
| ------------------- | ---------- |
| `braze.User.NotificationSubscriptionTypes.OPTED_IN` | 가입 상태, 명시적으로 옵트인 |
| `braze.User.NotificationSubscriptionTypes.SUBSCRIBED` | 가입 상태, 명시적으로 옵트인하지 않음 |
| `braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED` | 구독 취소 및/또는 명시적 수신 거부 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

사용자가 푸시에 등록되면 브라우저에서 알림 허용 또는 차단을 선택하도록 강제하고, 푸시 허용을 선택한 경우 기본적으로 `OPTED_IN`으로 설정됩니다. 

가입 및 명시적 옵트인 구현에 대한 자세한 내용은 [사용자 가입 관리]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions)를 참조하세요.

### 코드 예제

#### 이메일에서 사용자 구독 취소하기:
```javascript
braze.getUser().setEmailNotificationSubscriptionType(braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED);
```

#### 푸시에서 사용자 탈퇴:
```java
braze.getUser().setPushNotificationSubscriptionType(braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED);
```

