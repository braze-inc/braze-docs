---
nav_title: 高度な設定
article_title: 高度なプッシュ設定
platform: iOS
page_order: 5
description: "この参考記事では、アラートオプション、サウンド、有効期限など、iOS の高度なプッシュ通知設定について説明します。"
channel:
  - push

noindex: true
---

{% multi_lang_include archive/objective-c-deprecation-notice.md %}

# 高度な設定

プッシュキャンペーンを作成する際、作成ステップで [**設定**] を選択し、利用可能な高度な設定を表示します。

![][1]

## プッシュキーと値のペアからデータを抽出する

Braze を使用すると、`extras` として知られるカスタム定義の文字列キーと値のペアを、アプリケーションへプッシュ通知と一緒に送ることができます。エクストラは、ダッシュボードまたは API を介して定義することができ、プッシュデリゲートの実装に渡される `notification` 辞書内のキーと値のペアとして利用できます。

## アラートオプション

[**アラート・オプション**] チェックボックスをオンにすると、デバイスにどのように通知が表示されるかを調整するためのキーと値のドロップダウンが表示されます。

## コンテンツ利用可能フラグを追加する

新しいコンテンツをバックグラウンドでダウンロードするようにデバイスに指示するには、[**コンテンツ利用可能フラグを追加**] チェックボックスをオンにします。通常は、[サイレント通知][2] を送信したい場合にオンにします。

## mutable-content フラグを追加する

[**Add Mutable-Content Flag**] チェックボックスをオンにして、iOS 10 以上のデバイスで受信者の高度なカスタマイズを有効にします。このフラグは、このチェックボックスの値に関係なく、[リッチプッシュ通知] の作成時に自動的に送信されます。

## アプリのバッジ数を更新する

バッジ数を更新したい数値を入力するか、Liquid 構文を使用してカスタム条件を設定します。また、アプリケーションの `applicationIconBadgeNumber` プロパティやプッシュ通知のペイロードを使って、バッジ数を手動で更新することもできます。詳しくは、[バッジ数]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/customization/badges/)についての専用の記事を参照してください。

## サウンド

ここでは、アプリバンドル内のサウンドファイルへのパスを入力し、プッシュメッセージ受信時に再生するサウンドを指定することができます。指定されたサウンドファイルが存在しない場合、またはキーワード「default」が入力された場合、Braze はデフォルトのデバイスアラートサウンドを使用します。カスタマイズの詳細については、[カスタムサウンド]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/customization/custom_sounds/)についての専用の記事を参照してください。

## 折りたたみ ID

同様の通知をまとめるには、折りたたみ ID を指定します。同一の折りたたみ ID を使用して複数の通知を送信すると、デバイスには最後に受信した通知のみが表示されます。[coalesced notifications][4] に関する Apple のドキュメントを参照してください。

## 有効期限

[**有効期限**] チェックボックスをオンにすると、メッセージの有効期限を設定できます。ユーザーのデバイスが接続性を失った場合、Braze は指定された時間までメッセージの送信を試行し続けます。設定されていない場合、プラットフォームの有効期限はデフォルトで30日となります。配信前に有効期限切れとなったプッシュ通知は失敗とはみなされず、バウンスとして記録されないことに注意してください。

[1]: {% image_buster /assets/img_archive/ios_advanced_settings.png %}
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/silent_push_notifications/
[3]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/customization/rich_notifications/
[4]: https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1
