---
nav_title: カスタム属性の設定
article_title: Windows Universalのカスタム属性を設定する
platform: Windows Universal
page_order: 3
description: "このリファレンス記事では、Windowsユニバーサルプラットフォームでカスタム属性を設定する方法について説明する。"
hidden: true
---

# カスタム属性の設定
{% multi_lang_include archive/windows_deprecation.md %}

Braze には、ユーザーに属性を割り当てるメソッドが用意されています。ダッシュボードでこれらの属性に基づき、ユーザーをフィルターおよびセグメント化できます。

実施にあたっては、まずカスタムイベント、カスタム属性、購買イベントが提供するセグメンテーション選択肢の事例を[ベストプラクティス]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection)で検討してください。

ユーザー属性は、現在の`IAppboyUser` に割り当てることができる。現在の`IAppboyUser` への参照を取得するには、`Appboy.SharedInstance.AppboyUser` を呼び出します。

## デフォルトユーザー属性の割り当て

以下の属性は、`IAppboyUser` のプロパティとして定義されるべきである：

- `FirstName`
- `LastName`
- `Email`
- `Gender`
- `DateOfBirth`
- `Country`
- `HomeCity`
- `PhoneNumber`

**実施例**

```csharp
Appboy.SharedInstance.AppboyUser.FirstName = "User's First Name"
```

## カスタムユーザー属性の割り当て

デフォルトのユーザー属性だけでなく、Brazeではさまざまなデータタイプを使ってカスタム属性を定義することもできる。セグメンテーションオプションの詳細と、これらの属性のそれぞれがどのように影響するかについては、[ベストプラクティス]({{site.baseurl}}/developer_guide/platform_integration_guides/windows_universal/analytics/setting_user_ids/#user-id-integration-best-practices-and-notes)を参照してください。

### カスタム属性値を設定する

{% tabs %}
{% tab Boolean %}
```csharp
bool SetCustomAttribute(STRING_KEY, BOOL_VALUE);
```
{% endtab %}
{% tab Integer %}
```csharp
bool SetCustomAttribute(STRING_KEY, INT_VALUE);
```
{% endtab %}
{% tab Double or Float %}
```csharp
bool SetCustomAttribute(STRING_KEY, DOUBLE_VALUE);
```
Braze では、FLOAT 値と DOUBLE 値がデータベースでまったく同じく処理されます。
{% endtab %}
{% tab String %}
```csharp
bool SetCustomAttribute(STRING_KEY, "STRING_VALUE");
```
{% endtab %}
{% tab Long %}
```csharp
bool SetCustomAttribute(STRING_KEY, LONG_VALUE);
```
{% endtab %}
{% tab Date %}
```csharp
bool SetCustomAttribute(STRING_KEY, "DATE_VALUE");
```
>  Braze に渡される日付は、[ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) 形式、e.g `2013-07-16T19:20:30+01:00`、または`yyyy-MM-dd'T'HH:mm:ss:SSSZ` 形式のいずれかである必要があります e.g `2016-12-14T13:32:31.601-0800`
{% endtab %}
{% tab Array %}
```csharp
// Setting a custom attribute with an array value
Appboy.SharedInstance.EventLogger.SetCustomAttributeArray("custom_attribute_array_test", testSetArray);
// Adding to a custom attribute with an array value
Appboy.SharedInstance.EventLogger.AddToCustomAttributeArray("custom_attribute_array_test", testAddString);
// Removing a value from an array type custom attribute
Appboy.SharedInstance.EventLogger.RemoveFromCustomAttributeArray("custom_attribute_array_test", testRemString);
```
{% endtab %}
{% endtabs %}

### カスタム属性のインクリメント / デクリメント

このコードは、インクリメントカスタム属性の例です。カスタム属性の値は、正または負の整数値でインクリメントできます。

```csharp
bool IncrementCustomAttribute(STRING_KEY, INCREMENT_INTEGER_VALUE);
```

### カスタム属性の設定解除

カスタム属性は、次のメソッドを使用して設定を解除することもできます。

```csharp
bool UnsetCustomAttribute(STRING_KEY);
```

### REST API によるカスタム属性の設定

REST API を使用してユーザー属性を設定することもできます。詳細については、[ユーザー API]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data) のドキュメントを参照してください。

### カスタム属性値の制限

カスタム属性値の最大長は 255 文字です。これより長い値は切り捨てられます。

## 通知サブスクリプションのステータスを管理する

ユーザーにサブスクリプション (メールまたはプッシュ) を設定するには、`IAppboyUser` のプロパティとして、以下のサブスクリプションステータスを設定できます。Braze のサブスクリプションステータスには、メールとプッシュの両方で3つの異なるステータスがあります。

| サブスクリプションのステータス | 定義 |
| ------------------- | ---------- |
| `OptedIn` | 配信登録済み、かつ明示的にオプトイン済み |
| `Subscribed` | 購読済み、ただし明示的に選択されていない |
| `UnSubscribed` | 配信停止済みまたは明示的にオプトアウト済み、あるいはその両方 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

- `EmailNotificationSubscriptionType`
  - ユーザーは、有効なメールアドレスを取得すると自動的に `Subscribed` に設定されます 。ただし、明示的なオプトインのプロセスを確立し、ユーザーから明示的な同意を得た時点でこの値を `OptedIn` に設定することをお勧めします。
- `PushNotificationSubscriptionType`
  - ユーザーは、有効なプッシュ登録時に自動的に`Subscribed` に設定されるが、明示的なオプトイン・プロセスを確立し、ユーザーから明示的な同意を得た時点でこの値を`OptedIn` に設定することを推奨する。

>  これらのタイプは `AppboyPlatform.PCL.Models.NotificationSubscriptionType` に属します。詳細については、「[ユーザーサブスクリプションの管理]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions)」を参照してください。

