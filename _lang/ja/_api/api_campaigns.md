---
nav_title: API キャンペーン
article_title: API キャンペーン
page_order: 5
description: "このリファレンス記事では、APIコールに含めるcampaign_idの生成方法と、そのキャンペーンの設定方法について説明します。"
page_type: reference
tool: Campaigns

---
# APIキャンペーン

> このリファレンス記事では、API呼び出しに含める`campaign_id`の生成方法とそのキャンペーンの設定方法について説明します。

API キャンペーンは通常、トランザクションメッセージングに使用されます。APIキャンペーン（[APIトリガーキャンペーン]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/)ではない）を作成する場合、Brazeダッシュボードは`campaign_id`を生成するためだけに使用され、キャンペーンレポートの分析を追跡できます。また、キャンペーン内の各バリアントごとに異なるメッセージバリエーションIDを生成することもできます。 

次に、その情報を以下の情報とともに開発チームに送信し、API リクエストで使用します。
- キャンペーンコピー
- オーディエンスメンバーシップ
- 資産

キャンペーンが始まった後、結果をダッシュボードで確認できます。APIキャンペーンはBrazeの[メッセージングAPI]({{site.baseurl}}/api/endpoints/messaging/)を使用します。これらのAPIは、ダッシュボードを通じて完全に作成されたキャンペーンと同じ詳細なレポートおよびリターゲティングオプションを備えています。

{% alert warning %}
APIキャンペーンは通常トランザクション型であるため、グローバルコントロールグループに属するユーザーも含め、すべてのユーザーがAPIキャンペーンの対象となります。これらの送信には[ワンクリックリスト配信停止]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#list-unsubscribe)ヘッダーが追加されません。すべての API キャンペーンにワンクリックリスト登録解除ヘッダーを追加する場合は、カスタマーサクセスマネージャーにお問い合わせください。
{% endalert %}

## 新しいキャンペーンを作成する

[**メッセージング**] > [**キャンペーン**] に移動して [**キャンペーンを作成**] を選択し、[**API キャンペーン**] を選択します。これで、API キャンペーンの設定に進むことができます。

[API トリガーキャンペーン]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/)は、API キャンペーンとは異なります。

## キャンペーンを設定する

キャンペーンを設定するには、次の手順を実行します:

1. メッセージを送信した後、キャンペーンページで結果を見つけられるように、説明的なタイトルを追加してください。
2. **Add Message** をクリックして、APIキャンペーンに含まれるメッセージタイプを追加します。これにより、`campaign_id`とメッセージバリエーションIDを生成できます。これは、含める各チャネルごとに異なります。 
3. オプションとして、特定のアクションやキャンペーン目標でユーザーのコンバージョンを追跡するためにコンバージョンイベントを追加できます。
4. **キャンペーンを保存**をクリックすると、APIキャンペーンを開始する準備が整います！

## API呼び出し

API キャンペーンを保存したら、API リクエストに次の内容を含めます。 
- API リクエストで生成された `campaign_id` フィールドは、[]({{site.baseurl}}/api/endpoints/messaging/#send-endpoints)「メッセージ送信」エンドポイント[]({{site.baseurl}}/api/endpoints/messaging/#send-endpoints)に記載されています。
- キャンペーンに含まれる各プラットフォームの[メッセージオブジェクト]({{site.baseurl}}/api/objects_filters/#messaging-objects)。メッセージオブジェクトにメッセージバリエーションIDを提供します。これにより、統計が収集され、そのバリアントの下に表示されるように指定されます。次のメッセージオブジェクトがサポートされています：Android、コンテンツカード、メール、iOS、Kindle、SMS/MMS、Web プッシュ、Webhook。


