---
nav_title: eコマース推奨イベント
article_title: e コマースの推奨イベント
page_type: reference
alias: /ecommerce_events/
toc_headers: h2
description: "この参照記事では、e コマース推奨のイベントとプロパティ、その使用方法、セグメンテーション、関連する分析の表示場所などについて説明します。"
---

# e コマースの推奨イベント

> このページでは、e コマース推奨のイベントとプロパティについて説明します。これらのイベントは、マーケターが効果的なメッセージング (カート放棄のターゲット設定など) をトリガーするために必要な主要な購買行動をキャプチャするために作成されています。

{% alert important %}
e コマースの推奨イベントは現在、早期アクセス段階です。早期アクセスにご興味のある方は、Braze カスタマーサクセスマネージャーまでお問い合わせください。<br><br>新しい [Shopify コネクタ]({{site.baseurl}}/partners/ecommerce/shopify/multiple_stores/?tab=shopify%20connector)を使用している場合、これらの推奨イベントは統合を通じて自動的に利用可能になります。
{% endalert %}

Braze は、データプランニングには時間がかかることを認識しています。お客様の開発チームに周知し、これらのイベントの送信を今すぐ開始することをお勧めします。e コマース推奨イベントですぐに利用できない機能もあるかもしれませんが、e コマース機能を強化する新製品が2025年中に順次リリースされる予定です。

## e コマースの推奨イベントのタイプ

{% multi_lang_include alerts/important_alerts.md alert='Purchase event deprecation' %}

レポートされた米ドル以外の通貨は、レポート日の為替レートに基づき、Braze では米ドルで表示されます。通貨換算を防ぐには、通貨を米ドルにハードコードしてください。

{% tabs %}
{% tab ecommerce.product_viewed %}

顧客が商品詳細ページを閲覧した時点でトリガーされる製品閲覧イベントを使用できます。

#### プロパティ

| プロパティ名 | 必須 | データタイプ | 説明 | 
|---|---|---|---|
| `product_id` | はい | 文字列 | 閲覧された製品の一意の識別子。<br> Shopify 以外の顧客の場合、これは SKU のようなカタログアイテム ID に設定した値になります。 |
| `product_name` | はい | 文字列 | 閲覧された商品名。 | 
| `variant_id` | はい | 文字列 | 製品バリアントの一意の識別子。例: `shirt_medium_blue` |
| `image_url` | いいえ | 文字列 | 商品画像の URL。 |
| `product_url` | いいえ | 文字列 | 詳細情報がある製品ページの URL。 |
| `price` | はい | フロート | 閲覧時の製品のバリアント単価。 |
| `currency` | はい | 文字列 | 製品価格の表示通貨 (「USD」や「EUR」など)。[ISO 4217 フォーマット](https://www.iso.org/iso-4217-currency-codes.html)です。 |
| `source` | はい | 文字列 | イベントの派生元ソース。(Shopify の場合これはストアフロントです。) |
| `metadata` | いいえ | オブジェクト | |
| `type` | いいえ | オブジェクト | [再入荷通知]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications)と[値下げ通知]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/price_drop_notifications)に対応しています。 |
| `sku` | いいえ | 文字列 | (Shopify のみ) Shopify SKU。これはカタログ ID フィールドとして設定できます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### オブジェクトの例

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

**カート更新イベントの実行**トリガーを使用して、カートに製品が追加、削除、または更新された時点をトラッキングできます。このイベントはトリガー前に以下の情報を検証します。

- イベントの時刻が、ユーザーの特定のカートの `updated_at` の時刻よりも後である。
- カートが購入手続きに進んでいない。
- `products` の配列が空ではない。

#### カートマッピングオブジェクト

`ecommerce.cart_updated` イベントにはカートマッピングオブジェクトがあります。このオブジェクトは、カートのマッピングを含むユーザープロファイルに対して作成され、購入者のカートに入っているすべての製品が含まれています。Liquid タグを使用してショッピングカート内の製品にアクセスできます。 

