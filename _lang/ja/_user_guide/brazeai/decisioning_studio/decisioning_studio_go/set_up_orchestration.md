---
nav_title: オーケストレーションの設定
article_title: オーケストレーションの設定
page_order: 2
description: "BrazeAI Decisioning Studio Goをカスタマーエンゲージメントプラットフォームに接続し、パーソナライズされたコミュニケーションを可能にする方法を学習。"
toc_headers: h2
---

# オーケストレーションの設定

> BrazeAI Decisioning Studio™ Goは、カスタマーエンゲージメントプラットフォーム(CEP)に接続して、パーソナライズされたコミュニケーションをオーケストレーションする必要がある。この記事では、サポートされているCEPごとに統合を設定する方法を説明する。

## サポートされるCEP

Decisioning Studio Goは以下のカスタマーエンゲージメントプラットフォームをサポートしている：

| CEP | 統合タイプ | 主要な機能 |
|-----|-----------------|--------------|
| **Braze** | API トリガーキャンペーン | ネイティブ統合、リアルタイムトリガー |
| **セールスフォース・マーケティングクラウド** | APIイベントを使ったジャーニービルダー | SQLクエリーのオートメーション、データ拡張 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

以下からCEPを選択し、統合設定を開始する。

{% tabs %}
{% tab Braze %}

## Brazeとの統合設定

Decisioning Studio GoとBrazeを統合するには、APIキーを作成し、APIトリガーキャンペーンを設定し、必要な識別子をDecisioning Studio Goポータルに提供する。

### ステップ 1: REST APIキーを作成する

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
6. APIキーをコピーし、BrazeAI Decisioning Studio™ Goポータルに貼り付ける。

### ステップ 2:メールの表示名を探す

1. Brazeダッシュボードで、**設定**>**メール設定に**進む。
2. BrazeAI Decisioning Studio™ Goで使用する表示名を探す。
3. **送信元表示名**」をコピーし、「**メール表示名**」としてBrazeAI Decisioning Studio™ Goポータルに貼り付ける。
4. 関連するメールアドレスをコピーして、BrazeAI Decisioning Studio™ Goポータルの**Fromメールアドレスに**貼り付ける。

### ステップ 3:BrazeのURLとアプリIDを探す

**BrazeのURLを見つける：**
1. Brazeのダッシュボードに行く。
2. ブラウザのウィンドウでは、BrazeのURLは`https://` で始まり、`braze.com` で終わる。BrazeのURLの例は`https://dashboard-01.braze.com` 。

**アプリID（APIキー）を調べる：**

{% alert note %}
Brazeは、アプリID（BrazeダッシュボードではAPIキーと呼ばれる）を提供しており、アクティビティをワークスペース内の特定のアプリに関連付けるなど、トラッキング追跡に使用できる。アプリIDを使用する場合、BrazeAI Decisioning Studio™ Goは、各実験者にアプリIDを関連付けることをサポートしている。<br><br>アプリIDを使用しない場合は、プレースホルダーとして任意の文字列を入力できる。
{% endalert %}

1. Brazeダッシュボードで、**設定**>**アプリ設定に**進む。
2. トラッキングしたいアプリにアクセスする。
3. **APIキーを**コピーして、BrazeAI Decisioning Studio™ Goポータルに貼り付ける。

### ステップ 4: APIトリガーキャンペーンを作成する

1. Brazeのダッシュボードで、「**メッセージング**」>「キャンペーン」と進む。
2. **キャンペーンの作成を**選択する。
3. キャンペーンタイプは**APIキャンペーンを**選択する。
4. キャンペーン名を入力します。例えば、「決定戦スタジオ囲碁メール」である。

![決裁スタジオGoメール」というAPIキャンペーン。]({% image_buster /assets/img/decisioning_studio_go/api_campaign_name.png %})

{: start="5"}
5. メッセージング・チャネルには、**メールを**選択する。

![APIキャンペーンのメッセージングチャネルを選択するオプション。]({% image_buster /assets/img/decisioning_studio_go/select_api_campaign.png %})

{: start="6"}
6. **Additional Optionsで**、**Allow users to become re-eligible to receive campaign**チェックボックスを選択する。
7. 再資格となるまでの時間は、「**1**」を入力し、ドロップダウンから**「時間」を**選択する。

![選択したAPIキャンペーンの再資格。]({% image_buster /assets/img/decisioning_studio_go/additional_options.png %})

{: start="8"}
8. **キャンペーンを保存を**選択する。

### ステップ 5: キャンペーンIDとメッセージIDをコピーする。

