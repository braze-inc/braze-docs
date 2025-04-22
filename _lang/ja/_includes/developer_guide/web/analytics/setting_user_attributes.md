{% multi_lang_include developer_guide/prerequisites/web.md %}

## デフォルトのユーザー属性

{% tabs %}
{% tab 標準実装 %}
ユーザーのデフォルト属性を設定するには、Braze インスタンスで`getCurrentUser()` メソッドを呼び出して、アプリの現在のユーザーへの参照を取得します。次に、メソッドを呼び出してユーザー属性を設定できます。

{% subtabs local %}
{% subtab First name %}
```javascript
braze.getUser().setFirstName("SomeFirstName");
```
{% endsubtab %}
{% subtab Gender %}
```javascript
braze.getUser().setGender(braze.User.Genders.FEMALE);
```
{% endsubtab %}
{% subtab Date of birth %}
```javascript
braze.getUser().setDateOfBirth(2000, 12, 25);
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Google Tag Manager %}
Google Tag Manager を使用して、標準ユーザー属性(ユーザーのファーストネームなど) をカスタムユーザー属性と同じ方法でログに記録する必要があります。標準属性項目に渡す値が、[[ユーザークラス](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html)] のドキュメントで指定されている予期される形式と一致していることを確認します。

たとえば、性別属性は、値として次のいずれかを使用できます。`"m" | "f" | "o" | "u" | "n" | "p"`したがって、ユーザーの性別を女性に設定するには、次の内容のカスタムHTML タグを作成します。

```html
<script>
window.braze.getUser().setGender("f")
</script>
```
{% endtab %}
{% endtabs %}

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

## カスタムユーザー属性

{% tabs %}
{% tab 標準実装 %}
デフォルトのユーザー属性メソッドに加えて、ユーザーに[カスタム属性]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types)を設定することもできます。完全なメソッド指定については、[JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html)を参照してください。

{% subtabs local %}
{% subtab String %}
`string` 値を使用してカスタム属性を設定するには:

```javascript
braze.getUser().setCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  YOUR_STRING_VALUE
);
```

{% endsubtab %}
{% subtab Integer %}
`integer` 値を使用してカスタム属性を設定するには:

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

{% endsubtab %}
{% subtab Date %}
`date` 値を使用してカスタム属性を設定するには:

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

{% endsubtab %}
{% subtab Array %}

カスタム属性配列には最大25 個の要素を含めることができます。**データ型**に対して手動で設定された(自動的に検出されない)個々のアレイは、**データ設定**> **カスタム属性**の下のBrazeダッシュボードで100まで増加できます。この最大値を増やす場合は、Braze アカウントマネージャにお問い合わせください。

[配列]({{site.baseurl}}/developer_guide/platform_wide/getting_started/analytics_overview/#arrays) が要素数の最大値を超える場合、要素数の最大値に切り詰められます。

`array` 値を使用してカスタム属性を設定するには:

```javascript
braze.getUser().setCustomUserAttribute(YOUR_ATTRIBUTE_KEY_STRING, YOUR_ARRAY_OF_STRINGS);

// Adding a new element to a custom attribute with an array value
braze.getUser().addToCustomAttributeArray(YOUR_ATTRIBUTE_KEY_STRING, "new string");

// Removing an element from a custom attribute with an array value
braze.getUser().removeFromCustomAttributeArray(YOUR_ATTRIBUTE_KEY_STRING, "value to be removed");
```

{% alert important %}
このメソッドでBrazeに渡される日付は、JavaScriptのDateオブジェクトでなければなりません。
{% endalert %}
{% endsubtab %}
{% endsubtabs %}

{% alert important %}
カスタム属性のキーと値には、最大 255 文字しか使用できません。有効なカスタム属性値の詳細については、[リファレンスドキュメント](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html)を参照してください。
{% endalert %}
{% endtab %}

{% tab Google Tag Manager %}
Googleタグマネージャのスクリプト言語が制限されているため、カスタムユーザー 属性は使用できません。カスタム属性s を記録するには、次の内容でカスタムHTML タグを作成します。

```html
<script>
  // Note: If using SDK version 3.x or below, use `window.appboy` instead of `window.braze`
  // Version 4 or greater should use `window.braze`
window.braze.getUser().setCustomUserAttribute("attribute name", "attribute value");
</script>
```

{% alert important %}
GTM テンプレートでは、イベントまたは購買のネストされたプロパティは使用できません。前述のHTMLを使用して、ネストされたプロパティーを必要とするすべての行動または購入を記録できます。
{% endalert %}
{% endtab %}
{% endtabs %}

### カスタム属性の設定解除

カスタム属性は、その値を `null` に設定することで設定解除できます。

```javascript
braze.getUser().setCustomUserAttribute(YOUR_ATTRIBUTE_KEY_STRING, null);
```

### REST API の使用

REST API を使用して、ユーザー属性を設定または設定解除することもできます。詳細については、[User Data Endpoints]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data)を参照してください。

## ユーザーサブスクリプションの設定

ユーザーのサブスクリプション (メールまたはプッシュ) を設定するには、それぞれ関数 `setEmailNotificationSubscriptionType()` または `setPushNotificationSubscriptionType()` を呼び出します。どちらの関数も`enum` 型`braze.User.NotificationSubscriptionTypes` を引数として取ります。この型には、次の 3 つの状態があります。

| サブスクリプションのステータス | 定義 |
| ------------------- | ---------- |
| `braze.User.NotificationSubscriptionTypes.OPTED_IN` | 配信登録済み、かつ明示的にオプトイン済み |
| `braze.User.NotificationSubscriptionTypes.SUBSCRIBED` | 購読済み、ただし明示的に選択されていない |
| `braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED` | 配信停止済みまたは明示的にオプトアウト済み、あるいはその両方 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

ユーザーがプッシュに登録されると、ブラウザは通知を許可するかブロックするかを選択させ、プッシュを許可することを選択した場合、デフォルトで`OPTED_IN`に設定されます。 

[ユーザーのサブスクリプションの管理]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions)を訪れて、サブスクリプションと明示的なオプトインの実装に関する詳細情報をご覧ください。

### メールからのユーザの登録解除

```javascript
braze.getUser().setEmailNotificationSubscriptionType(braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED);
```

### プッシュからのユーザーのサブスクライブ解除

```java
braze.getUser().setPushNotificationSubscriptionType(braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED);
```
