---
nav_title: サイレントプッシュ通知
article_title: iOS 向けのサイレントプッシュ通知
platform: Swift
page_order: 4
description: "この記事では、Swift SDK にサイレント iOS プッシュ通知を実装する方法について説明します。"
channel:
  - push

---

# サイレントプッシュ通知

> プッシュ通知を使用すると、重要なイベントが発生したときにアプリから通知を送信できます。 

ユーザーにとって重要なアラートがある場合に、プッシュ通知を送信することがあります。プッシュ通知は、アラートメッセージやサウンドを含まず、アプリのインターフェイスを更新したり、バックグラウンド作業をトリガーしたりするためにのみ使用されるサイレント通知にすることもできます。サイレントプッシュ通知を使用すると、ユーザーに通知することなく、アプリを「一時停止」または「非実行」状態からスリープ解除し、コンテンツを更新したり、特定のタスクを実行したりできます。

Braze には、サイレント プッシュ通知を利用する機能がいくつかあります。

|機能|ユーザーエクスペリエンス|
|---|---|
||[Uninstall Tracking][6] | ユーザーは、夜間にサイレントにアンインストール追跡プッシュを受信します。|
|[Geofences]9] | サーバーからデバイスへのジオフェンスのサイレント同期。|
{: .reset-td-br-1 .reset-td-br-2}

## サイレントプッシュ通知の設定

サイレント プッシュ通知を使用してバックグラウンド作業をトリガーするには、アプリがバックグラウンドにあるときでも通知を受信するように構成する必要があります。これを行うには、Xcode のメイン アプリ ターゲットに **[署名と機能]** ペインを使用してバックグラウンド モード機能を追加します。**リモート通知** チェックボックスを選択します。

![Xcode の [機能] の下に [リモート通知] モードのチェックボックスが表示されています。][3]

リモート通知バックグラウンドモードが有効になっている場合でも、ユーザーがアプリケーションを強制終了した場合、システムはアプリをバックグラウンドで起動しません。システムによってアプリがバックグラウンドで自動的に起動される前に、ユーザーはアプリケーションを明示的に起動するか、デバイスを再起動する必要があります。

詳細については、[バックグラウンド更新のプッシュ][4]および `application:didReceiveRemoteNotification:fetchCompletionHandler:` [ドキュメント][5]

## サイレントプッシュ通知の送信

サイレントプッシュ通知を送信するには、プッシュ通知ペイロードで `content-available` フラグを `1` に設定します。 

{% alert note %}
Appleがリモート通知と呼んでいるものは、通常のプッシュ通知に `content-available` フラグが設定されました。
{% endalert %}

`content-available` フラグは、Braze ダッシュボードおよび[メッセージング API][1] の [Apple プッシュオブジェクト]({{site.baseurl}}/api/objects_filters/messaging/apple_object/)内で設定できます。

{% alert warning %}
タイトルと本文の両方を `content-available=1` でアタッチすることは、未定義の動作につながる可能性があるため、推奨されません。通知が本当にサイレントであることを確認するには、`content-available` フラグを `1.` に設定するときに、タイトルと本文の両方を除外します。詳細については、[バックグラウンド更新に関するAppleの公式ドキュメント](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/pushing_background_updates_to_your_app)を参照してください。
{% endalert %}

![プッシュコンポーザーの [設定] タブにある [コンテンツ利用可能] チェックボックスを表示する Braze ダッシュボード。][2]

サイレント プッシュ通知を送信する場合、アプリケーションがイベントを参照できるように、通知ペイロードにデータを含めることもできます。これにより、ネットワークリクエストがいくらか節約され、アプリの応答性が向上する可能性があります。

## iOS のサイレント通知の制限事項

iOS オペレーティングシステムは、一部の機能の通知をゲートする場合があります。これらの機能で問題が発生している場合は、iOS のサイレント通知ゲートが原因である可能性があることに注意してください。

詳細については、Apple の [インスタンスメソッド][7] および [未受信通知][8] のドキュメントを参照してください。

[1]: {{site.baseurl}}/api/endpoints/messaging/
[2]: {% image_buster /assets/img_archive/remote_notification.png %} 「利用可能なコンテンツ」
[3]: {% image_buster /assets/img_archive/background_mode.png %} 「バックグラウンドモードが有効になりました」
[4]: https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/pushing_background_updates_to_your_app
[5]: https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIApplicationDelegate_Protocol/index.html#//apple_ref/occ/intfm/UIApplicationDelegate/application:didReceiveRemoteNotification:fetchCompletionHandler:
[6]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/uninstall_tracking/
[7]: https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623013-application
[8]: https://developer.apple.com/library/content/technotes/tn2265/_index.html#//apple_ref/doc/uid/DTS40010376-CH1-TNTAG23
[9]: {{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences