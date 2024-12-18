---
nav_title: アンインストール追跡
article_title: iOS のアンインストール追跡
platform: Swift
page_order: 7
description: "この記事では、Swift SDK のアンインストール追跡を構成する方法について説明します。"

---

# アンインストール追跡

> iOSアプリケーションのアンインストール追跡の設定方法を学習し、Brazeのアンインストール追跡プッシュを受信した際にアプリが不要な自動アクションを取らないようにする。アンインストール追跡では、ペイロードに Braze フラグを含むバックグラウンドプッシュ通知を利用します。一般情報については、[アンインストール追跡][6]] を参照してください。

{% alert important %}
アンインストール追跡は不正確な場合があることを覚えておいてほしい。Brazeに表示される指標は、遅れたり不正確であったりする可能性がある。
{% endalert %}

## ステップ1:バックグラウンドのプッシュを有効にする

Xcode プロジェクトで、[**Capabilities**] に移動し、[**Background Modes**] が有効になっていることを確認します。詳しくは、[サイレント・プッシュ]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/)通知を参照のこと。

## ステップ 2:Braze のバックグラウンドプッシュを確認する

Braze では、バックグラウンドプッシュ通知を使用してアンインストール追跡分析を収集します。アンインストール追跡通知の受信時に、アプリケーションで[不要なアクションが実行されない]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/ignoring_internal_push/)ようにしてください。

## ステップ3: Braze ダッシュボードからテストする

次に、Brazeのダッシュボードから自分にテストプッシュを送る。このテストプッシュではユーザープロファイルは更新されないことを覚えておいてほしい。

1. [**キャンペーン**] ページで、プッシュ通知キャンペーンを作成し、プラットフォームとして [**iOS プッシュ**] を選択します。
2. [**設定**] ページで、キー `appboy_uninstall_tracking` および対応する値 `true` を追加し、[**コンテンツ利用可能フラグを追加**] チェックボックスをオンにします。
3. [**プレビュー**] ページを使用して、テストアンインストール追跡プッシュを自分に送信します。
4. プッシュの受信時に、アプリで不要な自動アクションが実行されないことを確認してください。

{% alert important %}
これらのテストステップは、Braze からアンインストール追跡プッシュを送信するためのプロキシです。バッジ数を有効にしている場合は、テストプッシュとともにバッジ番号が送信されますが、Braze のアンインストール追跡プッシュによってアプリケーションでバッジ番号が設定されることはありません。
{% endalert %}

## ステップ 4:アンインストール追跡を有効にする

[アンインストール追跡を有効にする]({{site.baseurl}}/user_guide/data_and_analytics/tracking/uninstall_tracking/#uninstall-tracking)手順に従ってください。

