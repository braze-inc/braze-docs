---
nav_title: Shopify Data in Braze
article_title:BrazeでShopifyデータを使用する
description:この記事では、パーソナライズとセグメンテーションのためにBrazeでShopifyデータを使用する方法について説明します。
page_type: partner
search_tag:Partner
alias: "/shopify_data/"
page_order:1
---

# BrazeのShopifyデータ

> ネストされたオブジェクトサポートを使用してカスタムイベントを作成することで、Braze Shopifyの顧客はネストされたイベントプロパティのLiquidテンプレート変数を使用できます。

アプリのインストールが完了すると、Brazeは自動的にShopifyとのウェブフックおよびScriptTag統合を作成します。詳細については、サポートされているShopifyイベントがBrazeのカスタムイベントおよびカスタム属性にどのようにマップされるかについて、次の表を参照してください。

## サポートされているShopifyイベント

{% tabs %}
{% tab Shopify Events %}
{% subtabs global %}
{% subtab Product Viewed %}
**イベント**： `shopify_product_viewed`<br>
**タイプ**：[カスタムイベント]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)


{% raw %}
| 変数 | 液体テンプレート |
| --- | --- |
| Item ID | `{{event_properties.${id}}}` |
| アイテムのタイトル  | `{{event_properties.${title}}}` |
| 商品価格 | `{{event_properties.${price}}}` |
| アイテムベンダー | `{{event_properties.${vendor}}}` |
| アイテム画像 | `{{event_properties.${images}}}` |


{% endraw %}
{% endsubtab %}


{% subtab Product Clicked %}
**イベント**： `shopify_product_clicked`<br>
**タイプ**：[カスタムイベント]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)


{% raw %}
| 変数 | 液体テンプレート |
| --- | --- |
| Item ID | `{{event_properties.${id}}}` |
| アイテムのタイトル  | `{{event_properties.${title}}}` |
| 商品価格 | `{{event_properties.${price}}}` |
| アイテムベンダー | `{{event_properties.${vendor}}}` |
| アイテム画像 | `{{event_properties.${images}}}` |
{% endraw %}
{% endsubtab %}


{% subtab Abandoned Cart %}
**イベント**： `shopify_abandoned_cart`<br>
**タイプ**：[カスタムイベント]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)


{% raw %}
| 変数 | 液体テンプレート |
| --- | --- |
| Item ID | `{{event_properties.${line_items}[0].product_id}}` |
| アイテム数量 | `{{event_properties.${line_items}[0].quantity}}` |
| アイテムSKU | `{{event_properties.${line_items}[0].sku}}` |
| アイテムのタイトル | `{{event_properties.${line_items}[0].title}}` |
| アイテムベンダー | `{{event_properties.${line_items}[0].vendor}}` |
| アイテムのプロパティ | `{{event_properties.${line_items}[0].properties}}` |
| アイテムの価格 | `{{event_properties.${line_items}[0].price}}` |
| バリアントID | `{{event_properties.${line_items}[0].variant_id}}` |
{% endraw %}
{% endsubtab %}


{% subtab Abandoned Checkout %}
**イベント**： `shopify_abandoned_checkout`<br>
**タイプ**：[カスタムイベント]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)


{% raw %}
| 変数 | 液体テンプレート |
| --- | --- |
チェックアウトID | `{{event_properties.${checkout_id}}}` |
放棄されたカードのURL `{{event_properties.${abandoned_checkout_url}}}`
| 割引コード | `{{event_properties.${discount_code}}}` |
| 合計金額 | `{{event_properties.${total_price}}}` |
| 割引額 | `{{event_properties.${applied_discount}[0].amount}}` |
| 割引タイトル | `{{event_properties.${applied_discount}[0].title}}` |
| 割引説明 | `{{event_properties.${applied_discount}[0].description}}` |
| アイテムID | `{{event_properties.${line_items}[0].product_id}}` |
| アイテム数量 | `{{event_properties.${line_items}[0].quantity}}` |
| アイテム SKU | `{{event_properties.${line_items}[0].sku}}` |
| アイテムのタイトル | `{{event_properties.${line_items}[0].title}}` |
| アイテムベンダー | `{{event_properties.${line_items}[0].vendor}}` |
| アイテムのプロパティ | `{{event_properties.${line_items}[0].properties}}` |
| 商品価格 | `{{event_properties.${line_items}[0].price}}` |
| バリアントID | `{{event_properties.${line_items}[0].variant_id}}` |
| バリアントタイトル | `{{event_properties.${line_items}[0].variant_title}}` |
{% endraw %}
{% endsubtab %}


{% subtab Created Order %}


**イベント**： `shopify_created_order`<br>
**タイプ**：[カスタムイベント]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)

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
| 変数 | 液体テンプレート |
| --- | --- |
| 注文ID | `{{event_properties.${order_id}}}` |
確認済みのステータス | `{{event_properties.${confirmed}}}` |
| 注文状況URL | `{{event_properties.${order_status_url}}}` |
| 注文番号 | `{{event_properties.${order_number}}}` |
| キャンセルされたタイムスタンプ | `{{event_properties.${cancelled_at}}}` |
| 合計割引 | `{{event_properties.${total_discounts}}}` |
| 合計金額 | `{{event_properties.${total_price}}}` |
| タグ: | `{{event_properties.${tags}}}` |
| 割引コード | `{{event_properties.${discount_codes}}}` |
| アイテムID | `{{event_properties.${line_items}[0].product_id}}` |
| アイテム数量 | `{{event_properties.${line_items}[0].quantity}}` |
| Item SKU | `{{event_properties.${line_items}[0].sku}}` |
| アイテムのタイトル | `{{event_properties.${line_items}[0].title}}` |
| アイテムベンダー | `{{event_properties.${line_items}[0].vendor}}` |
| アイテムのプロパティ | `{{event_properties.${line_items}[0].properties}}` |
| アイテムの価格 | `{{event_properties.${line_items}[0].price}}` |
| バリアントID | `{{event_properties.${line_items}[0].variant_id}}` |
| バリアントタイトル | `{{event_properties.${line_items}[0].variant_title}}` |
| 配送タイトル | `{{event_properties.${shipping}[0].title}}` |
| 配送料 | `{{event_properties.${shipping}[0].price}}` |
|Shopify ストア | `{{event_properties.${shopify_storefront}}}`|
| 履行状況 | `{{event_properties.${fulfillment_status}}}` |
| 紹介サイト | `{{event_properties.${referring_site}}}` |
| 支払いゲートウェイ名 | `{{event_properties.${payment_gateway_names}}}` |
| 配送先住所1行目 | `{{event_properties.${shipping_address[0].address1}}}` |
| 配送先住所2行目 | `{{event_properties.${shipping_address[0].address2}}}` |
| 配送先住所の市 | `{{event_properties.${shipping_address[0].city}}}` |
| 配送先住所の国 | `{{event_properties.${shipping_address[0].country}}}` |
| 配送先の名前 | `{{event_properties.${shipping_address[0].first_name}}}` |
| 配送先の姓 | `{{event_properties.${shipping_address[0].last_name}}}` |
| 配送先住所の都道府県 | `{{event_properties.${shipping_address[0].province}}}` |
配送先住所の郵便番号 | `{{event_properties.${shipping_address[0].zip}}}` |
| 請求先住所1行目 | `{{event_properties.${billing_address[0].address1}}}` |
| 請求先住所2行目 | `{{event_properties.${billing_address[0].address2}}}` |
| 請求先住所の市区町村 | `{{event_properties.${billing_address[0].city}}}` |
| 請求先住所の国 | `{{event_properties.${billing_address[0].country}}}` |
| 請求先住所の名 | `{{event_properties.${billing_address[0].first_name}}}` |
| 請求先住所の姓 | `{{event_properties.${shipping_address[0].last_name}}}` |
| 請求先住所の都道府県 | `{{event_properties.${billing_address[0].province}}}` |
請求先住所の郵便番号 | `{{event_properties.${billing_address[0].zip}}}` |
{% endraw %}


{% endsubtab %}
{% subtab Purchase %}


**イベント**:購入<br>
**タイプ**：[ブラゼ購入イベント]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events/)


{% raw %}
| 変数 | 液体テンプレート |
| --- | --- |
| アイテム SKU | `{{event_properties.${line_items}[0].sku}}` |
| アイテムのタイトル  | `{{event_properties.${line_items}[0].title}}` |
| アイテムベンダー | `{{event_properties.${line_items}[0].vendor}}` |
| アイテムのプロパティ | `{{event_properties.${line_items}[0].properties}}` |
| バリアントID | `{{event_properties.${line_items}[0].variant_id}}` |
| バリアントタイトル | `{{event_properties.${line_items}[0].variant_title}}` |
{% endraw %}


{% endsubtab %}
{% subtab Paid Order %}
**イベント**： `shopify_paid_order`<br>
**タイプ**：[カスタムイベント]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)


{% raw %}
| 変数 | 液体テンプレート |
| --- | --- |
| 注文ID | `{{event_properties.${order_id}}}` |
確認済みのステータス | `{{event_properties.${confirmed}}}` |
| 注文状況URL | `{{event_properties.${order_status_url}}}` |
| 注文番号 | `{{event_properties.${order_number}}}` |
| キャンセルされたタイムスタンプ | `{{event_properties.${cancelled_at}}}` |
| 合計割引 | `{{event_properties.${total_discounts}}}` |
| 合計金額 | `{{event_properties.${total_price}}}` |
| タグ: | `{{event_properties.${tags}}}` |
| 割引コード | `{{event_properties.${discount_codes}}}` |
| アイテムID | `{{event_properties.${line_items}[0].product_id}}` |
| アイテム数量 | `{{event_properties.${line_items}[0].quantity}}` |
| Item SKU | `{{event_properties.${line_items}[0].sku}}` |
| アイテムのタイトル | `{{event_properties.${line_items}[0].title}}` |
| アイテムベンダー | `{{event_properties.${line_items}[0].vendor}}` |
| アイテムのプロパティ | `{{event_properties.${line_items}[0].properties}}` |
| アイテムの価格 | `{{event_properties.${line_items}[0].price}}` |
| 配送タイトル | `{{event_properties.${shipping}[0].title}}` |
| 配送料 | `{{event_properties.${shipping}[0].price}}` |
| Variant ID | `{{event_properties.${line_items}[0].variant_id}}` |
| バリアントタイトル | `{{event_properties.${line_items}[0].variant_title}}` |
{% endraw %}
{% endsubtab %}


{% subtab Partially Fulfilled Order %}
**イベント**： `shopify_partially_fulfilled_order`<br>
**タイプ**：[カスタムイベント]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)


