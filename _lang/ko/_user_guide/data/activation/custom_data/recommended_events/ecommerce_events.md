---
nav_title: 전자상거래 추천 이벤트
article_title: 전자상거래 추천 이벤트
page_type: reference
alias: /ecommerce_events/
toc_headers: h2
description: "이 참조 문서에서는 전자상거래 추천 이벤트 및 속성, 사용법, 세분화, 관련 분석 보기 방법 등을 설명합니다."
---

# 전자상거래 추천 이벤트

> 이 페이지에서는 전자상거래 추천 이벤트 및 속성을 다룹니다. 이 이벤트는 마케터가 효과적인 메시지를 트리거하는 데 필요한 주요 쇼핑 행동을 포착하기 위해 생성되었습니다. 예를 들어, 장바구니 포기를 타겟팅하는 것입니다.

{% alert important %}
전자상거래 추천 이벤트는 현재 초기 액세스 중입니다. 이 초기 액세스에 참여하고 싶다면 Braze 고객 성공 관리자에게 문의하세요. <br><br>새로운 [Shopify 커넥터]({{site.baseurl}}/partners/ecommerce/shopify/multiple_stores/?tab=shopify%20connector)를 사용하고 있다면, 이 추천 이벤트는 통합을 통해 자동으로 사용할 수 있습니다.
{% endalert %}

Braze는 데이터 계획에 시간이 걸린다는 것을 인식하고 있습니다. 고객이 개발 팀을 익숙하게 하고 지금 이 이벤트를 보내기 시작할 것을 권장합니다. 전자상거래 추천 이벤트와 함께 일부 기능이 즉시 제공되지 않을 수 있지만, 2025년 동안 전자상거래 기능을 향상시킬 새로운 제품의 도입을 기대할 수 있습니다.

## 전자상거래 추천 이벤트의 유형

{% multi_lang_include alerts/important_alerts.md alert='Purchase event deprecation' %}

보고된 모든 비 USD 통화는 보고된 날짜의 환율에 따라 Braze에서 USD로 표시됩니다. 통화 변환을 방지하려면 통화를 USD로 하드코딩하세요.

{% tabs %}
{% tab ecommerce.product_viewed %}

고객이 제품 상세 페이지를 볼 때 트리거되도록 제품 조회 이벤트를 사용할 수 있습니다.

#### 속성

| 속성 이름 | 필수 | 데이터 유형 | 설명 | 
|---|---|---|---|
| `product_id` | 예 | 문자열 | 조회된 제품의 고유 식별자입니다. <br> 비-Shopify 고객의 경우, 이는 SKU와 같은 카탈로그 항목 ID에 대해 설정한 값입니다. |
| `product_name` | 예 | 문자열 | 조회된 제품의 이름입니다. | 
| `variant_id` | 예 | 문자열 | 제품 변형의 고유 식별자입니다. 예: `shirt_medium_blue` |
| `image_url` | 아니요 | 문자열 | 제품 이미지의 URL입니다. |
| `product_url` | 아니요 | 문자열 | 자세한 내용을 위한 제품 페이지의 URL입니다. |
| `price` | 예 | 부동 | 조회 시 제품의 변형 단가입니다. |
| `currency` | 예 | 문자열 | 제품 가격이 나열된 통화(예: "USD" 또는 "EUR")는 [ISO 4217 형식](https://www.iso.org/iso-4217-currency-codes.html)입니다. |
| `source` | 예 | 문자열 | 이벤트가 유래된 출처입니다. (Shopify의 경우, 이는 매장입니다). |
| `metadata` | 아니요 | 객체 | |
| `type` | 아니요 | 객체 | [재고 알림]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications) 및 [가격 인하 알림]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/price_drop_notifications)와 함께 작동합니다. |
| `sku` | 아니요 | 문자열 | (Shopify 전용) Shopify SKU. 이것은 카탈로그 ID 필드로 구성할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### 예제 객체들

{% subtabs %}
{% subtab Web SDK %}

```javascript
braze.logCustomEvent("ecommerce.product_viewed", {
    "product_id": "4111176",
    "product_name": "Torchie runners",
    "variant_id": "4111176700",
    "image_url": "https://braze-apparel.com/images/products/large/torchie-runners.jpg",
    "product_url": "https://braze-apparel.com/footwear-categories/sneakers/braze-orange-torchie-runners/",
    "price": 85,
    "currency": "GBP",
    "source": "https://braze-apparel.com/",
    "metadata": {
        "sku": "",
        "color": "ORANGE",
        "size": "6",
        "brand": "Braze"
    }
});
```

{% endsubtab %}
{% subtab Android SDK %}

```java
BrazeProperties properties = new BrazeProperties()
    .addProperty("product_id", "4111176")
    .addProperty("product_name", "Torchie runners")
    .addProperty("variant_id", "4111176700")
    .addProperty("image_url", "https://braze-apparel.com/images/products/large/torchie-runners.jpg")
    .addProperty("product_url", "https://braze-apparel.com/footwear-categories/sneakers/braze-orange-torchie-runners/")
    .addProperty("price", 85)
    .addProperty("currency", "GBP")
    .addProperty("source", "https://braze-apparel.com/")
    .addProperty("metadata", new JSONObject()
        .put("sku", "")
        .put("color", "ORANGE")
        .put("size", "6")
        .put("brand", "Braze"));

Braze.getInstance(context).logCustomEvent("ecommerce.product_viewed", properties);
```

{% endsubtab %}
{% subtab Swift SDK %}

```swift
let properties: [String: Any] = [
    "product_id": "4111176",
    "product_name": "Torchie runners",
    "variant_id": "4111176700",
    "image_url": "https://braze-apparel.com/images/products/large/torchie-runners.jpg",
    "product_url": "https://braze-apparel.com/footwear-categories/sneakers/braze-orange-torchie-runners/",
    "price": 85,
    "currency": "GBP",
    "source": "https://braze-apparel.com/",
    "metadata": [
        "sku": "",
        "color": "ORANGE",
        "size": "6",
        "brand": "Braze"
    ]
]

AppDelegate.braze?.logCustomEvent(name: "ecommerce.product_viewed", properties: properties)
```

{% endsubtab %}
{% subtab API Payload %}

```json
{
  "events": [
    {
      "external_id": "user_id",
      "app_id": "your_app_identifier",
      "name": "ecommerce.product_viewed",
      "time": "2024-01-15T09:03:45Z",
      "properties": {
        "product_id": "4111176",
        "product_name": "Torchie runners",
        "variant_id": "4111176700",
        "image_url": "https://braze-apparel.com/images/products/large/torchie-runners.jpg",
        "product_url": "https://braze-apparel.com/footwear-categories/sneakers/braze-orange-torchie-runners/",
        "price": 85,
        "currency": "GBP",
        "source": "https://braze-apparel.com/",
        "metadata": {
          "sku": "",
          "color": "ORANGE",
          "size": "6",
          "brand": "Braze"
        }
        "type": [
          "price_drop",
          "back_in_stock"
        ]
      }
    }
  ]
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab ecommerce.cart_updated %}

장바구니에 제품이 추가, 제거 또는 업데이트될 때 추적하기 위해 장바구니 업데이트 이벤트를 사용할 수 있습니다. `ecommerce.cart_updated` 이벤트는 트리거되기 전에 다음 정보를 확인합니다:

- 이벤트 시간은 사용자의 특정 장바구니에 대한 `updated_at` 시간보다 커야 합니다.
- 장바구니가 체크아웃 프로세스로 진행되지 않았습니다.
- `products` 배열이 비어 있지 않습니다.

#### 장바구니 매핑 객체

`ecommerce.cart_updated` 이벤트에는 장바구니 매핑 객체가 있습니다. 이 객체는 쇼핑객의 장바구니에 있는 모든 제품을 포함하는 장바구니의 매핑을 포함하는 사용자 프로필을 위해 생성됩니다. Liquid 태그를 통해 쇼핑 카트의 제품에 접근할 수 있습니다: 

{%raw%}
```liquid
{% shopping_cart {{context_properties.${cart_id}}} %}
{% for item in shopping_cart.products %}
{% catalog_items <add_your_catalog> {{item.variant_id}} %}
```
{%endraw%}

장바구니가 업데이트되지 않고 10일 이내에 주문이 진행되지 않으면 장바구니와 관련된 제품을 삭제합니다.

{% alert note %}
Braze에서는 장바구니당 제품 수에 제한이 없습니다. 그러나 Shopify의 제한은 500개입니다.
{% endalert %}

#### 사용자 프로필 병합 시 장바구니 동작

장바구니가 두 개 있는 경우, 두 개 모두 병합된 사용자에게 추가합니다. 가장 최근의 장바구니 정보를 포함하여 메시지를 보내기 위해 동일하거나 다른 장바구니일 경우 Canvas를 다시 큐에 추가합니다. `ecommerce.cart_updated` 이벤트는 최신 장바구니 ID와 장바구니의 최신 제품을 포함합니다.

#### 속성

| 속성 이름 | 필수 | 데이터 유형 | 설명 | 
|---|---|---|---|
| `cart_id` | 예 | 문자열 | 장바구니의 고유 식별자입니다. 값이 전달되지 않으면, 사용자 장바구니 매핑을 위해 기본값(장바구니, 체크아웃 및 주문 이벤트에서 공유됨)을 결정합니다. |
| `total_value` | 예 | 부동 | 장바구니의 총 금전적 가치입니다. | 
| `currency` | 예 | 문자열 | 제품 가격이 나열된 통화(예: "USD" 또는 "EUR")는 [ISO 4217 형식](https://www.iso.org/iso-4217-currency-codes.html)입니다. |
| `products` | 예 | 배열 |  |
| `product_id` | 예 | 문자열 | 조회된 제품의 고유 식별자입니다. <br> 이 값은 제품 ID 또는 SKU일 수 있습니다. |
| `product_name` | 예 | 문자열 | 조회된 제품의 이름입니다. |
| `variant_id` | 예 | 문자열 | 제품 변형의 고유 식별자입니다. 예: `shirt_medium_blue` |
| `image_url` | 아니요 | 문자열 | 제품 이미지의 URL입니다. |
| `product_url` | 아니요 | 문자열 | 자세한 내용을 위한 제품 페이지의 URL입니다. |
| `quantity` | 예 | 정수 | 장바구니에 있는 제품의 수량입니다. |
| `price` | 예 | 부동 | 조회 시 제품의 변형 단가입니다. |
| `metadata` | 아니요 | 객체 | 고객이 자신의 사용 사례를 위해 추가하고자 하는 제품에 대한 추가 메타데이터 필드입니다. Shopify의 경우, SKU를 추가할 것입니다. <br> 이것은 50kb의 일반 이벤트 속성 한도에 따라 제한이 있습니다. |
| `sku` | 아니요 | 문자열 | (Shopify 전용) Shopify SKU. 이것은 카탈로그 ID 필드로 구성할 수 있습니다. |
| `source` | 예 | 문자열 | 이벤트가 유래된 출처입니다. (Shopify의 경우, 이는 매장입니다). |
| `metadata` | 아니요 | 객체 | 고객이 자신의 사용 사례를 위해 추가하고자 하는 제품에 대한 추가 메타데이터 필드입니다. Shopify의 경우, SKU를 추가할 것입니다. <br> 이것은 50kb의 일반 이벤트 속성 한도에 따라 제한이 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### 예제 객체들

{% subtabs %}
{% subtab Web SDK %}

```javascript
braze.logCustomEvent("ecommerce.cart_updated", {
    "cart_id": "cart_12345",
    "currency": "USD",
    "total_value": 199.98,
    "products": [
        {
            "product_id": "8266836345064",
            "product_name": "Classic T-Shirt",
            "variant_id": "44610569208040",
            "image_url": "https://braze-apparel.com/images/tshirt-blue-medium.jpg",
            "product_url": "https://braze-apparel.com/products/classic-tshirt?variant=44610569208040",
            "quantity": 2,
            "price": 99.99,
            "metadata": {
                "sku": "TSH-BLU-M",
                "color": "BLUE",
                "size": "Medium",
                "brand": "Braze"
            }
        }
    ],
    "source": "https://braze-apparel.com",
    "metadata": {}
});
```

{% endsubtab %}
{% subtab Android SDK %}

```java
JSONArray products = new JSONArray();
JSONObject product = new JSONObject()
    .put("product_id", "8266836345064")
    .put("product_name", "Classic T-Shirt")
    .put("variant_id", "44610569208040")
    .put("image_url", "https://braze-apparel.com/images/tshirt-blue-medium.jpg")
    .put("product_url", "https://braze-apparel.com/products/classic-tshirt?variant=44610569208040")
    .put("quantity", 2)
    .put("price", 99.99)
    .put("metadata", new JSONObject()
        .put("sku", "TSH-BLU-M")
        .put("color", "BLUE")
        .put("size", "Medium")
        .put("brand", "Braze"));
