---
nav_title: アンインストール追跡
article_title: iOS のアンインストール追跡
platform: Swift
page_order: 7
description: "この記事では、Swift SDK のアンインストール追跡を構成する方法について説明します。"

---

# アンインストール追跡

> この記事では、iOS アプリケーションのアンインストール追跡を構成する方法と、Braze アンインストール追跡プッシュの受信時にアプリで不要な自動アクションが実行されないことを確認するためのテスト方法について説明します。

アンインストール追跡では、ペイロードに Braze フラグを含むバックグラウンドプッシュ通知を利用します。一般情報については、ユーザーガイドの「[アンインストール追跡][6]」を参照してください。

## ステップ1: バックグラウンドプッシュを有効にする

Xcode プロジェクトの [**機能**] タブの **[バックグラウンドモード**] セクションで、[**リモート通知**] オプションが有効になっていることを確認します。詳細については、 [サイレントプッシュ通知][5]のドキュメントを参照してください。

## ステップ2: Braze バックグラウンドプッシュの確認

Braze では、バックグラウンドプッシュ通知を使用してアンインストール追跡分析を収集します。アンインストール追跡通知の受信時に、アプリケーションで[不要なアクションが実行されない][4]ようにしてください。

## ステップ3: ダッシュボードからのテスト

次に、ダッシュボードからテストプッシュを自分に送信します。このテストプッシュでは、ユーザープロファイルが更新されません。

1. [**キャンペーン**] ページで、プッシュ通知キャンペーンを作成し、プラットフォームとして [**iOS プッシュ**] を選択します。<br><br>
2. [**設定**] ページで、キー `appboy_uninstall_tracking` および対応する値 `true` を追加し、[**コンテンツ利用可能フラグを追加**] にチェックします。<br><br>
3. [**プレビュー**] ページを使用して、テストアンインストール追跡プッシュを自分に送信します。<br><br>
4. プッシュの受信時に、アプリで不要な自動アクションが実行されないことを確認してください。

{% alert important %}
これらのテストステップは、Braze からアンインストール追跡プッシュを送信するためのプロキシです。バッジ数を有効にしている場合は、テストプッシュとともにバッジ番号が送信されますが、Braze のアンインストール追跡プッシュによってアプリケーションでバッジ番号が設定されることはありません。
{% endalert %}

## ステップ4: アンインストール追跡を有効にする

[アンインストール追跡を有効にする][6]手順に従ってください。

[4]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/ignoring_internal_push/
[5]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/
[6]: {{site.baseurl}}/user_guide/data_and_analytics/tracking/uninstall_tracking/#uninstall-tracking
[9]: {% image_buster /assets/img_archive/ios-uninstall-tracking-2.png %}
[10]: {% image_buster /assets/img_archive/ios-uninstall-tracking-3.png %}