{% raw %}
| 変数 | 液体テンプレート |
| --- | --- |
| 注文ID | `{{event_properties.${order_id}}}` |
| 合計金額 | `{{event_properties.${total_price}}}` |
| 合計割引 | `{{event_properties.${total_discounts}}}` |
確認済みのステータス | `{{event_properties.${confirmed}}}` |
| 注文状況のURL | `{{event_properties.${order_status_url}}}` |
| 注文番号 | `{{event_properties.${order_number}}}` |
| キャンセルされたタイムスタンプ | `{{event_properties.${cancelled_at}}}` |
| 閉じたタイムスタンプ | `{{event_properties.${closed_at}}}` |
| アイテムID | `{{event_properties.${line_items}[0].product_id}}` |
| アイテム数量 | `{{event_properties.${line_items}[0].quantity}}` |
| Item SKU | `{{event_properties.${line_items}[0].sku}}` |
| アイテムのタイトル | `{{event_properties.${line_items}[0].title}}` |
| アイテムベンダー | `{{event_properties.${line_items}[0].vendor}}` |
| アイテム名 | `{{event_properties.${line_items}[0].name}}` |
| アイテムのプロパティ | `{{event_properties.${line_items}[0].properties}}` |
| アイテムの価格 | `{{event_properties.${line_items}[0].price}}` |
| 配送タイトル | `{{event_properties.${shipping}[0].title}}` |
| 配送料 | `{{event_properties.${shipping}[0].price}}` |
| Fulfillment Status | `{{event_properties.${fulfillment_status}}}` |
| フルフィルメント出荷状況 | `{{event_properties.${fulfillments}[0].shipment_status}}` |
| Fulfillment Status | `{{event_properties.${fulfillments}[0].status}}` |
| フルフィルメント追跡会社 | `{{event_properties.${fulfillments}[0].tracking_company}}` |
| フルフィルメント追跡番号 | `{{event_properties.${fulfillments}[0].tracking_number}}` |
| フルフィルメント追跡番号 | `{{event_properties.${fulfillments}[0].tracking_numbers}}` |
| フルフィルメント追跡URL | `{{event_properties.${fulfillments}[0].tracking_url}}` |
| フルフィルメント追跡URL | `{{event_properties.${fulfillments}[0].tracking_urls}}` |
| 履行状況 | `{{event_properties.${fulfillments}[0].line_items[0].fulfillment_status}}` |
| Fulfillment Name | `{{event_properties.${fulfillments}[0].line_items[0].name}}` |
| 履行価格 | `{{event_properties.${fulfillments}[0].line_items[0].price}}` |
| Fulfillment Product ID | `{{event_properties.${fulfillments}[0].line_items[0].product_id}}` |
| Fulfillment Quantity | `{{event_properties.${fulfillments}[0].line_items[0].quantity}}`|
| フルフィルメント配送 | `{{event_properties.${fulfillments}[0].line_items[0].requires_shipping}}` |
| Fulfillment SKU | `{{event_properties.${fulfillments}[0].line_items[0].sku}}` |
| 実現タイトル | `{{event_properties.${fulfillments}[0].line_items[0].title}}` |
| フルフィルメントベンダー | `{{event_properties.${fulfillments}[0].line_items[0].vendor` |
| バリアントID | `{{event_properties.${line_items}[0].variant_id}}` |
| バリアントタイトル | `{{event_properties.${line_items}[0].variant_title}}` |
{% endraw %}
{% endsubtab %}


{% subtab Fulfilled Order %}
**イベント**： `shopify_fulfilled_order`<br>
**タイプ**：[カスタムイベント]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)


