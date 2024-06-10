---
nav_title: Braze の Shopify データ
article_title: "BrazeでShopifyデータを使用する"
description: "このリファレンス記事では、Braze で Shopify データを使用してパーソナライゼーションとセグメンテーションを行う方法について説明します。"
page_type: partner
search_tag: Partner
alias: "/shopify_data/"
page_order: 1
---

# Braze の Shopify データ

> カスタム イベントのネストされたオブジェクトのサポートを使用すると、Braze Shopify の顧客はネストされたイベント プロパティの Liquid テンプレート変数を使用できます。

アプリのインストールが完了すると、Braze は Shopify との Webhook と ScriptTag の統合を自動的に作成します。サポートされている Shopify イベントが Braze カスタム イベントおよびカスタム属性にどのようにマッピングされるかの詳細については、次の表を参照してください。

## サポートされているShopifyイベント

{% tabs %}
{% tab Shopify Events %}
{% subtabs global %}
{% subtab Product Viewed %}
イベント<br>
** =  ( タイプ)[カスタムイベント]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)


{% raw %}
| 変数 | リキッドテンプレート |
| --- | --- |
| アイテムID | `{{event_properties.${id}}}`|
| アイテムタイトル | `{{event_properties.${title}}}`|
| 商品価格 | `{{event_properties.${price}}}`|
| アイテムベンダー | `{{event_properties.${vendor}}}`|
| 商品画像 | `{{event_properties.${images}}}`|


{% endraw %}
{% endsubtab %}


{% subtab Product Clicked %}
イベント<br>
** =  ( タイプ)[カスタムイベント]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)


{% raw %}
| 変数 | リキッドテンプレート |
| --- | --- |
| アイテムID | `{{event_properties.${id}}}`|
| アイテムタイトル | `{{event_properties.${title}}}`|
| 商品価格 | `{{event_properties.${price}}}`|
| アイテムベンダー | `{{event_properties.${vendor}}}`|
| 商品画像 | `{{event_properties.${images}}}`|
{% endraw %}
{% endsubtab %}


{% subtab Abandoned Cart %}
イベント<br>
** =  ( タイプ)[カスタムイベント]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)


{% raw %}
| 変数 | リキッドテンプレート |
| --- | --- |
| アイテムID | `{{event_properties.${line_items}[0].product_id}}`|
| 商品の数量 | `{{event_properties.${line_items}[0].quantity}}`|
| 商品SKU | `{{event_properties.${line_items}[0].sku}}`|
| アイテムタイトル | `{{event_properties.${line_items}[0].title}}`|
| アイテムベンダー | `{{event_properties.${line_items}[0].vendor}}`|
| アイテムのプロパティ | `{{event_properties.${line_items}[0].properties}}`|
| 商品価格 | `{{event_properties.${line_items}[0].price}}`|
| バリアント ID | `{{event_properties.${line_items}[0].variant_id}}`|
{% endraw %}
{% endsubtab %}


{% subtab Abandoned Checkout %}
イベント<br>
**タイプ**:[カスタムイベント]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)


{% raw %}
| 変数 | リキッドテンプレート |
| --- | --- |
| チェックアウト ID | `{{event_properties.${checkout_id}}}`|
| 放棄されたカードの URL | `{{event_properties.${abandoned_checkout_url}}}`|
| 割引コード | `{{event_properties.${discount_code}}}`|
| 合計金額 | `{{event_properties.${total_price}}}`|
| 割引額 | `{{event_properties.${applied_discount}[0].amount}}`|
| 割引タイトル | `{{event_properties.${applied_discount}[0].title}}`|
| 割引の説明 | `{{event_properties.${applied_discount}[0].description}}`|
| アイテムID | `{{event_properties.${line_items}[0].product_id}}`|
| 商品の数量 | `{{event_properties.${line_items}[0].quantity}}`|
| 商品SKU | `{{event_properties.${line_items}[0].sku}}`|
| アイテムタイトル | `{{event_properties.${line_items}[0].title}}`|
| アイテムベンダー | `{{event_properties.${line_items}[0].vendor}}`|
| アイテムのプロパティ | `{{event_properties.${line_items}[0].properties}}`|
| 商品価格 | `{{event_properties.${line_items}[0].price}}`|
| バリアント ID | `{{event_properties.${line_items}[0].variant_id}}`|
| バリアントタイトル | `{{event_properties.${line_items}[0].variant_title}}`|
{% endraw %}
{% endsubtab %}


{% subtab Created Order %}


イベント<br>
**タイプ**:[カスタムイベント]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)

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
| 変数 | リキッドテンプレート |
| --- | --- |
| 注文ID | `{{event_properties.${order_id}}}`|
| 確認済みステータス | `{{event_properties.${confirmed}}}`|
| 注文状況 URL | `{{event_properties.${order_status_url}}}`|
| 注文番号 | `{{event_properties.${order_number}}}`|
| キャンセルされたタイムスタンプ | `{{event_properties.${cancelled_at}}}`|
| 合計割引 | `{{event_properties.${total_discounts}}}`|
| 合計金額 | `{{event_properties.${total_price}}}`|
タグ:
| 割引コード | `{{event_properties.${discount_codes}}}`|
| アイテムID | `{{event_properties.${line_items}[0].product_id}}`|
| 商品の数量 | `{{event_properties.${line_items}[0].quantity}}`|
| 商品SKU | `{{event_properties.${line_items}[0].sku}}`|
| アイテムタイトル | `{{event_properties.${line_items}[0].title}}`|
| アイテムベンダー | `{{event_properties.${line_items}[0].vendor}}`|
| アイテムのプロパティ | `{{event_properties.${line_items}[0].properties}}`|
| 商品価格 | `{{event_properties.${line_items}[0].price}}`|
| バリアント ID | `{{event_properties.${line_items}[0].variant_id}}`|
| バリアントタイトル | `{{event_properties.${line_items}[0].variant_title}}`|
| 配送タイトル | `{{event_properties.${shipping}[0].title}}`|
| 配送料金 | `{{event_properties.${shipping}[0].price}}`|
Shopify ストア
| 履行状況 | `{{event_properties.${fulfillment_status}}}`|
| 参照サイト | `{{event_properties.${referring_site}}}`|
| 決済ゲートウェイ名 | `{{event_properties.${payment_gateway_names}}}`|
| 配送先住所 1 行目 | `{{event_properties.${shipping_address[0].address1}}}`|
| 配送先住所 2 行目 | `{{event_properties.${shipping_address[0].address2}}}`|
| 配送先住所市区町村 | `{{event_properties.${shipping_address[0].city}}}`|
| 配送先住所の国 | `{{event_properties.${shipping_address[0].country}}}`|
| 配送先住所 名 | `{{event_properties.${shipping_address[0].first_name}}}`|
| 配送先住所 姓 | `{{event_properties.${shipping_address[0].last_name}}}`|
| 配送先住所の都道府県 | `{{event_properties.${shipping_address[0].province}}}`|
| 発送先住所 郵便番号 | `{{event_properties.${shipping_address[0].zip}}}`|
| 請求先住所 1 行目 | `{{event_properties.${billing_address[0].address1}}}`|
| 請求先住所 2 行目 | `{{event_properties.${billing_address[0].address2}}}`|
| 請求先住所市区町村 | `{{event_properties.${billing_address[0].city}}}`|
| 請求先住所の国 | `{{event_properties.${billing_address[0].country}}}`|
| 請求先住所 名 | `{{event_properties.${billing_address[0].first_name}}}`|
| 請求先住所 姓 | `{{event_properties.${shipping_address[0].last_name}}}`|
| 請求先住所の都道府県 | `{{event_properties.${billing_address[0].province}}}`|
| 請求先住所 郵便番号 | `{{event_properties.${billing_address[0].zip}}}`|
{% endraw %}


{% endsubtab %}
{% subtab Purchase %}


**イベント**:購入<br>
**タイプ**:[Braze 購入イベント]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events/)


{% raw %}
| 変数 | リキッドテンプレート |
| --- | --- |
| 商品SKU | `{{event_properties.${line_items}[0].sku}}`|
| アイテムタイトル | `{{event_properties.${line_items}[0].title}}`|
| アイテムベンダー | `{{event_properties.${line_items}[0].vendor}}`|
| アイテムのプロパティ | `{{event_properties.${line_items}[0].properties}}`|
| バリアント ID | `{{event_properties.${line_items}[0].variant_id}}`|
| バリアントタイトル | `{{event_properties.${line_items}[0].variant_title}}`|
{% endraw %}


{% endsubtab %}
{% subtab Paid Order %}
**イベント**: `shopify_paid_order`<br>
**タイプ**:[カスタムイベント]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)


{% raw %}
| 変数 | リキッドテンプレート |
| --- | --- |
| 注文ID | `{{event_properties.${order_id}}}`|
| 確認済みステータス | `{{event_properties.${confirmed}}}`|
| 注文状況 URL | `{{event_properties.${order_status_url}}}`|
| 注文番号 | `{{event_properties.${order_number}}}`|
| キャンセルされたタイムスタンプ | `{{event_properties.${cancelled_at}}}`|
| 合計割引 | `{{event_properties.${total_discounts}}}`|
| 合計金額 | `{{event_properties.${total_price}}}`|
| タグ: | `{{event_properties.${tags}}}` |
| 割引コード | `{{event_properties.${discount_codes}}}`|
| アイテムID | `{{event_properties.${line_items}[0].product_id}}`|
| 商品の数量 | `{{event_properties.${line_items}[0].quantity}}`|
| 商品SKU | `{{event_properties.${line_items}[0].sku}}`|
| アイテムタイトル | `{{event_properties.${line_items}[0].title}}`|
| アイテムベンダー | `{{event_properties.${line_items}[0].vendor}}`|
| アイテムのプロパティ | `{{event_properties.${line_items}[0].properties}}`|
| 商品価格 | `{{event_properties.${line_items}[0].price}}`|
| 配送タイトル | `{{event_properties.${shipping}[0].title}}`|
| 配送料金 | `{{event_properties.${shipping}[0].price}}`|
| バリアント ID | `{{event_properties.${line_items}[0].variant_id}}`|
| バリアントタイトル | `{{event_properties.${line_items}[0].variant_title}}`|
{% endraw %}
{% endsubtab %}


{% subtab Partially Fulfilled Order %}
**イベント**: `shopify_partially_fulfilled_order`<br>
**タイプ**:[カスタムイベント]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)


{% raw %}
| 変数 | リキッドテンプレート |
| --- | --- |
| 注文ID | `{{event_properties.${order_id}}}`|
| 合計金額 | `{{event_properties.${total_price}}}`|
| 合計割引 | `{{event_properties.${total_discounts}}}`|
| 確認済みステータス | `{{event_properties.${confirmed}}}`|
| 注文状況 URL | `{{event_properties.${order_status_url}}}`|
| 注文番号 | `{{event_properties.${order_number}}}`|
| キャンセルされたタイムスタンプ | `{{event_properties.${cancelled_at}}}`|
| クローズタイムスタンプ | `{{event_properties.${closed_at}}}`|
| アイテムID | `{{event_properties.${line_items}[0].product_id}}`|
| 商品の数量 | `{{event_properties.${line_items}[0].quantity}}`|
| 商品SKU | `{{event_properties.${line_items}[0].sku}}`|
| アイテムタイトル | `{{event_properties.${line_items}[0].title}}`|
| アイテムベンダー | `{{event_properties.${line_items}[0].vendor}}`|
| アイテム名 | `{{event_properties.${line_items}[0].name}}`|
| アイテムのプロパティ | `{{event_properties.${line_items}[0].properties}}`|
| 商品価格 | `{{event_properties.${line_items}[0].price}}`|
| 配送タイトル | `{{event_properties.${shipping}[0].title}}`|
| 配送料金 | `{{event_properties.${shipping}[0].price}}`|
| 履行状況 | `{{event_properties.${fulfillment_status}}}`|
| フルフィルメント出荷ステータス | `{{event_properties.${fulfillments}[0].shipment_status}}`|
| 履行状況 | `{{event_properties.${fulfillments}[0].status}}`|
| フルフィルメント追跡会社 | `{{event_properties.${fulfillments}[0].tracking_company}}`|
| フルフィルメント追跡番号 | `{{event_properties.${fulfillments}[0].tracking_number}}`|
| フルフィルメント追跡番号 | `{{event_properties.${fulfillments}[0].tracking_numbers}}`|
| フルフィルメント追跡 URL | `{{event_properties.${fulfillments}[0].tracking_url}}`|
| フルフィルメント追跡 URL | `{{event_properties.${fulfillments}[0].tracking_urls}}`|
| 履行状況 | `{{event_properties.${fulfillments}[0].line_items[0].fulfillment_status}}`|
| フルフィルメント名 | `{{event_properties.${fulfillments}[0].line_items[0].name}}`|
| 履行価格 | `{{event_properties.${fulfillments}[0].line_items[0].price}}`|
| フルフィルメント製品 ID | `{{event_properties.${fulfillments}[0].line_items[0].product_id}}`|
| 履行数量 | `{{event_properties.${fulfillments}[0].line_items[0].quantity}}`|
| フルフィルメント配送 | `{{event_properties.${fulfillments}[0].line_items[0].requires_shipping}}`|
| フルフィルメント SKU | `{{event_properties.${fulfillments}[0].line_items[0].sku}}`|
| 履行タイトル | `{{event_properties.${fulfillments}[0].line_items[0].title}}`|
| フルフィルメントベンダー | `{{event_properties.${fulfillments}[0].line_items[0].vendor`|
| バリアント ID | `{{event_properties.${line_items}[0].variant_id}}`|
| バリアントタイトル | `{{event_properties.${line_items}[0].variant_title}}`|
{% endraw %}
{% endsubtab %}


{% subtab Fulfilled Order %}
**イベント**: `shopify_fulfilled_order`<br>
**タイプ**:[カスタムイベント]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)


{% raw %}
| 変数 | リキッドテンプレート |
| --- | --- |
| 注文ID | `{{event_properties.${order_id}}}`|
| 合計金額 | `{{event_properties.${total_price}}}`|
| 合計割引 | `{{event_properties.${total_discounts}}}`|
| 確認済みステータス | `{{event_properties.${confirmed}}}`|
| 注文状況 URL | `{{event_properties.${order_status_url}}}`|
| 注文番号 | `{{event_properties.${order_number}}}`|
| キャンセルされたタイムスタンプ | `{{event_properties.${cancelled_at}}}`|
| クローズタイムスタンプ | `{{event_properties.${closed_at}}}`|
| アイテムID | `{{event_properties.${line_items}[0].product_id}}`|
| 商品の数量 | `{{event_properties.${line_items}[0].quantity}}`|
| 商品SKU | `{{event_properties.${line_items}[0].sku}}`|
| アイテムタイトル | `{{event_properties.${line_items}[0].title}}`|
| アイテムベンダー | `{{event_properties.${line_items}[0].vendor}}`|
| アイテム名 | `{{event_properties.${line_items}[0].name}}`|
| アイテムのプロパティ | `{{event_properties.${line_items}[0].properties}}`|
| 商品価格 | `{{event_properties.${line_items}[0].price}}`|
| 配送タイトル | `{{event_properties.${shipping}[0].title}}`|
| 配送料金 | `{{event_properties.${shipping}[0].price}}`|
| 履行状況 | `{{event_properties.${fulfillment_status}}}`|
| フルフィルメント出荷ステータス | `{{event_properties.${fulfillments}[0].shipment_status}}`|
| ステータス| `{{event_properties.${fulfillments}[0].status}}` |
| フルフィルメント追跡会社 | `{{event_properties.${fulfillments}[0].Fulfillment tracking_company}}`|
| フルフィルメント追跡番号 | `{{event_properties.${fulfillments}[0].Fulfillment tracking_number}}`|
| フルフィルメント追跡番号 | `{{event_properties.${fulfillments}[0].Fulfillment tracking_numbers}}`|
| フルフィルメント追跡 URL | `{{event_properties.${fulfillments}[0].Fulfillment tracking_url}}`|
| フルフィルメント追跡 URL | `{{event_properties.${fulfillments}[0].Fulfillment tracking_urls}}`|
| 履行状況 | `{{event_properties.${fulfillments}[0].line_items[0].fulfillment_status}}`|
| フルフィルメント名 | `{{event_properties.${fulfillments}[0].line_items[0].name}}`|
| 履行価格 | `{{event_properties.${fulfillments}[0].line_items[0].price}}`|
| フルフィルメント製品 ID | `{{event_properties.${fulfillments}[0].line_items[0].product_id}}`|
| 履行数量 | `{{event_properties.${fulfillments}[0].line_items[0].quantity}}`|
| フルフィルメント配送 | `{{event_properties.${fulfillments}[0].line_items[0].requires_shipping}}`|
| フルフィルメント SKU | `{{event_properties.${fulfillments}[0].line_items[0].sku}}`|
| 履行タイトル | `{{event_properties.${fulfillments}[0].line_items[0].title}}`|
| フルフィルメントベンダー | `{{event_properties.${fulfillments}[0].line_items[0].vendor`|
| バリアント ID | `{{event_properties.${line_items}[0].variant_id}}`|
| バリアントタイトル | `{{event_properties.${line_items}[0].variant_title}}`|
{% endraw %}
{% endsubtab %}


{% subtab Cancelled Order %}
**イベント**: `shopify_cancelled_order`<br>
**タイプ**:[カスタムイベント]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)


{% raw %}
| 変数 | リキッドテンプレート |
| --- | --- |
| 注文ID | `{{event_properties.${order_id}}}`|
| 合計金額 | `{{event_properties.${total_price}}}`|
| 合計割引 | `{{event_properties.${total_discounts}}}`|
| 確認済み | `{{event_properties.${confirmed}}}`|
| 注文状況 URL | `{{event_properties.${order_status_url}}}`|
| 注文番号 | `{{event_properties.${order_number}}}`|
| キャンセルされたタイムスタンプ | `{{event_properties.${cancelled_at}}}`|
| タグ: | `{{event_properties.${tags}}}` |
| 割引コード | `{{event_properties.${discount_codes}}}`|
| 履行状況 | `{{event_properties.${fulfillment_status}}}`|
| フルフィルメント | `{{event_properties.${fulfillments}}}`|
| アイテムID | `{{event_properties.${line_items}[0].product_id}}`|
| 商品の数量 | `{{event_properties.${line_items}[0].quantity}}`|
| 商品SKU | `{{event_properties.${line_items}[0].sku}}`|
| アイテムタイトル | `{{event_properties.${line_items}[0].title}}`|
| アイテムベンダー | `{{event_properties.${line_items}[0].vendor}}`|
| アイテム名 | `{{event_properties.${line_items}[0].name}}`|
| アイテムのプロパティ | `{{event_properties.${line_items}[0].properties}}`|
| 履行状況 | `{{event_properties.${line_items}[0].fulfillment_status}}`|
| 配送タイトル | `{{event_properties.${shipping}[0].title}}`|
| 配送料金 | `{{event_properties.${shipping}[0].price}}`|
| バリアント ID | `{{event_properties.${line_items}[0].variant_id}}`|
| バリアントタイトル | `{{event_properties.${line_items}[0].variant_title}}`|
{% endraw %}
{% endsubtab %}

{% subtab Created Refund %}
**イベント**: `shopify_created_refund`<br>
**タイプ**:[カスタムイベント]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)


