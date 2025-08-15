---
nav_title: e コマースのおすすめイベント
article_title: e コマースのおすすめイベント
page_type: reference
alias: /ecommerce_events/
toc_headers: h2
description: "この参考記事では、eコマース推奨のイベントとプロパティ、その使用方法、セグメンテーション、関連する分析を表示する場所などについて説明している。"
---

# e コマースの推奨イベント

> このページでは、e コマース推奨のイベントとプロパティについて説明します。これらのイベントは、マーケターが効果的なメッセージング (カート放棄のターゲット設定など) をトリガーするために必要な主な購入行動をキャプチャする貯めに作成されます。

Braze は、データプランニングには時間がかかることを認識しています。お客様の開発チームに周知し、このイベント微送信を今すぐ開始することををお勧めします。eコマース推奨イベントですぐに利用できない機能もあるかもしれないが、eコマース機能を強化する新製品の登場を2025年中に期待できる。

{% alert important %}
e コマースの推奨イベントは現在、早期アクセス段階です。早期アクセスに参加したい場合は、Braze カスタマーサクセスマネージャーにお問い合わせください。<br><br>新しい[Shopifyコネクタを]({{site.baseurl}}/partners/ecommerce/shopify/multiple_stores/?tab=shopify%20connector)活用している場合、これらの推奨イベントは統合によって自動的に利用できるようになる。
{% endalert %}


## e コマースの推奨イベントのタイプ

{% tabs %}
{% tab ecommerce.product_viewed %}

顧客が商品詳細ページを閲覧する時点でトリガーされる製品閲覧イベントを使用できます。

#### プロパティ

| プロパティ名 | required | データタイプ | 説明 | 
|---|---|---|---|
| `product_id` | はい | string | 閲覧された製品の一意の識別子。<br> Shopify以外の顧客の場合、これはSKUのようなカタログアイテムIDに設定した値になる。 |
| `product_name` | はい | string | 閲覧された商品名。 | 
| `variant_id` | はい | string | 製品バリアントに固有の識別子。例は`shirt_medium_blue`です |
| `image_url` | いいえ | string | 商品画像のURL。 |
| `product_url` | いいえ | string | 詳細情報がある製品ページの URL。 |
| `price` | はい | フロート | 閲覧時の製品のバリアント単価。 |
| `currency` | はい | string | 製品価格の表示通貨 (「USD」や「EUR」など)。[ISO 4217 フォーマット](https://www.iso.org/iso-4217-currency-codes.html)です。 |
| `source` | はい | string | イベントの派生元ソース。(Shopify の場合これはストアフロントです。) |
| `metadata` | いいえ | オブジェクト | |
| `sku` | いいえ | string | (Shopifyのみ）Shopify SKU.これはカタログ ID フィールドとして設定できます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### オブジェクトの例

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
{% tab ecommerce.cart_updated %}

カートに製品が追加された時点、削除された時点、更新された時点を追跡するには、カードの更新イベントを使用できます。`ecommerce.cart_updated` イベントはトリガー前に以下の情報を検証します。

- イベントの時刻が、ユーザーの特定のカートの`updated_at` の時刻よりも後である。
- カートが購入手続きに進んでいない。
- `products` の配列が空ではない。

#### カートマッピングオブジェクト

`ecommerce.cart_updated` イベントにはカートマッピングオブジェクトがあります。このオブジェクトは、カートのマッピングを含むユーザープロファイルに対して作成されます。購入者のカートに入っているすべての製品が含まれています。Liquid タグを使用してショッピングカート内の製品にアクセスできます。 

{%raw%}
```liquid
{% shopping_cart {{context_properties.${cart_id}}} %}
{% for item in shopping_cart.products %}
{% catalog_items <add_your_catalog> {{item.variant_id}} %}
```
{%endraw%}

10日以内にカートが更新されず、注文イベントに進まなかった場合、カートと関連製品は削除されます。

{% alert note %}
Braze ではカートあたりの製品の数に制限はありません。ただし Shopify での上限は500です。
{% endalert %}

#### ユーザープロファイルをマージする際のカートの動作

カートが2つある場合は、この両方がマージユーザーに追加されます。同じカートまたは異なるカートが最新のカート情報を含むメッセージを送信する場合、キャンバスを再度キューに入れます。`ecommerce.cart_updated` イベントには、最新のカート ID とカート内の最新の商品が含まれます。

#### プロパティ

| プロパティ名 | required | データタイプ | 説明 | 
|---|---|---|---|
| `cart_id` | はい | string | カートの一意の識別子。値が渡されない場合、Braze によりユーザーカートマッピングのデフォルト値 (カート、チェックアウト、注文イベントで共有) が決定します。 |
| `total_value` | はい | フロート | カートの合計金額。 | 
| `currency` | はい | string | 製品価格の表示通貨 (「USD」や「EUR」など)。[ISO 4217 フォーマット](https://www.iso.org/iso-4217-currency-codes.html)です。 |
| `products` | はい | 配列 |  |
| `product_id` | はい | string | 閲覧された製品の一意の識別子。<br> この値には、製品 ID または SKU を使用できます。 |
| `product_name` | はい | string | 閲覧された商品名。 |
| `variant_id` | はい | string | 製品バリアントに固有の識別子。例は`shirt_medium_blue`です |
| `image_url` | いいえ | string | 商品画像のURL。 |
| `product_url` | いいえ | string | 詳細情報がある製品ページの URL。 |
| `quantity` | はい | 整数 | カートに入っている製品の個数。 |
| `price` | はい | フロート | 閲覧時の製品のバリアント単価。 |
| `metadata` | いいえ | オブジェクト | 顧客がユースケースのために追加する製品に関する追加のメタデータフィールド。Shopify の場合は SKU が追加されます。<br> 一般的なイベントプロパティの上限である50kb に基づく制限があります。 |
| `sku` | いいえ | string | (Shopifyのみ）Shopify SKU.これはカタログ ID フィールドとして設定できます。 |
| `source` | はい | string | イベントの派生元ソース。(Shopify の場合これはストアフロントです。) |
| `metadata` | いいえ | オブジェクト | 顧客がユースケースのために追加する製品に関する追加のメタデータフィールド。Shopify の場合は SKU が追加されます。<br> 一般的なイベントプロパティの上限である50kb に基づく制限があります。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### オブジェクトの例

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

チェックアウト開始イベントを使用して、チェックアウトプロセスを開始したが発注していない顧客をリターゲティングできます。

`ecommerce.cart_updated` イベントと同様に、このイベントでは、ショッピングカート Liquid タグを使用して、購入手続き放棄メッセージのためにカート内のすべての製品にアクセスできます。

{%raw%}
```liquid
{% shopping_cart {{context_properties.${cart_id}}} :abort_if_not_abandoned false %}
{% for item in shopping_cart.products %}
{% catalog_items <add_your_catalog> {{item.variant_id}} %}
```
{%endraw%}

#### プロパティ

| プロパティ名 | required | データタイプ | 説明 | 
|---|---|---|---|
| `checkout_id` | はい | string | チェックアウトの一意の識別子。 |
| `cart_id` | いいえ | string | カートの一意の識別子。値が渡されない場合、Braze によりユーザーカートマッピングのデフォルト値 (カート、チェックアウト、注文イベントで共有) が決定します。 | 
| `total_value` | はい | フロート | カートの合計金額。 |
| `currency` | はい | string | カートの金額の通貨。 |
| `products` | はい | オブジェクト配列 |  |
| `product_id` | はい | string | 閲覧された製品の一意の識別子。例えば製品 ID や SKU がこの値になります。 |
| `product_name` | はい | string | 閲覧された商品名。  |
| `variant_id` | はい | string | 製品バリアントに固有の識別子。例は`shirt_medium_blue`です |
| `image_url` | いいえ | string | 商品画像のURL。 |
| `product_url` | いいえ | string | 詳細情報がある製品ページの URL。 |
| `quantity` | はい | 整数 | カートに入っている製品の個数。 |
| `price` | はい | フロート | 閲覧時の製品のバリアント単価。 |
| `metadata` | いいえ | オブジェクト | 顧客がユースケースのために追加する製品に関する追加のメタデータフィールド。Shopify の場合は SKU が追加されます。<br> 一般的なイベントプロパティの上限である50kb に基づく制限があります。 |
| `sku` | いいえ | string | (Shopifyのみ）Shopify SKU.これはカタログ ID フィールドとして設定できます。 |
| `source` | はい | string | イベントの派生元ソース。(Shopify の場合これはストアフロントです。) |
| `metadata` | いいえ | オブジェクト |  |
| `checkout_url` | いいえ | string | チェックアウトページのURL。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### オブジェクトの例

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
{% tab ecommerce.order_placed %}

顧客が正常にチェックアウトを完了し、発注した時点でトリガーする注文イベントを使用できます。

#### プロパティ

| プロパティ名 | required | データタイプ | 説明 | 
|---|---|---|---|
| `order_id` | はい | string | 注文の一意の識別子。 |
| `cart_id` | いいえ | string | カートの一意の識別子。値が渡されない場合、Braze によりユーザーカートマッピングのデフォルト値 (カート、チェックアウト、注文イベントで共有) が決定します。 |
| `total_value` | はい | フロート | カートの合計金額。 | 
| `currency` | はい | string | カートの金額の通貨。 |
| `total_discounts` | いいえ | フロート | 注文に適用された割引の総額。 | 
| `discounts`| いいえ | オブジェクト配列 | 注文に適用される割引の詳細リスト。 |
| `products` | はい | オブジェクト配列 |  |
| `product_id` | はい | string | 閲覧された製品の一意の識別子。この値には、製品 ID または SKU を使用できます。 |
| `product_name` | はい | string | 閲覧された商品名。 |
| `variant_id` | はい | string | 製品バリアントに固有の識別子。例は`shirt_medium_blue`です |
| `image_url` | いいえ | string | 商品画像のURL。 |
| `product_url` | いいえ | string | 詳細情報がある製品ページの URL。 |
| `quantity` | はい | 整数 | カートに入っている製品の個数。 |
| `price` | はい | フロート | 閲覧時の製品のバリアント単価。 |
| `metadata` | いいえ | オブジェクト | 顧客がユースケースのために追加する製品に関する追加のメタデータフィールド。Shopify の場合は SKU が追加されます。<br> 一般的なイベントプロパティの上限である50kb に基づく制限があります。 |
| `sku` | いいえ | string | (Shopifyのみ）Shopify SKU.これはカタログ ID フィールドとして設定できます。 |
| `source` | はい | string | イベントの派生元ソース。(Shopify の場合これはストアフロントです。) |
| `metadata` | いいえ | オブジェクト |  |
| `order_status_url` | いいえ | string | 注文のステータスを見るためのURL。 |
| `order_number` | いいえ | string | (Shopifyのみ) 発注された注文の固有の注文番号。 |
| `tags` | いいえ | 配列 | (Shopifyのみ）注文タグ
| `referring_site` | いいえ | string | (Shopifyのみ）注文の発信元サイト（Metaなど）。 |
| `payment_gateway_names` | いいえ | 配列 | (Shopifyのみ）決済システムのソース（POSやモバイルなど）。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### オブジェクトの例

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
{% tab ecommerce.order_refunded %}

注文の一部または全体の払い戻しが行われた時点でトリガーする注文払い戻しイベントを使用できます。

#### プロパティ

| プロパティ名       | required | データ型 | 説明   |
|---------------|---------|-----------|-------------------------|
| `order_id`            | はい      | string    | 注文の一意の識別子。        |
| `total_value`         | はい      | フロート     | カートの合計金額。    |
| `currency`            | はい      | string    | カートの金額の通貨。    |
| `total_discounts`     | いいえ       | フロート     | 注文に適用された割引の総額。   |
| `discounts`           | いいえ       | オブジェクト配列     | 注文に適用される割引の詳細リスト。 |
| `products`            | はい      | オブジェクト配列     |  |
| `product_id`       | はい      | string    | 閲覧された製品の一意の識別子。この値には、製品 ID、SKU などを使用できます。<br>一部払い戻しが行われ、払い戻しに `product_id` が割り当てられていない場合 (注文レベルの払い戻しなど) には、一般化された`product_id` を指定します。             |
| `product_name`     | はい      | string    | 閲覧された商品名。                                                                      |
| `variant_id`       | はい      | string    | 製品バリアントの一意の識別子 (`shirt_medium_blue` など)。                                         |
| `image_url`        | いいえ       | string    | 商品画像のURL。     |
| `product_url`      | いいえ       | string    | 詳細情報がある製品ページの URL。  |
| `quantity`         | はい      | 整数   | カートに入っている製品の個数。   |
| `price`            | はい      | フロート     | 閲覧時の製品のバリアント単価。  |
| `metadata`         | いいえ       | オブジェクト    | 顧客がユースケースのために追加する製品に関する追加のメタデータフィールド。Shopify の場合は SKU が追加されます。一般的なイベントプロパティの上限である50kb に基づく制限があります。 |
| `sku`            | いいえ       | string    | (Shopifyのみ）Shopify SKU.これはカタログ ID フィールドとして設定できます。  |
| `source`              | はい      | string    | イベントの派生元ソース。(Shopify の場合これはストアフロントです。)    |
| `metadata`            | いいえ       | オブジェクト    |                |
| `order_status_url`  | いいえ       | string    | 注文のステータスを見るためのURL。     |
| `order_note`       | いいえ       | string    | (Shopify のみ) マーチャントが注文に追加したメモ。    |
| `order_number`     | いいえ       | string    | (Shopifyのみ) 発注された注文の固有の注文番号。   |
| `tags`             | いいえ       | 配列     | (Shopifyのみ）注文タグ。  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### オブジェクトの例

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
{% tab ecommerce.order_cancelled %}

顧客が注文をキャンセルした時点でトリガーする注文キャンセルイベントを使用できます。

#### プロパティ

| プロパティ名      | required | データ型 | 説明       |
|---------------------|----------|-----------|-------------------|
| `order_id`            | はい      | string    | 注文の一意の識別子。              |
| `cancel_reason`       | はい      | string    | 注文がキャンセルされた理由。           |
| `total_value`         | はい      | フロート     | カートの合計金額。         |
| `currency`            | はい      | string    | カートの金額の通貨。           |
| `total_discounts`     | いいえ       | フロート     | 注文に適用された割引の総額。     |
| `discounts`           | いいえ       | オブジェクト配列     | 注文に適用される割引の詳細リスト。             |
| `products`            | はい      | オブジェクト配列     |         |
| `product_id`          | はい      | string    | 閲覧された製品の一意の識別子。この値には、製品 ID、SKU などを使用できます。             |
| `product_name`        | はい      | string    | 閲覧された商品名。          |
| `variant_id`          | はい      | string    | 製品バリアントの一意の識別子 (`shirt_medium_blue` など)。        |
| `image_url`           | いいえ       | string    | 商品画像のURL。           |
| `product_url`         | いいえ       | string    | 詳細情報がある製品ページの URL。                                                                     |
| `quantity`            | はい      | 整数   | カートに入っている製品の個数。        |
| `price`               | はい      | フロート     | 閲覧時の製品のバリアント単価。     |
| `metadata`            | いいえ       | オブジェクト    | 顧客がユースケースのために追加する製品に関する追加のメタデータフィールド。Shopify の場合は SKU が追加されます。一般的なイベントプロパティの上限である50kb に基づく制限があります。 |
| `sku`                 | いいえ       | string    | (Shopifyのみ）Shopify SKU.これはカタログ ID フィールドとして設定できます。        |
| `source`              | はい      | string    | イベントの派生元ソース。(Shopify の場合これはストアフロントです。)    |
| `metadata`            | いいえ       | オブジェクト    |       |
| `order_status_url`    | いいえ       | string    | 注文のステータスを見るためのURL。                                                                          |
| `order_number`        | いいえ       | string    | (Shopifyのみ) 発注された注文の固有の注文番号。  |
| `tags`                | いいえ       | 配列     | (Shopifyのみ）注文タグ。            |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### オブジェクトの例

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

## eコマースキャンバスのテンプレート

Braze では、e コマースの推奨イベントを使用した事前作成済みのキャンバステンプレートを用意しています (チェックアウトプロセスを開始したが注文前に離脱した顧客のターゲティングなど)。メッセージングをパーソナライズしたり、特定のオーディエンスをターゲットにすることで、ユーザー・ジャーニーを向上させるための情報に基づいた決定を下すために、これらのイベントを利用することができる。

Canvasテンプレートでこれらのイベントを使用する方法については、[eコマース専用のユースケースを]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/ecommerce_use_cases)チェックしてほしい。

## ユーザー計算フィールド

以下のフィールドについては、標準化されたユーザーフィールド計算を使用しています。 

- **総収益** = 発注額の合計 - 払い戻し金額の合計
- **注文数の合計** = 個別の注文イベントの数 - 個別の注文キャンセルの数
- **払い戻し合計額** = 払い戻された注文の合計額 

これらのユーザーフィールド計算は、ユーザープロファイルの [**トランザクション**] タブにも含まれています。

![ユーザー計算フィールドが含まれている [トランザクション] タブ。]({% image_buster /assets/img/Shopify/transactions_tab.png %}){: style="max-width:60%;"}

{% alert important %}
購入イベントの段階的廃止計画が2025年後半に発表される予定です。将来的には、購入イベントは新しい[e コマースの推奨イベント]({{site.baseurl}}/user_guide/data/custom_data/recommended_events/ecommerce_events/)に置き換わる予定です。新しい e コマースの推奨イベントには、セグメンテーション、レポート、分析などの強化された機能が組み込まれる予定です。ただし新しい e コマースイベントでは、購入イベントに関連する既存の機能 (キャンバスまたはキャンペーンでの生涯価値 (LTV) または収益の報告など) はサポートされません。購入イベントに関連する機能の完全なリストについては、「[購入イベントのログ]({{site.baseurl}}/user_guide/data/custom_data/purchase_events/#logging-purchase-events)」のセクションを参照のこと。
{% endalert %}
