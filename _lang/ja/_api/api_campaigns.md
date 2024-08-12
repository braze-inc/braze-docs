---
nav_title: API キャンペーン
article_title: API キャンペーン
page_order: 5
description: "このリファレンス記事では、API コールに含めるcampaign_id を生成する方法と、そのキャンペーンを設定する方法について説明します。"
page_type: reference
tool: Campaigns

---
# APIキャンペーン

> このリファレンス記事では、`campaign_id` を生成してAPI コールに含める方法と、そのキャンペーンを設定する方法について説明します。

API キャンペーンは通常、トランザクションメッセージングに使用されます。API キャンペーンを登録する場合([API トリガキャンペーン]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/) ではなく)、Braze ダッシュボードは`campaign_id` の生成にのみ使用され、キャンペーンレポートの分析を追跡できます。また、キャンペーンのバリアントごとに異なるメッセージバリエーションID を生成することもできます。 

次に、その情報を開発チームに送信し、API リクエストで使用します。
\- キャンペーンコピー
\- 視聴者メンバーシップ
アセット

キャンペーンが開始されたら、ダッシュボードで結果を表示できます。API キャンペーンでは、Braze [メッセージングAPI]({{site.baseurl}}/api/endpoints/messaging/) を使用します。これは、ダッシュボードで完全に作成されたキャンペーンと同じ詳細なレポートおよびターゲット変更オプションを持ちます。

{% alert warning %}
API キャンペーンは通常トランザクションであるため、Global Control Group 内のユーザでも、すべてのユーザがAPI キャンペーンの対象になります。
{% endalert %}

## 新しいキャンペーンを作成する

**Messaging**> **Campaigns**に進み、**Create Campaign**をクリックし、**API Campaigns**を選択します。これで、API キャンペーンの設定に進むことができます。

[API トリガキャンペーン]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/) はAPI キャンペーンとは異なります。

## キャンペーンの設定

キャンペーンを設定するには、次の手順を実行します。

1. メッセージを送信した後、キャンペーンページで結果を確認できるように、説明的なタイトルを追加します。
2. **Add Message**をクリックし、API キャンペーンに含まれるメッセージタイプを追加します。これにより、`campaign_id` とメッセージバリエーションID を生成できます。これらは、含めるチャンネルごとに異なります。 
3. 必要に応じて、特定のアクションまたはキャンペーン目標のユーザ変換を追跡する変換イベントを追加できます。
4. **Save Campaign**をクリックすると、APIキャンペーンを開始するように設定されます!

## APIコール

API キャンペーンを保存した後、API リクエストに以下を含めます。
\- 生成された`campaign_id` フィールドとAPI リクエスト。[メッセージエンドポイントの送信][2] に記載されています。
\- キャンペーンに含まれる各プラットフォームの[message オブジェクト]({{site.baseurl}}/api/objects_filters/#messaging-objects)。メッセージオブジェクトで、メッセージバリエーションID を指定します。これにより、統計を収集し、そのバリアントの下に表示するように指定します。以下のメッセージオブジェクトがサポートされています。Android、コンテンツカード、メール、iOS、Kindle、SMS/MMS、ウェブプッシュ、ウェブフック。

[2]: {{site.baseurl}}/api/endpoints/messaging/#send-endpoints

