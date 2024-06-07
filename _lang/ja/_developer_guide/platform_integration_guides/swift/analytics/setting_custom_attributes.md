---
nav_title: カスタム属性の設定
article_title: iOS のカスタム属性の設定
platform: Swift
page_order: 3
description: "このリファレンス記事では、Swift SDK のカスタム属性を設定する方法を説明します。"

---

# カスタム属性の設定

> Braze では、ユーザーに属性を割り当てるメソッドが提供されています。ダッシュボードでこれらの属性に基づき、ユーザーをフィルターおよびセグメント化できます。

実装前に、[ベストプラクティス][1]のカスタムイベント、カスタム属性、および購入イベントによって提供されるセグメンテーションオプションの例と、[イベント命名規則]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/)のメモを必ず確認してください。

## デフォルトユーザー属性の割り当て

ユーザー属性を割り当てるには、共有 `ABKUser` オブジェクトで適切なフィールドを設定する必要があります。

以下は名属性の設定例です。

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.set(firstName: "first_name")
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
[AppDelegate.braze.user setFirstName:@"first_name"];
```

{% endtab %}
{% endtabs %}

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

## カスタムユーザー属性の割り当て

Braze では、デフォルトユーザー属性以外にも、複数の異なるデータタイプを使用してカスタム属性を定義できます。これらの各属性で提供されるセグメンテーションオプションの詳細については、[ユーザーデータ収集]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/)を参照してください。

### 文字列値のカスタム属性

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.setCustomAttribute(key: "your_attribute_key", value: "your_attribute_value")
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" stringValue:"your_attribute_value"];
```

{% endtab %}
{% endtabs %}

### 整数値のカスタム属性

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.setCustomAttribute(key: "your_attribute_key", value: yourIntegerValue)
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" andIntegerValue:yourIntegerValue];
```

{% endtab %}
{% endtabs %}

### double 値のカスタム属性

Braze では、`float` 値と `double` 値がデータベース内で同じく処理されます。

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.setCustomAttribute(key: "your_attribute_key", value: yourDoubleValue)
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" andDoubleValue:yourDoubleValue];
```

{% endtab %}
{% endtabs %}

### ブール値のカスタム属性

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.setCustomAttribute("your_attribute_key", value: yourBoolValue)
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" andBOOLValue:yourBOOLValue];
```

{% endtab %}
{% endtabs %}

### 日付値のカスタム属性

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.setCustomAttribute("your_attribute_key", dateValue:yourDateValue)
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" andDateValue:yourDateValue];
```

{% endtab %}
{% endtabs %}

### 配列値のカスタム属性

[カスタム属性配列][8]内の要素の最大数は、25にデフォルト設定されています。要素の最大数を超える配列は、含まれる要素が最大数になるよう切り捨てられます。個別の配列の最大数は、100まで増やすことができます。この最大数を増やす必要がある場合は、カスタマーサービスマネージャーに連絡してください。 


{% tabs %}
{% tab swift %}

```swift
// Setting a custom attribute with an array value
AppDelegate.braze?.user.setCustomAttributeArray(key: "array_name", array: ["value1",  "value2"])
// Adding to a custom attribute with an array value
AppDelegate.braze?.user.addToCustomAttributeArray(key: "array_name", value: "value3")
// Removing a value from an array type custom attribute
AppDelegate.braze?.user.removeFromCustomAttributeArray(key: "array_name", value: "value2")
```

{% endtab %}
{% tab OBJECTIVE-C %}

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

{% endtab %}
{% endtabs %}

### カスタム属性の設定解除

カスタム属性は、次のメソッドを使用して設定を解除することもできます。

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.unsetCustomAttribute(key: "your_attribute_key")
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
[AppDelegate.braze.user unsetCustomAttributeWithKey:@"your_attribute_key"];
```

{% endtab %}
{% endtabs %}

### インクリメント/デクリメントカスタム属性

このコードは、インクリメントカスタム属性の例です。カスタム属性の値は、正または負の整数か、long 値でインクリメントできます。

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.incrementCustomUserAttribute(key: "your_attribute_key", by: incrementIntegerValue)
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
[AppDelegate.braze.user incrementCustomUserAttribute:@"your_attribute_key" by:incrementIntegerValue];
```

{% endtab %}
{% endtabs %}

### REST API によるカスタム属性の設定

REST API を使用してユーザー属性を設定することもできます。詳細については、[ユーザー API のドキュメント][3]を参照してください。

### カスタム属性値の制限

カスタム属性値の最大長は 255 文字です。これより長い値は切り捨てられます。

#### 追加情報

- 詳細については、[`Braze.User` のドキュメント][6]を参照してください。

## ユーザーサブスクリプションの設定

ユーザーのサブスクリプション (メールまたはプッシュ) を設定するには、それぞれ関数 `set(emailSubscriptionState:)` または `set(pushNotificationSubscriptionState:)` を呼び出します。これらの関数では、いずれも引数として列挙型 `Braze.User.SubscriptionState` が使用されます。この型には、次の3つの状態があります。

| サブスクリプションステータス | 定義 |
| ------------------- | ---------- |
| `optedIn` | サブスクリプション登録済み、かつ明示的にオプトイン済み |
| `subscribed` | サブスクリプション登録済み、ただし明示的なオプトイン未実行 |
| `unsubscribed` | 配信停止済みおよび/または明示的にオプトアウト済み |
{: .reset-td-br-1 .reset-td-br-2}

アプリにプッシュ通知の送信を許可するユーザーは、iOS で明示的なオプトインが必要であるため、ステータス `optedIn` にデフォルト設定されます。

ユーザーは、有効なメールアドレスを取得すると自動的に `subscribed` に設定されます 。ただし、明示的なオプトインのプロセスを確立し、ユーザーから明示的な同意を得た時点でこの値を `optedIn` に設定することをお勧めします。詳細については、「[ユーザーサブスクリプションの管理]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/)」を参照してください。

### メールサブスクリプションの設定

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.set(emailSubscriptionState: Braze.User.SubscriptionState)
```

{% endtab %}
{% tab OBJECTIVE-C %}

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
{% tab OBJECTIVE-C %}

```objc
[AppDelegate.braze.user setPushNotificationSubscriptionState: BRZUserSubscriptionState]
```

{% endtab %}
{% endtabs %}

詳細については、「[ユーザーサブスクリプションの管理]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/)」を参照してください。

[1]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection
[2]: http://en.wikipedia.org/wiki/ISO_8601
[3]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
[6]: https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class
[8]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#arrays
[10]: {{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions
[12]: {{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions
