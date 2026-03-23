---
nav_title: オーケストレーションを設定する
article_title: オーケストレーションを設定する
page_order: 2
description: "BrazeAI Decisioning Studio Goをカスタマーエンゲージメントプラットフォームに接続する方法を学び、パーソナライズされたコミュニケーションを実現する。"
toc_headers: h2
---

# オーケストレーションを設定する

> BrazeAI Decisioning Studio™ Goは、パーソナライズされたコミュニケーションのオーケストレーションを行うために、カスタマーエンゲージメントプラットフォーム（CEP）に接続する必要がある。この記事では、サポートされている各CEPの統合設定方法を説明する。

## サポートされているCEP

Decisioning Studio Goは、以下のカスタマーエンゲージメントプラットフォームをサポートする：

| CEP | 統合タイプ | 主要な機能 |
|-----|-----------------|--------------|
| **Braze** | API トリガーキャンペーン | ネイティブ統合、リアルタイムトリガー |
| **セールスフォース・マーケティングクラウド** | APIイベントを使ったジャーニービルダー | SQLクエリーのオートメーション、データ拡張 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

以下のCEPを選択して、統合設定を開始する。

{% tabs %}
{% tab Braze %}

## Brazeの連携設定

Decisioning Studio GoをBrazeと統合するには、API キーを作成し、APIトリガー型キャンペーンを設定し、必要な識別子をDecisioning Studio Goポータルに提供する。

### ステップ 1: REST APIキーを作成する

1. Brazeのダッシュボードで、**設定**＞**APIと識別子**＞**API キー**に移動する。
2. [**API キーを作成**] を選択します。
3. API キーの名前を入力せよ。例として「DecisioningStudioGoEmail」がある。
4. 以下のカテゴリに基づいて権限を選択する：
    - **ユーザーデータ：**選択する `users.track`, `users.delete`, `users.export.ids`, `users.export.segment`
    - **メッセージング：**選択 `messages.send`
    - **キャンペーン：**リストされたすべての権限を選択する
    - **キャンバス：**リストされている全ての権限を選択する
    - **セグメント：**リストされている全ての権限を選択する
    - **テンプレート：**リストされている全ての権限を選択する

{: start="5"}
5. [**API キーを作成**] を選択します。
6. API キーをコピーし、BrazeAI Decisioning Studio™ Goポータルに貼り付けろ。

### ステップ 2:メールの表示名を確認する

1. Brazeのダッシュボードで、**設定**＞**メール設定**に移動する。
2. BrazeAI Decisioning Studio™ Goで使用する表示名を探せ。
3. 「**From Display Name**」をコピーして、BrazeAI Decisioning Studio™ Go ポータルに「**Email Display Name**」として貼り付けろ。
4. 関連するメールアドレスを、**送信元メールアドレス**としてBrazeAI Decisioning Studio™ Goポータルにコピー＆ペーストする。このメールアドレスはローカル部分とドメインを組み合わせたものである。

### ステップ 3:BrazeのURLとApp IDを見つける

**BrazeのURLを見つけるには：**
1. Brazeのダッシュボードに行け。
2. ブラウザのウィンドウでは、BrazeのURLは で始まり`https://`、 で終わる`braze.com`。例として、BrazeのURLはである`https://dashboard-01.braze.com`。

**アプリ ID（API キー）を見つけるには：**

{% alert note %}
BrazeはアプリID（BrazeダッシュボードではAPI キーと呼ばれる）を提供している。これはトラッキング目的で使用でき、例えばワークスペース内の特定のアプリとアクティビティを関連付けるのに役立つ。アプリIDを使用する場合、BrazeAI Decisioning Studio™ Goは各実験担当者にアプリIDを関連付けることをサポートする。<br><br>アプリIDを使用しない場合、任意の文字列をプレースホルダーとして入力できる。
{% endalert %}

1. Brazeのダッシュボードで、**設定**＞**アプリ設定**に移動する。
2. トラッキングしたいアプリを開け。
3. **API キー**をコピーして、BrazeAI Decisioning Studio™ Goポータルに貼り付けろ。

### ステップ 4: APIトリガー型キャンペーンを作成する

1. Brazeのダッシュボードで、**メッセージング**＞**キャンペーン**に移動する。
2. **キャンペーンを作成する**を選択する。
3. キャンペーンの種類として、**APIキャンペーン**を選択せよ。
4. キャンペーン名を入力します。例として「Decisioning Studio Go メール」がある。

![「Decisioning Studio Go メール」というAPIキャンペーン。]({% image_buster /assets/img/decisioning_studio_go/api_campaign_name.png %})

{: start="5"}
5. メッセージングチャネルとして、**メール**を選択せよ。

![APIキャンペーンのメッセージングチャネルを選択するオプション。]({% image_buster /assets/img/decisioning_studio_go/select_api_campaign.png %})

{: start="6"}
6. **追加オプション**で、**「ユーザーがキャンペーンの受取資格を再取得できるようにする」**チェックボックスを選択する。
7. 再資格取得までの期間を設定するには、**1**を入力し、ドロップダウンから**「時間」**を選択せよ。

![選択したAPIキャンペーンの再参加資格。]({% image_buster /assets/img/decisioning_studio_go/additional_options.png %})

{: start="8"}
8. **キャンペーンを保存する**を選択する。

### ステップ 5: キャンペーンとメッセージのIDをコピーしろ

1. APIキャンペーンでは、**キャンペーンID**をコピーする。次に、BrazeAI Decisioning Studio™ Go ポータルに移動し、**キャンペーンID**を貼り付ける。

![コピーして貼り付けるメッセージバリエーションIDの例だ。]({% image_buster /assets/img/decisioning_studio_go/campaign_id.png %})

{: start="2"}
2\.**メッセージバリエーションID**をコピーする。次に、BrazeAI Decisioning Studio™ Go ポータルに移動し、**メッセージバリエーションID**を貼り付ける。

### ステップ 6: テストユーザー IDを探す

統合をテストするには、ユーザー ID が必要だ。

1. Brazeのダッシュボードで、**オーディエンス**＞**ユーザー検索**へ移動する。
2. ユーザーを外部ユーザー ID、ユーザーエイリアス、メール、電話番号、またはプッシュトークンで検索する。
3. 設定で参照するためにユーザー IDをコピーせよ。

![ユーザー ID でユーザーを検索した際のユーザープロファイルの例。]({% image_buster /assets/img/decisioning_studio_go/user_id.png %})

{% endtab %}
{% tab Salesforce Marketing Cloud %}

## SFMC統合の設定

Decisioning Studio GoをSalesforce Marketing Cloudと統合するには、アプリパッケージを設定し、データクエリアオートメーションを作成し、トリガー送信を処理するJourneyを構築する。

### パート 1:SFMCアプリパッケージを設定する

1. マーケティングクラウドのホームページに移動する。
2. グローバルヘッダーのメニューを開封し、**設定**を選択する。
3. サイドパネルのナビゲーションで**「プラットフォームツール」**内の**「アプリ」**に移動し、「**インストール済みパッケージ**」を選択する。
4. **新規**を選択してアプリパッケージを作成する。
5. アプリパッケージに名前と説明を付ける。

![「実験者1 - テスト5」という名前のアプリパッケージ。]({% image_buster /assets/img/decisioning_studio_go/sfmc_app_package1.png %})

{: start="6"}
6. **コンポーネントの追加**を選択する。
7. **コンポーネントタイプ**には、**API統合**を選択する。次に、**「次へ」**を選択する。
8. **統合タイプ**では、**サーバー間**を選択する。次に、**「次へ」**を選択する。
9\.アプリパッケージに対してのみ、以下の推奨スコープを選択せよ：
    \- チャネル > メール > 読み取り、書き込み、送信
    \- チャネル > OTT > 読む
    \- チャネル > プッシュ > 読み取り
    \- チャネル > SMS > 読む
    \- チャネル > ソーシャル > 読む
    \- チャネル > Web > 読む
    \- アセット > ドキュメントと写真 > 読み取り、書き込み
    \- アセット > 保存済みコンテンツ > 読み取り、書き込み
    \- オートメーション > オートメーション > 読み取り、書き込み、実行
    \- オートメーション > ジャーニー > 読み取り、書き込み、実行、起動/停止/一時停止/送信/スケジュールされた送信
    \- 連絡先 > オーディエンス > 読む
    \- 連絡先 > リストとサブスクライバー > 読み取り、書き込み
    \- クロスクラウドプラットフォーム > 市場オーディエンス > 表示
    \- クロスクラウドプラットフォーム > 市場オーディエンスメンバー > 表示
    \- クロスクラウドプラットフォーム > マーケティングクラウドコネクト > 読み取り
    \- データ > データ拡張機能 > 読み取り、書き込み
    \- データ > ファイルの場所 > 読み取り
    \- データ > トラッキングイベント > 読み取り、書き込み
    \- イベント通知 > コールバック > 読み取り
    \- イベント通知 > サブスクリプション > 読む

{% details Show image of recommended scopes %}

![Salesforce Marketing Cloudアプリパッケージの推奨スコープ。]({% image_buster /assets/img/decisioning_studio_go/app_package_scopes.png %})

{% enddetails %}

{: start="10"}
10\.[**保存**] を選択します。
11\.以下のフィールドをBrazeAI Decisioning Studio™ Goポータルにコピーして貼り付けろ：**クライアントID**、**クライアントシークレット**、**認証ベースURI**、**RESTベースURI**、**SOAPベースURI**。

### パート 2:データクエリのオートメーションを設定する

#### ステップ 1: 新しいオートメーションを作成する

1. Salesforce Marketing Cloud のホーム画面から、**Journey Builder** に移動し、**オートメーション Studio** を選択する。

![ジャーニービルダーのナビゲーションにあるオートメーションスタジオのオプション。]({% image_buster /assets/img/decisioning_studio_go/query13.png %})

{: start="2"}
2\.**新しいオートメーション**を選択する。
3\.**スケジュール**ノードをドラッグ＆ドロップして**開始ソース**とする。

![「スケジュール」をジャーニーの開始元とする。]({% image_buster /assets/img/decisioning_studio_go/query14.png %})

{: start="4"}
4. **スケジュール**ノードで、**設定**を選択する。
5. スケジュールには以下を設定する：
    - **開始日：**明日の暦日
    - **時間：****午前0時**
    - **タイムゾーン：****(GMT-05:00) 東部 (米国 &カナダ)**
6. **繰り返し**設定では、**毎日**を選択する。
7. このスケジュールを永遠に終わらないように設定しろ。
8. スケジュールを保存するには**「完了」**を選択せよ。

![2024年1月25日午前0時（米国東部時間）に定義されたスケジュール例。毎日繰り返される。]({% image_buster /assets/img/decisioning_studio_go/query12.png %})

#### ステップ 2:SQLクエリを作成する

次に、2つのSQLクエリを作成する：サブスクライバークエリとエンゲージメントクエリだ。これらのクエリにより、BrazeAI Decisioning Studio™ Goはオーディエンスを埋めるデータとエンゲージメントイベントを取得できる。

**サブスクライバーの問い合わせ：**

1. **SQLクエリ**をキャンバスにドラッグ＆ドロップする。
2. 選択**せよ**。
3. **新規クエリアクティビティの作成**を選択する。
4. クエリに名前と外部キーを付ける。BrazeAI Decisioning Studio™ Go ポータルで提供されているサブスクライバー クエリ用の推奨名と外部キーを使用することを推奨する。

![例"OFE_Subscribers_query_Test5"と外部キー。]({% image_buster /assets/img/decisioning_studio_go/query11.png %})

{: start="5"}
5. [**次へ**] を選択します。
6. BrazeAI Decisioning Studio™ Go ポータルで、**サブスクライバー クエリ リソース**の下にあるシステム データ SQL クエリを探せ。
7. クエリをテキストボックスにコピーして貼り付け、**次に進む**を選択する。

![SQLクエリセクションの例示クエリ。]({% image_buster /assets/img/decisioning_studio_go/query10.png %})

{: start="8"}
8. BrazeAI Decisioning Studio™ Go ポータル内の「**使用するリソース**」セクションで、対象データ拡張の外部キーを探せ。それから、検索バーに貼り付けて検索するんだ。

![検索バーに貼り付けられた外部キー]({% image_buster /assets/img/decisioning_studio_go/query9.png %})

{: start="9"}
9\.検索した外部キーに一致するデータ拡張を選択せよ。ターゲットデータ拡張子の名前は、参照用にBrazeAI Decisioning Studio™ Goポータルにも記載されている。サブスクライバークエリのデータ拡張子は、接尾`BASE_AUDIENCE_DATA`辞で終わるべきだ。

