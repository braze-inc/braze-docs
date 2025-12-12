---
nav_title: "구매 객체"
article_title: API 구매 개체
page_order: 8
page_type: reference
description: "이 참고 문서에서는 구매 개체의 다양한 구성 요소, 올바른 사용 방법 및 참고할 수 있는 예시를 설명합니다."

---

# 구매 객체

> 이 문서에서는 구매 개체의 다양한 구성 요소, 올바른 사용 방법, 모범 사례 및 참고할 수 있는 예시를 설명합니다.

{% multi_lang_include alerts/important_alerts.md alert='Purchase event deprecation' %}

## 구매 객체란 무엇인가요?

구매 객체는 구매가 이루어졌을 때 API를 통해 전달되는 객체입니다. 각 구매 개체는 구매 배열 내에 위치하며, 각 개체는 특정 시간에 특정 사용자가 구매한 단일 구매입니다. 구매 개체에는 사용자 지정, 데이터 수집 및 개인화를 위해 Braze 백엔드에서 이 정보를 저장하고 사용할 수 있는 다양한 필드가 있습니다.

### 개체 본문

```json
{
  // One of "external_id" or "user_alias" or "braze_id" or "email" or "phone" is required.
  "external_id" : (optional, string) External user ID,
  "user_alias" : (optional, User Alias Object) User alias object,
  "braze_id" : (optional, string) Braze user identifier,
  "email": (optional, string) User email address,
  "phone": (optional, string) User phone number,
  "app_id" : (optional, string) see App Identifier,
  // See the following product_id naming conventions for clarification.
  "product_id" : (required, string) identifier for the purchase, for example, Product Name or Product Category,
  "currency" : (required, string) ISO 4217 Alphabetic Currency Code,
  //Revenue from a purchase object is calculated as the product of quantity and price.
  "price" : (required, float) value in the base currency unit (for example, Dollars for USD, Yen for JPY),
  "quantity" : (optional, integer) the quantity purchased (defaults to 1, must be <= 100 -- currently, Braze treats a quantity _X_ as _X_ separate purchases with quantity 1),
  "time" : (required, datetime as string in ISO 8601) Time of purchase,
  // See the following purchase object explanation for clarification.
  "properties" : (optional, Properties Object) properties of the event,
  // Setting this flag to true will put the API in "Update Only" mode.
  // When using a "user_alias", "Update Only" mode is always true.
  "_update_existing_only" : (optional, boolean)
}
```

- [외부 사용자 ID]({{site.baseurl}}/api/basics/#user-ids)
- [앱 식별자]({{site.baseurl}}/api/identifier_types/)
- [ISO 4217 통화 코드 위키](http://en.wikipedia.org/wiki/ISO_4217)
- [ISO 8601 타임 코드 위키](https://en.wikipedia.org/wiki/ISO_8601)

## 제품 ID 구매

구매 개체 내에서 `product_id` 는 구매 식별자(예: `Product Name` 또는 `Product Category`)입니다:

- Braze는 대시보드에 최대 5,000개의 `product_id`초를 저장할 수 있습니다.
- `product_id` 은 최대 255자까지 입력할 수 있습니다.

### 이름 명명 규칙

Braze에서는 구매 개체에 대한 몇 가지 일반적인 이름 지정 규칙을 제공합니다 `product_id`. `product_id` 을 선택할 경우, Braze는 모든 로깅된 항목을 이 `product_id` 으로 그룹화하기 위해 SKU 대신 제품 이름 또는 제품 카테고리와 같은 간단한 이름을 사용할 것을 제안합니다.

이렇게 하면 세분화 및 트리거를 위해 제품을 쉽게 식별할 수 있습니다.

### 주문 수준에서 구매 기록

제품 수준이 아닌 주문 수준에서 구매를 기록하려면 주문 이름 또는 주문 카테고리를 `product_id` (예: `Online Order` 또는 `Completed Order`)로 사용하면 됩니다.

예를 들어 웹 SDK의 주문 수준에서 구매를 기록하려면 다음을 수행합니다.

```html
POST https://YOUR_REST_API_URL/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "purchases" : [
    {
      "external_id" : "user1",
      "app_id" : "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id" : "Completed Order",
      "currency" : "USD",
      "price" : 219.98,
      "time" : "2013-07-16T19:20:30+01:00",
      "properties" : {
        "products" : [ { "name": "Monitor", "category": "Gaming", "product_amount": 19.99, },
        { "name": "Gaming Keyboard", "category": "Gaming ", "product_amount": 199.99, }
        ]
      }
    }
  ]
}
```

## 구매 속성 개체

사용자 지정 이벤트 및 구매에는 이벤트 속성이 있을 수 있습니다. "속성" 값은 키가 속성 이름이고 값이 속성 값인 객체여야 합니다. 속성 이름은 비어 있지 않은 255자 이하의 문자열이어야 하며 선행 달러 기호가 없어야 합니다. 

속성 값은 다음 데이터 유형 중 하나를 사용할 수 있습니다.

| 데이터 유형 | 설명 |
| --- | --- |
| 숫자 | [정수](https://en.wikipedia.org/wiki/Integer) 또는 [부동 소수점](https://en.wikipedia.org/wiki/Floating-point_arithmetic) |
| 부울 |  |
| 데이터 시간 | [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 또는 `yyyy-MM-dd'T'HH:mm:ss:SSSZ` 형식의 문자열로 포맷됩니다. 배열 내에서는 지원되지 않습니다. |
| 문자열 | 255자 이하. |
| 배열 | 배열에는 날짜/시간을 포함할 수 없습니다. |
| 개체 | 오브젝트는 문자열로 수집됩니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

배열 또는 객체 값을 포함하는 이벤트 속성 객체는 최대 50KB의 이벤트 속성 페이로드를 가질 수 있습니다.

### 구매 등록정보

[구매 속성을]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events/#purchase-properties) 사용하여 메시지를 트리거하고 Liquid를 사용하여 개인화할 수 있으며, 이러한 속성을 기반으로 세분화할 수도 있습니다.

#### 이름 명명 규칙

이 기능은 구매 단위가 아닌 **제품 단위로** 설정된다는 점에 유의하세요. 예를 들어, 고유한 제품 수가 많지만 각각의 속성이 동일한 경우 세분화가 더 불필요할 수 있습니다.

이 경우 데이터 구조를 설정할 때 세분화된 제품 이름 대신 '그룹 수준'의 제품 이름을 사용하는 것이 좋습니다. 예를 들어 기차표 회사는 '거래 123' 또는 '거래 046'과 같은 특정 거래가 아닌 '단거리 여행', '왕복 여행', '다구간 여행'에 대한 상품을 보유하고 있어야 합니다. 다른 예로 '음식' 구매 이벤트의 경우 속성을 '케이크'와 '샌드위치'로 설정하는 것이 가장 좋습니다.

{% alert important %}
Braze REST API를 통해 제품을 추가할 수 있습니다. 예를 들어 `/users/track` 엔드포인트로 호출을 보내고 새 구매 ID를 포함하면 대시보드의 **데이터 설정** > **제품** 섹션에 제품이 자동으로 만들어집니다.
{% endalert %}

### 구매 개체 예시

```html
POST https://YOUR_REST_API_URL/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "purchases" : [
    {
      "external_id" : "user1",
      "app_id" : "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id" : "backpack",
      "currency" : "USD",
      "price" : 40.00,
      "time" : "2013-07-16T19:20:30+01:00",
      "properties" : {
        "color" : "red",
        "monogram" : "ABC",
        "checkout_duration" : 180,
        "size" : "Large",
        "brand" : "Backpack Locker"
      }
    },
    {
      "external_id" : "user1",
      "app_id" : "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id" : "pencil",
      "currency" : "USD",
      "price" : 2.00,
      "time" : "2013-07-17T19:20:20+01:00",
      "properties" : {
        "number" : 2,
        "sharpened" : true
      }
    },
    {
      "user_alias" : { "alias_name" : "device123", "alias_label" : "my_device_identifier"},
      "app_id" : "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id" : "pen",
      "currency" : "USD",
      "price" : 2.50,
      "time" : "2013-07-17T19:20:20+01:00",
      "properties" : {
        "color" : "blue",
      }
    }
  ]
}
```

### 구매 개체, 이벤트 개체 및 웹후크

제공된 예를 사용하면 누군가 색상, 모노그램, 결제 기간, 사이즈, 브랜드 속성을 가진 배낭을 구매했음을 알 수 있습니다. 그런 다음 [구매 이벤트 속성을]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events/#purchase-properties) 사용하여 이러한 속성을 가진 세그먼트를 만들거나 Liquid를 사용하여 채널을 통해 사용자 지정 메시지를 보낼 수 있습니다. 예를 들어, "안녕하세요 **Ann F.**, **빨간색 중형 백팩을** **$40.00에** 구매해 주셔서 감사합니다! **백팩락커에서** 쇼핑해 주셔서 감사합니다!"

세그먼트할 속성을 저장, 저장 및 추적하려면 해당 속성을 사용자 지정 속성으로 설정해야 합니다. [세그먼트 확장을]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/) 사용하면 해당 사용자 프로필의 수명 기간 동안 저장된 사용자 지정 이벤트 또는 구매 행동을 기반으로 사용자를 타겟팅할 수 있습니다.


