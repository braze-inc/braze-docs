{% multi_lang_include developer_guide/prerequisites/web.md %}

## デフォルトのユーザー属性

### 定義済みのメソッド

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

### デフォルト属性の設定

{% tabs %}
{% tab using methods %}
ユーザーにデフォルト属性を設定するには、Brazeインスタンスで`getUser()` メソッドを呼び出し、アプリの現在のユーザーへの参照を取得する。そして、ユーザー属性を設定するメソッドを呼び出すことができる。

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
Googleタグマネージャーを使用して、標準ユーザー属性（ユーザーの名など）は、カスタムユーザー属性と同じ方法でログに記録されるべきである。標準属性項目に渡す値が、[[ユーザークラス](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html)] のドキュメントで指定されている予期される形式と一致していることを確認します。

たとえば、性別属性は、値として次のいずれかを使用できます。`"m" | "f" | "o" | "u" | "n" | "p"`したがって、ユーザーの性別を女性に設定するには、次の内容のカスタムHTML タグを作成します。

```html
<script>
window.braze.getUser().setGender("f")
</script>
```
{% endtab %}
{% endtabs %}

### デフォルト属性の設定を解除する

デフォルトのユーザー属性を解除するには、関連するメソッドに`null` 。以下に例を示します。

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
デフォルトのユーザー属性に加え、[カスタム属性を]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types)設定することもできる。メソッドの全仕様については、[JSDocsを](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html)参照のこと。

{% subtabs local %}
{% subtab String %}
`string` 、カスタム属性を設定する：

```javascript
braze.getUser().setCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  YOUR_STRING_VALUE
);
```

{% endsubtab %}
{% subtab Integer %}
`integer` 、カスタム属性を設定する：

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
`date` 、カスタム属性を設定する：

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

カスタム属性配列の要素は最大25個まで持つことができる。**データ型を**手動で設定した（自動検出しない）個々のアレイは、Brazeダッシュボードの「**データ設定**」>「カスタム属性」で100まで増やすことができる。この上限を増やしたい場合は、Brazeアカウントマネージャーに連絡すること。

[配列]({{site.baseurl}}/developer_guide/platform_wide/getting_started/analytics_overview/#arrays) が要素数の最大値を超える場合、要素数の最大値に切り詰められます。

`array` 、カスタム属性を設定する：

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
カスタム属性のキーと値は、最大255文字までしか持つことができない。有効なカスタム属性値の詳細については、[リファレンスドキュメントを](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html)参照のこと。
{% endalert %}
{% endtab %}

{% tab google tag manager %}
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

### カスタム属性の設定を解除する

カスタム属性を解除するには、関連するメソッドに`null` 。

```javascript
braze.getUser().setCustomUserAttribute(YOUR_ATTRIBUTE_KEY_STRING, null);
```

### 階層化カスタム属性

また、カスタム属性の中にプロパティを入れ子にすることもできる。以下の例では、階層化プロパティを持つ`favorite_book` オブジェクトが、ユーザープロファイルのカスタム属性として設定されている。詳しくは、[階層化カスタム]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support)属性を参照のこと。

```javascript
import * as braze from "@braze/web-sdk";

const favoriteBook = {
  title: "The Hobbit",
  author: "J.R.R. Tolkien",
  publishing_date: "1937"
};

braze.getUser().setCustomUserAttribute("favorite_book", favoriteBook);
```

### REST API の使用

また、REST APIを使用して、ユーザー属性を設定または解除することもできる。詳細については、[ユーザーデータエンドポイント]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data)を参照してください。

## ユーザーサブスクリプションの設定

ユーザーのサブスクリプション (メールまたはプッシュ) を設定するには、それぞれ関数 `setEmailNotificationSubscriptionType()` または `setPushNotificationSubscriptionType()` を呼び出します。どちらの関数も引数として`enum` 型`braze.User.NotificationSubscriptionTypes` を取る。この型には、次の 3 つの状態があります。

| サブスクリプションのステータス | 定義 |
| ------------------- | ---------- |
| `braze.User.NotificationSubscriptionTypes.OPTED_IN` | 配信登録済み、かつ明示的にオプトイン済み |
| `braze.User.NotificationSubscriptionTypes.SUBSCRIBED` | 購読済み、ただし明示的に選択されていない |
| `braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED` | 配信停止済みまたは明示的にオプトアウト済み、あるいはその両方 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

ユーザーがプッシュに登録されると、ブラウザは通知を許可するかブロックするかを選択させ、プッシュを許可することを選択した場合、デフォルトで`OPTED_IN`に設定されます。 

[ユーザーのサブスクリプションの管理]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions)を訪れて、サブスクリプションと明示的なオプトインの実装に関する詳細情報をご覧ください。

### ユーザーのメール登録を解除する:

```javascript
braze.getUser().setEmailNotificationSubscriptionType(braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED);
```

### プッシュからユーザーの登録を解除する:

```java
braze.getUser().setPushNotificationSubscriptionType(braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED);
```
