---
nav_title: 分析
article_title: React Native 向け分析
platform: React Native
page_order: 5
description: "この記事では、React Native アプリで、セッショントラッキングやカスタムイベントのロギングなど、基本的な分析をセットアップして追跡する方法を説明します。"

---
 
# React Native による分析

> この記事では、React Native アプリで基本的な分析を設定し、追跡する方法を説明します。

始める前に、[分析の概要]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/)の記事を読んで、Braze 分析の詳細と、デフォルトで追跡されている内容を確認してください。また、[イベントの命名規則]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/)についてもよく理解しておくことをお勧めします。

## セッショントラッキング

Braze SDK は、Braze ダッシュボードで使用されるセッションデータをレポートし、ユーザーエンゲージメントや、ユーザーを理解するために不可欠なその他の分析を計算します。以下のセッションセマンティクスに基づき、SDK は、Braze ダッシュボード内で表示可能なセッションの長さとセッション数を考慮した「セッション開始」と「セッション終了」のデータポイントを生成します。

ユーザー ID を設定したり、セッションを開始したりするには、ユーザー ID パラメーターを受け取る `changeUser` メソッドを使用します。

```javascript
Braze.changeUser("user_id");
```

## カスタムイベントのログ記録

Braze でカスタムイベントを記録することで、アプリの使用パターンについて詳しく知ることができ、ダッシュボードでの行動によってユーザーを分類できます。

```javascript
Braze.logCustomEvent("react_native_custom_event");
```

カスタムイベントで properties オブジェクトを渡すことによって、イベントに関するメタデータを追加できます。

```javascript
Braze.logCustomEvent("custom_event_with_properties", {
    key1: "value1",
    key2: ["value2", "value3"],
    key3: false,
});
```

## カスタム属性を記録する

Braze では、ユーザーに属性を割り当てるメソッドが提供されています。ダッシュボードでこれらの属性に基づき、ユーザーをフィルターおよびセグメント化できます。

### デフォルトのユーザー属性

Braze が自動収集したユーザー属性を割り当てるには、SDK に付属のセッターメソッドを使用します。

```javascript
Braze.setFirstName("Name");
```

以下の属性がサポートされています。

- 名
- 姓
- 性別
- 生年月日
- 市区町村
- 国
- 電話番号
- 言語
- メールアドレス

姓、名、国、市区町村などの文字列値はすべて255文字に制限されています。

### カスタムユーザー属性

Braze は、定義済みのユーザー属性メソッドに加えて、アプリケーションからのデータを追跡するための[カスタム属性]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types)も提供しています。 

```javascript
Braze.setCustomUserAttribute("attribute_key", "attribute_value", function(){
    // optional onResult callback
});
```

#### カスタム属性の設定解除


```javascript
Braze.unsetCustomUserAttribute("attribute_key", function(){
    // optional onResult callback
});
```

#### カスタム属性配列

```javascript

// Adds a string to a custom atttribute string array, or creates that array if one doesn't exist.
Braze.addToCustomUserAttributeArray("my-attribute-array", "new or existing value", optionalCallback);

// Removes a string from a custom attribute string array.


Braze.removeFromCustomUserAttributeArray("my-attribute-array", "existing value", optionalCallback);
```

## 購入のロギング

アプリ内での購入を記録して、売上を経時的にトラッキングしたり、売上源を横断してトラッキングしたりできます。また、ユーザーを生涯価値でセグメント化することもできます。

Braze は複数の通貨での購入に対応しています。米ドル以外の通貨でレポートする購入は、レポートされた日付の為替レートに基づいて米ドル単位でダッシュボードに表示されます。

```javascript
Braze.logPurchase(productId, price, currencyCode, quantity, properties);
```

以下に例を示します。

```javascript
Braze.logPurchase("product_id", 9.99, "USD", 1, {
    key1: "value"
});
```

{% alert tip %}
値 `10 USD` と数量 `3` を渡すと、10 ドルの購入 3 件、合計 30 ドルがユーザープロファイルに記録されます。数量は 100 以下でなければなりません。購入額がマイナスになることもあります。
{% endalert %}

### 注文レベルで購入を記録する
商品レベルではなく、注文レベルで購入を記録したい場合、注文名または注文カテゴリを `product_id` として使用できます。詳細については、[購入オブジェクトの仕様]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions)を参照してください。 

### 予約済みのキー

以下のキーは**予約されている**ため、購入プロパティとして使用**できません**。

- `time`
- `product_id`
- `quantity`
- `event_name`
- `price`
- `currency`

