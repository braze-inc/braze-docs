---
nav_title: サイレントプッシュ通知
article_title: iOS 向けのサイレントプッシュ通知
platform: Swift
page_order: 4
description: "この記事では、SWIFT SDK 用のサイレント iOS プッシュ通知の実装方法について説明します。"
channel:
  - push

---

# iOS用のサイレントプッシュ通知

> プッシュ通知を使用すると、重要なイベントが発生したときにアプリから通知を送ることができます。 

ユーザーにとって重要なアラートがあるときにプッシュ通知を送るかもしれない。プッシュ通知は、アラートメッセージやサウンドを含まず、アプリのインターフェイスを更新したり、バックグラウンド作業をトリガーしたりするためにのみ使用されるサイレント通知にすることもできます。サイレントプッシュ通知を使用すると、ユーザーに通知することなく、アプリを「一時停止」または「非実行」状態からスリープ解除し、コンテンツを更新したり、特定のタスクを実行したりできます。

Brazeには、サイレント・プッシュ通知に依存する機能がいくつかある：

|特徴|ユーザー・エクスペリエンス|
|---|---|
|[アンインストール追跡]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/uninstall_tracking/) | ユーザーは毎晩、無言のアンインストール追跡プッシュを受け取る。|
|[ジオフェンス]({{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences) | サーバーからデバイスへのジオフェンスのサイレント同期。|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## サイレント・プッシュ通知を設定する

サイレント・プッシュ通知を使用してバックグラウンド作業をトリガーするには、アプリがバックグラウンドでも通知を受け取れるように設定する必要がある。これを行うには、Xcode で、[**署名 & 機能**] ペインを使ってメインアプリのターゲットにバックグラウンドモード機能を追加します。**リモート通知**チェックボックスを選択する。

![Xcode の [機能] の下に [リモート通知] モードのチェックボックスが表示されています。]({% image_buster /assets/img_archive/background_mode.png %}「バックグラウンドモードが有効になりました」)

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

![プッシュコンポーザーの [設定] タブにある [利用可能なコンテンツ] チェックボックスを表示する Braze ダッシュボード。]({% image_buster /assets/img_archive/remote_notification.png %}「利用可能なコンテンツ」)

サイレント プッシュ通知を送信する場合、アプリケーションがイベントを参照できるように、通知ペイロードにデータを含めることもできます。これにより、ネットワークリクエストがいくらか節約され、アプリの応答性が向上する可能性があります。

## iOS のサイレント通知の制限事項

iOS オペレーティングシステムは、一部の機能の通知をゲートする場合があります。これらの機能で問題が発生している場合は、iOS のサイレント通知ゲートが原因である可能性があることに注意してください。

詳細については、Apple の[instance method](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623013-application) および[未受信通知](https://developer.apple.com/library/content/technotes/tn2265/_index.html#//apple_ref/doc/uid/DTS40010376-CH1-TNTAG23) のドキュメントを参照してください。

