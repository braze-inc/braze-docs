---
nav_title: 内部プッシュ通知の無視
article_title: iOS 向け Braze 内部プッシュ通知の無視
platform: Swift
page_order: 6
description: "この記事では、Swift SDK のBraze 内部プッシュ通知を無視する方法について説明します。"
channel:
  - push

---

# 内部プッシュ通知の無視

> Braze は、特定の高度な機能の内部実装に[サイレントプッシュ通知][2]を使用します。ほとんどの統合では、アプリに代わって変更を行う必要はありません。ただし、内部プッシュ通知に依存する Braze 機能(アンインストールのトラッキングやジオフェンスなど)を統合する場合は、アプリケーションを更新して、 Braze からの内部プッシュを無視することができます。

アプリケーションの起動時またはバックグラウンドプッシュ時にアプリケーションが自動アクションを実行する場合は、内部プッシュ通知によってトリガーされないようにそのアクティビティをゲートすることを検討してください。たとえば、すべてのバックグラウンドプッシュまたはアプリケーションの起動時に新しいコンテンツのためにサーバーを呼び出すロジックがある場合、不要なネットワークトラフィックが発生するため、Braze の内部プッシュトリガーを使用しないことがあります。さらに、Braze は特定の種類の内部プッシュをすべてのユーザーにほぼ同時に送信するため、起動時に内部プッシュからのネットワーク呼び出しをゲートしないと、サーバーに重大な負荷がかかる可能性があります。

## アプリの自動アクションを確認する

以下の箇所で自動アクションがないかアプリケーションをチェックし、Braze の内部プッシュを無視するようにコードを更新します。

1. **プッシュレシーバー。**バックグラウンドプッシュ通知により、`UIApplicationDelegate` の `application:didReceiveRemoteNotification:fetchCompletionHandler:` が呼び出されます。
2. **アプリケーションデリゲート。**バックグラウンドプッシュにより、中断されたアプリがバックグラウンドで起動し、`UIApplicationDelegate` の `application:willFinishLaunchingWithOptions:` および `application:didFinishLaunchingWithOptions:` メソッドがトリガーされます。これらのメソッドの `launchOptions` をチェックして、アプリケーションがバックグラウンドプッシュから起動されたかどうかを判断できます。

## 内部プッシュ・ユーティリティ・メソッドの使用

`Braze.Notifications` の静的ユーティリティメソッドを使用して、アプリがBraze 内部プッシュによって受信されたか、起動されたかどうかを確認できます。[`Braze.Notifications.isInternalNotification(_:)`][1] は、アンインストールの追跡、機能フラグの同期、およびジオフェンスの同期通知を含むすべてのBraze 内部プッシュ通知で`true` を返します。

## 実装例 {#internal-push-implementation-example}

{% tabs %}
{% tab swift %}


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

[1]: https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/notifications-swift.class/isinternalnotification(_:)
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/
[4]: https://developer.apple.com/documentation/uikit/app_and_environment/managing_your_app_s_life_cycle