{% raw %}
| 変数 | 液体テンプレート |
| --- | --- |
| 注文ID | `{{event_properties.${order_id}}}` |
| 合計金額 | `{{event_properties.${total_price}}}` |
| 合計割引 | `{{event_properties.${total_discounts}}}` |
確認済みのステータス | `{{event_properties.${confirmed}}}` |
| 注文状況のURL | `{{event_properties.${order_status_url}}}` |
| 注文番号 | `{{event_properties.${order_number}}}` |
| キャンセルされたタイムスタンプ | `{{event_properties.${cancelled_at}}}` |
| 閉じたタイムスタンプ | `{{event_properties.${closed_at}}}` |
| アイテムID | `{{event_properties.${line_items}[0].product_id}}` |
| アイテム数量 | `{{event_properties.${line_items}[0].quantity}}` |
| Item SKU | `{{event_properties.${line_items}[0].sku}}` |
| アイテムのタイトル | `{{event_properties.${line_items}[0].title}}` |
| アイテムベンダー | `{{event_properties.${line_items}[0].vendor}}` |
| アイテム名 | `{{event_properties.${line_items}[0].name}}` |
| アイテムのプロパティ | `{{event_properties.${line_items}[0].properties}}` |
| アイテムの価格 | `{{event_properties.${line_items}[0].price}}` |
| 配送タイトル | `{{event_properties.${shipping}[0].title}}` |
| 配送料 | `{{event_properties.${shipping}[0].price}}` |
| Fulfillment Status | `{{event_properties.${fulfillment_status}}}` |
| フルフィルメント出荷状況 | `{{event_properties.${fulfillments}[0].shipment_status}}` |
| ステータス| `{{event_properties.${fulfillments}[0].status}}` |
| フルフィルメント追跡会社 | `{{event_properties.${fulfillments}[0].Fulfillment tracking_company}}` |
| フルフィルメント追跡番号 | `{{event_properties.${fulfillments}[0].Fulfillment tracking_number}}` |
| フルフィルメント追跡番号 | `{{event_properties.${fulfillments}[0].Fulfillment tracking_numbers}}` |
| フルフィルメント追跡URL | `{{event_properties.${fulfillments}[0].Fulfillment tracking_url}}` |
| フルフィルメント追跡URL | `{{event_properties.${fulfillments}[0].Fulfillment tracking_urls}}` |
| 履行状況 | `{{event_properties.${fulfillments}[0].line_items[0].fulfillment_status}}` |
| Fulfillment Name | `{{event_properties.${fulfillments}[0].line_items[0].name}}` |
| 履行価格 | `{{event_properties.${fulfillments}[0].line_items[0].price}}` |
| Fulfillment Product ID | `{{event_properties.${fulfillments}[0].line_items[0].product_id}}` |
| Fulfillment Quantity | `{{event_properties.${fulfillments}[0].line_items[0].quantity}}`|
| フルフィルメント配送 | `{{event_properties.${fulfillments}[0].line_items[0].requires_shipping}}` |
| Fulfillment SKU | `{{event_properties.${fulfillments}[0].line_items[0].sku}}` |
| 実現タイトル | `{{event_properties.${fulfillments}[0].line_items[0].title}}` |
| フルフィルメントベンダー | `{{event_properties.${fulfillments}[0].line_items[0].vendor` |
| バリアントID | `{{event_properties.${line_items}[0].variant_id}}` |
| バリアントタイトル | `{{event_properties.${line_items}[0].variant_title}}` |
{% endraw %}
{% endsubtab %}


{% subtab Cancelled Order %}
**イベント**： `shopify_cancelled_order`<br>
**タイプ**：[カスタムイベント]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)


{% raw %}
| 変数 | 液体テンプレート |
| --- | --- |
| 注文ID | `{{event_properties.${order_id}}}` |
| 合計金額 | `{{event_properties.${total_price}}}` |
| 合計割引 | `{{event_properties.${total_discounts}}}` |
確認済み `{{event_properties.${confirmed}}}`
| 注文状況のURL | `{{event_properties.${order_status_url}}}` |
| 注文番号 | `{{event_properties.${order_number}}}` |
| キャンセルされたタイムスタンプ | `{{event_properties.${cancelled_at}}}` |
| タグ: | `{{event_properties.${tags}}}` |
| 割引コード | `{{event_properties.${discount_codes}}}` |
| 履行状況 | `{{event_properties.${fulfillment_status}}}` |
| Fulfillments | `{{event_properties.${fulfillments}}}` |
| Item ID | `{{event_properties.${line_items}[0].product_id}}` |
| アイテム数量 | `{{event_properties.${line_items}[0].quantity}}` |
| Item SKU | `{{event_properties.${line_items}[0].sku}}` |
| アイテムのタイトル | `{{event_properties.${line_items}[0].title}}` |
| アイテムベンダー | `{{event_properties.${line_items}[0].vendor}}` |
| アイテム名 | `{{event_properties.${line_items}[0].name}}` |
| アイテムのプロパティ | `{{event_properties.${line_items}[0].properties}}` |
| Fulfillment Status | `{{event_properties.${line_items}[0].fulfillment_status}}` |
| 配送タイトル | `{{event_properties.${shipping}[0].title}}` |
| 配送料 | `{{event_properties.${shipping}[0].price}}` |
| バリアントID | `{{event_properties.${line_items}[0].variant_id}}` |
| バリアントタイトル | `{{event_properties.${line_items}[0].variant_title}}` |
{% endraw %}
{% endsubtab %}

