---
nav_title: 内部プッシュ通知の無視
article_title: iOS 向け Braze 内部プッシュ通知の無視
platform: iOS
page_order: 4
description: "この参考記事では、Braze の内部プッシュ通知を無視する方法について説明します。"
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Braze 内部プッシュ通知を無視する

Braze は、特定の高度な機能の内部実装にサイレントプッシュ通知を使用します。ほとんどの統合では、アプリに代わって変更を行う必要はありません。ただし、内部プッシュ通知に依存する Braze 機能 (アンインストール追跡やジオフェンスなど) を統合する場合は、内部プッシュ通知を無視するようにアプリを更新することが必要になる場合があります。

アプリで、アプリケーションの起動またはバックグラウンドプッシュで自動アクションが実行される場合は、\\ 内部プッシュ通知によってトリガーされないように、そのアクティビティをゲートすることを検討する必要があります。たとえば、バックグラウンドプッシュまたはアプリケーションの起動のたびに新しいコンテンツを取得するためにサーバーを呼び出すロジックがある場合、不要なネットワーク トラフィックが発生するため、内部プッシュによってそれがトリガーされることは望ましくないでしょう。さらに、Braze は特定の種類の内部プッシュをすべてのユーザーにほぼ同時に送信するため、起動時に内部プッシュからのネットワーク呼び出しをゲートしないと、サーバーに重大な負荷がかかる可能性があります。

## アプリの自動アクションを確認する

次の場所でアプリケーションの自動アクションを確認し、内部プッシュを無視するようにコードを更新する必要があります。

1. **プッシュレシーバー。**バックグラウンドプッシュ通知により、`UIApplicationDelegate` の `application:didReceiveRemoteNotification:fetchCompletionHandler:` が呼び出されます。
2. **アプリケーションデリゲート。**バックグラウンドプッシュにより、[中断された](https://developer.apple.com/library/ios/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/TheAppLifeCycle/TheAppLifeCycle.html#//apple_ref/doc/uid/TP40007072-CH2-SW3)アプリがバックグラウンドで起動し、`UIApplicationDelegate` の `application:willFinishLaunchingWithOptions:` および `application:didFinishLaunchingWithOptions:` メソッドがトリガーされます。これらのメソッドの `launchOptions` をチェックして、アプリケーションがバックグラウンドプッシュから起動されたかどうかを判断できます。

## Braze 内部プッシュユーティリティ メソッドの使用

`ABKPushUtils` のユーティリティーメソッドを使用して、アプリが Braze の内部プッシュを受信したか、または Braze の内部プッシュによって起動されたかを確認できます。`isAppboyInternalRemoteNotification:` はすべての Braze 内部プッシュ通知で `YES` を返し、`isUninstallTrackingRemoteNotification:` と `isGeofencesSyncRemoteNotification:` はそれぞれアンインストール追跡とジオフェンス同期通知で `YES` を返します。メソッド宣言については、[`ABKPushUtils.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKPushUtils.h) を参照してください。

## 実装例 {#internal-push-implementation-example}

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  NSDictionary *pushDictionary = launchOptions[UIApplicationLaunchOptionsRemoteNotificationKey];
  BOOL launchedFromAppboyInternalPush = pushDictionary && [ABKPushUtils isAppboyInternalRemoteNotification:pushDictionary];
  if (!launchedFromAppboyInternalPush) {
    // ... Gated logic here (such as pinging your server to download content) ...
  }
}
```

```objc
- (void)application:(UIApplication *)application didReceiveRemoteNotification:(NSDictionary *)userInfo fetchCompletionHandler:(void (^)(UIBackgroundFetchResult result))completionHandler {
  if (![ABKPushUtils isAppboyInternalRemoteNotification:userInfo]) {
    // ... Gated logic here (such as pinging server for content) ...
  }
}
```

{% endtab %}
{% tab swift %}

```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplicationLaunchOptionsKey : Any]? = nil) -> Bool {
  let pushDictionary = launchOptions?[UIApplicationLaunchOptionsKey.remoteNotification] as? NSDictionary as? [AnyHashable : Any] ?? [:]
  let launchedFromAppboyInternalPush = ABKPushUtils.isAppboyInternalRemoteNotification(pushDictionary)
  if (!launchedFromAppboyInternalPush) {
    // ... Gated logic here (such as pinging your server to download content) ...
  }
}
```

```swift
func application(_ application: UIApplication,
                 didReceiveRemoteNotification userInfo: [AnyHashable : Any],
                 fetchCompletionHandler completionHandler: @escaping (UIBackgroundFetchResult) -> Void) {
  if (!ABKPushUtils.isAppboyInternalRemoteNotification(userInfo)) {
    // ... Gated logic here (such as pinging server for content) ...
  }
}
```

{% endtab %}
{% endtabs %}

