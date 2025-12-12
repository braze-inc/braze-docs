{% multi_lang_include developer_guide/prerequisites/android.md %}

## デフォルトのユーザー属性

### 定義済みのメソッド

Brazeには、以下のユーザー属性を設定するための定義済みメソッドがある。 [`BrazeUser`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/index.html)クラス内でメソッドの仕様については、[KDocを](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/index.html)参照のこと。

- 名
- 姓
- 国
- 言語
- 生年月日
- メールアドレス
- 性別
- 市区町村
- 電話番号

{% alert note %}
姓、名、国、市区町村などの文字列値はすべて255文字に制限されています。
{% endalert %}

### デフォルト属性の設定

ユーザーにデフォルト属性を設定するには、Brazeインスタンスで`getCurrentUser()` メソッドを呼び出し、アプリの現在のユーザーへの参照を取得する。そして、ユーザー属性を設定するメソッドを呼び出すことができる。

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
  @Override
  public void onSuccess(BrazeUser brazeUser) {
    brazeUser.setFirstName("first_name");
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  brazeUser.setFirstName("first_name")
}
```

{% endtab %}
{% endtabs %}

### デフォルト属性の設定を解除する

ユーザー属性を解除するには、関連するメソッドに`null` 。

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
  @Override
  public void onSuccess(BrazeUser brazeUser) {
    brazeUser.setFirstName(null);
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  brazeUser.setFirstName(null)
}
```

{% endtab %}
{% endtabs %}

## カスタムユーザー属性

デフォルトのユーザー属性に加え、Brazeではいくつかのデータタイプを使用してカスタム属性を定義することができる。各属性のセグメンテーションオプションの詳細については、[ユーザーデータ収集を]({{site.baseurl}}/developer_guide/analytics)参照のこと。

### カスタム属性の設定

{% tabs local %}
{% tab String %}
`string` 、カスタム属性を設定する：

{% subtabs global %}
{% subtab JAVA %}

```java
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
  @Override
  public void onSuccess(BrazeUser brazeUser) {
    brazeUser.setCustomUserAttribute("your_attribute_key", "your_attribute_value");
  }
}
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  brazeUser.setCustomUserAttribute("your_attribute_key", "your_attribute_value")
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab 整数 %}
`int` 、カスタム属性を設定する：

{% subtabs global %}
{% subtab JAVA %}

```java
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
  @Override
  public void onSuccess(BrazeUser brazeUser) {
    brazeUser.setCustomUserAttribute("your_attribute_key", YOUR_INT_VALUE);
    
    // Integer attributes may also be incremented using code like the following:
    brazeUser.incrementCustomUserAttribute("your_attribute_key", YOUR_INCREMENT_VALUE);
  }
}
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  brazeUser.setCustomUserAttribute("your_attribute_key", YOUR_INT_VALUE)

  // Integer attributes may also be incremented using code like the following:
  brazeUser.incrementCustomUserAttribute("your_attribute_key", YOUR_INCREMENT_VALUE)
}
```

{% endsubtab %}
{% endsubtabs %}

`long` 、整数値でカスタム属性を設定する：

{% subtabs global %}
{% subtab JAVA %}

```java
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
  @Override
  public void onSuccess(BrazeUser brazeUser) {
    brazeUser.setCustomUserAttribute("your_attribute_key", YOUR_LONG_VALUE);
  }
});
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  brazeUser.setCustomUserAttribute("your_attribute_key", YOUR_LONG_VALUE)
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab 浮動小数点 %}
`float` 、カスタム属性を設定する：

{% subtabs global %}
{% subtab JAVA %}

```java
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
  @Override
  public void onSuccess(BrazeUser brazeUser) {
    brazeUser.setCustomUserAttribute("your_attribute_key", YOUR_FLOAT_VALUE);
  }
});
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  brazeUser.setCustomUserAttribute("your_attribute_key", YOUR_FLOAT_VALUE)
}
```

{% endsubtab %}
{% endsubtabs %}

`double` 、カスタム属性を設定する：

{% subtabs global %}
{% subtab JAVA %}

```java
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
  @Override
  public void onSuccess(BrazeUser brazeUser) {
    brazeUser.setCustomUserAttribute("your_attribute_key", YOUR_DOUBLE_VALUE);
  }
});
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  brazeUser.setCustomUserAttribute("your_attribute_key", YOUR_DOUBLE_VALUE)
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Boolean %}
`boolean` 、カスタム属性を設定する：

{% subtabs global %}
{% subtab JAVA %}

```java
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
  @Override
  public void onSuccess(BrazeUser brazeUser) {
    brazeUser.setCustomUserAttribute("your_attribute_key", YOUR_BOOLEAN_VALUE);
  }
});
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  brazeUser.setCustomUserAttribute("your_attribute_key", YOUR_BOOLEAN_VALUE)
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab 日付 %}
{% subtabs global %}
{% subtab JAVA %}

```java
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
  @Override
  public void onSuccess(BrazeUser brazeUser) {
    brazeUser.setCustomUserAttribute("your_attribute_key", YOUR_DATE_VALUE);
    // This method will assign the current time to a custom attribute at the time the method is called:
    brazeUser.setCustomUserAttributeToNow("your_attribute_key");
    // This method will assign the date specified by SECONDS_FROM_EPOCH to a custom attribute:
    brazeUser.setCustomUserAttributeToSecondsFromEpoch("your_attribute_key", SECONDS_FROM_EPOCH);
  }
});
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  brazeUser.setCustomUserAttribute("your_attribute_key", YOUR_DATE_VALUE)
  // This method will assign the current time to a custom attribute at the time the method is called:
  brazeUser.setCustomUserAttributeToNow("your_attribute_key")
  // This method will assign the date specified by SECONDS_FROM_EPOCH to a custom attribute:
  brazeUser.setCustomUserAttributeToSecondsFromEpoch("your_attribute_key", SECONDS_FROM_EPOCH)
}
```

{% endsubtab %}
{% endsubtabs %}

{% alert warning %}
この方法でBrazeに渡される日付は、[ISO 8601](http://en.wikipedia.org/wiki/ISO_8601)形式（e.g `2013-07-16T19:20:30+01:00`）または`yyyy-MM-dd'T'HH:mm:ss:SSSZ`形式（e.g `2016-12-14T13:32:31.601-0800`）のいずれかでなければなりません。
{% endalert %}

{% endtab %}
{% tab 配列 %}

カスタム属性配列内の要素の最大数は、25にデフォルト設定されています。個々の配列の最大値は、Braze ダッシュボードの [**データ設定**] > [**カスタム属性**] で100まで増やすことができます。要素の最大数を超える配列は、含まれる要素が最大数になるよう切り捨てられます。カスタム属性配列とその動作の詳細については、[配列に関する]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#arrays)ドキュメントを参照してください。

{% subtabs global %}
{% subtab JAVA %}

```java
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
  @Override
  public void onSuccess(BrazeUser brazeUser) {
    // Setting a custom attribute with an array value
    brazeUser.setCustomAttributeArray("your_attribute_key", testSetArray);
    // Adding to a custom attribute with an array value
    brazeUser.addToCustomAttributeArray("your_attribute_key", "value_to_add");
    // Removing a value from an array type custom attribute
    brazeUser.removeFromCustomAttributeArray("your_attribute_key", "value_to_remove");
  }
});
```
{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  // Setting a custom attribute with an array value
  brazeUser.setCustomAttributeArray("your_attribute_key", testSetArray)
  // Adding to a custom attribute with an array value
  brazeUser.addToCustomAttributeArray("your_attribute_key", "value_to_add")
  // Removing a value from an array type custom attribute
  brazeUser.removeFromCustomAttributeArray("your_attribute_key", "value_to_remove")
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### カスタム属性の設定を解除する

カスタム属性を解除するには、`unsetCustomUserAttribute` メソッドに関連する属性キーを渡す。

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
  @Override
  public void onSuccess(BrazeUser brazeUser) {
    brazeUser.unsetCustomUserAttribute("your_attribute_key");
  }
});
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  brazeUser.unsetCustomUserAttribute("your_attribute_key")
}
```

{% endtab %}
{% endtabs %}

### 階層化カスタム属性

また、カスタム属性の中にプロパティを入れ子にすることもできる。以下の例では、階層化プロパティを持つ`favorite_book` オブジェクトが、ユーザープロファイルのカスタム属性として設定されている。詳しくは、[階層化カスタム]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support)属性を参照のこと。

{% tabs %}
{% tab JAVA %}
```java
JSONObject favoriteBook = new JSONObject();
try {
  favoriteBook.put("title", "The Hobbit");
  favoriteBook.put("author", "J.R.R. Tolkien");
  favoriteBook.put("publishing_date", "1937");
} catch (JSONException e) {
  e.printStackTrace();
}

braze.getCurrentUser(user -> {
  user.setCustomUserAttribute("favorite_book", favoriteBook);
  return null;
});
```
{% endtab %}

{% tab KOTLIN %}
```kotlin
val favoriteBook = JSONObject()
  .put("title", "The Hobbit")
  .put("author", "J.R.R. Tolkien")
  .put("publishing_date", "1937")

braze.getCurrentUser { user ->
  user.setCustomUserAttribute("favorite_book", favoriteBook)
}
```
{% endtab %}
{% endtabs %}

### REST API の使用

また、REST APIを使用して、ユーザー属性を設定または解除することもできる。詳細については、[ユーザーデータエンドポイント]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data)を参照してください。

## ユーザーサブスクリプションの設定

ユーザーのサブスクリプション (メールまたはプッシュ) を設定するには、それぞれ関数 `setEmailNotificationSubscriptionType()` または `setPushNotificationSubscriptionType()` を呼び出します。これらの関数では、いずれも引数として列挙型 `NotificationSubscriptionType` が使用されます。この型には、次の 3 つの状態があります。

| サブスクリプションステータス | 定義 |
| ------------------- | ---------- |
| `OPTED_IN` | 配信登録済み、かつ明示的にオプトイン済み |
| `SUBSCRIBED` | 購読済み、ただし明示的に選択されていない |
| `UNSUBSCRIBED` | 配信停止済みまたは明示的にオプトアウト済み、あるいはその両方 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Android では、ユーザーにプッシュ通知を送る際に明示的なオプトインは必要ありません。ユーザーがプッシュ登録されると、デフォルトで`OPTED_IN`ではなく`SUBSCRIBED`に設定されます。サブスクリプションと明示的オプトインの実装の詳細については、[ユーザーサブスクリプションの管理]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions)を参照してください。
{% endalert %}

### メールサブスクリプションの設定

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
  @Override
  public void onSuccess(BrazeUser brazeUser) {
    brazeUser.setEmailNotificationSubscriptionType(emailNotificationSubscriptionType);
  }
});
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  brazeUser.setEmailNotificationSubscriptionType(emailNotificationSubscriptionType)
}
```

{% endtab %}
{% endtabs %}

### プッシュ通知サブスクリプションの設定

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
  @Override
  public void onSuccess(BrazeUser brazeUser) {
    brazeUser.setPushNotificationSubscriptionType(pushNotificationSubscriptionType);
  }
});
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  brazeUser.setPushNotificationSubscriptionType(pushNotificationSubscriptionType)
}
```

{% endtab %}
{% endtabs %}

