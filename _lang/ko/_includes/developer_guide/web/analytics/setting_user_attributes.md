{% multi_lang_include developer_guide/prerequisites/web.md %}

## 기본 사용자 속성

### 미리 정의된 메서드

Braze는 [`User` 클래스](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html) 내에서 다음 사용자 속성을 설정하기 위해 미리 정의된 메서드를 제공합니다:

- 이름
- Last Name
- 언어
- 국가
- 생년월일
- 이메일
- 성별
- 출생지
- 전화번호

### 기본 속성 설정

{% tabs %}
{% tab 메서드 사용 %}
사용자에 대한 기본 속성을 설정하려면, Braze 인스턴스에서 `getUser()` 메서드를 호출하여 앱의 현재 사용자에 대한 참조를 가져옵니다. 그런 다음 사용자 속성을 설정하기 위해 메서드를 호출할 수 있습니다.

{% subtabs local %}
{% subtab First name %}
```javascript
braze.getUser().setFirstName("SomeFirstName");
```
{% endsubtab %}
{% subtab Gender %}
```javascript
braze.getUser().setGender(braze.User.Genders.FEMALE);
```
{% endsubtab %}
{% subtab Date of birth %}
```javascript
braze.getUser().setDateOfBirth(2000, 12, 25);
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Google 태그 관리자 %}
Google Tag Manager를 사용하여 표준 사용자 속성(예: 사용자의 이름)은 커스텀 사용자 속성과 동일한 방식으로 기록되어야 합니다. 표준 속성으로 전달하는 값이 [사용자 클래스](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html) 문서에 지정된 예상 형식과 일치하는지 확인합니다.

예를 들어 성별 속성은 다음 중 하나를 값으로 사용할 수 있습니다. `"m" | "f" | "o" | "u" | "n" | "p"`. 따라서 사용자의 성별을 여성으로 설정하려면 다음 내용으로 사용자 지정 HTML 태그를 만드세요:

```html
<script>
window.braze.getUser().setGender("f")
</script>
```
{% endtab %}
{% endtabs %}

### 기본 속성 해제

기본 사용자 속성을 해제하려면 관련 메서드에 `null`을 전달합니다. For example:

{% tabs local %}
{% tab 이름 %}
```javascript
braze.getUser().setFirstName(null);
```
{% endtab %}
{% tab 성별 %}
```javascript
braze.getUser().setGender(null);
```
{% endtab %}
{% tab 생년월일 %}
```javascript
braze.getUser().setDateOfBirth(null, null, null);
```
{% endtab %}
{% endtabs %}

## 사용자 지정 사용자 속성

### 사용자 지정 속성 설정

{% tabs %}
{% tab 메서드 사용 %}
기본 사용자 속성 메서드 외에도 사용자에 대해 [커스텀 속성]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types)을 설정할 수 있습니다. 전체 메서드 사양은 [우리 JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html)를 참조하세요.

{% subtabs local %}
{% subtab String %}
`string` 값으로 커스텀 속성을 설정하려면:

```javascript
braze.getUser().setCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  YOUR_STRING_VALUE
);
```

{% endsubtab %}
{% subtab Integer %}
`integer` 값으로 커스텀 속성을 설정하려면:

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

{% endsubtab %}
{% subtab Date %}
`date` 값으로 커스텀 속성을 설정하려면:

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

{% endsubtab %}
{% subtab Array %}

커스텀 속성 배열에는 최대 25개의 요소를 가질 수 있습니다. 수동으로 설정된 개별 배열(자동으로 감지되지 않음)은 Braze 대시보드의 **데이터 유형** 아래 **데이터 설정** > **커스텀 속성**에서 최대 100으로 증가할 수 있습니다. 이 최대치를 늘리고 싶다면 Braze 계정 매니저에게 문의하세요.

최대 요소 수를 초과하는 [배열은]({{site.baseurl}}/developer_guide/platform_wide/getting_started/analytics_overview/#arrays) 최대 요소 수를 포함하도록 잘립니다.

`array` 값으로 커스텀 속성을 설정하려면:

```javascript
braze.getUser().setCustomUserAttribute(YOUR_ATTRIBUTE_KEY_STRING, YOUR_ARRAY_OF_STRINGS);

