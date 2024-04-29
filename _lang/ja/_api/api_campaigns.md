---
nav_title: API キャンペーン
article_title: API キャンペーン
page_order: 5
description: "このリファレンス記事では、API 呼び出しに含める campaign_id を生成する方法と、そのキャンペーンを構成する方法について説明します。"
page_type: reference
tool: Campaigns

---
# API キャンペーン

> この参考記事では、 `campaign_id`API 呼び出しに含める内容と、そのキャンペーンを構成する方法について説明します。

API キャンペーンは通常、トランザクション メッセージングに使用されます。APIキャンペーン（[APIトリガーキャンペーン]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/)ではない）を作成する場合、Brazeダッシュボードは、 `campaign_id`、キャンペーンレポートの分析を追跡できます。キャンペーン内のバリエーションごとに異なるメッセージ バリエーション ID を生成することもできます。 

次に、その情報を以下の情報とともに開発チームに送信し、API リクエストで使用します。
\- キャンペーンコピー
\- 観客のメンバーシップ
\- アセット

キャンペーンが開始すると、ダッシュボードで結果を確認できます。API キャンペーンでは、ダッシュボードから完全に作成されたキャンペーンと同じ詳細なレポートとリターゲティング オプションを備えた Braze [メッセージング API]({{site.baseurl}}/api/endpoints/messaging/)が使用されます。

{% alert warning %}
API キャンペーンは通常トランザクション型であるため、グローバル コントロール グループ内のユーザーも含め、すべてのユーザーが API キャンペーンの対象となります。
{% endalert %}

## 新しいキャンペーンを作成する

**「メッセージング」**>**「キャンペーン」** に移動し、**「キャンペーンの作成」を**クリックして、**「API キャンペーン」**を選択します。これで、API キャンペーンの設定に進むことができます。

[API トリガー キャンペーンは]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/) API キャンペーンとは異なります。

## キャンペーンを設定する

キャンペーンを設定するには、次の手順を実行します。

1. メッセージを送信した後、キャンペーン ページで結果を見つけられるように、わかりやすいタイトルを追加します。
2. **「メッセージの追加」** をクリックし、API キャンペーンに含めるメッセージ タイプを追加します。これにより、 `campaign_id` メッセージ バリエーション ID は、含めるチャネルごとに異なります。 
3. オプションで、コンバージョン イベントを追加して、特定のアクションまたはキャンペーン目標でのユーザー コンバージョンを追跡できます。
4. **「キャンペーンを保存」** をクリックすると、API キャンペーンを開始する準備が整います。

## API 呼び出し:

API キャンペーンを保存したら、API リクエストに次の内容を含めます。
\- 生成された `campaign_id`[メッセージ送信エンドポイント][2]に記載されている API リクエストのフィールド。
\- キャンペーンに含まれる各プラットフォームの [メッセージ オブジェクト]({{site.baseurl}}/api/objects_filters/#messaging-objects) 。メッセージ オブジェクトに、メッセージ バリエーション ID を指定します。これにより、統計が収集され、そのバリアントの下に表示されるようになります。次のメッセージ オブジェクトがサポートされています。Android、コンテンツ カード、電子メール、iOS、Kindle、SMS/MMS、Web プッシュ、Webhook。

[2]: {{site.baseurl}}/api/endpoints/messaging/#send-endpoints