{%raw%}
```liquid
{% shopping_cart {{context_properties.${cart_id}}} %}
{% for item in shopping_cart.products %}
{% catalog_items <add_your_catalog> {{item.variant_id}} %}
```
{%endraw%}

10日以内にカートが更新されず、注文確定イベントに進まなかった場合、カートと関連製品は削除されます。

{% alert note %}
Braze ではカートあたりの製品数に制限はありません。ただし Shopify での上限は500です。
{% endalert %}

#### ユーザープロファイルをマージする際のカートの動作

カートが2つある場合は、両方がマージされたユーザーに追加されます。同じカートまたは異なるカートの場合、最新のカート情報を含むメッセージを送信するためにキャンバスを再度キューに入れます。`ecommerce.cart_updated` イベントには、最新のカート ID とカート内の最新の商品が含まれます。

#### プロパティ

| プロパティ名 | 必須 | データタイプ | 説明 | 
|---|---|---|---|
| `cart_id` | はい | 文字列 | `cart_id` を提供するサードパーティプラットフォームを使用していない場合は、[Braze のセッション ID]({{site.baseurl}}/developer_guide/analytics/tracking_sessions) を使用できます。 |
| `total_value` | はい | フロート | カートの合計金額。 | 
| `currency` | はい | 文字列 | 製品価格の表示通貨 (「USD」や「EUR」など)。[ISO 4217 フォーマット](https://www.iso.org/iso-4217-currency-codes.html)です。 |
| `products` | はい | 配列 |  |
| `product_id` | はい | 文字列 | 閲覧された製品の一意の識別子。<br> この値には、製品 ID または SKU を使用できます。 |
| `product_name` | はい | 文字列 | 閲覧された商品名。 |
| `variant_id` | はい | 文字列 | 製品バリアントの一意の識別子。例: `shirt_medium_blue` |
| `image_url` | いいえ | 文字列 | 商品画像の URL。 |
| `product_url` | いいえ | 文字列 | 詳細情報がある製品ページの URL。 |
| `quantity` | はい | 整数 | カートに入っている製品の個数。 |
| `price` | はい | フロート | 閲覧時の製品のバリアント単価。 |
| `metadata` | いいえ | オブジェクト | 顧客がユースケースのために追加する製品に関する追加のメタデータフィールド。Shopify の場合は SKU が追加されます。<br> 一般的なイベントプロパティの上限である 50KB に基づく制限があります。 |
| `sku` | いいえ | 文字列 | (Shopify のみ) Shopify SKU。これはカタログ ID フィールドとして設定できます。 |
| `source` | はい | 文字列 | イベントの派生元ソース。(Shopify の場合これはストアフロントです。) |
| `metadata` | いいえ | オブジェクト | 顧客がユースケースのために追加する製品に関する追加のメタデータフィールド。Shopify の場合は SKU が追加されます。<br> 一般的なイベントプロパティの上限である 50KB に基づく制限があります。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### オブジェクトの例

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

チェックアウト開始イベントを使用して、チェックアウトプロセスを開始したが注文を完了していない顧客をリターゲティングできます。

`ecommerce.cart_updated` イベントと同様に、このイベントではショッピングカート Liquid タグを使用して、購入手続き放棄メッセージのためにカート内のすべての製品にアクセスできます。

{%raw%}
```liquid
{% shopping_cart {{context_properties.${cart_id}}} :abort_if_not_abandoned false %}
{% for item in shopping_cart.products %}
{% catalog_items <add_your_catalog> {{item.variant_id}} %}
```
{%endraw%}

#### プロパティ

| プロパティ名 | 必須 | データタイプ | 説明 | 
|---|---|---|---|
| `checkout_id` | はい | 文字列 | チェックアウトの一意の識別子。 |
| `cart_id` | いいえ | 文字列 | `cart_id` を提供するサードパーティプラットフォームを使用していない場合は、[Braze のセッション ID]({{site.baseurl}}/developer_guide/analytics/tracking_sessions) を使用できます。 | 
| `total_value` | はい | フロート | カートの合計金額。 |
| `currency` | はい | 文字列 | カートの金額の通貨。 |
| `products` | はい | オブジェクト配列 |  |
| `product_id` | はい | 文字列 | 閲覧された製品の一意の識別子。例えば製品 ID や SKU がこの値になります。 |
| `product_name` | はい | 文字列 | 閲覧された商品名。  |
| `variant_id` | はい | 文字列 | 製品バリアントの一意の識別子。例: `shirt_medium_blue` |
| `image_url` | いいえ | 文字列 | 商品画像の URL。 |
| `product_url` | いいえ | 文字列 | 詳細情報がある製品ページの URL。 |
| `quantity` | はい | 整数 | カートに入っている製品の個数。 |
| `price` | はい | フロート | 閲覧時の製品のバリアント単価。 |
| `metadata` | いいえ | オブジェクト | 顧客がユースケースのために追加する製品に関する追加のメタデータフィールド。Shopify の場合は SKU が追加されます。<br> 一般的なイベントプロパティの上限である 50KB に基づく制限があります。 |
| `sku` | いいえ | 文字列 | (Shopify のみ) Shopify SKU。これはカタログ ID フィールドとして設定できます。 |
| `source` | はい | 文字列 | イベントの派生元ソース。(Shopify の場合これはストアフロントです。) |
| `metadata` | いいえ | オブジェクト |  |
| `checkout_url` | いいえ | 文字列 | チェックアウトページの URL。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### オブジェクトの例

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

顧客が正常にチェックアウトを完了し、注文を確定した時点でトリガーする注文確定イベントを使用できます。

#### プロパティ

| プロパティ名 | 必須 | データタイプ | 説明 | 
|---|---|---|---|
| `order_id` | はい | 文字列 | 注文の一意の識別子。 |
| `cart_id` | いいえ | 文字列 | `cart_id` を提供するサードパーティプラットフォームを使用していない場合は、[Braze のセッション ID]({{site.baseurl}}/developer_guide/analytics/tracking_sessions) を使用できます。 |
| `total_value` | はい | フロート | カートの合計金額。 | 
| `currency` | はい | 文字列 | カートの金額の通貨。 |
| `total_discounts` | いいえ | フロート | 注文に適用された割引の総額。 | 
| `discounts`| いいえ | オブジェクト配列 | 注文に適用された割引の詳細リスト。 |
| `products` | はい | オブジェクト配列 |  |
| `product_id` | はい | 文字列 | 閲覧された製品の一意の識別子。この値には、製品 ID または SKU を使用できます。 |
| `product_name` | はい | 文字列 | 閲覧された商品名。 |
| `variant_id` | はい | 文字列 | 製品バリアントの一意の識別子。例: `shirt_medium_blue` |
| `image_url` | いいえ | 文字列 | 商品画像の URL。 |
| `product_url` | いいえ | 文字列 | 詳細情報がある製品ページの URL。 |
| `quantity` | はい | 整数 | カートに入っている製品の個数。 |
| `price` | はい | フロート | 閲覧時の製品のバリアント単価。 |
| `metadata` | いいえ | オブジェクト | 顧客がユースケースのために追加する製品に関する追加のメタデータフィールド。Shopify の場合は SKU が追加されます。<br> 一般的なイベントプロパティの上限である 50KB に基づく制限があります。 |
| `sku` | いいえ | 文字列 | (Shopify のみ) Shopify SKU。これはカタログ ID フィールドとして設定できます。 |
| `source` | はい | 文字列 | イベントの派生元ソース。(Shopify の場合これはストアフロントです。) |
| `order_status_url` | いいえ | 文字列 | 注文のステータスを確認するための URL。 |
| `order_number` | いいえ | 文字列 | (Shopify のみ) 注文の固有の注文番号。 |
| `tags` | いいえ | 配列 | (Shopify のみ) 注文タグ
| `referring_site` | いいえ | 文字列 | (Shopify のみ) 注文の発信元サイト (Meta など)。 |
| `payment_gateway_names` | いいえ | 配列 | (Shopify のみ) 決済システムのソース (POS システムやモバイル端末など)。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### オブジェクトの例

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

| プロパティ名       | 必須 | データタイプ | 説明   |
|---------------|---------|-----------|-------------------------|
| `order_id`            | はい      | 文字列    | 注文の一意の識別子。        |
| `total_value`         | はい      | フロート     | カートの合計金額。    |
| `currency`            | はい      | 文字列    | カートの金額の通貨。    |
| `total_discounts`     | いいえ       | フロート     | 注文に適用された割引の総額。   |
| `discounts`           | いいえ       | オブジェクト配列     | 注文に適用された割引の詳細リスト。 |
| `products`            | はい      | オブジェクト配列     |  |
| `product_id`       | はい      | 文字列    | 閲覧された製品の一意の識別子。この値には、製品 ID、SKU などを使用できます。<br>一部払い戻しが行われ、払い戻しに `product_id` が割り当てられていない場合 (注文レベルの払い戻しなど) には、汎用の `product_id` を指定してください。             |
| `product_name`     | はい      | 文字列    | 閲覧された商品名。                                                                      |
| `variant_id`       | はい      | 文字列    | 製品バリアントの一意の識別子 (`shirt_medium_blue` など)。                                         |
| `image_url`        | いいえ       | 文字列    | 商品画像の URL。     |
| `product_url`      | いいえ       | 文字列    | 詳細情報がある製品ページの URL。  |
| `quantity`         | はい      | 整数   | カートに入っている製品の個数。   |
| `price`            | はい      | フロート     | 閲覧時の製品のバリアント単価。  |
| `metadata`         | いいえ       | オブジェクト    | 顧客がユースケースのために追加する製品に関する追加のメタデータフィールド。Shopify の場合は SKU が追加されます。一般的なイベントプロパティの上限である 50KB に基づく制限があります。 |
| `sku`            | いいえ       | 文字列    | (Shopify のみ) Shopify SKU。これはカタログ ID フィールドとして設定できます。  |
| `source`              | はい      | 文字列    | イベントの派生元ソース。(Shopify の場合これはストアフロントです。)    |
| `metadata`            | いいえ       | オブジェクト    |                |
| `order_status_url`  | いいえ       | 文字列    | 注文のステータスを確認するための URL。     |
| `order_note`       | いいえ       | 文字列    | (Shopify のみ) マーチャントが注文に追加したメモ。    |
| `order_number`     | いいえ       | 文字列    | (Shopify のみ) 注文の固有の注文番号。   |
| `tags`             | いいえ       | 配列     | (Shopify のみ) 注文タグ。  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### オブジェクトの例

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

| プロパティ名      | 必須 | データタイプ | 説明       |
|---------------------|----------|-----------|-------------------|
| `order_id`            | はい      | 文字列    | 注文の一意の識別子。              |
| `cancel_reason`       | はい      | 文字列    | 注文がキャンセルされた理由。           |
| `total_value`         | はい      | フロート     | カートの合計金額。         |
| `currency`            | はい      | 文字列    | カートの金額の通貨。           |
| `total_discounts`     | いいえ       | フロート     | 注文に適用された割引の総額。     |
| `discounts`           | いいえ       | オブジェクト配列     | 注文に適用された割引の詳細リスト。             |
| `products`            | はい      | オブジェクト配列     |         |
| `product_id`          | はい      | 文字列    | 閲覧された製品の一意の識別子。この値には、製品 ID、SKU などを使用できます。             |
| `product_name`        | はい      | 文字列    | 閲覧された商品名。          |
| `variant_id`          | はい      | 文字列    | 製品バリアントの一意の識別子 (`shirt_medium_blue` など)。        |
| `image_url`           | いいえ       | 文字列    | 商品画像の URL。           |
| `product_url`         | いいえ       | 文字列    | 詳細情報がある製品ページの URL。                                                                     |
| `quantity`            | はい      | 整数   | カートに入っている製品の個数。        |
| `price`               | はい      | フロート     | 閲覧時の製品のバリアント単価。     |
| `metadata`            | いいえ       | オブジェクト    | 顧客がユースケースのために追加する製品に関する追加のメタデータフィールド。Shopify の場合は SKU が追加されます。一般的なイベントプロパティの上限である 50KB に基づく制限があります。 |
| `sku`                 | いいえ       | 文字列    | (Shopify のみ) Shopify SKU。これはカタログ ID フィールドとして設定できます。        |
| `source`              | はい      | 文字列    | イベントの派生元ソース。(Shopify の場合これはストアフロントです。)    |
| `metadata`            | いいえ       | オブジェクト    |       |
| `order_status_url`    | いいえ       | 文字列    | 注文のステータスを確認するための URL。                                                                          |
| `order_number`        | いいえ       | 文字列    | (Shopify のみ) 注文の固有の注文番号。  |
| `tags`                | いいえ       | 配列     | (Shopify のみ) 注文タグ。            |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### オブジェクトの例

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

## e コマースキャンバステンプレート

Braze では、e コマースの推奨イベントを活用した事前作成済みのキャンバステンプレートを用意しています (チェックアウトプロセスを開始したが注文前に離脱した顧客のターゲティングなど)。これらのイベントを使用して、メッセージングをパーソナライズしたり、特定のオーディエンスをターゲットにすることで、ユーザージャーニーを向上させるための情報に基づいた意思決定を行うことができます。

キャンバステンプレートでこれらのイベントを使用する方法については、[e コマース専用のユースケース]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/ecommerce_use_cases)をご覧ください。

## ユーザー計算フィールド

以下のフィールドについては、標準化されたユーザーフィールド計算を使用しています。 

- **総収益** = 注文確定額の合計 - 払い戻し金額の合計
- **注文数の合計** = 個別の注文確定イベントの数 - 個別の注文キャンセルの数
- **払い戻し合計額** = 払い戻された注文の合計額 

これらのユーザーフィールド計算は、ユーザープロファイルの [**トランザクション**] タブにも含まれています。

![ユーザー計算フィールドを含む「トランザクション」タブ。]({% image_buster /assets/img/Shopify/transactions_tab.png %}){: style="max-width:70%;"}

## よくある質問

### 製品レベルの購入データはどこで確認できますか？

ユーザープロファイルの [**トランザクション**] タブには、高レベルの計算フィールド (総収益や総注文数など) が表示されます。特定のユーザーに関する製品レベルの詳細を表示するには、[クエリビルダー]({{site.baseurl}}/user_guide/analytics/query_builder/)を使用して e コマースイベントデータをクエリするか、[Currents]({{site.baseurl}}/user_guide/data/braze_currents/) を通じてイベントデータをエクスポートしてください。

従来の購入イベントとは異なり、e コマース推奨イベントでは、商品詳細が `products` 配列内のネストされたイベントプロパティとして保存されます。これらのプロパティは、Liquid によるメッセージングと、[セグメントエクステンション]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/)によるセグメンテーションで利用できます。