![例示された外部キーに一致するデータ拡張子の名前。]({% image_buster /assets/img/decisioning_studio_go/query8.png %})

{: start="10"}
10\.**上書き**を選択し、次に**進む**。

**エンゲージメントクエリ：**

1. **SQLクエリ**をキャンバスにドラッグ＆ドロップする。

![「SQLクエリ」がジャーニーのアクティビティとして追加された。]({% image_buster /assets/img/decisioning_studio_go/query7.png %})

{: start="2"}
2\.選択**せよ**。
3\.**新規クエリアクティビティの作成**を選択する。
4. クエリに名前と外部キーを付ける。BrazeAI Decisioning Studio™ Go ポータルで提供されているエンゲージメント クエリには、推奨される名前と外部キーを使用することを推奨する。

![例"OFE_Engagement_query"と外部キー。]({% image_buster /assets/img/decisioning_studio_go/query6.png %})

{: start="5"}
5. [**次へ**] を選択します。
6. BrazeAI Decisioning Studio™ Go ポータルで、**エンゲージメント クエリ リソース**の下にあるシステム データ SQL クエリを探せ。
7. クエリをテキストボックスにコピーして貼り付け、**次に進む**を選択する。

![SQLクエリセクションの例示クエリ。]({% image_buster /assets/img/decisioning_studio_go/query5.png %})

{: start="8"}
8. BrazeAI Decisioning Studio™ Go ポータルで指定されたエンゲージメントクエリの対象となるデータエクステンションを探し、選択する。

{% alert tip %}
ターゲットデータ拡張子の名前は、参照用にBrazeAI Decisioning Studio™ Goポータルにも記載されている。エンゲージメントクエリのターゲットとなるデータエクステンションを確認していることを確認せよ。エンゲージメントクエリのデータ拡張子は、接尾ENGAGEMENT_DATA辞で終わるべきだ。
{% endalert %}

{: start="9"}
9\.**上書き**を選択し、次に**進む**。

![例示された外部キーに一致するデータ拡張子の名前。]({% image_buster /assets/img/decisioning_studio_go/query4.png %})

#### ステップ 3:オートメーションを実行する

1. オートメーションに名前を付け、**保存**を選択する。

![オートメーションの例    "OFE_Experimenter_Test5_Automation".]({% image_buster /assets/img/decisioning_studio_go/query3.png %})

{: start="2"}
2\.次に、**一度だけ実行**を選択して、すべてが期待通りに動作していることを確認する。
3\.両方のクエリを選択し、**実行**を選択する。

![実行するSQLクエリアクティビティの選択リストを持つ"OFE_Experimenter_Test5_Automation"オートメーション。]({% image_buster /assets/img/decisioning_studio_go/query2.png %})

{: start="4"}
4. **今すぐ実行**を選択せよ。

![選択されたSQLクエリアクティビティ。]({% image_buster /assets/img/decisioning_studio_go/query1.png %})

さて、オートメーションが正常に動作しているか確認できる。オートメーションが期待通りに動作しない場合は、Brazeサポートに連絡して追加の支援を受けよ。

### パート3：SFMCの旅を始めよう

#### ステップ 1: 旅の準備を整える

1. セールスフォース・マーケティングクラウドで、**ジャーニービルダー**＞**ジャーニービルダー**に移動する。
2. **新規ジャーニーを作成**を選択せよ。
3. 旅程タイプとして「**複数ステップの旅程**」を選択し、次に**「作成**」を選択する。

![APIエントリのソースが、条件分岐ノードと複数のメールノードに接続されている。]({% image_buster /assets/img/decisioning_studio_go/journey1.png %})

#### ステップ 2:旅を築け

**エントリソースを作成する：**

1. エントリソースとして、**APIイベントを**ジャーニービルダーにドラッグする。

![「APIイベント」がエントリ元として選択された。]({% image_buster /assets/img/decisioning_studio_go/journey2.png %})

{: start="2"}
2\.**APIイベント**で、**イベントを作成する**を選択する。

![APIイベントの「イベントを作成する」オプション。]({% image_buster /assets/img/decisioning_studio_go/journey3.png %})

{: start="3"}
3\.**データ拡張**を選択せよ。BrazeAI Decisioning Studio™ Goが推奨事項を書き込むデータ拡張機能を探し、選択する。
4. 変更を保存するには**「概要」**を選択せよ。
5. **「完了」**を選択してAPIイベントを保存する。

![APIイベントの概要。]({% image_buster /assets/img/decisioning_studio_go/journey4.png %}){: style="max-width:80%;"}

**条件分岐を追加する：**

1. **APIエントリイベント**の後に**、条件分岐**をドラッグ＆ドロップする。
2. **条件分岐**の詳細で、最初のパスに対して**編集**を選択する。

![「編集」ボタンで条件分岐の詳細を確認する。]({% image_buster /assets/img/decisioning_studio_go/journey5.png %})

{: start="3"}
3\.レコメンデーションデータ拡張機能から渡されたテンプレートIDを使用するように**、条件分岐**を更新する。**旅程データ**の下にある適切なフィールドを探せ。

![条件分岐のパス1にある「旅程データ」セクション。]({% image_buster /assets/img/decisioning_studio_go/journey6.png %})

{: start="4"}
4. エントリイベントを選択し、目的のテンプレートIDフィールドを探し、それをワークスペースにドラッグする。

![含めるべきメールテンプレートID。]({% image_buster /assets/img/decisioning_studio_go/journey7.png %})

{: start="5"}
5. 最初のメールテンプレートのテンプレートIDを入力し、**完了**を選択する。
6. このパスを保存するには**「概要」**を選択せよ。
7. 各メールテンプレートにパスを追加し、その後、上記のステップ4～6を繰り返してフィルター条件を設定する。テンプレートIDが各テンプレートのID値と一致するようにするのだ。
8. **条件分岐**ノードを保存するには**「完了」**を選択する。

![各メールテンプレートIDごとに、条件分岐で2つのパスがある。]({% image_buster /assets/img/decisioning_studio_go/journey10.png %}){: style="max-width:65%;"}

**各条件分岐ごとにメールを追加する。**

1. **条件分岐**の各パスに**メール**ノードをドラッグする。
2. **メール**を選択し、各パスに適用すべき適切なテンプレートを選択する（つまり、ID値を持つテンプレートが、あなたの条件分岐のロジックと一致する必要がある）。

![ジャーニーに追加されたメールノード。]({% image_buster /assets/img/decisioning_studio_go/journey9.png %})

#### ステップ 3:旅を始めろ

ジャーニーを設定したら、それを有効化し、以下の詳細をBrazeAI Decisioning Studio™ Goチームと共有する：

* 旅のID
* 旅の名前
* APIイベント定義キー
* 推薦データ拡張外部キー

{% alert note %}
BrazeAI Decisioning Studio™ Go ポータルは、サブスクライバーとエンゲージメントデータを1日1回エクスポートするために設定したSFMCオートメーション機能を表示する。このオートメーションをSFMCで開封する場合、必ず一時停止を解除してライブ状態に戻すこと。
{% endalert %}

1. BrazeAI Decisioning Studio™ Go ポータルで、**ジャーニー名を**コピーする。
2. 次に、Salesforce Marketing Cloud Journey Builder で、ジャーニー名を検索バーに貼り付ける。
3. 旅程名を選択せよ。なお、この旅は現在下書きステータスにある。
4. **「検証」**を選択せよ。

![完了した旅を起動する。]({% image_buster /assets/img/decisioning_studio_go/activate3.png %})

{: start="5"}
5. 次に、検証結果を確認し、**「有効化」**を選択する。

![検証ルールセクションに記載されている推奨事項。]({% image_buster /assets/img/decisioning_studio_go/activate1.png %}){: style="max-width:60%;"}

{: start="6"}
6. **「アクティベート・ジャーニー**」のサマリーで、もう一度**「アクティベート」**を選択する。

![旅のまとめ。]({% image_buster /assets/img/decisioning_studio_go/activate2.png %}){: style="max-width:85%;"}

すべて完了しました。BrazeAI Decisioning Studio™ Goを通じて送信をトリガーできるようになりました。

{% endtab %}
{% endtabs %}

## 次のステップ

オーケストレーションの設定が完了したから、次にエージェントの設計に進む：

- [エージェントの設計]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/design_your_agent/)