{% subtab Created Refund %}
**イベント**： `shopify_created_refund`<br>
**タイプ**：[カスタムイベント]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)


{% raw %}
| 変数 | 液体テンプレート |
| --- | --- |
| 注文ID | `{{event_properties.${order_id}}}` |
| 注文メモ | `{event_properties.${note}}}` |
| アイテムID | `{{event_properties.${line_items}[0].product_id}}` |
| アイテム数量 | `{{event_properties.${line_items}[0].quantity}}` |
| Item SKU | `{{event_properties.${line_items}[0].sku}}` |
| アイテムのタイトル | `{{event_properties.${line_items}[0].title}}` |
| アイテムベンダー | `{{event_properties.${line_items}[0].vendor}}` |
| アイテム名 | `{{event_properties.${line_items}[0].name}}` |
| アイテムのプロパティ | `{{event_properties.${line_items}[0].properties}}` |
| アイテムの価格 | `{{event_properties.${line_items}[0].price}}` |
| Variant ID | `{{event_properties.${line_items}[0].variant_id}}` |
| バリアントタイトル | `{{event_properties.${line_items}[0].variant_title}}` |
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
```json
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
     ]
   },
   "braze_id": "63497b3ca3eabd0053380451"
 }

```
{% endsubtab %}
{% subtab Abandoned Checkout %}
```json
{
 "name": "shopify_abandoned_checkout",
 "time": "2020-09-10T18:53:37-04:00",
 "properties": {
   "applied_discount": {
     "amount": "30.00",
     "title": "XYZPromotion",
     "description": "Promotionalitemforblackfriday."
   },
   "discount_code": "30_DOLLARS_OFF",
   "total_price": "398.00",
   "line_items": [
     {
   "price": "199.00",
   "properties": {},       
   "product_id": 632910392,
       "quantity": 1,
       "sku": "IPOD2008PINK",
       "title": "IPodNano-8GB",
       "variant_id": 40094740545625,
       "variant_title": "Pink iPod Nano 8 GB",
       "vendor": "Apple",
     }
   ],
   "abandoned_checkout_url": "https://checkout.local/690933842/checkouts/123123123/recover?key=example-secret-token",
   "checkout_id": "123123123"
 }
}
```
{% endsubtab %}
{% subtab Created Order %}
```json
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
   ],
   "order_id": 820982911946154500,
   "confirmed": false,
   "order_status_url": "https://apple.myshopify.com/690933842/orders/123456abcd/authenticate?key=abcdefg",
   "order_number": 1234,
   "cancelled_at": "2020-09-10T18:53:45-04:00",
   "shipping": [
     {
       "title": "Standard",
       "price": "10.00"
     },
     {
       "title": "Expedited",
       "price": "25.00"
     }
   ],
   "tags": "heavy"
 }
}
```
{% endsubtab %}
{% subtab Purchase %}
```json
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
}
```
{% endsubtab %}
{% subtab Paid Order %}
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
{% subtab Partially Fulfilled Order %}
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
{% subtab Fulfilled Order %}
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
{% subtab Cancelled Order %}
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
{% subtab Created Refund %}
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
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## サポートされているShopifyカスタム属性
{% tabs local %}
{% tab Shopify Custom Attributes %}
| 属性名 | 説明 |
| --- | --- |
`shopify_tags` 店主が顧客に付けたタグで、カンマ区切りの値の文字列としてフォーマットされています。顧客は最大で250のタグを持つことができます。各タグは最大255文字まで使用できます。
| `shopify_total_spent` | 顧客が注文履歴全体で費やした総額。 |
`shopify_order_count` この顧客に関連する注文の数。テストおよびアーカイブされた注文はカウントされません。 |
`shopify_last_order_id` | 顧客の最後の注文のID。 |
`shopify_last_order_name` | 顧客の最後の注文の名前。これは注文リソースの`name`フィールドに直接関連しています。
`shopify_zipcode` | 顧客のデフォルト住所の郵便番号。
`shopify_province` | 顧客のデフォルト住所からの州。 |
{: .reset-td-br-1 .reset-td-br-2}

### Liquid のパーソナライゼーション

Shopifyのカスタム属性にLiquidパーソナライゼーションを追加するには、**\+ パーソナライゼーション**を選択します。次に、パーソナライズのタイプとして**カスタム属性**を選択します。

![The "Add Personalization" section with the "Attribute" dropdown extended.]({% image_buster /assets/img/Shopify/add_personalization_2.png %}){: style="max-width:40%;"}

カスタム属性を選択した後、デフォルト値を入力し、Liquidスニペットをメッセージにコピーします。

![Pasting a Liquid snippet into a message.]({% image_buster /assets/img/Shopify/copy_liquid_snippet.png %})

#### 例のペイロード

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

## サポートされているShopify標準属性

- メール
- 名
- 姓
- 電話
- 市区町村
- 国

{% alert note %}
Brazeは、既存のユーザープロファイルのデータに違いがある場合にのみ、サポートされているShopifyカスタム属性およびBraze標準属性を更新します。例えば、インバウンドのShopifyデータにBobという名前が含まれていて、BobがすでにBrazeユーザープロファイルの名前として存在している場合、Brazeは更新をトリガーせず、データポイントの料金も発生しません。
{% endalert %}

## セグメンテーション

セグメンテーションの[既存のカスタムフィルター]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)を使用して、Shopifyのイベントをフィルタリングできます。 

![Shopify_Testセグメントのセグメント詳細ページで、カスタムイベント「shopify_checkouts_abandon」のフィルターがハイライトされています。][12]{: style="max-width:80%;"}

さらに、Brazeの購入フィルターの幅を使用して、次の条件に基づいてユーザーのセグメントを作成することもできます:
- 最初/最後の購入
- 特定のアプリの最初/最後の購入
- 過去30日以内に購入した製品
- 彼らが行った購入数

![2020年10月17日以降に初めて購入したユーザーのセグメンテーションフィルター。][13]

![特定の製品IDをセグメンテーションフィルターとして検索します。][14]

{% alert note %}
カスタムイベントプロパティでセグメント化を行いたい場合は、セグメンテーションおよびLiquid内で使用したいすべての関連イベントプロパティのフィルタリングを有効にするために、カスタマーサクセスマネージャーまたはBraze [サポート]({{site.baseurl}}/braze_support/)と連携してください。
{% endalert %} 

## キャンペーンとキャンバスのトリガー 

ShopifyのカスタムイベントをBrazeで使用すると、他の[カスタムイベント]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-storage)と同様にキャンバスやキャンペーンをトリガーできます。例えば、Canvasエントリー基準内のShopify `shopify_checkouts_abandon` イベントをトリガーするアクションベースのCanvasを作成することができます。 

![カスタムイベント「shopify_checkouts_abandon」を実行するユーザーを入力するアクションベースのキャンバス。][5]

カスタムイベントプロパティのネストされたオブジェクトサポートにより、顧客はネストされたイベントプロパティを使用してキャンペーンやキャンバスをトリガーできるようになりました。次の例は、`shopify_created_order`カスタムイベントから特定の製品を使用してキャンペーンをトリガーする例です。アイテムリストをインデックスするために`list_items[].product_id`を使用し、製品IDにアクセスしてください。

![カスタムイベント「shopify_created_order」を実行し、ネストされたプロパティ「product_id」が特定の番号に等しいユーザーに送信されるアクションベースのキャンペーン。][26]

[5]: {% image_buster /assets/img/Shopify/shopify_integration11.png %}
[12]: {% image_buster /assets/img/Shopify/shopify_segmentation2.png %}
[13]: {% image_buster /assets/img/Shopify/shopify_segmentation3.png %}
[14]: {% image_buster /assets/img/Shopify/shopify_segmentation4.png %}
[26]: {% image_buster /assets/img/Shopify/shopify_integration17.png %}
