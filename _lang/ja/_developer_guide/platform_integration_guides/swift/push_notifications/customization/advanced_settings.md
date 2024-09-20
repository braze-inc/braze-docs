---
nav_title: プッシュ設定
article_title: iOSのプッシュ設定
platform: Swift
page_order: 7
description: "この参考記事では、Swift SDKのアラートオプション、サウンド、有効期限など、iOSの高度なプッシュ通知設定を取り上げている。"
channel:
  - push

---

# プッシュ設定

> ダッシュボードからプッシュキャンペーンを作成する場合、**作成**ステップで**設定**タブをクリックし、利用可能な詳細設定を表示する。

![][1]

## キーと値のペア

Braze を使用すると、`extras` として知られるカスタム定義の文字列キーと値のペアを、アプリケーションへプッシュ通知と一緒に送ることができます。エクストラは、ダッシュボードまたは API を介して定義することができ、プッシュデリゲートの実装に渡される `notification` 辞書内のキーと値のペアとして利用できます。

## アラートオプション

**Alert Options（アラート・オプション）**チェックボックスを選択すると、デバイスにどのように通知が表示されるかを調整するために利用可能なキー値のドロップダウンが表示される。

## コンテンツ利用可能フラグを追加する

新しいコンテンツをバックグラウンドでダウンロードするようにデバイスに指示するには、\[**コンテンツ利用可能フラグを追加**] チェックボックスをオンにします。最も一般的なのは、\[サイレント通知]][2] の送信に関心がある場合にチェックすることである。

## mutable-content フラグを追加する

**Add Mutable-Content Flag**チェックボックスをチェックして、受信機の高度なカスタマイズを有効にする。このフラグは、このチェックボックスの値に関係なく、\[リッチ通知][3]]を作成するときに自動的に送信される。

## アプリのバッジ数を更新する

バッジ数を更新したい数値を入力するか、リキッド構文を使用してカスタム条件を設定する。メッセージバッジの数をプログラムで更新することもできる。

## サウンド

プッシュ通知受信時にカスタムサウンドを鳴らしたい場合は、**サウンド**フィールドでサウンドファイルのプロトコルURLを指定する。カスタマイズの詳細については、[カスタムサウンドの]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/custom_sounds/)記事を参照のこと。

## 折りたたみ ID

同様の通知をまとめるには、折りたたみ ID を指定します。同一の折りたたみ ID を使用して複数の通知を送信すると、デバイスには最後に受信した通知のみが表示されます。coalesced notifications\[][4]]に関するアップルのドキュメントを参照のこと。

## 有効期限

\[**有効期限**] チェックボックスをオンにすると、メッセージの有効期限を設定できます。ユーザーのデバイスが接続性を失った場合、Braze は指定された時間までメッセージの送信を試行し続けます。設定されていない場合、プラットフォームの有効期限はデフォルトで30日となります。配信前に有効期限切れとなったプッシュ通知は失敗とはみなされず、バウンスとして記録されないことに注意してください。

[1]: {% image_buster /assets/img_archive/ios_advanced_settings.png %}
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/
[3]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/rich_notifications/
[4]: https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1
