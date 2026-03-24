{% multi_lang_include developer_guide/prerequisites/unity.md %}

## デフォルトのユーザー属性

### 定義済みのメソッド

Brazeは、`BrazeBinding` オブジェクトを使用して以下のユーザー属性を設定するための定義済みメソッドを提供する。詳しくは[Braze Unity宣言ファイルを](https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/BrazePlatform.cs)参照のこと。

- 名
- 姓
- ユーザーのメールアドレス
- 性別
- 生年月日
- ユーザー国
- ユーザーの市区町村
- ユーザーのメールサブスクリプション
- ユーザプッシュサブスクリプション
- ユーザーの電話番号

### デフォルト属性の設定

デフォルト属性を設定するには、`BrazeBinding` オブジェクトの関連メソッドを呼び出す。

{% tabs local %}
{% tab First name %}
```csharp
BrazeBinding.SetUserFirstName("first name");
```
{% endtab %}
{% tab Last name %}
```csharp
BrazeBinding.SetUserLastName("last name");
```
{% endtab %}
{% tab Email %}
```csharp
BrazeBinding.SetUserEmail("email@email.com");
```
{% endtab %}
{% tab Gender %}
```csharp
BrazeBinding.SetUserGender(Appboy.Models.Gender);
```
{% endtab %}
{% tab Birth date %}
```csharp
BrazeBinding.SetUserDateOfBirth("year(int)", "month(int)", "day(int)");
```
{% endtab %}
{% tab Country %}
```csharp
BrazeBinding.SetUserCountry("country name");
```
{% endtab %}
{% tab Home city %}
```csharp
BrazeBinding.SetUserHomeCity("city name");
```
{% endtab %}
{% tab Email subscription %}
```csharp
BrazeBinding.SetUserEmailNotificationSubscriptionType(AppboyNotificationSubscriptionType);
```
{% endtab %}
{% tab Push subscription %}
```csharp
BrazeBinding.SetUserPushNotificationSubscriptionType(AppboyNotificationSubscriptionType);
```
{% endtab %}
{% tab Phone number %}
```csharp
BrazeBinding.SetUserPhoneNumber("phone number");
```
{% endtab %}
{% endtabs %}

### デフォルト属性の設定を解除する

デフォルトのユーザー属性を解除するには、関連するメソッドに`null` 。

```csharp
BrazeBinding.SetUserFirstName(null);
```

## カスタムユーザー属性

デフォルトのユーザー属性に加え、Brazeではいくつかのデータタイプを使用してカスタム属性を定義することができる。各属性のセグメンテーションオプションの詳細については、[ユーザーデータ収集を]({{site.baseurl}}/developer_guide/analytics)参照のこと。

### カスタム属性の設定

カスタム属性を設定するには、属性タイプに対応するメソッドを使用する： 

{% tabs %}
{% tab String %}

```csharp
AppboyBinding.SetCustomUserAttribute("custom string attribute key", "string custom attribute");
```

{% endtab %}

{% tab Integer %}

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

{% tab Date %}

```csharp
AppboyBinding.SetCustomUserAttributeToNow("custom date attribute key");
```

```csharp
AppboyBinding.SetCustomUserAttributeToSecondsFromEpoch("custom date attribute key", 'integer value');
```

{% alert note %}
Brazeに渡される日付は、[ISO 8601](http://en.wikipedia.org/wiki/ISO_8601)形式（`2013-07-16T19:20:30+01:00` など）か、`yyyy-MM-dd'T'HH:mm:ss:SSSZ` 形式（`2016-12-14T13:32:31.601-0800` など）でなければならない。
{% endalert %}

{% endtab %}

{% tab Array %}

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

### カスタム属性の設定を解除する

カスタム属性を解除するには、`UnsetCustomUserAttribute` メソッドに関連する属性キーを渡す。 

```csharp
AppboyBinding.UnsetCustomUserAttribute("custom attribute key");
```

### REST API の使用

また、REST APIを使用して、ユーザー属性を設定または解除することもできる。詳細については、[ユーザーデータエンドポイント]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data)を参照してください。

## ユーザーサブスクリプションの設定

ユーザーにメールまたはプッシュサブスクリプションを設定するには、以下のいずれかの機能を呼び出す。

```csharp
// Email notifications
AppboyBinding.SetUserEmailNotificationSubscriptionType()

// Push notifications
AppboyBinding.SetPushNotificationSubscriptionType()`
```

どちらの関数も引数として`Appboy.Models.AppboyNotificationSubscriptionType` 、3つの異なる状態を持つ：

| サブスクリプション ステータス | 定義 |
| ------------------- | ---------- |
| `OPTED_IN` | 配信登録済み、かつ明示的にオプトイン済み |
| `SUBSCRIBED` | 購読済み、ただし明示的に選択されていない |
| `UNSUBSCRIBED` | 配信停止済みまたは明示的にオプトアウト済み、あるいはその両方 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Windows では、ユーザーにプッシュ通知を送る際に明示的なオプトインは必要ありません。ユーザーがプッシュ登録されると、デフォルトで `OPTED_IN` ではなく `SUBSCRIBED` に設定されます。詳細については、[ サブスクリプションs と明示的なopt-ins]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions) の実装に関するドキュメントを参照してください。
{% endalert %}

| サブスクリプション・タイプ                        | 説明 |
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
