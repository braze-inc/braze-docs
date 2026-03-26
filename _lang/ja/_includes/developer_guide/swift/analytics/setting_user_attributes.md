{% multi_lang_include developer_guide/prerequisites/swift.md %}

## デフォルトのユーザー属性

### サポートされている属性

`Braze.User` オブジェクトでは、以下の属性を設定する必要があります。

- `firstName`
- `lastName`
- `email`
- `dateOfBirth`
- `country`
- `language`
- `homeCity`
- `phone`
- `gender`

### デフォルト属性の設定

デフォルトのユーザー属性を設定するには、共有 `Braze.User` オブジェクトの適切なフィールドを設定します。以下は名属性の設定例です。

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.set(firstName: "Alex")
```

{% endtab %}
{% tab objective-c %}

```objc
[AppDelegate.braze.user setFirstName:@"Alex"];
```

{% endtab %}
{% endtabs %}

### デフォルト属性の解除

デフォルトのユーザー属性を解除するには、関連するメソッドに `nil` を渡します。

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.set(firstName: nil)
```

{% endtab %}
{% tab objective-c %}

```objc
[AppDelegate.braze.user setFirstName:nil];
```

{% endtab %}
{% endtabs %}

## カスタムユーザー属性

デフォルトのユーザー属性に加えて、Braze では複数の異なるデータタイプを使用してカスタム属性を定義することもできます。各属性のセグメンテーションオプションの詳細については、[ユーザーデータ収集]({{site.baseurl}}/developer_guide/analytics/)を参照してください。

{% alert important %}
カスタム属性値の最大長は 255 文字です。これより長い値は切り捨てられます。詳細については、[`Braze.User`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class) を参照してください。
{% endalert %}

### カスタム属性の設定

{% tabs local %}
{% tab string %}
`string` 値でカスタム属性を設定するには：

{% subtabs %}
{% subtab swift %}
```swift
AppDelegate.braze?.user.setCustomAttribute(key: "your_attribute_key", value: "your_attribute_value")
```
{% endsubtab %}

{% subtab objective-c %}
```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" stringValue:"your_attribute_value"];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab integer %}
`integer` 値でカスタム属性を設定するには：

{% subtabs %}
{% subtab swift %}
```swift
AppDelegate.braze?.user.setCustomAttribute(key: "your_attribute_key", value: yourIntegerValue)
```
{% endsubtab %}

{% subtab objective-c %}
```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" andIntegerValue:yourIntegerValue];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab floating-points %}
Braze では、データベース内での `float` 値と `double` 値の扱いが同じです。倍精度値でカスタム属性を設定するには：

{% subtabs %}
{% subtab swift %}
```swift
AppDelegate.braze?.user.setCustomAttribute(key: "your_attribute_key", value: yourDoubleValue)
```
{% endsubtab %}

{% subtab objective-c %}
```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" andDoubleValue:yourDoubleValue];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab boolean %}
`boolean` 値でカスタム属性を設定するには：

{% subtabs %}
{% subtab swift %}
```swift
AppDelegate.braze?.user.setCustomAttribute("your_attribute_key", value: yourBoolValue)
```
{% endsubtab %}

{% subtab objective-c %}
```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" andBOOLValue:yourBOOLValue];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab date %}
`date` 値でカスタム属性を設定するには：

{% subtabs %}
{% subtab swift %}
```swift
AppDelegate.braze?.user.setCustomAttribute("your_attribute_key", dateValue:yourDateValue)
```
{% endsubtab %}

{% subtab objective-c %}
```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" andDateValue:yourDateValue];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab array %}
配列内の要素のデフォルトおよび最大数は 500 です。最大数は Braze ダッシュボードの**データ設定** > **カスタム属性**で更新できます。要素の最大数を超える配列は、最大数に切り捨てられます。

`array` 値でカスタム属性を設定するには：

{% subtabs %}
{% subtab swift %}
```swift
// Setting a custom attribute with an array value
AppDelegate.braze?.user.setCustomAttributeArray(key: "array_name", array: ["value1",  "value2"])
// Adding to a custom attribute with an array value
AppDelegate.braze?.user.addToCustomAttributeArray(key: "array_name", value: "value3")
// Removing a value from an array type custom attribute
AppDelegate.braze?.user.removeFromCustomAttributeArray(key: "array_name", value: "value2")
```
{% endsubtab %}

{% subtab objective-c %}
```objc
// Setting a custom attribute with an array value
[AppDelegate.braze.user setCustomAttributeArrayWithKey:@"array_name" array:@[@"value1",  @"value2"]];
// Adding to a custom attribute with an array value
[AppDelegate.braze.user addToCustomAttributeArrayWithKey:@"array_name" value:@"value3"];
// Removing a value from an array type custom attribute
[AppDelegate.braze.user removeFromCustomAttributeArrayWithKey:@"array_name" value:@"value2"];
// Removing an entire array and key
[AppDelegate.braze.user setCustomAttributeArrayWithKey:@"array_name" array:nil];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### カスタム属性の増減

このコードは、カスタム属性のインクリメントの例です。カスタム属性の値は、任意の `integer` または `long` の値で増加させることができます。

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.incrementCustomUserAttribute(key: "your_attribute_key", by: incrementIntegerValue)
```

{% endtab %}
{% tab objective-c %}

```objc
[AppDelegate.braze.user incrementCustomUserAttribute:@"your_attribute_key" by:incrementIntegerValue];
```

{% endtab %}
{% endtabs %}

### カスタム属性の設定解除

{% tabs %}
{% tab swift %}
カスタム属性を解除するには、該当する属性キーを `unsetCustomAttribute` メソッドに渡します。

```swift
AppDelegate.braze?.user.unsetCustomAttribute(key: "your_attribute_key")
```

{% endtab %}
{% tab objective-c %}
カスタム属性を解除するには、該当する属性キーを `unsetCustomAttributeWithKey` メソッドに渡します。

```objc
[AppDelegate.braze.user unsetCustomAttributeWithKey:@"your_attribute_key"];
```

{% endtab %}
{% endtabs %}

### 階層化カスタム属性

カスタム属性内にプロパティをネストすることもできます。次の例では、ネストされたプロパティを持つ `favorite_book` オブジェクトが、ユーザープロファイルのカスタム属性として設定されます。詳細については、[階層化カスタム属性]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support)を参照してください。

{% tabs %}
{% tab swift %}
```swift
let favoriteBook: [String: Any?] = [
  "title": "The Hobbit",
  "author": "J.R.R. Tolkien",
  "publishing_date": "1937"
]

braze.user.setCustomAttribute(key: "favorite_book", dictionary: favoriteBook)
```
{% endtab %}

{% tab objective-c %}
```objc
NSDictionary *favoriteBook = @{
  @"title": @"The Hobbit",
  @"author": @"J.R.R. Tolkien",
  @"publishing_date": @"1937"
};

[AppDelegate.braze.user setCustomAttributeWithKey:@"favorite_book" dictionary:favoriteBook];
```
{% endtab %}
{% endtabs %}

### REST API の使用

ユーザー属性を設定または解除するには、REST API も利用できます。詳細については、[ユーザーデータエンドポイント]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data)を参照してください。

## ユーザーサブスクリプションの設定

ユーザーのサブスクリプション（メールまたはプッシュ）を設定するには、それぞれ関数 `set(emailSubscriptionState:)` または `set(pushNotificationSubscriptionState:)` を呼び出します。これらの関数では、いずれも引数として列挙型 `Braze.User.SubscriptionState` が使用されます。この型には、次の 3 つの状態があります。

| サブスクリプションのステータス | 定義 |
| ------------------- | ---------- |
| `optedIn` | 配信登録済み、かつ明示的にオプトイン済み |
| `subscribed` | 購読中、ただし明示的にオプトイン済みではない |
| `unsubscribed` | 配信停止済みまたは明示的にオプトアウト済み、あるいはその両方 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

アプリにプッシュ通知の送信を許可したユーザーは、iOS で明示的なオプトインが必要であるため、デフォルトでステータスが `optedIn` に設定されます。

ユーザーは、有効なメールアドレスを受信すると自動的に `subscribed` に設定されます。ただし、明示的なオプトインのプロセスを確立し、ユーザーから明示的な同意を得た時点でこの値を `optedIn` に設定することをお勧めします。詳細については、「[ユーザーサブスクリプションの管理]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/)」を参照してください。

### メールサブスクリプションの設定

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.set(emailSubscriptionState: Braze.User.SubscriptionState)
```

{% endtab %}
{% tab objective-c %}

```objc
[AppDelegate.braze.user setEmailSubscriptionState: BRZUserSubscriptionState]
```

{% endtab %}
{% endtabs %}

### プッシュ通知サブスクリプションの設定

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.set(pushNotificationSubscriptionState: Braze.User.SubscriptionState)
```

{% endtab %}
{% tab objective-c %}

```objc
[AppDelegate.braze.user setPushNotificationSubscriptionState: BRZUserSubscriptionState]
```

{% endtab %}
{% endtabs %}

詳細については、「[ユーザーサブスクリプションの管理]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/)」を参照してください。