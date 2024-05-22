---
nav_title: ユーザー ID の設定
article_title: Unity のユーザー ID の設定
platform: 
  - Unity
  - iOS
  - Android
page_order: 0
description: "このリファレンス記事では、推奨される命名規則やベストプラクティスなど、Unity プラットフォームでユーザー ID を設定する方法について説明します。"
 
---

# ユーザー ID の設定

> このリファレンス記事では、推奨される命名規則やベストプラクティスなど、Unity プラットフォームでユーザー ID を設定する方法について説明します。

{% multi_lang_include archive/setting_user_ids/setting_user_ids.md %}

ユーザー ID を設定するため、ユーザが識別された直後 (一般的にはログイン後) に以下の呼び出しを行う必要があります。

```csharp
AppboyBinding.ChangeUser("YOUR_USER_ID_STRING");
```

{% alert warning %}
**ユーザーがログアウトするときに `ChangeUser()` を呼び出さないでください。`ChangeUser()` は、ユーザーがアプリケーションにログインするときにのみ呼び出される必要があります。**`ChangeUser()`を静的なデフォルト値に設定すると、ユーザーが再度ログインするまで、すべてのユーザーアクティビティがそのデフォルト「ユーザー」に関連付けられます。
{% endalert %}

また、ユーザーがログアウトするときにユーザー ID を変更しないでください。変更すると、以前にログインしたユーザーを再エンゲージメントキャンペーンでターゲットにできなくなるためです。同じデバイスに複数のユーザーが存在することが予想されるものの、アプリがログアウト状態の間にそのうちの 1 ユーザーのみをターゲットにする場合は、ログアウト中にターゲットにするユーザー ID を個別に追跡し、アプリのログアウトプロセスの中でそのユーザー ID に戻すことをお勧めします。

## 推奨されるユーザー ID の命名規則

{% multi_lang_include archive/setting_user_ids/naming_convention.md %}

## ユーザー ID 統合のベストプラクティスとメモ

{% multi_lang_include archive/setting_user_ids/best_practices.md %}

[1]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
[2]: {{site.baseurl}}/api/endpoints/messaging/
