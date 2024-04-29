---
nav_title: BrazeのShopifyデータ
article_title: "BrazeでShopify Dataを使用する"
description: "このリファレンス記事では、BrazeでShopifyのデータを使用してパーソナライゼーションとセグメンテーションを行う方法について概説します。"
page_type: partner
search_tag: Partner
alias: "/shopify_data/"
page_order: 1
---

# BrazeのShopifyデータ

> Braze Shopifyのお客様は、カスタムイベントにネストされたオブジェクトのサポートを使用することで、ネストされたイベントプロパティのLiquidテンプレート変数を使用できます。

アプリのインストールが完了すると、BrazeはWebhookとScriptTagのShopifyインテグレーションを自動的に作成します。サポートされているShopifyイベントがBrazeカスタムイベントおよびカスタム属性にどのようにマッピングされるかについては、以下の表を参照してください。

## サポートされているShopifyイベント

{% tabs %}
{% tab Shopify Events %}
{% subtabs global %}
{% subtab Product Viewed %}
イベント<br>
** =  ( タイプ)[カスタムイベント]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)


{% raw %}
|変数 |リキッドテンプレート |
| --- | --- |
|アイテム ID | `{{event_properties.${id}}}` |
|アイテムタイトル | `{{event_properties.${title}}}` |
|商品価格 | `{{event_properties.${price}}}` |
|アイテムベンダー | `{{event_properties.${vendor}}}` |
|アイテム画像 | `{{event_properties.${images}}}` |


{% endraw %}
{% endsubtab %}


{% subtab Product Clicked %}
イベント<br>
** =  ( タイプ)[カスタムイベント]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)


{% raw %}
|変数 |リキッドテンプレート |
| --- | --- |
|アイテム ID | `{{event_properties.${id}}}` |
|アイテムタイトル | `{{event_properties.${title}}}` |
|商品価格 | `{{event_properties.${price}}}` |
|アイテムベンダー | `{{event_properties.${vendor}}}` |
|アイテム画像 | `{{event_properties.${images}}}` |
{% endraw %}
{% endsubtab %}


{% subtab Abandoned Cart %}
イベント<br>
** =  ( タイプ)[カスタムイベント]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)


{% raw %}
|変数 |リキッドテンプレート |
| --- | --- |
|アイテム ID | `{{event_properties.${line_items}[0].product_id}}` |
|アイテム数量 | `{{event_properties.${line_items}[0].quantity}}` |
|アイテムSKU | `{{event_properties.${line_items}[0].sku}}` |
|アイテムタイトル | `{{event_properties.${line_items}[0].title}}` |
|アイテムベンダー | `{{event_properties.${line_items}[0].vendor}}` |
|アイテムのプロパティ | `{{event_properties.${line_items}[0].properties}}` |
|商品価格 | `{{event_properties.${line_items}[0].price}}` |
|バリアント ID | `{{event_properties.${line_items}[0].variant_id}}` |
{% endraw %}
{% endsubtab %}


{% subtab Abandoned Checkout %}
イベント<br>
** =  ( タイプ)[カスタムイベント]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)


{% raw %}
|変数 |リキッドテンプレート |
| --- | --- |
|チェックアウト ID | `{{event_properties.${checkout_id}}}` |
|放棄されたカードのURL | `{{event_properties.${abandoned_checkout_url}}}` |
|割引コード | `{{event_properties.${discount_code}}}` |
|合計金額 | `{{event_properties.${total_price}}}` |
|割引額 | `{{event_properties.${applied_discount}[0].amount}}` |
|割引タイトル | `{{event_properties.${applied_discount}[0].title}}` |
|割引の説明 | `{{event_properties.${applied_discount}[0].description}}` |
|アイテム ID | `{{event_properties.${line_items}[0].product_id}}` |
|アイテム数量 | `{{event_properties.${line_items}[0].quantity}}` |
|アイテムSKU | `{{event_properties.${line_items}[0].sku}}` |
|アイテムタイトル | `{{event_properties.${line_items}[0].title}}` |
|アイテムベンダー | `{{event_properties.${line_items}[0].vendor}}` |
|アイテムのプロパティ | `{{event_properties.${line_items}[0].properties}}` |
|商品価格 | `{{event_properties.${line_items}[0].price}}` |
|バリアント ID | `{{event_properties.${line_items}[0].variant_id}}` |
|バリアントタイトル | `{{event_properties.${line_items}[0].variant_title}}` |
{% endraw %}
{% endsubtab %}


{% subtab Created Order %}


イベント<br>
** =  ( タイプ)[カスタムイベント]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)

{% raw %}
```json
{
"name": "shopify_created_order",
    "time": "2024-03-26T11:03:55-04:00",
    "properties": {
      "order_id": 5603014377622,
      "line_items": [
        {
          "fulfillment_status": null,
          "name": "Blue Silk Tuxedo - xs",
          "price": 78,
          "product_id": 5847345004694,
          "properties": [],
          "quantity": 1,
          "sku": "",
          "title": "Blue Silk Tuxedo",
          "variant_id": 36790647521430,
          "variant_title": "xs",
          "vendor": "Liam Fashions"
        }
      ],
      "fulfillments": [],
      "shipping": [
        {
          "title": "First Class Package International",
          "price": 33.85
        }
      ],
      "shopify_storefront": "example-store.myshopify.com",
      "total_price": 111.85,
      "confirmed": true,
      "total_discounts": 0,
      "discount_codes": [],
      "order_number": 1005,
      "order_status_url": "https://example-store.myshopify.com/50699042966/orders/6e43c91d84b8e7832990502aca637a13/authenticate?key=d8184818cd06f09ac680ea82da78ce3e",
      "cancelled_at": null,
      "tags": "",
      "closed_at": null,
      "fulfillment_status": null,
      "referring_site": "",
      "payment_gateway_names": [
        "bogus"
      ],
      "shipping_address": {
        "address1": "1111 street",
        "address2": null,
        "city": "New York",
        "country": "United States",
        "first_name": "John",
        "last_name": "Doe",
        "province": "New York",
        "zip": "11111"
      },
      "billing_address": {
        "address1": "1111 street",
        "address2": null,
        "city": "New York",
        "country": "United States",
        "first_name": "John",
        "last_name": "Doe",
        "province": "New York",
        "zip": "11111"
      }
    }
  }
```
{% endraw %}

{% raw %}
|変数 |リキッドテンプレート |
| --- | --- |
|注文番号 | `{{event_properties.${order_id}}}` |
|確認済みステータス | `{{event_properties.${confirmed}}}` |
|注文状況 URL | `{{event_properties.${order_status_url}}}` |
|注文番号 | `{{event_properties.${order_number}}}` |
|キャンセルされたタイムスタンプ | `{{event_properties.${cancelled_at}}}` |
|合計割引 | `{{event_properties.${total_discounts}}}` |
|合計金額 | `{{event_properties.${total_price}}}` |
タグ
|割引コード | `{{event_properties.${discount_codes}}}` |
|アイテム ID | `{{event_properties.${line_items}[0].product_id}}` |
|アイテム数量 | `{{event_properties.${line_items}[0].quantity}}` |
|アイテムSKU | `{{event_properties.${line_items}[0].sku}}` |
|アイテムタイトル | `{{event_properties.${line_items}[0].title}}` |
|アイテムベンダー | `{{event_properties.${line_items}[0].vendor}}` |
|アイテムのプロパティ | `{{event_properties.${line_items}[0].properties}}` |
|商品価格 | `{{event_properties.${line_items}[0].price}}` |
|バリアント ID | `{{event_properties.${line_items}[0].variant_id}}` |
|バリアントタイトル | `{{event_properties.${line_items}[0].variant_title}}` |
|船荷地 | `{{event_properties.${shipping}[0].title}}` |
|配送料 | `{{event_properties.${shipping}[0].price}}` |
Shopify ストア
|フルフィルメントステータス | `{{event_properties.${fulfillment_status}}}` |
|参考サイト | `{{event_properties.${referring_site}}}` |
|支払いゲートウェイ名 | `{{event_properties.${payment_gateway_names}}}` |
|配送先住所 1 行 | `{{event_properties.${shipping_address[0].address1}}}` |
|配送先住所 2 行目 | `{{event_properties.${shipping_address[0].address2}}}` |
|配送先住所の市区町村 | `{{event_properties.${shipping_address[0].city}}}` |
|配送先住所の国 | `{{event_properties.${shipping_address[0].country}}}` |
|配送先住所の名 | `{{event_properties.${shipping_address[0].first_name}}}` |
|配送先住所の姓 | `{{event_properties.${shipping_address[0].last_name}}}` |
|配送先住所の都道府県 | `{{event_properties.${shipping_address[0].province}}}` |
|配送先住所 Zip | `{{event_properties.${shipping_address[0].zip}}}` |
|請求先住所 1 行目 | `{{event_properties.${billing_address[0].address1}}}` |
|請求先住所 2 行目 | `{{event_properties.${billing_address[0].address2}}}` |
|請求先住所の市区町村 | `{{event_properties.${billing_address[0].city}}}` |
|請求先住所の国 | `{{event_properties.${billing_address[0].country}}}` |
|請求先住所の名 | `{{event_properties.${billing_address[0].first_name}}}` |
|請求先住所の姓 | `{{event_properties.${shipping_address[0].last_name}}}` |
|請求先住所の都道府県 | `{{event_properties.${billing_address[0].province}}}` |
|請求先住所 Zip | `{{event_properties.${billing_address[0].zip}}}` |
{% endraw %}


{% endsubtab %}
{% subtab Purchase %}


イベント購入<br>
** =  ( タイプ)[Braze 購入イベント]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events/)


{% raw %}
|変数 |リキッドテンプレート |
| --- | --- |
|アイテムSKU | `{{event_properties.${line_items}[0].sku}}` |
|アイテムタイトル | `{{event_properties.${line_items}[0].title}}` |
|アイテムベンダー | `{{event_properties.${line_items}[0].vendor}}` |
|アイテムのプロパティ | `{{event_properties.${line_items}[0].properties}}` |
|バリアント ID | `{{event_properties.${line_items}[0].variant_id}}` |
|バリアントタイトル | `{{event_properties.${line_items}[0].variant_title}}` |
{% endraw %}


{% endsubtab %}
{% subtab Paid Order %}
イベント<br>
** =  ( タイプ)[カスタムイベント]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)


{% raw %}
|変数 |リキッドテンプレート |
| --- | --- |
|注文番号 | `{{event_properties.${order_id}}}` |
|確認済みステータス | `{{event_properties.${confirmed}}}` |
|注文状況 URL | `{{event_properties.${order_status_url}}}` |
|注文番号 | `{{event_properties.${order_number}}}` |
|キャンセルされたタイムスタンプ | `{{event_properties.${cancelled_at}}}` |
|合計割引 | `{{event_properties.${total_discounts}}}` |
|合計金額 | `{{event_properties.${total_price}}}` |
タグ
|割引コード | `{{event_properties.${discount_codes}}}` |
|アイテム ID | `{{event_properties.${line_items}[0].product_id}}` |
|アイテム数量 | `{{event_properties.${line_items}[0].quantity}}` |
|アイテムSKU | `{{event_properties.${line_items}[0].sku}}` |
|アイテムタイトル | `{{event_properties.${line_items}[0].title}}` |
|アイテムベンダー | `{{event_properties.${line_items}[0].vendor}}` |
|アイテムのプロパティ | `{{event_properties.${line_items}[0].properties}}` |
|商品価格 | `{{event_properties.${line_items}[0].price}}` |
|船荷地 | `{{event_properties.${shipping}[0].title}}` |
|配送料 | `{{event_properties.${shipping}[0].price}}` |
|バリアント ID | `{{event_properties.${line_items}[0].variant_id}}` |
|バリアントタイトル | `{{event_properties.${line_items}[0].variant_title}}` |
{% endraw %}
{% endsubtab %}


{% subtab Partially Fulfilled Order %}
イベント<br>
** =  ( タイプ)[カスタムイベント]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)


