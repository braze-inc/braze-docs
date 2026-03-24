---
nav_title: Shopify 데이터 기능
article_title: "Shopify 데이터 기능"
description: "이 참조 문서에서는 Shopify 데이터 기능을 다룹니다."
page_type: partner
search_tag: Partner
alias: /shopify_data_features/
page_order: 4
---

# Shopify 데이터 기능

> 이 문서에서는 추적되는 Shopify 데이터와 예시 페이로드, 과거 데이터 백필, 제품 동기화를 포함한 Shopify 기능에 대한 개요를 제공합니다.

## 추적되는 Shopify 이벤트

Shopify 통합은 [전자상거래 추천 이벤트]({{site.baseurl}}/user_guide/data/custom_data/recommended_events/ecommerce_events/)를 사용하여 주요 쇼핑 동작을 캡처합니다. 이러한 이벤트를 활용한 구현 사례 및 마케팅 전략은 [이커머스 활용 사례]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/ecommerce_use_cases/)를 참조하세요.

{% multi_lang_include alerts/important_alerts.md alert='Shopify customer create' %}

{% tabs %}
{% tab 예시 페이로드 %}
{% subtabs global %}
{% subtab Product viewed %}
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
        },
        "type": [
          "price_drop",
          "back_in_stock"
        ]
    }
}
```
{% endsubtab %}
{% subtab Cart updated %}
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
{% endsubtab %}
{% subtab Checkout started %}
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
{% endsubtab %}
{% subtab Order placed %}
{% raw %}
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
{% endraw %}
{% endsubtab %}
{% subtab Fulfilled order %}
```json
{
 "name": "shopify_fulfilled_order",
 "time": "2022-05-23T14:44:34-04:00",
 "properties": {
   "order_id": 4444668657855,
   "line_items": [
     {
       "quantity": 1,
       "product_id": 6143032066239,
       "sku": null,
       "title": "Dark Denim Top",
  "variant_id": 40094740549876,
       "variant_title": "Small Dark Denim Top",


       "vendor": "partners-demo",
       "name": "Dark Denim Top",
       "properties": [],
       "price": "60.00",
       "fulfillment_status": "fulfilled"
     }
   ],
   "shipping": [
     {
       "title": "Standard",
       "price": "0.00"
     }
   ],
   "total_price": "130.66",
   "confirmed": true,
   "total_discounts": "0.00",
   "discount_codes": [],
   "order_number": 1093,
   "order_status_url": "https://test-store.myshopify.com/",
   "cancelled_at": null,
   "tags": "",
   "closed_at": "2022-05-23T14:44:34-04:00",
   "fulfillment_status": "fulfilled",
   "fulfillments": [
     {
       "shipment_status": null,
       "status": "success",
       "tracking_company": "Other",
       "tracking_number": "456",
       "tracking_numbers": [
         "456"
       ],
       "tracking_url": "https://braze.com",
       "tracking_urls": [
         "https://braze.com"
       ],
       "line_items": [
         {
           "fulfillment_status": "fulfilled",
           "name": "Dark Denim Top",
           "price": "60.00",
           "product_id": 6143032066239,
           "quantity": 1,
           "requires_shipping": true,
           "sku": null,
           "title": "Dark Denim Top",
           "variant_id": 40094740549876,
           "variant_title": "Small Dark Denim Top",
           "vendor": "partners-demo"
         }
       ]
     }
   ]
 },
 "braze_id": "123abc123abc"
}
```
{% endsubtab %}
{% subtab Partially fulfilled order %}
```json
{
 "name": "shopify_partially_fulfilled_order",
 "time": "2022-05-23T14:43:34-04:00",
 "properties": {
   "order_id": 4444668657855,
   "line_items": [
     {
       "quantity": 1,
       "product_id": 6143032066239,
       "sku": null,
       "title": "Dark Denim Top",
       "variant_id": 40094740549876,
       "variant_title": "",
       "vendor": "partners-demo",
       "name": "Dark Denim Top",
       "properties": [],
       "price": "60.00",
       "fulfillment_status": "fulfilled"
     }
   ],
   "shipping": [
     {
       "title": "Standard",
       "price": "0.00"
     }
   ],
   "total_price": "130.66",
   "confirmed": true,
   "total_discounts": "0.00",
   "discount_codes": [],
   "order_number": 1093,
   "order_status_url": "https://test-store.myshopify.com/",
   "cancelled_at": null,
   "tags": "",
   "closed_at": null,
   "fulfillment_status": "partial",
   "fulfillments": [
     {
       "shipment_status": null,
       "status": "success",
       "tracking_company": "Other",
       "tracking_number": "123",
       "tracking_numbers": [
         "123"
       ],
       "tracking_url": "https://braze.com",
       "tracking_urls": [
         "https://braze.com"
       ],
       "line_items": [
         {
           "fulfillment_status": "fulfilled",
           "name": "Dark Denim Top",
           "price": "60.00",
           "product_id": 6143032066239,
           "properties": [],
           "quantity": 1,
           "requires_shipping": true,
           "sku": null,
           "title": "Dark Denim Top",
           "variant_id": 40094740549876,
           "variant_title": "",
           "vendor": "partners-demo"
         }
       ]
     }
   ]
 },
 "braze_id": "abc123abc123"
}
```
{% endsubtab %}
{% subtab Paid order %}
```json
{
 "name": "shopify_paid_order",
 "time": "2022-05-23T13:52:38-04:00",
 "properties": {
   "order_id": 4444596371647,
   "line_items": [
     {
       "quantity": 1,
       "product_id": 6143033344191,
       "sku": null,
       "title": "LED High Tops",
       "variant_id": 40094740549876,
       "variant_title": null,
       "vendor": "partners-demo",
       "name": "LED High Tops",
       "properties": [],
       "price": "80.00",
       "fulfillment_status": null
     }
   ]
 }
}
```
{% endsubtab %}
{% subtab Order cancelled %}
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
{% endsubtab %}
{% subtab Order refunded %}
```json
{
    "name": "ecommerce.order_refunded",
    "time": "2022-05-23T13:52:38-04:00",
    "properties": {
        "order_id": "820982911946154508",
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
        "metadata": {
		"order_note": "item was broken"
        }
    }
} 
```
{% endsubtab %}
{% subtab Account login %}
```json
{
	"name": "shopify_account_login",
	"properties": {
	"source": "braze-mock-storefront.myshopify.com"
  }
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Shopify 이벤트 %}
{% subtabs global %}
{% subtab Product viewed %}
**이벤트**: `ecommerce.product_viewed`<br>
**유형**: 추천 이벤트<br>
**트리거 조건**: 고객이 제품 페이지를 조회할 때<br>
**데이터 소스**: Braze SDK<br>
**활용 사례**: 탐색 이탈

{% raw %}
| 변수 | Liquid 템플릿 |
| --- | --- |
|------------------|-----------------------------------------------------|
| `product_id`       | `{{event_properties.${product_id}}}`                |
| `product_name `    | `{{event_properties.${product_name}}}`              |
| `variant_id`       | `{{event_properties.${variant_id}}}`                |
| `image_url `       | `{{event_properties.${image_url}}}`                 |
| `product_url`      | `<your-store.myshopify.com>{{event_properties.${product_url}}}` <br><br>URL 앞에 Shopify 사이트 도메인을 추가하세요. |
| `price`            | `{{event_properties.${price}}}`                     |
| `currency`         | `{{event_properties.${currency}}}`                  |
| `source`           | `{{event_properties.${source}}}`                    |
| `sku`              | `{{event_properties.${metadata}[0].sku}}`          |
| `type`             | `event_properties.${type}`          |
{: .reset-br-td-1 .reset-br-td-2 role="presentation" }
{% endraw %}

{% endsubtab %}
{% subtab Cart updated %}
**이벤트**: `ecommerce.cart_updated`<br>
**유형**: 추천 이벤트<br>
**트리거 조건**: 고객이 장바구니에 상품을 추가, 제거 또는 업데이트할 때<br>
**데이터 소스**: Braze SDK<br>
**활용 사례**: 장바구니 유기

유기한 장바구니 캔버스의 경우, 먼저 메시지에서 장바구니 컨텍스트를 얻기 위해 초기 장바구니 Liquid 태그를 추가해야 합니다.

{% raw %}
```liquid
{% shopping_cart {{context.${cart_id}}} %}
```
{% endraw %}

그런 다음 메시지에 다음 장바구니 Liquid 태그를 추가할 수 있습니다.

{% raw %}
| 변수         | Liquid 템플릿                                   |
|------------------|-----------------------------------------------------|
| `cart_id`          | `{{ shopping_cart.cart_id }}`                       |
| `currency`         | `{{ shopping_cart.currency }}`                      |
| `total_value`      | `{{ shopping_cart.total_value }}`                   |
| `product_id`       | `{{ shopping_cart.products[0].product_id }}`       |
| `product_name`     | `{{ shopping_cart.products[0].product_name }}`     |
| `variant_id`       | `{{ shopping_cart.products[0].variant_id }}`       |
| `image_url`        | `{{ shopping_cart.products[0].image_url }}`        |
| `product_url`      | `{{ shopping_cart.products[0].product_url }}`      |
| `quantity`         | `{{ shopping_cart.products[0].quantity }}`         |
| `price`            | `{{ shopping_cart.products[0].price }}`            |
| `sku`              | `{{ shopping_cart.products[0].metadata[0].sku }}`  |
| `source`           | `{{ shopping_cart.source }}`                        |
| `metadata (value)` | `{{ shopping_cart.metadata[0].<add_value_here> }}` |
{: .reset-br-td-1 .reset-br-td-2 role="presentation" }
{% endraw %}

{% alert tip %}
Liquid `for` 루프를 구축하여 이메일에 모든 제품을 동적으로 추가하는 방법에 대한 자세한 내용은 [이메일용 유기한 장바구니 제품 개인화]({{site.baseurl}}/ecommerce_use_cases/#abandoned-cart)를 참조하세요. 
{% endalert %}

{% endsubtab %}
{% subtab Checkout started %}
**이벤트**: `ecommerce.checkout_started`<br>
**유형**: 추천 이벤트<br>
**트리거 조건**: 사용자가 결제 페이지로 이동할 때<br>
**데이터 소스**: Braze REST API<br>
**활용 사례**: 결제 이탈

{% alert important %}
고객이 Shop Pay를 빠른 결제 옵션으로 사용하는 경우, Shopify가 특정 표준 결제 이벤트(예: Shopify 결제 시작 웹훅)를 건너뛸 수 있습니다. 이 경우 Braze가 결제 토큰 별칭을 추가하는 데 필요한 데이터를 수신하지 못할 수 있으며, 결제 이탈 추적 및 고객 프로필 조정에 영향을 줄 수 있습니다.
{% endalert %}

결제 이탈 캔버스의 경우, 먼저 다음 Liquid 태그를 사용해야 합니다:

{% raw %}
```liquid
{% shopping_cart {{context.${cart_id}}} :abort_if_not_abandoned false %}
{{context.${cart_id}}}
```
{% endraw %}

그런 다음 메시지에 다음 Liquid 태그를 추가하여 결제 시점의 장바구니 내 제품을 참조할 수 있습니다.

{% raw %}
| 변수         | Liquid 템플릿                                   |
|------------------|-----------------------------------------------------|
| `cart_id`          | `{{ shopping_cart.cart_id }}`                       |
| `currency`         | `{{ shopping_cart.currency }}`                      |
| `total_value`      | `{{ shopping_cart.total_value }}`                   |
| `product_id`       | `{{ shopping_cart.products[0].product_id }}`       |
| `product_name`     | `{{ shopping_cart.products[0].product_name }}`     |
| `variant_id`       | `{{ shopping_cart.products[0].variant_id }}`       |
| `image_url`        | `{{ shopping_cart.products[0].image_url }}`        |
| `product_url`      | `{{ shopping_cart.products[0].product_url }}`      |
| `quantity`         | `{{ shopping_cart.products[0].quantity }}`         |
| `price`            | `{{ shopping_cart.products[0].price }}`            |
| `sku`              | `{{ shopping_cart.products[0].metadata.sku }}`     |
| `source`           | `{{ shopping_cart.source }}`                        |
| `checkout_url`     | `{{ shopping_cart.metadata[0].checkout_url }}`     |
{: .reset-br-td-1 .reset-br-td-2 role="presentation" }
{% endraw %}

{% endsubtab %}
{% subtab Order placed %}
**이벤트**: `ecommerce.order_placed`<br>
**유형**: 추천 이벤트<br>
**트리거 조건**: 사용자가 결제 프로세스를 성공적으로 완료하고 주문할 때<br>
**데이터 소스**: Braze REST API<br>
**활용 사례**: 주문 확인, 구매 후 리타겟팅, 업셀 또는 크로스셀 

{% raw %}
| 변수                | Liquid 템플릿                                   |
|-------------------------|-----------------------------------------------------|
| cart_id                 | `{{event_properties.${cart_id}}}`                   |
| currency                | `{{event_properties.${currency}}}`                  |
| discounts               | `{{event_properties.${discounts}}}`                 |
| order_id                | `{{event_properties.${order_id}}}`                  |
| product_id              | `{{event_properties.${products}[0].product_id}}`   |
| product_name            | `{{event_properties.${products}[0].product_name}}` |
| variant_id              | `{{event_properties.${products}[0].variant_id}}`   |
| quantity                | `{{event_properties.${products}[0].quantity}}`     |
| sku                     | `{{event_properties.${products}[0].metadata.sku}}` |
| total_discounts         | `{{event_properties.${total_discounts}}}`           |
| order_status_url        | `{{event_properties.${metadata}.order_status_url}}` |
| order_number            | `{{event_properties.${metadata}.order_number}}`     |
| tags                    | `{{event_properties.${metadata}.tags}}`             |
| referring_site          | `{{event_properties.${metadata}.referring_site}}`   |
| payment_gateway_names    | `{{event_properties.${metadata}.payment_gateway_names}}` |
{: .reset-br-td-1 .reset-br-td-2 role="presentation" }
{% endraw %}

{% alert tip %}
Shopify의 결제 완료 웹훅에는 제품 URL이나 이미지 URL이 포함되지 않습니다. 따라서 [이메일용 주문 확인 및 피드백 설문조사]({{site.baseurl}}/ecommerce_use_cases/#order-confirmation-and-feedback-survey)에서 언급된 카탈로그 Liquid 개인화를 사용해야 합니다. 
{% endalert %}

{% endsubtab %}
{% subtab Fulfilled order %}
**이벤트**: `shopify_fulfilled_order`<br>
**유형**: [커스텀 이벤트]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)<br>
**트리거 조건**: 사용자의 주문이 이행되어 배송 준비가 완료될 때<br>
**데이터 소스**: Braze REST API<br>
**활용 사례**: (트랜잭션) 이행 업데이트 

{% raw %}
| 변수 | Liquid 템플릿 |
| --- | --- |
| Order ID | `{{event_properties.${order_id}}}` |
| Total Price | `{{event_properties.${total_price}}}` |
| Total Discounts | `{{event_properties.${total_discounts}}}` |
| Confirmed Status | `{{event_properties.${confirmed}}}` |
| Order Status URL | `{{event_properties.${order_status_url}}}` |
| Order Number | `{{event_properties.${order_number}}}` |
| Cancelled Timestamp | `{{event_properties.${cancelled_at}}}` |
| Closed Timestamp | `{{event_properties.${closed_at}}}` |
| Item ID | `{{event_properties.${line_items}[0].product_id}}` |
| Item Quantity | `{{event_properties.${line_items}[0].quantity}}` |
| Item SKU | `{{event_properties.${line_items}[0].sku}}` |
| Item Title | `{{event_properties.${line_items}[0].title}}` |
| Item Vendor | `{{event_properties.${line_items}[0].vendor}}` |
| Item Name | `{{event_properties.${line_items}[0].name}}` |
| Item Properties | `{{event_properties.${line_items}[0].properties}}` |
| Item Price | `{{event_properties.${line_items}[0].price}}` |
| Shipping Title | `{{event_properties.${shipping}[0].title}}` |
| Shipping Price | `{{event_properties.${shipping}[0].price}}` |
| Fulfillment Status | `{{event_properties.${fulfillment_status}}}` |
| Fulfillment Shipment Status | `{{event_properties.${fulfillments}[0].shipment_status}}` |
| Status | `{{event_properties.${fulfillments}[0].status}}` |
| Fulfillment Tracking Company | `{{event_properties.${fulfillments}[0].Fulfillment tracking_company}}` |
| Fulfillment Tracking Number | `{{event_properties.${fulfillments}[0].Fulfillment tracking_number}}` |
| Fulfillment Tracking Numbers | `{{event_properties.${fulfillments}[0].Fulfillment tracking_numbers}}` |
| Fulfillment Tracking URL | `{{event_properties.${fulfillments}[0].Fulfillment tracking_url}}` |
| Fulfillment Tracking URLs | `{{event_properties.${fulfillments}[0].Fulfillment tracking_urls}}` |
| Fulfillment Status | `{{event_properties.${fulfillments}[0].line_items[0].fulfillment_status}}` |
| Fulfillment Name | `{{event_properties.${fulfillments}[0].line_items[0].name}}` |
| Fulfillment Price | `{{event_properties.${fulfillments}[0].line_items[0].price}}` |
| Fulfillment Product ID | `{{event_properties.${fulfillments}[0].line_items[0].product_id}}` |
| Fulfillment Quantity | `{{event_properties.${fulfillments}[0].line_items[0].quantity}}`|
| Fulfillment Shipping | `{{event_properties.${fulfillments}[0].line_items[0].requires_shipping}}` |
| Fulfillment SKU | `{{event_properties.${fulfillments}[0].line_items[0].sku}}` |
| Fulfillment Title | `{{event_properties.${fulfillments}[0].line_items[0].title}}` |
| Fulfillment Vendor | `{{event_properties.${fulfillments}[0].line_items[0].vendor}}` |
| Variant ID | `{{event_properties.${line_items}[0].variant_id}}` |
| Variant Title | `{{event_properties.${line_items}[0].variant_title}}` |
{: .reset-br-td-1 .reset-br-td-2 role="presentation" }
{% endraw %}

{% endsubtab %}
{% subtab Partially fulfilled order %}
**이벤트**: `shopify_partially_fulfilled_order`<br>
**유형**: [커스텀 이벤트]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)<br>
**트리거 조건**: 사용자 주문의 일부가 이행되어 배송 준비가 완료될 때<br> 
**데이터 소스**: Braze REST API<br>
**활용 사례**: (트랜잭션) 이행 업데이트 

{% raw %}
| 변수 | Liquid 템플릿 |
| --- | --- |
| Order ID | `{{event_properties.${order_id}}}` |
| Total Price | `{{event_properties.${total_price}}}` |
| Total Discounts | `{{event_properties.${total_discounts}}}` |
| Confirmed Status | `{{event_properties.${confirmed}}}` |
| Order Status URL | `{{event_properties.${order_status_url}}}` |
| Order Number | `{{event_properties.${order_number}}}` |
| Cancelled Timestamp | `{{event_properties.${cancelled_at}}}` |
| Closed Timestamp | `{{event_properties.${closed_at}}}` |
| Item ID | `{{event_properties.${line_items}[0].product_id}}` |
| Item Quantity | `{{event_properties.${line_items}[0].quantity}}` |
| Item SKU | `{{event_properties.${line_items}[0].sku}}` |
| Item Title | `{{event_properties.${line_items}[0].title}}` |
| Item Vendor | `{{event_properties.${line_items}[0].vendor}}` |
| Item Name | `{{event_properties.${line_items}[0].name}}` |
| Item Properties | `{{event_properties.${line_items}[0].properties}}` |
| Item Price | `{{event_properties.${line_items}[0].price}}` |
| Shipping Title | `{{event_properties.${shipping}[0].title}}` |
| Shipping Price | `{{event_properties.${shipping}[0].price}}` |
| Fulfillment Status | `{{event_properties.${fulfillment_status}}}` |
| Fulfillment Shipment Status | `{{event_properties.${fulfillments}[0].shipment_status}}` |
| Fulfillment Status | `{{event_properties.${fulfillments}[0].status}}` |
| Fulfillment Tracking Company | `{{event_properties.${fulfillments}[0].tracking_company}}` |
| Fulfillment Tracking Number | `{{event_properties.${fulfillments}[0].tracking_number}}` |
| Fulfillment Tracking Numbers | `{{event_properties.${fulfillments}[0].tracking_numbers}}` |
| Fulfillment Tracking URL | `{{event_properties.${fulfillments}[0].tracking_url}}` |
| Fulfillment Tracking URLs | `{{event_properties.${fulfillments}[0].tracking_urls}}` |
| Fulfillment Status | `{{event_properties.${fulfillments}[0].line_items[0].fulfillment_status}}` |
| Fulfillment Name | `{{event_properties.${fulfillments}[0].line_items[0].name}}` |
| Fulfillment Price | `{{event_properties.${fulfillments}[0].line_items[0].price}}` |
| Fulfillment Product ID | `{{event_properties.${fulfillments}[0].line_items[0].product_id}}` |
| Fulfillment Quantity | `{{event_properties.${fulfillments}[0].line_items[0].quantity}}`|
| Fulfillment Shipping | `{{event_properties.${fulfillments}[0].line_items[0].requires_shipping}}` |
| Fulfillment SKU | `{{event_properties.${fulfillments}[0].line_items[0].sku}}` |
| Fulfillment Title | `{{event_properties.${fulfillments}[0].line_items[0].title}}` |
| Fulfillment Vendor | `{{event_properties.${fulfillments}[0].line_items[0].vendor}}` |
| Variant ID | `{{event_properties.${line_items}[0].variant_id}}` |
| Variant Title | `{{event_properties.${line_items}[0].variant_title}}` |
{: .reset-br-td-1 .reset-br-td-2 role="presentation" }
{% endraw %}

