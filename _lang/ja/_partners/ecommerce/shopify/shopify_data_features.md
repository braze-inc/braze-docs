---
nav_title: Shopify のデータ機能
article_title: "Shopify のデータ機能"
description: "このリファレンス記事では、Shopify のデータ機能について説明します。"
page_type: partner
search_tag: Partner
alias: /shopify_data_features/
page_order: 4
---

# Shopify のデータ機能

> この記事では、Shopify の機能の概要を示します。これには、追跡対象の Shopify データ、ペイロード例、履歴バックフィル、および製品の同期などが含まれます。

## 追跡対象の Shopifyイベント

Shopifyインテグレーションでは、[eコマース推奨イベント]({{site.baseurl}}/user_guide/data/custom_data/recommended_events/ecommerce_events/)を使用して、主要な買い物行動をキャプチャします。これらのイベントを使用した実装例およびマーケティング方法については、[eCommerce ユースケース s]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/ecommerce_use_cases/)を参照してください。

{% multi_lang_include alerts/important_alerts.md alert='Shopify customer create' %}

{% tabs %}
{% tab Example Payload %}
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
**イベント**： `ecommerce.product_viewed`<br>
**タイプ**：推奨イベント<br>
**トリガー済み**顧客による製品ページの閲覧<br>
**ユースケース**ブラウズ放棄

{% raw %}
| 変数| Liquid テンプレート |
| --- | --- |
\|------------------|-----------------------------------------------------|
| `product_id`       | `{{event_properties.${product_id}}}`                |
| `product_name `    | `{{event_properties.${product_name}}}`              |
| `variant_id`       | `{{event_properties.${variant_id}}}`                |
| `image_url `       | `{{event_properties.${image_url}}}`                 |
| `product_url` | `<your-store.myshopify.com>{{event_properties.${product_url}}}`<br><br>URL の前にShopify サイトドメインを追加します。|
| `price`            | `{{event_properties.${price}}}`                     |
| `currency`         | `{{event_properties.${currency}}}`                  |
| `source`           | `{{event_properties.${source}}}`                    |
| `sku`              | `{{event_properties.${metadata}[0].sku}}`          |
| `type`             | `event_properties.${type}`          |
{: .reset-br-td-1 .reset-br-td-2 role="presentation" }
{% endraw %}

{% endsubtab %}
{% subtab Cart updated %}
**イベント**： `ecommerce.cart_updated`<br>
**タイプ**：推奨イベント<br>
**トリガー済み**顧客によるショッピングカートの追加、削除、更新<br>
**ユースケース**カート放棄

カート放棄キャンバスでは、まず最初のショッピングカートの Liquid タグを追加し、メッセージ内のショッピングカートのコンテキストを取得する必要があります。 

{% raw %}
```liquid
{% shopping_cart {{context.${cart_id}}} %}
```
{% endraw %}

そして、次のショッピングカートの Liquid タグをメッセージに追加できます。

{% raw %}
| Variable         | Liquid テンプレート                                   |
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
Liquid `for` ループを構築してすべての製品をメールに動的に追加する方法の詳細については、[メール用の放棄されたカートの商品のパーソナライゼーション]({{site.baseurl}}/ecommerce_use_cases/#abandoned-cart)を参照してください。
{% endalert %}

{% endsubtab %}
{% subtab Checkout started %}
**イベント**： `ecommerce.checkout_started`<br>
**タイプ**：推奨イベント<br>
**トリガー済み**ユーザーがチェックアウトページに移動したとき<br>
**ユースケース**チェックアウト放棄

放棄されたチェックアウトキャンバスでは、まず次の Liquid タグを使用する必要があります。

{% raw %}
```liquid
{% shopping_cart {{context.${cart_id}}} :abort_if_not_abandoned false %}
{{context.${cart_id}}}
```
{% endraw %}

次に、以下の Liquid タグをメッセージに追加し、チェックアウト時にカート内の商品を参照できます。

{% raw %}
| Variable         | Liquid テンプレート                                   |
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
**イベント**： `ecommerce.order_placed`<br>
**タイプ**：推奨イベント<br>
**トリガー済み**ユーザーがチェックアウトプロセスを正常に完了し、注文を出すとき<br>
**ユースケース**注文確認、購入後リターゲット、アップセル、クロスセル 

{% raw %}
| 変数| 液体テンプレーティング|
\|-------------------------|-----------------------------------------------------|
| cart_id                 | `{{event_properties.${cart_id}}}`                   |
| currency                | `{{event_properties.${currency}}}`                  |
| discounts               | `{{event_properties.${discounts}}}`                 |
| order_id                | `{{event_properties.${order_id}}}`                  |
| product_id              | `{{event_properties.${products}[0].product_id}}`   |
| product_name            | `{{event_properties.${products}[0].product_name}}` |
| variant_id              | `{{event_properties.${products}[0].variant_id}}`   |
| quantity                | `{{event_properties.${products}[0].quantity}}`     |
| sku | `{{event_properties.${products}[0].metadata.sku}}` |
| total_discounts         | `{{event_properties.${total_discounts}}}`           |
| order_status_url        | `{{event_properties.${metadata}.order_status_url}}` |
| order_number            | `{{event_properties.${metadata}.order_number}}`     |
| tags                    | `{{event_properties.${metadata}.tags}}`             |
| referring_site          | `{{event_properties.${metadata}.referring_site}}`   |
| payment_gateway_names    | `{{event_properties.${metadata}.payment_gateway_names}}` |
{: .reset-br-td-1 .reset-br-td-2 role="presentation" }
{% endraw %}

{% alert tip %}
Shopify のチェックアウト完了 Webhook には、商品 URL や画像 URL が含まれていません。その結果、[メール用の放棄カート商品のパーソナライゼーション]({{site.baseurl}}/ecommerce_use_cases/#order-confirmation-and-feedback-survey)で述べたように、カタログ Liquid のパーソナライゼーションを使用する必要があります。
{% endalert %}

{% endsubtab %}
{% subtab Fulfilled order %}
**イベント**： `shopify_fulfilled_order`<br>
**タイプ**：[カスタムイベント]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)<br>
**トリガー済み**ユーザーの注文が満たされ、発送の準備ができたとき<br>
**ユースケース**(トランザクション) フルフィルメントの更新 

{% raw %}
| 変数| Liquid テンプレート |
| --- | --- |
| オーダーID｜`{{event_properties.${order_id}}}` ｜
| 価格｜総額｜`{{event_properties.${total_price}}}` ｜
| 割引総額｜`{{event_properties.${total_discounts}}}` ｜
| 確認ステータス | `{{event_properties.${confirmed}}}` |
| 注文状況URL｜`{{event_properties.${order_status_url}}}` ｜
| 注文番号｜`{{event_properties.${order_number}}}` ｜
| キャンセルされたタイムスタンプ |`{{event_properties.${cancelled_at}}}` |
| クローズド・タイムスタンプ｜`{{event_properties.${closed_at}}}` ｜
| アイテムID｜`{{event_properties.${line_items}[0].product_id}}` ｜
| アイテム数量 | `{{event_properties.${line_items}[0].quantity}}` |
| アイテムSKU｜`{{event_properties.${line_items}[0].sku}}` ｜
| アイテムタイトル | `{{event_properties.${line_items}[0].title}}` |
| アイテムベンダー | `{{event_properties.${line_items}[0].vendor}}` |
| アイテム名｜`{{event_properties.${line_items}[0].name}}` ｜
| アイテムプロパティ | `{{event_properties.${line_items}[0].properties}}` |
| アイテム価格 | `{{event_properties.${line_items}[0].price}}` |
| 配送タイトル | `{{event_properties.${shipping}[0].title}}` |
| 価格｜送料｜`{{event_properties.${shipping}[0].price}}`
| フルフィルメントステータス | `{{event_properties.${fulfillment_status}}}` |
| フルフィルメント出荷ステータス | `{{event_properties.${fulfillments}[0].shipment_status}}` |
| ステータス| `{{event_properties.${fulfillments}[0].status}}` |
\|`{{event_properties.${fulfillments}[0].Fulfillment tracking_company}}` ｜フルフィルメント・トラッキング・カンパニー｜Fulfillment Tracking Company｜フルフィルメント・トラッキング・カンパニー
| フルフィルメント追跡番号｜`{{event_properties.${fulfillments}[0].Fulfillment tracking_number}}` ｜
| フルフィルメント追跡番号｜`{{event_properties.${fulfillments}[0].Fulfillment tracking_numbers}}` ｜
| フルフィルメント・トラッキングURL｜`{{event_properties.${fulfillments}[0].Fulfillment tracking_url}}` ｜
| フルフィルメント・トラッキングURL｜`{{event_properties.${fulfillments}[0].Fulfillment tracking_urls}}` ｜
| フルフィルメントステータス | `{{event_properties.${fulfillments}[0].line_items[0].fulfillment_status}}` |
| フルフィルメント名 | `{{event_properties.${fulfillments}[0].line_items[0].name}}` |
| フルフィルメント価格｜`{{event_properties.${fulfillments}[0].line_items[0].price}}` ｜
| フルフィルメント・プロダクトID｜`{{event_properties.${fulfillments}[0].line_items[0].product_id}}` ｜
| フルフィルメント数量 | `{{event_properties.${fulfillments}[0].line_items[0].quantity}}` |
| フルフィルメント配送 | `{{event_properties.${fulfillments}[0].line_items[0].requires_shipping}}` |
| フルフィルメント SKU｜`{{event_properties.${fulfillments}[0].line_items[0].sku}}`
| フルフィルメントタイトル| `{{event_properties.${fulfillments}[0].line_items[0].title}}` |
| フルフィルメントベンダー | `{{event_properties.${fulfillments}[0].line_items[0].vendor` |
| バリアント ID | `{{event_properties.${line_items}[0].variant_id}}` |
| バリアントタイトル |`{{event_properties.${line_items}[0].variant_title}}` |
{: .reset-br-td-1 .reset-br-td-2 role="presentation" }
{% endraw %}

{% endsubtab %}
{% subtab Partially fulfilled order %}
**イベント**： `shopify_partially_fulfilled_order`<br>
**タイプ**：[カスタムイベント]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)<br>
**トリガー済み**ユーザーの注文の一部が履行され、発送の準備ができたとき<br> 
**ユースケース**(トランザクション) フルフィルメントの更新 

{% raw %}
| 変数| Liquid テンプレート |
| --- | --- |
| オーダーID｜`{{event_properties.${order_id}}}` ｜
| 価格｜総額｜`{{event_properties.${total_price}}}` ｜
| 割引総額｜`{{event_properties.${total_discounts}}}` ｜
| 確認ステータス | `{{event_properties.${confirmed}}}` |
| 注文状況URL｜`{{event_properties.${order_status_url}}}` ｜
| 注文番号｜`{{event_properties.${order_number}}}` ｜
| キャンセルされたタイムスタンプ |`{{event_properties.${cancelled_at}}}` |
| クローズド・タイムスタンプ｜`{{event_properties.${closed_at}}}` ｜
| アイテムID｜`{{event_properties.${line_items}[0].product_id}}` ｜
| アイテム数量 | `{{event_properties.${line_items}[0].quantity}}` |
| アイテムSKU｜`{{event_properties.${line_items}[0].sku}}` ｜
| アイテムタイトル | `{{event_properties.${line_items}[0].title}}` |
| アイテムベンダー | `{{event_properties.${line_items}[0].vendor}}` |
| アイテム名｜`{{event_properties.${line_items}[0].name}}` ｜
| アイテムプロパティ | `{{event_properties.${line_items}[0].properties}}` |
| アイテム価格 | `{{event_properties.${line_items}[0].price}}` |
| 配送タイトル | `{{event_properties.${shipping}[0].title}}` |
| 価格｜送料｜`{{event_properties.${shipping}[0].price}}`
| フルフィルメントステータス | `{{event_properties.${fulfillment_status}}}` |
| フルフィルメント出荷ステータス | `{{event_properties.${fulfillments}[0].shipment_status}}` |
| フルフィルメントステータス | `{{event_properties.${fulfillments}[0].status}}` |
\|`{{event_properties.${fulfillments}[0].tracking_company}}` ｜フルフィルメント・トラッキング・カンパニー｜Fulfillment Tracking Company｜フルフィルメント・トラッキング・カンパニー
| フルフィルメント追跡番号｜`{{event_properties.${fulfillments}[0].tracking_number}}` ｜
| フルフィルメント追跡番号｜`{{event_properties.${fulfillments}[0].tracking_numbers}}` ｜
| フルフィルメント・トラッキングURL｜`{{event_properties.${fulfillments}[0].tracking_url}}` ｜
| フルフィルメント・トラッキングURL｜`{{event_properties.${fulfillments}[0].tracking_urls}}` ｜
| フルフィルメントステータス | `{{event_properties.${fulfillments}[0].line_items[0].fulfillment_status}}` |
| フルフィルメント名 | `{{event_properties.${fulfillments}[0].line_items[0].name}}` |
| フルフィルメント価格｜`{{event_properties.${fulfillments}[0].line_items[0].price}}` ｜
| フルフィルメント・プロダクトID｜`{{event_properties.${fulfillments}[0].line_items[0].product_id}}` ｜
| フルフィルメント数量 | `{{event_properties.${fulfillments}[0].line_items[0].quantity}}` |
| フルフィルメント配送 | `{{event_properties.${fulfillments}[0].line_items[0].requires_shipping}}` |
| フルフィルメント SKU｜`{{event_properties.${fulfillments}[0].line_items[0].sku}}`
| フルフィルメントタイトル| `{{event_properties.${fulfillments}[0].line_items[0].title}}` |
| フルフィルメントベンダー | `{{event_properties.${fulfillments}[0].line_items[0].vendor` |
| バリアント ID | `{{event_properties.${line_items}[0].variant_id}}` |
| バリアントタイトル |`{{event_properties.${line_items}[0].variant_title}}` |
{: .reset-br-td-1 .reset-br-td-2 role="presentation" }
{% endraw %}

{% endsubtab %}
{% subtab Paid order %}
**イベント**： `shopify_paid_order`<br>
**タイプ**：[カスタムイベント]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)<br>
**トリガー済み**ユーザの注文がShopify内で支払済みとマークされたとき<br>  
**ユースケース**(トランザクション) 支払いの確認

{% raw %}
| 変数| Liquid テンプレート |
| --- | --- |
| オーダーID｜`{{event_properties.${order_id}}}` ｜
| 確認ステータス | `{{event_properties.${confirmed}}}` |
| 注文状況URL｜`{{event_properties.${order_status_url}}}` ｜
| 注文番号｜`{{event_properties.${order_number}}}` ｜
| キャンセルされたタイムスタンプ |`{{event_properties.${cancelled_at}}}` |
| 割引総額｜`{{event_properties.${total_discounts}}}` ｜
| 価格｜総額｜`{{event_properties.${total_price}}}` ｜
| タグ: | `{{event_properties.${tags}}}` |
| 割引コード｜`{{event_properties.${discount_codes}}}`
| アイテムID｜`{{event_properties.${line_items}[0].product_id}}` ｜
| アイテム数量 | `{{event_properties.${line_items}[0].quantity}}` |
| アイテムSKU｜`{{event_properties.${line_items}[0].sku}}` ｜
| アイテムタイトル | `{{event_properties.${line_items}[0].title}}` |
| アイテムベンダー | `{{event_properties.${line_items}[0].vendor}}` |
| アイテムプロパティ | `{{event_properties.${line_items}[0].properties}}` |
| アイテム価格 | `{{event_properties.${line_items}[0].price}}` |
| 配送タイトル | `{{event_properties.${shipping}[0].title}}` |
| 価格｜送料｜`{{event_properties.${shipping}[0].price}}`
| バリアント ID | `{{event_properties.${line_items}[0].variant_id}}` |
| バリアントタイトル |`{{event_properties.${line_items}[0].variant_title}}` |
{: .reset-br-td-1 .reset-br-td-2 role="presentation" }
{% endraw %}

{% endsubtab %}
{% subtab Order cancelled %}
**イベント**： `shopify_cancelled_order`<br>
**タイプ**：[カスタムイベント]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)<br>
**トリガー済み**ユーザーの注文がキャンセルされた場合<br> 
**ユースケース**(取引）注文のキャンセル確認

{% raw %}
| 変数| Liquid テンプレート |
| --- | --- |
| オーダーID｜`{{event_properties.${order_id}}}` ｜
| 価格｜総額｜`{{event_properties.${total_price}}}` ｜
| 割引総額｜`{{event_properties.${total_discounts}}}` ｜
| 確認済み |`{{event_properties.${confirmed}}}` |
| 注文状況URL｜`{{event_properties.${order_status_url}}}` ｜
| 注文番号｜`{{event_properties.${order_number}}}` ｜
| キャンセルされたタイムスタンプ |`{{event_properties.${cancelled_at}}}` |
| タグ: | `{{event_properties.${tags}}}` |
| 割引コード｜`{{event_properties.${discount_codes}}}`
| フルフィルメントステータス | `{{event_properties.${fulfillment_status}}}` |
| フルフィルメント | `{{event_properties.${fulfillments}}}` |
| アイテムID｜`{{event_properties.${line_items}[0].product_id}}` ｜
| アイテム数量 | `{{event_properties.${line_items}[0].quantity}}` |
| アイテムSKU｜`{{event_properties.${line_items}[0].sku}}` ｜
| アイテムタイトル | `{{event_properties.${line_items}[0].title}}` |
| アイテムベンダー | `{{event_properties.${line_items}[0].vendor}}` |
| アイテム名｜`{{event_properties.${line_items}[0].name}}` ｜
| アイテムプロパティ | `{{event_properties.${line_items}[0].properties}}` |
| フルフィルメントステータス | `{{event_properties.${line_items}[0].fulfillment_status}}` |
| 配送タイトル | `{{event_properties.${shipping}[0].title}}` |
| 価格｜送料｜`{{event_properties.${shipping}[0].price}}`
| バリアント ID | `{{event_properties.${line_items}[0].variant_id}}` |
| バリアントタイトル |`{{event_properties.${line_items}[0].variant_title}}` |
{: .reset-br-td-1 .reset-br-td-2 role="presentation" }
{% endraw %}
{% endsubtab %}
{% subtab Order refunded %}
**イベント**： `shopify_order_refunded`<br>
**タイプ**：[カスタムイベント]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)<br>
**トリガー済み**利用者の注文が払い戻されたとき<br>
**ユースケース**(取引) 返金の確認

{% raw %}
| 変数| Liquid テンプレート |
| --- | --- |
| オーダーID｜`{{event_properties.${order_id}}}` ｜
| 注文メモ | `{event_properties.${note}}}` |
| アイテムID｜`{{event_properties.${line_items}[0].product_id}}` ｜
| アイテム数量 | `{{event_properties.${line_items}[0].quantity}}` |
| アイテムSKU｜`{{event_properties.${line_items}[0].sku}}` ｜
| アイテムタイトル | `{{event_properties.${line_items}[0].title}}` |
| アイテムベンダー | `{{event_properties.${line_items}[0].vendor}}` |
| アイテム名｜`{{event_properties.${line_items}[0].name}}` ｜
| アイテムプロパティ | `{{event_properties.${line_items}[0].properties}}` |
| アイテム価格 | `{{event_properties.${line_items}[0].price}}` |
| バリアント ID | `{{event_properties.${line_items}[0].variant_id}}` |
| バリアントタイトル |`{{event_properties.${line_items}[0].variant_title}}` |
{: .reset-br-td-1 .reset-br-td-2 role="presentation" }
{% endraw %}

{% endsubtab %}
{% subtab Account login %}

**イベント**： `shopify_account_login`<br>
**タイプ**：[カスタムイベント]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)<br>
**トリガー済み**ユーザーが自分のアカウントにログインするとき<br>
**ユースケース**ウェルカムシリーズ

{% raw %}
| 変数| Liquid テンプレート |
| --- | --- |
| `source` | {{event_properties.${source}}} |
{: .reset-br-td-1 .reset-br-td-2 role="presentation" }
{% endraw %}

{% alert note %}
現在、Shopify 統合では、Braze [購入イベント]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events#purchase-events)への入力はサポートされていません。このため、フィルターs、リキッドタグs、アクション ベースのトリガーs、および分析 は、`ecommerce.order_placed` を使用する必要があります。
{% endalert %}

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## サポートされているShopifyカスタム属性

{% tabs local %}
{% tab Example Payload %}
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
{% tab Shopify Custom Attributes %}
| 属性名 | 説明 |
| --- | --- |
| `shopify_total_spent` | 注文履歴全体で顧客が支払った総額。 |
｜`shopify_order_count` ｜この顧客に関連する注文数。テストオーダーとアーカイブオーダーはカウントされない。|
\|`shopify_last_order_id` | 顧客の最後の注文のID。|
\|`shopify_last_order_name` | 顧客の最後の注文の名前。これは、注文リソースの `name` フィールドに直接関係しています。 |
\|`shopify_zipcode` ｜顧客のデフォルト住所の郵便番号。|
| `shopify_province` | 顧客のデフォルトの住所の都道府県。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert important %}
現行のShopify API バージョンに既知の問題があると、`shopify_last_order_name` ユーザー 属性が正しく入力されません。ユーザーs への影響は以下のとおりです。<br><br>

- **既設ユーザーs:**すでに`shopify_last_order_name` の値を持っているユーザーの場合、その値は保持されますが、後続の順序では更新d になりません。
- **新しいユーザー:**新しいユーザーs の場合、フィールドは入力せず、空またはNULL のままになります。

このページは、Shopify がこの問題を解決した後に更新されます。
{% endalert %}

### Liquid のパーソナライゼーション

Shopify カスタム属性に Liquid パーソナライゼーションを追加するには、[**\+ パーソナライゼーション**] を選択します。次に、[パーソナライゼーションタイプ] として [**カスタム属性**] を選択します。

!["Add Personalization"セクションで"Attribute"ドロップダウンが拡張されています。]({% image_buster /assets/img/Shopify/add_personalization_2.png %}){: style="max-width:40%;"}

カスタム属性を選択したら、デフォルト値を入力して Liquid スニペットをメッセージにコピーします。

![液体スニペットをメッセージにペーストする。]({% image_buster /assets/img/Shopify/copy_liquid_snippet.png %})
{% endtab %}
{% endtabs %}

## サポートされるShopify標準属性

- メール
- 名
- 姓
- 電話
- 市区町村
- 国

{% alert note %}
Brazeは、サポートされているShopifyカスタム属性とBraze標準属性を更新するのは、既存のユーザープロファイルとデータに違いがある場合のみである。たとえば、インバウンド Shopify データに Bob という名前が含まれており、Bob が Braze のユーザープロファイルに名前としてすでに存在している場合、Braze では更新はトリガーされず、データポイントにつ課金されません。
{% endalert %}

## SDK によるデータ収集 

Braze SDK が収集するデータの詳細については、[SDK データ収集]({{site.baseurl}}/user_guide/data/user_data_collection/sdk_data_collection/)を参照してください。 

## 歴史的埋め戻し

Shopify ストアのオンボーディング中に、履歴バックフィルを通して初期データ同期を開始し、顧客とすぐにやり取りすることができます。このバックアップの一環として、Brazeは、Shopify統合接続前の過去90日間のすべての顧客と注文の初期データ同期を実行する。Braze が Shopify の顧客をインポートする際、設定にて選択した `external_id` タイプを割り当てます。

{% alert note %}
カスタム外部ID（[標準統合]({{site.baseurl}}/partners/ecommerce/shopify/shopify_standard_integration/#step-4-configure-how-you-manage-users)または[カスタム統合の]({{site.baseurl}}/partners/ecommerce/shopify/shopify_custom_integration/#step-6-configure-how-you-manage-users-optional)いずれか）との統合を計画している場合、既存のすべてのShopify顧客プロファイルにShopify顧客メタフィールドとしてカスタム外部IDを追加し、ヒストリカル・バックフィルを実行する必要がある。
{% endalert %}

### Shopify 履歴バックフィルの設定

1. **Shopify データの追跡**ステップで、履歴バックフィルをオンにします。

!["Track Shopify data"選択した履歴バックフィルを示すShopifyインテグレーションのステップ。]({% image_buster /assets/img/Shopify/historical_data_backfill_sync.png %})

{: start="2"}

2. 統合設定が完了すると、Braze は初期データ同期を開始します。進捗状況は、統合設定の [**Shopify データ**] タブで確認できます。 

![「Shopify統合設定」ページには、イベントがアクティブに同期していることを示すスピナーが表示されます。]({% image_buster /assets/img/Shopify/historical_data_backfill_syncing.png %})

### 同期データ 

初期データ同期の場合、Braze は、Shopify 統合接続の直前の 90 日分の顧客と注文をインポートします。Braze が Shopify の顧客をインポートする際、設定にて選択した `external_id` タイプを割り当てます。