{% raw %}
|変数 |リキッドテンプレート |
| --- | --- |
|注文番号 | `{{event_properties.${order_id}}}` |
|合計金額 | `{{event_properties.${total_price}}}` |
|合計割引 | `{{event_properties.${total_discounts}}}` |
|確認済みステータス | `{{event_properties.${confirmed}}}` |
|注文状況 URL | `{{event_properties.${order_status_url}}}` |
|注文番号 | `{{event_properties.${order_number}}}` |
|キャンセルされたタイムスタンプ | `{{event_properties.${cancelled_at}}}` |
|クローズドタイムスタンプ | `{{event_properties.${closed_at}}}` |
|アイテム ID | `{{event_properties.${line_items}[0].product_id}}` |
|アイテム数量 | `{{event_properties.${line_items}[0].quantity}}` |
|アイテムSKU | `{{event_properties.${line_items}[0].sku}}` |
|アイテムタイトル | `{{event_properties.${line_items}[0].title}}` |
|アイテムベンダー | `{{event_properties.${line_items}[0].vendor}}` |
|アイテム名 | `{{event_properties.${line_items}[0].name}}` |
|アイテムのプロパティ | `{{event_properties.${line_items}[0].properties}}` |
|商品価格 | `{{event_properties.${line_items}[0].price}}` |
|船荷地 | `{{event_properties.${shipping}[0].title}}` |
|配送料 | `{{event_properties.${shipping}[0].price}}` |
|フルフィルメントステータス | `{{event_properties.${fulfillment_status}}}` |
|フルフィルメントの出荷状況 | `{{event_properties.${fulfillments}[0].shipment_status}}` |
|フルフィルメントステータス | `{{event_properties.${fulfillments}[0].status}}` |
|フルフィルメント追跡会社| `{{event_properties.${fulfillments}[0].tracking_company}}` |
|フルフィルメント追跡番号 | `{{event_properties.${fulfillments}[0].tracking_number}}` |
|フルフィルメント追跡番号 | `{{event_properties.${fulfillments}[0].tracking_numbers}}` |
|フルフィルメント追跡URL | `{{event_properties.${fulfillments}[0].tracking_url}}` |
|フルフィルメント追跡URL | `{{event_properties.${fulfillments}[0].tracking_urls}}` |
|フルフィルメントステータス | `{{event_properties.${fulfillments}[0].line_items[0].fulfillment_status}}` |
|フルフィルメント名 | `{{event_properties.${fulfillments}[0].line_items[0].name}}` |
|フルフィルメント価格 | `{{event_properties.${fulfillments}[0].line_items[0].price}}` |
|フルフィルメント製品ID | `{{event_properties.${fulfillments}[0].line_items[0].product_id}}` |
|フルフィルメント数量 | `{{event_properties.${fulfillments}[0].line_items[0].quantity}}`|
|フルフィルメント配送 | `{{event_properties.${fulfillments}[0].line_items[0].requires_shipping}}` |
|フルフィルメントSKU | `{{event_properties.${fulfillments}[0].line_items[0].sku}}` |
|フルフィルメントタイトル | `{{event_properties.${fulfillments}[0].line_items[0].title}}` |
|フルフィルメントベンダー | `{{event_properties.${fulfillments}[0].line_items[0].vendor` |
|バリアント ID | `{{event_properties.${line_items}[0].variant_id}}` |
|バリアントタイトル | `{{event_properties.${line_items}[0].variant_title}}` |
{% endraw %}
{% endsubtab %}


{% subtab Fulfilled Order %}
イベント<br>
** =  ( タイプ)[カスタムイベント]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)


