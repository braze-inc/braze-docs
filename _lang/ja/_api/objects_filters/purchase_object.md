---
nav_title: "購入オブジェクト"
article_title: API 購入オブジェクト
page_order: 8
page_type: reference
description: "このリファレンス記事では、購入オブジェクトのさまざまなコンポーネント、正しく使用する方法、および使用例について説明します。"

---

# 購入対象

> この記事では、購入オブジェクトのさまざまなコンポーネント、正しく使用する方法、ベストプラクティス、およびそこから引き出す例について説明します。

## 購入対象とは。

購入オブジェクトは、購入が行われたときにAPI を通過するオブジェクトです。各購入オブジェクトは、購入アレイ内に配置され、各オブジェクトは、特定の時点での特定のユーザによる単一購入となります。購入オブジェクトには、Braze のバックエンドがカスタマイズ、データ収集、パーソナライズのためにこの情報を保存して使用できるようにするさまざまな項目があります。

### オブジェクト本体

```json
{
  // One of "external_id" or "user_alias" or "braze_id" or "email" is required.
  "external_id" : (optional, string) External user ID,
  "user_alias" : (optional, User Alias Object) User alias object,
  "braze_id" : (optional, string) Braze user identifier,
  "email": (optional, string) User email address,
  "app_id" : (optional, string) see App Identifier,
  // See the following product_id naming conventions for clarification.
  "product_id" : (required, string) identifier for the purchase, for example, Product Name or Product Category,
  "currency" : (required, string) ISO 4217 Alphabetic Currency Code,
  //Revenue from a purchase object is calculated as the product of quantity and price.
  "price" : (required, float) value in the base currency unit (for example, Dollars for USD, Yen for JPY),
  "quantity" : (optional, integer) the quantity purchased (defaults to 1, must be <= 100 -- currently, Braze treats a quantity _X_ as _X_ separate purchases with quantity 1),
  "time" : (required, datetime as string in ISO 8601) Time of purchase,
  // See the following purchase object explanation for clarification.
  "properties" : (optional, Properties Object) properties of the event,
  // Setting this flag to true will put the API in "Update Only" mode.
  // When using a "user_alias", "Update Only" mode is always true.
  "_update_existing_only" : (optional, boolean)
}
```

