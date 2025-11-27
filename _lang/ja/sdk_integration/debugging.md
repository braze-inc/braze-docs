---
page_order: 1.3
nav_title: デバッグ
article_title: Braze SDKのデバッグ 
description: "Braze SDK デバッガの使用方法について説明します。これにより、アプリの詳細なログインを手動で有効にせずに、SDK 対応チャネルの問題をトラブルシューティングできます。"
---

# Braze SDKのデバッグ

> Braze SDK の組み込みデバッガを使用する方法を説明します。これにより、アプリで詳細なログを有効にする必要なく、SDK 対応チャネルの問題をトラブルシューティングできます。

## 前提条件

Braze SDKデバッガーを使用するには、"View PII "と "View User Profiles PII Compliant "の権限が必要。デバッグ・セッションのログをダウンロードするには、「ユーザーデータのエクスポート」権限も必要だ。さらに、Braze SDK は、次の最小バージョンを満たしているか、参照している必要があります。 

{% sdk_min_versions swift:10.2.0 android:32.1.0 %}

## Braze SDKのデバッグ

{% alert tip %}
Braze Web SDK のデバッグを有効にするには、[URL パラメータ]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/#logging)を使用します。
{% endalert %}

### ステップ1:アプリを閉じる

デバッグセッションを開始する前に、現在問題が発生しているアプリを閉じます。セッションの開始時にアプリを再起動できます。

### ステップ 2:デバッグセッションの作成

Braze で、**Settings** に移動し、**Setup and Testing** で**SDK Debugger** を選択します。

![「SDK デバッガー」が強調表示された「設定およびテスト」セクション。]({% image_buster /assets/img/sdk_debugger/select_sdk_debugger.png %})()

**デバッグセッションの作成**を選択します。

![「SDK デバッガー」ページ。]({% image_buster /assets/img/sdk_debugger/select_create_debugging_session.png %})()

### ステップ 3: ユーザーを選択

メールアドレス、`external_id`、ユーザーエイリアス、またはプッシュトークンを使用してユーザーを検索します。セッションを開始する準備ができたら、**Select User**を選択します。

![選択したユーザーのデバッグページ。]({% image_buster /assets/img/sdk_debugger/search_and_select_user.png %})({: style="max-width:85%;"})

### ステップ 4: アプリを再起動する

まずアプリを起動し、デバイスがペアリングされていることを確認します。ペアリングが成功した場合は、アプリを再起動します。これにより、アプリの初期化ログが完全にキャプチャされます。

### ステップ5: 再現ステップを完了する

アプリを再起動した後、手順に従ってエラーを再現します。

{% alert tip %}
エラーを再現する場合は、[quality logs](#step-6-export-your-session-logs-optional)を作成できるように、再現手順をできるだけ厳密に実行してください。
{% endalert %}

### ステップ 6: セッションを終了する

再現手順が完了したら、**End Session**> **Close**を選択します。

![「セッションを終了」ボタンが表示されているデバッグセッション。]({% image_buster /assets/img/sdk_debugger/close_debugging_session.png %})({: style="max-width:85%;"})

{% alert note %}
セッションの長さとネットワーク接続に応じて、ログの生成に数分かかる場合があります。
{% endalert %}

### ステップ 7:セッションを共有またはエクスポートする(オプション)

セッション終了後、セッションログを CSV ファイルとしてエクスポートできます。また、他のユーザーは [**セッション ID**] を使用してデバッグセッションを検索できるため、ログを直接送信する必要はありません。

![セッション後に表示される「ログをダウンロード」と「セッション ID をコピー」を含むデバッグページ。]({% image_buster /assets/img/sdk_debugger/copy_id_and_export_logs.png %})()