### 特定の製品でユーザーをセグメントするにはどうすればよいですか？

セグメンターでは、ユーザーが e コマースイベントを実行した回数でフィルターをかけることができます。特定の製品プロパティ (`product_id` や `product_name` など) でフィルターするには、ネストされたイベントプロパティフィルターをサポートする[セグメントエクステンション]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/)を使用してください。例えば、過去90日間に商品「SKU-123」を購入した全ユーザーを検索できます。

### レガシー購入イベントと e コマース推奨イベントの違いは何ですか？

従来の購入イベントは Braze の[購入オブジェクト]({{site.baseurl}}/api/objects_filters/purchase_object/)を使用し、個々の製品購入を `product_id` と `price` で記録します。e コマース推奨イベント (`ecommerce.order_placed` など) はカスタムイベントプロパティを使用し、複数の製品、割引、メタデータを含む完全な注文コンテキストを単一のイベントでキャプチャします。

e コマースの推奨イベントの導入に伴い、Braze は今後、従来の購入イベントを段階的に廃止していく予定です。現在購入イベントを使用している場合は、事前に通知が届きます。その間、正式な廃止日までは購入イベントを引き続き使用できます。詳細は[推奨イベントの概要]({{site.baseurl}}/user_guide/data/activation/custom_data/recommended_events/)を参照してください。

