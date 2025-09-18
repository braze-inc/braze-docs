---
nav_title: Shopify Data Features
article_title: "Shopify Data Features"
description: "This reference article covers Shopify data features."
page_type: partner
search_tag: Partner
alias: /shopify_data_features/
page_order: 3
---

# Shopify data features

> This article provides an overview of our Shopify features, including what Shopify data is tracked and example payloads, historical backfill, and product syncs.

## Tracked Shopify events

{% tabs %}
{% tab 페이로드 예제 %}
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
   ],
 }
}
```
{% endsubtab %}
{% subtab Order cancelled %}
```json
{
 "name": "shopify_cancelled_order",
 "time": "2022-05-23T14:40:52-04:00",
 "properties": {
   "order_id": 4444596371647,
   "line_items": [
     {
       "quantity": 1,
       "product_id": 6143033344191,
       "sku": null,
       "title": "LED High Tops",
       "variant_id": 40094740549876,
       "variant_title": "",
       "vendor": "partners-demo",
       "name": "LED High Tops",
       "properties": [],
       "price": "80.00",
       "fulfillment_status": null
     }
   ],
   "shipping": [
     {
       "title": "Standard",
       "price": "0.00"
     }
   ],
   "total_price": "141.54",
   "confirmed": true,
   "total_discounts": "0.00",
   "discount_codes": [],
   "order_number": 1092,
   "order_status_url": "https://test-store.myshopify.com/",
   "cancelled_at": "2022-05-23T14:40:52-04:00",
   "tags": "",
   "closed_at": "2022-05-23T14:40:51-04:00",
   "fulfillment_status": null,
   "fulfillments": []
 },
 "braze_id": "123abc123abc"
}
```
{% endsubtab %}
{% subtab Order refunded %}
```json
{
 "name": "shopify_created_refund",
 "time": "2022-05-23T14:40:50-04:00",
 "properties": {
   "order_id": 4444596371647,
   "note": null,
   "line_items": [
     {
       "quantity": 1,
       "product_id": 6143033344191,
       "sku": null,
       "title": "LED High Tops",
       "variant_id": 40094740549876,
       "variant_title": "",
       "vendor": "partners-demo",
       "properties": [],
       "price": "80.00"
     },
     {
       "quantity": 1,
       "product_id": 6143032852671,
       "sku": null,
       "title": "Chequered Red Shirt",
       "variant_id": 40094796619876,
       "variant_title": "",
       "vendor": "partners-demo",
       "properties": [],
       "price": "50.00"
     }
   ]
 },
 "braze_id": "abc123abc123"
}
```
{% endsubtab %}
{% subtab Account login %}
```json
{
	name: "shopify_account_login",
	properties: {
	source: "braze-mock-storefront.myshopify.com"
  }
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Shopify events %}
{% subtabs global %}
{% subtab Product viewed %}
**이벤트**: `ecommerce.v1.product_viewed`<br>
**유형**: Recommended event<br>
**Triggered**: When a customer views a product page<br>
**Use Case**: 유기 찾아보기

{% raw %}
| Variable | Liquid templating |
| --- | --- |
\|------------------|-----------------------------------------------------|
| `product_id`       | `{{event_properties.${product_id}}}`                |
| `product_name `    | `{{event_properties.${product_name}}}`              |
| `variant_id`       | `{{event_properties.${variant_id}}}`                |
| `image_url `       | `{{event_properties.${image_url}}}`                 |
| `product_url`      | `<your-store.myshopify.com>{{event_properties.${product_url}}}` <br><br>Add your Shopify site domain before the URL. |
| `price`            | `{{event_properties.${price}}}`                     |
| `currency`         | `{{event_properties.${currency}}}`                  |
| `source`           | `{{event_properties.${source}}}`                    |
| `sku`              | `{{event_properties.${metadata}[0].sku}}`          |
| `type`             | `event_properties.${type}`          |
{: .reset-br-td-1 .reset-br-td-2 role="presentation" }
{% endraw %}