products.put(product);

BrazeProperties properties = new BrazeProperties()
    .addProperty("cart_id", "cart_12345")
    .addProperty("currency", "USD")
    .addProperty("total_value", 199.98)
    .addProperty("products", products)
    .addProperty("source", "https://braze-apparel.com")
    .addProperty("metadata", new JSONObject());

Braze.getInstance(context).logCustomEvent("ecommerce.cart_updated", properties);
```

{% endsubtab %}
{% subtab Swift SDK %}

```swift
let products: [[String: Any]] = [
    [
        "product_id": "8266836345064",
        "product_name": "Classic T-Shirt",
        "variant_id": "44610569208040",
        "image_url": "https://braze-apparel.com/images/tshirt-blue-medium.jpg",
        "product_url": "https://braze-apparel.com/products/classic-tshirt?variant=44610569208040",
        "quantity": 2,
        "price": 99.99,
        "metadata": [
            "sku": "TSH-BLU-M",
            "color": "BLUE",
            "size": "Medium",
            "brand": "Braze"
        ]
    ]
]

let properties: [String: Any] = [
    "cart_id": "cart_12345",
    "currency": "USD",
    "total_value": 199.98,
    "products": products,
    "source": "https://braze-apparel.com",
    "metadata": [:]
]

AppDelegate.braze?.logCustomEvent(name: "ecommerce.cart_updated", properties: properties)
```

{% endsubtab %}
{% subtab API Payload %}

```json
{
  "events": [
    {
      "external_id": "user_id",
      "app_id": "your_app_identifier",
      "name": "ecommerce.cart_updated",
      "time": "2024-01-15T09:15:30Z",
      "properties": {
        "cart_id": "cart_12345",
        "currency": "USD",
        "total_value": 199.98,
        "products": [
          {
            "product_id": "8266836345064",
            "product_name": "Classic T-Shirt",
            "variant_id": "44610569208040",
            "image_url": "https://braze-apparel.com/images/tshirt-blue-medium.jpg",
            "product_url": "https://braze-apparel.com/products/classic-tshirt?variant=44610569208040",
            "quantity": 2,
            "price": 99.99,
            "metadata": {
              "sku": "TSH-BLU-M",
              "color": "BLUE",
              "size": "Medium",
              "brand": "Braze"
            }
          }
        ],
        "source": "https://braze-apparel.com",
        "metadata": {}
      }
    }
  ]
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab ecommerce.checkout_started %}

주문을 하지 않은 체크아웃 프로세스를 시작한 고객을 재타겟팅하기 위해 체크아웃 시작 이벤트를 사용할 수 있습니다.

`ecommerce.cart_updated` 이벤트와 유사하게, 이 이벤트는 장바구니 내의 모든 제품에 접근하기 위해 쇼핑 카트 Liquid 태그를 활용할 수 있게 해줍니다. 포기된 체크아웃 메시지에 사용됩니다:

{%raw%}
```liquid
{% shopping_cart {{context_properties.${cart_id}}} :abort_if_not_abandoned false %}
{% for item in shopping_cart.products %}
{% catalog_items <add_your_catalog> {{item.variant_id}} %}
```
{%endraw%}

#### 속성

| 속성 이름 | 필수 | 데이터 유형 | 설명 | 
|---|---|---|---|
| `checkout_id` | 예 | 문자열 | 체크아웃의 고유 식별자입니다. |
| `cart_id` | 아니요 | 문자열 | 장바구니의 고유 식별자입니다. 값이 전달되지 않으면, 사용자 장바구니 매핑을 위해 기본값(장바구니, 체크아웃 및 주문 이벤트에서 공유됨)을 결정합니다. | 
| `total_value` | 예 | 부동 | 장바구니의 총 금전적 가치입니다. |
| `currency` | 예 | 문자열 | 장바구니의 가치가 평가되는 통화입니다. |
| `products` | 예 | 객체 배열 |  |
| `product_id` | 예 | 문자열 | 조회된 제품의 고유 식별자입니다. 예를 들어, 이 값은 제품 ID 또는 SKU일 수 있습니다. |
| `product_name` | 예 | 문자열 | 조회된 제품의 이름입니다.  |
| `variant_id` | 예 | 문자열 | 제품 변형의 고유 식별자입니다. 예: `shirt_medium_blue` |
| `image_url` | 아니요 | 문자열 | 제품 이미지의 URL입니다. |
| `product_url` | 아니요 | 문자열 | 자세한 내용을 위한 제품 페이지의 URL입니다. |
| `quantity` | 예 | 정수 | 장바구니에 있는 제품의 수량입니다. |
| `price` | 예 | 부동 | 조회 시 제품의 변형 단가입니다. |
| `metadata` | 아니요 | 객체 | 고객이 자신의 사용 사례를 위해 추가하고자 하는 제품에 대한 추가 메타데이터 필드입니다. Shopify의 경우, SKU를 추가할 것입니다. <br> 이것은 50kb의 일반 이벤트 속성 한도에 따라 제한이 있습니다. |
| `sku` | 아니요 | 문자열 | (Shopify 전용) Shopify SKU. 이것은 카탈로그 ID 필드로 구성할 수 있습니다. |
| `source` | 예 | 문자열 | 이벤트가 유래된 출처입니다. (Shopify의 경우, 이는 매장입니다). |
| `metadata` | 아니요 | 객체 |  |
| `checkout_url` | 아니요 | 문자열 | 체크아웃 페이지의 URL입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### 예제 객체들

