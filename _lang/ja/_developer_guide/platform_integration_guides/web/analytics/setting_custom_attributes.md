---
nav_title: カスタム属性の設定
article_title: Webのカスタム属性の設定
platform: Web
page_order: 3
description: "このリファレンス記事では、Web のカスタム属性を割り当てて、設定する方法を説明します。"

---

# カスタム属性の設定

> Braze では、ユーザーに属性を割り当てるメソッドが提供されています。ダッシュボードでこれらの属性に従ってユーザーをフィルターおよびSegmentできます。

実装前に、カスタムイベント、カスタム属性、および購入イベントによって提供されるセグメンテーションオプションの例を[ベストプラクティス]({{site.baseurl}}/developer_guide/platform_wide/getting_started/analytics_overview/#best-practices)で確認してください。

ユーザーに属性を割り当てるには、`braze.getUser()` メソッドを呼び出して、アプリの現在のユーザーへの参照を取得します。現在のユーザーへの参照を取得した後、定義済みまたはカスタム属性を設定するメソッドを呼び出すことができます。

## 定義済みのユーザー属性の割り当て

Brazeは、[`User`クラス](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html)内で次のユーザー属性を設定するための定義済みメソッドを提供します:

- 名
- 姓
- 言語
- 国
- 生年月日
- メールアドレス
- 性別
- 市区町村
- 電話番号

### 実装例

#### 名の設定

```javascript
braze.getUser().setFirstName("SomeFirstName");
```

#### 性別の設定

```javascript
braze.getUser().setGender(braze.User.Genders.FEMALE);
```

#### 生年月日の設定

```javascript
braze.getUser().setDateOfBirth(2000, 12, 25);
```

## カスタムユーザー属性の割り当て

Braze は、定義済みのユーザー属性メソッドに加えて、アプリケーションからのデータを追跡するための[カスタム属性]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types)も提供しています。 

カスタム属性の完全なメソッドの仕様は、[JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html) 内にあります。

### カスタム属性の長さ

カスタム属性キーと値の最大長は255文字です。有効なカスタム属性値の詳細については、[完全な技術ドキュメント](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html)を参照してください。

### 実装例

#### 文字列値を持つカスタム属性の設定
```javascript
braze.getUser().setCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  YOUR_STRING_VALUE
);
```

#### 整数値を持つカスタム属性の設定
```javascript
braze.getUser().setCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  YOUR_INT_VALUE
);

// Integer attributes may also be incremented using code like the following
braze.getUser().incrementCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  THE_INTEGER_VALUE_BY_WHICH_YOU_WANT_TO_INCREMENT_THE_ATTRIBUTE
);
```

#### 日付値を持つカスタム属性の設定
```javascript
braze.getUser().setCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  YOUR_DATE_VALUE
);

// This method will assign the current time to a custom attribute at the time the method is called
braze.getUser().setCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  new Date()
);

// This method will assign the date specified by secondsFromEpoch to a custom attribute
braze.getUser().setCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  new Date(secondsFromEpoch * 1000)
);
```
>  このメソッドでBrazeに渡される日付は、JavaScriptのDateオブジェクトでなければなりません。

#### 配列値でカスタム属性を設定する

カスタム属性配列内の要素の最大数は、25にデフォルト設定されています。個々の配列は、**データ設定** > **カスタム属性** のBrazeダッシュボードで最大100まで増やすことができます。この最大値を増やしたい場合は、顧客サービスマネージャーに連絡してください。[配列]({{site.baseurl}}/developer_guide/platform_wide/getting_started/analytics_overview/#arrays) が要素数の最大値を超える場合、要素数の最大値に切り詰められます。

```javascript
braze.getUser().setCustomUserAttribute(YOUR_ATTRIBUTE_KEY_STRING, YOUR_ARRAY_OF_STRINGS);

// Adding a new element to a custom attribute with an array value
braze.getUser().addToCustomAttributeArray(YOUR_ATTRIBUTE_KEY_STRING, "new string");

// Removing an element from a custom attribute with an array value
braze.getUser().removeFromCustomAttributeArray(YOUR_ATTRIBUTE_KEY_STRING, "value to be removed");
```

### カスタム属性の設定解除

カスタム属性は、その値を `null` に設定することで設定解除できます。

```javascript
braze.getUser().setCustomUserAttribute(YOUR_ATTRIBUTE_KEY_STRING, null);
```

### REST API によるカスタム属性の設定

REST API を使用してユーザー属性を設定することもできます。詳細については、[ユーザー API]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data) のドキュメントを参照してください。

## ユーザーサブスクリプションの設定

ユーザーのサブスクリプション (メールまたはプッシュ) を設定するには、それぞれ関数 `setEmailNotificationSubscriptionType()` または `setPushNotificationSubscriptionType()` を呼び出します。これらの関数は両方とも、引数として`enum`型`braze.User.NotificationSubscriptionTypes`を取ります。この型には、次の 3 つの状態があります。

| サブスクリプションのステータス | 定義 |
| ------------------- | ---------- |
| `braze.User.NotificationSubscriptionTypes.OPTED_IN` | 配信登録済み、かつ明示的にオプトイン済み |
| `braze.User.NotificationSubscriptionTypes.SUBSCRIBED` | 購読済み、ただし明示的に選択されていない |
| `braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED` | 配信停止済みまたは明示的にオプトアウト済み、あるいはその両方 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

ユーザーがプッシュに登録されると、ブラウザは通知を許可するかブロックするかを選択させ、プッシュを許可することを選択した場合、デフォルトで`OPTED_IN`に設定されます。 

[ユーザーのサブスクリプションの管理]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions)を訪れて、サブスクリプションと明示的なオプトインの実装に関する詳細情報をご覧ください。

### サンプルコード

#### ユーザーのメール登録を解除する:
```javascript
braze.getUser().setEmailNotificationSubscriptionType(braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED);
```

#### プッシュからユーザーの登録を解除する: 
```java
braze.getUser().setPushNotificationSubscriptionType(braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED);
```

