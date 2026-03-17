---
nav_title: eコマース推奨イベント
article_title: e コマースのおすすめイベント
page_type: reference
alias: /ecommerce_events/
toc_headers: h2
description: "この参考記事では、eコマース推奨のイベントとプロパティ、その使用方法、セグメンテーション、関連する分析を表示する場所などについて説明している。"
---

# e コマースの推奨イベント

> このページでは、e コマース推奨のイベントとプロパティについて説明します。これらのイベントは、マーケターが効果的なメッセージング (カート放棄のターゲット設定など) をトリガーするために必要な主な購入行動をキャプチャする貯めに作成されます。

{% alert important %}
e コマースの推奨イベントは現在、早期アクセス段階です。早期アクセスにご興味のある方は、Brazeカスタマーサクセスマネージャーまでお問い合わせください。<br><br>新しい[Shopifyコネクタ]({{site.baseurl}}/partners/ecommerce/shopify/multiple_stores/?tab=shopify%20connector)を使用している場合、これらの推奨イベントは統合を通じて自動的に利用可能になる。
{% endalert %}

Braze は、データプランニングには時間がかかることを認識しています。お客様の開発チームに周知し、このイベント微送信を今すぐ開始することををお勧めします。eコマース推奨イベントですぐに利用できない機能もあるかもしれないが、eコマース機能を強化する新製品の登場を2025年中に期待できる。

## e コマースの推奨イベントのタイプ

{% multi_lang_include alerts/important_alerts.md alert='Purchase event deprecation' %}

レポートされた米ドル以外の通貨は、レポート日の為替レートに基づき、Brazeでは米ドルで表示される。コンバージョンを防ぐため、通貨を米ドルに固定する。

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
| `type` | いいえ | オブジェクト | [再入荷通知]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications)と[値下げ通知]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/price_drop_notifications)に対応している。 |
| `sku` | いいえ | string | (Shopifyのみ）Shopify SKU.これはカタログ ID フィールドとして設定できます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### 例示されるオブジェクト

{% subtabs %}
{% subtab Web SDK %}

```javascript
braze.logCustomEvent("ecommerce.product_viewed", {
    "product_id": "4111176",
    "product_name": "Torchie runners",
    "variant_id": "4111176700",
    "image_url": "https://braze-apparel.com/images/products/large/torchie-runners.jpg",
    "product_url": "https://braze-apparel.com/footwear-categories/sneakers/braze-orange-torchie-runners/",
    "price": 85,
    "currency": "GBP",
    "source": "https://braze-apparel.com/",
    "metadata": {
        "sku": "",
        "color": "ORANGE",
        "size": "6",
        "brand": "Braze"
    }
});
```

{% endsubtab %}
{% subtab Android SDK %}

```java
BrazeProperties properties = new BrazeProperties()
    .addProperty("product_id", "4111176")
    .addProperty("product_name", "Torchie runners")
    .addProperty("variant_id", "4111176700")
    .addProperty("image_url", "https://braze-apparel.com/images/products/large/torchie-runners.jpg")
    .addProperty("product_url", "https://braze-apparel.com/footwear-categories/sneakers/braze-orange-torchie-runners/")
    .addProperty("price", 85)
    .addProperty("currency", "GBP")
    .addProperty("source", "https://braze-apparel.com/")
    .addProperty("metadata", new JSONObject()
        .put("sku", "")
        .put("color", "ORANGE")
        .put("size", "6")
        .put("brand", "Braze"));

Braze.getInstance(context).logCustomEvent("ecommerce.product_viewed", properties);
```

{% endsubtab %}
{% subtab Swift SDK %}

```swift
let properties: [String: Any] = [
    "product_id": "4111176",
    "product_name": "Torchie runners",
    "variant_id": "4111176700",
    "image_url": "https://braze-apparel.com/images/products/large/torchie-runners.jpg",
    "product_url": "https://braze-apparel.com/footwear-categories/sneakers/braze-orange-torchie-runners/",
    "price": 85,
    "currency": "GBP",
    "source": "https://braze-apparel.com/",
    "metadata": [
        "sku": "",
        "color": "ORANGE",
        "size": "6",
        "brand": "Braze"
    ]
]

AppDelegate.braze?.logCustomEvent(name: "ecommerce.product_viewed", properties: properties)
```

{% endsubtab %}
{% subtab API Payload %}

```json
{
  "events": [
    {
      "external_id": "user_id",
      "app_id": "your_app_identifier",
      "name": "ecommerce.product_viewed",
      "time": "2024-01-15T09:03:45Z",
      "properties": {
        "product_id": "4111176",
        "product_name": "Torchie runners",
        "variant_id": "4111176700",
        "image_url": "https://braze-apparel.com/images/products/large/torchie-runners.jpg",
        "product_url": "https://braze-apparel.com/footwear-categories/sneakers/braze-orange-torchie-runners/",
        "price": 85,
        "currency": "GBP",
        "source": "https://braze-apparel.com/",
        "metadata": {
          "sku": "",
          "color": "ORANGE",
          "size": "6",
          "brand": "Braze"
        },
        "type": [
          "price_drop",
          "back_in_stock"
        ]
      }
    }
  ]
}
```

{% endsubtab %}
{% endsubtabs %}
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
| `cart_id` | はい | string | サードパーティのプラットフォームを利用していない場合、[BrazeのセッションID]({{site.baseurl}}/developer_guide/analytics/tracking_sessions)を使用できる`cart_id`。 |
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

#### 例示されるオブジェクト

{% subtabs %}
{% subtab Web SDK %}

```javascript
braze.logCustomEvent("ecommerce.cart_updated", {
    "cart_id": "cart_12345",
    "currency": "USD",
    "total_value": 199.98,
    "products": [
        {
            "product_id": "8266836345064",
            "product_name": "Classic T-Shirt",
            "variant_id": "44610569208040",
            "image_url": "https://braze-apparel.com/images/tshirt-blue-medium.jpg",
            "product_url": "https://braze-apparel.com/products/classic-tshirt?variant=44610569208040",
            "quantity": 2,
            "price": 99.99,
            "metadata": {
                "sku": "TSH-BLU-M",
                "color": "BLUE",
                "size": "Medium",
                "brand": "Braze"
            }
        }
    ],
    "source": "https://braze-apparel.com",
    "metadata": {}
});
```

{% endsubtab %}
{% subtab Android SDK %}

```java
JSONArray products = new JSONArray();
JSONObject product = new JSONObject()
    .put("product_id", "8266836345064")
    .put("product_name", "Classic T-Shirt")
    .put("variant_id", "44610569208040")
    .put("image_url", "https://braze-apparel.com/images/tshirt-blue-medium.jpg")
    .put("product_url", "https://braze-apparel.com/products/classic-tshirt?variant=44610569208040")
    .put("quantity", 2)
    .put("price", 99.99)
    .put("metadata", new JSONObject()
        .put("sku", "TSH-BLU-M")
        .put("color", "BLUE")
        .put("size", "Medium")
        .put("brand", "Braze"));
products.put(product);

BrazeProperties properties = new BrazeProperties()
    .addProperty("cart_id", "cart_12345")
    .addProperty("currency", "USD")
    .addProperty("total_value", 199.98)
    .addProperty("products", products)
    .addProperty("source", "https://braze-apparel.com")
    .addProperty("metadata", new JSONObject());

Braze.getInstance(context).logCustomEvent("ecommerce.cart_updated", properties);
```

{% endsubtab %}
{% subtab Swift SDK %}

```swift
let products: [[String: Any]] = [
    [
        "product_id": "8266836345064",
        "product_name": "Classic T-Shirt",
        "variant_id": "44610569208040",
        "image_url": "https://braze-apparel.com/images/tshirt-blue-medium.jpg",
        "product_url": "https://braze-apparel.com/products/classic-tshirt?variant=44610569208040",
        "quantity": 2,
        "price": 99.99,
        "metadata": [
            "sku": "TSH-BLU-M",
            "color": "BLUE",
            "size": "Medium",
            "brand": "Braze"
        ]
    ]
]

let properties: [String: Any] = [
    "cart_id": "cart_12345",
    "currency": "USD",
    "total_value": 199.98,
    "products": products,
    "source": "https://braze-apparel.com",
    "metadata": [:]
]

AppDelegate.braze?.logCustomEvent(name: "ecommerce.cart_updated", properties: properties)
```

{% endsubtab %}
{% subtab API Payload %}

```json
{
  "events": [
    {
      "external_id": "user_id",
      "app_id": "your_app_identifier",
      "name": "ecommerce.cart_updated",
      "time": "2024-01-15T09:15:30Z",
      "properties": {
        "cart_id": "cart_12345",
        "currency": "USD",
        "total_value": 199.98,
        "products": [
          {
            "product_id": "8266836345064",
            "product_name": "Classic T-Shirt",
            "variant_id": "44610569208040",
            "image_url": "https://braze-apparel.com/images/tshirt-blue-medium.jpg",
            "product_url": "https://braze-apparel.com/products/classic-tshirt?variant=44610569208040",
            "quantity": 2,
            "price": 99.99,
            "metadata": {
              "sku": "TSH-BLU-M",
              "color": "BLUE",
              "size": "Medium",
              "brand": "Braze"
            }
          }
        ],
        "source": "https://braze-apparel.com",
        "metadata": {}
      }
    }
  ]
}
```

{% endsubtab %}
{% endsubtabs %}
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
| `cart_id` | いいえ | string | サードパーティのプラットフォームを利用していない場合、[BrazeのセッションID]({{site.baseurl}}/developer_guide/analytics/tracking_sessions)を使用できる`cart_id`。 | 
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

#### 例示されるオブジェクト

{% subtabs %}
{% subtab Web SDK %}

```javascript
braze.logCustomEvent("ecommerce.checkout_started", {
    "checkout_id": "checkout_abc123",
    "cart_id": "cart_12345",
    "total_value": 199.98,
    "currency": "USD",
    "products": [
        {
            "product_id": "632910392",
            "product_name": "Wireless Headphones",
            "variant_id": "808950810",
            "quantity": 1,
            "price": 199.98,
            "metadata": {
                "sku": "WH-BLK-PRO",
                "color": "Black",
                "brand": "BrazeAudio"
            }
        }
    ],
    "source": "https://braze-audio.com",
    "metadata": {
        "checkout_url": "https://checkout.braze-audio.com/abc123"
    }
});
```

{% endsubtab %}
{% subtab Android SDK %}

```java
JSONArray products = new JSONArray();
JSONObject product = new JSONObject()
    .put("product_id", "632910392")
    .put("product_name", "Wireless Headphones")
    .put("variant_id", "808950810")
    .put("quantity", 1)
    .put("price", 199.98)
    .put("metadata", new JSONObject()
        .put("sku", "WH-BLK-PRO")
        .put("color", "Black")
        .put("brand", "AudioTech"));
products.put(product);

BrazeProperties properties = new BrazeProperties()
    .addProperty("checkout_id", "checkout_abc123")
    .addProperty("cart_id", "cart_12345")
    .addProperty("total_value", 199.98)
    .addProperty("currency", "USD")
    .addProperty("products", products)
    .addProperty("source", "https://braze-audio.com")
    .addProperty("metadata", new JSONObject()
        .put("checkout_url", "https://checkout.braze-audio.com/abc123"));

Braze.getInstance(context).logCustomEvent("ecommerce.checkout_started", properties);
```

{% endsubtab %}
{% subtab Swift SDK %}

```swift
let products: [[String: Any]] = [
    [
        "product_id": "632910392",
        "product_name": "Wireless Headphones",
        "variant_id": "808950810",
        "quantity": 1,
        "price": 199.98,
        "metadata": [
            "sku": "WH-BLK-PRO",
            "color": "Black",
            "brand": "BrazeAudio"
        ]
    ]
]

let properties: [String: Any] = [
    "checkout_id": "checkout_abc123",
    "cart_id": "cart_12345",
    "total_value": 199.98,
    "currency": "USD",
    "products": products,
    "source": "https://braze-audio.com",
    "metadata": [
        "checkout_url": "https://checkout.braze-audio.com/abc123"
    ]
]

AppDelegate.braze?.logCustomEvent(name: "ecommerce.checkout_started", properties: properties)
```

{% endsubtab %}
{% subtab API Payload %}

```json
{
  "events": [
    {
      "external_id": "user_id",
      "app_id": "your_app_identifier",
      "name": "ecommerce.checkout_started",
      "time": "2024-01-15T09:25:45Z",
      "properties": {
        "checkout_id": "checkout_abc123",
        "cart_id": "cart_12345",
        "total_value": 199.98,
        "currency": "USD",
        "products": [
          {
            "product_id": "632910392",
            "product_name": "Wireless Headphones",
            "variant_id": "808950810",
            "quantity": 1,
            "price": 199.98,
            "metadata": {
              "sku": "WH-BLK-PRO",
              "color": "Black",
              "brand": "BrazeAudio"
            }
          }
        ],
        "source": "https://braze-audio.com",
        "metadata": {
          "checkout_url": "https://checkout.braze-audio.com/abc123"
        }
      }
    }
  ]
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab ecommerce.order_placed %}

顧客が正常にチェックアウトを完了し、発注した時点でトリガーする注文イベントを使用できます。

#### プロパティ

| プロパティ名 | required | データタイプ | 説明 | 
|---|---|---|---|
| `order_id` | はい | string | 注文の一意の識別子。 |
| `cart_id` | いいえ | string | サードパーティのプラットフォームを利用していない場合、[BrazeのセッションID]({{site.baseurl}}/developer_guide/analytics/tracking_sessions)を使用できる`cart_id`。 |
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
| `order_status_url` | いいえ | string | 注文のステータスを見るためのURL。 |
| `order_number` | いいえ | string | (Shopifyのみ) 発注された注文の固有の注文番号。 |
| `tags` | いいえ | 配列 | (Shopifyのみ）注文タグ
| `referring_site` | いいえ | string | (Shopifyのみ）注文の発信元サイト（Metaなど）。 |
| `payment_gateway_names` | いいえ | 配列 | （Shopifyのみ）決済システムのソース（例：POSシステムやモバイル端末など）。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### 例示されるオブジェクト

{% subtabs %}
{% subtab Web SDK %}

```javascript
braze.logCustomEvent("ecommerce.order_placed", {
    "order_id": "order_67890",
    "cart_id": "cart_12345",
    "total_value": 189.98,
    "currency": "USD",
    "total_discounts": 10.00,
    "discounts": [
        {
            "code": "SAVE10",
            "amount": 10.00
        }
    ],
    "products": [
        {
            "product_id": "632910392",
            "product_name": "Wireless Headphones",
            "variant_id": "808950810",
            "quantity": 1,
            "price": 199.98,
            "metadata": {
                "sku": "WH-BLK-PRO",
                "color": "Black",
                "brand": "BrazeAudio"
            }
        }
    ],
    "source": "https://braze-audio.com",
    "metadata": {
        "order_status_url": "https://braze-audio.com/orders/67890/status",
        "order_number": "ORD-2024-001234",
        "tags": ["electronics", "audio"],
        "referring_site": "https://www.e-referrals.com",
        "payment_gateway_names": ["tap2pay", "dotcash"]
    }
});
```

{% endsubtab %}
{% subtab Android SDK %}

```java
JSONArray discounts = new JSONArray();
discounts.put(new JSONObject()
    .put("code", "SAVE10")
    .put("amount", 10.00));

JSONArray products = new JSONArray();
JSONObject product = new JSONObject()
    .put("product_id", "632910392")
    .put("product_name", "Wireless Headphones")
    .put("variant_id", "808950810")
    .put("quantity", 1)
    .put("price", 199.98)
    .put("metadata", new JSONObject()
        .put("sku", "WH-BLK-PRO")
        .put("color", "Black")
        .put("brand", "AudioTech"));
products.put(product);

BrazeProperties properties = new BrazeProperties()
    .addProperty("order_id", "order_67890")
    .addProperty("cart_id", "cart_12345")
    .addProperty("total_value", 189.98)
    .addProperty("currency", "USD")
    .addProperty("total_discounts", 10.00)
    .addProperty("discounts", discounts)
    .addProperty("products", products)
    .addProperty("source", "https://braze-audio.com")
    .addProperty("metadata", new JSONObject()
        .put("order_status_url", "https://braze-audio.com/orders/67890/status")
        .put("order_number", "ORD-2024-001234")
        .put("tags", new JSONArray().put("electronics").put("audio"))
        .put("referring_site", "https://www.e-referrals.com")
        .put("payment_gateway_names", new JSONArray().put("tap2pay").put("dotcash")));

Braze.getInstance(context).logCustomEvent("ecommerce.order_placed", properties);
```

{% endsubtab %}
{% subtab Swift SDK %}

```swift
let discounts: [[String: Any]] = [
    [
        "code": "SAVE10",
        "amount": 10.00
    ]
]

let products: [[String: Any]] = [
    [
        "product_id": "632910392",
        "product_name": "Wireless Headphones",
        "variant_id": "808950810",
        "quantity": 1,
        "price": 199.98,
        "metadata": [
            "sku": "WH-BLK-PRO",
            "color": "Black",
            "brand": "BrazeAudio"
        ]
    ]
]

let properties: [String: Any] = [
    "order_id": "order_67890",
    "cart_id": "cart_12345",
    "total_value": 189.98,
    "currency": "USD",
    "total_discounts": 10.00,
    "discounts": discounts,
    "products": products,
    "source": "https://braze-audio.com",
    "metadata": [
        "order_status_url": "https://braze-audio.com/orders/67890/status",
        "order_number": "ORD-2024-001234",
        "tags": ["electronics", "audio"],
        "referring_site": "https://www.e-referrals.com",
        "payment_gateway_names": ["tap2pay", "dotcash"]
    ]
]

AppDelegate.braze?.logCustomEvent(name: "ecommerce.order_placed", properties: properties)
```

{% endsubtab %}
{% subtab API Payload %}

```json
{
  "events": [
    {
      "external_id": "user_id",
      "app_id": "your_app_identifier",
      "name": "ecommerce.order_placed",
      "time": "2024-01-15T09:35:20Z",
      "properties": {
        "order_id": "order_67890",
        "cart_id": "cart_12345",
        "total_value": 189.98,
        "currency": "USD",
        "total_discounts": 10.00,
        "discounts": [
          {
            "code": "SAVE10",
            "amount": 10.00
          }
        ],
        "products": [
          {
            "product_id": "632910392",
            "product_name": "Wireless Headphones",
            "variant_id": "808950810",
            "quantity": 1,
            "price": 199.98,
            "metadata": {
              "sku": "WH-BLK-PRO",
              "color": "Black",
              "brand": "BrazeAudio"
            }
          }
        ],
        "source": "https://braze-audio.com",
        "metadata": {
          "order_status_url": "https://braze-audio.com/orders/67890/status",
          "order_number": "ORD-2024-001234",
          "tags": ["electronics", "audio"],
          "referring_site": "https://www.e-referrals.com",
          "payment_gateway_names": ["tap2pay", "dotcash"]
        }
      }
    }
  ]
}
```

{% endsubtab %}
{% endsubtabs %}
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

#### 例示されるオブジェクト

{% subtabs %}
{% subtab Web SDK %}

```javascript
braze.logCustomEvent("ecommerce.order_refunded", {
    "order_id": "order_67890",
    "total_value": 99.99,
    "currency": "USD",
    "total_discounts": 5.00,
    "discounts": [
        {
            "code": "SAVE5",
            "amount": 5.00
        }
    ],
    "products": [
        {
            "product_id": "632910392",
            "product_name": "Wireless Headphones",
            "variant_id": "808950810",
            "quantity": 1,
            "price": 99.99,
            "metadata": {
                "sku": "WH-BLK-PRO",
                "color": "Black",
                "brand": "BrazeAudio"
            }
        }
    ],
    "source": "https://braze-audio.com",
    "metadata": {
        "order_status_url": "https://braze-audio.com/orders/67890/status",
        "order_note": "Customer requested refund due to defective item",
        "order_number": "ORD-2024-001234",
        "tags": ["refund", "defective"]
    }
});
```

{% endsubtab %}
{% subtab Android SDK %}

```java
JSONArray discounts = new JSONArray();
discounts.put(new JSONObject()
    .put("code", "SAVE5")
    .put("amount", 5.00));

JSONArray products = new JSONArray();
JSONObject product = new JSONObject()
    .put("product_id", "632910392")
    .put("product_name", "Wireless Headphones")
    .put("variant_id", "808950810")
    .put("quantity", 1)
    .put("price", 99.99)
    .put("metadata", new JSONObject()
        .put("sku", "WH-BLK-PRO")
        .put("color", "Black")
        .put("brand", "AudioTech"));
products.put(product);

BrazeProperties properties = new BrazeProperties()
    .addProperty("order_id", "order_67890")
    .addProperty("total_value", 99.99)
    .addProperty("currency", "USD")
    .addProperty("total_discounts", 5.00)
    .addProperty("discounts", discounts)
    .addProperty("products", products)
    .addProperty("source", "https://braze-audio.com")
    .addProperty("metadata", new JSONObject()
        .put("order_status_url", "https://braze-audio.com/orders/67890/status")
        .put("order_note", "Customer requested refund due to defective item")
        .put("order_number", "ORD-2024-001234")
        .put("tags", new JSONArray().put("refund").put("defective")));

Braze.getInstance(context).logCustomEvent("ecommerce.order_refunded", properties);
```

{% endsubtab %}
{% subtab Swift SDK %}

```swift
let discounts: [[String: Any]] = [
    [
        "code": "SAVE5",
        "amount": 5.00
    ]
]

let products: [[String: Any]] = [
    [
        "product_id": "632910392",
        "product_name": "Wireless Headphones",
        "variant_id": "808950810",
        "quantity": 1,
        "price": 99.99,
        "metadata": [
            "sku": "WH-BLK-PRO",
            "color": "Black",
            "brand": "BrazeAudio"
        ]
    ]
]

let properties: [String: Any] = [
    "order_id": "order_67890",
    "total_value": 99.99,
    "currency": "USD",
    "total_discounts": 5.00,
    "discounts": discounts,
    "products": products,
    "source": "https://braze-audio.com",
    "metadata": [
        "order_status_url": "https://braze-audio.com/orders/67890/status",
        "order_note": "Customer requested refund due to defective item",
        "order_number": "ORD-2024-001234",
        "tags": ["refund", "defective"]
    ]
]

AppDelegate.braze?.logCustomEvent(name: "ecommerce.order_refunded", properties: properties)
```

{% endsubtab %}
{% subtab API Payload %}

```json
{
  "events": [
    {
      "external_id": "user_id",
      "app_id": "your_app_identifier",
      "name": "ecommerce.order_refunded",
      "time": "2024-01-15T10:15:30Z",
      "properties": {
        "order_id": "order_67890",
        "total_value": 99.99,
        "currency": "USD",
        "total_discounts": 5.00,
        "discounts": [
          {
            "code": "SAVE5",
            "amount": 5.00
          }
        ],
        "products": [
          {
            "product_id": "632910392",
            "product_name": "Wireless Headphones",
            "variant_id": "808950810",
            "quantity": 1,
            "price": 99.99,
            "metadata": {
              "sku": "WH-BLK-PRO",
              "color": "Black",
              "brand": "BrazeAudio"
            }
          }
        ],
        "source": "https://braze-audio.com",
        "metadata": {
          "order_status_url": "https://braze-audio.com/orders/67890/status",
          "order_note": "Customer requested refund due to defective item",
          "order_number": "ORD-2024-001234",
          "tags": ["refund", "defective"]
        }
      }
    }
  ]
}
```

{% endsubtab %}
{% endsubtabs %}
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

#### 例示されるオブジェクト

{% subtabs %}
{% subtab Web SDK %}

```javascript
braze.logCustomEvent("ecommerce.order_cancelled", {
    "order_id": "order_67890",
    "cancel_reason": "customer changed mind",
    "total_value": 189.98,
    "currency": "USD",
    "total_discounts": 10.00,
    "discounts": [
        {
            "code": "SAVE10",
            "amount": 10.00
        }
    ],
    "products": [
        {
            "product_id": "632910392",
            "product_name": "Wireless Headphones",
            "variant_id": "808950810",
            "quantity": 1,
            "price": 199.98,
            "metadata": {
                "sku": "WH-BLK-PRO",
                "color": "Black",
                "brand": "BrazeAudio"
            }
        }
    ],
    "source": "https://braze-audio.com",
    "metadata": {
        "order_status_url": "https://braze-audio.com/orders/67890/status",
        "order_number": "ORD-2024-001234",
        "tags": ["cancelled", "customer_request"]
    }
});
```

{% endsubtab %}
{% subtab Android SDK %}

```java
JSONArray discounts = new JSONArray();
discounts.put(new JSONObject()
    .put("code", "SAVE10")
    .put("amount", 10.00));

JSONArray products = new JSONArray();
JSONObject product = new JSONObject()
    .put("product_id", "632910392")
    .put("product_name", "Wireless Headphones")
    .put("variant_id", "808950810")
    .put("quantity", 1)
    .put("price", 199.98)
    .put("metadata", new JSONObject()
        .put("sku", "WH-BLK-PRO")
        .put("color", "Black")
        .put("brand", "AudioTech"));
products.put(product);

BrazeProperties properties = new BrazeProperties()
    .addProperty("order_id", "order_67890")
    .addProperty("cancel_reason", "customer changed mind")
    .addProperty("total_value", 189.98)
    .addProperty("currency", "USD")
    .addProperty("total_discounts", 10.00)
    .addProperty("discounts", discounts)
    .addProperty("products", products)
    .addProperty("source", "https://braze-audio.com")
    .addProperty("metadata", new JSONObject()
        .put("order_status_url", "https://braze-audio.com/orders/67890/status")
        .put("order_number", "ORD-2024-001234")
        .put("tags", new JSONArray().put("cancelled").put("customer_request")));

Braze.getInstance(context).logCustomEvent("ecommerce.order_cancelled", properties);
```

{% endsubtab %}
{% subtab Swift SDK %}

```swift
let discounts: [[String: Any]] = [
    [
        "code": "SAVE10",
        "amount": 10.00
    ]
]

let products: [[String: Any]] = [
    [
        "product_id": "632910392",
        "product_name": "Wireless Headphones",
        "variant_id": "808950810",
        "quantity": 1,
        "price": 199.98,
        "metadata": [
            "sku": "WH-BLK-PRO",
            "color": "Black",
            "brand": "BrazeAudio"
        ]
    ]
]

let properties: [String: Any] = [
    "order_id": "order_67890",
    "cancel_reason": "customer changed mind",
    "total_value": 189.98,
    "currency": "USD",
    "total_discounts": 10.00,
    "discounts": discounts,
    "products": products,
    "source": "https://braze-audio.com",
    "metadata": [
        "order_status_url": "https://braze-audio.com/orders/67890/status",
        "order_number": "ORD-2024-001234",
        "tags": ["cancelled", "customer_request"]
    ]
]

AppDelegate.braze?.logCustomEvent(name: "ecommerce.order_cancelled", properties: properties)
```

{% endsubtab %}
{% subtab API Payload %}

```json
{
  "events": [
    {
      "external_id": "user_id",
      "app_id": "your_app_identifier",
      "name": "ecommerce.order_cancelled",
      "time": "2024-01-15T10:45:15Z",
      "properties": {
        "order_id": "order_67890",
        "cancel_reason": "customer changed mind",
        "total_value": 189.98,
        "currency": "USD",
        "total_discounts": 10.00,
        "discounts": [
          {
            "code": "SAVE10",
            "amount": 10.00
          }
        ],
        "products": [
          {
            "product_id": "632910392",
            "product_name": "Wireless Headphones",
            "variant_id": "808950810",
            "quantity": 1,
            "price": 199.98,
            "metadata": {
              "sku": "WH-BLK-PRO",
              "color": "Black",
              "brand": "BrazeAudio"
            }
          }
        ],
        "source": "https://braze-audio.com",
        "metadata": {
          "order_status_url": "https://braze-audio.com/orders/67890/status",
          "order_number": "ORD-2024-001234",
          "tags": ["cancelled", "customer_request"]
        }
      }
    }
  ]
}
```

{% endsubtab %}
{% endsubtabs %}

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

![ユーザーが計算したフィールドを含む「取引」タブ。]({% image_buster /assets/img/Shopify/transactions_tab.png %}){: style="max-width:70%;"}

## よくある質問

### 製品レベルの購入データはどこで確認できるか？

ユーザープロファイルの「**取引**」タブには、高レベルの計算フィールド（総収益や総注文数など）が表示される。特定のユーザーに関する製品レベルの詳細を表示するには、[クエリ]({{site.baseurl}}/user_guide/analytics/query_builder/)ビルダーを使用してe コマースイベントデータをクエリするか、[Currents]({{site.baseurl}}/user_guide/data/braze_currents/)を通じてイベントデータをエクスポートする。

従来の購入イベントとは異なり、e コマース推奨イベントでは、商品詳細が`products`配列内のネストされたイベントプロパティとして保存される。これらのプロパティは、Liquidによるメッセージングと、[セグメントエクステンション]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/)によるセグメンテーションで利用可能だ。

### 特定の製品でユーザーをセグメントするにはどうすればよいのか？

セグメンターは、ユーザーがe コマースイベントを実行した回数でフィルターをかけることを可能にする。特定の製品プロパティ（例：`product_id`や`product_name`）でフィルターするには、ネストされたイベントプロパティフィルターをサポートする[セグメントエクステンション]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/)を使用する。例えば、過去90日間に商品「SKU-123」を購入した全ユーザーを検索できる。

### レガシー購入イベントとe コマース推奨イベントの違いは何だ？

従来の購入イベントはBrazeの[購入オブジェクト]({{site.baseurl}}/api/objects_filters/purchase_object/)を使用し、個々の製品購入を\`product_id`product_id``と`price`\`price\`で記録する。e コマース推奨イベント（例：\`purchase`ecommerce.order_placed``）はカスタムイベントプロパティを使用し、複数の製品、割引、メタデータを含む完全な注文コンテキストを単一のイベントで捕捉する。

e コマースの推奨イベントの導入に伴い、Braze は今後、従来の購入イベントを段階的に廃止していく予定です。現在購入イベントを利用している場合、事前に通知が届く。その間、正式な廃止日までは購入イベントを引き続き使用できる。詳細は[推奨イベント]({{site.baseurl}}/user_guide/data/activation/custom_data/recommended_events/)の[概要]({{site.baseurl}}/user_guide/data/activation/custom_data/recommended_events/)を参照せよ。

### e コマースの推奨イベントにカスタムプロパティを追加できるか？

e コマースの推奨イベントには、必須フィールドとオプションフィールドを含む定義済みスキーマがある。各イベントごとに、オブジェクト`metadata`内に追加のカスタムデータを含めることができる。ただし、カスタム注文レベルのタグや独自フィールド（購入チャネルや小売店情報など）は、最上位のプロパティとしてサポートされていない。セグメンテーションにこれらのフィールドが必要な場合は、e コマースイベントとは別にカスタムイベントとして送信し続けること。

### e コマースイベントを送信するexternal_id際に含める必要があるか？

それはイベントの送信方法による。

- **SDK経由で**：いいえ。Braze SDKを使用する場合、イベントは自動的にSDKの現在のユーザーコンテキスト（匿名または識別子を持つユーザー）に関連付けられる。各イベント呼び出しごとにユーザー識別子を渡す必要はない。代わりに、そのコンテキストにおけるユーザーを特定するには、`changeUser`. などのメソッドを使用できる。
- **REST API を通じて**`/users/track`：はい。各APIリクエストには、ユーザー識別子を含める必要がある。`external_id`例えば、`user_alias``braze_id````email`、\`\`、`phone```、``、``などである。なぜなら、このAPIには「現在のユーザー」という文脈が存在しないからだ。

### なぜネストされた製品プロパティがAIレコメンデーション設定のドロップダウンに表示されないのか？

[AIアイテム推薦]({{site.baseurl}}/user_guide/brazeai/recommendations/)を設定する際、**プロパティ**名のドロップダウンには最上位のイベントプロパティ（例`order_id`：`total_value`、など`currency`）のみが表示される。配列`products`内のネストされたプロパティ（例えば、`products.product_id`や`products.variant_id`）はこのリストに表示されない場合があるが、フィールド内でドット表記を使って手動で入力できる。ほとんどのe コマース実装において、Brazeはアイテム識別子として`products.product_id`を使用し、そのアイテムIDが`product_id`または`variant_id`の値と一致する[カタログ]({{site.baseurl}}/user_guide/data/activation/catalogs/)と組み合わせることを推奨する。

### なぜ一部のe コマースイベントがBrazeに表示されないのか？

イベントがユーザープロファイルやログに表示されない場合、以下の点を確認せよ：

- **SDKデータのフラッシュタイミング**：Braze SDKはデータをローカルにキャッシュし、定期的にアップロードする（通常10～60秒以内）。直ちにアップロードを強制するには、`logCustomEvent()`後で`requestImmediateDataFlush()`呼び出す。
- **必須プロパティ**：e コマースイベントには必須のプロパティがある。必要なプロパティが欠けているか、データ型が無効な場合、イベントは拒否される可能性がある。イベントペイロードが[要求されるスキーマ](#types-of-ecommerce-recommended-events)と一致していることを確認せよ。
- **イベント名の正確性**：e コマースのイベント名は大文字小文字を区別し、完全に一致しなければならない（例：`ecommerce.checkout_started`ではなく`ecommerce.checkoutStarted`）。