{% subtabs %}
{% subtab Web SDK %}

```javascript
braze.logCustomEvent("ecommerce.checkout_started", {
    "checkout_id": "checkout_abc123",
    "cart_id": "cart_12345",
    "total_value": 199.98,
    "currency": "USD",
    "products": [
        {
            "product_id": "632910392",
            "product_name": "Wireless Headphones",
            "variant_id": "808950810",
            "quantity": 1,
            "price": 199.98,
            "metadata": {
                "sku": "WH-BLK-PRO",
                "color": "Black",
                "brand": "BrazeAudio"
            }
        }
    ],
    "source": "https://braze-audio.com",
    "metadata": {
        "checkout_url": "https://checkout.braze-audio.com/abc123"
    }
});
```

{% endsubtab %}
{% subtab Android SDK %}

```java
JSONArray products = new JSONArray();
JSONObject product = new JSONObject()
    .put("product_id", "632910392")
    .put("product_name", "Wireless Headphones")
    .put("variant_id", "808950810")
    .put("quantity", 1)
    .put("price", 199.98)
    .put("metadata", new JSONObject()
        .put("sku", "WH-BLK-PRO")
        .put("color", "Black")
        .put("brand", "AudioTech"));
products.put(product);

BrazeProperties properties = new BrazeProperties()
    .addProperty("checkout_id", "checkout_abc123")
    .addProperty("cart_id", "cart_12345")
    .addProperty("total_value", 199.98)
    .addProperty("currency", "USD")
    .addProperty("products", products)
    .addProperty("source", "https://braze-audio.com")
    .addProperty("metadata", new JSONObject()
        .put("checkout_url", "https://checkout.braze-audio.com/abc123"));

Braze.getInstance(context).logCustomEvent("ecommerce.checkout_started", properties);
```

{% endsubtab %}
{% subtab Swift SDK %}

```swift
let products: [[String: Any]] = [
    [
        "product_id": "632910392",
        "product_name": "Wireless Headphones",
        "variant_id": "808950810",
        "quantity": 1,
        "price": 199.98,
        "metadata": [
            "sku": "WH-BLK-PRO",
            "color": "Black",
            "brand": "BrazeAudio"
        ]
    ]
]

let properties: [String: Any] = [
    "checkout_id": "checkout_abc123",
    "cart_id": "cart_12345",
    "total_value": 199.98,
    "currency": "USD",
    "products": products,
    "source": "https://braze-audio.com",
    "metadata": [
        "checkout_url": "https://checkout.braze-audio.com/abc123"
    ]
]

AppDelegate.braze?.logCustomEvent(name: "ecommerce.checkout_started", properties: properties)
```

{% endsubtab %}
{% subtab API Payload %}

```json
{
  "events": [
    {
      "external_id": "user_id",
      "app_id": "your_app_identifier",
      "name": "ecommerce.checkout_started",
      "time": "2024-01-15T09:25:45Z",
      "properties": {
        "checkout_id": "checkout_abc123",
        "cart_id": "cart_12345",
        "total_value": 199.98,
        "currency": "USD",
        "products": [
          {
            "product_id": "632910392",
            "product_name": "Wireless Headphones",
            "variant_id": "808950810",
            "quantity": 1,
            "price": 199.98,
            "metadata": {
              "sku": "WH-BLK-PRO",
              "color": "Black",
              "brand": "BrazeAudio"
            }
          }
        ],
        "source": "https://braze-audio.com",
        "metadata": {
          "checkout_url": "https://checkout.braze-audio.com/abc123"
        }
      }
    }
  ]
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab ecommerce.order_placed %}

고객이 체크아웃 프로세스를 성공적으로 완료하고 주문을 할 때 트리거되는 주문 배치 이벤트를 사용할 수 있습니다.

#### 속성

| 속성 이름 | 필수 | 데이터 유형 | 설명 | 
|---|---|---|---|
| `order_id` | 예 | 문자열 | 주문 배치의 고유 식별자입니다. |
| `cart_id` | 아니요 | 문자열 | 장바구니의 고유 식별자입니다. 값이 전달되지 않으면, 사용자 장바구니 매핑을 위해 기본값(장바구니, 체크아웃 및 주문 이벤트에서 공유됨)을 결정합니다. |
| `total_value` | 예 | 부동 | 장바구니의 총 금전적 가치입니다. | 
| `currency` | 예 | 문자열 | 장바구니의 가치가 평가되는 통화입니다. |
| `total_discounts` | 아니요 | 부동 | 주문에 적용된 총 할인 금액입니다. | 
| `discounts`| 아니요 | 객체 배열 | 주문에 적용된 할인 내역의 상세 목록입니다. |
| `products` | 예 | 객체 배열 |  |
| `product_id` | 예 | 문자열 | 조회된 제품의 고유 식별자입니다. 이 값은 제품 ID 또는 SKU일 수 있습니다. |
| `product_name` | 예 | 문자열 | 조회된 제품의 이름입니다. |
| `variant_id` | 예 | 문자열 | 제품 변형의 고유 식별자입니다. 예: `shirt_medium_blue` |
| `image_url` | 아니요 | 문자열 | 제품 이미지의 URL입니다. |
| `product_url` | 아니요 | 문자열 | 자세한 내용을 위한 제품 페이지의 URL입니다. |
| `quantity` | 예 | 정수 | 장바구니에 있는 제품의 수량입니다. |
| `price` | 예 | 부동 | 조회 시 제품의 변형 단가입니다. |
| `metadata` | 아니요 | 객체 | 고객이 자신의 사용 사례를 위해 추가하고자 하는 제품에 대한 추가 메타데이터 필드입니다. Shopify의 경우, SKU를 추가할 것입니다. <br> 이것은 50kb의 일반 이벤트 속성 한도에 따라 제한이 있습니다. |
| `sku` | 아니요 | 문자열 | (Shopify 전용) Shopify SKU. 이것은 카탈로그 ID 필드로 구성할 수 있습니다. |
| `source` | 예 | 문자열 | 이벤트가 유래된 출처입니다. (Shopify의 경우, 이는 매장입니다). |
| `metadata` | 아니요 | 객체 |  |
| `order_status_url` | 아니요 | 문자열 | 주문의 상태를 확인할 수 있는 URL입니다. |
| `order_number` | 아니요 | 문자열 | (Shopify 전용) 주문에 대한 고유 주문 번호입니다. |
| `tags` | 아니요 | 배열 | (Shopify 전용) 주문 태그입니다.
| `referring_site` | 아니요 | 문자열 | (Shopify 전용) 주문이 발생한 사이트(예: Meta)입니다. |
| `payment_gateway_names` | 아니요 | 배열 | (Shopify 전용) 결제 시스템 출처(예: 판매 시점 또는 모바일)입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### 예제 객체들

{% subtabs %}
{% subtab Web SDK %}

```javascript
braze.logCustomEvent("ecommerce.order_placed", {
    "order_id": "order_67890",
    "cart_id": "cart_12345",
    "total_value": 189.98,
    "currency": "USD",
    "total_discounts": 10.00,
    "discounts": [
        {
            "code": "SAVE10",
            "amount": 10.00
        }
    ],
    "products": [
        {
            "product_id": "632910392",
            "product_name": "Wireless Headphones",
            "variant_id": "808950810",
            "quantity": 1,
            "price": 199.98,
            "metadata": {
                "sku": "WH-BLK-PRO",
                "color": "Black",
                "brand": "BrazeAudio"
            }
        }
    ],
    "source": "https://braze-audio.com",
    "metadata": {
        "order_status_url": "https://braze-audio.com/orders/67890/status",
        "order_number": "ORD-2024-001234",
        "tags": ["electronics", "audio"],
        "referring_site": "https://www.e-referrals.com",
        "payment_gateway_names": ["tap2pay", "dotcash"]
    }
});
```

{% endsubtab %}
{% subtab Android SDK %}

```java
JSONArray discounts = new JSONArray();
discounts.put(new JSONObject()
    .put("code", "SAVE10")
    .put("amount", 10.00));

JSONArray products = new JSONArray();
JSONObject product = new JSONObject()
    .put("product_id", "632910392")
    .put("product_name", "Wireless Headphones")
    .put("variant_id", "808950810")
    .put("quantity", 1)
    .put("price", 199.98)
    .put("metadata", new JSONObject()
        .put("sku", "WH-BLK-PRO")
        .put("color", "Black")
        .put("brand", "AudioTech"));
products.put(product);

BrazeProperties properties = new BrazeProperties()
    .addProperty("order_id", "order_67890")
    .addProperty("cart_id", "cart_12345")
    .addProperty("total_value", 189.98)
    .addProperty("currency", "USD")
    .addProperty("total_discounts", 10.00)
    .addProperty("discounts", discounts)
    .addProperty("products", products)
    .addProperty("source", "https://braze-audio.com")
    .addProperty("metadata", new JSONObject()
        .put("order_status_url", "https://braze-audio.com/orders/67890/status")
        .put("order_number", "ORD-2024-001234")
        .put("tags", new JSONArray().put("electronics").put("audio"))
        .put("referring_site", "https://www.e-referrals.com")
        .put("payment_gateway_names", new JSONArray().put("tap2pay").put("dotcash")));

Braze.getInstance(context).logCustomEvent("ecommerce.order_placed", properties);
```

{% endsubtab %}
{% subtab Swift SDK %}

```swift
let discounts: [[String: Any]] = [
    [
        "code": "SAVE10",
        "amount": 10.00
    ]
]

let products: [[String: Any]] = [
    [
        "product_id": "632910392",
        "product_name": "Wireless Headphones",
        "variant_id": "808950810",
        "quantity": 1,
        "price": 199.98,
        "metadata": [
            "sku": "WH-BLK-PRO",
            "color": "Black",
            "brand": "BrazeAudio"
        ]
    ]
]

let properties: [String: Any] = [
    "order_id": "order_67890",
    "cart_id": "cart_12345",
    "total_value": 189.98,
    "currency": "USD",
    "total_discounts": 10.00,
    "discounts": discounts,
    "products": products,
    "source": "https://braze-audio.com",
    "metadata": [
        "order_status_url": "https://braze-audio.com/orders/67890/status",
        "order_number": "ORD-2024-001234",
        "tags": ["electronics", "audio"],
        "referring_site": "https://www.e-referrals.com",
        "payment_gateway_names": ["tap2pay", "dotcash"]
    ]
]

AppDelegate.braze?.logCustomEvent(name: "ecommerce.order_placed", properties: properties)
```

{% endsubtab %}
{% subtab API Payload %}

```json
{
  "events": [
    {
      "external_id": "user_id",
      "app_id": "your_app_identifier",
      "name": "ecommerce.order_placed",
      "time": "2024-01-15T09:35:20Z",
      "properties": {
        "order_id": "order_67890",
        "cart_id": "cart_12345",
        "total_value": 189.98,
        "currency": "USD",
        "total_discounts": 10.00,
        "discounts": [
          {
            "code": "SAVE10",
            "amount": 10.00
          }
        ],
        "products": [
          {
            "product_id": "632910392",
            "product_name": "Wireless Headphones",
            "variant_id": "808950810",
            "quantity": 1,
            "price": 199.98,
            "metadata": {
              "sku": "WH-BLK-PRO",
              "color": "Black",
              "brand": "BrazeAudio"
            }
          }
        ],
        "source": "https://braze-audio.com",
        "metadata": {
          "order_status_url": "https://braze-audio.com/orders/67890/status",
          "order_number": "ORD-2024-001234",
          "tags": ["electronics", "audio"],
          "referring_site": "https://www.e-referrals.com",
          "payment_gateway_names": ["tap2pay", "dotcash"]
        }
      }
    }
  ]
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab ecommerce.order_refunded %}

주문이 부분적으로 또는 전액 환불될 때 트리거하기 위해 주문 환불 이벤트를 사용할 수 있습니다.

#### 속성

| 속성 이름       | 필수 | 데이터 유형 | 설명   |
|---------------|---------|-----------|-------------------------|
| `order_id`            | 예      | 문자열    | 주문 배치의 고유 식별자입니다.        |
| `total_value`         | 예      | 부동     | 장바구니의 총 금전적 가치입니다.    |
| `currency`            | 예      | 문자열    | 장바구니의 가치가 평가되는 통화입니다.    |
| `total_discounts`     | 아니요       | 부동     | 주문에 적용된 총 할인 금액입니다.   |
| `discounts`           | 아니요       | 객체 배열     | 주문에 적용된 할인 내역의 상세 목록입니다. |
| `products`            | 예      | 객체 배열     |  |
| `product_id`       | 예      | 문자열    | 조회된 제품의 고유 식별자입니다. 이 값은 제품 ID, SKU 또는 유사한 값일 수 있습니다. <br>부분 환불이 발행되고 환불에 `product_id`이 할당되지 않은 경우(예: 주문 수준 환불), 일반화된 `product_id`를 제공하십시오.             |
| `product_name`     | 예      | 문자열    | 조회된 제품의 이름입니다.                                                                      |
| `variant_id`       | 예      | 문자열    | 제품 변형에 대한 고유 식별자(예: `shirt_medium_blue`)입니다.                                         |
| `image_url`        | 아니요       | 문자열    | 제품 이미지의 URL입니다.     |
| `product_url`      | 아니요       | 문자열    | 자세한 내용을 위한 제품 페이지의 URL입니다.  |
| `quantity`         | 예      | 정수   | 장바구니에 있는 제품의 수량입니다.   |
| `price`            | 예      | 부동     | 조회 시 제품의 변형 단가입니다.  |
| `metadata`         | 아니요       | 객체    | 고객이 자신의 사용 사례를 위해 추가하고자 하는 제품에 대한 추가 메타데이터 필드입니다. Shopify의 경우, SKU를 추가할 것입니다. 이것은 50kb의 일반 이벤트 속성 한도에 따라 제한이 있습니다. |
| `sku`            | 아니요       | 문자열    | (Shopify 전용) Shopify SKU. 이것은 카탈로그 ID 필드로 구성할 수 있습니다.  |
| `source`              | 예      | 문자열    | 이벤트가 유래된 출처입니다. (Shopify의 경우, 이는 매장입니다).    |
| `metadata`            | 아니요       | 객체    |                |
| `order_status_url`  | 아니요       | 문자열    | 주문의 상태를 확인할 수 있는 URL입니다.     |
| `order_note`       | 아니요       | 문자열    | (Shopify 전용) 상인이 주문에 추가한 메모입니다.    |
| `order_number`     | 아니요       | 문자열    | (Shopify 전용) 주문에 대한 고유 주문 번호입니다.   |
| `tags`             | 아니요       | 배열     | (Shopify 전용) 주문 태그.  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### 예제 객체들

{% subtabs %}
{% subtab Web SDK %}

```javascript
braze.logCustomEvent("ecommerce.order_refunded", {
    "order_id": "order_67890",
    "total_value": 99.99,
    "currency": "USD",
    "total_discounts": 5.00,
    "discounts": [
        {
            "code": "SAVE5",
            "amount": 5.00
        }
    ],
    "products": [
        {
            "product_id": "632910392",
            "product_name": "Wireless Headphones",
            "variant_id": "808950810",
            "quantity": 1,
            "price": 99.99,
            "metadata": {
                "sku": "WH-BLK-PRO",
                "color": "Black",
                "brand": "BrazeAudio"
            }
        }
    ],
    "source": "https://braze-audio.com",
    "metadata": {
        "order_status_url": "https://braze-audio.com/orders/67890/status",
        "order_note": "Customer requested refund due to defective item",
        "order_number": "ORD-2024-001234",
        "tags": ["refund", "defective"]
    }
});
```

{% endsubtab %}
{% subtab Android SDK %}

```java
JSONArray discounts = new JSONArray();
discounts.put(new JSONObject()
    .put("code", "SAVE5")
    .put("amount", 5.00));

JSONArray products = new JSONArray();
JSONObject product = new JSONObject()
    .put("product_id", "632910392")
    .put("product_name", "Wireless Headphones")
    .put("variant_id", "808950810")
    .put("quantity", 1)
    .put("price", 99.99)
    .put("metadata", new JSONObject()
        .put("sku", "WH-BLK-PRO")
        .put("color", "Black")
        .put("brand", "AudioTech"));
products.put(product);

BrazeProperties properties = new BrazeProperties()
    .addProperty("order_id", "order_67890")
    .addProperty("total_value", 99.99)
    .addProperty("currency", "USD")
    .addProperty("total_discounts", 5.00)
    .addProperty("discounts", discounts)
    .addProperty("products", products)
    .addProperty("source", "https://braze-audio.com")
    .addProperty("metadata", new JSONObject()
        .put("order_status_url", "https://braze-audio.com/orders/67890/status")
        .put("order_note", "Customer requested refund due to defective item")
        .put("order_number", "ORD-2024-001234")
        .put("tags", new JSONArray().put("refund").put("defective")));

Braze.getInstance(context).logCustomEvent("ecommerce.order_refunded", properties);
```

{% endsubtab %}
{% subtab Swift SDK %}

```swift
let discounts: [[String: Any]] = [
    [
        "code": "SAVE5",
        "amount": 5.00
    ]
]

let products: [[String: Any]] = [
    [
        "product_id": "632910392",
        "product_name": "Wireless Headphones",
        "variant_id": "808950810",
        "quantity": 1,
        "price": 99.99,
        "metadata": [
            "sku": "WH-BLK-PRO",
            "color": "Black",
            "brand": "BrazeAudio"
        ]
    ]
]

let properties: [String: Any] = [
    "order_id": "order_67890",
    "total_value": 99.99,
    "currency": "USD",
    "total_discounts": 5.00,
    "discounts": discounts,
    "products": products,
    "source": "https://braze-audio.com",
    "metadata": [
        "order_status_url": "https://braze-audio.com/orders/67890/status",
        "order_note": "Customer requested refund due to defective item",
        "order_number": "ORD-2024-001234",
        "tags": ["refund", "defective"]
    ]
]

AppDelegate.braze?.logCustomEvent(name: "ecommerce.order_refunded", properties: properties)
```

{% endsubtab %}
{% subtab API Payload %}

```json
{
  "events": [
    {
      "external_id": "user_id",
      "app_id": "your_app_identifier",
      "name": "ecommerce.order_refunded",
      "time": "2024-01-15T10:15:30Z",
      "properties": {
        "order_id": "order_67890",
        "total_value": 99.99,
        "currency": "USD",
        "total_discounts": 5.00,
        "discounts": [
          {
            "code": "SAVE5",
            "amount": 5.00
          }
        ],
        "products": [
          {
            "product_id": "632910392",
            "product_name": "Wireless Headphones",
            "variant_id": "808950810",
            "quantity": 1,
            "price": 99.99,
            "metadata": {
              "sku": "WH-BLK-PRO",
              "color": "Black",
              "brand": "BrazeAudio"
            }
          }
        ],
        "source": "https://braze-audio.com",
        "metadata": {
          "order_status_url": "https://braze-audio.com/orders/67890/status",
          "order_note": "Customer requested refund due to defective item",
          "order_number": "ORD-2024-001234",
          "tags": ["refund", "defective"]
        }
      }
    }
  ]
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab ecommerce.order_cancelled %}

고객이 주문을 취소할 때 트리거할 수 있는 주문 취소 이벤트를 사용할 수 있습니다.

#### 속성

| 속성 이름      | 필수 | 데이터 유형 | 설명       |
|---------------------|----------|-----------|-------------------|
| `order_id`            | 예      | 문자열    | 주문에 대한 고유 식별자입니다.              |
| `cancel_reason`       | 예      | 문자열    | 주문이 취소된 이유입니다.           |
| `total_value`         | 예      | 부동 소수점     | 장바구니의 총 금전적 가치입니다.         |
| `currency`            | 예      | 문자열    | 장바구니의 가치가 평가되는 통화입니다.           |
| `total_discounts`     | 아니요       | 부동 소수점     | 주문에 적용된 총 할인 금액입니다.     |
| `discounts`           | 아니요       | 객체 배열     | 주문에 적용된 할인에 대한 자세한 목록입니다.             |
| `products`            | 예      | 객체 배열     |         |
| `product_id`          | 예      | 문자열    | 조회된 제품의 고유 식별자입니다. 이 값은 제품 ID, SKU 또는 유사한 것이 될 수 있습니다.             |
| `product_name`        | 예      | 문자열    | 조회된 제품의 이름입니다.          |
| `variant_id`          | 예      | 문자열    | 제품 변형에 대한 고유 식별자입니다(예: `shirt_medium_blue`).        |
| `image_url`           | 아니요       | 문자열    | 제품 이미지의 URL입니다.           |
| `product_url`         | 아니요       | 문자열    | 자세한 내용을 위한 제품 페이지의 URL입니다.                                                                     |
| `quantity`            | 예      | 정수   | 장바구니에 있는 제품의 수량입니다.        |
| `price`               | 예      | 부동 소수점     | 조회 시 제품의 변형 단가입니다.     |
| `metadata`            | 아니요       | 객체    | 고객이 자신의 사용 사례를 위해 추가하고자 하는 제품에 대한 추가 메타데이터 필드입니다. Shopify의 경우 SKU를 추가할 것입니다. 이는 50kb의 일반 이벤트 속성 한도에 따라 제한됩니다. |
| `sku`                 | 아니요       | 문자열    | (Shopify 전용) Shopify SKU입니다. 이것은 카탈로그 ID 필드로 구성될 수 있습니다.        |
| `source`              | 예      | 문자열    | 이벤트가 유래된 출처입니다. (Shopify의 경우, 이는 매장입니다).    |
| `metadata`            | 아니요       | 객체    |       |
| `order_status_url`    | 아니요       | 문자열    | 주문 상태를 확인할 URL입니다.                                                                          |
| `order_number`        | 아니요       | 문자열    | (Shopify 전용) 주문에 대한 고유 주문 번호입니다.  |
| `tags`                | 아니요       | 배열     | (Shopify 전용) 주문 태그.            |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### 예제 객체들

{% subtabs %}
{% subtab Web SDK %}

```javascript
braze.logCustomEvent("ecommerce.order_cancelled", {
    "order_id": "order_67890",
    "cancel_reason": "customer changed mind",
    "total_value": 189.98,
    "currency": "USD",
    "total_discounts": 10.00,
    "discounts": [
        {
            "code": "SAVE10",
            "amount": 10.00
        }
    ],
    "products": [
        {
            "product_id": "632910392",
            "product_name": "Wireless Headphones",
            "variant_id": "808950810",
            "quantity": 1,
            "price": 199.98,
            "metadata": {
                "sku": "WH-BLK-PRO",
                "color": "Black",
                "brand": "BrazeAudio"
            }
        }
    ],
    "source": "https://braze-audio.com",
    "metadata": {
        "order_status_url": "https://braze-audio.com/orders/67890/status",
        "order_number": "ORD-2024-001234",
        "tags": ["cancelled", "customer_request"]
    }
});
```

{% endsubtab %}
{% subtab Android SDK %}

```java
JSONArray discounts = new JSONArray();
discounts.put(new JSONObject()
    .put("code", "SAVE10")
    .put("amount", 10.00));

JSONArray products = new JSONArray();
JSONObject product = new JSONObject()
    .put("product_id", "632910392")
    .put("product_name", "Wireless Headphones")
    .put("variant_id", "808950810")
    .put("quantity", 1)
    .put("price", 199.98)
    .put("metadata", new JSONObject()
        .put("sku", "WH-BLK-PRO")
        .put("color", "Black")
        .put("brand", "AudioTech"));
products.put(product);

BrazeProperties properties = new BrazeProperties()
    .addProperty("order_id", "order_67890")
    .addProperty("cancel_reason", "customer changed mind")
    .addProperty("total_value", 189.98)
    .addProperty("currency", "USD")
    .addProperty("total_discounts", 10.00)
    .addProperty("discounts", discounts)
    .addProperty("products", products)
    .addProperty("source", "https://braze-audio.com")
    .addProperty("metadata", new JSONObject()
        .put("order_status_url", "https://braze-audio.com/orders/67890/status")
        .put("order_number", "ORD-2024-001234")
        .put("tags", new JSONArray().put("cancelled").put("customer_request")));

Braze.getInstance(context).logCustomEvent("ecommerce.order_cancelled", properties);
```

{% endsubtab %}
{% subtab Swift SDK %}

```swift
let discounts: [[String: Any]] = [
    [
        "code": "SAVE10",
        "amount": 10.00
    ]
]

let products: [[String: Any]] = [
    [
        "product_id": "632910392",
        "product_name": "Wireless Headphones",
        "variant_id": "808950810",
        "quantity": 1,
        "price": 199.98,
        "metadata": [
            "sku": "WH-BLK-PRO",
            "color": "Black",
            "brand": "BrazeAudio"
        ]
    ]
]

let properties: [String: Any] = [
    "order_id": "order_67890",
    "cancel_reason": "customer changed mind",
    "total_value": 189.98,
    "currency": "USD",
    "total_discounts": 10.00,
    "discounts": discounts,
    "products": products,
    "source": "https://braze-audio.com",
    "metadata": [
        "order_status_url": "https://braze-audio.com/orders/67890/status",
        "order_number": "ORD-2024-001234",
        "tags": ["cancelled", "customer_request"]
    ]
]

AppDelegate.braze?.logCustomEvent(name: "ecommerce.order_cancelled", properties: properties)
```

{% endsubtab %}
{% subtab API Payload %}

```json
{
  "events": [
    {
      "external_id": "user_id",
      "app_id": "your_app_identifier",
      "name": "ecommerce.order_cancelled",
      "time": "2024-01-15T10:45:15Z",
      "properties": {
        "order_id": "order_67890",
        "cancel_reason": "customer changed mind",
        "total_value": 189.98,
        "currency": "USD",
        "total_discounts": 10.00,
        "discounts": [
          {
            "code": "SAVE10",
            "amount": 10.00
          }
        ],
        "products": [
          {
            "product_id": "632910392",
            "product_name": "Wireless Headphones",
            "variant_id": "808950810",
            "quantity": 1,
            "price": 199.98,
            "metadata": {
              "sku": "WH-BLK-PRO",
              "color": "Black",
              "brand": "BrazeAudio"
            }
          }
        ],
        "source": "https://braze-audio.com",
        "metadata": {
          "order_status_url": "https://braze-audio.com/orders/67890/status",
          "order_number": "ORD-2024-001234",
          "tags": ["cancelled", "customer_request"]
        }
      }
    }
  ]
}
```

{% endsubtab %}
{% endsubtabs %}

{% endtab %}
{% endtabs %}

## 전자상거래 캔버스 템플릿

Braze는 체크아웃 프로세스를 시작했지만 주문을 하기 전에 떠난 고객을 타겟팅하는 것과 같은 전자상거래 추천 이벤트에 의해 구동되는 미리 구축된 캔버스 템플릿을 생성했습니다. 이 이벤트를 사용하여 메시지를 개인화하고 특정 대상을 타겟팅하여 사용자 여정을 향상시키기 위한 정보에 기반한 결정을 내릴 수 있습니다.

캔버스 템플릿과 함께 이러한 이벤트를 사용할 수 있는 방법에 대한 더 많은 정보를 보려면 전용 [전자상거래 사용 사례]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/ecommerce_use_cases)를 확인하세요.

## 사용자 계산 필드

다음 필드에 대해 표준화된 사용자 필드 계산을 사용합니다: 

- **총 수익** = 총 주문 금액의 합 - 총 환불 금액의 합
- **총 주문 수** = 고유한 주문 발생 이벤트 수 - 고유한 주문 취소 수
- **총 환불 금액** = 총 환불 금액의 합 

이 사용자 필드 계산은 사용자 프로필의 **거래** 탭에도 포함되어 있습니다.

\![사용자 계산 필드가 있는 "거래" 탭.]({% image_buster /assets/img/Shopify/transactions_tab.png %}){: style="max-width:60%;"}
