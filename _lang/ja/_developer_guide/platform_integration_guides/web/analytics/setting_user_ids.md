---
nav_title: ユーザー ID の設定
article_title: ウェブ用ユーザ ID の設定
platform: Web
page_order: 1
page_type: reference
description: "この記事では、ベストプラクティスや変更を加える前に考慮すべき重要な点など、各ユーザーのユーザー ID を設定する方法について説明します。"
 
---

# ユーザー ID の設定

> この記事では、ベストプラクティスや変更を加える前に考慮すべき重要な点など、各ユーザーのユーザー ID を設定する方法について説明します。

{% multi_lang_include archive/setting_user_ids/setting_user_ids.md %}

ユーザーが識別されたらすぐに (通常はログイン後)、次の呼び出しを行ってユーザー ID を設定する必要があります。

```javascript
braze.changeUser(YOUR_USER_ID_STRING);
```

{% alert warning %}
**`changeUser()`ユーザーがログアウトしても呼び出さないでください。**`changeUser()`を静的なデフォルト値に設定すると、ユーザーが再度ログインするまで、すべてのユーザーアクティビティがそのデフォルト「ユーザー」に関連付けられます。
{% endalert %}

ユーザーがログアウトしたときにユーザー ID を変更しないことをお勧めします。変更すると、以前にログインしたユーザーをリエンゲージメントキャンペーンでターゲットにできなくなります。同じデバイスに複数のユーザーが存在することが予想されるものの、アプリがログアウト状態の間にそのうちの1ユーザーのみをターゲットにする場合は、ログアウト中にターゲットにするユーザー ID を個別に追跡し、アプリのログアウトプロセスの中でそのユーザー ID に戻すことをお勧めします。

詳細については、[`changeUser()` のドキュメント][4]を参照してください。

## 推奨されるユーザー ID の命名規則

{% multi_lang_include archive/setting_user_ids/naming_convention.md %}

## ユーザー ID 統合のベストプラクティスとメモ

{% multi_lang_include archive/setting_user_ids/best_practices.md %}

## ユーザーのエイリアシング

{% multi_lang_include archive/setting_user_ids/aliasing.md platform="Web" %}

[1]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
[2]: {{site.baseurl}}/api/endpoints/messaging/
[4]: https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser "Javadocs"
[5]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases
