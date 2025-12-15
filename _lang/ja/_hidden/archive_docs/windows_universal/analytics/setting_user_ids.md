---
nav_title: ユーザー ID の設定
article_title: Windows UniversalのユーザーIDを設定する
platform: Windows Universal
page_order: 1
description: "このリファレンス記事では、WindowsユニバーサルプラットフォームでユーザーIDを設定する方法について説明する。"
hidden: true
---

# ユーザー ID の設定
{% multi_lang_include archive/windows_deprecation.md %}

{% multi_lang_include archive/setting_user_ids/setting_user_ids.md %}

ユーザーが識別されたらすぐに (通常はログイン後)、次の呼び出しを行ってユーザー ID を設定する必要があります。

```csharp
Appboy.SharedInstance.ChangeUser(YOUR_USER_ID_STRING);
```

{% alert warning %}
**ユーザーがログアウトするときに `changeUser()` を呼び出さないでください。`changeUser()` は、ユーザーがアプリケーションにログインするときにのみ呼び出される必要があります。**`changeUser()`を静的なデフォルト値に設定すると、ユーザーが再度ログインするまで、すべてのユーザーアクティビティがそのデフォルト「ユーザー」に関連付けられます。
{% endalert %}

また、ユーザーがログアウトするときにユーザー ID を変更しないでください。変更すると、以前にログインしたユーザーを再エンゲージメントキャンペーンでターゲットにできなくなるためです。同じデバイスに複数のユーザーが存在することが予想されるものの、アプリがログアウト状態の間にそのうちの1ユーザーのみをターゲットにする場合は、ログアウト中にターゲットにするユーザー ID を個別に追跡し、アプリのログアウトプロセスの中でそのユーザー ID に戻すことをお勧めします。

## 推奨されるユーザー ID の命名規則

{% multi_lang_include archive/setting_user_ids/naming_convention.md %}

## ユーザー ID 統合のベストプラクティスとメモ

{% multi_lang_include archive/setting_user_ids/best_practices.md %}

