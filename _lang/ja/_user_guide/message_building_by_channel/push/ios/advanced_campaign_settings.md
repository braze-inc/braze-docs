---
nav_title: "プッシュキャンペーンの詳細設定"
article_title: プッシュキャンペーンの詳細設定
page_type: reference
page_order: 6
description: "このリファレンス記事では、アラートオプション、フラグ、サウンド、有効期限など、いくつかの高度なプッシュキャンペーン 設定について説明します。"
platform: iOS
channel:
  - push
tool:
  - Campaigns

---

# 高度なプッシュキャンペーン 設定

> このリファレンス記事では、アラートオプション、フラグ、サウンド、有効期限など、いくつかの高度なプッシュキャンペーン 設定について説明します。

プッシュエンゲージメントを作成する場合、**Compose** ステップで、<i class="fas fa-cog"></i> cog アイコンを選択して、メッセージの詳細設定s を表示できます。

![][1]

## アラートオプション

このチェックボックスをオンにすると、デバイスでの通知の表示を調整するために使用できるキー値のドロップダウンメニューが表示されます。

## コンテンツ利用可能フラグを追加する

`content-available` フラグは、デバイスにバックグラウンドで新しいコンテンツをダウンロードするように指示します。通常は、[サイレント通知][2]を送信する場合にオンにします。

## mutable-content フラグを追加する

`mutable-content` フラグを使用すると、iOS 10 以降のデバイスで受信機の高度なカスタマイズができます。このフラグは、このチェックボックスの値に関係なく、[リッチプッシュ通知][3]の作成時に自動的に送信されます。

## サウンド

ここでは、アプリバンドルのサウンドファイルへのパスを入力して、プッシュメッセージを受信したときに再生されるサウンドを指定できます。指定されたサウンドファイルが存在しない場合、またはキーワード「default」が入力された場合、Braze はデフォルトのデバイスアラートサウンドを使用します。

## 折りたたみ ID
同様の通知をまとめるには、折りたたみ ID を指定します。同一の折りたたみ ID を使用して複数の通知を送信すると、デバイスには最後に受信した通知のみが表示されます。詳細については、Apple の[ドキュメント][4]を参照してください。

## 有効期限

**Expiry**を選択すると、メッセージの有効期限を設定できます。ユーザーのデバイスが接続を失った場合、Brazeは指定された時刻までメッセージを送信しようとします。設定されていない場合、プラットフォームの有効期限はデフォルトで30日となります。納品前に期限切れになったプッシュ通知は、失敗とは見なされず、バウンスとして記録されません。

[1]: {% image_buster /assets/img_archive/ios_advanced_settings.gif %}
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/
[3]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#ios-10-rich-notifications
[4]: https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1
