{% multi_lang_include developer_guide/prerequisites/flutter.md %}

## デフォルトのユーザー属性

Brazeによって自動的に収集されるユーザー属性を設定するには、SDKに付属のsetterメソッドを使用します。

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
- メール

{% alert important %}
姓、名、国、市区町村などの文字列値はすべて255文字に制限されています。
{% endalert %}

## カスタムユーザー属性

### カスタム属性の設定

Braze では、デフォルトのユーザー属性に加えて、さまざまなデータ型を使用してカスタム属性を定義することもできます。

{% tabs %}
{% tab String %}
`string` 値を使用してカスタム属性を設定するには:

```dart
braze.setStringCustomUserAttribute("custom string attribute", "string custom attribute");
```

{% endtab %}
{% tab 整数 %}
`integer` 値を使用してカスタム属性を設定するには:

```dart
// Set Integer Attribute
braze.setIntCustomUserAttribute("custom int attribute key", integer);
// Increment Integer Attribute
braze.incrementCustomUserAttribute("key", integer);
```

{% endtab %}
{% tab Double %}
`double` 値を使用してカスタム属性を設定するには:

```dart
braze.setDoubleCustomUserAttribute("custom double attribute key", double);
```

{% endtab %}
{% tab Boolean %}
`boolean` 値を使用してカスタム属性を設定するには:

```dart
braze.setBoolCustomUserAttribute("custom boolean attribute key", boolean);
```
{% endtab %}

{% tab 日付 %}
`date` 値を使用してカスタム属性を設定するには:

```dart
braze.setDateCustomUserAttribute("custom date attribute key", date);
```
{% endtab %}
{% tab 配列 %}
`array` 値を使用してカスタム属性を設定するには:

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

### カスタム属性の設定解除

```dart
braze.unsetCustomUserAttribute('attribute_key');
```
