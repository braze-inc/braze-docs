---
nav_title: カスタム属性の設定
article_title: Unityのカスタム属性の設定
platform: 
  - Unity
  - iOS
  - Android
page_order: 2
description: "このリファレンス記事では、Unityプラットフォームでカスタム属性を設定および設定解除する方法について説明します。"

---

# カスタム属性の設定

> Braze では、ユーザーに属性を割り当てるメソッドが提供されています。ダッシュボード上のこれらの属性に従って、ユーザーのフィルター処理とセグメント化を行うことができます。

実装前に、[ベストプラクティス][1]記事のカスタムイベント、カスタム属性、および購入イベントで提供されるセグメンテーションオプションの例を確認してください。

## デフォルトユーザー属性の割り当て

ユーザ属性を割り当てるには、BrazeBinding オブジェクトで適切なメソッドを呼び出す必要があります。以下は、このメソッドを使用して呼び出すことができる組み込み属性のリストです。

### 名
`AppboyBinding.SetUserFirstName("first name");`

### 姓
`AppboyBinding.SetUserLastName("last name");`

### ユーザーのメールアドレス
`AppboyBinding.SetUserEmail("email@email.com");`

>  Brazeを介してメールを送信していなくても、メールアドレスを設定することはまだ価値があります。電子メールを使用すると、個々のユーザープロファイルを検索しやすくなり、問題が発生したときにトラブルシューティングが容易になります。

### 性別
`AppboyBinding.SetUserGender(Appboy.Models.Gender);`

### 生年月日
`AppboyBinding.SetUserDateOfBirth("year(int)", "month(int)", "day(int)");`

### ユーザー国
`AppboyBinding.SetUserCountry("country name");`

### ユーザーホームシティ
`AppboyBinding.SetUserHomeCity("city name");`

### ユーザメールサブスクリプション
`AppboyBinding.SetUserEmailNotificationSubscriptionType(AppboyNotificationSubscriptionType);`

### ユーザープッシュサブスクリプション
`AppboyBinding.SetUserPushNotificationSubscriptionType(AppboyNotificationSubscriptionType);`

### USER\_PHONE\_NUMBER
`AppboyBinding.SetUserPhoneNumber("phone number");`

## カスタムユーザー属性の割り当て

Braze では、デフォルトユーザー属性以外にも、複数の異なるデータ型を使用してカスタム属性を定義できます。
これらの各属性のセグメンテーションオプションの詳細については、このセクションの["Best Practices" documentation][1] を参照してください。

### カスタム属性値を設定する

{% tabs %}
{% tab Boolean Value %}

```csharp
AppboyBinding.SetCustomUserAttribute("custom boolean attribute key", 'boolean value');
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
{% tab String %}

```csharp
AppboyBinding.SetCustomUserAttribute("custom string attribute key", "string custom attribute");
```

{% endtab %}
{% tab Date %}

```csharp
AppboyBinding.SetCustomUserAttributeToNow("custom date attribute key");
```

```csharp
AppboyBinding.SetCustomUserAttributeToSecondsFromEpoch("custom date attribute key", 'integer value');
```

>  Braze に渡される日付は、[ISO 8601][2] 形式、たとえば`2013-07-16T19:20:30+01:00` または`yyyy-MM-dd'T'HH:mm:ss:SSSZ` 形式のいずれかである必要があります `2016-12-14T13:32:31.601-0800`

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
{% endtabs
%}
### カスタム属性の設定解除

カスタム属性は、次のメソッドを使用して設定を解除することもできます。

```csharp
AppboyBinding.UnsetCustomUserAttribute("custom attribute key");
```

## REST API によるカスタム属性の設定
REST API を使用してユーザー属性を設定することもできます。これを行うには、[ユーザー API のドキュメントを][3]参照してください。

## カスタム属性値の制限
カスタム属性値の最大長は 255 文字です。これより長い値は切り捨てられます。

## ユーザーサブスクリプションの設定

ユーザのサブスクリプションを設定するには(メールまたはプッシュのいずれか)、関数を呼び出します     
`AppboyBinding.SetUserEmailNotificationSubscriptionType()` または`AppboyBinding.SetPushNotificationSubscriptionType()`。これらの関数はどちらも引数としてパラメータ`Appboy.Models.AppboyNotificationSubscriptionType` を取ります。この型には、次の 3 つの状態があります。

| サブスクリプションステータス | 定義 |
| ------------------- | ---------- |
| `OPTED_IN` | 配信登録済み、かつ明示的にオプトイン済み |
| `SUBSCRIBED` | 配信登録済みだが、明示的なオプトインは未実行 |
| `UNSUBSCRIBED` | 配信停止済みまたは明示的にオプトアウト済み、あるいはその両方 |
{: .reset-td-br-1 .reset-td-br-2}

>  Windowsでは、ユーザーにプッシュ通知を送信するために明示的なオプトインは必要ありません。ユーザーがプッシュ登録されると、デフォルトで`OPTED_IN`ではなく`SUBSCRIBED`に設定されます。詳細については、[サブスクリプションと明示的なopt-ins][10] の実装に関するドキュメントを参照してください。

- `EmailNotificationSubscriptionType`
  - 有効なメールアドレスを受信すると、ユーザは自動的に`SUBSCRIBED` に設定されます。ただし、明示的なオプトインプロセスを確立し、ユーザーから明示的な同意を受け取った時点でこの値を`OPTED_IN` に設定することをお勧めします。詳細については、[ユーザーサブスクリプションの変更][8]のドキュメントを参照してください。
- `PushNotificationSubscriptionType`
  - ユーザは、有効なプッシュ登録時に自動的に`SUBSCRIBED` に設定されます。ただし、明示的なオプトインプロセスを確立し、ユーザーから明示的な同意を受け取った時点でこの値を`OPTED_IN` に設定することをお勧めします。詳細については、[ユーザーサブスクリプションの変更][8]のドキュメントを参照してください。

>  これらの型は `Appboy.Models.AppboyNotificationSubscriptionType` に属します

## サンプルコード

### Email, Subscription

```csharp
AppboyBinding.SetUserEmailNotificationSubscriptionType(AppboyNotificationSubscriptionType.OPTED_IN);
```

### プッシュ通知サブスクリプション

```csharp
AppboyBinding.SetUserPushNotificationSubscriptionType(AppboyNotificationSubscriptionType.OPTED_IN);
```

[1]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection
[2]: http://en.wikipedia.org/wiki/ISO_8601
[3]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
[8]: {{site.baseurl}}/user_guide/administrative/manage_your_users/managing_user_subscriptions/#changing-subscriptions
[10]: {{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions
