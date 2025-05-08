---
nav_title: カスタム属性の設定
article_title: Roku のカスタム属性の設定
platform: Roku
page_order: 4
page_type: reference
description: "このリファレンス記事では、Braze SDK を介して Roku のカスタム属性をユーザーに割り当てる方法を説明します。"

---

# カスタム属性の設定

> Braze では、ユーザーに属性を割り当てるメソッドが提供されています。ダッシュボードでこれらの属性に基づき、ユーザーをフィルターおよびセグメント化できます。

実装前に、[ベストプラクティス]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection)記事のカスタムイベント、ユーザー属性、および購入イベントで提供されるセグメンテーションオプションの例を確認してください。また、[イベントの命名規則]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/)についてもよく理解しておくことをお勧めします。

## デフォルトユーザー属性の割り当て

ユーザー属性は、現在のアクティブユーザーに割り当てられます。以下のデフォルトフィールドを設定できます。

- `FirstName`
- `LastName`
- `Email`
- `Gender`
- `DateOfBirth`
- `Country`
- `Language`
- `HomeCity`
- `PhoneNumber`

**実装例**<br>名を設定するコードは以下のようになります。

```brightscript
m.Braze.setFirstName("User's First Name")
```

## カスタムユーザー属性の割り当て

Braze では、デフォルトユーザー属性以外にも、複数の異なるデータタイプを使用してカスタム属性を定義できます。

### カスタム属性値の設定
{% tabs %}
{% tab Boolean %}
```brightscript
m.Braze.setCustomAttribute("boolAttribute", true)
```
{% endtab %}
{% tab 整数 %}
```brightscript
m.Braze.setCustomAttribute("intAttribute", 5)
```
{% endtab %}
{% tab フロートまたはダブル %}
```brightscript
m.Braze.setCustomAttribute("floatAttribute", 3.5)
```
Braze では、FLOAT 値と DOUBLE 値がデータベースでまったく同じく処理されます。
{% endtab %}
{% tab String %}
```brightscript
m.Braze.setCustomAttribute("stringAttribute", "stringValue")
```
{% endtab %}
{% tab 日付 %}
```brightscript
dateAttribute = CreateObject("roDateTime")
dateAttribute.fromISO8601String("1992-11-29 00:00:00.000")
m.Braze.setCustomAttribute("dateAttribute", dateAttribute)
```
{% endtab %}
{% tab 配列 %}
```brightscript
stringArray = createObject("roArray", 3, true)
stringArray.Push("string1")
stringArray.Push("string2")
stringArray.Push("string3")
m.Braze.setCustomAttribute("arrayAttribute", stringArray)
```
{% endtab %}
{% endtabs %}

### カスタム属性のインクリメント / デクリメント

このコードは、インクリメントカスタム属性の例です。カスタム属性の値は、正または負の整数値でインクリメントできます。

```brightscript
m.Braze.incrementCustomUserAttribute("intAttribute", 3)
```

### カスタム属性の設定解除

カスタム属性は、次のメソッドを使用して設定を解除することもできます。

```brightscript
m.Braze.unsetCustomAttribute("attributeName")
```

### REST API によるカスタム属性の設定

REST API を使用してユーザー属性を設定することもできます。詳細については、[ユーザー API]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data) のドキュメントを参照してください。

### カスタム属性値の制限

カスタム属性値の最大長は255文字です。

## メールのサブスクリプションステータスの管理

SDK から、ユーザーに対して以下のメールのサブスクリプションステータスをプログラムで設定できます。

| サブスクリプションのステータス | 定義 |
| ------------------- | ---------- |
| `OptedIn` | 配信登録済み、かつ明示的にオプトイン済み |
| `Subscribed` | 購読済み、ただし明示的に選択されていない |
| `UnSubscribed` | 配信停止済みまたは明示的にオプトアウト済み、あるいはその両方 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

>  これらの型は `BrazeConstants().SUBSCRIPTION_STATES` に属します

メールのサブスクリプションステータスを設定するメソッドは `setEmailSubscriptionState()` です。ユーザーは、有効なメールアドレスを取得すると自動的に `Subscribed` に設定されます 。ただし、明示的なオプトインのプロセスを確立し、ユーザーから明示的な同意を得た時点でこの値を `OptedIn` に設定することをお勧めします。詳細については、「[ユーザーサブスクリプションの管理]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions)」を参照してください。

使用例:
```brightscript
m.Braze.setEmailSubscriptionState(BrazeConstants().SUBSCRIPTION_STATES.OPTED_IN)
```

