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

### 設定デフォルト 属性s

デフォルト ユーザー 属性を設定するには、共有`Braze.User` オブジェクトにアプリの適切なフィールドを設定します。以下は名属性の設定例です。

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

### 設定 デフォルト 属性解除

デフォルト ユーザー 属性を設定解除するには、`nil` を該当するメソッドに渡します。

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

デフォルト ユーザー 属性sに加えて、Brazeでは、複数のデータタイプを使用してカスタム属性sを定義することもできます。それぞれの属性のセグメンテーションの詳細については、[ユーザデータ収集]({{site.baseurl}}/developer_guide/analytics/)を参照してください。

{% alert important %}
カスタム属性値の最大長は 255 文字です。これより長い値は切り捨てられます。詳細については、参照してください。
{% endalert %}

### カスタム属性の設定

{% tabs local %}
{% tab string %}
`string` を指定してカスタム属性を設定するには:

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
`integer` を指定してカスタム属性を設定するには:

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
Braze では、データベース内での `float` 値と `double` 値の扱いが同じです。倍精度でカスタム属性を設定するには:

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
`boolean` を指定してカスタム属性を設定するには:

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
`date` を指定してカスタム属性を設定するには:

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
[カスタム属性配列]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#arrays)内の要素の最大数は、デフォルトで 25 に設定されています。要素の最大数を超える配列は、含まれる要素が最大数になるよう切り捨てられます。個々の配列の最大数は、100 まで増やすことができます。この上限を引き上げる場合は、顧客保守マネージャーにお問い合わせください。

`array` を指定してカスタム属性を設定するには:

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

### カスタム属性のインクリメントまたはデクリメント

このコードは、カスタム属性のインクリメントの例です。カスタム属性の値は、`integer` または`long` のいずれかの値だけ増やすことができます。

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

### 設定 カスタム属性解除

{% tabs %}
{% tab swift %}
カスタム属性を設定解除するには、関連する属性鍵を`unsetCustomAttribute` メソッドに渡します。

```swift
AppDelegate.braze?.user.unsetCustomAttribute(key: "your_attribute_key")
```

{% endtab %}
{% tab objective-c %}
カスタム属性を設定解除するには、関連する属性鍵を`unsetCustomAttributeWithKey` メソッドに渡します。

```objc
[AppDelegate.braze.user unsetCustomAttributeWithKey:@"your_attribute_key"];
```

{% endtab %}
{% endtabs %}

### カスタム属性のネスト

カスタム属性s 内にプロパティーをネストすることもできます。次の例では、ネストされたプロパティーを持つ`favorite_book` オブジェクトがユーザープロファイルのカスタム属性として設定されます。詳細については、[ネストされたカスタム属性]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support)を参照してください。

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

REST API を使用して、ユーザー 属性s を設定または設定解除することもできます。詳細については、[ユーザーデータエンドポイント]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data)を参照してください。

## 設定ユーザー サブスクリプションs

ユーザーのサブスクリプション (メールまたはプッシュ) を設定するには、それぞれ関数 `set(emailSubscriptionState:)` または `set(pushNotificationSubscriptionState:)` を呼び出します。これらの関数では、いずれも引数として列挙型 `Braze.User.SubscriptionState` が使用されます。この型には、次の 3 つの状態があります。

| サブスクリプションのステータス | 定義 |
| ------------------- | ---------- |
| `optedIn` | 配信登録済み、かつ明示的にオプトイン済み |
| `subscribed` | 購読済み、ただし明示的に選択されていない |
| `unsubscribed` | 配信停止済みまたは明示的にオプトアウト済み、あるいはその両方 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

アプリにプッシュ通知の送信を許可するユーザーは、iOS で明示的なオプトインが必要であるため、ステータス `optedIn` にデフォルト設定されます。

ユーザーは、有効なメールアドレスを取得すると自動的に `subscribed` に設定されます。ただし、明示的なオプトインのプロセスを確立し、ユーザーから明示的な同意を得た時点でこの値を `optedIn` に設定することをお勧めします。詳細については、「[ユーザーサブスクリプションの管理]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/)」を参照してください。

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