{% endsubtab %}
{% subtab Paid order %}
**이벤트**: `shopify_paid_order`<br>
**유형**: [커스텀 이벤트]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)<br>
**트리거 조건**: Shopify에서 사용자의 주문이 결제 완료로 표시될 때<br>
**데이터 소스**: Braze REST API<br>
**활용 사례**: (트랜잭션) 결제 확인

{% raw %}
| 변수 | Liquid 템플릿 |
| --- | --- |
| Order ID | `{{event_properties.${order_id}}}` |
| Confirmed Status | `{{event_properties.${confirmed}}}` |
| Order Status URL | `{{event_properties.${order_status_url}}}` |
| Order Number | `{{event_properties.${order_number}}}` |
| Cancelled Timestamp | `{{event_properties.${cancelled_at}}}` |
| Total Discounts | `{{event_properties.${total_discounts}}}` |
| Total Price | `{{event_properties.${total_price}}}` |
| Tags | `{{event_properties.${tags}}}` |
| Discount Codes | `{{event_properties.${discount_codes}}}` |
| Item ID | `{{event_properties.${line_items}[0].product_id}}` |
| Item Quantity | `{{event_properties.${line_items}[0].quantity}}` |
| Item SKU | `{{event_properties.${line_items}[0].sku}}` |
| Item Title | `{{event_properties.${line_items}[0].title}}` |
| Item Vendor | `{{event_properties.${line_items}[0].vendor}}` |
| Item Properties | `{{event_properties.${line_items}[0].properties}}` |
| Item Price | `{{event_properties.${line_items}[0].price}}` |
| Shipping Title | `{{event_properties.${shipping}[0].title}}` |
| Shipping Price | `{{event_properties.${shipping}[0].price}}` |
| Variant ID | `{{event_properties.${line_items}[0].variant_id}}` |
| Variant Title | `{{event_properties.${line_items}[0].variant_title}}` |
{: .reset-br-td-1 .reset-br-td-2 role="presentation" }
{% endraw %}

{% endsubtab %}
{% subtab Order cancelled %}
**이벤트**: `shopify_cancelled_order`<br>
**유형**: [커스텀 이벤트]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)<br>
**트리거 조건**: 사용자의 주문이 취소될 때<br> 
**데이터 소스**: Braze REST API<br>
**활용 사례**: (트랜잭션) 주문 취소 확인

{% raw %}
| 변수 | Liquid 템플릿 |
| --- | --- |
| Order ID | `{{event_properties.${order_id}}}` |
| Total Price | `{{event_properties.${total_price}}}` |
| Total Discounts | `{{event_properties.${total_discounts}}}` |
| Confirmed | `{{event_properties.${confirmed}}}` |
| Order Status URL | `{{event_properties.${order_status_url}}}` |
| Order Number | `{{event_properties.${order_number}}}` |
| Cancelled Timestamp | `{{event_properties.${cancelled_at}}}` |
| Tags | `{{event_properties.${tags}}}` |
| Discount Codes | `{{event_properties.${discount_codes}}}` |
| Fulfillment Status | `{{event_properties.${fulfillment_status}}}` |
| Fulfillments | `{{event_properties.${fulfillments}}}` |
| Item ID | `{{event_properties.${line_items}[0].product_id}}` |
| Item Quantity | `{{event_properties.${line_items}[0].quantity}}` |
| Item SKU | `{{event_properties.${line_items}[0].sku}}` |
| Item Title | `{{event_properties.${line_items}[0].title}}` |
| Item Vendor | `{{event_properties.${line_items}[0].vendor}}` |
| Item Name | `{{event_properties.${line_items}[0].name}}` |
| Item Properties | `{{event_properties.${line_items}[0].properties}}` |
| Fulfillment Status | `{{event_properties.${line_items}[0].fulfillment_status}}` |
| Shipping Title | `{{event_properties.${shipping}[0].title}}` |
| Shipping Price | `{{event_properties.${shipping}[0].price}}` |
| Variant ID | `{{event_properties.${line_items}[0].variant_id}}` |
| Variant Title | `{{event_properties.${line_items}[0].variant_title}}` |
{: .reset-br-td-1 .reset-br-td-2 role="presentation" }
{% endraw %}
{% endsubtab %}
{% subtab Order refunded %}
**이벤트**: `shopify_order_refunded`<br>
**유형**: [커스텀 이벤트]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)<br>
**트리거 조건**: 사용자의 주문이 환불될 때<br>
**데이터 소스**: Braze REST API<br>
**활용 사례**: (트랜잭션) 환불 확인

{% raw %}
| 변수 | Liquid 템플릿 |
| --- | --- |
| Order ID | `{{event_properties.${order_id}}}` |
| Order Note | `{event_properties.${note}}}` |
| Item ID | `{{event_properties.${line_items}[0].product_id}}` |
| Item Quantity | `{{event_properties.${line_items}[0].quantity}}` |
| Item SKU | `{{event_properties.${line_items}[0].sku}}` |
| Item Title | `{{event_properties.${line_items}[0].title}}` |
| Item Vendor | `{{event_properties.${line_items}[0].vendor}}` |
| Item Name | `{{event_properties.${line_items}[0].name}}` |
| Item Properties | `{{event_properties.${line_items}[0].properties}}` |
| Item Price | `{{event_properties.${line_items}[0].price}}` |
| Variant ID | `{{event_properties.${line_items}[0].variant_id}}` |
| Variant Title | `{{event_properties.${line_items}[0].variant_title}}` |
{: .reset-br-td-1 .reset-br-td-2 role="presentation" }
{% endraw %}

{% endsubtab %}
{% subtab Account login %}

**이벤트**: `shopify_account_login`<br>
**유형**: [커스텀 이벤트]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)<br>
**트리거 조건**: 사용자가 계정에 로그인할 때<br>
**데이터 소스**: Braze REST API<br>
**활용 사례**: 웰컴 시리즈

{% raw %}
| 변수 | Liquid 템플릿 |
| --- | --- |
| `source` | {{event_properties.${source}}} |
{: .reset-br-td-1 .reset-br-td-2 role="presentation" }
{% endraw %}

{% alert note %}
Shopify 통합은 현재 Braze [구매 이벤트]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events#purchase-events) 채우기를 지원하지 않습니다. 따라서 구매 필터, Liquid 태그, 액션 기반 트리거 및 분석에는 `ecommerce.order_placed` 이벤트를 사용해야 합니다. 
{% endalert %}

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## 지원되는 Shopify 커스텀 속성

{% multi_lang_include alerts/note_alerts.md alert='Shopify attributes REST API' %}

