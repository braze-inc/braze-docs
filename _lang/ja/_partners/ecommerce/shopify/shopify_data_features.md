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

## 追跡対象の Shopify イベント

Shopify インテグレーションでは、[e コマース推奨イベント]({{site.baseurl}}/user_guide/data/custom_data/recommended_events/ecommerce_events/)を使用して、主要な買い物行動をキャプチャします。これらのイベントを使用した実装例およびマーケティング戦略については、[e コマースユースケース]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/ecommerce_use_cases/)を参照してください。

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
{% tab Shopify events %}
{% subtabs global %}
{% subtab Product viewed %}
**イベント**: `ecommerce.product_viewed`<br>
**タイプ**: 推奨イベント<br>
**トリガー**: 顧客が製品ページを閲覧したとき<br>
**データソース**: Braze SDK<br>
**ユースケース**: ブラウズ放棄

{% raw %}
| 変数 | Liquid テンプレート |
| --- | --- |
|------------------|-----------------------------------------------------|
| `product_id`       | `{{event_properties.${product_id}}}`                |
| `product_name `    | `{{event_properties.${product_name}}}`              |
| `variant_id`       | `{{event_properties.${variant_id}}}`                |
| `image_url `       | `{{event_properties.${image_url}}}`                 |
| `product_url`      | `<your-store.myshopify.com>{{event_properties.${product_url}}}` <br><br>URL の前に Shopify サイトドメインを追加します。 |
| `price`            | `{{event_properties.${price}}}`                     |
| `currency`         | `{{event_properties.${currency}}}`                  |
| `source`           | `{{event_properties.${source}}}`                    |
| `sku`              | `{{event_properties.${metadata}[0].sku}}`          |
| `type`             | `event_properties.${type}`          |
{: .reset-br-td-1 .reset-br-td-2 role="presentation" }
{% endraw %}

{% endsubtab %}
{% subtab Cart updated %}
**イベント**: `ecommerce.cart_updated`<br>
**タイプ**: 推奨イベント<br>
**トリガー**: 顧客がショッピングカートに商品を追加、削除、または更新したとき<br>
**データソース**: Braze SDK<br>
**ユースケース**: カート放棄

放棄カートキャンバスでは、まず最初のショッピングカートの Liquid タグを追加し、メッセージ内のショッピングカートのコンテキストを取得する必要があります。

{% raw %}
```liquid
{% shopping_cart {{context.${cart_id}}} %}
```
{% endraw %}

そして、次のショッピングカートの Liquid タグをメッセージに追加できます。

{% raw %}
| 変数         | Liquid テンプレート                                   |
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
Liquid `for` ループを構築してすべての製品をメールにダイナミックに追加する方法の詳細については、[メール用の放棄カート商品のパーソナライゼーション]({{site.baseurl}}/ecommerce_use_cases/#abandoned-cart)を参照してください。
{% endalert %}

{% endsubtab %}
{% subtab Checkout started %}
**イベント**: `ecommerce.checkout_started`<br>
**タイプ**: 推奨イベント<br>
**トリガー**: ユーザーがチェックアウトページに移動したとき<br>
**データソース**: Braze REST API<br>
**ユースケース**: チェックアウト放棄

{% alert important %}
顧客が Shop Pay を高速チェックアウトオプションとして使用した場合、Shopify は特定の標準チェックアウトイベント（Shopify チェックアウト開始 Webhook など）をスキップすることがあります。これにより、Braze がチェックアウトトークンエイリアスの追加に必要なデータを受信できず、チェックアウト放棄のトラッキングやユーザープロファイルの照合に影響を与える可能性があります。
{% endalert %}

放棄チェックアウトキャンバスでは、まず次の Liquid タグを使用する必要があります。

{% raw %}
```liquid
{% shopping_cart {{context.${cart_id}}} :abort_if_not_abandoned false %}
{{context.${cart_id}}}
```
{% endraw %}

次に、以下の Liquid タグをメッセージに追加し、チェックアウト時にカート内の商品を参照できます。

{% raw %}
| 変数         | Liquid テンプレート                                   |
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
**イベント**: `ecommerce.order_placed`<br>
**タイプ**: 推奨イベント<br>
**トリガー**: ユーザーがチェックアウトプロセスを正常に完了し、注文を確定したとき<br>
**データソース**: Braze REST API<br>
**ユースケース**: 注文確認、購入後リターゲティング、アップセルまたはクロスセル

{% raw %}
| 変数                | Liquid テンプレート                                   |
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
Shopify のチェックアウト完了 Webhook には、商品 URL や画像 URL が含まれていません。そのため、[メール用の注文確認とフィードバック調査]({{site.baseurl}}/ecommerce_use_cases/#order-confirmation-and-feedback-survey)で説明されているように、カタログ Liquid のパーソナライゼーションを使用する必要があります。
{% endalert %}

{% endsubtab %}
{% subtab Fulfilled order %}
**イベント**: `shopify_fulfilled_order`<br>
**タイプ**: [カスタムイベント]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)<br>
**トリガー**: ユーザーの注文がフルフィルメントされ、発送の準備ができたとき<br>
**データソース**: Braze REST API<br>
**ユースケース**: (トランザクション) フルフィルメントの更新

{% raw %}
| 変数 | Liquid テンプレート |
| --- | --- |
| オーダー ID | `{{event_properties.${order_id}}}` |
| 合計金額 | `{{event_properties.${total_price}}}` |
| 割引総額 | `{{event_properties.${total_discounts}}}` |
| 確認ステータス | `{{event_properties.${confirmed}}}` |
| 注文状況 URL | `{{event_properties.${order_status_url}}}` |
| 注文番号 | `{{event_properties.${order_number}}}` |
| キャンセルタイムスタンプ | `{{event_properties.${cancelled_at}}}` |
| クローズタイムスタンプ | `{{event_properties.${closed_at}}}` |
| アイテム ID | `{{event_properties.${line_items}[0].product_id}}` |
| アイテム数量 | `{{event_properties.${line_items}[0].quantity}}` |
| アイテム SKU | `{{event_properties.${line_items}[0].sku}}` |
| アイテムタイトル | `{{event_properties.${line_items}[0].title}}` |
| アイテムベンダー | `{{event_properties.${line_items}[0].vendor}}` |
| アイテム名 | `{{event_properties.${line_items}[0].name}}` |
| アイテムプロパティ | `{{event_properties.${line_items}[0].properties}}` |
| アイテム価格 | `{{event_properties.${line_items}[0].price}}` |
| 配送タイトル | `{{event_properties.${shipping}[0].title}}` |
| 配送料金 | `{{event_properties.${shipping}[0].price}}` |
| フルフィルメントステータス | `{{event_properties.${fulfillment_status}}}` |
| フルフィルメント出荷ステータス | `{{event_properties.${fulfillments}[0].shipment_status}}` |
| ステータス | `{{event_properties.${fulfillments}[0].status}}` |
| フルフィルメント追跡会社 | `{{event_properties.${fulfillments}[0].Fulfillment tracking_company}}` |
| フルフィルメント追跡番号 | `{{event_properties.${fulfillments}[0].Fulfillment tracking_number}}` |
| フルフィルメント追跡番号（複数） | `{{event_properties.${fulfillments}[0].Fulfillment tracking_numbers}}` |
| フルフィルメント追跡 URL | `{{event_properties.${fulfillments}[0].Fulfillment tracking_url}}` |
| フルフィルメント追跡 URL（複数） | `{{event_properties.${fulfillments}[0].Fulfillment tracking_urls}}` |
| フルフィルメントステータス | `{{event_properties.${fulfillments}[0].line_items[0].fulfillment_status}}` |
| フルフィルメント名 | `{{event_properties.${fulfillments}[0].line_items[0].name}}` |
| フルフィルメント価格 | `{{event_properties.${fulfillments}[0].line_items[0].price}}` |
| フルフィルメント製品 ID | `{{event_properties.${fulfillments}[0].line_items[0].product_id}}` |
| フルフィルメント数量 | `{{event_properties.${fulfillments}[0].line_items[0].quantity}}`|
| フルフィルメント配送 | `{{event_properties.${fulfillments}[0].line_items[0].requires_shipping}}` |
| フルフィルメント SKU | `{{event_properties.${fulfillments}[0].line_items[0].sku}}` |
| フルフィルメントタイトル | `{{event_properties.${fulfillments}[0].line_items[0].title}}` |
| フルフィルメントベンダー | `{{event_properties.${fulfillments}[0].line_items[0].vendor}}` |
| バリアント ID | `{{event_properties.${line_items}[0].variant_id}}` |
| バリアントタイトル | `{{event_properties.${line_items}[0].variant_title}}` |
{: .reset-br-td-1 .reset-br-td-2 role="presentation" }
{% endraw %}

{% endsubtab %}
{% subtab Partially fulfilled order %}
**イベント**: `shopify_partially_fulfilled_order`<br>
**タイプ**: [カスタムイベント]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)<br>
**トリガー**: ユーザーの注文の一部がフルフィルメントされ、発送の準備ができたとき<br> 
**データソース**: Braze REST API<br>
**ユースケース**: (トランザクション) フルフィルメントの更新

{% raw %}
| 変数 | Liquid テンプレート |
| --- | --- |
| オーダー ID | `{{event_properties.${order_id}}}` |
| 合計金額 | `{{event_properties.${total_price}}}` |
| 割引総額 | `{{event_properties.${total_discounts}}}` |
| 確認ステータス | `{{event_properties.${confirmed}}}` |
| 注文状況 URL | `{{event_properties.${order_status_url}}}` |
| 注文番号 | `{{event_properties.${order_number}}}` |
| キャンセルタイムスタンプ | `{{event_properties.${cancelled_at}}}` |
| クローズタイムスタンプ | `{{event_properties.${closed_at}}}` |
| アイテム ID | `{{event_properties.${line_items}[0].product_id}}` |
| アイテム数量 | `{{event_properties.${line_items}[0].quantity}}` |
| アイテム SKU | `{{event_properties.${line_items}[0].sku}}` |
| アイテムタイトル | `{{event_properties.${line_items}[0].title}}` |
| アイテムベンダー | `{{event_properties.${line_items}[0].vendor}}` |
| アイテム名 | `{{event_properties.${line_items}[0].name}}` |
| アイテムプロパティ | `{{event_properties.${line_items}[0].properties}}` |
| アイテム価格 | `{{event_properties.${line_items}[0].price}}` |
| 配送タイトル | `{{event_properties.${shipping}[0].title}}` |
| 配送料金 | `{{event_properties.${shipping}[0].price}}` |
| フルフィルメントステータス | `{{event_properties.${fulfillment_status}}}` |
| フルフィルメント出荷ステータス | `{{event_properties.${fulfillments}[0].shipment_status}}` |
| フルフィルメントステータス | `{{event_properties.${fulfillments}[0].status}}` |
| フルフィルメント追跡会社 | `{{event_properties.${fulfillments}[0].tracking_company}}` |
| フルフィルメント追跡番号 | `{{event_properties.${fulfillments}[0].tracking_number}}` |
| フルフィルメント追跡番号（複数） | `{{event_properties.${fulfillments}[0].tracking_numbers}}` |
| フルフィルメント追跡 URL | `{{event_properties.${fulfillments}[0].tracking_url}}` |
| フルフィルメント追跡 URL（複数） | `{{event_properties.${fulfillments}[0].tracking_urls}}` |
| フルフィルメントステータス | `{{event_properties.${fulfillments}[0].line_items[0].fulfillment_status}}` |
| フルフィルメント名 | `{{event_properties.${fulfillments}[0].line_items[0].name}}` |
| フルフィルメント価格 | `{{event_properties.${fulfillments}[0].line_items[0].price}}` |
| フルフィルメント製品 ID | `{{event_properties.${fulfillments}[0].line_items[0].product_id}}` |
| フルフィルメント数量 | `{{event_properties.${fulfillments}[0].line_items[0].quantity}}`|
| フルフィルメント配送 | `{{event_properties.${fulfillments}[0].line_items[0].requires_shipping}}` |
| フルフィルメント SKU | `{{event_properties.${fulfillments}[0].line_items[0].sku}}` |
| フルフィルメントタイトル | `{{event_properties.${fulfillments}[0].line_items[0].title}}` |
| フルフィルメントベンダー | `{{event_properties.${fulfillments}[0].line_items[0].vendor}}` |
| バリアント ID | `{{event_properties.${line_items}[0].variant_id}}` |
| バリアントタイトル | `{{event_properties.${line_items}[0].variant_title}}` |
{: .reset-br-td-1 .reset-br-td-2 role="presentation" }
{% endraw %}

{% endsubtab %}
{% subtab Paid order %}
**イベント**: `shopify_paid_order`<br>
**タイプ**: [カスタムイベント]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)<br>
**トリガー**: ユーザーの注文が Shopify 内で支払い済みとマークされたとき<br>
**データソース**: Braze REST API<br>
**ユースケース**: (トランザクション) 支払い確認

{% raw %}
| 変数 | Liquid テンプレート |
| --- | --- |
| オーダー ID | `{{event_properties.${order_id}}}` |
| 確認ステータス | `{{event_properties.${confirmed}}}` |
| 注文状況 URL | `{{event_properties.${order_status_url}}}` |
| 注文番号 | `{{event_properties.${order_number}}}` |
| キャンセルタイムスタンプ | `{{event_properties.${cancelled_at}}}` |
| 割引総額 | `{{event_properties.${total_discounts}}}` |
| 合計金額 | `{{event_properties.${total_price}}}` |
| タグ | `{{event_properties.${tags}}}` |
| 割引コード | `{{event_properties.${discount_codes}}}` |
| アイテム ID | `{{event_properties.${line_items}[0].product_id}}` |
| アイテム数量 | `{{event_properties.${line_items}[0].quantity}}` |
| アイテム SKU | `{{event_properties.${line_items}[0].sku}}` |
| アイテムタイトル | `{{event_properties.${line_items}[0].title}}` |
| アイテムベンダー | `{{event_properties.${line_items}[0].vendor}}` |
| アイテムプロパティ | `{{event_properties.${line_items}[0].properties}}` |
| アイテム価格 | `{{event_properties.${line_items}[0].price}}` |
| 配送タイトル | `{{event_properties.${shipping}[0].title}}` |
| 配送料金 | `{{event_properties.${shipping}[0].price}}` |
| バリアント ID | `{{event_properties.${line_items}[0].variant_id}}` |
| バリアントタイトル | `{{event_properties.${line_items}[0].variant_title}}` |
{: .reset-br-td-1 .reset-br-td-2 role="presentation" }
{% endraw %}

{% endsubtab %}
{% subtab Order cancelled %}
**イベント**: `shopify_cancelled_order`<br>
**タイプ**: [カスタムイベント]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)<br>
**トリガー**: ユーザーの注文がキャンセルされたとき<br> 
**データソース**: Braze REST API<br>
**ユースケース**: (トランザクション) 注文キャンセル確認

{% raw %}
| 変数 | Liquid テンプレート |
| --- | --- |
| オーダー ID | `{{event_properties.${order_id}}}` |
| 合計金額 | `{{event_properties.${total_price}}}` |
| 割引総額 | `{{event_properties.${total_discounts}}}` |
| 確認済み | `{{event_properties.${confirmed}}}` |
| 注文状況 URL | `{{event_properties.${order_status_url}}}` |
| 注文番号 | `{{event_properties.${order_number}}}` |
| キャンセルタイムスタンプ | `{{event_properties.${cancelled_at}}}` |
| タグ | `{{event_properties.${tags}}}` |
| 割引コード | `{{event_properties.${discount_codes}}}` |
| フルフィルメントステータス | `{{event_properties.${fulfillment_status}}}` |
| フルフィルメント | `{{event_properties.${fulfillments}}}` |
| アイテム ID | `{{event_properties.${line_items}[0].product_id}}` |
| アイテム数量 | `{{event_properties.${line_items}[0].quantity}}` |
| アイテム SKU | `{{event_properties.${line_items}[0].sku}}` |
| アイテムタイトル | `{{event_properties.${line_items}[0].title}}` |
| アイテムベンダー | `{{event_properties.${line_items}[0].vendor}}` |
| アイテム名 | `{{event_properties.${line_items}[0].name}}` |
| アイテムプロパティ | `{{event_properties.${line_items}[0].properties}}` |
| フルフィルメントステータス | `{{event_properties.${line_items}[0].fulfillment_status}}` |
| 配送タイトル | `{{event_properties.${shipping}[0].title}}` |
| 配送料金 | `{{event_properties.${shipping}[0].price}}` |
| バリアント ID | `{{event_properties.${line_items}[0].variant_id}}` |
| バリアントタイトル | `{{event_properties.${line_items}[0].variant_title}}` |
{: .reset-br-td-1 .reset-br-td-2 role="presentation" }
{% endraw %}
{% endsubtab %}
{% subtab Order refunded %}
**イベント**: `shopify_order_refunded`<br>
**タイプ**: [カスタムイベント]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)<br>
**トリガー**: ユーザーの注文が返金されたとき<br>
**データソース**: Braze REST API<br>
**ユースケース**: (トランザクション) 返金確認

{% raw %}
| 変数 | Liquid テンプレート |
| --- | --- |
| オーダー ID | `{{event_properties.${order_id}}}` |
| 注文メモ | `{event_properties.${note}}}` |
| アイテム ID | `{{event_properties.${line_items}[0].product_id}}` |
| アイテム数量 | `{{event_properties.${line_items}[0].quantity}}` |
| アイテム SKU | `{{event_properties.${line_items}[0].sku}}` |
| アイテムタイトル | `{{event_properties.${line_items}[0].title}}` |
| アイテムベンダー | `{{event_properties.${line_items}[0].vendor}}` |
| アイテム名 | `{{event_properties.${line_items}[0].name}}` |
| アイテムプロパティ | `{{event_properties.${line_items}[0].properties}}` |
| アイテム価格 | `{{event_properties.${line_items}[0].price}}` |
| バリアント ID | `{{event_properties.${line_items}[0].variant_id}}` |
| バリアントタイトル | `{{event_properties.${line_items}[0].variant_title}}` |
{: .reset-br-td-1 .reset-br-td-2 role="presentation" }
{% endraw %}

{% endsubtab %}
{% subtab Account login %}

**イベント**: `shopify_account_login`<br>
**タイプ**: [カスタムイベント]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)<br>
**トリガー**: ユーザーがアカウントにログインしたとき<br>
**データソース**: Braze REST API<br>
**ユースケース**: ウェルカムシリーズ

{% raw %}
| 変数 | Liquid テンプレート |
| --- | --- |
| `source` | {{event_properties.${source}}} |
{: .reset-br-td-1 .reset-br-td-2 role="presentation" }
{% endraw %}

{% alert note %}
現在、Shopify インテグレーションでは、Braze [購入イベント]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events#purchase-events)への入力はサポートされていません。そのため、購入フィルター、Liquid タグ、アクションベースのトリガー、および分析には `ecommerce.order_placed` イベントを使用する必要があります。
{% endalert %}

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## サポートされている Shopify カスタム属性

{% multi_lang_include alerts/note_alerts.md alert='Shopify attributes REST API' %}

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
| `shopify_order_count` | この顧客に関連する注文数。テストオーダーとアーカイブオーダーはカウントされません。 |
| `shopify_last_order_id` | 顧客の最後の注文の ID。 |
| `shopify_last_order_name` | 顧客の最後の注文の名前。これは、注文リソースの `name` フィールドに直接関係しています。 |
| `shopify_zipcode` | 顧客のデフォルト住所の郵便番号。 |
| `shopify_province` | 顧客のデフォルト住所の都道府県。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert important %}
現行の Shopify API バージョンに既知の問題があり、`shopify_last_order_name` ユーザー属性が正しく入力されません。ユーザーへの影響は以下のとおりです。<br><br>

- **既存ユーザー:** すでに `shopify_last_order_name` の値を持っているユーザーの場合、その値は保持されますが、後続の注文では更新されません。
- **新規ユーザー:** 新規ユーザーの場合、フィールドは入力されず、空または null のままになります。

このページは、Shopify がこの問題を解決した後に更新されます。
{% endalert %}

### Liquid のパーソナライゼーション

Shopify カスタム属性に Liquid パーソナライゼーションを追加するには、[**+ パーソナライゼーション**] を選択します。次に、パーソナライゼーションタイプとして [**カスタム属性**] を選択します。

![「パーソナライゼーションの追加」セクションで「属性」ドロップダウンが展開されています。]({% image_buster /assets/img/Shopify/add_personalization_2.png %}){: style="max-width:40%;"}

カスタム属性を選択したら、デフォルト値を入力して Liquid スニペットをメッセージにコピーします。

![Liquid スニペットをメッセージに貼り付ける。]({% image_buster /assets/img/Shopify/copy_liquid_snippet.png %})
{% endtab %}
{% endtabs %}

## サポートされている Shopify 標準属性

{% multi_lang_include alerts/note_alerts.md alert='Shopify attributes REST API' %}

- メール
- 名
- 姓
- 電話
- 市区町村
- 国

{% alert note %}
Braze がサポートされている Shopify カスタム属性と Braze 標準属性を更新するのは、既存のユーザープロファイルとデータに違いがある場合のみです。たとえば、インバウンド Shopify データに Bob という名前が含まれており、Bob が Braze のユーザープロファイルに名前としてすでに存在している場合、Braze では更新はトリガーされず、データポイントは課金されません。
{% endalert %}

## SDK によるデータ収集

Braze SDK が収集するデータの詳細については、[SDK データ収集]({{site.baseurl}}/user_guide/data/user_data_collection/sdk_data_collection/)を参照してください。

## 履歴バックフィル

Shopify ストアのオンボーディング中に、履歴バックフィルを通じて初期データ同期を開始し、顧客とすぐにエンゲージメントを開始できます。このバックフィルの一環として、Braze は Shopify インテグレーション接続前の過去 90 日間のすべての顧客と注文確定イベントの初期データ同期を実行します。Braze が Shopify の顧客をインポートする際、設定で選択した `external_id` タイプを割り当てます。

{% alert note %}
カスタム external ID（[標準インテグレーション]({{site.baseurl}}/partners/ecommerce/shopify/shopify_standard_integration/#step-4-configure-how-you-manage-users)または[カスタムインテグレーション]({{site.baseurl}}/partners/ecommerce/shopify/shopify_custom_integration/#step-6-configure-how-you-manage-users-optional)のいずれか）との統合を計画している場合、既存のすべての Shopify 顧客プロファイルに Shopify 顧客メタフィールドとしてカスタム external ID を追加し、その後に履歴バックフィルを実行する必要があります。
{% endalert %}

同期された注文イベントデータはセグメンテーションに使用できますが、収益データ自体はユーザープロファイルや[収益 – ラストタッチアトリビューションダッシュボード]({{site.baseurl}}/user_guide/analytics/reporting/dashboard_builder/#revenue---last-touch-attribution)には反映されません。

### Shopify 履歴バックフィルの設定

1. **Shopify データの追跡**ステップで、履歴バックフィルをオンにします。

![履歴バックフィルが選択された Shopify インテグレーションの「Shopify データの追跡」ステップ。]({% image_buster /assets/img/Shopify/historical_data_backfill_sync.png %})

{: start="2"}

2. インテグレーション設定が完了すると、Braze は初期データ同期を開始します。進捗状況は、インテグレーション設定の [**Shopify データ**] タブで確認できます。

![イベントがアクティブに同期中であることを示すスピナーが表示された Shopify インテグレーション設定ページ。]({% image_buster /assets/img/Shopify/historical_data_backfill_syncing.png %})

### 同期データ

初期データ同期では、Braze は Shopify インテグレーション接続前の過去 90 日間の顧客と注文確定をインポートします。Braze が Shopify の顧客をインポートする際、設定で選択した `external_id` タイプを割り当てます。