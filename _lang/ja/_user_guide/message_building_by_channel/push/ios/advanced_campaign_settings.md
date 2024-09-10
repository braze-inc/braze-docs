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

ここでチェックボックスを選択すると、通知が機器の耳をどのようにアプリするかを調整するために使用できるキー値のドロップダウンメニューが表示されます。

## コンテンツ利用可能フラグを追加する

`content-available` フラグは、バックグラウンド内の新しい内容を読み込むするように指示します。最も一般的には、これは\[無音通知s][2]] を送ることに興味があるかどうかでチェックできます。

## mutable-content フラグを追加する

`mutable-content` フラグは、iOS 10+ デバイスで高度なレシーバカスタマイズを有効にします。このフラグは、\[リッチプッシュ通知][3] を作成するときに、このチェックボックスの値に関係なく自動的に送信されます。

## サウンド

ここでは、アプリバンドルのサウンドファイルへのパスを入力して、プッシュメッセージを受信したときに再生されるサウンドを指定できます。指定されたサウンドファイルが存在しない場合、またはキーワード「default」が入力された場合、Braze はデフォルトのデバイスアラートサウンドを使用します。

## 折りたたみ ID
類似の通知s を結合するための折りたたみID を指定します。同じCollapse IDで複数の通知を送信すると、最後に受信した通知のみが表示されます。詳細については、アップルの\[ドキュメント][4]] を参照してください。

## 有効期限

**Expiry**を選択すると、メッセージの有効期限を設定できます。ユーザーのデバイスが接続を失った場合、Brazeは指定された時刻までメッセージを送信しようとします。設定されていない場合、プラットフォームの有効期限はデフォルトで30日となります。納品前に期限切れになったプッシュ通知は、失敗とは見なされず、バウンスとして記録されません。

[1]: {% image_buster /assets/img_archive/ios_advanced_settings.gif %}
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/
[3]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#ios-10-rich-notifications
[4]: https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1
