---
nav_title: 전자상거래 추천 이벤트
article_title: 전자상거래 추천 이벤트
page_type: reference
alias: /ecommerce_events/
toc_headers: h2
description: "이 참조 문서에서는 전자상거래 추천 이벤트 및 속성, 사용법, 세분화, 관련 분석을 볼 수 있는 위치 등을 설명합니다."
---

# eCommerce 추천 이벤트

> 이 페이지에서는 전자상거래 추천 이벤트 및 속성을 다룹니다. 이 이벤트는 마케터가 효과적인 메시징을 트리거하는 데 필요한 주요 쇼핑 행동을 포착하기 위해 생성되었습니다. 예를 들어, 장바구니를 포기한 고객을 타겟팅하는 것입니다.

Braze는 데이터 계획에 시간이 걸린다는 것을 인식하고 있습니다. 우리는 고객이 개발 팀을 익숙하게 하고 지금 이러한 이벤트를 보내기 시작할 것을 권장합니다. 전자상거래 추천 이벤트와 함께 즉시 사용할 수 없는 기능이 있을 수 있지만, 2025년 동안 전자상거래 기능을 향상시킬 새로운 제품의 도입을 기대할 수 있습니다.

{% alert important %}
eCommerce 추천 이벤트는 현재 초기 액세스 중입니다. 이 초기 액세스에 참여하고 싶다면 Braze 고객 성공 매니저에게 문의하세요. <br><br>새로운 [Shopify 커넥터를]({{site.baseurl}}/partners/ecommerce/shopify/multiple_stores/?tab=shopify%20connector) 활용하는 경우 이러한 권장 이벤트는 통합을 통해 자동으로 사용할 수 있습니다.
{% endalert %}


## 전자상거래 추천 이벤트의 유형

{% tabs %}
{% tab ecommerce.제품_조회 %}

고객이 제품 상세 페이지를 조회할 때 트리거하기 위해 제품 조회 이벤트를 사용할 수 있습니다.

#### 등록정보

| 속성 이름 | 필수 | 데이터 유형 | 설명 | 
|---|---|---|---|
| `product_id` | 예 | 문자열 | 조회된 제품에 대한 고유 식별자입니다. <br> 비-Shopify 고객의 경우, 이는 SKU와 같은 카탈로그 항목 ID에 대해 설정한 값이 됩니다. |
| `product_name` | 예 | 문자열 | 조회된 제품의 이름입니다. | 
| `variant_id` | 예 | 문자열 | 제품 변형에 대한 고유 식별자입니다. 예는`shirt_medium_blue`입니다. |
| `image_url` | 아니요 | 문자열 | 제품 이미지의 URL입니다. |
| `product_url` | 아니요 | 문자열 | 자세한 내용을 위한 제품 페이지의 URL입니다. |
| `price` | 예 | 플로트 | 조회 시 제품의 변형 단가입니다. |
| `currency` | 예 | 문자열 | 제품 가격이 기재된 통화(예: "USD" 또는 "EUR")는 [ISO 4217 형식](https://www.iso.org/iso-4217-currency-codes.html)입니다. |
| `source` | 예 | 문자열 | 이벤트가 유래된 출처입니다. (Shopify의 경우, 이는 상점 프론트입니다). |
| `metadata` | 아니요 | 객체 | |
| `sku` | 아니요 | 문자열 | (Shopify 전용) Shopify SKU입니다. 이것은 카탈로그 ID 필드로 구성할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### 예시 객체

```json
{
    "name": "ecommerce.product_viewed",
    "properties": {
        "product_id": "12345",
        "product_name": "product",
        "variant_id": "123",
        "image_url": "www.image-url.com",
        "product_url": "mystorefront.myshopify.com/product",
        "price": 10,
        "currency": "USD",
        "source": "mystorefront.myshopify.com",
        "metadata": {
            "sku": "sku"
        }
    }
}
```
{% endtab %}
{% tab ecommerce.장바구니_업데이트됨 %}

장바구니 업데이트 이벤트를 사용하여 제품이 장바구니에 추가, 제거 또는 업데이트될 때를 추적할 수 있습니다. `ecommerce.cart_updated` 이벤트는 트리거되기 전에 다음 정보를 확인합니다:

- 이벤트 시간이 사용자의 특정 장바구니에 대한 `updated_at` 시간보다 큽니다.
- 장바구니가 체크아웃 프로세스로 진행되지 않았습니다.
- `products` 배열이 비어 있지 않습니다.

#### 장바구니 매핑 객체

`ecommerce.cart_updated` 이벤트에는 장바구니 매핑 객체가 있습니다. 이 객체는 쇼핑객의 장바구니에 있는 모든 제품을 포함하는 장바구니의 매핑을 포함하는 고객 프로필을 위해 생성됩니다. Liquid 태그를 통해 장바구니에 있는 제품에 접근할 수 있습니다: 

{%raw%}
```liquid
{% shopping_cart {{context_properties.${cart_id}}} %}
{% for item in shopping_cart.products %}
{% catalog_items <add_your_catalog> {{item.variant_id}} %}
```
{%endraw%}

장바구니가 업데이트되지 않고 10일 이내에 주문이 진행되지 않으면 장바구니와 관련된 제품을 삭제합니다.

{% alert note %}
장바구니당 제품 수는 Braze에서 제한되지 않습니다. 그러나 Shopify의 제한은 500입니다.
{% endalert %}

#### 사용자 프로필 병합 시 장바구니 동작

장바구니가 두 개 있는 경우, 두 개 모두 병합된 사용자에게 추가합니다. 가장 최근 장바구니 정보를 포함한 메시지를 보내기 위해 동일하거나 다른 장바구니일 경우 Canvas를 다시 대기열에 추가합니다. `ecommerce.cart_updated` 이벤트는 가장 최근 장바구니 ID와 장바구니의 가장 최근 제품을 포함합니다.

#### 등록정보

| 속성 이름 | 필수 | 데이터 유형 | 설명 | 
|---|---|---|---|
| `cart_id` | 예 | 문자열 | 장바구니의 고유 식별자입니다. 값이 전달되지 않으면, 사용자 장바구니 매핑을 위해 기본값(장바구니, 체크아웃 및 주문 이벤트 간에 공유됨)을 결정합니다. |
| `total_value` | 예 | 플로트 | 장바구니의 총 금전적 가치입니다. | 
| `currency` | 예 | 문자열 | 제품 가격이 기재된 통화(예: "USD" 또는 "EUR")는 [ISO 4217 형식](https://www.iso.org/iso-4217-currency-codes.html)입니다. |
| `products` | 예 | 배열 |  |
| `product_id` | 예 | 문자열 | 조회된 제품에 대한 고유 식별자입니다. <br> 이 값은 제품 ID 또는 SKU일 수 있습니다. |
| `product_name` | 예 | 문자열 | 조회된 제품의 이름입니다. |
| `variant_id` | 예 | 문자열 | 제품 변형에 대한 고유 식별자입니다. 예는`shirt_medium_blue`입니다. |
| `image_url` | 아니요 | 문자열 | 제품 이미지의 URL입니다. |
| `product_url` | 아니요 | 문자열 | 자세한 내용을 위한 제품 페이지의 URL입니다. |
| `quantity` | 예 | 정수 | 장바구니에 있는 제품의 단위 수입니다. |
| `price` | 예 | 플로트 | 조회 시 제품의 변형 단가입니다. |
| `metadata` | 아니요 | 객체 | 고객이 자신의 사용 사례를 위해 추가하고자 하는 제품에 대한 추가 메타데이터 필드입니다. Shopify의 경우, SKU를 추가합니다. <br> 이는 50kb의 일반 이벤트 속성 제한에 따라 제한이 있습니다. |
| `sku` | 아니요 | 문자열 | (Shopify 전용) Shopify SKU입니다. 이것은 카탈로그 ID 필드로 구성할 수 있습니다. |
| `source` | 예 | 문자열 | 이벤트가 유래된 출처입니다. (Shopify의 경우, 이는 상점 프론트입니다). |
| `metadata` | 아니요 | 객체 | 고객이 자신의 사용 사례를 위해 추가하고자 하는 제품에 대한 추가 메타데이터 필드입니다. Shopify의 경우, SKU를 추가합니다. <br> 이는 50kb의 일반 이벤트 속성 제한에 따라 제한이 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### 예시 객체

```json
{
    "name": "ecommerce.cart_updated",
    "properties": {
        "cart_id": "Z2NwLXVzLWVhc3QxOjAxSjk3UFg4RlFZMjVTVkRHRlc1RlI3SlRY",
        "currency": "USD",
        "total_value": 2000000,
        "products": [
            {
                "product_id": "8266836345064",
                "product_name": "PANTS!!!",
                "variant_id": "44610569208040",
                "image_url": "https://cdn.shopify.com/s/files/1/0604/4211/6328/files/1200px-Trousers-colourisolated.jpg?v=1689256168",
                "product_url": "https://test-store.myshopify.com/products/pants?variant=44610569208040",
                "quantity": 2,
                "price": 1000000,
                "metadata": {
                    "sku": "007"
                }
            }
        ],
        "source": "https://test-store.myshopify.com",
        "metadata": {}
    }
}
```
{% endtab %}
{% tab ecommerce.checkout_started %}

체크아웃 프로세스를 시작했지만 주문을 하지 않은 고객을 리타겟하기 위해 체크아웃 시작 이벤트를 사용할 수 있습니다.

`ecommerce.cart_updated` 이벤트와 유사하게, 이 이벤트는 장바구니 내 모든 제품에 접근하기 위해 쇼핑 카트 Liquid 태그를 활용할 수 있게 해줍니다. 이 기능은 포기된 체크아웃 메시지에 사용됩니다:

{%raw%}
```liquid
{% shopping_cart {{context_properties.${cart_id}}} :abort_if_not_abandoned false %}
{% for item in shopping_cart.products %}
{% catalog_items <add_your_catalog> {{item.variant_id}} %}
```
{%endraw%}

#### 등록정보

| 속성 이름 | 필수 | 데이터 유형 | 설명 | 
|---|---|---|---|
| `checkout_id` | 예 | 문자열 | 체크아웃의 고유 식별자입니다. |
| `cart_id` | 아니요 | 문자열 | 장바구니의 고유 식별자입니다. 값이 전달되지 않으면, 사용자 장바구니 매핑을 위해 기본값(장바구니, 체크아웃 및 주문 이벤트 간에 공유됨)을 결정합니다.. | 
| `total_value` | 예 | 플로트 | 장바구니의 총 금전적 가치입니다. |
| `currency` | 예 | 문자열 | 장바구니의 가치가 평가되는 통화입니다. |
| `products` | 예 | 객체 배열 |  |
| `product_id` | 예 | 문자열 | 조회된 제품에 대한 고유 식별자입니다. 예를 들어, 이 값은 제품 ID 또는 SKU일 수 있습니다. |
| `product_name` | 예 | 문자열 | 조회된 제품의 이름입니다.  |
| `variant_id` | 예 | 문자열 | 제품 변형에 대한 고유 식별자입니다. 예는`shirt_medium_blue`입니다. |
| `image_url` | 아니요 | 문자열 | 제품 이미지의 URL입니다. |
| `product_url` | 아니요 | 문자열 | 자세한 내용을 위한 제품 페이지의 URL입니다. |
| `quantity` | 예 | 정수 | 장바구니에 있는 제품의 단위 수입니다. |
| `price` | 예 | 플로트 | 조회 시 제품의 변형 단가입니다. |
| `metadata` | 아니요 | 객체 | 고객이 자신의 사용 사례를 위해 추가하고자 하는 제품에 대한 추가 메타데이터 필드입니다. Shopify의 경우, SKU를 추가합니다. <br> 이는 50kb의 일반 이벤트 속성 제한에 따라 제한이 있습니다. |
| `sku` | 아니요 | 문자열 | (Shopify 전용) Shopify SKU입니다. 이것은 카탈로그 ID 필드로 구성할 수 있습니다. |
| `source` | 예 | 문자열 | 이벤트가 유래된 출처입니다. (Shopify의 경우, 이는 상점 프론트입니다). |
| `metadata` | 아니요 | 객체 |  |
| `checkout_url` | 아니요 | 문자열 | 체크아웃 페이지의 URL입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### 예시 객체

```json
{
    "name": "ecommerce.checkout_started",
    "time": "2022-05-23T13:52:38-04:00",
    "properties": {
        "cart_id": "eeafa272cebfd4b22385bc4b645e762c",
        "total_value": 421.88,
        "currency": "USD",
        "products": [
            {
                "product_id": "632910392",
                "product_name": "IPod Nano - 8GB",
                "variant_id": "808950810",
                "quantity": 1,
                "price": 199,
                "metadata": {
                    "sku": "IPOD2008PINK"
                }
            }
        ],
        "source": "braze-mock-storefront.myshopify.com",
        "checkout_id": "123123123",
        "metadata": {
            "checkout_url": "https://checkout.local/548380009/checkouts/123123123/recover?key=example-secret-token"
        }
    }
}
```
{% endtab %}
{% tab ecommerce.주문_완료 %}

고객이 체크아웃 프로세스를 성공적으로 완료하고 주문을 할 때 트리거되는 주문 완료 이벤트를 사용할 수 있습니다.

#### 등록정보

| 속성 이름 | 필수 | 데이터 유형 | 설명 | 
|---|---|---|---|
| `order_id` | 예 | 문자열 | 주문 완료에 대한 고유 식별자입니다. |
| `cart_id` | 아니요 | 문자열 | 장바구니의 고유 식별자입니다. 값이 전달되지 않으면, 사용자 장바구니 매핑을 위해 기본값(장바구니, 체크아웃 및 주문 이벤트 간에 공유됨)을 결정합니다. |
| `total_value` | 예 | 플로트 | 장바구니의 총 금전적 가치입니다. | 
| `currency` | 예 | 문자열 | 장바구니의 가치가 평가되는 통화입니다. |
| `total_discounts` | 아니요 | 플로트 | 주문에 적용된 총 할인 금액입니다. | 
| `discounts`| 아니요 | 객체 배열 | 주문에 적용된 할인 목록입니다. |
| `products` | 예 | 객체 배열 |  |
| `product_id` | 예 | 문자열 | 조회된 제품에 대한 고유 식별자입니다. 이 값은 제품 ID 또는 SKU일 수 있습니다. |
| `product_name` | 예 | 문자열 | 조회된 제품의 이름입니다. |
| `variant_id` | 예 | 문자열 | 제품 변형에 대한 고유 식별자입니다. 예는`shirt_medium_blue`입니다. |
| `image_url` | 아니요 | 문자열 | 제품 이미지의 URL입니다. |
| `product_url` | 아니요 | 문자열 | 자세한 내용을 위한 제품 페이지의 URL입니다. |
| `quantity` | 예 | 정수 | 장바구니에 있는 제품의 단위 수입니다. |
| `price` | 예 | 플로트 | 조회 시 제품의 변형 단가입니다. |
| `metadata` | 아니요 | 객체 | 고객이 자신의 사용 사례를 위해 추가하고자 하는 제품에 대한 추가 메타데이터 필드입니다. Shopify의 경우, SKU를 추가합니다. <br> 이는 50kb의 일반 이벤트 속성 제한에 따라 제한이 있습니다. |
| `sku` | 아니요 | 문자열 | (Shopify 전용) Shopify SKU입니다. 이것은 카탈로그 ID 필드로 구성할 수 있습니다. |
| `source` | 예 | 문자열 | 이벤트가 유래된 출처입니다. (Shopify의 경우, 이는 상점 프론트입니다). |
| `metadata` | 아니요 | 객체 |  |
| `order_status_url` | 아니요 | 문자열 | 주문 상태를 보기 위한 URL입니다. |
| `order_number` | 아니요 | 문자열 | (Shopify 전용) 주문 완료에 대한 고유 주문 번호입니다. |
| `tags` | 아니요 | 배열 | (Shopify 전용) 주문 태그입니다.
| `referring_site` | 아니요 | 문자열 | (Shopify 전용) 주문이 발생한 사이트(예: Meta)입니다. |
| `payment_gateway_names` | 아니요 | 배열 | (Shopify 전용) 결제 시스템 출처(예: 판매 시점 또는 모바일)입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### 예시 객체

```json
{
    "name": "ecommerce.order_placed",
    "time": "2022-05-23T13:52:38-04:00",
    "properties": {
        "order_id": "820982911946154508",
        "cart_id": "eeafa272cebfd4b22385bc4b645e762c",
        "total_value": 421.88,
        "currency": "USD",
        "total_discounts": 5,
        "discounts": [],
        "products": [
            {
                "product_id": "632910392",
                "product_name": "IPod Nano - 8GB",
                "variant_id": "808950810",
                "quantity": 1,
                "price": 199,
                "metadata": {
                    "sku": "IPOD2008PINK"
                }
            }
        ],
        "source": "braze-mock-storefront.myshopify.com",
        "metadata": {
            "order_status_url": "https://apple.myshopify.com/690933842/orders/123456abcd/authenticate?key=abcdefg",
            "order_number": 1234,
            "tags": [
                "heavy",
                "heavy2"
            ],
            "referring_site": "https://www.google.com",
            "payment_gateway_names": [
                "visa",
                "bogus"
            ]
        }
    }
}
```
{% endtab %}
{% tab ecommerce.주문_환불 %}

주문이 부분적으로 또는 전부 환불될 때 트리거되는 주문 환불 이벤트를 사용할 수 있습니다.

#### 등록정보

| 등록정보 이름       | 필수 | 데이터 유형 | 설명   |
|---------------|---------|-----------|-------------------------|
| `order_id`            | 예      | 문자열    | 주문 완료에 대한 고유 식별자입니다.        |
| `total_value`         | 예      | 플로트     | 장바구니의 총 금전적 가치입니다.    |
| `currency`            | 예      | 문자열    | 장바구니의 가치가 평가되는 통화입니다.    |
| `total_discounts`     | 아니요       | 플로트     | 주문에 적용된 총 할인 금액입니다.   |
| `discounts`           | 아니요       | 객체 배열     | 주문에 적용된 할인 목록입니다. |
| `products`            | 예      | 객체 배열     |  |
| `product_id`       | 예      | 문자열    | 조회된 제품에 대한 고유 식별자입니다. 이 값은 제품 ID, SKU 또는 유사한 것이 될 수 있습니다. <br>부분 환불이 발행되고 환불에 할당된 `product_id`이 없는 경우(예: 주문 수준 환불), 일반화된 `product_id`를 제공합니다.             |
| `product_name`     | 예      | 문자열    | 조회된 제품의 이름입니다.                                                                      |
| `variant_id`       | 예      | 문자열    | 제품 변형에 대한 고유 식별자(예: `shirt_medium_blue`)입니다.                                         |
| `image_url`        | 아니요       | 문자열    | 제품 이미지의 URL입니다.     |
| `product_url`      | 아니요       | 문자열    | 자세한 내용을 위한 제품 페이지의 URL입니다.  |
| `quantity`         | 예      | 정수   | 장바구니에 있는 제품의 단위 수입니다.   |
| `price`            | 예      | 플로트     | 조회 시 제품의 변형 단가입니다.  |
| `metadata`         | 아니요       | 객체    | 고객이 자신의 사용 사례를 위해 추가하고자 하는 제품에 대한 추가 메타데이터 필드입니다. Shopify의 경우, SKU를 추가합니다. 이는 50kb의 일반 이벤트 속성 제한에 따라 제한이 있습니다. |
| `sku`            | 아니요       | 문자열    | (Shopify 전용) Shopify SKU입니다. 이것은 카탈로그 ID 필드로 구성할 수 있습니다.  |
| `source`              | 예      | 문자열    | 이벤트가 유래된 출처입니다. (Shopify의 경우, 이는 상점 프론트입니다).    |
| `metadata`            | 아니요       | 객체    |                |
| `order_status_url`  | 아니요       | 문자열    | 주문 상태를 보기 위한 URL입니다.     |
| `order_note`       | 아니요       | 문자열    | (Shopify 전용) 상인이 주문에 추가한 메모입니다.    |
| `order_number`     | 아니요       | 문자열    | (Shopify 전용) 주문 완료에 대한 고유 주문 번호입니다.   |
| `tags`             | 아니요       | 배열     | (Shopify 전용) 주문 태그입니다.  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### 예시 객체

```json
{
    "name": "ecommerce.order_refunded",
    "time": "2022-05-23T13:52:38-04:00",
    "properties": {
        "order_id": "820982911946154508",
        "total_value": 421.88,
        "currency": "USD",
        "total_discounts": 5,
        "discounts": [],
        "products": [
            {
                "product_id": "632910392",
                "product_name": "IPod Nano - 8GB",
                "variant_id": "808950810",
                "quantity": 1,
                "price": 199,
                "metadata": {
                    "sku": "IPOD2008PINK"
                }
            }
        ],
        "source": "braze-mock-storefront.myshopify.com",
        "metadata": {
            "order_status_url": "https://apple.myshopify.com/690933842/orders/123456abcd/authenticate?key=abcdefg",
			"order_note": "item was broken",
            "order_number": 1234,
            "tags": [
                "heavy",
                "heavy2"
            ]
        }
    }
}
```
{% endtab %}
{% tab ecommerce.주문_취소 %}

주문이 취소되었을 때 고객이 주문을 취소할 때 트리거할 수 있는 주문 취소 이벤트를 사용할 수 있습니다.

#### 등록정보

| 등록정보 이름      | 필수 | 데이터 유형 | 설명       |
|---------------------|----------|-----------|-------------------|
| `order_id`            | 예      | 문자열    | 주문 완료에 대한 고유 식별자입니다.              |
| `cancel_reason`       | 예      | 문자열    | 주문이 취소된 이유.           |
| `total_value`         | 예      | 플로트     | 장바구니의 총 금전적 가치입니다.         |
| `currency`            | 예      | 문자열    | 장바구니의 가치가 평가되는 통화입니다.           |
| `total_discounts`     | 아니요       | 플로트     | 주문에 적용된 총 할인 금액입니다.     |
| `discounts`           | 아니요       | 객체 배열     | 주문에 적용된 할인 목록입니다.             |
| `products`            | 예      | 객체 배열     |         |
| `product_id`          | 예      | 문자열    | 조회된 제품에 대한 고유 식별자입니다. 이 값은 제품 ID, SKU 또는 유사한 것이 될 수 있습니다.             |
| `product_name`        | 예      | 문자열    | 조회된 제품의 이름입니다.          |
| `variant_id`          | 예      | 문자열    | 제품 변형에 대한 고유 식별자(예: `shirt_medium_blue`)입니다.        |
| `image_url`           | 아니요       | 문자열    | 제품 이미지의 URL입니다.           |
| `product_url`         | 아니요       | 문자열    | 자세한 내용을 위한 제품 페이지의 URL입니다.                                                                     |
| `quantity`            | 예      | 정수   | 장바구니에 있는 제품의 단위 수입니다.        |
| `price`               | 예      | 플로트     | 조회 시 제품의 변형 단가입니다.     |
| `metadata`            | 아니요       | 객체    | 고객이 자신의 사용 사례를 위해 추가하고자 하는 제품에 대한 추가 메타데이터 필드입니다. Shopify의 경우, SKU를 추가합니다. 이는 50kb의 일반 이벤트 속성 제한에 따라 제한이 있습니다. |
| `sku`                 | 아니요       | 문자열    | (Shopify 전용) Shopify SKU입니다. 이것은 카탈로그 ID 필드로 구성할 수 있습니다.        |
| `source`              | 예      | 문자열    | 이벤트가 유래된 출처입니다. (Shopify의 경우, 이는 상점 프론트입니다).    |
| `metadata`            | 아니요       | 객체    |       |
| `order_status_url`    | 아니요       | 문자열    | 주문 상태를 보기 위한 URL입니다.                                                                          |
| `order_number`        | 아니요       | 문자열    | (Shopify 전용) 주문 완료에 대한 고유 주문 번호입니다.  |
| `tags`                | 아니요       | 배열     | (Shopify 전용) 주문 태그입니다.            |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### 예시 객체

```json
{
    "name": "ecommerce.order_cancelled",
    "time": "2022-05-23T13:52:38-04:00",
    "properties": {
        "order_id": "820982911946154508",
        "cancel_reason": "no longer necessary",
        "total_value": 421.88,
        "currency": "USD",
        "total_discounts": 5,
        "discounts": [],
        "products": [
            {
                "product_id": "632910392",
                "product_name": "IPod Nano - 8GB",
                "variant_id": "808950810",
                "quantity": 1,
                "price": 199,
                "metadata": {
                    "sku": "IPOD2008PINK"
                }
            }
        ],
        "source": "braze-mock-storefront.myshopify.com",
        "metadata": {
            "order_status_url": "https://apple.myshopify.com/690933842/orders/123456abcd/authenticate?key=abcdefg",
            "order_number": 1234,
            "tags": [
                "heavy",
                "heavy2"
            ]
        }
    }
}
```

{% endtab %}
{% endtabs %}

## eCommerce 캔버스 템플릿

Braze는 체크아웃 프로세스를 시작했지만 주문을 하기 전에 떠난 고객을 타겟팅하는 등 전자상거래 추천 이벤트에 의해 구동되는 미리 구축된 캔버스 템플릿을 생성했습니다. 이러한 이벤트를 사용하여 메시징을 개인화하고 특정 대상을 타겟팅하여 사용자 여정을 향상시키기 위한 정보에 기반한 결정을 내릴 수 있습니다.

캔버스 템플릿과 함께 이러한 이벤트를 사용할 수 있는 방법에 대한 더 많은 정보를 보려면 전용 [전자상거래 사용 사례]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/ecommerce_use_cases)를 확인하세요.

## 사용자 계산 필드

다음 필드에 대해 표준화된 사용자 필드 계산을 사용합니다: 

- **총 매출** = 총 주문 금액의 합계 - 총 환불 금액의 합계
- **총 주문 수** = 고유한 주문 발생 이벤트 수 - 고유한 주문 취소 수
- **총 환불 금액** = 총 환불 금액의 합계 

이 사용자 필드 계산은 사용자 프로필의 **거래** 탭에도 포함되어 있습니다.

![사용자 계산 필드가 있는 "거래" 탭.]({% image_buster /assets/img/Shopify/transactions_tab.png %}){: style="max-width:60%;"}

{% alert important %}
구매 이벤트를 단계적으로 종료할 계획은 2025년 말에 발표될 예정입니다. 장기적으로 구매 이벤트는 세분화, 보고, 분석 및 기타 기능을 향상시킨 새로운 [전자상거래 추천 이벤트]({{site.baseurl}}/user_guide/data/custom_data/recommended_events/ecommerce_events/)로 대체될 것입니다. 그러나 새로운 전자상거래 이벤트는 생애주기 가치(LTV) 또는 캔버스나 캠페인에서의 매출 보고와 같은 기존 구매 이벤트 관련 기능을 지원하지 않습니다. 구매 이벤트와 관련된 기능의 전체 목록은 [구매 이벤트 기록]({{site.baseurl}}/user_guide/data/custom_data/purchase_events/#logging-purchase-events) 섹션을 참조하십시오.
{% endalert %}
