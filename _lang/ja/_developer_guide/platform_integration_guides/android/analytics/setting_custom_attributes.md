---
nav_title: カスタム属性の設定
article_title: Android と FireOS のカスタム属性の設定
platform: 
  - Android
  - FireOS
page_order: 3
description: "このリファレンス記事では、Android または FireOS アプリケーションのカスタム属性を設定する方法を説明します。"

---

# カスタム属性の設定

> Braze では、ユーザーに属性を割り当てるメソッドが提供されています。ダッシュボードでこれらの属性に基づき、ユーザーをフィルターおよびセグメント化できます。このリファレンス記事では、Android または FireOS アプリケーションのカスタム属性を設定する方法を説明します。

実装前に、[分析の概要][7]のカスタムイベント、カスタム属性、および購入イベントによって提供されるセグメンテーションオプションの例と、[イベント命名規則]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/)のメモを必ず確認してください。

## ユーザー属性の割り当て

ユーザーに属性を割り当てるには、Braze インスタンスの`getCurrentUser()`メソッドを呼び出して、アプリの現在のユーザーへの参照を取得します。現在のユーザーへの参照を取得した後、定義済みまたはカスタム属性を設定するメソッドを呼び出すことができます。

### 標準ユーザー属性

Brazeは、[BrazeUser クラス][2]内で以下のユーザー属性を設定するための定義済みメソッドを提供しています。[メソッドの仕様][2]については、KDoc を参照してください。

- 名
- 姓
- 国
- 言語
- 生年月日
- メールアドレス
- 性別
- 市区町村
- 電話番号

姓、名、国、市区町村などの文字列値はすべて255文字に制限されています。

#### 標準属性値の設定

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).getCurrentUser().setFirstName("first_name");
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).currentUser?.setFirstName("first_name")
```

{% endtab %}
{% endtabs %}

#### カスタム属性値の設定

{% tabs local %}
{% tab String %}
{% subtabs global %}
{% subtab JAVA %}

```java
Braze.getInstance(context).getCurrentUser().setCustomUserAttribute("your_attribute_key", "your_attribute_value");
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.getInstance(context).currentUser?.setCustomUserAttribute("your_attribute_key", "your_attribute_value")
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Integer %}
{% subtabs global %}
{% subtab JAVA %}

```java
Braze.getInstance(context).getCurrentUser().setCustomUserAttribute("your_attribute_key", YOUR_INT_VALUE);
// Integer attributes may also be incremented using code like the following:
Braze.getInstance(context).getCurrentUser().incrementCustomUserAttribute("your_attribute_key", YOUR_INCREMENT_VALUE);
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.getInstance(context).currentUser?.setCustomUserAttribute("your_attribute_key", YOUR_INT_VALUE)
// Integer attributes may also be incremented using code like the following:
Braze.getInstance(context).currentUser?.incrementCustomUserAttribute("your_attribute_key", YOUR_INCREMENT_VALUE)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Boolean %}
{% subtabs global %}
{% subtab JAVA %}

```java
Braze.getInstance(context).getCurrentUser().setCustomUserAttribute("your_attribute_key", YOUR_BOOLEAN_VALUE);
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.getInstance(context).currentUser?.setCustomUserAttribute("your_attribute_key", YOUR_BOOLEAN_VALUE)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Long %}
{% subtabs global %}
{% subtab JAVA %}

```java
Braze.getInstance(context).getCurrentUser().setCustomUserAttribute("your_attribute_key", YOUR_LONG_VALUE);
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.getInstance(context).currentUser?.setCustomUserAttribute("your_attribute_key", YOUR_LONG_VALUE)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Float %}
{% subtabs global %}
{% subtab JAVA %}

```java
Braze.getInstance(context).getCurrentUser().setCustomUserAttribute("your_attribute_key", YOUR_FLOAT_VALUE);
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.getInstance(context).currentUser?.setCustomUserAttribute("your_attribute_key", YOUR_FLOAT_VALUE)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Double %}
{% subtabs global %}
{% subtab JAVA %}

