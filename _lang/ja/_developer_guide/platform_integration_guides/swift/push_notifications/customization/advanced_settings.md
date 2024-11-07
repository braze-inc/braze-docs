---
nav_title: プッシュ設定
article_title: iOSのプッシュ設定
platform: Swift
page_order: 7
description: "この参考記事では、Swift SDK のアラートオプション、サウンド、有効期限など、iOS の高度なプッシュ通知設定について説明します。"
channel:
  - push

---

# プッシュ設定

> ダッシュボードからプッシュキャンペーンを作成する場合、**作成**ステップで**設定**タブをクリックし、利用可能な詳細設定を表示する。

![]({% image_buster /assets/img_archive/ios_advanced_settings.png %})

## キーと値のペア

Braze を使用すると、`extras` として知られるカスタム定義の文字列キーと値のペアを、アプリケーションへプッシュ通知と一緒に送ることができます。エクストラは、ダッシュボードまたは API を介して定義することができ、プッシュデリゲートの実装に渡される `notification` 辞書内のキーと値のペアとして利用できます。

## アラートオプション

**Alert Options（アラート・オプション）**チェックボックスを選択すると、デバイスにどのように通知が表示されるかを調整するために利用可能なキー値のドロップダウンが表示される。

## コンテンツ利用可能フラグを追加する

新しいコンテンツをバックグラウンドでダウンロードするようにデバイスに指示するには、[**コンテンツ利用可能フラグを追加**] チェックボックスをオンにします。最も一般的には、これは[サイレント通知]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/)の送信に関心がある場合にチェックできます。

## mutable-content フラグを追加する

**Add Mutable-Content Flag**チェックボックスをチェックして、受信機の高度なカスタマイズを有効にする。このフラグは、このチェックボックスの値に関係なく、[rich notification]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/rich_notifications/)を作成するときに自動的に送信されます。

## アプリのバッジ数を更新する

バッジ数を更新する数値を入力するか、Liquid 構文を使用してカスタム条件を設定します。また、プログラムでメッセージバッジ数を更新することもできます。専用の[バッジ数]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/badges/)に関する記事を参照してください。

## サウンド

プッシュ通知受信時にカスタムサウンドを鳴らしたい場合は、**サウンド**フィールドでサウンドファイルのプロトコルURLを指定する。カスタマイズの詳細については、[カスタムサウンド]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/custom_sounds/)の記事を参照してください。

## 折りたたみ ID

同様の通知をまとめるには、折りたたみ ID を指定します。同一の折りたたみ ID を使用して複数の通知を送信すると、デバイスには最後に受信した通知のみが表示されます。[統合された通知](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1)については、Apple のドキュメントを参照してください。

## 有効期限

[**有効期限**] チェックボックスをオンにすると、メッセージの有効期限を設定できます。ユーザーのデバイスが接続性を失った場合、Braze は指定された時間までメッセージの送信を試行し続けます。設定されていない場合、プラットフォームの有効期限はデフォルトで30日となります。配信前に有効期限切れとなったプッシュ通知は失敗とはみなされず、バウンスとして記録されないことに注意してください。

