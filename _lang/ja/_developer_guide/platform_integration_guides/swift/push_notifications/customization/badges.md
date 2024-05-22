---
nav_title: バッジ
article_title: iOS のプッシュ通知バッジ数
platform: Swift
page_order: 2
description: "この記事では、Swift SDKにiOSのバッジカウントを実装する方法を説明します。"
channel:
  - push

---

# バッジ

> バッジは小さなアイコンで、ユーザーの注意を引くのに最適です。バッジの数は [**設定**][1]タブで指定できます。アプリケーションの [`applicationIconBadgeNumber`][20] プロパティまたは[リモート通知ペイロード][21]を使用して、バッジ数を手動で更新することもできます。 

Brazeは、アプリがフォアグラウンドの状態でBraze通知を受信すると、自動的にバッジカウントをクリアします。手動でバッジ番号を0に設定すると、通知センターの通知も消去されます。 

通常のアプリ操作の一部として、またはバッジをクリアするプッシュを送信してバッジをクリアする計画がない場合は、次のコードをアプリの `applicationDidBecomeActive:` デリゲートメソッドに追加してアプリがアクティブになったときにバッジをクリアする必要があります。

{% tabs %}
{% tab swift %}

```swift
UIApplication.shared.applicationIconBadgeNumber = 0
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
[UIApplication sharedApplication].applicationIconBadgeNumber = 0;
```

{% endtab %}
{% endtabs %}

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/advanced_settings/
[20]: https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIApplication_Class/index.html#//apple_ref/occ/instp/UIApplication/applicationIconBadgeNumber
[21]: https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/CreatingtheNotificationPayload.html#//apple_ref/doc/uid/TP40008194-CH10-SW1