```java
Braze.getInstance(context).getCurrentUser().setCustomUserAttribute("your_attribute_key", YOUR_DOUBLE_VALUE);
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.getInstance(context).currentUser?.setCustomUserAttribute("your_attribute_key", YOUR_DOUBLE_VALUE)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Date %}
{% subtabs global %}
{% subtab JAVA %}

```java
Braze.getInstance(context).getCurrentUser().setCustomUserAttribute("your_attribute_key", YOUR_DATE_VALUE);
// This method will assign the current time to a custom attribute at the time the method is called:
Braze.getInstance(context).getCurrentUser().setCustomUserAttributeToNow("your_attribute_key");
// This method will assign the date specified by SECONDS_FROM_EPOCH to a custom attribute:
Braze.getInstance(context).getCurrentUser().setCustomUserAttributeToSecondsFromEpoch("your_attribute_key", SECONDS_FROM_EPOCH);
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.getInstance(context).currentUser?.setCustomUserAttribute("your_attribute_key", YOUR_DATE_VALUE)
// This method will assign the current time to a custom attribute at the time the method is called:
Braze.getInstance(context).currentUser?.setCustomUserAttributeToNow("your_attribute_key")
// This method will assign the date specified by SECONDS_FROM_EPOCH to a custom attribute:
Braze.getInstance(context).currentUser?.setCustomUserAttributeToSecondsFromEpoch("your_attribute_key", SECONDS_FROM_EPOCH)
```

{% endsubtab %}
{% endsubtabs %}

{% alert warning %}
このメソッドで Braze に渡される日付は、[ISO 8601](http://en.wikipedia.org/wiki/ISO_8601)フォーマット (例: `2013-07-16T19:20:30+01:00`) または`yyyy-MM-dd'T'HH:mm:ss:SSSZ`フォーマット (例: `2016-12-14T13:32:31.601-0800`) のいずれかである必要があります。
{% endalert %}

{% endtab %}
{% tab Array %}

カスタム属性配列内の要素の最大数は、25にデフォルト設定されています。個々の配列の最大値は、Braze ダッシュボードの [**データ設定**] > [**カスタム属性**] で100まで増やすことができます。要素の最大数を超える配列は、含まれる要素が最大数になるよう切り捨てられます。カスタム属性配列とその動作の詳細については、[配列に関する]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#arrays)ドキュメントを参照してください。

{% subtabs global %}
{% subtab JAVA %}

```java
// Setting a custom attribute with an array value
Braze.getInstance(context).getCurrentUser().setCustomAttributeArray("your_attribute_key", testSetArray);
// Adding to a custom attribute with an array value
Braze.getInstance(context).getCurrentUser().addToCustomAttributeArray("your_attribute_key", "value_to_add");
// Removing a value from an array type custom attribute
Braze.getInstance(context).getCurrentUser().removeFromCustomAttributeArray("your_attribute_key", "value_to_remove");
```
{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
// Setting a custom attribute with an array value
Braze.getInstance(context).currentUser?.setCustomAttributeArray("your_attribute_key", testSetArray)
// Adding to a custom attribute with an array value
Braze.getInstance(context).currentUser?.addToCustomAttributeArray("your_attribute_key", "value_to_add")
// Removing a value from an array type custom attribute
Braze.getInstance(context).currentUser?.removeFromCustomAttributeArray("your_attribute_key", "value_to_remove")
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

#### カスタム属性の設定解除

カスタム属性は、次のメソッドを使用して設定を解除することもできます。

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).getCurrentUser().unsetCustomUserAttribute("your_attribute_key");
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).currentUser?.unsetCustomUserAttribute("your_attribute_key")
```

{% endtab %}
{% endtabs %}

#### REST API によるカスタム属性

REST API を使用してユーザー属性を設定することもできます。これを行うには、[ユーザー API のドキュメントを][4]参照してください。

## ユーザーサブスクリプションの設定

ユーザーのサブスクリプション (メールまたはプッシュ) を設定するには、それぞれ関数 `setEmailNotificationSubscriptionType()` または `setPushNotificationSubscriptionType()` を呼び出します。これらの関数では、いずれも引数として列挙型 `NotificationSubscriptionType` が使用されます。この型には、次の3つの状態があります。

| サブスクリプションステータス | 定義 |
| ------------------- | ---------- |
| `OPTED_IN` | サブスクリプション登録済み、かつ明示的にオプトイン済み |
| `SUBSCRIBED` | サブスクリプション登録済み、ただし明示的なオプトイン未実行 |
| `UNSUBSCRIBED` | 配信停止済みおよび/または明示的にオプトアウト済み |
{: .reset-td-br-1 .reset-td-br-2}

{% alert important %}
Android では、ユーザーにプッシュ通知を送る際に明示的なオプトインは必要ありません。ユーザーがプッシュ登録されると、デフォルトで`OPTED_IN`ではなく`SUBSCRIBED`に設定されます。サブスクリプションと明示的オプトインの実装の詳細については、[ユーザーサブスクリプションの管理]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions)を参照してください。
{% endalert %}

### メールサブスクリプションの設定

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).getCurrentUser().setEmailNotificationSubscriptionType(emailNotificationSubscriptionType);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).currentUser?.setEmailNotificationSubscriptionType(emailNotificationSubscriptionType)
```

{% endtab %}
{% endtabs %}

### プッシュ通知サブスクリプションの設定

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).getCurrentUser().setPushNotificationSubscriptionType(pushNotificationSubscriptionType);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).currentUser?.setPushNotificationSubscriptionType(pushNotificationSubscriptionType)
```

{% endtab %}
{% endtabs %}

[2]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/index.html
[4]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
[6]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#arrays
[7]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection
