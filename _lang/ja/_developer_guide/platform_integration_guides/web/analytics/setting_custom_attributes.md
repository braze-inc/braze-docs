---
nav_title: カスタム属性の設定
article_title: iOS のカスタム属性の設定
platform: Web
page_order: 3
description: "このリファレンス記事では、Webのカスタム属性の割り当てと設定方法について説明します。"

---

# カスタム属性の設定

> Braze には、ユーザーに属性を割り当てるメソッドが用意されています。ダッシュボード上のこれらの属性に従って、ユーザーのフィルター処理とセグメント化を行うことができます。

実装前に、[ベストプラクティス][7]記事のカスタムイベント、カスタム属性、および購入イベントで提供されるセグメンテーションオプションの例を確認してください。

ユーザーに属性を割り当てるには、`braze.getUser()` メソッドを呼び出して、アプリの現在のユーザーへの参照を取得します。現在のユーザーへの参照を取得した後、定義済みまたはカスタム属性を設定するメソッドを呼び出すことができます。

## 定義済みユーザー属性の割り当て

Brazeは、[`User` クラス][1]内で以下のユーザー属性を設定するための定義済みメソッドを提供します：

- 名
- 姓
- 伝記ストリングス
- 国
- 生年月日
- メール
- 性別
- 市区町村
- 電話番号

### 実施例

#### ファーストネームの設定

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

Braze は、定義済みのユーザー属性メソッドに加えて、アプリケーションからのデータを追跡するための[カスタム属性](https://www.braze.com/docs/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types)も提供しています。 

カスタム属性の完全なメソッド仕様は、[JSDocsの][1]ここにある。

### カスタム属性の長さ

カスタム属性のキーと値の長さは最大255文字です。有効なカスタム属性値の詳細については、[テクニカル・ドキュメントを][1]参照してください。

### 実施例

#### カスタム属性に文字列値を設定する
```javascript
braze.getUser().setCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  YOUR_STRING_VALUE
);
```

#### カスタム属性に整数値を設定する
\`\`\`javascript
braze.getUser().setCustomUserAttribute(
  YOUR\_ATTRIBUTE\_KEY\_STRING、
  YOUR\_INT\_VALUE
);

// 整数属性は、以下のようなコードを使ってインクリメントすることもできる。
braze.getUser().incrementCustomUserAttribute(
  YOUR\_ATTRIBUTE\_KEY\_STRING、
  その属性を増やしたい整数値を指定します。
);
\`\`\`

#### カスタム属性に日付値を設定する
\`\`\`javascript
braze.getUser().setCustomUserAttribute(
  YOUR\_ATTRIBUTE\_KEY\_STRING、
  あなたの日付の値
);

// このメソッドは、メソッドが呼び出された時点で、現在の時刻をカスタム属性に割り当てます。
braze.getUser().setCustomUserAttribute(
  YOUR\_ATTRIBUTE\_KEY\_STRING、
  new Date()
);

// このメソッドは、secondsFromEpoch で指定された日付をカスタム属性に割り当てます。
braze.getUser().setCustomUserAttribute(
  YOUR\_ATTRIBUTE\_KEY\_STRING、
  new Date(secondsFromEpoch * 1000)
);
\`\`\`
>  このメソッドでBrazeに渡す日付は、JavaScriptのDateオブジェクトでなければなりません。

#### カスタム属性に配列値を設定する

カスタム属性配列内の要素の最大数は、25にデフォルト設定されています。個々の配列の最大値は、Braze ダッシュボードの [**データ設定**] > [**カスタム属性**] で100まで増やすことができます。この最大数を増やす必要がある場合は、カスタマーサービスマネージャーに連絡してください。要素の最大数を超える配列は、含まれる要素が最大数になるよう切り捨てられます。

\`\`\`javascript
braze.getUser().setCustomUserAttribute(YOUR\_ATTRIBUTE\_KEY\_STRING, YOUR\_ARRAY\_OF\_STRINGS);

// 配列値を持つカスタム属性に新しい要素を追加する
braze.getUser().addToCustomAttributeArray(YOUR\_ATTRIBUTE\_KEY\_STRING, "new string");

// 配列値を持つカスタム属性から要素を削除する
braze.getUser().removeFromCustomAttributeArray("custom\_attribute\_array\_test", "value to be removed");
\`\`\`

### カスタム属性の設定解除

カスタム属性は、その値を`null` に設定することで解除できる。

```javascript
braze.getUser().setCustomUserAttribute(YOUR_ATTRIBUTE_KEY_STRING, null);
```

### REST API によるカスタム属性の設定

REST API を使用してユーザー属性を設定することもできます。詳細については、[ユーザー API][4] のドキュメントを参照してください。

## ユーザーサブスクリプションの設定

ユーザーのサブスクリプション (メールまたはプッシュ) を設定するには、それぞれ関数 `setEmailNotificationSubscriptionType()` または `setPushNotificationSubscriptionType()` を呼び出します。これらの関数はどちらも引数として`enum` 型`braze.User.NotificationSubscriptionTypes` を取る。この型には、次の 3 つの状態があります。

| サブスクリプションステータス | 定義 |
| ------------------- | ---------- |
| `braze.User.NotificationSubscriptionTypes.OPTED_IN` | 配信登録済み、かつ明示的にオプトイン済み |
| `braze.User.NotificationSubscriptionTypes.SUBSCRIBED` | 配信登録済みだが、明示的なオプトインは未実行 |
| `braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED` | 配信停止済みまたは明示的にオプトアウト済み、あるいはその両方 |
{: .reset-td-br-1 .reset-td-br-2}

ユーザーがプッシュに登録されると、ブラウザは強制的に通知を許可するかブロックするかを選択させ、プッシュを許可することを選択した場合は、デフォルトで`OPTED_IN` 。 

サブスクリプションと明示的オプトインの実装の詳細については、[ユーザーサブスクリプションの管理][10]を参照してください。

### サンプルコード

#### ユーザーのメール配信を停止する：
```javascript
braze.getUser().setEmailNotificationSubscriptionType(braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED);
```

#### ユーザーのプッシュ配信を停止する：
```java
braze.getUser().setPushNotificationSubscriptionType(braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED);
```

[1]: https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html
[4]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
[6]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#arrays
[7]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection
[10]: {{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions
