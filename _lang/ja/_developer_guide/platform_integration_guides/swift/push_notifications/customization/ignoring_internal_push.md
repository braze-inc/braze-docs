---
nav_title: 内部プッシュ通知の無視
article_title: iOS 向け Braze 内部プッシュ通知の無視
platform: Swift
page_order: 6
description: "この参考記事では、Swift SDK に関して、Braze の内部プッシュ通知を無視する方法について説明します。"
channel:
  - push

---

# 内部 プッシュ通知を無視する

> Braze は、特定の高度な機能の内部インプリメンテーションに[サイレントプッシュ通知]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/)を使用します。ほとんどの統合では、アプリに代わって変更を行う必要はありません。ただし、内部プッシュ通知に依存する Braze 機能 (アンインストール追跡やジオフェンスなど) を統合する場合は、Braze から内部プッシュ通知を無視するようにアプリを更新することが必要になる場合があります。

アプリで、アプリケーションの起動またはバックグラウンドプッシュで自動アクションが実行される場合は、内部プッシュ通知によってトリガーされないように、そのアクティビティをゲートすることを検討する必要があります。たとえば、すべてのバックグラウンドプッシュまたはアプリケーションの起動時に新しいコンテンツのためにサーバーを呼び出すロジックがある場合、不要なネットワークトラフィックが発生するため、Braze の内部プッシュトリガーを使用しないことがあります。さらに、Braze は特定の種類の内部プッシュをすべてのユーザーにほぼ同時に送信するため、起動時に内部プッシュからのネットワーク呼び出しをゲートしないと、サーバーに重大な負荷がかかる可能性があります。

## アプリの自動アクションを確認する

次の場所でアプリケーションの自動アクションを確認し、Braze の内部プッシュを無視するようにコードを更新します。

1. **プッシュレシーバー。**バックグラウンドプッシュ通知により、`UIApplicationDelegate` の `application:didReceiveRemoteNotification:fetchCompletionHandler:` が呼び出されます。
2. **アプリケーションデリゲート。**バックグラウンドプッシュにより、[中断された](https://developer.apple.com/documentation/uikit/app_and_environment/managing_your_app_s_life_cycle)アプリがバックグラウンドで起動し、`UIApplicationDelegate` の `application:willFinishLaunchingWithOptions:` および `application:didFinishLaunchingWithOptions:` メソッドがトリガーされます。これらのメソッドの `launchOptions` をチェックして、アプリケーションがバックグラウンドプッシュから起動されたかどうかを判断できます。

## 内部プッシュユーティリティメソッドの使用

`Braze.Notifications` の静的ユーティリティメソッドを使用して、アプリが Braze の内部プッシュを受信したかを確認できます。[`Braze.Notifications.isInternalNotification(_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/notifications-swift.class/isinternalnotification(_:)) はすべての Braze 内部プッシュ通知で `true` を返します。これには、アンインストール追跡、フィーチャーフラグ同期、ジオフェンス同期通知が含まれます。

## 実装例 {#internal-push-implementation-example}

{% tabs %}
{% tab SWIFT %}


```swift
func application(_ application: UIApplication,
                 didReceiveRemoteNotification userInfo: [AnyHashable : Any],
                 fetchCompletionHandler completionHandler: @escaping (UIBackgroundFetchResult) -> Void) {
  if (!Braze.Notifications.isInternalNotification(userInfo)) {
    // Gated logic here (for example pinging server for content)
  }
}
```

{% endtab %}
{% tab OBJECTIVE-C %}


```objc
- (void)application:(UIApplication *)application didReceiveRemoteNotification:(NSDictionary *)userInfo fetchCompletionHandler:(void (^)(UIBackgroundFetchResult result))completionHandler {
  if (![BRZNotifications isInternalNotification:userInfo]) {
    // Gated logic here (for example pinging server for content)
  }
}
```

{% endtab %}
{% endtabs %}

