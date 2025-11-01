{% multi_lang_include developer_guide/prerequisites/flutter.md %}

## デフォルトのユーザー属性

### サポートされている属性

以下の属性がサポートされています。

- 名
- 姓
- 性別
- 生年月日
- 市区町村
- 国
- 電話番号
- 言語
- メール

{% alert important %}
姓、名、国、市区町村などの文字列値はすべて255文字に制限されています。
{% endalert %}

### デフォルト属性の設定 

Brazeが自動的に収集したユーザー属性を設定するには、SDKに付属のセッターメソッドを使用する。

```dart
braze.setFirstName('Name');
```

## カスタムユーザー属性

### カスタム属性の設定

デフォルトのユーザー属性に加え、Brazeでは様々なデータタイプを使用してカスタム属性を定義することができる：

{% tabs %}
{% tab String %}
`string` 、カスタム属性を設定する：

```dart
braze.setStringCustomUserAttribute("custom string attribute", "string custom attribute");
```

{% endtab %}
{% tab 整数 %}
`integer` 、カスタム属性を設定する：

```dart
// Set Integer Attribute
braze.setIntCustomUserAttribute("custom int attribute key", integer);
// Increment Integer Attribute
braze.incrementCustomUserAttribute("key", integer);
```

{% endtab %}
{% tab Double %}
`double` 、カスタム属性を設定する：

```dart
braze.setDoubleCustomUserAttribute("custom double attribute key", double);
```

{% endtab %}
{% tab Boolean %}
`boolean` 、カスタム属性を設定する：

```dart
braze.setBoolCustomUserAttribute("custom boolean attribute key", boolean);
```
{% endtab %}

{% tab 日付 %}
`date` 、カスタム属性を設定する：

```dart
braze.setDateCustomUserAttribute("custom date attribute key", date);
```
{% endtab %}
{% tab 配列 %}
`array` 、カスタム属性を設定する：

```dart
// Adding to an Array
braze.addToCustomAttributeArray("key", "attribute");
// Removing an item from an Array
braze.removeFromCustomAttributeArray("key", "attribute");
```
{% endtab %}
{% endtabs %}

{% alert important %}
カスタム属性値の最大長は 255 文字です。これより長い値は切り捨てられます。
{% endalert %}

### カスタム属性の設定を解除する

カスタム属性を解除するには、`unsetCustomUserAttribute` メソッドに関連する属性キーを渡す。

```dart
braze.unsetCustomUserAttribute('attribute_key');
```