// Adding a new element to a custom attribute with an array value
braze.getUser().addToCustomAttributeArray(YOUR_ATTRIBUTE_KEY_STRING, "new string");

// Removing an element from a custom attribute with an array value
braze.getUser().removeFromCustomAttributeArray(YOUR_ATTRIBUTE_KEY_STRING, "value to be removed");
```

{% alert important %}
이 메서드를 통해 Braze에 전달되는 날짜는 JavaScript 날짜 객체여야 합니다.
{% endalert %}
{% endsubtab %}
{% endsubtabs %}

{% alert important %}
커스텀 속성 키와 값은 최대 255자만 가질 수 있습니다. 유효한 커스텀 속성 값에 대한 자세한 내용은 [참조 설명서](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html)를 참조하십시오.
{% endalert %}
{% endtab %}

{% tab Google 태그 관리자 %}
Google 태그 관리자의 스크립팅 언어 제한으로 인해 사용자 지정 사용자 속성을 사용할 수 없습니다. 사용자 지정 속성을 기록하려면 다음 내용으로 사용자 지정 HTML 태그를 만듭니다:

```html
<script>
  // Note: If using SDK version 3.x or below, use `window.appboy` instead of `window.braze`
  // Version 4 or greater should use `window.braze`
window.braze.getUser().setCustomUserAttribute("attribute name", "attribute value");
</script>
```

{% alert important %}
GTM 템플릿은 이벤트 또는 구매에 중첩된 속성을 지원하지 않습니다. 앞의 HTML을 사용하여 중첩된 속성이 필요한 이벤트 또는 구매를 기록할 수 있습니다.
{% endalert %}
{% endtab %}
{% endtabs %}

### 커스텀 속성 해제

커스텀 속성을 해제하려면 관련 메서드에 `null`을(를) 전달하십시오.

```javascript
braze.getUser().setCustomUserAttribute(YOUR_ATTRIBUTE_KEY_STRING, null);
```

### 커스텀 속성 중첩

커스텀 속성 내에서 속성을 중첩할 수도 있습니다. 다음 예제에서는 중첩 속성이 있는 `favorite_book` 객체가 사용자 프로필의 커스텀 속성으로 설정됩니다. 자세한 내용은 [중첩 커스텀 속성]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support)를 참조하십시오.

```javascript
import * as braze from "@braze/web-sdk";

const favoriteBook = {
  title: "The Hobbit",
  author: "J.R.R. Tolkien",
  publishing_date: "1937"
};

braze.getUser().setCustomUserAttribute("favorite_book", favoriteBook);
```

### REST API 사용

REST API를 사용하여 사용자 속성을 설정하거나 해제할 수도 있습니다. 자세한 정보는 [사용자 데이터 엔드포인트]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data)를 참조하십시오.

## 사용자 구독 설정

사용자에 대한 가입(이메일 또는 푸시)을 설정하려면 각각 `setEmailNotificationSubscriptionType()` 또는 `setPushNotificationSubscriptionType()` 함수를 호출합니다. 두 함수 모두 `enum` 유형 `braze.User.NotificationSubscriptionTypes`을(를) 인수로 사용합니다. 이 유형에는 세 가지 상태가 있습니다:

| 구독 상태 | 정의 |
| ------------------- | ---------- |
| `braze.User.NotificationSubscriptionTypes.OPTED_IN` | 구독하고 명시적으로 동의한 경우 |
| `braze.User.NotificationSubscriptionTypes.SUBSCRIBED` | 구독 중이지만 명시적으로 옵트인하지 않은 경우 |
| `braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED` | 구독 취소 및/또는 명시적 수신 거부 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

사용자가 푸시에 등록되면 브라우저에서 알림 허용 또는 차단을 선택하도록 강제하고, 푸시 허용을 선택한 경우 기본적으로 `OPTED_IN`으로 설정됩니다. 

가입 및 명시적 옵트인 구현에 대한 자세한 내용은 [사용자 가입 관리]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions)를 참조하세요.

### 사용자를 이메일 구독 해지

```javascript
braze.getUser().setEmailNotificationSubscriptionType(braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED);
```

### 사용자를 푸시 구독 해지

```java
braze.getUser().setPushNotificationSubscriptionType(braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED);
```
