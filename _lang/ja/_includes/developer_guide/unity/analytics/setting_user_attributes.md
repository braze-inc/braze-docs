{% multi_lang_include developer_guide/prerequisites/unity.md %}

## デフォルトのユーザー属性

ユーザ属性を設定するには、`BrazeBinding` オブジェクトで適切なメソッドを呼び出す必要があります。以下は、このメソッドを使用して呼び出すことができる組み込み属性s の一覧です。

| 属性                 | コードサンプル |
|---------------------------|-------------|
| 名                | `AppboyBinding.SetUserFirstName("first name");` |
| 姓                 | `AppboyBinding.SetUserLastName("last name");` |
| ユーザーのメールアドレス                | `AppboyBinding.SetUserEmail("email@email.com");` |
| 性別                    | `AppboyBinding.SetUserGender(Appboy.Models.Gender);` |
| 生年月日                | `AppboyBinding.SetUserDateOfBirth("year(int)", "month(int)", "day(int)");` |
| ユーザー国              | `AppboyBinding.SetUserCountry("country name");` |
| ユーザーの市区町村            | `AppboyBinding.SetUserHomeCity("city name");` |
| ユーザーのメールサブスクリプション   | `AppboyBinding.SetUserEmailNotificationSubscriptionType(AppboyNotificationSubscriptionType);` |
| ユーザプッシュサブスクリプション    | `AppboyBinding.SetUserPushNotificationSubscriptionType(AppboyNotificationSubscriptionType);` |
| ユーザーの電話番号         | `AppboyBinding.SetUserPhoneNumber("phone number");` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## カスタムユーザー属性

デフォルトのユーザー属性に加えて、Braze では複数の異なるデータ型を使用してカスタム属性を定義することもできます。各属性のセグメンテーションオプションの詳細については、[ユーザーデータ収集]({{site.baseurl}}/developer_guide/analytics)を参照してください。

### カスタム属性の設定

{% tabs %}
{% tab String %}

```csharp
AppboyBinding.SetCustomUserAttribute("custom string attribute key", "string custom attribute");
```

{% endtab %}

{% tab 整数 %}

```csharp
// Set Integer Attribute
AppboyBinding.SetCustomUserAttribute("custom int attribute key", 'integer value');
// Increment Integer Attribute
AppboyBinding.IncrementCustomUserAttribute("key", increment(int))
```
{% endtab %}

{% tab Double %}

```csharp
AppboyBinding.SetCustomUserAttribute("custom double attribute key", 'double value');
```

{% endtab %}

{% tab Boolean %}

```csharp
AppboyBinding.SetCustomUserAttribute("custom boolean attribute key", 'boolean value');
```
{% endtab %}

{% tab 日付 %}

```csharp
AppboyBinding.SetCustomUserAttributeToNow("custom date attribute key");
```

```csharp
AppboyBinding.SetCustomUserAttributeToSecondsFromEpoch("custom date attribute key", 'integer value');
```

{% alert note %}
Braze に渡される日付は、[ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) 形式(`2013-07-16T19:20:30+01:00` など) または`yyyy-MM-dd'T'HH:mm:ss:SSSZ` 形式(`2016-12-14T13:32:31.601-0800` など) のいずれかである必要があります。
{% endalert %}

{% endtab %}

{% tab 配列 %}

```csharp
// Setting An Array
AppboyBinding.SetCustomUserAttributeArray("key", array(List), sizeOfTheArray(int))
// Adding to an Array
AppboyBinding.AddToCustomUserAttributeArray("key", "Attribute")
// Removing an item from an Array
AppboyBinding.RemoveFromCustomUserAttributeArray("key", "Attribute")
```
{% endtab %}
{% endtabs %}

{% alert important %}
カスタム属性値の最大長は 255 文字です。これより長い値は切り捨てられます。
{% endalert %}

### カスタム属性の設定解除

カスタムユーザー属性を設定解除するには、次の方法を使用します。

```csharp
AppboyBinding.UnsetCustomUserAttribute("custom attribute key");
```

### REST API の使用

REST API を使用して、ユーザー属性を設定または設定解除することもできます。詳細については、[User Data Endpoints]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data)を参照してください。

## ユーザーサブスクリプションの設定

ユーザのメールサブスクリプションまたはプッシュサブスクリプションを設定するには、次のいずれかの関数を呼び出します。

```csharp
// Email notifications
AppboyBinding.SetUserEmailNotificationSubscriptionType()

// Push notifications
AppboyBinding.SetPushNotificationSubscriptionType()`
```

どちらの関数も引数として`Appboy.Models.AppboyNotificationSubscriptionType` を取ります。これは3 つの異なる状態を持ちます。

| サブスクリプション ステータス | 定義 |
| ------------------- | ---------- |
| `OPTED_IN` | 配信登録済み、かつ明示的にオプトイン済み |
| `SUBSCRIBED` | 購読済み、ただし明示的に選択されていない |
| `UNSUBSCRIBED` | 配信停止済みまたは明示的にオプトアウト済み、あるいはその両方 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Windows では、ユーザーにプッシュ通知を送る際に明示的なオプトインは必要ありません。ユーザーがプッシュ登録されると、デフォルトで `OPTED_IN` ではなく `SUBSCRIBED` に設定されます。詳細については、[ サブスクリプションs と明示的なopt-ins]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions) の実装に関するドキュメントを参照してください。
{% endalert %}

| サブスクリプションタイプ                        | 説明 |
|------------------------------------------|-------------|
| `EmailNotificationSubscriptionType`      | 有効なメールアドレスを受信すると、ユーザは自動的に`SUBSCRIBED` に設定されます。ただし、明示的なオプトインプロセスを確立し、ユーザーから明示的な同意を受け取ったときにこの値を`OPTED_IN` に設定することをお勧めします。詳細については、[ユーザーサブスクリプションの変更]({{site.baseurl}}/user_guide/administrative/manage_your_users/managing_user_subscriptions/#changing-subscriptions)のドキュメントを参照してください。 |
| `PushNotificationSubscriptionType`       | ユーザは、有効なプッシュ登録時に自動的に`SUBSCRIBED` に設定されます。ただし、明示的なオプトインプロセスを確立し、ユーザーから明示的な同意を受け取ったときにこの値を`OPTED_IN` に設定することをお勧めします。詳細については、[ユーザーサブスクリプションの変更]({{site.baseurl}}/user_guide/administrative/manage_your_users/managing_user_subscriptions/#changing-subscriptions)のドキュメントを参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
これらのタイプは `Appboy.Models.AppboyNotificationSubscriptionType` に属します。
{% endalert %}

### メールサブスクリプションの設定

```csharp
AppboyBinding.SetUserEmailNotificationSubscriptionType(AppboyNotificationSubscriptionType.OPTED_IN);
```

### プッシュ通知サブスクリプションの設定

```csharp
AppboyBinding.SetUserPushNotificationSubscriptionType(AppboyNotificationSubscriptionType.OPTED_IN);
```
