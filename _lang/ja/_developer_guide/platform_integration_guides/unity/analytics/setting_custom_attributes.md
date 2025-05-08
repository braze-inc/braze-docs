---
nav_title: カスタム属性の設定
article_title: Unityのカスタム属性の設定
platform: 
  - Unity
  - iOS
  - Android
page_order: 2
description: "このリファレンス記事では、Unity プラットフォームでカスタム属性を設定および設定解除する方法について説明します。"

---

# カスタム属性の設定

> Braze では、ユーザーに属性を割り当てるメソッドが提供されています。ダッシュボードでこれらの属性に基づき、ユーザーをフィルターおよびセグメント化できます。

実施にあたっては、まずカスタムイベントs、カスタム属性s、購買イベントが提供するセグメンテーション選択肢の事例を[ベストプラクティス][1]で検討すること。

## デフォルトユーザー属性の割り当て

ユーザー属性を割り当てるには、共有 BrazeBinding オブジェクトで適切なメソッドを呼び出す必要があります。以下は、このメソッドを使用して呼び出すことができる組み込み属性s の一覧です。

### 名
`AppboyBinding.SetUserFirstName("first name");`

### 姓
`AppboyBinding.SetUserLastName("last name");`

### ユーザーのメールアドレス
`AppboyBinding.SetUserEmail("email@email.com");`

>  Braze 経由でメールを送信していない場合でも、メールアドレスを設定しておくと便利です。電子メールを使用すると、個々のユーザープロファイルの検索や問題の発生時のトラブルシューティングが容易になります。

### 性別
`AppboyBinding.SetUserGender(Appboy.Models.Gender);`

### 生年月日
`AppboyBinding.SetUserDateOfBirth("year(int)", "month(int)", "day(int)");`

### ユーザー国
`AppboyBinding.SetUserCountry("country name");`

### ユーザーの市区町村
`AppboyBinding.SetUserHomeCity("city name");`

### ユーザーのメールサブスクリプション
`AppboyBinding.SetUserEmailNotificationSubscriptionType(AppboyNotificationSubscriptionType);`

### ユーザプッシュサブスクリプション
`AppboyBinding.SetUserPushNotificationSubscriptionType(AppboyNotificationSubscriptionType);`

### ユーザーの電話番号
`AppboyBinding.SetUserPhoneNumber("phone number");`

## カスタムユーザー属性の割り当て

Braze では、デフォルトユーザー属性以外にも、複数の異なるデータ型を使用してカスタム属性を定義できます。
これらの各属性で使用できるセグメンテーションオプションの詳細については、このセクション内の「[ベストプラクティス][1]」ドキュメントを参照してください。

### カスタム属性値を設定する

{% tabs %}
{% tab ブール値 %}

```csharp
AppboyBinding.SetCustomUserAttribute("custom boolean attribute key", 'boolean value');
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
{% tab String %}

```csharp
AppboyBinding.SetCustomUserAttribute("custom string attribute key", "string custom attribute");
```

{% endtab %}
{% tab 日付 %}

```csharp
AppboyBinding.SetCustomUserAttributeToNow("custom date attribute key");
```

```csharp
AppboyBinding.SetCustomUserAttributeToSecondsFromEpoch("custom date attribute key", 'integer value');
```

>  Braze に渡される日付は、[ISO 8601][2] 形式、e.g `2013-07-16T19:20:30+01:00`、または`yyyy-MM-dd'T'HH:mm:ss:SSSZ` 形式のいずれかである必要があります e.g `2016-12-14T13:32:31.601-0800`

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
{% endtabs
%}
### カスタム属性の設定解除

カスタム属性は、次のメソッドを使用して設定を解除することもできます。

```csharp
AppboyBinding.UnsetCustomUserAttribute("custom attribute key");
```

## REST API によるカスタム属性の設定
REST API を使用してユーザー属性を設定することもできます。そのためには、[ ユーザー API ドキュメント][3] を参照してください。

## カスタム属性値の制限
カスタム属性値の最大長は 255 文字です。これより長い値は切り捨てられます。

## ユーザーサブスクリプションの設定

ユーザーのサブスクリプション (メールまたはプッシュ) を設定するには、以下の関数を呼び出します。     
それぞれ `AppboyBinding.SetUserEmailNotificationSubscriptionType()` または`AppboyBinding.SetPushNotificationSubscriptionType()`。これらの関数はどちらも引数としてパラメータ`Appboy.Models.AppboyNotificationSubscriptionType` を取ります。この型には、次の 3 つの状態があります。

| サブスクリプションのステータス | 定義 |
| ------------------- | ---------- |
| `OPTED_IN` | 配信登録済み、かつ明示的にオプトイン済み |
| `SUBSCRIBED` | 購読済み、ただし明示的に選択されていない |
| `UNSUBSCRIBED` | 配信停止済みまたは明示的にオプトアウト済み、あるいはその両方 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

>  Windows では、ユーザーにプッシュ通知を送る際に明示的なオプトインは必要ありません。ユーザーがプッシュ登録されると、デフォルトで `OPTED_IN` ではなく `SUBSCRIBED` に設定されます。詳細については、[ サブスクリプションs と明示的なopt-ins][10] の実装に関するドキュメントを参照してください。

- `EmailNotificationSubscriptionType`
  - 有効なメールアドレスを受信すると、ユーザは自動的に`SUBSCRIBED` に設定されます。ただし、明示的なオプトインプロセスを確立し、ユーザーから明示的な同意を受け取ったときにこの値を`OPTED_IN` に設定することをお勧めします。詳細については、[ユーザーサブスクリプションの変更][8]のドキュメントを参照してください。
- `PushNotificationSubscriptionType`
  - ユーザは、有効なプッシュ登録時に自動的に`SUBSCRIBED` に設定されます。ただし、明示的なオプトインプロセスを確立し、ユーザーから明示的な同意を受け取ったときにこの値を`OPTED_IN` に設定することをお勧めします。詳細については、[ユーザーサブスクリプションの変更][8]のドキュメントを参照してください。

>  これらのタイプは `Appboy.Models.AppboyNotificationSubscriptionType` に属します

## サンプルコード

### メールサブスクリプション:

```csharp
AppboyBinding.SetUserEmailNotificationSubscriptionType(AppboyNotificationSubscriptionType.OPTED_IN);
```

### プッシュ通知 サブスクリプション:

```csharp
AppboyBinding.SetUserPushNotificationSubscriptionType(AppboyNotificationSubscriptionType.OPTED_IN);
```

[1]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection
[2]: http://en.wikipedia.org/wiki/ISO_8601
[3]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
[8]: {{site.baseurl}}/user_guide/administrative/manage_your_users/managing_user_subscriptions/#changing-subscriptions
[10]: {{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions
