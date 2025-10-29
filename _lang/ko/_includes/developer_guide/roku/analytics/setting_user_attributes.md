{% multi_lang_include developer_guide/prerequisites/roku.md %}

## 기본 사용자 속성

### 미리 정의된 메서드

Braze는 `m.Braze` 객체를 사용하여 다음 사용자 속성을 설정하기 위한 미리 정의된 메서드를 제공합니다.

- `FirstName`
- `LastName`
- `Email`
- `Gender`
- `DateOfBirth`
- `Country`
- `Language`
- `HomeCity`
- `PhoneNumber`

### 기본 속성 설정

기본 속성을 설정하려면 `m.Braze` 객체에서 관련 메서드를 호출하십시오.

{% tabs local %}
{% tab 이름 %}
```brightscript
m.Braze.setFirstName("Alex")
```
{% endtab %}
{% tab 성 %}
```brightscript
m.Braze.setLastName("Smith")
```
{% endtab %}
{% tab 이메일 %}
```brightscript
m.Braze.setEmail("alex@example.com")
```
{% endtab %}
{% tab 성별 %}
```brightscript
m.Braze.setGender("m") ' Accepts: "m", "f", "o", "n", "u", "p"
```
{% endtab %}
{% tab 생년월일 %}
```brightscript
m.Braze.setDateOfBirth(1990, 5, 15) ' Year, month, day
```
{% endtab %}
{% tab 국가 %}
```brightscript
m.Braze.setCountry("United States")
```
{% endtab %}
{% tab 언어 %}
```brightscript
m.Braze.setLanguage("en")
```
{% endtab %}
{% tab 거주 도시 %}
```brightscript
m.Braze.setHomeCity("New York")
```
{% endtab %}
{% tab 전화번호 %}
```brightscript
m.Braze.setPhoneNumber("+1234567890")
```
{% endtab %}
{% endtabs %}

## 사용자 지정 사용자 속성

기본 사용자 속성 외에도 Braze는 여러 가지 데이터 유형을 사용하여 커스텀 속성을 정의할 수 있도록 허용합니다.

### 커스텀 속성 설정

{% tabs %}
{% tab 문자열 %}
커스텀 속성을 설정하려면 `string` 값을 사용하십시오:

```brightscript
m.Braze.setCustomAttribute("stringAttribute", "stringValue")
```
{% endtab %}

{% tab 정수 %}
`integer` 값을 사용하여 커스텀 속성을 설정하려면:

```brightscript
m.Braze.setCustomAttribute("intAttribute", 5)
```
{% endtab %}

{% tab 부동 소수점 %}
Braze는 `float` 및 `double` 값을 정확히 동일하게 처리합니다. 어떤 값으로든 커스텀 속성을 설정하려면:

```brightscript
m.Braze.setCustomAttribute("floatAttribute", 3.5)
```
{% endtab %}

{% tab 부울 %}
커스텀 속성을 `boolean` 값으로 설정하려면:

```brightscript
m.Braze.setCustomAttribute("boolAttribute", true)
```
{% endtab %}

{% tab 날짜 %}
커스텀 속성을 `date` 값으로 설정하려면:

```brightscript
dateAttribute = CreateObject("roDateTime")
dateAttribute.fromISO8601String("1992-11-29 00:00:00.000")
m.Braze.setCustomAttribute("dateAttribute", dateAttribute)
```
{% endtab %}

{% tab 배열 %}
`array` 값을 사용하여 커스텀 속성을 설정하려면:

```brightscript
stringArray = createObject("roArray", 3, true)
stringArray.Push("string1")
stringArray.Push("string2")
stringArray.Push("string3")
m.Braze.setCustomAttribute("arrayAttribute", stringArray)
```
{% endtab %}
{% endtabs %}

{% alert important %}
커스텀 속성 값의 최대 길이는 255자이며, 이보다 긴 값은 잘립니다.
{% endalert %}

### 커스텀 속성을 증가 및 감소시키기

이 코드는 증분 사용자 지정 속성의 예시입니다. 커스텀 속성의 값을 양수 또는 음수의 정수 값만큼 증가시킬 수 있습니다.

```brightscript
m.Braze.incrementCustomUserAttribute("intAttribute", 3)
```

### 커스텀 속성을 해제하기

커스텀 속성을 해제하려면, 관련 속성 키를 `unsetCustomAttribute` 메서드에 전달하십시오.

```brightscript
m.Braze.unsetCustomAttribute("attributeName")
```

### REST API 사용

사용자 속성을 설정하거나 해제하기 위해 REST API를 사용할 수도 있습니다. 자세한 정보는 [사용자 데이터 엔드포인트]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data)를 참조하십시오.

## 이메일 구독 설정

SDK를 통해 프로그래밍 방식으로 사용자의 이메일 가입 상태를 다음과 같이 설정할 수 있습니다.

| 구독 상태 | 정의 |
| ------------------- | ---------- |
| `OptedIn` | 구독하고 명시적으로 동의한 경우 |
| `Subscribed` | 구독 중이지만 명시적으로 옵트인하지 않은 경우 |
| `UnSubscribed` | 구독 취소 및/또는 명시적 수신 거부 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
이러한 유형은 `BrazeConstants().SUBSCRIPTION_STATES`에 해당합니다.
{% endalert %}

이메일 구독 상태를 설정하는 방법은 `setEmailSubscriptionState()` 입니다. 유효한 이메일 주소가 수신되면 자동으로 `Subscribed` 로 설정되지만, 명시적인 옵트인 프로세스를 설정하고 사용자의 명시적인 동의를 받은 후 이 값을 `OptedIn` 으로 설정하는 것이 좋습니다. 자세한 내용은 [사용자 가입 관리]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions)를 참조하세요.

```brightscript
m.Braze.setEmailSubscriptionState(BrazeConstants().SUBSCRIPTION_STATES.OPTED_IN)
```
