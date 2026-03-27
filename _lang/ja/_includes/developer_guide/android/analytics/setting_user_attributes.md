{% multi_lang_include developer_guide/prerequisites/android.md %}

## デフォルトのユーザー属性

### 事前定義されたメソッド

Brazeは、[`BrazeUser`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/index.html)クラス内で以下のユーザー属性を設定するための事前定義されたメソッドを提供しています。メソッド仕様については、[KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/index.html)を参照してください。

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

ユーザーにデフォルト属性を設定するには、Brazeインスタンスの`getCurrentUser()`メソッドを呼び出して、アプリの現在のユーザーへの参照を取得します。その後、メソッドを呼び出してユーザー属性を設定できます。

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

### デフォルト属性の解除

ユーザー属性を解除するには、該当するメソッドに`null`を渡します。

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

デフォルトのユーザー属性に加えて、Brazeでは複数の異なるデータタイプを使用してカスタム属性を定義することもできます。各属性のセグメンテーションオプションの詳細については、[データ収集]({{site.baseurl}}/developer_guide/analytics)を参照してください。

### カスタム属性の設定

{% tabs local %}
{% tab String %}
カスタム属性を`string`値で設定するには：

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
{% tab Integers %}
カスタム属性を`int`値で設定するには：

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

カスタム属性を`long`整数値で設定するには：

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
{% tab Floating-points %}
カスタム属性を`float`値で設定するには：

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

カスタム属性を`double`値で設定するには：

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
カスタム属性を`boolean`値で設定するには：

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

{% tab Date %}
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
このメソッドでBrazeに渡される日付は、[ISO 8601](http://en.wikipedia.org/wiki/ISO_8601)形式（例：`2013-07-16T19:20:30+01:00`）または`yyyy-MM-dd'T'HH:mm:ss:SSSZ`形式（例：`2016-12-14T13:32:31.601-0800`）のいずれかである必要があります。
{% endalert %}

{% endtab %}
{% tab Array %}

配列内の要素のデフォルトおよび最大数は500です。最大数はBrazeダッシュボードの**データ設定** > **カスタム属性**で更新できます。要素数が最大値を超える配列は、最大要素数に切り詰められます。カスタム属性配列とその動作の詳細については、[配列]({{site.baseurl}}/developer_guide/analytics/#arrays)を参照してください。

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

### カスタム属性の設定解除

カスタム属性を解除するには、該当する属性キーを`unsetCustomUserAttribute`メソッドに渡します。

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

カスタム属性内にプロパティをネストすることもできます。次の例では、ネストされたプロパティを持つ`favorite_book`オブジェクトが、ユーザープロファイルのカスタム属性として設定されます。詳細については、[階層化カスタム属性]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support)を参照してください。

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

### REST APIの使用

ユーザー属性の設定や解除には、REST APIも使用できます。詳細については、[ユーザーデータエンドポイント]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data)を参照してください。

## ユーザーサブスクリプションの設定

ユーザーのサブスクリプション（メールまたはプッシュ）を設定するには、それぞれ`setEmailNotificationSubscriptionType()`関数または`setPushNotificationSubscriptionType()`関数を呼び出します。これらの関数はいずれも引数として列挙型`NotificationSubscriptionType`を受け取ります。この型には、次の3つの状態があります。

| サブスクリプションステータス | 定義 |
| ------------------- | ---------- |
| `OPTED_IN` | 配信登録済み、かつ明示的にオプトイン済み |
| `SUBSCRIBED` | 購読中、ただし明示的にオプトインしていない |
| `UNSUBSCRIBED` | 配信停止済みまたは明示的にオプトアウト済み、あるいはその両方 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Androidでは、ユーザーにプッシュ通知を送信する際に明示的なオプトインは必要ありません。ユーザーがプッシュ登録されると、デフォルトで`OPTED_IN`ではなく`SUBSCRIBED`に設定されます。サブスクリプションと明示的オプトインの実装の詳細については、[ユーザーサブスクリプションの管理]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions)を参照してください。
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