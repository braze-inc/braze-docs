---
nav_title: ユーザー ID の設定
article_title: iOS のユーザー ID の設定
platform: Swift
page_order: 1
description: "この記事では、iOS アプリでユーザー ID を設定する方法、推奨されるユーザー ID の命名規則、およびいくつかのベストプラクティスを説明します。"
 
---

# ユーザー ID の設定

{% multi_lang_include archive/setting_user_ids/setting_user_ids.md %}

## 推奨されるユーザー ID の命名規則

{% multi_lang_include archive/setting_user_ids/naming_convention.md %}

## ユーザー ID の割り当て

ユーザー ID を設定するため、ユーザが識別された直後 (一般的にはログイン後) に以下の呼び出しを行う必要があります。

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.changeUser(userId: "YOUR_USER_ID")
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
[AppDelegate.braze changeUser:@"YOUR_USER_ID_STRING"];
```

{% endtab %}
{% endtabs %}

{% alert warning %}
**ユーザーがログアウトするときに `changeUser()` を呼び出さないでください。`changeUser()` は、ユーザーがアプリケーションにログインするときにのみ呼び出される必要があります。**[`changeUser()`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/changeuser%28userid%3Asdkauthsignature%3Afileid%3Aline%3A%29) を静的なデフォルト値に設定すると、ユーザーが再度ログインするまで、すべてのユーザーアクティビティがそのデフォルト「ユーザー」に関連付けられます。
{% endalert %}

また、ユーザーがログアウトするときにユーザー ID を変更しないことをお勧めします。変更すると、以前にログインしたユーザーを再エンゲージメントキャンペーンでターゲットにできなくなるためです。同じデバイスに複数のユーザーが存在することが予想されるものの、アプリがログアウト状態の間にそのうちの1ユーザーのみをターゲットにする場合は、ログアウト中にターゲットにするユーザー ID を個別に追跡し、アプリのログアウトプロセスの中でそのユーザー ID に戻すことをお勧めします。

## ユーザー ID 統合のベストプラクティスとメモ

{% multi_lang_include archive/setting_user_ids/best_practices.md %}

## ユーザーのエイリアシング

{% multi_lang_include archive/setting_user_ids/aliasing.md platform="Swift" %}

[1]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
[2]: {{site.baseurl}}/api/endpoints/messaging/
[5]: https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/changeuser%28userid%3Asdkauthsignature%3Afileid%3Aline%3A%29 "changeuser"