{% raw %}
|変数 |リキッドテンプレート |
| --- | --- |
|注文番号 | `{{event_properties.${order_id}}}` |
|合計金額 | `{{event_properties.${total_price}}}` |
|合計割引 | `{{event_properties.${total_discounts}}}` |
|確認済みステータス | `{{event_properties.${confirmed}}}` |
|注文状況 URL | `{{event_properties.${order_status_url}}}` |
|注文番号 | `{{event_properties.${order_number}}}` |
|キャンセルされたタイムスタンプ | `{{event_properties.${cancelled_at}}}` |
|クローズドタイムスタンプ | `{{event_properties.${closed_at}}}` |
|アイテム ID | `{{event_properties.${line_items}[0].product_id}}` |
|アイテム数量 | `{{event_properties.${line_items}[0].quantity}}` |
|アイテムSKU | `{{event_properties.${line_items}[0].sku}}` |
|アイテムタイトル | `{{event_properties.${line_items}[0].title}}` |
|アイテムベンダー | `{{event_properties.${line_items}[0].vendor}}` |
|アイテム名 | `{{event_properties.${line_items}[0].name}}` |
|アイテムのプロパティ | `{{event_properties.${line_items}[0].properties}}` |
|商品価格 | `{{event_properties.${line_items}[0].price}}` |
|船荷地 | `{{event_properties.${shipping}[0].title}}` |
|配送料 | `{{event_properties.${shipping}[0].price}}` |
|フルフィルメントステータス | `{{event_properties.${fulfillment_status}}}` |
|フルフィルメントの出荷状況 | `{{event_properties.${fulfillments}[0].shipment_status}}` |
ステータス
|フルフィルメント追跡会社| `{{event_properties.${fulfillments}[0].Fulfillment tracking_company}}` |
|フルフィルメント追跡番号 | `{{event_properties.${fulfillments}[0].Fulfillment tracking_number}}` |
|フルフィルメント追跡番号 | `{{event_properties.${fulfillments}[0].Fulfillment tracking_numbers}}` |
|フルフィルメント追跡URL | `{{event_properties.${fulfillments}[0].Fulfillment tracking_url}}` |
|フルフィルメント追跡URL | `{{event_properties.${fulfillments}[0].Fulfillment tracking_urls}}` |
|フルフィルメントステータス | `{{event_properties.${fulfillments}[0].line_items[0].fulfillment_status}}` |
|フルフィルメント名 | `{{event_properties.${fulfillments}[0].line_items[0].name}}` |
|フルフィルメント価格 | `{{event_properties.${fulfillments}[0].line_items[0].price}}` |
|フルフィルメント製品ID | `{{event_properties.${fulfillments}[0].line_items[0].product_id}}` |
|フルフィルメント数量 | `{{event_properties.${fulfillments}[0].line_items[0].quantity}}`|
|フルフィルメント配送 | `{{event_properties.${fulfillments}[0].line_items[0].requires_shipping}}` |
|フルフィルメントSKU | `{{event_properties.${fulfillments}[0].line_items[0].sku}}` |
|フルフィルメントタイトル | `{{event_properties.${fulfillments}[0].line_items[0].title}}` |
|フルフィルメントベンダー | `{{event_properties.${fulfillments}[0].line_items[0].vendor` |
|バリアント ID | `{{event_properties.${line_items}[0].variant_id}}` |
|バリアントタイトル | `{{event_properties.${line_items}[0].variant_title}}` |
{% endraw %}
{% endsubtab %}


{% subtab Cancelled Order %}
イベント<br>
** =  ( タイプ)[カスタムイベント]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)


{% raw %}
|変数 |リキッドテンプレート |
| --- | --- |
|注文番号 | `{{event_properties.${order_id}}}` |
|合計金額 | `{{event_properties.${total_price}}}` |
|合計割引 | `{{event_properties.${total_discounts}}}` |
|確認済み | `{{event_properties.${confirmed}}}` |
|注文状況 URL | `{{event_properties.${order_status_url}}}` |
|注文番号 | `{{event_properties.${order_number}}}` |
|キャンセルされたタイムスタンプ | `{{event_properties.${cancelled_at}}}` |
タグ
|割引コード | `{{event_properties.${discount_codes}}}` |
|フルフィルメントステータス | `{{event_properties.${fulfillment_status}}}` |
|フルフィルメント | `{{event_properties.${fulfillments}}}` |
|アイテム ID | `{{event_properties.${line_items}[0].product_id}}` |
|アイテム数量 | `{{event_properties.${line_items}[0].quantity}}` |
|アイテムSKU | `{{event_properties.${line_items}[0].sku}}` |
|アイテムタイトル | `{{event_properties.${line_items}[0].title}}` |
|アイテムベンダー | `{{event_properties.${line_items}[0].vendor}}` |
|アイテム名 | `{{event_properties.${line_items}[0].name}}` |
|アイテムのプロパティ | `{{event_properties.${line_items}[0].properties}}` |
|フルフィルメントステータス | `{{event_properties.${line_items}[0].fulfillment_status}}` |
|船荷地 | `{{event_properties.${shipping}[0].title}}` |
|配送料 | `{{event_properties.${shipping}[0].price}}` |
|バリアント ID | `{{event_properties.${line_items}[0].variant_id}}` |
|バリアントタイトル | `{{event_properties.${line_items}[0].variant_title}}` |
{% endraw %}
{% endsubtab %}