{% tabs local %}
{% tab 예시 페이로드 %}
{% subtabs %}
{% subtab Shopify Tags %}
```json
{
  "attributes": [
    {
      "shopify_tags": "VIP_customer",
      "shopify_total_spent": "60.00",
      "shopify_order_count": "3",
      "shopify_last_order_id": "1234567",
      "shopify_last_order_name": "test_order",
      "shopify_zipcode": "10001",
      "shopify_province": "null"
    }
  ]
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Shopify 커스텀 속성 %}
| 속성 이름 | 설명 |
| --- | --- |
| `shopify_total_spent` | 고객이 주문 내역 전체에서 지출한 총 금액입니다. |
| `shopify_order_count` | 이 고객과 연결된 주문 수입니다. 테스트 및 아카이브된 주문은 포함되지 않습니다. |
| `shopify_last_order_id` | 고객의 마지막 주문 ID입니다. |
| `shopify_last_order_name` | 고객의 마지막 주문 이름입니다. 이는 주문 리소스의 `name` 필드와 직접 관련됩니다. |
| `shopify_zipcode` | 고객의 기본 주소에 있는 우편번호입니다. |
| `shopify_province` | 고객의 기본 주소에 있는 시/도입니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert important %}
현재 Shopify API 버전의 알려진 문제로 인해 `shopify_last_order_name` 사용자 속성이 올바르게 채워지지 않습니다. 사용자에게 미치는 영향은 다음과 같습니다:<br><br>

- **기존 사용자:** 이미 `shopify_last_order_name` 값이 있는 사용자의 경우 해당 값은 유지되지만 후속 주문에 의해 업데이트되지 않습니다.
- **신규 사용자:** 새 사용자의 경우 필드가 채워지지 않고 비어 있거나 null로 유지됩니다.

이 페이지는 Shopify에서 이 문제를 해결한 후에 업데이트됩니다.
{% endalert %}

### Liquid 개인화

Shopify 커스텀 속성에 대한 Liquid 개인화를 추가하려면 **+ Personalization**을 선택합니다. 그런 다음 개인화 유형으로 **Custom Attributes**를 선택합니다.

!['속성' 드롭다운이 확장된 '개인화 추가' 섹션.]({% image_buster /assets/img/Shopify/add_personalization_2.png %}){: style="max-width:40%;"}

커스텀 속성을 선택한 후 기본값을 입력하고 Liquid 스니펫을 메시지에 복사합니다.

![Liquid 스니펫을 메시지에 붙여넣기.]({% image_buster /assets/img/Shopify/copy_liquid_snippet.png %})
{% endtab %}
{% endtabs %}

## 지원되는 Shopify 표준 속성

{% multi_lang_include alerts/note_alerts.md alert='Shopify attributes REST API' %}

- Email
- First Name
- Last Name
- Phone
- City
- Country

{% alert note %}
Braze는 기존 고객 프로필의 데이터와 차이가 있는 경우에만 지원되는 Shopify 커스텀 속성 및 Braze 표준 속성을 업데이트합니다. 예를 들어, 수신된 Shopify 데이터에 이름이 Bob으로 포함되어 있고 Braze 고객 프로필에 이미 Bob이 이름으로 존재하는 경우, Braze는 업데이트를 트리거하지 않으며 데이터 포인트가 차감되지 않습니다.
{% endalert %}

## SDK 데이터 수집 

Braze SDK가 수집하는 데이터에 대한 자세한 내용은 [SDK 데이터 수집]({{site.baseurl}}/user_guide/data/user_data_collection/sdk_data_collection/)을 참조하세요. 

## 과거 데이터 백필

Shopify 스토어 온보딩 중에 과거 데이터 백필을 통해 초기 데이터 동기화를 시작하여 고객과 즉시 소통할 수 있습니다. 이 백필의 일환으로 Braze는 Shopify 통합 연결 이전 최근 90일간의 모든 고객 및 주문 완료 이벤트에 대한 초기 데이터 동기화를 실행합니다. Braze가 Shopify 고객을 가져올 때 구성 설정에서 선택한 `external_id` 유형을 할당합니다.

{% alert note %}
커스텀 외부 ID로 통합할 계획인 경우([표준 통합]({{site.baseurl}}/partners/ecommerce/shopify/shopify_standard_integration/#step-4-configure-how-you-manage-users) 또는 [커스텀 통합]({{site.baseurl}}/partners/ecommerce/shopify/shopify_custom_integration/#step-6-configure-how-you-manage-users-optional) 모두 해당), 모든 기존 Shopify 고객 프로필에 커스텀 외부 ID를 Shopify 고객 메타필드로 추가한 후 과거 데이터 백필을 수행해야 합니다. 
{% endalert %}

동기화된 주문 이벤트 데이터는 세분화에 사용할 수 있지만, 매출 데이터 자체는 고객 프로필이나 [매출 - 라스트 터치 기여도 대시보드]({{site.baseurl}}/user_guide/analytics/reporting/dashboard_builder/#revenue---last-touch-attribution)에 채워지지 않습니다.

### Shopify 과거 데이터 백필 설정

1. **Shopify 데이터 추적** 단계에서 과거 데이터 백필을 켭니다.

![과거 데이터 백필이 선택된 Shopify 통합의 "Shopify 데이터 추적" 단계.]({% image_buster /assets/img/Shopify/historical_data_backfill_sync.png %})

{: start="2"}

2. 통합 설정을 완료하면 Braze가 초기 데이터 동기화를 시작합니다. 통합 설정의 **Shopify Data** 탭에서 진행 상황을 모니터링할 수 있습니다. 

![이벤트가 활발하게 동기화 중임을 나타내는 스피너가 있는 Shopify 통합 설정 페이지.]({% image_buster /assets/img/Shopify/historical_data_backfill_syncing.png %})

### 동기화된 데이터 

초기 데이터 동기화에서 Braze는 Shopify 통합 연결 이전 최근 90일간의 고객 및 주문 완료 데이터를 가져옵니다. Braze가 Shopify 고객을 가져올 때 구성 설정에서 선택한 `external_id` 유형을 할당합니다.