{% endsubtab %}
{% subtab Cart updated %}
**이벤트**: `ecommerce.v1.cart_updated`<br>
**유형**: Recommended event<br>
**Triggered**: When a customer adds, removes, or updates their shopping cart<br>
**Use Case**: 장바구니 포기

For Abandoned Cart Canvases, you first need to add the initial shopping cart Liquid tag to gain context of the shopping cart in your message. 

{% raw %}
```liquid
{% shopping_cart {{context.${cart_id}}} %}
```
{% endraw %}

Then you can add the following shopping cart Liquid tags into your message.

{% raw %}
| Variable         | Liquid templating                                   |
\|------------------|-----------------------------------------------------|
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
For more information on how to build out a Liquid `for` loop to dynamically add all products into your email, refer to [Abandoned Cart product personalization for emails]({{site.baseurl}}/ecommerce_use_cases/#abandoned-cart).
{% endalert %}

{% endsubtab %}
{% subtab Checkout started %}
**이벤트**: `ecommerce.v1.checkout_started`<br>
**유형**: Recommended event<br>
**Triggered**: When a customer adds, removes, or updates their shopping cart<br>
**Use Case**: Checkout abandonment

For Abandoned Checkout Canvases, you first need to use the following Liquid tag:

{% raw %}
```liquid
{% shopping_cart {{context.${cart_id}}} :abort_if_not_abandoned false %}
{{context.${cart_id}}}
```
{% endraw %}

Then you can add the following Liquid tags into your message to reference the products within your cart at the point of checkout.

{% raw %}
| Variable         | Liquid templating                                   |
\|------------------|-----------------------------------------------------|
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
**이벤트**: `ecommerce.v1.order_placed`<br>
**유형**: Recommended event<br>
**Triggered**: When a user successfully completes the checkout process and places an order<br>
**Use Case**: Order confirmation, post-purchase retargeting, upsells or cross-sells 

{% raw %}
| Variable                | Liquid templating                                   |
\|-------------------------|-----------------------------------------------------|
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
Shopify’s checkout completed webhook doesn't contain product URLs or image URLs. As a result, you need to use Catalogs Liquid personalization as mentioned in [Abandoned Cart product personalization for emails]({{site.baseurl}}/ecommerce_use_cases/#order-confirmation-and-feedback-survey).
{% endalert %}

{% endsubtab %}
{% subtab Fulfilled order %}
**이벤트**: `shopify_fulfilled_order`<br>
**유형**: [커스텀 이벤트]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events)<br>
**Triggered**: When a user’s order is fulfilled and ready for shipping<br>
**Use Case**: (Transactional) Fulfillment update 

{% raw %}
| Variable | Liquid templating |
| --- | --- |
| 주문 ID | `{{event_properties.${order_id}}}` |
| 총 가격 | `{{event_properties.${total_price}}}` |
| 총 할인 | `{{event_properties.${total_discounts}}}` |
| 확인 상태 | `{{event_properties.${confirmed}}}` |
| 주문 상태 URL | `{{event_properties.${order_status_url}}}` |
| 주문 번호 | `{{event_properties.${order_number}}}` |
| 취소된 타임스탬프 | `{{event_properties.${cancelled_at}}}` |
| 비공개 타임스탬프 | `{{event_properties.${closed_at}}}` |
| 아이템 ID | `{{event_properties.${line_items}[0].product_id}}` |
| 아이템 수량 | `{{event_properties.${line_items}[0].quantity}}` |
| 상품 SKU | `{{event_properties.${line_items}[0].sku}}` |
| 항목 제목 | `{{event_properties.${line_items}[0].title}}` |
| 항목 제공업체 | `{{event_properties.${line_items}[0].vendor}}` |
| 항목 이름 | `{{event_properties.${line_items}[0].name}}` |
| 항목 속성정보 | `{{event_properties.${line_items}[0].properties}}` |
| 아이템 가격 | `{{event_properties.${line_items}[0].price}}` |
| 배송 제목 | `{{event_properties.${shipping}[0].title}}` |
| 배송비 | `{{event_properties.${shipping}[0].price}}` |
| 주문 처리 상태 | `{{event_properties.${fulfillment_status}}}` |
| 주문 처리 배송 상태 | `{{event_properties.${fulfillments}[0].shipment_status}}` |
| 상태 | `{{event_properties.${fulfillments}[0].status}}` |
| 주문 처리 추적 회사 | `{{event_properties.${fulfillments}[0].Fulfillment tracking_company}}` |
| 주문 처리 추적 번호 | `{{event_properties.${fulfillments}[0].Fulfillment tracking_number}}` |
| 주문 처리 추적 번호 | `{{event_properties.${fulfillments}[0].Fulfillment tracking_numbers}}` | 주문 처리 추적 번호
| 주문 처리 추적 URL | `{{event_properties.${fulfillments}[0].Fulfillment tracking_url}}` |
| 주문 처리 추적 URL | `{{event_properties.${fulfillments}[0].Fulfillment tracking_urls}}` |
| 주문 처리 상태 | `{{event_properties.${fulfillments}[0].line_items[0].fulfillment_status}}` |
| 주문 처리 이름 | `{{event_properties.${fulfillments}[0].line_items[0].name}}` |
| 주문 처리 가격 | `{{event_properties.${fulfillments}[0].line_items[0].price}}` |
| 주문 처리 제품 ID | `{{event_properties.${fulfillments}[0].line_items[0].product_id}}` |
| 주문 처리 수량 | `{{event_properties.${fulfillments}[0].line_items[0].quantity}}`|
| 주문 처리 배송 | `{{event_properties.${fulfillments}[0].line_items[0].requires_shipping}}` |
| 주문 처리 SKU | `{{event_properties.${fulfillments}[0].line_items[0].sku}}` |
| 주문 처리 제목 | `{{event_properties.${fulfillments}[0].line_items[0].title}}` |
| 주문 처리 공급업체 | `{{event_properties.${fulfillments}[0].line_items[0].vendor` |
| 배리언트 ID | `{{event_properties.${line_items}[0].variant_id}}` |
| 배리언트 제목 | `{{event_properties.${line_items}[0].variant_title}}` |
{: .reset-br-td-1 .reset-br-td-2 role="presentation" }
{% endraw %}

{% endsubtab %}
{% subtab Partially fulfilled order %}
**이벤트**: `shopify_partially_fulfilled_order`<br>
**유형**: [커스텀 이벤트]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events)<br>
**Triggered**: When part of a user’s order is fulfilled and ready for shipping<br> 
**Use Case**: (Transactional) Fulfillment update 

{% raw %}
| Variable | Liquid templating |
| --- | --- |
| 주문 ID | `{{event_properties.${order_id}}}` |
| 총 가격 | `{{event_properties.${total_price}}}` |
| 총 할인 | `{{event_properties.${total_discounts}}}` |
| 확인 상태 | `{{event_properties.${confirmed}}}` |
| 주문 상태 URL | `{{event_properties.${order_status_url}}}` |
| 주문 번호 | `{{event_properties.${order_number}}}` |
| 취소된 타임스탬프 | `{{event_properties.${cancelled_at}}}` |
| 비공개 타임스탬프 | `{{event_properties.${closed_at}}}` |
| 아이템 ID | `{{event_properties.${line_items}[0].product_id}}` |
| 아이템 수량 | `{{event_properties.${line_items}[0].quantity}}` |
| 상품 SKU | `{{event_properties.${line_items}[0].sku}}` |
| 항목 제목 | `{{event_properties.${line_items}[0].title}}` |
| 항목 제공업체 | `{{event_properties.${line_items}[0].vendor}}` |
| 항목 이름 | `{{event_properties.${line_items}[0].name}}` |
| 항목 속성정보 | `{{event_properties.${line_items}[0].properties}}` |
| 아이템 가격 | `{{event_properties.${line_items}[0].price}}` |
| 배송 제목 | `{{event_properties.${shipping}[0].title}}` |
| 배송비 | `{{event_properties.${shipping}[0].price}}` |
| 주문 처리 상태 | `{{event_properties.${fulfillment_status}}}` |
| 주문 처리 배송 상태 | `{{event_properties.${fulfillments}[0].shipment_status}}` |
| 주문 처리 상태 | `{{event_properties.${fulfillments}[0].status}}` |
| 주문 처리 추적 회사 | `{{event_properties.${fulfillments}[0].tracking_company}}` |
| 주문 처리 추적 번호 | `{{event_properties.${fulfillments}[0].tracking_number}}` |
| 주문 처리 추적 번호 | `{{event_properties.${fulfillments}[0].tracking_numbers}}` | 주문 처리 추적 번호
| 주문 처리 추적 URL | `{{event_properties.${fulfillments}[0].tracking_url}}` |
| 주문 처리 추적 URL | `{{event_properties.${fulfillments}[0].tracking_urls}}` |
| 주문 처리 상태 | `{{event_properties.${fulfillments}[0].line_items[0].fulfillment_status}}` |
| 주문 처리 이름 | `{{event_properties.${fulfillments}[0].line_items[0].name}}` |
| 주문 처리 가격 | `{{event_properties.${fulfillments}[0].line_items[0].price}}` |
| 주문 처리 제품 ID | `{{event_properties.${fulfillments}[0].line_items[0].product_id}}` |
| 주문 처리 수량 | `{{event_properties.${fulfillments}[0].line_items[0].quantity}}`|
| 주문 처리 배송 | `{{event_properties.${fulfillments}[0].line_items[0].requires_shipping}}` |
| 주문 처리 SKU | `{{event_properties.${fulfillments}[0].line_items[0].sku}}` |
| 주문 처리 제목 | `{{event_properties.${fulfillments}[0].line_items[0].title}}` |
| 주문 처리 공급업체 | `{{event_properties.${fulfillments}[0].line_items[0].vendor` |
| 배리언트 ID | `{{event_properties.${line_items}[0].variant_id}}` |
| 배리언트 제목 | `{{event_properties.${line_items}[0].variant_title}}` |
{: .reset-br-td-1 .reset-br-td-2 role="presentation" }
{% endraw %}

{% endsubtab %}
{% subtab Paid order %}
**이벤트**: `shopify_paid_order`<br>
**유형**: [커스텀 이벤트]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events)<br>
**Triggered**: When a user’s order is marked as paid within Shopify<br>  
**Use Case**: (Transactional) Payment confirmation

{% raw %}
| Variable | Liquid templating |
| --- | --- |
| 주문 ID | `{{event_properties.${order_id}}}` |
| 확인 상태 | `{{event_properties.${confirmed}}}` |
| 주문 상태 URL | `{{event_properties.${order_status_url}}}` |
| 주문 번호 | `{{event_properties.${order_number}}}` |
| 취소된 타임스탬프 | `{{event_properties.${cancelled_at}}}` |
| 총 할인 | `{{event_properties.${total_discounts}}}` |
| 총 가격 | `{{event_properties.${total_price}}}` |
| 태그 | `{{event_properties.${tags}}}` |
| 할인 코드 | `{{event_properties.${discount_codes}}}` |
| 아이템 ID | `{{event_properties.${line_items}[0].product_id}}` |
| 아이템 수량 | `{{event_properties.${line_items}[0].quantity}}` |
| 상품 SKU | `{{event_properties.${line_items}[0].sku}}` |
| 항목 제목 | `{{event_properties.${line_items}[0].title}}` |
| 항목 제공업체 | `{{event_properties.${line_items}[0].vendor}}` |
| 항목 속성정보 | `{{event_properties.${line_items}[0].properties}}` |
| 아이템 가격 | `{{event_properties.${line_items}[0].price}}` |
| 배송 제목 | `{{event_properties.${shipping}[0].title}}` |
| 배송비 | `{{event_properties.${shipping}[0].price}}` |
| 배리언트 ID | `{{event_properties.${line_items}[0].variant_id}}` |
| 배리언트 제목 | `{{event_properties.${line_items}[0].variant_title}}` |
{: .reset-br-td-1 .reset-br-td-2 role="presentation" }
{% endraw %}

{% endsubtab %}
{% subtab Order cancelled %}
**이벤트**: `shopify_cancelled_order`<br>
**유형**: [커스텀 이벤트]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events)<br>
**Triggered**: When a user’s order is cancelled<br> 
**Use Case**: (Transactional) Order cancellation confirmation

{% raw %}
| Variable | Liquid templating |
| --- | --- |
| 주문 ID | `{{event_properties.${order_id}}}` |
| 총 가격 | `{{event_properties.${total_price}}}` |
| 총 할인 | `{{event_properties.${total_discounts}}}` |
| 확인됨 | `{{event_properties.${confirmed}}}` |
| 주문 상태 URL | `{{event_properties.${order_status_url}}}` |
| 주문 번호 | `{{event_properties.${order_number}}}` |
| 취소된 타임스탬프 | `{{event_properties.${cancelled_at}}}` |
| 태그 | `{{event_properties.${tags}}}` |
| 할인 코드 | `{{event_properties.${discount_codes}}}` |
| 주문 처리 상태 | `{{event_properties.${fulfillment_status}}}` |
| 주문 처리 | `{{event_properties.${fulfillments}}}` |
| 아이템 ID | `{{event_properties.${line_items}[0].product_id}}` |
| 아이템 수량 | `{{event_properties.${line_items}[0].quantity}}` |
| 상품 SKU | `{{event_properties.${line_items}[0].sku}}` |
| 항목 제목 | `{{event_properties.${line_items}[0].title}}` |
| 항목 제공업체 | `{{event_properties.${line_items}[0].vendor}}` |
| 항목 이름 | `{{event_properties.${line_items}[0].name}}` |
| 항목 속성정보 | `{{event_properties.${line_items}[0].properties}}` |
| 주문 처리 상태 | `{{event_properties.${line_items}[0].fulfillment_status}}` |
| 배송 제목 | `{{event_properties.${shipping}[0].title}}` |
| 배송비 | `{{event_properties.${shipping}[0].price}}` |
| 배리언트 ID | `{{event_properties.${line_items}[0].variant_id}}` |
| 배리언트 제목 | `{{event_properties.${line_items}[0].variant_title}}` |
{: .reset-br-td-1 .reset-br-td-2 role="presentation" }
{% endraw %}
{% endsubtab %}
{% subtab Order refunded %}
**이벤트**: `shopify_order_refunded`<br>
**유형**: [커스텀 이벤트]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events)<br>
**Triggered**: When a user’s order is refunded<br>
**Use Case**: (Transactional) Refund confirmation

{% raw %}
| Variable | Liquid templating |
| --- | --- |
| 주문 ID | `{{event_properties.${order_id}}}` |
| 주문 참고 사항 | `{event_properties.${note}}}` |
| 아이템 ID | `{{event_properties.${line_items}[0].product_id}}` |
| 아이템 수량 | `{{event_properties.${line_items}[0].quantity}}` |
| 상품 SKU | `{{event_properties.${line_items}[0].sku}}` |
| 항목 제목 | `{{event_properties.${line_items}[0].title}}` |
| 항목 제공업체 | `{{event_properties.${line_items}[0].vendor}}` |
| 항목 이름 | `{{event_properties.${line_items}[0].name}}` |
| 항목 속성정보 | `{{event_properties.${line_items}[0].properties}}` |
| 아이템 가격 | `{{event_properties.${line_items}[0].price}}` |
| 배리언트 ID | `{{event_properties.${line_items}[0].variant_id}}` |
| 배리언트 제목 | `{{event_properties.${line_items}[0].variant_title}}` |
{: .reset-br-td-1 .reset-br-td-2 role="presentation" }
{% endraw %}

{% endsubtab %}
{% subtab Account login %}

**이벤트**: `shopify_account_login`<br>
**유형**: [커스텀 이벤트]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events)<br>
**Triggered**: When a user logs into their account<br>
**Use Case**: Welcome series

{% raw %}
| Variable | Liquid templating |
| --- | --- |
| `source` | {{event_properties.${source}}} |
{: .reset-br-td-1 .reset-br-td-2 role="presentation" }
{% endraw %}

{% alert note %}
The Shopify integration currently doesn't support populating the Braze [purchase event]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events#purchase-events). As a result, purchase filters, Liquid tags, action-based triggers, and analytics should use the ecommerce.order_placed event.
{% endalert %}

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## 지원되는 Shopify 사용자 지정 속성
{% tabs local %}
{% tab 페이로드 예제 %}
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
{% tab Shopify 사용자 지정 속성 %}
| 속성 이름 | 설명 | 설명
| --- | --- |
| `shopify_total_spent` | 고객이 주문 내역에서 지출한 총 금액입니다. |
| `shopify_order_count` | 이 고객과 관련된 주문 수입니다. 테스트 및 보관된 주문은 계산되지 않습니다. |
| `shopify_last_order_id` | 고객의 마지막 주문 ID입니다. |
| `shopify_last_order_name` | 고객의 마지막 주문 이름입니다. 이는 주문 리소스의 `name` 필드와 직접 관련이 있습니다. |
| `shopify_zipcode` | 기본 주소의 고객 우편번호입니다. |
| `shopify_province` | 기본 주소에서 고객의 시/도입니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### 유동적인 개인화

Shopify 커스텀 속성에 대한 Liquid 개인화를 추가하려면 **\+ 개인화**를 선택합니다. 그런 다음 **사용자 지정 속성을** 개인화 유형으로 선택합니다.

!['속성' 드롭다운이 확장된 '개인화 추가' 섹션.]({% image_buster /assets/img/Shopify/add_personalization_2.png %}){: style="max-width:40%;"}

커스텀 속성을 선택한 후 기본값을 입력하고 Liquid 스니펫을 메시지에 복사합니다.

![리퀴드 스니펫을 메시지에 붙여넣기]({% image_buster /assets/img/Shopify/copy_liquid_snippet.png %})
{% endtab %}
{% endtabs %}

## 지원되는 Shopify 표준 속성

- 이메일
- 이름
- 성
- 전화
- 도시
- 국가

{% alert note %}
Braze는 기존 사용자 프로필과 데이터에 차이가 있는 경우에만 지원되는 Shopify 사용자 지정 속성 및 Braze 표준 속성을 업데이트합니다. 예를 들어, 인바운드 Shopify 데이터에 Bob이라는 이름이 포함되어 있고 Braze 고객 프로필에 Bob이 이미 이름으로 존재하는 경우 Braze는 업데이트를 트리거하지 않으며 데이터 포인트가 청구되지 않습니다.
{% endalert %}

## SDK 데이터 수집 

For more information on what data is collected by the Braze SDKs, see [SDK data collection]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/). 

## 기록 백필

During your Shopify store onboarding, you can initiate an initial data sync through historical backfill to immediately engage with your customers. As part of this backfill, Braze will run an initial data sync of all customers and order placed from the last 90 days prior to your Shopify integration connection. 

### Setting up Shopify historical backfill

1. Turn on historical backfill in the **Track Shopify data** step.

![The "Track Shopify data" step of the Shopify integration showing historical backfill selected.]({% image_buster /assets/img/Shopify/historical_data_backfill_sync.png %})

{: start="2"}

2. After you complete your integration setup, Braze will begin the initial data sync. You can monitor progress on the **Shopify Data** tab of your integration settings. 

![The Shopify Integration Settings page with a spinner showing that events are actively syncing.]({% image_buster /assets/img/Shopify/historical_data_backfill_syncing.png %})

### Synced data 

For the initial data sync, Braze will import customers and order placed from the last 90 days prior to your Shopify integration connection. When Braze imports your Shopify customers, it will assign the `external_id` type that you chose in your configuration settings.