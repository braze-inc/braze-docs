---
nav_title: ユーザーIDの設定
article_title: Windows ユニバーサルのユーザー ID の設定
platform: Windows Universal
page_order: 1
description: "このリファレンス記事では、Windows ユニバーサル プラットフォームでユーザー ID を設定する方法について説明します。"
hidden: true
---

# ユーザーIDの設定
{% multi_lang_include archive/windows_deprecation.md %}

{% multi_lang_include archive/setting_user_ids/setting_user_ids.md %}

ユーザーが識別されたらすぐに (通常はログイン後) 次の呼び出しを実行して、ユーザー ID を設定する必要があります。

```csharp
Appboy.SharedInstance.ChangeUser(YOUR_USER_ID_STRING);
```

{% alert warning %}
**電話はしないで下さい `changeUser()` ユーザーがログアウトしたとき。 `changeUser()` ユーザーがアプリケーションにログインしたときにのみ呼び出されます。**設定 `changeUser()` 静的なデフォルト値に設定すると、ユーザーが再度ログインするまで、すべてのユーザー アクティビティがそのデフォルトの「ユーザー」に関連付けられます。
{% endalert %}

さらに、ユーザーがログアウトしたときにユーザー ID を変更することはお勧めしません。変更すると、再エンゲージメント キャンペーンで以前ログインしていたユーザーをターゲットにすることができなくなるためです。同じデバイスに複数のユーザーがいることが予想されるが、アプリがログアウト状態のときにそのうちの 1 人のユーザーのみをターゲットにしたい場合は、ログアウト中にターゲットにするユーザー ID を別途追跡し、アプリのログアウト プロセスの一環としてそのユーザー ID に切り替えることをお勧めします。

## 推奨されるユーザーIDの命名規則

{% multi_lang_include archive/setting_user_ids/naming_convention.md %}

## ユーザーID統合のベストプラクティスと注意事項

{% multi_lang_include archive/setting_user_ids/best_practices.md %}

[1]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
[2]: {{site.baseurl}}/developer_guide/rest_api/messaging/
[6]: http://developer.android.com/reference/java/util/Locale.html#default_locale "Android 開発者向けドキュメント - ローカリゼーション"
