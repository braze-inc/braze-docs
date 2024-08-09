---
nav_title: LINE の設定
article_title: LINE の設定
description: "この記事では、Braze の LINE チャネルを設定する方法について、前提条件や推奨される次のステップを含めて説明します。"
page_type: partner
search_tag: Partner
page_order: 0
channel:
 - LINE
hidden: true
permalink: /line/line_setup/
---


# LINE の設定

> この記事では、Braze で LINE チャネルを設定する方法について説明します。また、この記事は LINE ベータ版コレクションの一部です。[メインページに戻ります](https://www.braze.com/docs/line/)。

{% alert important %}
LINE アクセスはベータ版であり、一部の Braze パッケージでのみ利用できます。利用を始めるには、アカウントマネージャーまたはカスタマーサクセスマネージャーにお問い合わせください。
{% endalert %}

## 前提条件

LINE と Braze を統合するには、以下が必要です。

- [LINE ビジネスアカウント](https://www.linebiz.com/jp-en/manual/OfficialAccountManager/tutorial-steps/?list=7171)
- [プレミアムアカウントまたは認証済みアカウント](https://www.infobip.com/docs/line/get-started#premium-id-line-official-account)のステータス (既存のフォロワーを同期するために必要)
   - [LINE のアカウントガイドライン](https://terms2.line.me/official_account_guideline_oth)を見る
- [LINE 開発者アカウント](https://developers.line.biz/en/docs/line-developers-console/login-account/)
- [LINE メッセージング API チャネル](https://developers.line.biz/en/docs/line-developers-console/overview/#channel)

## 統合

### ステップ 1:LINE チャネルを Braze に接続する

1. LINE の \[**メッセージング API**] タブで、\[**Webhook の設定**] を編集します。
   - \[**Webhook URL**] を \[`https://anna.braze.com/line/events`] に設定します。
       - これは、Braze により、ダッシュボードのクラスターに基づいて、統合時に別の URL に自動的に変更されます。
   - \[**Webhook を使用**] と \[**Webhook の再配信**] をオンにします。<br><br> ![Webhook 設定ページでは、Webhook URL の確認や編集、\[webhook を使用]、\[Webhook の再配信]、\[エラー統計の集約]のオンとオフを切り替えることができます。][1]{: style="max-width:70%;"}
2. \[**プロバイダー**] タブに表示される以下の情報をメモしておきます。

| 情報タイプ | ロケーション |
| --- | --- |
| プロバイダー ID | プロバイダーを選択し、\[**設定**] > \[**基本情報**] の順に進みます。 |
| チャネル ID | プロバイダーを選択し、\[**チャネル**] > \[チャネル] > \[**基本設定**] の順に進みます。 |
| チャネルシークレット | プロバイダーを選択し、\[**チャネル**] > \[チャネル] > \[**基本設定**] の順に進みます。 |
| チャネルアクセストークン | プロバイダーを選択し、\[**チャネル**] > \[チャネル] > \[**メッセージング API**] の順に進みます。チャネルアクセストークンがない場合は、\[**発行**] を選択してください。 |
{: .reset-td-br-1 .reset-td-br-2}

{: start="3"}
3\.\[**設定**] ページ > \[**応答設定**]の順に進み、以下を実行します。
   - \[**グリーティングメッセージ**]をオフにする。これは、Braze では、トリガーオンフォロー (trigger on follow) で処理できます。
   - \[**自動応答メッセージ**] をオフにする。トリガーメッセージはすべて Braze 経由で送信されます。これにより、LINE コンソールから直接送信できなくなることはありません。
   - \[**Webhook**] をオンにする。

![アカウントがチャットを処理する方法を切り替えられる、応答設定ページ。][2]{: style="max-width:80%;"}

### ステップ 2:Braze で LINE ページを設定する

1. LINE の Braze テクノロジーパートナーページにアクセスし、LINE の \[**プロバイダー**] タブからメモした情報を入力します。
   - プロバイダー ID
   - チャネル ID
   - チャネルシークレット
   - チャネルアクセストークン

![LINE 統合セクションが掲載された、LINE メッセージング統合ページ。][3]{: style="max-width:80%;"}

{: start="2"}
2\.接続後、Brazeによって、ワークスペースに正常に追加された LINE 統合ごとに Braze サブスクリプショングループが自動的に生成されます。<br><br> フォロワーリストの変更 (新しいフォロワーやフォロー解除など) は、自動的に Braze にプッシュされます。

![「LINE」チャネルに 1 つのサブスクリプショングループを表示する LINE サブスクリプショングループセクション。][4]{: style="max-width:80%;"}

## LINE アカウントのタイプ

| アカウントタイプ | 説明 |
| --- | --- |
| 未認証アカウント | 未審査のアカウントで、誰でも (個人でも法人でも) 取得できます。このアカウントはグレーのバッジで表示され、LINE アプリ内の検索結果には表示されません。 |
| 認証済みアカウント | LINE Yahoo の審査に合格したアカウント。このアカウントは青いバッジで表示され、LINE アプリ内の検索結果に表示されます。<br><br>このアカウントは、日本、台湾、タイ、インドネシアに拠点を置くアカウントでのみ利用できます。  |
| プレミアムアカウント | LINE Yahoo の審査に合格したアカウント。このアカウントは緑色のバッジで表示され、LINE アプリ内の検索結果に表示されます。このアカウントタイプは、LINE の判断で審査時に自動的に付与されます。 |
{: .reset-td-br-1 .resest-td-br-2}

## 既存のフォロワーを Braze に同期する

フォロワーを Braze に同期するには、LINE アカウントが認証済みかプレミアムである必要があります。アカウントを作成すると、デフォルトのステータスは「未認証」になります。アカウント認証を申請する必要があります。

### 認証済みLINEアカウントを申請する

{% alert important %}
認証済みアカウントは、日本、台湾、タイ、インドネシアを拠点とするアカウントでのみ利用できます。
{% endalert %}

1. LINE の \[**公式アカウント**] ページで \[**設定**] を選択します。
2. \[**情報の公開**] の \[認証ステータス]で、\[**アカウント認証をリクエスト**] を選択します。
3. 必要な情報を入力します。
4. 審査結果の通知を待ちます。

チャネルが Braze と同期される前に特定のチャネルをフォローしていたユーザーを同期する場合は、カスタマーサクセスマネージャーまたはアカウントマネージャーに、WhatsApp チームに[リクエストを提出](https://servicedesk.braze.com/plugins/servlet/desk/portal/12)するよう依頼してください。

## Braze で LINE テストユーザーを作成する

ユーザーの照合を設定する前に、次の 2 種類の方法で LINE チャネルをテストできます。

### LINE セグメントを参照する

1. アカウント接続後、LINE チャネルをフォローします。

2. Braze の \[**セグメント**] から、LINE のサブスクリプショングループのセグメントを作成します。<br><br>![サブスクリプショングループを持つフィルターグループ。][5]{: style="max-width:80%;"}<br><br>

3. \[**ユーザーデータ**] > \[**ユーザーデータを CSV 形式でエクスポート**] の順に選択します。<br><br>![「LINE の配信登録済み」という名前のセグメントの \[セグメントの詳細] と、エクスポートオプションのリストが表示される \[ユーザーデータ] メニュー。][6]{: style="max-width:80%;"}<br><br>

4. CSV ダウンロードで、`created_at` フィールドと LINE チャネルをフォローした日時を参照し、ユーザーを検索します。

5. Braze で、Appboy ID を使用して特定のユーザーを検索し、必要に応じて修正します。

### 「IDがわかる」キャンバスまたはキャンペーンを作成する

1. 特定のトリガーワードでユーザーの Braze ユーザー ID を返すキャンバスを設定します。<br><br>トリガーの例 <br><br>![特定のサブスクリプショングループにインバウンド LINE を送信したユーザーにキャンペーンを送信するトリガー。][7]{: style="max-width:80%;"}<br><br>メッセージの例<br><br>![Braze ユーザー ID を記載した LINE メッセージ。][8]{: style="max-width:40%;"}<br><br>

2. Braze で、Braze ID を使用して特定のユーザーを検索し、必要に応じて変更します。

{% alert important %}
キャンバスに、送信を妨げるグローバルコントロールやコントロールグループがないことを確認します。
{% endalert %}


[1]: {% image_buster /assets/img/line/webhook_settings.png %}
[2]: {% image_buster /assets/img/line/response_settings.png %}
[3]: {% image_buster /assets/img/line/integration.png %}
[4]: {% image_buster /assets/img/line/line_subscription_groups.png %}
[5]: {% image_buster /assets/img/line/filter_group.png %}
[6]: {% image_buster /assets/img/line/csv_export_user_data.png %}
[7]: {% image_buster /assets/img/line/trigger.png %}
[8]: {% image_buster /assets/img/line/message.png %}