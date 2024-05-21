---
nav_title: 分析
article_title: Flutter の分析
platform: Flutter
page_order: 5
description: "この記事では、Flutter アプリでの基本的な分析の設定および追跡方法について説明します。"

---
 
# Flutter 分析

> この記事では、Flutter アプリでの基本的な分析の設定方法と追跡方法について説明します。

始める前に、[分析の概要][0]の記事を読んで、Braze 分析の詳細と、デフォルトで追跡されている内容を確認してください。また、[イベントの命名規則][1]についてもよく理解しておくことをお勧めします。

## セッショントラッキング

Braze SDK では、ユーザーエンゲージメントやユーザーの理解に不可欠なその他の分析を計算するため、Braze ダッシュボードで使用されるセッションデータがレポートされます。SDK では、以下のセッションセマンティクスに基づいて、Braze ダッシュボード内で表示可能なセッションの長さとセッション数を考慮した「セッション開始」と「セッション終了」のデータポイントが生成されます。

ユーザー ID を設定したり、セッションを開始したりするには、ユーザー ID パラメーターを受け取る `changeUser` メソッドを使用します。

```dart
braze.changeUser('user_id');
```

## カスタムイベントを記録する

Braze でカスタムイベントを記録することで、アプリの使用パターンについて詳しく知ることができ、ダッシュボードでの行動によってユーザーを分類できます。

```dart
braze.logCustomEvent('my_custom_event');
```

カスタムイベントで properties オブジェクトを渡すことによって、イベントに関するメタデータを追加できます。

```dart
braze.logCustomEvent('custom_event_with_properties', properties: {
    'key1': 'value1',
    'key2': ['value2', 'value3'],
    'key3': false,
});
```

## カスタム属性を記録する

Braze では、ユーザーに属性を割り当てるメソッドが提供されています。ダッシュボードでこれらの属性に基づき、ユーザーをフィルターおよびセグメント化できます。

### デフォルトのユーザー属性

Braze が自動収集したユーザー属性を割り当てるには、SDK に付属のセッターメソッドを使用します。

```dart
braze.setFirstName('Name');
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

### カスタム属性値を設定する

Braze では、デフォルトユーザー属性以外にも、複数の異なるデータ型を使用してカスタム属性を定義できます。

{% tabs %}
{% tab Boolean Value %}

```dart
braze.setBoolCustomUserAttribute("custom boolean attribute key", boolean);
```

{% endtab %}
{% tab Integer %}

```dart
// Set Integer Attribute
braze.setIntCustomUserAttribute("custom int attribute key", integer);
// Increment Integer Attribute
braze.incrementCustomUserAttribute("key", integer);
```

{% endtab %}
{% tab Double %}
```dart
braze.setDoubleCustomUserAttribute("custom double attribute key", double);
```

{% endtab %}
{% tab String %}

```dart
braze.setStringCustomUserAttribute("custom string attribute", "string custom attribute");
```

{% endtab %}
{% tab Date %}

```dart
braze.setDateCustomUserAttribute("custom date attribute key", date);
```
{% endtab %}
{% tab Array %}

```dart
// Adding to an Array
braze.addToCustomAttributeArray("key", "attribute");
// Removing an item from an Array
braze.removeFromCustomAttributeArray("key", "attribute");
```
{% endtab %}
{% endtabs %}

### カスタム属性の設定解除

```dart
braze.unsetCustomUserAttribute('attribute_key');
```

## 購入のロギング

アプリ内での購入を記録して、売上を経時的にトラッキングしたり、売上源を横断してトラッキングしたりできます。また、ユーザーを生涯価値でセグメント化することもできます。

Braze は複数の通貨での購入に対応しています。米ドル以外の通貨でレポートする購入は、レポートされた日付の為替レートに基づいて米ドル単位でダッシュボードに表示されます。

```dart
braze.logPurchase(productId, currencyCode, price, quantity, properties: properties);
```

以下に例を示します。

```dart
braze.logPurchase('product_id', 'USD', 9.99, 1, properties: {
    'key1': 'value'
});
```

{% alert tip %}
値 `10 USD` と数量 `3` を渡すと、10 ドルの購入 3 件、合計 30 ドルがユーザープロファイルに記録されます。数量は 100 以下でなければなりません。購入額がマイナスになることもあります。
{% endalert %}

### 注文レベルで購入を記録する
商品レベルではなく、注文レベルで購入を記録したい場合、注文名または注文カテゴリを `product_id` として使用できます。詳細については、[購入オブジェクトの仕様]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions)を参照してください。 

### 予約済みのキー

以下のキーは予約されているため、購入プロパティとして使用できません。

- `time`
- `product_id`
- `quantity`
- `event_name`
- `price`
- `currency`

[0]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/
[1]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/
