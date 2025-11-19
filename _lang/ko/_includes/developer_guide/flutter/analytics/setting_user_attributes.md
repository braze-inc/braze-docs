{% multi_lang_include developer_guide/prerequisites/flutter.md %}

## 기본 사용자 속성

### Supported attributes

지원되는 속성은 다음과 같습니다:

- 이름
- 성
- 성별
- 생년월일
- 출생지
- 국가
- 전화번호
- 언어
- Email

{% alert important %}
이름과 성, 국가, 출생지와 같은 모든 문자열 값은 255자로 제한됩니다.
{% endalert %}

### 기본 속성 설정하기 

Braze에서 자동으로 수집한 사용자 속성을 설정하려면 소프트웨어 개발 키트에 포함된 세터 메서드를 사용할 수 있습니다.

```dart
braze.setFirstName('Name');
```

## 사용자 지정 사용자 속성

### 사용자 지정 속성 설정

기본 사용자 속성 외에도 Braze에서는 다양한 데이터 유형을 사용하여 커스텀 속성을 정의할 수 있습니다:

{% tabs %}
{% tab 문자열 %}
`string` 값으로 커스텀 속성을 설정하려면 다음과 같이 하세요:

```dart
braze.setStringCustomUserAttribute("custom string attribute", "string custom attribute");
```

{% endtab %}
{% tab 정수 %}
`integer` 값으로 커스텀 속성을 설정하려면 다음과 같이 하세요:

```dart
// Set Integer Attribute
braze.setIntCustomUserAttribute("custom int attribute key", integer);
// Increment Integer Attribute
braze.incrementCustomUserAttribute("key", integer);
```

{% endtab %}
{% tab Double %}
`double` 값으로 커스텀 속성을 설정하려면 다음과 같이 하세요:

```dart
braze.setDoubleCustomUserAttribute("custom double attribute key", double);
```

{% endtab %}
{% tab 부울 %}
`boolean` 값으로 커스텀 속성을 설정하려면 다음과 같이 하세요:

```dart
braze.setBoolCustomUserAttribute("custom boolean attribute key", boolean);
```
{% endtab %}

{% tab 날짜 %}
`date` 값으로 커스텀 속성을 설정하려면 다음과 같이 하세요:

```dart
braze.setDateCustomUserAttribute("custom date attribute key", date);
```
{% endtab %}
{% tab 배열 %}
`array` 값으로 커스텀 속성을 설정하려면 다음과 같이 하세요:

```dart
// Adding to an Array
braze.addToCustomAttributeArray("key", "attribute");
// Removing an item from an Array
braze.removeFromCustomAttributeArray("key", "attribute");
```
{% endtab %}
{% endtabs %}

{% alert important %}
커스텀 속성 값의 최대 길이는 255자이며, 이보다 긴 값은 잘립니다.
{% endalert %}

### 커스텀 속성 설정 해제하기

커스텀 속성을 설정 해제하려면 관련 속성 키를 `unsetCustomUserAttribute` 메서드에 전달하세요.

```dart
braze.unsetCustomUserAttribute('attribute_key');
```
