---
nav_title: 분석
article_title: Flutter용 애널리틱스
platform: Flutter
page_order: 5
description: "이 문서에서는 Flutter 앱에서 기본 분석을 설정하고 추적하는 방법에 대해 설명합니다."

---
 
# Flutter 분석

> 이 문서에서는 Flutter 앱에서 기본 분석을 설정하고 추적하는 방법에 대해 설명합니다.

시작하기 전에 [애널리틱스 개요]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/) 문서를 읽고 Braze 애널리틱스와 기본으로 추적되는 항목에 대해 자세히 알아보세요. 또한 [이벤트 이름 지정 규칙을]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/) 숙지하는 것이 좋습니다.

## 세션 추적

Braze SDK는 사용자 인게이지먼트를 계산하기 위해 Braze 대시보드에서 사용하는 세션 데이터 및 사용자를 이해하는 데 핵심적인 기타 분석을 보고합니다. SDK는 다음 세션 의미 체계에 따라 Braze 대시보드 내에서 볼 수 있는 세션 길이와 세션 수를 설명하는 '세션 시작' 및 '세션 종료' 데이터 포인트를 생성합니다.

사용자 ID를 설정하거나 세션을 시작하려면 사용자 ID 매개변수를 받는 `changeUser` 메서드를 사용합니다.

```dart
braze.changeUser('user_id');
```

## 사용자 지정 이벤트 로깅

Braze에서 커스텀 이벤트를 기록하여 앱의 사용 패턴에 대해 자세히 알아보고 대시보드에서 사용자의 작업에 따라 사용자를 세분화할 수 있습니다.

```dart
braze.logCustomEvent('my_custom_event');
```

사용자 지정 이벤트와 함께 속성 개체를 전달하여 이벤트에 대한 메타데이터를 추가할 수 있습니다.

```dart
braze.logCustomEvent('custom_event_with_properties', properties: {
    'key1': 'value1',
    'key2': ['value2', 'value3'],
    'key3': false,
});
```

## 사용자 지정 속성 로깅

Braze는 사용자에게 속성을 할당하는 방법을 제공합니다. 대시보드에서 이러한 속성에 따라 사용자를 필터링하고 세분화할 수 있습니다.

### 기본 사용자 속성

Braze에서 자동으로 수집한 사용자 속성을 할당하려면 SDK와 함께 제공되는 setter 메서드를 사용할 수 있습니다.

```dart
braze.setFirstName('Name');
```

지원되는 속성은 다음과 같습니다:

- 이름
- 성
- 성별
- 생년월일
- 출생지
- 국가
- 전화번호
- 언어
- 이메일

이름과 성, 국가, 출생지와 같은 모든 문자열 값은 255자로 제한됩니다.

### 사용자 지정 속성 값 설정

기본 사용자 속성 외에도 Braze에서는 여러 가지 데이터 유형을 사용하여 커스텀 속성을 정의할 수 있습니다.

{% tabs %}
{% tab 부울 값 %}

```dart
braze.setBoolCustomUserAttribute("custom boolean attribute key", boolean);
```

{% endtab %}
{% tab 정수 %}

```dart
// Set Integer Attribute
braze.setIntCustomUserAttribute("custom int attribute key", integer);
// Increment Integer Attribute
braze.incrementCustomUserAttribute("key", integer);
```

{% endtab %}
{% tab Double %}
```dart
braze.setDoubleCustomUserAttribute("custom double attribute key", double);
```

{% endtab %}
{% tab 문자열 %}

```dart
braze.setStringCustomUserAttribute("custom string attribute", "string custom attribute");
```

{% endtab %}
{% tab 날짜 %}

```dart
braze.setDateCustomUserAttribute("custom date attribute key", date);
```
{% endtab %}
{% tab 배열 %}

```dart
// Adding to an Array
braze.addToCustomAttributeArray("key", "attribute");
// Removing an item from an Array
braze.removeFromCustomAttributeArray("key", "attribute");
```
{% endtab %}
{% endtabs %}

### 사용자 지정 속성 설정 해제하기

```dart
braze.unsetCustomUserAttribute('attribute_key');
```

## 구매 기록

인앱 구매를 기록하면 여러 매출원에서 시간 경과에 따른 매출을 추적하고 생애주기 가치에 따라 사용자를 세분화할 수 있습니다.

Braze는 여러 통화로 구매를 지원합니다. USD가 아닌 다른 통화로 신고한 구매는 신고한 날짜의 환율을 기준으로 대시보드에 USD로 표시됩니다.

```dart
braze.logPurchase(productId, currencyCode, price, quantity, properties: properties);
```

예를 들어, 다음과 같습니다.

```dart
braze.logPurchase('product_id', 'USD', 9.99, 1, properties: {
    'key1': 'value'
});
```

{% alert tip %}
`10 USD`의 가격과 `3`개의 수량을 전달하면 고객 프로필에 10 USD 항목의 3번 구매로 총 30 USD가 기록됩니다. 수량은 100보다 작거나 같아야 합니다. 구매 금액은 음수일 수 있습니다.
{% endalert %}

### 주문 수준에서 구매 기록
제품 수준 대신 주문 수준에서 구매를 기록하려면 주문 이름 또는 주문 카테고리를 `product_id` 으로 사용하면 됩니다. 자세한 내용은 [구매 개체 사양을]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions) 참조하세요. 

### 예약 키

다음 키는 예약되어 있으며 구매 속성으로 사용할 수 없습니다:

- `time`
- `product_id`
- `quantity`
- `event_name`
- `price`
- `currency`

