{% multi_lang_include developer_guide/prerequisites/web.md %}

## デフォルトのユーザー属性

### 事前定義されたメソッド

Brazeは、[`User`クラス](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html)内で次のユーザー属性を設定するための定義済みメソッドを提供しています:

- 名
- 姓
- 言語
- 国
- 生年月日
- メールアドレス
- 性別
- 市区町村
- 電話番号

### デフォルト属性の設定

{% tabs %}
{% tab using methods %}
ユーザーにデフォルト属性を設定するには、Brazeインスタンスの`getUser()`メソッドを呼び出して、アプリの現在のユーザーへの参照を取得します。その後、メソッドを呼び出してユーザー属性を設定できます。

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

{% tab google tag manager %}
Google Tag Managerを使用する場合、標準属性項目（ユーザーの名など）は、カスタムユーザー属性と同様の方法で記録します。標準属性項目に渡す値が、[Userクラス](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html)のドキュメントで指定されている想定される形式と一致していることを確認してください。

たとえば、性別属性は、値として次のいずれかを使用できます: `"m" | "f" | "o" | "u" | "n" | "p"`。したがって、ユーザーの性別を女性に設定するには、次の内容のカスタムHTMLタグを作成します:

```html
<script>
window.braze.getUser().setGender("f")
</script>
```
{% endtab %}
{% endtabs %}

### デフォルト属性の解除

デフォルトのユーザー属性を解除するには、関連するメソッドに`null`を渡します。以下に例を示します:

{% tabs local %}
{% tab First name %}
```javascript
braze.getUser().setFirstName(null);
```
{% endtab %}
{% tab Gender %}
```javascript
braze.getUser().setGender(null);
```
{% endtab %}
{% tab Date of birth %}
```javascript
braze.getUser().setDateOfBirth(null, null, null);
```
{% endtab %}
{% endtabs %}

## カスタムユーザー属性

### カスタム属性の設定

{% tabs %}
{% tab using methods %}
デフォルトのユーザー属性メソッドに加えて、ユーザーに対して[カスタム属性]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types)を設定することもできます。完全なメソッド仕様については、[JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html)を参照してください。

{% subtabs local %}
{% subtab String %}
`string`値でカスタム属性を設定するには:

```javascript
braze.getUser().setCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  YOUR_STRING_VALUE
);
```

{% endsubtab %}
{% subtab Integer %}
`integer`値でカスタム属性を設定するには:

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
`date`値でカスタム属性を設定するには:

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

配列のデフォルトおよび最大要素数は500です。最大要素数は、Brazeダッシュボードの**[データ設定]** > **[カスタム属性]**で更新できます。最大要素数を超える配列は、最大要素数に切り詰められます。


`array`値でカスタム属性を設定するには:

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
カスタム属性のキーと値は、最大255文字までです。有効なカスタム属性の値に関する詳細については、[リファレンスドキュメント](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html)を参照してください。
{% endalert %}
{% endtab %}

{% tab google tag manager %}
Google Tag Managerのスクリプト言語の制限により、カスタムユーザー属性は使用できません。カスタム属性を記録するには、次の内容でカスタムHTMLタグを作成します:

```html
<script>
  // Note: If using SDK version 3.x or below, use `window.appboy` instead of `window.braze`
  // Version 4 or greater should use `window.braze`
window.braze.getUser().setCustomUserAttribute("attribute name", "attribute value");
</script>
```

{% alert important %}
GTMテンプレートでは、イベントまたは購入のネストされたプロパティはサポートされていません。前述のHTMLを使用して、ネストされたプロパティを必要とするイベントや購入を記録できます。
{% endalert %}
{% endtab %}
{% endtabs %}

### カスタム属性の設定解除

カスタム属性を解除するには、関連するメソッドに`null`を渡します。

```javascript
braze.getUser().setCustomUserAttribute(YOUR_ATTRIBUTE_KEY_STRING, null);
```

### 階層化カスタム属性

カスタム属性内にプロパティをネストすることもできます。次の例では、ネストされたプロパティを持つ`favorite_book`オブジェクトが、ユーザープロファイルのカスタム属性として設定されています。詳細については、[階層化カスタム属性]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support)を参照してください。

```javascript
import * as braze from "@braze/web-sdk";

const favoriteBook = {
  title: "The Hobbit",
  author: "J.R.R. Tolkien",
  publishing_date: "1937"
};

braze.getUser().setCustomUserAttribute("favorite_book", favoriteBook);
```

### REST APIの使用

ユーザー属性を設定または解除するには、REST APIも使用できます。詳細については、[ユーザーデータエンドポイント]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data)を参照してください。

## ユーザーサブスクリプションの設定

ユーザーのサブスクリプション（メールまたはプッシュ）を設定するには、それぞれ関数`setEmailNotificationSubscriptionType()`または`setPushNotificationSubscriptionType()`を呼び出します。両方の関数は`enum`型`braze.User.NotificationSubscriptionTypes`を引数として取ります。この型には、次の3つの状態があります:

| サブスクリプションのステータス | 定義 |
| ------------------- | ---------- |
| `braze.User.NotificationSubscriptionTypes.OPTED_IN` | 配信登録済み、かつ明示的にオプトイン済み |
| `braze.User.NotificationSubscriptionTypes.SUBSCRIBED` | 購読中、ただし明示的にオプトインしていない |
| `braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED` | 配信停止済みまたは明示的にオプトアウト済み、あるいはその両方 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

ユーザーがプッシュに登録されると、ブラウザは通知を許可するかブロックするかの選択を求めます。プッシュを許可することを選択した場合、デフォルトで`OPTED_IN`に設定されます。

サブスクリプションと明示的なオプトインの実装に関する詳細については、[ユーザーのサブスクリプションの管理]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions)を参照してください。

### ユーザーのメール配信停止

```javascript
braze.getUser().setEmailNotificationSubscriptionType(braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED);
```

### ユーザーのプッシュ通知の配信停止

```java
braze.getUser().setPushNotificationSubscriptionType(braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED);
```