{% subtab Created Refund %}
イベント<br>
** =  ( タイプ)[カスタムイベント]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)


{% raw %}
|変数 |リキッドテンプレート |
| --- | --- |
|注文番号 | `{{event_properties.${order_id}}}` |
|オーダーノート | `{event_properties.${note}}}` |
|アイテム ID | `{{event_properties.${line_items}[0].product_id}}` |
|アイテム数量 | `{{event_properties.${line_items}[0].quantity}}` |
|アイテムSKU | `{{event_properties.${line_items}[0].sku}}` |
|アイテムタイトル | `{{event_properties.${line_items}[0].title}}` |
|アイテムベンダー | `{{event_properties.${line_items}[0].vendor}}` |
|アイテム名 | `{{event_properties.${line_items}[0].name}}` |
|アイテムのプロパティ | `{{event_properties.${line_items}[0].properties}}` |
|商品価格 | `{{event_properties.${line_items}[0].price}}` |
|バリアント ID | `{{event_properties.${line_items}[0].variant_id}}` |
|バリアントタイトル | `{{event_properties.${line_items}[0].variant_title}}` |
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Example Payload %}
{% subtabs global %}
{% subtab Product Viewed %}
```json
{
 "name": "shopify_product_viewed",
 "properties": {
     "id": 5971657097407,
     "title": "Example T-Shirt",
     "price": 1999,
     "vendor": "Acme",
     "images": [
         "//cdn.shopify.com/s/files/1/0503/3849/6703/products/green-t-shirt.jpg?v=1603397913"
     ]
 }
}
```
{% endsubtab %}
{% subtab Product Clicked %}
```json
{
   "name": "shopify_product_clicked",
   "properties": {
       "id": 5971657097407,
       "title": "Example T-Shirt",
       "price": 1999,
       "vendor": "Acme",
       "images": [
           "//cdn.shopify.com/s/files/1/0503/3849/6703/products/green-t-shirt.jpg?v=1603397913"
       ]
   }
}
```
{% endsubtab %}
{% subtab Abandoned Cart %}
\`\`\`json
{
"name": "shopify_abandoned_cart",
"time": "2022-10-14T15:08:31.571Z",
"properties": {
"cart_id": "163989958f6b0de13f3b4f702fa5ee0d",
"line_items": [
       {
         "price": 60,
         "product_id": 7110622675033,
         "properties": null,
         "quantity": 1,
         "sku": null,
         "title": "Spinach Surprise Smoothie - 12 Pack",
         "variant_id": 40094740545625,
         "vendor": "Jennifer's Juice"
       }
        
   
   "braze\_id":"63497b3ca3eabd0053380451"
     

\`\`\`json
{
"name": "shopify_abandoned_checkout",
"time": "2020-09-10T18:53:37-04:00",
"properties": {
"applied_discount": {
"amount": "30.00",
"title": "XYZPromotion",
"description": "Promotionalitemforblackfriday."
},
 "discount\_code":"30\_DOLLARS\_OFF"、
 "total\_price":1\.
 "line\_items": [
        {
   "price": "199.00",
   "properties": {},      
        PRODUCT\_ID1\.
            "数量":1\.
            SKU"IPOD2008PINK"、
          Title: 「iPodNano-8GB」、
          "variant\_id":1\.
          "variant\_title":「ピンクのiPod Nano 8 GB」、
          「ベンダー」:「りんご」、
        
      
 "abandoned\_checkout\_url": "https://checkout.local/690933842/checkouts/123123123/recover?key=example-secret-token",
"checkout\_id":1\.


 \`\`\`json
 {
"name": "shopify_created_order",
"time": "2020-09-10T18:53:45-04:00",
"properties": {
"total_discounts": "5.00",
"total_price": "403.00",
"discount_codes": [],
"line_items": [
{
"product_id": 632910392,
"quantity": 1,
"sku": "IPOD2008PINK",
"title": "IPodNano-8GB",
"variant_id": 40094740545625,
"variant_title": "Pink iPod Nano 8 GB",
"vendor": null,
"name": "IPodNano-8GB",
"properties": [],
"price": "199.00"
},
 {
"product_id": 632910393,
"quantity": 1,
"sku": "IPOD2008SILVER",
"title": "IPodNano-8GB",
"variant_id": 40094740545626,
"variant_title": "Silver iPod Nano 8 GB",
"vendor": null,
"name": "IPodNano-8GB",
"properties": [],
"price": "199.00"
}
   
   "order\_id":1\.
   「確認済み」:false、
   "order\_status\_url": "https://apple.myshopify.com/690933842/orders/123456abcd/authenticate?key=abcdefg",
     "order\_number":1\.
       "cancelled\_at":"2020-09-10T18:53:45-04:00"、
       "shipping": [
            {
       "title": "Standard",
       "price": "10.00"
     },
            {
       "title": "Expedited",
       "price": "25.00"
     }
          
       "タグ": "重い"
       
       
       \`\`\`json
       {
"product_id": 632910392,
"currency": "USD",
"price": "199.00",
"time": "2020-09-10T18:53:45-04:00",
"quantity": 1,
"source": "shopify",
"properties": {
"name": "IPodNano-8GB",
"sku": "IPOD2008PINK",
"variant_id": 40094740545626,
"variant_title": "Silver iPod Nano 8 GB",
"vendor": null,
"properties": []
}
     
     \`\`\`json
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
       
       
       
       \`\`\`json
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
       
       "shipping": [
            {
       "title": "Standard",
       "price": "0.00"
     }
          
     "total\_price":1\.
   "confirmed":true、
   "total\_discounts":1\.
   "discount\_codes":[]、
   "order\_number":1\.
   "order\_status\_url": "https://test-store.myshopify.com/",
   "cancelled\_at":null、
   タグ
   "closed\_at":null、
 "fulfillment\_status": "部分的",
"フルフィルメント": [
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

 
 
 
 "braze\_id": "abc123abc123"
 
 \`\`\`json
 
   "名前": "shopify\_fulfilled\_order",
   時間"2022-05-23T14:44:34-04:00",
   プロパティ：
   "order\_id":1\.
   "line\_items": [
   
 "数量":1\.
PRODUCT\_ID1\.
"sku":null、
Title: 「ダークデニムトップス」、
 "variant\_id":1\.
 "variant\_title":「スモールダークデニムトップス」、


       "vendor": "partners-demo",
       "name": "Dark Denim Top",
       "properties": [],
       "price": "60.00",
       "fulfillment_status": "fulfilled"
     }
   
   "shipping": [
        {
       "title": "Standard",
       "price": "0.00"
     }
      
   "total\_price":1\.
   "confirmed":true、
   "total\_discounts":1\.
   "discount\_codes":[]、
   "order\_number":1\.
   "order\_status\_url": "https://test-store.myshopify.com/",
   "cancelled\_at":null、
   タグ
   "closed\_at":"2022-05-23T14:44:34-04:00",
     "fulfillment\_status": "履行済み",
       "フルフィルメント": [
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
              
       
       
       
       "braze\_id":"123abc123abc"
       
     \`\`\`json
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
 
 "shipping": [
     {
       "title": "Standard",
       "price": "0.00"
     }
   
"total\_price":1\.
 "confirmed":true、
 "total\_discounts":1\.
 "discount\_codes":[]、
   "order\_number":1\.
   "order\_status\_url": "https://test-store.myshopify.com/",
     "cancelled\_at":"2022-05-23T14:40:52-04:00",
       タグ
       "closed\_at":"2022-05-23T14:40:51-04:00",
       "fulfillment\_status":null、
       「フルフィルメント」:[]
       
       "braze\_id":"123abc123abc"
       
       \`\`\`json
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
       
     
   "braze\_id": "abc123abc123"
   
   \`\`\`
   {% endsubtab %}
   {% endsubtabs %}
   {% endtab %}
   {% endtabs %}

## サポートされているShopifyカスタム属性
{% tabs local %}
{% tab Shopify Custom Attributes %}
|属性名 |説明 |

| `shopify_tags`  |ショップのオーナーが顧客に添付したタグで、カンマ区切り値の文字列としてフォーマットされています。顧客は最大 250 個のタグを持つことができます。各タグは最大 255 文字です。|
| `shopify_total_spent` |顧客が注文履歴全体で支払った合計金額。|
| `shopify_order_count` |この顧客に関連付けられている注文の数。テスト注文とアーカイブされた注文はカウントされません。|
| `shopify_last_order_id` |顧客の最後の注文の ID。|
| `shopify_last_order_name` |顧客の最後の注文の名前。これは、注文リソースのフィールドに直接 `name` 関連しています。 |
| `shopify_zipcode` |既定の住所からの顧客の郵便番号。|
| `shopify_province` |既定の住所からの顧客の都道府県。|
{: .reset-td-br-1 .reset-td-br-2}

### Liquid のパーソナライゼーション

Shopifyのカスタム属性にリキッドパーソナライゼーションを追加するには、[ **\+ パーソナライゼーション**] を選択します。次に、パーソナライゼーションタイプとして **「カスタム属性** 」を選択します。

![The "Add Personalization" section with the "Attribute" dropdown extended.]({% image_buster /assets/img/Shopify/add_personalization_2.png %}){: style="max-width:40%;"}

カスタム属性を選択したら、デフォルト値を入力し、Liquid スニペットをメッセージにコピーします。

![Pasting a Liquid snippet into a message.]({% image_buster /assets/img/Shopify/copy_liquid_snippet.png %})

{% endtab %}
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
{% endtabs %}

## サポートされているShopifyの標準属性

- メール
- 名
- 姓
- 電話
- 市区町村
- 国

{% alert note %}
Brazeは、既存のユーザープロフィールとのデータに違いがある場合にのみ、サポートされているShopifyカスタム属性とBraze標準属性を更新します。たとえば、受信Shopifyデータにボブの名が含まれていて、ボブがBrazeユーザープロフィールに名としてすでに存在する場合、Brazeは更新をトリガーせず、データポイントは請求されません。
{% endalert %}

## セグメンテーション

Shopifyのイベントは、セグメンテーションの [既存のカスタムフィルター]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) すべてで絞り込むことができます。 

![カスタムイベント「shopify\_checkouts\_abandon」のフィルターが強調表示されたShopify\_Testセグメントのセグメント詳細ページ。[12]{: style="max-width:80%;"}

さらに、Brazeの幅広い購入フィルターを使用して、以下に基づいてユーザーのセグメントを作成することもできます。
最初
\- 過去30日以内に購入した商品
\- 購入回数

![2020 年 10 月 17 日以降に初めて購入したユーザーのセグメンテーション フィルター。[13]

![特定の製品 ID をセグメンテーション フィルターとして検索します。[14]

{% alert note %}
カスタムイベントプロパティでセグメント化する場合は、カスタマーサクセスマネージャーまたはBraze [サポート]({{site.baseurl}}/braze_support/) と協力して、セグメンテーションとLiquid内で使用するすべての関連イベントプロパティのフィルタリングを有効にしてください。
{% endalert %} 

## キャンペーンとキャンバスのトリガー 

BrazeのShopifyカスタムイベントでは、他の [カスタムイベント]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-storage)と同じようにキャンバスやキャンペーンをトリガーできます。たとえば、キャンバスのエントリー条件内でShopify `shopify_checkouts_abandon` イベントからトリガーされるアクションベースのキャンバスを作成できます。 

![カスタムイベント「shopify\_checkouts\_abandon」を実行するユーザーを入力するアクションベースのキャンバス。[5]

カスタムイベントプロパティのネストされたオブジェクトのサポートにより、お客様はネストされたイベントプロパティを使用してキャンペーンとキャンバスをトリガーできるようになりました。以下は、カスタムイベントの特定の商品を使用してキャンペーンをトリガーする `shopify_created_order` 例です。必ず を使用して `list_items[].product_id` 、アイテム リストのインデックスを作成し、製品 ID にアクセスしてください。

![ネストされたプロパティ「product\_id」が特定の数値に等しいカスタムイベント「shopify\_created\_order」を実行するユーザーに送信するアクションベースのキャンペーン。[26]

[5]: {% image_buster /assets/img/Shopify/shopify_integration11.png %}
[12]: {% image_buster /assets/img/Shopify/shopify_segmentation2.png %}
[13]: {% image_buster /assets/img/Shopify/shopify_segmentation3.png %}
[14]: {% image_buster /assets/img/Shopify/shopify_segmentation4.png %}
[26]: {% image_buster /assets/img/Shopify/shopify_integration17.png %}
