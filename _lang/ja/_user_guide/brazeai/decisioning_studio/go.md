---
nav_title: デシジョン・スタジオ・ゴー
article_title: BrazeAIデシジョニングスタジオGo
page_order: 0
description: "BrazeAI Decisioning<sup>StudioTM</sup>Goを設定し、Brazeに統合する方法を学ぶ。"
---

# BrazeAI Decisioning Studio™ Go

> BrazeAI Decisioning Studio™ Goとの統合を開始するために、Brazeで重要な情報を見つける。

## エッセンシャルズ

### BrazeでREST APIキーを作成する

新しいREST APIキーを作成する：

1. ダッシュボードで、**設定**＞**APIと識別子**＞**APIキーに**進む。
2. [**API キーを作成**] を選択します。
3. APIキーの名前を入力する。例えば、"DecisioningStudioGoEmail "である。
4. 以下のカテゴリーに基づいて権限を選択する：
    - **ユーザーデータ：** `users.track`,`users.delete`,`users.export.ids` を選択する、 `users.export.segment`
    - **メッセージング：**選択する `messages.send`
    - **キャンペーン：**リストアップされた権限をすべて選択する。
    - **キャンバス：**リストアップされた権限をすべて選択する。
    - **セグメンテーション：**リストされたすべての権限を選択する。
    - **テンプレート：**リストされた権限をすべて選択する。

{: start="5"}
5. [**API キーを作成**] を選択します。
6. 次に、APIキーをコピーして、BrazeAI Decisioning Studio™ Goポータルに貼り付ける。

### Brazeメールの表示名を確認する

Brazeメールの表示名を検索する：

1. Brazeダッシュボードで、**設定**>**メール設定に**進む。
2. BrazeAI Decisioning Studio™ Goで使用する表示名を探す。
3. **送信元表示名**」をコピーし、「**メール表示名**」としてBrazeAI Decisioning Studio™ Goポータルに貼り付ける。
4. 関連するメールアドレスをコピーして、BrazeAI Decisioning Studio™ Goポータルの**Fromメールアドレスに**貼り付ける。

### ユーザーIDを探す

ユーザーIDを探す：

1. Brazeダッシュボードで、**オーディエンス**>**ユーザーを検索する**。
2. 外部ユーザーID、ユーザーエイリアス、メール、電話番号、プッシュトークンでユーザーを検索する。
3. ユーザーIDをコピーしてセットアップで参照する。

![ユーザーIDとユーザープロファイルの例。]({% image_buster /assets/img/decisioning_studio_go/user_id.png %})

### BrazeのURLを見つける

あなたのBraze URLを識別子する：

1. Brazeのダッシュボードに行く。
2. ブラウザのウィンドウでは、BrazeのURLは`https://` で始まり、`braze.com` で終わる。BrazeのURLの例は`https://dashboard-01.braze.com` 。

### APIキーを探す

{% alert note %}
Brazeは、アプリID（BrazeダッシュボードではAPIキーと呼ばれる）を提供しており、アクティビティをワークスペース内の特定のアプリに関連付けるなど、トラッキング追跡に使用できる。アプリIDを使用する場合、BrazeAI Decisioning Studio™ Goは、各実験者にアプリIDを関連付けることをサポートしている。<br><br>アプリIDを使用しない場合は、プレースホルダーとして任意の文字列を入力できる。
{% endalert %}

1. Brazeダッシュボードで、**設定**>**アプリ設定に**進む。
2. トラッキングしたいアプリにアクセスする。
3. **APIキーを**コピーして、BrazeAI Decisioning Studio™ Goポータルに貼り付ける。

### KlaviyoのAPIキーを設定する

BrazeAI Decisioning Studio™ GoでKlaviyoを使用するには、APIキーを設定する必要がある。

1. Klaviyoで、**設定**>**APIキーに**行く。
2. **Create Private API Keyを**選択する。 
3. APIキーの名前を入力する。例えば、"決定力のあるスタジオ・エクスペリメンター "だ。
4. APIキーに対して以下の権限を選択する：
    - キャンペーン:アクセスを読む
    - データのプライバシーフルアクセス
    - イベントだ：フルアクセス
    - フローだ：フルアクセス
    - 画像、写真：アクセスを読む
    - リストを見てみよう：フルアクセス
    - 指標:フルアクセス
    - プロファイルだ：フルアクセス
    - セグメント:アクセスを読む
    - テンプレートだ：フルアクセス
    - Webhookだ：アクセスを読む

![選択した権限を持つKlaviyo APIキー。]({% image_buster /assets/img/decisioning_studio_go/klaviyo_api_key.png %})

{: start="5"}
5. [**作成**] を選択します。
6. このAPIキーをコピーして、BrazeAI Decisioning Studio™ Goポータルにペーストする。

### SFMCアプリパッケージの設定

BrazeAI Decisioning Studio™ GoでSalesforce Marketing Cloudを使用するには、Salesforce Marketing Cloudでアプリパッケージを設定する必要がある。 

1. マーケティングクラウドのホームページにアクセスする。 
2. グローバルヘッダーでメニューを開封し、**セットアップを**選択する。
3. サイドパネルのナビゲーションの「**Platform Tools**」にある「**Apps**」を開き、「**Installed Packages**」を選択する。
4. アプリ・パッケージを作成するには「**新規**」を選択する。
5. アプリパッケージに名前と説明をつける。

![Experimenter 1 - Test 5」という名前のアプリパッケージ。]({% image_buster /assets/img/decisioning_studio_go/sfmc_app_package1.png %})

{: start="6"}
6. **Add Componentを**選択する。
7. **Component Type（コンポーネント・タイプ**）」で「**API Integration（API統合）**」を選択する。次に**「Next」を**選択する。
8. **Integration Type（統合タイプ**）」で「**Server-to-server（サーバー間）**」を選択する。次に**「Next」を**選択する。
9\.次に、アプリパッケージに対してのみ、以下の推奨スコープを選択する：
    \- チャネル > メール > 読み取り、書き込み、送信
    \- チャンネル > OTT > 読む
    \- チャネル > プッシュ > リード
    \- チャネル > SMS > 読む
    \- チャネル > ソーシャル > 読む
    \- チャンネル > ウェブ > 読む
    \- 資産 > ドキュメントと画像写真 > 読み取り、書き込み
    \- 資産 > 保存されたコンテンツ > 読み取り、書き込み
    \- オートメーション > オートメーション > 読み取り、書き込み、実行
    \- オートメーション > ジャーニー > 読み取り、書き込み、実行、アクティベート/停止/一時停止/送信/スケジュール
    \- コンタクト >オーディエンス > 読む
    \- 連絡先 > リストとサブスクライバー > 読み取り、書き込み
    \- Cross Cloud Platform > マーケットオーディエンス > ビュー
    \- Cross Cloud Platform > マーケットオーディエンス > 見る
    \- Cross Cloud Platform > Marketing Cloud Connect > 読む
    \- データ > データ拡張 > 読み取り、書き込み
    \- データ > ファイルの場所 > 読み込み
    \- データ > イベントトラッキング > 読み取り、書き込み
    \- イベント通知 > コールバック > 読み取り
    \- イベント通知 > サブスクリプション > 読む

{% details Show image of recommended scopes %}

![Salesforce Marketing Cloudアプリパッケージの推奨スコープ。]({% image_buster /assets/img/decisioning_studio_go/app_package_scopes.png %})

{% enddetails %}

{: start="10"}
10\.[**保存**] を選択します。
11\.以下のフィールドをコピーし、BrazeAI Decisioning Studio™ Goポータルに貼り付ける：**クライアント ID**、**クライアント秘密鍵**、**認証ベース URI**、**REST ベース URI**、**SOAP ベース URI**。