---
nav_title: "購入オブジェクト"
article_title: API購入オブジェクト
page_order: 8
page_type: reference
description: "この参考記事では、購入オブジェクトのさまざまなコンポーネント、正しい使用方法、参考となる例について説明します。"

---

# 購入対象

> この記事では、購入オブジェクトのさまざまなコンポーネント、正しい使用方法、ベストプラクティス、参考となる例について説明します。

## 購入オブジェクトとは何ですか？

購入オブジェクトは、購入が行われたときにAPIを通じて渡されるオブジェクトです。各購入オブジェクトは購入配列内にあり、各オブジェクトは特定のユーザーが特定の時間に行った単一の購入です。購入オブジェクトにはさまざまなフィールドがあり、Braze のバックエンドはこの情報を保存して、カスタマイズ、データ収集、パーソナライゼーションに使用できます。

### オブジェクト本体

```json
{
  // One of "external_id" or "user_alias" or "braze_id" or "email" or "phone" is required.
  "external_id" : (optional, string) External user ID,
  "user_alias" : (optional, User Alias Object) User alias object,
  "braze_id" : (optional, string) Braze user identifier,
  "email": (optional, string) User email address,
  "phone": (optional, string) User phone number,
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
- [ISO 4217 通貨コード Wiki](http://en.wikipedia.org/wiki/ISO_4217)
- [ISO 8601 時間コード Wiki](https://en.wikipedia.org/wiki/ISO_8601)

## 購入製品 ID

購入オブジェクト内では、`product_id` は購入の識別子です (`Product Name` や `Product Category` など)。

- Braze では、ダッシュボードに最大 5,000 個の `product_id` を保存できます。
- `product_id` は最大 255 文字までです。

### 命名規則

Brazeでは、購入オブジェクト`product_id`の一般的な命名規則を提供しています。`product_id` を選択する場合、Braze は、記録されたすべての項目をこの `product_id` でグループ化することを目的として、(SKU ではなく) 製品名や製品カテゴリなどの単純な名前を使用することを提案します。

これにより、製品をセグメンテーションとトリガーのために識別しやすくなります。

### 注文レベルでの購入記録

商品レベルではなく、注文レベルで購入を記録したい場合は、注文名または注文カテゴリを `product_id` (`Online Order` や `Completed Order` など) として使用できます。

Web SDK で注文レベルの購入を記録する例は以下のとおりです。

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

## プロパティオブジェクトを購入

カスタムイベントと購入にはイベントプロパティが含まれる場合があります。「プロパティ」値は、キーがプロパティ名で値がプロパティ値であるオブジェクトである必要があります。プロパティ名は、255 文字以下の空でない文字列でなければならず、先頭にドル記号は使用できません。 

プロパティ値は、次のデータ型のいずれでもかまいません。

| データ型 | 説明 |
| --- | --- |
| 数値 | [整数](https://en.wikipedia.org/wiki/Integer)または[浮動小数点数として](https://en.wikipedia.org/wiki/Floating-point_arithmetic) |
| ブール値 |  |
| 日時 | [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)または`yyyy-MM-dd'T'HH:mm:ss:SSSZ` 形式の文字列としてフォーマットされる。アレイ内ではサポートされていない。 |
| 文字列 | 255 文字以下。 |
| 配列 | 配列に日時を含めることはできない。 |
| オブジェクト | オブジェクトは文字列として取り込まれます。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

配列またはオブジェクト値を含むイベントプロパティオブジェクトには、最大 50 KB のイベントプロパティペイロードを設定できます。

### 購入プロパティ

[購入プロパティ]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events/#purchase-properties)は、Liquid を使用したメッセージのトリガーやパーソナライゼーションに使用でき、これらのプロパティに基づいてセグメント化することもできます。

#### 命名規則

この機能は購入ごとではなく、**製品ごとに**有効であることに注意することが重要です。例えば、個別の製品が大量にあったとしても、それぞれの特性が同じである場合、セグメンテーションは不要になる可能性があります。

この例では、データ構造を設定する際には、詳細なものではなく、「グループレベル」で製品名を使用することをお勧めします。例えば、トレーニングチケット企業では、「片道」、「往復」、「複数市区町村」の製品を持つべきであり、「取引123」や「取引046」などの特定の取引ではありません。または、たとえば、「食べ物」の購入イベントでは、プロパティは「ケーキ」と「サンドイッチ」に設定するのが最適です。

{% alert important %}
Braze REST API を使用して製品を追加することができます。例えば、`/users/track` エンドポイントに呼び出しを送信し、新しい購入 ID を含めると、ダッシュボードの [**データ設定**] > [**製品**] セクションに製品が自動的に作成されます。
{% endalert %}

### 購入オブジェクトの例

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

### 購入オブジェクト、イベントオブジェクト、およびwebhook

提供された例を使用すると、誰かが色、モノグラム、チェックアウト期間、サイズ、およびブランドのプロパティを持つバックパックを購入したことがわかります。次に、[購入イベントプロパティ]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events/#purchase-properties)を使用してこれらのプロパティを持つセグメントを作成したり、Liquidを使用してチャネルを通じてカスタムメッセージを送信したりできます。例えば、「こんにちは **Ann F.**、**赤のミディアムバックパック** を購入していただきありがとうございます。価格は **$40.00** です！」お買い物は**Backpack Locker**でありがとうございました！

セグメント化に使用するプロパティを保存、保管、追跡する場合は、それらをカスタム属性として設定する必要があります。これは[セグメントエクステンション]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/)を使用して行うことができ、カスタムイベントやそのユーザープロファイルの生涯にわたって保存される購入行動に基づいてユーザーをターゲットにすることができます。


