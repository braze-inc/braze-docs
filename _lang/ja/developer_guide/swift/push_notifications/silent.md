{% multi_lang_include developer_guide/prerequisites/swift.md %} また、[プッシュ通知s]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift)を設定する必要があります。

## iOSの制限

iOS オペレーティングシステムは、一部の機能の通知をゲートする場合があります。これらの機能で問題が発生している場合は、iOS のサイレント通知ゲートが原因である可能性があることに注意してください。詳しくは、Apple の[インスタンスメソッド](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623013-application) および[未受信通知s](https://developer.apple.com/library/content/technotes/tn2265/_index.html#//apple_ref/doc/uid/DTS40010376-CH1-TNTAG23) ドキュメントを参照してください。

## サイレント・プッシュ通知を設定する

サイレント・プッシュ通知を使用してバックグラウンド作業をトリガーするには、アプリがバックグラウンドでも通知を受け取れるように設定する必要がある。これを行うには、Xcode で、[**署名 & 機能**] ペインを使ってメインアプリのターゲットにバックグラウンドモード機能を追加します。**リモート通知**チェックボックスを選択する。

![Xcode の [機能] の下に [リモート通知] モードのチェックボックスが表示されています。]({% image_buster /assets/img_archive/background_mode.png %} "background mode enabled")

リモート通知バックグラウンドモードが有効になっている場合でも、ユーザーがアプリケーションを強制終了した場合、システムはアプリをバックグラウンドで起動しません。システムによってアプリがバックグラウンドで自動的に起動される前に、ユーザーはアプリケーションを明示的に起動するか、デバイスを再起動する必要があります。

詳細については、[[バックグラウンド更新のプッシュ](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/pushing_background_updates_to_your_app)] および `application:didReceiveRemoteNotification:fetchCompletionHandler:` [[ドキュメント](https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIApplicationDelegate_Protocol/index.html#//apple_ref/occ/intfm/UIApplicationDelegate/application:didReceiveRemoteNotification:fetchCompletionHandler:)] を参照してください。

## サイレントプッシュ通知の送信

サイレントプッシュ通知を送信するには、プッシュ通知ペイロードで `content-available` フラグを `1` に設定します。 

{% alert note %}
Apple がリモート通知と呼ぶものは、`content-available` フラグが設定された通常のプッシュ通知です。
{% endalert %}

`content-available` フラグは、Braze ダッシュボードおよび[メッセージング API]({{site.baseurl}}/api/endpoints/messaging/) の [Apple プッシュオブジェクト]({{site.baseurl}}/api/objects_filters/messaging/apple_object/)内で設定できます。

{% alert warning %}
タイトルと本文の両方を `content-available=1` でアタッチすることは、未定義の動作につながる可能性があるため、推奨されません。通知が本当にサイレントであることを確認するには、`content-available` フラグを `1.` に設定するときに、タイトルと本文の両方を除外します。詳細については、[バックグラウンド更新に関するAppleの公式ドキュメント](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/pushing_background_updates_to_your_app)を参照してください。
{% endalert %}

![プッシュコンポーザーの [設定] タブにある [コンテンツ利用可能] チェックボックスを表示する Braze ダッシュボード。]({% image_buster /assets/img_archive/remote_notification.png %} "content available")

サイレント プッシュ通知を送信する場合、アプリケーションがイベントを参照できるように、通知ペイロードにデータを含めることもできます。これにより、ネットワークリクエストがいくらか節約され、アプリの応答性が向上する可能性があります。

## 内部 プッシュ通知を無視する

Braze はサイレントプッシュ通知s を使用して、アンインストール追跡 やジオフェンス s などの特定の高度な機能を内部します。アプリがアプリライケーションの起動時またはバックグラウンドのプッシュ時に自動的にアクションを実行する場合は、アクティビティがトリガーでないように内部 プッシュ通知s でゲートすることを検討してください。

たとえば、すべてのバックグラウンドプッシュまたはアプリライケーションの起動時に新しいコンテンツをサーバーに呼び出すロジックがある場合、不必要なネットワークトラフィックを避けるために、Brazeの内部プッシュをトリガーしないようにすることができます。Braze は、特定の内部プッシュをすべてのユーザーに同時にアプリで送信するため、内部プッシュからのオンローンチネットワークコールがゲートされない場合、重大なサーバー読み込むが発生する可能性があります。

### ステップ 1: アプリに自動的にアクションがないか確認します

次の場所でアプリケーションの自動アクションを確認し、Braze の内部プッシュを無視するようにコードを更新します。

1. **プッシュレシーバー。**バックグラウンドプッシュ通知により、`UIApplicationDelegate` の `application:didReceiveRemoteNotification:fetchCompletionHandler:` が呼び出されます。
2. **アプリケーションデリゲート。**バックグラウンドプッシュにより、[中断された](https://developer.apple.com/documentation/uikit/app_and_environment/managing_your_app_s_life_cycle)アプリがバックグラウンドで起動し、`UIApplicationDelegate` の `application:willFinishLaunchingWithOptions:` および `application:didFinishLaunchingWithOptions:` メソッドがトリガーされます。これらのメソッドの `launchOptions` をチェックして、アプリケーションがバックグラウンドプッシュから起動されたかどうかを判断できます。

### ステップ 2: 内部プッシュユーティリティメソッドを使用する

`Braze.Notifications` の静的ユーティリティメソッドを使用して、アプリが Braze の内部プッシュを受信したかを確認できます。[`Braze.Notifications.isInternalNotification(_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/notifications-swift.class/isinternalnotification(_:)) はすべての Braze 内部プッシュ通知で `true` を返します。これには、アンインストール追跡、フィーチャーフラグ同期、ジオフェンス同期通知が含まれます。

以下に例を示します。

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
