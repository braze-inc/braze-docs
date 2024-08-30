---
nav_title: バッジ
article_title: iOS のプッシュ通知バッジ数
platform: Swift
page_order: 2
description: "この記事では、SWIFT SDKのiOSバッジカウントの実装方法について説明します。"
channel:
  - push

---

# バッジ

> バッジは小さなアイコンで、ユーザーの注意を引くのに最適です。Brazeのダッシュボードを使用してプッシュ通知を作成する際に、[**設定**][1]タブでバッジカウントを指定できます。アプリケーションの [`applicationIconBadgeNumber`][20] プロパティまたは[リモート通知ペイロード][21]を使用して、バッジ数を手動で更新することもできます。 

Brazeは、アプリがフォアグラウンドにあるときにBraze通知を受信すると、バッジカウントを自動的にクリアします。バッジ番号を手動で0に設定すると、通知センターの通知もクリアされます。 

通常のアプリ操作の一部として、またはバッジをクリアするプッシュを送信してバッジをクリアする計画がない場合は、次のコードをアプリの `applicationDidBecomeActive:` デリゲートメソッドに追加してアプリがアクティブになったときにバッジをクリアする必要があります。

{% tabs %}
{% tab SWIFT %}

```swift
// For iOS 16.0+
let center = UNUserNotificationCenter.current()
do {
  try await center.setBadgeCount(0)
} catch {
  // Handle errors
}

// Prior to iOS 16. Deprecated in iOS 17+.
UIApplication.shared.applicationIconBadgeNumber = 0
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
// For iOS 16.0+
UNUserNotificationCenter *center = [UNUserNotificationCenter currentNotificationCenter];
[center setBadgeCount:0 withCompletionHandler:^(NSError * _Nullable error) {
    if (error != nil) {
        // Handle errors
    }
}];

// Prior to iOS 16. Deprecated in iOS 17+.
[UIApplication sharedApplication].applicationIconBadgeNumber = 0;
```

{% endtab %}
{% endtabs %}

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/advanced_settings/
[20]: https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIApplication_Class/index.html#//apple_ref/occ/instp/UIApplication/applicationIconBadgeNumber
[21]: https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/CreatingtheNotificationPayload.html#//apple_ref/doc/uid/TP40008194-CH10-SW1