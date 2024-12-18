---
nav_title: ユーザー ID の設定
article_title: iOS のユーザー ID の設定
platform: iOS
page_order: 1
description: "このリファレンス記事では、iOS アプリでユーザー ID を設定する方法、推奨されるユーザー ID の命名規則、およびベストプラクティスをいくつか示します。"
 
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# iOS のユーザー ID の設定

{% multi_lang_include archive/setting_user_ids/setting_user_ids.md %}

## 推奨されるユーザー ID の命名規則

{% multi_lang_include archive/setting_user_ids/naming_convention.md %}

## ユーザー ID の割り当て

ユーザーが識別されたらすぐに (通常はログイン後)、次の呼び出しを行ってユーザー ID を設定する必要があります。

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance] changeUser:@"YOUR_USER_ID_STRING"];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.changeUser("YOUR_USER_ID")
```

{% endtab %}
{% endtabs %}

{% alert warning %}
**ユーザーがログアウトするときに `changeUser()` を呼び出さないでください。`changeUser()` の呼び出しは、ユーザーがアプリケーションにログインするときにのみ行う必要があります。**[`changeUser()`](https://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#ac8b369b40e15860b0ec18c0f4b46ac69%20%22changeuser%22) を静的なデフォルト値に設定すると、ユーザーが再度ログインするまで、すべてのユーザーアクティビティがそのデフォルト「ユーザー」に関連付けられます。
{% endalert %}

このメソッドはアプリケーションのメインスレッドで呼び出してください。メソッドを非同期的に呼び出すと、定義されていない動作が生じる可能性があります。

また、ユーザーがログアウトするときにユーザー ID を変更しないでください。変更すると、以前にログインしたユーザーを再エンゲージメントキャンペーンでターゲットにできなくなるためです。同じデバイスに複数のユーザーが存在することが予想されるものの、アプリがログアウト状態の間にそのうちの 1 ユーザーのみをターゲットにする場合は、ログアウト中にターゲットにするユーザー ID を個別に追跡し、アプリのログアウトプロセスの中でそのユーザー ID に戻すことをお勧めします。

## ユーザー ID 統合のベストプラクティスとメモ

{% multi_lang_include archive/setting_user_ids/best_practices.md %}

## ユーザーのエイリアシング

{% multi_lang_include archive/setting_user_ids/aliasing.md platform="iOS" %}

