---
nav_title: カスタム属性の設定
article_title: Windows Universalのカスタム属性の設定
platform: Windows Universal
page_order: 3
description: "このリファレンス記事では、Windowsユニバーサルプラットフォームでカスタム属性を設定する方法について説明します。"
hidden: true
---

# カスタム属性の設定
{% multi_lang_include archive/windows_deprecation.md %}

Brazeは、ユーザーに属性を割り当てるメソッドを提供します。ダッシュボードでは、これらの属性に従ってユーザーをフィルタリングし、セグメント化することができます。

実装する前に、カスタムイベント、カスタム属性、購入イベントによって提供されるセグメンテーションオプションの例を、[ベストプラクティスで][7]確認してください。

ユーザー属性は、現在の`IAppboyUser` に割り当てることができる。現在の`IAppboyUser` への参照を得るには、以下を呼び出す。 `Appboy.SharedInstance.AppboyUser`

## デフォルトのユーザー属性の割り当て

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

デフォルトのユーザー属性だけでなく、Brazeではさまざまなデータタイプを使用してカスタム属性を定義することもできます。セグメンテーションのオプションと、それぞれの属性がどのように影響するかについての詳細は、[ベストプラクティスを]({{site.baseurl}}/developer_guide/platform_integration_guides/windows_universal/analytics/setting_user_ids/#user-id-integration-best-practices-and-notes)ご覧ください。

### カスタム属性値の設定

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
{% tab Double/Float %}
```csharp
bool SetCustomAttribute(STRING_KEY, DOUBLE_VALUE);
```
Brazeのデータベースでは、FLOAT値とDOUBLE値はまったく同じように扱われます。
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
>  Brazeに渡される日付は、[ISO 8601][2]形式（例：`2013-07-16T19:20:30+01:00` ）または`yyyy-MM-dd'T'HH:mm:ss:SSSZ` 形式（例： ）のいずれかでなければなりません。 `2016-12-14T13:32:31.601-0800`
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

### カスタム属性のインクリメント／デクリメント

このコードはインクリメント・カスタム属性の例である。カスタム属性の値は、正または負の整数値でインクリメントすることができます。

```csharp
bool IncrementCustomAttribute(STRING_KEY, INCREMENT_INTEGER_VALUE);
```

### カスタム属性の設定解除

カスタム属性は、以下の方法で設定を解除することもできる：

```csharp
bool UnsetCustomAttribute(STRING_KEY);
```

### REST APIによるカスタム属性の設定

また、REST APIを使用してユーザー属性を設定することもできます。詳細については、[ユーザーAPIの][4]ドキュメントを参照のこと。

### カスタム属性値の制限

カスタム属性の値の長さは最大255文字です。

## 通知購読ステータスの管理

ユーザーに購読を設定するために（電子メールまたはプッシュのいずれか）、`IAppboyUser` のプロパティとして以下の購読ステータスを設定することができます。Brazeのサブスクリプションステータスには、メールとプッシュの両方で3つの異なるステータスがあります：

| サブスクリプション・ステータス
| ------------------- | ---------- |
|`OptedIn` ｜購読しており、明示的にオプトインしている。
|`Subscribed` ｜購読しているが、明示的にオプトインしていない。
|`UnSubscribed` ｜配信停止および/または明示的なオプトアウト｜｜。
{: .reset-td-br-1 .reset-td-br-2}

- `EmailNotificationSubscriptionType`
  - 有効な電子メールアドレスの受信時に自動的に`Subscribed` に設定されますが、明示的なオプトインプロセスを確立し、ユーザーからの明示的な同意の受信時にこの値を`OptedIn` に設定することをお勧めします。
- `PushNotificationSubscriptionType`
  - ユーザーは、有効なプッシュ登録時に自動的に`Subscribed` に設定されますが、明示的なオプトインプロセスを確立し、ユーザーから明示的な同意を得た時点でこの値を`OptedIn` に設定することをお勧めします。

>  これらのタイプは`AppboyPlatform.PCL.Models.NotificationSubscriptionType` に該当する。詳細については、[Managing user subscriptionsを][10]ご覧ください。

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/windows_universal/analytics/setting_user_ids/#user-id-integration-best-practices--notes
[2]: http://en.wikipedia.org/wiki/ISO_8601
[4]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
[7]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection
[10]: {{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions
