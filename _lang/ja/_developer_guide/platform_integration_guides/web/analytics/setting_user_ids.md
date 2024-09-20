---
nav_title: ユーザー ID の設定
article_title: ウェブのユーザーIDを設定する
platform: Web
page_order: 1
page_type: reference
description: "この記事では、ベストプラクティスや変更を行う前に考慮すべき重要な点を含め、各ユーザにユーザIDを設定する方法について説明する。"
 
---

# ユーザー ID の設定

> この記事では、ベストプラクティスや変更を行う前に考慮すべき重要な点を含め、各ユーザにユーザIDを設定する方法について説明する。

{% multi_lang_include archive/setting_user_ids/setting_user_ids.md %}

ユーザーが識別されたらすぐに (通常はログイン後)、次の呼び出しを行ってユーザー ID を設定する必要があります。

```javascript
braze.changeUser(YOUR_USER_ID_STRING);
```

{% alert warning %}
**ユーザーがログアウトしたときに`changeUser()` 。**`changeUser()`を静的なデフォルト値に設定すると、ユーザーが再度ログインするまで、すべてのユーザーアクティビティがそのデフォルト「ユーザー」に関連付けられます。
{% endalert %}

ユーザーがログアウトした際にユーザーIDを変更することは、以前ログインしていたユーザーをターゲットとしたリエンゲージメントキャンペーンができなくなるため、お勧めしない。同じデバイスに複数のユーザーが存在することが予想されるものの、アプリがログアウト状態の間にそのうちの1ユーザーのみをターゲットにする場合は、ログアウト中にターゲットにするユーザー ID を個別に追跡し、アプリのログアウトプロセスの中でそのユーザー ID に戻すことをお勧めします。

詳細については、[`changeUser()` のドキュメント][4]を参照してください。

## 推奨されるユーザー ID の命名規則

{% multi_lang_include archive/setting_user_ids/naming_convention.md %}

## ユーザー ID 統合のベストプラクティスとメモ

{% multi_lang_include archive/setting_user_ids/best_practices.md %}

## ユーザーのエイリアシング

{% multi_lang_include archive/setting_user_ids/aliasing.md platform="Web" %}

[1]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
[2]: {{site.baseurl}}/api/endpoints/messaging/
[4]: https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser "Javadocs（ジャバドックス"
[5]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases
