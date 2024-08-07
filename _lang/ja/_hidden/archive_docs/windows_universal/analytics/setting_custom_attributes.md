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

Braze には、ユーザーに属性を割り当てるメソッドが用意されています。ダッシュボード上のこれらの属性に従って、ユーザーのフィルター処理とセグメント化を行うことができます。

実装する前に、カスタムイベント、カスタム属性、購入イベントによって提供されるセグメンテーションオプションの例を、[ベストプラクティスで][7]確認してほしい。

ユーザー属性は、現在の`IAppboyUser` に割り当てることができる。現在の`IAppboyUser` への参照を得るには、以下をコールする。 `Appboy.SharedInstance.AppboyUser`

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

デフォルトのユーザー属性だけでなく、Brazeではさまざまなデータタイプを使ってカスタム属性を定義することもできる。セグメンテーションのオプションと、それぞれの属性がどのように影響するかについての詳細は、[ベストプラクティスを]({{site.baseurl}}/developer_guide/platform_integration_guides/windows_universal/analytics/setting_user_ids/#user-id-integration-best-practices-and-notes)参照のこと。

### カスタム属性値を設定する

{% tabs %}
{% tab ブーリアン %}
```csharp
bool SetCustomAttribute(STRING_KEY, BOOL_VALUE);
```
{% endtab %}
{% tab 整数 %}
```csharp
bool SetCustomAttribute(STRING_KEY, INT_VALUE);
```
{% endtab %}
{% tab ダブル/フロート %}
```csharp
bool SetCustomAttribute(STRING_KEY, DOUBLE_VALUE);
```
Braze では、FLOAT 値と DOUBLE 値がデータベースでまったく同じく処理されます。
{% endtab %}
{% tab ストリング %}
```csharp
bool SetCustomAttribute(STRING_KEY, "STRING_VALUE");
```
{% endtab %}
{% tab ロング %}
```csharp
bool SetCustomAttribute(STRING_KEY, LONG_VALUE);
```
{% endtab %}
{% tab 日付 %}
```csharp
bool SetCustomAttribute(STRING_KEY, "DATE_VALUE");
```
>  Brazeに渡される日付は、[ISO 8601][2]形式、e.g `2013-07-16T19:20:30+01:00` 、または`yyyy-MM-dd'T'HH:mm:ss:SSSZ` 形式のいずれかでなければならない。 e.g `2016-12-14T13:32:31.601-0800`
{% endtab %}
{% tab 配列 %}
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

REST API を使用してユーザー属性を設定することもできます。詳細については、[ユーザー API][4] のドキュメントを参照してください。

### カスタム属性値の制限

カスタム属性値の最大長は 255 文字です。これより長い値は切り捨てられます。

## 通知購読ステータスを管理する

ユーザーに購読を設定するために（Eメールまたはプッシュ）、`IAppboyUser` のプロパティとして、以下の購読ステータスを設定することができる。Brazeのサブスクリプションステータスには、メールとプッシュの両方で3つの異なるステータスがある：

| 購読状況 | 定義 |
| ------------------- | ---------- |
| `OptedIn` | 加入し、明示的にオプトインした |
| `Subscribed` | 購読しているが、明示的にオプトインしていない |
| `UnSubscribed` | 配信停止および/または明示的にオプトアウトした |
{: .reset-td-br-1 .reset-td-br-2}

- `EmailNotificationSubscriptionType`
  - ユーザーは、有効なメールアドレスを取得すると自動的に `Subscribed` に設定されます 。ただし、明示的なオプトインのプロセスを確立し、ユーザーから明示的な同意を得た時点でこの値を `OptedIn` に設定することをお勧めします。
- `PushNotificationSubscriptionType`
  - ユーザーは、有効なプッシュ登録時に自動的に`Subscribed` に設定されるが、明示的なオプトイン・プロセスを確立し、ユーザーから明示的な同意を得た時点でこの値を`OptedIn` に設定することを推奨する。

>  これらのタイプは`AppboyPlatform.PCL.Models.NotificationSubscriptionType` に該当する。詳しくは[Managing user subscriptionsを][10]参照のこと。

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/windows_universal/analytics/setting_user_ids/#user-id-integration-best-practices--notes
[2]: http://en.wikipedia.org/wiki/ISO_8601
[4]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
[7]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection
[10]: {{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions
