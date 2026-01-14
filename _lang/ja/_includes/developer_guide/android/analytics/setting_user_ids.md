 
# ユーザー ID の設定
 
> このリファレンス記事では、Android または FireOS アプリでユーザー ID を設定する方法、推奨されるユーザー ID 命名規則、およびいくつかのベストプラクティスを説明します。

{% multi_lang_include archive/setting_user_ids/setting_user_ids.md %}

## 推奨されるユーザー ID の命名規則

{% multi_lang_include archive/setting_user_ids/naming_convention.md %}

### ユーザー ID の割り当て

ユーザー ID を設定するため、ユーザが識別された直後 (一般的にはログイン後) に以下の呼び出しを行う必要があります。

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).changeUser(YOUR_USER_ID_STRING);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).changeUser(YOUR_USER_ID_STRING)
```

{% endtab %}
{% endtabs %}

{% alert warning %}
**ユーザーがログアウトするときに `changeUser()` を呼び出さないでください。`changeUser()` は、ユーザーがアプリケーションにログインするときにのみ呼び出される必要があります。**`changeUser()`を静的なデフォルト値に設定すると、ユーザーが再度ログインするまで、すべてのユーザーアクティビティがそのデフォルト「ユーザー」に関連付けられます。
{% endalert %}

また、ユーザーがログアウトするときにユーザー ID を変更**しない**ことをお勧めします。変更すると、以前にログインしたユーザーを再エンゲージメントキャンペーンでターゲットにできなくなるためです。同じデバイスに複数のユーザーが存在することが予想されるものの、アプリがログアウト状態の間にそのうちの1ユーザーのみをターゲットにする場合は、ログアウト中にターゲットにするユーザー ID を個別に追跡し、アプリのログアウトプロセスの中でそのユーザー ID に戻すことをお勧めします。

詳細については、[`changeUser` のドキュメント](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/change-user.html) を参照してください。

## ユーザー ID 統合のベストプラクティスとメモ

{% multi_lang_include archive/setting_user_ids/best_practices.md %}

## ユーザーのエイリアシング

{% multi_lang_include archive/setting_user_ids/aliasing.md platform="Android" %}

