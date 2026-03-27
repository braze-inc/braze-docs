---
page_order: 1.3
nav_title: デバッグ
article_title: Braze SDKのデバッグ 
description: "Braze SDK デバッガーの使用方法について説明します。これにより、アプリの詳細ログを手動で有効にせずに、SDK 対応チャネルの問題をトラブルシューティングできます。"
---

# Braze SDKのデバッグ

> Braze SDK の組み込みデバッガーを使用する方法を説明します。これにより、アプリで詳細ログを有効にする必要なく、SDK 対応チャネルの問題をトラブルシューティングできます。

{% alert tip %}
より詳細な調査のために、[詳細ログを有効にして]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging)詳細な SDK 出力をキャプチャしたり、特定のチャネルに関する[詳細ログの読み方を学習]({{site.baseurl}}/developer_guide/sdk_integration/reading_verbose_logs)したりすることもできます。
{% endalert %}

## 前提条件

Braze SDK デバッガーを使用するには、「個人識別情報（PII）の閲覧」および「ユーザープロファイルの閲覧（PII 編集済み）」の詳細権限（または「ユーザープロファイルの PII 準拠閲覧」のレガシー権限）が必要です。デバッグセッションのログをダウンロードするには、「ユーザーデータのエクスポート」権限も必要です。さらに、Braze SDK は以下の最小バージョンを満たしているか、参照している必要があります。 

{% sdk_min_versions swift:10.2.0 android:32.1.0 %}

## Braze SDKのデバッグ

{% alert tip %}
Braze Web SDK のデバッグを有効にするには、[URL パラメーターを使用]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/#logging)します。
{% endalert %}

### ステップ 1: アプリを閉じる

デバッグセッションを開始する前に、現在問題が発生しているアプリを閉じます。セッションの開始時にアプリを再起動できます。

### ステップ 2: デバッグセッションを作成する

Braze で、**Settings** に移動し、**Setup and Testing** で **SDK Debugger** を選択します。

![「SDK Debugger」がハイライトされた「Setup and Testing」セクション。]({% image_buster /assets/img/sdk_debugger/select_sdk_debugger.png %})

**Create debugging session** を選択します。

![「SDK Debugger」ページ。]({% image_buster /assets/img/sdk_debugger/select_create_debugging_session.png %})

### ステップ 3: ユーザーを選択する

メールアドレス、`external_id`、ユーザーエイリアス、またはプッシュトークンを使用してユーザーを検索します。セッションを開始する準備ができたら、**Select User** を選択します。

![選択したユーザーのデバッグページ。]({% image_buster /assets/img/sdk_debugger/search_and_select_user.png %}){: style="max-width:85%;"}

### ステップ 4: アプリを再起動する

まずアプリを起動し、デバイスがペアリングされていることを確認します。ペアリングが成功した場合は、アプリを再起動します&#8212;これにより、アプリの初期化ログが完全にキャプチャされます。

### ステップ 5: 再現ステップを完了する

アプリを再起動した後、手順に従ってエラーを再現します。

{% alert tip %}
エラーを再現する際は、[高品質なログ](#step-6-export-your-session-logs-optional)を作成できるように、再現手順をできるだけ正確に実行してください。
{% endalert %}

### ステップ 6: セッションを終了する

再現手順が完了したら、**End Session** > **Close** を選択します。

![「End Session」ボタンが表示されているデバッグセッション。]({% image_buster /assets/img/sdk_debugger/close_debugging_session.png %}){: style="max-width:85%;"}

{% alert note %}
セッションの長さとネットワーク接続状況に応じて、ログの生成に数分かかる場合があります。
{% endalert %}

### ステップ 7: セッションを共有またはエクスポートする（オプション）

セッション終了後、セッションログを CSVファイル としてエクスポートできます。また、他のユーザーは **Session ID** を使用してデバッグセッションを検索できるため、ログを直接送信する必要はありません。

![セッション終了後に「Export Logs」と「Copy Session ID」が表示されたデバッグページ。]({% image_buster /assets/img/sdk_debugger/copy_id_and_export_logs.png %})