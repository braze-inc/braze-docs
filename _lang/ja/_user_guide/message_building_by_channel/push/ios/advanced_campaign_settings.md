---
nav_title: "プッシュキャンペーンの詳細設定"
article_title: プッシュキャンペーンの詳細設定
page_type: reference
page_order: 6
description: "この参考記事では、アラートオプション、フラグ、サウンド、有効期限など、いくつかの高度なプッシュキャンペーン設定について説明しています。"
platform: iOS
channel:
  - push
tool:
  - Campaigns

---

# プッシュキャンペーンの詳細設定

> この参考記事では、アラートオプション、フラグ、サウンド、有効期限など、いくつかの高度なプッシュキャンペーン設定について説明します。

プッシュエンゲージメントを作成する場合、**<i class="fas fa-cog"></i>作成ステップで歯車アイコンを選択してメッセージの詳細設定を表示できます**。

![][1]

## アラートオプション

ここでチェックボックスを選択すると、デバイスでの通知の表示方法を調整できるキー値のドロップダウンメニューが表示されます。

## コンテンツ利用可能フラグの追加

`content-available`このフラグは、新しいコンテンツをバックグラウンドでダウンロードするようにデバイスに指示します。ほとんどの場合、[サイレント通知] [2] の送信に興味がある場合にチェックを入れることができます。

## 可変コンテンツフラグの追加

`mutable-content`このフラグにより、iOS 10 以降のデバイスで受信機を高度にカスタマイズできます。このフラグは、このチェックボックスの値に関係なく、リッチプッシュ通知の作成時に自動的に送信されます。

## サウンド

ここでは、アプリバンドルのサウンドファイルへのパスを入力して、プッシュメッセージを受信したときに再生するサウンドを指定できます。指定したサウンドファイルが存在しない場合、または「default」というキーワードを入力した場合、Braze はデフォルトのデバイスアラートサウンドを使用します。

## 折りたたみ ID
同様の通知をまとめるには、折りたたみ ID を指定します。同じ折りたたみ ID を指定して複数の通知を送信すると、デバイスには最後に受信した通知のみが表示されます。詳細については、Apple の [ドキュメンテーション] [4] を参照してください。

## 有効期限

[**有効期限**] を選択すると、メッセージの有効期限を設定するオプションが表示されます。ユーザーのデバイスが接続できなくなった場合、Braze は指定された時間までメッセージの送信を試み続けます。これが設定されていない場合、プラットフォームはデフォルトで30日間の有効期限になります。配信前に期限切れになったプッシュ通知は失敗とは見なされず、バウンスとして記録されないことに注意してください。

[1]: {% image_buster /assets/img_archive/ios_advanced_settings.gif %}
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/
[3]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#ios-10-rich-notifications
[4]: https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1
