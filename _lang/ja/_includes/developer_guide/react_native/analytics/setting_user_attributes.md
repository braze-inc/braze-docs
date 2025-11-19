{% multi_lang_include developer_guide/prerequisites/react_native.md %}

## カスタム属性を記録する

Braze では、ユーザーに属性を割り当てるメソッドが提供されています。ダッシュボードでこれらの属性に基づき、ユーザーをフィルターおよびセグメント化できます。

### デフォルトのユーザー属性

Brazeが自動収集したユーザー属性を設定するには、SDK付属のセッターメソッドを使用する。

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

#### カスタム属性の設定を解除する

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
