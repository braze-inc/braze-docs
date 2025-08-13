---
nav_title: BrazeのShopifyデータ
article_title: "BrazeでShopifyのデータを使う"
description: "この参考記事では、BrazeでShopifyのデータをパーソナライズとセグメンテーションのために使用する方法を概説している。"
page_type: partner
search_tag: Partner
alias: "/shopify_data_legacy/"
page_order: 1
---

# BrazeのShopifyデータ

> カスタムイベント用のネストされたオブジェクトサポートを使用して、Braze Shopifyの顧客は、ネストされたイベントプロパティのリキッドテンプレート変数を使用することができる。

アプリのインストールが完了すると、Brazeは自動的にShopifyとのWebhookとScriptTagの統合を作成する。サポートされているShopifyのイベントが、Brazeのカスタムイベントやカスタム属性にどのようにマッピングされるかについては、以下の表を参照のこと。

## Shopifyがサポートするイベント

{% tabs %}
{% tab Shopifyイベント %}
{% subtabs global %}
{% subtab Product Viewed %}
**イベント**： `shopify_product_viewed`<br>
**タイプ**：[カスタムイベント]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)


{% raw %}
| バリアブル｜リキッド・テンプレーティング
| --- | --- |
| アイテムID｜`{{event_properties.${id}}}` ｜
| アイテムタイトル  | `{{event_properties.${title}}}` |
| アイテム価格 | `{{event_properties.${price}}}` |
| アイテムベンダー | `{{event_properties.${vendor}}}` |
| アイテム画像｜`{{event_properties.${images}}}` ｜


{% endraw %}
{% endsubtab %}


{% subtab Product Clicked %}
**イベント**： `shopify_product_clicked`<br>
**タイプ**：[カスタムイベント]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)


{% raw %}
| バリアブル｜リキッド・テンプレーティング
| --- | --- |
| アイテムID｜`{{event_properties.${id}}}` ｜
| アイテムタイトル  | `{{event_properties.${title}}}` |
| アイテム価格 | `{{event_properties.${price}}}` |
| アイテムベンダー | `{{event_properties.${vendor}}}` |
| アイテム画像｜`{{event_properties.${images}}}` ｜
{% endraw %}
{% endsubtab %}


{% subtab Abandoned Cart %}
**イベント**： `shopify_abandoned_cart`<br>
**タイプ**：[カスタムイベント]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)


{% raw %}
| バリアブル｜リキッド・テンプレーティング
| --- | --- |
| カートID｜`{{event_properties.${cart_id}}}` ｜。
| アイテムID｜`{{event_properties.${line_items}[0].product_id}}` ｜
| アイテム数量 | `{{event_properties.${line_items}[0].quantity}}` |
| アイテムSKU｜`{{event_properties.${line_items}[0].sku}}` ｜
| アイテムタイトル | `{{event_properties.${line_items}[0].title}}` |
| アイテムベンダー | `{{event_properties.${line_items}[0].vendor}}` |
| アイテムプロパティ | `{{event_properties.${line_items}[0].properties}}` |
| アイテム価格 | `{{event_properties.${line_items}[0].price}}` |
| バリアント ID | `{{event_properties.${line_items}[0].variant_id}}` |
{% endraw %}
{% endsubtab %}


{% subtab Abandoned Checkout %}
**イベント**： `shopify_abandoned_checkout`<br>
**タイプ**：[カスタムイベント]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)


{% raw %}
| バリアブル｜リキッド・テンプレーティング
| --- | --- |
| チェックアウト ID | `{{event_properties.${checkout_id}}}` |
| 放棄されたカートのURL｜`{{event_properties.${abandoned_checkout_url}}}` ｜
| 割引コード｜`{{event_properties.${discount_code}}}` ｜
| 価格｜総額｜`{{event_properties.${total_price}}}` ｜
| 割引額｜`{{event_properties.${applied_discount}[0].amount}}` ｜
| 割引タイトル | `{{event_properties.${applied_discount}[0].title}}` |
| 割引内容｜`{{event_properties.${applied_discount}[0].description}}` ｜
| アイテムID｜`{{event_properties.${line_items}[0].product_id}}` ｜
| アイテム数量 | `{{event_properties.${line_items}[0].quantity}}` |
| アイテムSKU｜`{{event_properties.${line_items}[0].sku}}` ｜
| アイテムタイトル | `{{event_properties.${line_items}[0].title}}` |
| アイテムベンダー | `{{event_properties.${line_items}[0].vendor}}` |
| アイテムプロパティ | `{{event_properties.${line_items}[0].properties}}` |
| アイテム価格 | `{{event_properties.${line_items}[0].price}}` |
| バリアント ID | `{{event_properties.${line_items}[0].variant_id}}` |
| バリアントタイトル |`{{event_properties.${line_items}[0].variant_title}}` |
{% endraw %}
{% endsubtab %}


{% subtab Created Order %}


**イベント**： `shopify_created_order`<br>
**タイプ**：[カスタムイベント]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)

{% raw %}
| バリアブル｜リキッド・テンプレーティング
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
| バリアント ID | `{{event_properties.${line_items}[0].variant_id}}` |
| バリアントタイトル |`{{event_properties.${line_items}[0].variant_title}}` |
| 配送タイトル | `{{event_properties.${shipping}[0].title}}` |
| 価格｜送料｜`{{event_properties.${shipping}[0].price}}`
|Shopify ストア | `{{event_properties.${shopify_storefront}}}`|
| フルフィルメントステータス | `{{event_properties.${fulfillment_status}}}` |
| 参照元サイト | `{{event_properties.${referring_site}}}` |
| 決済ゲートウェイ名｜`{{event_properties.${payment_gateway_names}}}` ｜
| 発送先住所1行目｜`{{event_properties.${shipping_address[0].address1}}}` ｜
| 発送先住所 2行目｜`{{event_properties.${shipping_address[0].address2}}}` ｜
| 配送先住所 都市名`{{event_properties.${shipping_address[0].city}}}`
| 発送先住所 国｜`{{event_properties.${shipping_address[0].country}}}` ｜
| 発送先住所 姓名`{{event_properties.${shipping_address[0].first_name}}}`
| 発送先住所 姓｜`{{event_properties.${shipping_address[0].last_name}}}` ｜
| 発送先住所 都道府県`{{event_properties.${shipping_address[0].province}}}`
| 発送先住所 郵便番号`{{event_properties.${shipping_address[0].zip}}}`
| 請求先住所行1 | `{{event_properties.${billing_address[0].address1}}}` |
| 請求書送付先住所2行目｜`{{event_properties.${billing_address[0].address2}}}` ｜
| 請求書送付先住所 都市名`{{event_properties.${billing_address[0].city}}}`
| 請求先住所 国名`{{event_properties.${billing_address[0].country}}}`
| 請求先住所 姓名`{{event_properties.${billing_address[0].first_name}}}`
| 請求先住所 姓名`{{event_properties.${shipping_address[0].last_name}}}`
| 請求先住所 都道府県`{{event_properties.${billing_address[0].province}}}`
| 請求先住所 郵便番号`{{event_properties.${billing_address[0].zip}}}`
{% endraw %}


{% endsubtab %}
{% subtab Purchase %}


**イベント**:購入<br>
**タイプ**：[Braze 購入イベント]({{site.baseurl}}/user_guide/data/custom_data/purchase_events/)


{% raw %}
| バリアブル｜リキッド・テンプレーティング
| --- | --- |
| アイテムSKU｜`{{event_properties.${line_items}[0].sku}}` ｜
| アイテムタイトル  | `{{event_properties.${line_items}[0].title}}` |
| アイテムベンダー | `{{event_properties.${line_items}[0].vendor}}` |
| アイテムプロパティ | `{{event_properties.${line_items}[0].properties}}` |
| バリアント ID | `{{event_properties.${line_items}[0].variant_id}}` |
| バリアントタイトル |`{{event_properties.${line_items}[0].variant_title}}` |
{% endraw %}


{% endsubtab %}
{% subtab Paid Order %}
**イベント**： `shopify_paid_order`<br>
**タイプ**：[カスタムイベント]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)


{% raw %}
| バリアブル｜リキッド・テンプレーティング
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
{% endraw %}
{% endsubtab %}


{% subtab Partially Fulfilled Order %}
**イベント**： `shopify_partially_fulfilled_order`<br>
**タイプ**：[カスタムイベント]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)


{% raw %}
| バリアブル｜リキッド・テンプレーティング
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
{% endraw %}
{% endsubtab %}


{% subtab Fulfilled Order %}
**イベント**： `shopify_fulfilled_order`<br>
**タイプ**：[カスタムイベント]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)


{% raw %}
| バリアブル｜リキッド・テンプレーティング
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
{% endraw %}
{% endsubtab %}


{% subtab Cancelled Order %}
**イベント**： `shopify_cancelled_order`<br>
**タイプ**：[カスタムイベント]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)


{% raw %}
| バリアブル｜リキッド・テンプレーティング
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
{% endraw %}
{% endsubtab %}

{% subtab Created Refund %}
**イベント**： `shopify_created_refund`<br>
**タイプ**：[カスタムイベント]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)


{% raw %}
| バリアブル｜リキッド・テンプレーティング
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
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab ペイロードの例 %}
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
{% tabs ローカル %}
{% tab Shopifyカスタム属性 %}
| 属性名 | 説明 |
| --- | --- |
\|`shopify_tags` | ショップオーナーが顧客に付けたタグ。カンマで区切られた値の文字列としてフォーマットされる。顧客には最大250個のタグを付けることができます。各タグの最大文字数は255文字です。 |
| `shopify_total_spent` | 注文履歴全体で顧客が支払った総額。 |
｜`shopify_order_count` ｜この顧客に関連する注文数。テストオーダーとアーカイブオーダーはカウントされない。|
\|`shopify_last_order_id` | 顧客の最後の注文のID。|
\|`shopify_last_order_name` | 顧客の最後の注文の名前。これは、注文リソースの `name` フィールドに直接関係しています。 |
\|`shopify_zipcode` ｜顧客のデフォルト住所の郵便番号。|
| `shopify_province` | 顧客のデフォルトの住所の都道府県。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Liquid のパーソナライゼーション

Shopify カスタム属性に Liquid パーソナライゼーションを追加するには、[**\+ パーソナライゼーション**] を選択します。次に、[パーソナライゼーションタイプ] として [**カスタム属性**] を選択します。

![パーソナライズの追加」セクションの「属性」ドロップダウンが拡張された。]({% image_buster /assets/img/Shopify/add_personalization_2.png %}){: style="max-width:40%;"}

カスタム属性を選択したら、デフォルト値を入力して Liquid スニペットをメッセージにコピーします。

![リキッドのスニペットをメッセージに貼り付ける。]({% image_buster /assets/img/Shopify/copy_liquid_snippet.png %})

#### ペイロードの例

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
{% tab ペイロードの例 %}
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

## セグメンテーション

Shopify のイベントは、セグメンテーションのすべての[既存のカスタムフィルター]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)を使用してフィルタリングできます。 

![Shopify_Test セグメントの詳細ページ。カスタムイベント "shopify_checkouts_abandon" のフィルターがハイライトされている。][12]{: style="max-width:80%;"}

さらに、Braze のさまざまな購入フィルターを利用して、以下を基準にしてセグメントを作成することもできます。
- 最初の購入 / 最後の購入
- 特定のアプリの最初の購入 / 最後の購入
- 過去30日以内に購入した製品
- 購入した製品の数

![2020年10月17日以降に初めて購入したユーザーを対象としたセグメンテーションフィルター。][13]

![セグメンテーション・フィルターとして特定の製品IDを検索する。][14]

{% alert note %}
カスタムイベントプロパティでセグメント化する場合は、カスタマーサクセスマネージャーまたは Braze[サポート]({{site.baseurl}}/braze_support/)と協力して、セグメンテーションと Liquid で使用するすべての関連イベントプロパティのフィルタリングを有効にしてください。
{% endalert %} 

## キャンペーンとキャンバスのトリガー 

Braze の Shopify カスタムイベントを使用することで、他の[カスタムイベント]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-storage)と同様にキャンバスやキャンペーンをトリガーできます。たとえば、キャンバスのエントリ基準内で Shopify `shopify_checkouts_abandon` イベントをトリガーするアクションベースのキャンバスを作成できます。 

![カスタムイベント "shopify_checkouts_abandon "を実行したユーザーを入力するアクションベースのキャンバス。][5]

カスタムイベントプロパティのネストされたオブジェクトのサポートを使用すると、顧客がネストされたイベントプロパティを使用してキャンペーンとキャンバスをトリガーできます。以下は、`shopify_created_order` カスタムイベントから特定の商品を使用してキャンペーンをトリガーする例である。`list_items[0].product_id` を使用してアイテムリストのインデックスを作成し、製品 ID にアクセスするようにしてください。

![カスタムイベント "shopify_created_order "を実行し、ネストされたプロパティ "product_id "が特定の数字と等しいユーザーに送信するアクションベースのキャンペーン。][26]

[5]: {% image_buster /assets/img/Shopify/shopify_integration11.png %}
[12]: {% image_buster /assets/img/Shopify/shopify_segmentation2.png %}
[13]: {% image_buster /assets/img/Shopify/shopify_segmentation3.png %}
[14]: {% image_buster /assets/img/Shopify/shopify_segmentation4.png %}
[26]: {% image_buster /assets/img/Shopify/shopify_integration17.png %}