### e コマースの推奨イベントにカスタムプロパティを追加できますか？

e コマースの推奨イベントには、必須フィールドとオプションフィールドを含む定義済みスキーマがあります。各イベントの `metadata` オブジェクト内に追加のカスタムデータを含めることができます。ただし、カスタム注文レベルのタグや独自フィールド (購入チャネルや小売店情報など) は、最上位のプロパティとしてサポートされていません。セグメンテーションにこれらのフィールドが必要な場合は、e コマースイベントとは別にカスタムイベントとして送信し続けてください。

### e コマースイベントを送信する際に `external_id` を含める必要がありますか？

イベントの送信方法によって異なります。

- **SDK 経由の場合**: いいえ。Braze SDK を使用する場合、イベントは自動的に SDK の現在のユーザーコンテキスト (匿名または識別済みユーザー) に関連付けられます。各イベント呼び出しごとにユーザー識別子を渡す必要はありません。代わりに、`changeUser` などのメソッドを使用してそのコンテキストのユーザーを特定できます。
- **REST API (`/users/track`) 経由の場合**: はい。各 API リクエストには、`external_id`、`braze_id`、`user_alias`、`email`、`phone` などのユーザー識別子を含める必要があります。API には「現在のユーザー」というコンテキストが存在しないためです。

### なぜネストされた製品プロパティが AI レコメンデーション設定のドロップダウンに表示されないのですか？

[AI アイテムレコメンデーション]({{site.baseurl}}/user_guide/brazeai/recommendations/)を設定する際、**プロパティ名**のドロップダウンには最上位のイベントプロパティ (`order_id`、`total_value`、`currency` など) のみが表示されます。`products` 配列内のネストされたプロパティ (`products.product_id` や `products.variant_id` など) はこのリストに表示されない場合がありますが、フィールド内でドット表記を使って手動で入力できます。ほとんどの e コマース実装において、Braze はアイテム識別子として `products.product_id` を使用し、アイテム ID が `product_id` または `variant_id` の値と一致する[カタログ]({{site.baseurl}}/user_guide/data/activation/catalogs/)と組み合わせることを推奨しています。

### なぜ一部の e コマースイベントが Braze に表示されないのですか？

イベントがユーザープロファイルやログに表示されない場合は、以下の点を確認してください。

- **SDK データのフラッシュタイミング**: Braze SDK はデータをローカルにキャッシュし、定期的にアップロードします (通常10〜60秒以内)。即時アップロードを強制するには、`logCustomEvent()` の後に `requestImmediateDataFlush()` を呼び出してください。
- **必須プロパティ**: e コマースイベントには必須のプロパティがあります。必須プロパティが欠けているか、データタイプが無効な場合、イベントは拒否される可能性があります。イベントペイロードが[必須スキーマ](#types-of-ecommerce-recommended-events)と一致していることを確認してください。
- **イベント名の正確性**: e コマースのイベント名は大文字小文字を区別し、完全に一致する必要があります (例: `ecommerce.checkoutStarted` ではなく `ecommerce.checkout_started`)。