{% raw %}
| 変数 | リキッドテンプレート |
| --- | --- |
| 注文ID | `{{event_properties.${order_id}}}`|
| 注文メモ | `{event_properties.${note}}}`|
| アイテムID | `{{event_properties.${line_items}[0].product_id}}`|
| 商品の数量 | `{{event_properties.${line_items}[0].quantity}}`|
| 商品SKU | `{{event_properties.${line_items}[0].sku}}`|
| アイテムタイトル | `{{event_properties.${line_items}[0].title}}`|
| アイテムベンダー | `{{event_properties.${line_items}[0].vendor}}`|
| アイテム名 | `{{event_properties.${line_items}[0].name}}`|
| アイテムのプロパティ | `{{event_properties.${line_items}[0].properties}}`|
| 商品価格 | `{{event_properties.${line_items}[0].price}}`|
| バリアント ID | `{{event_properties.${line_items}[0].variant_id}}`|
| バリアントタイトル | `{{event_properties.${line_items}[0].variant_title}}`|
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
\`\`json
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
        
   
   "braze\_id":「63497b3ca3eabd0053380451」
     

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
 "ディスカウントコード"：「30\_DOLLARS\_OFF」、
 "合計金額"："398.00",
 "line\_items": [
        {
   "price": "199.00",
   "properties": {},      
        PRODUCT\_ID632910392、
            数量1,
            「SKU」:「IPOD2008ピンク」、
          役職: 「iPodNano-8GB」、
          「バリアントID」:40094740545625,
          「バリアントタイトル」:「ピンクの iPod Nano 8 GB」、
          "ベンダー"："りんご"、
        
      
 "abandoned\_checkout\_url": "https://checkout.local/690933842/checkouts/123123123/recover?key=example-secret-token",
「チェックアウトID」:「123123123」


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
   
   「注文ID」:820982911946154500,
   「確認済み」: 偽、
   "order\_status\_url": "https://apple.myshopify.com/690933842/orders/123456abcd/authenticate?key=abcdefg",
     "注文番号"：2.3.
       「キャンセル日時」:「2020-09-10T18:53:45-04:00」、
       "shipping": [
            {
       "title": "Standard",
       "price": "10.00"
     },
            {
       "title": "Expedited",
       "price": "25.00"
     }
          
       「タグ」：「重い」
       
       
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
       
       "shipping": [
            {
       "title": "Standard",
       "price": "0.00"
     }
          
     "合計金額"：2.3.
   「確認済み」：true、
   「合計割引」:2.3.
   "discount\_codes": [],
   "注文番号"：2.3.
   "order\_status\_url": "https://test-store.myshopify.com/",
   "cancelled\_at": null、
   タグ:
   "closed\_at": null、
 "fulfillment\_status": "一部",
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
 
 
 
 "braze\_id": "abc123abc123"
 
 ```
{% endsubtab %}
{% subtab Fulfilled Order %}
```json
 {
   "名前": "shopify\_fulfilled\_order",
   時刻「2022-05-23T14:44:34-04:00」、
   "properties": {
   「注文ID」:4444668657855、
   "line\_items": [
   {
 数量1,
PRODUCT\_ID6143032066239、
"SKU": null、
役職: 「ダークデニムトップ」、
 「バリアントID」:40094740549876、
 「バリアントタイトル」:「スモールダークデニムトップ」


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
      
   "合計金額"：2.3.
   「確認済み」：true、
   「合計割引」:2.3.
   "discount\_codes": [],
   "注文番号"：2.3.
   "order\_status\_url": "https://test-store.myshopify.com/",
   "cancelled\_at": null、
   タグ:
   「閉店時間」:「2022-05-23T14:44:34-04:00」、
     "fulfillment\_status": "履行済み",
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
       
       
       
       "braze\_id":「123abc123abc」
       
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
 
 "shipping": [
     {
       "title": "Standard",
       "price": "0.00"
     }
   
"合計金額"：2.3.
 「確認済み」：true、
 「合計割引」:2.3.
 "discount\_codes": [],
   "注文番号"：2.3.
   "order\_status\_url": "https://test-store.myshopify.com/",
     「キャンセル日時」:「2022-05-23T14:40:52-04:00」、
       タグ:
       「閉店時間」:「2022-05-23T14:40:51-04:00」、
       「履行ステータス」: null、
       "fulfillments": []
       
       "braze\_id":「123abc123abc」
       
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
       
     
   "braze\_id": "abc123abc123"
   
   \`\`\`
   {% endsubtab %}
   {% endsubtabs %}
   {% endtab %}
   {% endtabs %}

## サポートされているShopifyカスタム属性
{% tabs local %}
{% tab Shopify Custom Attributes %}
| 属性名 | 説明 |
| --- | --- |
| `shopify_tags`| ショップオーナーが顧客に付けたタグ。コンマ区切りの値の文字列としてフォーマットされます。顧客は最大 250 個のタグを持つことができます。各タグには最大 255 文字を使用できます。 |
| `shopify_total_spent`| 顧客が注文履歴を通じて支払った合計金額。 |
| `shopify_order_count`| この顧客に関連付けられている注文の数。テスト注文とアーカイブ注文はカウントされません。 |
| `shopify_last_order_id`| 顧客の最終注文の ID。 |
| `shopify_last_order_name`| 顧客の最後の注文の名前。これは直接的に `name` 注文リソースのフィールド。 |
| `shopify_zipcode`| 顧客のデフォルト住所の郵便番号。 |
| `shopify_province`| 顧客のデフォルト住所からの都道府県。 |
{: .reset-td-br-1 .reset-td-br-2}

### Liquid のパーソナライゼーション

Shopify カスタム属性に Liquid パーソナライゼーションを追加するには、**[+ パーソナライゼーション]**を選択します。次に、パーソナライズタイプとして **「カスタム属性」** を選択します。

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

## サポートされているShopify標準属性

- メールアドレス
- 名
- 姓
- 電話
- 市区町村
- 国

{% alert note %}
Braze は、既存のユーザー プロファイルのデータに差異がある場合にのみ、サポートされている Shopify カスタム属性と Braze 標準属性を更新します。たとえば、受信 Shopify データに Bob という名前が含まれており、Bob がすでに Braze ユーザー プロファイルに名前として存在する場合、Braze は更新をトリガーせず、データ ポイントは課金されません。
{% endalert %}

## セグメンテーション

セグメンテーションの [既存のカスタム フィルター]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) すべてを使用して、Shopify のイベントをフィルターできます。 

![Shopify\_Test セグメントのセグメント詳細ページで、カスタム イベント「shopify\_checkouts\_abandon」のフィルターが強調表示されています。][12]{: style="max-width:80%;"}

さらに、Braze の幅広い購入フィルターを使用して、次の基準に基づいてユーザーのセグメントを作成することもできます。
まず、/last purchase
- First/last purchase for a specific app
\- 過去30日以内に購入した商品
\- 購入した回数

![2020年10月17日以降に初めて購入したユーザー向けのセグメンテーションフィルター。][13]

![セグメンテーションフィルターとして特定の商品IDを検索します。][14]

{% alert note %}
カスタム イベント プロパティでセグメント化する場合は、カスタマー サクセス マネージャーまたは Braze [サポート]({{site.baseurl}}/braze_support/) と連携して、セグメンテーションと Liquid 内で使用するすべての関連イベント プロパティのフィルタリングを有効にしてください。
{% endalert %} 

## キャンペーンとキャンバスのトリガー 

Braze の Shopify カスタム イベントを使用すると、他の [カスタム イベント]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-storage)と同じようにキャンバスやキャンペーンをトリガーできます。例えば、Shopifyからトリガーされるアクションベースのキャンバスを作成することができます。 `shopify_checkouts_abandon`Canvas のエントリー基準内でのイベント。 

![カスタムイベント「shopify\_checkouts\_abandon」を実行するユーザーを入力するアクションベースのキャンバス。][5]

カスタム イベント プロパティのネストされたオブジェクトのサポートにより、顧客はネストされたイベント プロパティを使用してキャンペーンやキャンバスをトリガーできるようになりました。以下は、特定の商品を使用してキャンペーンをトリガーする例です。 `shopify_created_order` カスタムイベント。必ず使用してください `list_items[].product_id` アイテムリストをインデックス化し、製品 ID にアクセスします。

![ネストされたプロパティ「product\_id」が特定の番号に等しいカスタムイベント「shopify\_created\_order」を実行するユーザーに送信するアクションベースのキャンペーン。][26]

[5]: {% image_buster /assets/img/Shopify/shopify_integration11.png %}
[12]: {% image_buster /assets/img/Shopify/shopify_segmentation2.png %}
[13]: {% image_buster /assets/img/Shopify/shopify_segmentation3.png %}
[14]: {% image_buster /assets/img/Shopify/shopify_segmentation4.png %}
[26]: {% image_buster /assets/img/Shopify/shopify_integration17.png %}