- [外部ユーザ ID]({{site.baseurl}}/api/basics/#user-ids)
- [アプリ識別子]({{site.baseurl}}/api/identifier_types/)
- [ISO 4217通貨コードWiki][20]
- [ISO 8601タイムコードWiki][22]

## Purchase product\_id

購入オブジェクト内では、`product_id` は購入の識別子です(`Product Name` や`Product Category` など)。

- Braze では、最大5000 `product_id`s をダッシュボードに保存できます。
- `product_id` は最大255 文字です。

### 製品IDの命名規則

Braze では、購入オブジェクト`product_id` の一般的な命名規則をいくつか提供しています。`product_id` を選択した場合、Braze は、ログに記録されたすべてのアイテムをこの`product_id` でグループ化する目的で、製品名や製品カテゴリ(SKU ではなく) などの単純な名前を使用することを推奨します。

これにより、製品がセグメンテーションとトリガーを識別しやすくなります。

### 注文レベルでの購買履歴

製品レベルではなく注文レベルで購入を記録する場合は、`product_id` として注文名または注文カテゴリを使用できます(`Online Order` または`Completed Order` など)。

たとえば、Web SDK の注文レベルで購入を記録するには、次のようにします。

```html
POST https://YOUR_REST_API_URL/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "purchases" : [
    {
      "external_id" : "user1",
      "app_id" : "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id" : "Completed Order",
      "currency" : "USD",
      "price" : 219.98,
      "time" : "2013-07-16T19:20:30+01:00",
      "properties" : {
        "products" : [ { "name": "Monitor", "category": "Gaming", "product_amount": 19.99, },
        { "name": "Gaming Keyboard", "category": "Gaming ", "product_amount": 199.99, }
        ]
      }
    }
  ]
}
```

## 購買物件オブジェクト

カスタムイベントおよび購入には、イベントプロパティがある場合があります。"properties"値は、キーがプロパティ名であり、値がプロパティ値であるオブジェクトである必要があります。プロパティ名は、255 文字以下の空でない文字列で、先頭にドル記号が付いていない必要があります。 

プロパティ値には、次のデータ型のいずれかを指定できます。

| データ型| 説明|
| --- | --- |
| 数値| [整数](https://en.wikipedia.org/wiki/Integer) または[floats](https://en.wikipedia.org/wiki/Floating-point_arithmetic) |
| ブール値| |
| 日時| [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) または`yyyy-MM-dd'T'HH:mm:ss:SSSZ` 形式の文字列としてフォーマットされます。配列内ではサポートされません。|
| 文字列| 255 文字以下|
| 配列| 配列に日時を含めることはできません。|
| オブジェクト| オブジェクトは文字列として取り込まれます。|
{: .reset-td-br-1 .reset-td-br-2}

配列またはオブジェクト値を含むイベント・プロパティ・オブジェクトは、最大50KBのイベント・プロパティ・ペイロードを持つことができます。

### 購入プロパティ

[購入プロパティ]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events/#purchase-properties) を使用して、メッセージをトリガしたり、Liquid を使用してパーソナライズしたりすることができます。また、これらのプロパティに基づいてセグメント化することもできます。

### 購入プロパティの命名規則

この機能は、購入ごとではなく、製品 ごとに** 有効になっていることに注意してください。たとえば、顧客が異なる製品を大量に持っていても、それぞれが同じ特性を持っている場合、セグメンテーションはむしろ無意味になる。

この場合、データ構造を設定するときに、粒度の細かいものではなく、"group-level"で製品名を使用することをお勧めします。例えば、列車チケット会社は、"single trip"、"return trip"、"、&multi-city"の製品を持つべきであり、"transaction 123"または"transaction 046"のような特定の取引ではない。または、購入イベント"food"では、プロパティは"cake"および"sandwich"として設定するのが最適です。

### 購入対象例
```html
POST https://YOUR_REST_API_URL/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "purchases" : [
    {
      "external_id" : "user1",
      "app_id" : "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id" : "backpack",
      "currency" : "USD",
      "price" : 40.00,
      "time" : "2013-07-16T19:20:30+01:00",
      "properties" : {
        "color" : "red",
        "monogram" : "ABC",
        "checkout_duration" : 180,
        "size" : "Large",
        "brand" : "Backpack Locker"
      }
    },
    {
      "external_id" : "user1",
      "app_id" : "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id" : "pencil",
      "currency" : "USD",
      "price" : 2.00,
      "time" : "2013-07-17T19:20:20+01:00",
      "properties" : {
        "number" : 2,
        "sharpened" : true
      }
    },
    {
      "user_alias" : { "alias_name" : "device123", "alias_label" : "my_device_identifier"},
      "app_id" : "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id" : "pen",
      "currency" : "USD",
      "price" : 2.50,
      "time" : "2013-07-17T19:20:20+01:00",
      "properties" : {
        "color" : "blue",
      }
    }
  ]
}
```

## オブジェクト、イベントオブジェクト、およびウェブフックを購入する

提供された例を使えば、誰かが、カラー、モノグラム、チェックアウト期間、サイズ、ブランドのプロパティを持つバックパックを購入したことがわかります。次に、[購入イベントプロパティ][2] を使用してこれらのプロパティを持つセグメントを作成するか、Liquid を使用してチャネル経由でカスタムメッセージを送信できます。たとえば、"Hello **Ann F.**, that **red, medium backpack** for **$40.00** をお買い上げいただきありがとうございます。**Backpack Locker**!&quotでお買い物いただきありがとうございます;

プロパティをセグメントに保存、保存、追跡する場合は、カスタム属性として設定する必要があります。これは、[Segment Extensions]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/) を使用して実行できます。これにより、ユーザプロファイルの存続期間中に保存されたカスタムイベントまたは購入動作に基づいて、ユーザをターゲットにすることができます。

[2]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events/#purchase-properties
[20]: http://en.wikipedia.org/wiki/ISO_4217 "ISO 4217通貨コード"
[21]: {{site.baseurl}}/api/api_key/#the-app-identifier-api-key
[22]: https://en.wikipedia.org/wiki/ISO_8601 "ISO 8601タイムコード"
[23]: {{site.baseurl}}/api/basics/#external-user-id-explanation