1. APIキャンペーンで、**キャンペーンIDを**コピーする。次に、BrazeAI Decisioning Studio™ Goポータルに行き、**キャンペーンIDを**貼り付ける。

![コピー＆ペーストするメッセージバリエーションIDの例。]({% image_buster /assets/img/decisioning_studio_go/campaign_id.png %})

{: start="2"}
2\.**メッセージバリエーション ID** をコピーする。次に、BrazeAI Decisioning Studio™ Goポータルに行き、**メッセージバリエーションIDを**貼り付ける。

### ステップ 6: テストユーザーIDを探す

統合をテストするには、ユーザーIDが必要だ：

1. Brazeダッシュボードで、**オーディエンス**>**ユーザーを検索する**。
2. 外部ユーザーID、ユーザーエイリアス、メール、電話番号、プッシュトークンでユーザーを検索する。
3. ユーザーIDをコピーしてセットアップで参照する。

![ユーザーIDとユーザープロファイルの例。]({% image_buster /assets/img/decisioning_studio_go/user_id.png %})

{% endtab %}
{% tab Salesforce Marketing Cloud %}

## SFMC統合の設定

Decisioning Studio GoとSalesforce Marketing Cloudを統合するには、アプリパッケージを設定し、データクエリーオートメーションを作成し、トリガー送信を処理するジャーニーを構築する。

### パート 1:SFMCアプリパッケージを設定する

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
9\.アプリパッケージにのみ、以下の推奨スコープを選択する：
    \- チャネル > メール > 読み取り、書き込み、送信
    \- チャンネル > OTT > 読む
    \- チャネル > プッシュ > リード
    \- チャネル > SMS > 読む
    \- チャネル > ソーシャル > 読む
    \- チャンネル > ウェブ > 読む
    \- 資産 > ドキュメントと画像写真 > 読み取り、書き込み
    \- 資産 > 保存されたコンテンツ > 読み取り、書き込み
    \- オートメーション > オートメーション > 読み取り、書き込み、実行
    \- オートメーション > ジャーニー > 読み取り、書き込み、実行、アクティベート／停止／一時停止／送信／スケジュール
    \- コンタクト >オーディエンス > 読む
    \- 連絡先 > リストとサブスクライバー > 読み取り、書き込み
    \- Cross Cloud Platform > マーケットオーディエンス > ビュー
    \- Cross Cloud Platform > マーケットオーディエンス > ビュー
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

### パート 2:データクエリーオートメーションの設定

#### ステップ 1: 新しいオートメーションを作成する

1. Salesforce Marketing Cloudのホームから**Journey Builderに**移動し、**オートメーションスタジオを**選択する。

![ジャーニービルダーのナビゲーションにオートメーションスタジオオプションがある。]({% image_buster /assets/img/decisioning_studio_go/query13.png %})

{: start="2"}
2\.**新しいオートメーション**」を選択する。
3\.**スケジュール**ノードを**開始ソースとして**ドラッグ＆ドロップする。

!["スケジュール "を旅の出発点とする。]({% image_buster /assets/img/decisioning_studio_go/query14.png %})

{: start="4"}
4. **スケジュール**ノードで、**Configureを**選択する。
5. スケジュールには以下を設定する：
    **\- 開始日**明日のカレンダー
    **\- 時間だ：****12:00 AM**
    **\- タイムゾーン：****(GMT-05:00) 東部 (米国& カナダ)**
6. **Repeatでは**、**Dailyを**選択する。
7. このスケジュールは終わらないように設定する。
8. **完了を**選択してスケジュールを保存する。

![スケジュール例は2024年1月25日午前12時（東部標準時）、毎日繰り返される。]({% image_buster /assets/img/decisioning_studio_go/query12.png %})

#### ステップ 2:SQLクエリを作成する

次に、サブスクライバークエリーとエンゲージメントクエリーの2つのSQLクエリーを作成する。これらのクエリにより、BrazeAI Decisioning Studio™ Goはデータを取得してオーディエンスに入力し、エンゲージメントイベントを取り込むことができる。

**サブスクライバーからの問い合わせだ：**

1. **SQLクエリを**キャンバスにドラッグ＆ドロップする。
2. 選択**する**。
3. **Create New Query Activityを**選択する。
4. クエリーに名前と外部キーを付ける。BrazeAI Decisioning Studio™ Goポータルで提供されるサブスクライバークエリーの推奨される名前と外部キーを使用することを推奨する。

!["OFE_Subscribers_query_Test5" と内部キーの例。]({% image_buster /assets/img/decisioning_studio_go/query11.png %})

{: start="5"}
5. [**次へ**] を選択します。
6. BrazeAI Decisioning Studio™ Goポータルで、**サブスクライバー・クエリ・リソースの**下にあるシステムデータSQLクエリを探す。
7. クエリをコピーしてテキストボックスに貼り付け、**「Next**」を選択する。

![SQLクエリーセクションのクエリー例。]({% image_buster /assets/img/decisioning_studio_go/query10.png %})

{: start="8"}
8. BrazeAI Decisioning Studio™ Goポータルの「**使用するリソース**」セクションで、対象データ拡張子の外部キーを探す。そして、検索バーに貼り付けて検索する。

![検索バーに貼り付けられた外部キー]({% image_buster /assets/img/decisioning_studio_go/query9.png %})

{: start="9"}
9\.検索した外部キーに一致するデータ拡張子を選択する。BrazeAI Decisioning Studio™ Goポータルで相互参照するために、ターゲットデータの拡張子名も提供される。サブスクライバークエリーの**Data Extensionは**、`BASE_AUDIENCE_DATA` のサフィックスで終わるべきである。

![外部キーの例と一致するデータ拡張子名。]({% image_buster /assets/img/decisioning_studio_go/query8.png %})

{: start="10"}
10\.**Overwriteを**選択し、**Nextを**選択する。

**エンゲージメントの問い合わせだ：**

1. **SQLクエリを**キャンバスにドラッグ＆ドロップする。

![ジャーニーのアクティビティに「SQLクエリ」が追加された。]({% image_buster /assets/img/decisioning_studio_go/query7.png %})

{: start="2"}
2\.選択**する**。
3\.**Create New Query Activityを**選択する。
4. クエリーに名前と外部キーを付ける。BrazeAI Decisioning Studio™ Goポータルで提供されるエンゲージメントクエリの推奨される名前と外部キーを使用することを推奨する。

!["OFE_Engagement_query" と内部キーの例。]({% image_buster /assets/img/decisioning_studio_go/query6.png %})

{: start="5"}
5. [**次へ**] を選択します。
6. BrazeAI Decisioning Studio™ Goポータルで、**Engagement Query Resourcesの**下にSystem data SQLクエリを見つける。
7. クエリをコピーしてテキストボックスに貼り付け、**「Next**」を選択する。

![SQLクエリーセクションのクエリー例。]({% image_buster /assets/img/decisioning_studio_go/query5.png %})

{: start="8"}
8. BrazeAI Decisioning Studio™ Goポータルで指定したエンゲージメントクエリーのターゲットData Extensionを探し、選択する。

{% alert tip %}
BrazeAI Decisioning Studio™ Goポータルで相互参照するために、ターゲットデータの拡張子名も提供される。エンゲージメント・クエリーのターゲットとなるData Extensionを見ていることを確認する。エンゲージメント・クエリーの**Data Extensionは**、ENGAGEMENT_DATA というサフィックスで終わる必要がある。
{% endalert %}

{: start="9"}
9\.**Overwriteを**選択し、**Nextを**選択する。

![外部キーの例と一致するデータ拡張子名。]({% image_buster /assets/img/decisioning_studio_go/query4.png %})

#### ステップ 3:オートメーションを実行する

1. オートメーションに名前をつけ、**Saveを**選択する。

![オートメーションの例"OFE_Experimenter_Test5_Automation".]({% image_buster /assets/img/decisioning_studio_go/query3.png %})

{: start="2"}
2\.次に、「**Run Once**」を選択して、すべてが期待通りに動いていることを確認する。
3\.両方のクエリーを選択し、**Runを**選択する。

![オートメーション"OFE_Experimenter_Test5_Automation" 、実行するSQLクエリ・アクティビティを選択したリストがある。]({% image_buster /assets/img/decisioning_studio_go/query2.png %})

{: start="4"}
4. **今すぐ実行**」を選択する。

![選択されたSQLクエリのアクティビティ。]({% image_buster /assets/img/decisioning_studio_go/query1.png %})

これで、オートメーションが正常に実行されていることを確認できる。オートメーションが期待通りに作動しない場合は、Brazeサポートに問い合わせること。

### パート3：SFMCの旅を創造する

#### ステップ 1: 旅の設定

1. Salesforce Marketing Cloudで、**Journey Builder**>**Journey Builderに**進む。
2. **Create New Journeyを**選択する。
3. ジャーニーのタイプで「**Multi-Step Journey（マルチステップ・ジャーニー）**」を選択し、「**Create（作成）**」を選択する。

![条件分岐ノードと複数のメールノードに接続されたAPIイベントエントリソース。]({% image_buster /assets/img/decisioning_studio_go/journey1.png %})

#### ステップ 2:旅を構築する

**エントリソースを作成する：**

1. エントリーのソースとして、**APIイベントを**ジャーニービルダーにドラッグする。

![エントリーソースとして "APIイベント "を選択した。]({% image_buster /assets/img/decisioning_studio_go/journey2.png %})

{: start="2"}
2\.**API Eventで**、**Create an eventを**選択する。

![API Eventの "create an event "オプション。]({% image_buster /assets/img/decisioning_studio_go/journey3.png %})

{: start="3"}
3\.**Select Data Extensionを**選択する。BrazeAI Decisioning Studio™ Goがレコメンデーションを書き込むデータエクステンションを探し、選択する。
4. **Summaryを**選択して変更を保存する。
5. **Doneを**選択してAPIイベントを保存する。

![APIイベントの概要。]({% image_buster /assets/img/decisioning_studio_go/journey4.png %}){: style="max-width:80%;"}

**条件分岐を追加する：**

1. **APIエントリイベントの**後に**条件分岐を**ドラッグ＆ドロップする。
2. **条件分岐の**詳細で、最初のパスの**編集を**選択する。

![編集」ボタンで条件分岐の詳細を決定する。]({% image_buster /assets/img/decisioning_studio_go/journey5.png %})

{: start="3"}
3\.レコメンデーションデータエクステンションから渡されたテンプレートIDを使用するように、**条件分岐を**更新する。**Journey Dataの**下にある適切なフィールドを探す。

![条件分岐のパス1にあるジャーニー・データのセクション。]({% image_buster /assets/img/decisioning_studio_go/journey6.png %})

{: start="4"}
4. エントリイベントを選択し、目的のテンプレートIDフィールドを探し、ワークスペースにドラッグする。

![含まれるメールテンプレートID。]({% image_buster /assets/img/decisioning_studio_go/journey7.png %})

{: start="5"}
5. 最初のメールテンプレートのテンプレートIDを入力し、「**完了**」を選択する。
6. このパスを保存するには「**Summary**」を選択する。
7. 各メールテンプレートのパスを追加し、上記のステップ4～6を繰り返して、テンプレートIDが各テンプレートのID値と一致するようにフィルター条件を設定する。
8. **Doneを**選択して**条件分岐**ノードを保存する。

![各メールテンプレートIDに対して、条件分岐で2つのパスを設定する。]({% image_buster /assets/img/decisioning_studio_go/journey10.png %}){: style="max-width:65%;"}

**条件分岐ごとにメールを追加する：**

1. **条件分岐の**各パスに**メール**ノードをドラッグする。
2. **メールを**選択し、各パスに入る適切なテンプレートを選択する（つまり、ID値を持つテンプレートが条件分岐のロジックと一致する必要がある）。

![ジャーニーに追加されたメールノード。]({% image_buster /assets/img/decisioning_studio_go/journey9.png %})

#### ステップ 3:旅を活性化する

Journeyの設定後、Journeyを有効化し、以下の詳細をBrazeAI Decisioning Studio™ Goチームと共有する：

* 旅のID
* 旅程名
* APIイベント定義キー
* 推奨データ拡張外部キー

{% alert note %}
BrazeAI Decisioning Studio™ Goポータルには、1日1回サブスクライバーとエンゲージメントデータをエクスポートするためにプロビジョニングしたSFMCオートメーションが表示される。SFMCでこのオートメーションを開封したら、必ず一時停止を解除し、ライブに戻すこと。
{% endalert %}

1. BrazeAI Decisioning Studio™ Goポータルで、**ジャーニー名を**コピーする。
2. 次に、Salesforce Marketing Cloud Journey Builderで、ジャーニー名を検索バーに貼り付ける。
3. ジャーニー名を選択する。なお、「旅」は現在ドラフトステータスである。
4. **Validateを**選択する。

![完成した活性化への旅。]({% image_buster /assets/img/decisioning_studio_go/activate3.png %})

{: start="5"}
5. その後、検証結果を確認し、**Activateを**選択する。

![バリデーションルールのセクションに記載されている推奨事項。]({% image_buster /assets/img/decisioning_studio_go/activate1.png %}){: style="max-width:60%;"}

{: start="6"}
6. **Activate Journey**要約で、再度**Activateを**選択する。

![旅のまとめ]({% image_buster /assets/img/decisioning_studio_go/activate2.png %}){: style="max-width:85%;"}

すべて完了しました。BrazeAI Decisioning Studio™ Goでトリガーを開始できる。

{% endtab %}
{% endtabs %}

## 次のステップ

オーケストレーションの設定ができたところで、エージェントの設計に進む：

- [エージェントの設計]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/design_your_agent/)
