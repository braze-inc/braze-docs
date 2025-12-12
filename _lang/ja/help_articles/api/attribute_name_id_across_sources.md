---
nav_title: Brazeにおけるキャンペーン属性とキャンバス属性の違い
article_title: Brazeにおけるキャンペーン属性とキャンバス属性の違い
page_order: 1

page_type: reference
description: "このヘルプ記事では、キャンペーンとキャンバスの属性の名前と ID を Braze のソース間で比較します。"
platform: API
---

# キャンペーンとキャンバスの属性は、Brazeのソースによってどのように異なるのか？

キャンペーン、キャンバス、キャンバスステップの名前と ID はすべて、Liquid、REST API、Currents で利用できます。これらの属性は、3 つのソースすべてで同じ値にマッピングされますが、名前は異なる場合があります。このページは、3 つの間の接続を描くのに役立ちます。

## ユースケース

### Liquid

キャンペーンおよびキャンバスの属性は、ダッシュボード{% raw %} (`{{campaign.${api_id}}}` など) {% endraw %} で Liquid タグとして使用できます。Liquid を使用して、これらの属性をメッセージ自体や Connected Content 呼び出しで、またはキーと値のペアとして渡すことができます。これは通常、トラッキングの目的で行われる。

### REST API

キャンペーンとキャンバスの属性は、[キャンペーンの詳細をエクスポートするエンドポイント]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details/)または[キャンバスの詳細をエクスポートするエンドポイントでも]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/)利用できる。REST API を使用してマッピングを構築できます。これは、すべてのキャンバス名と、対応する ID のリストです。

### Currents

キャンペーンとキャンバスの属性s は、Currents の[メッセージエンゲージメントイベント]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) に関連付けられています。これは、プッシュ送信やメール開封が関連付けられているキャンペーンまたはキャンバスコンポーネントを特定するために重要です。

## キャンペーン属性

| 属性 | Liquid | REST API | Currents |
| --- | --- | --- | --- |
| キャンペーン名 | {% raw %}`{{campaign.${name}}}`{% endraw %} | `name` | `campaign_name` |
| キャンペーン ID | {% raw %}`{{campaign.${api_id}}}`{% endraw %} | 該当なし（APIコール自体の入力として使用される） | campaign_id |
| 変種名 | {% raw %}`{{campaign.${message_name}}}`{% endraw %} | `messages.message_variation_id.name` | 該当なし（キャンペーン詳細のエクスポートエンドポイントを使ってバリアント名をバリアント ID にマップする） |
| バリアントID | {% raw %}`{{campaign.${message_api_id}}}`{% endraw %} | `messages.message_variation_id` | `message_variation_api_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## キャンバスの属性

| 属性 | Liquid | REST API | Currents |
| --- | --- | --- | --- |
| キャンバス名 | {% raw %}`{{canvas.${name}}}`{% endraw %} | `name` | `canvas_name` |
| キャンバスID | {% raw %}`{{canvas.${api_id}}}`{% endraw %} | 該当なし（APIコール自体の入力として使用される） | canvas_id |
| 変種名 | {% raw %}`{{canvas.${variant_name}}}`{% endraw %} | `variants.name` | `canvas_variation_name` |
| バリアントID | {% raw %}`{{canvas.${variant_api_id}}}`{% endraw %} | `variants.name.id` | `canvas_variation_id` |
| ステップ名 | {% raw %}`{{campaign.${name}}}`{% endraw %} | `steps.name` | `canvas_step_name` |
| ステップID | {% raw %}`{{campaign.${api_id}}}`{% endraw %} | `steps.id` | `canvas_step_id` |
| メッセージチャンネル | 該当なし | `steps.messages.message_variation_id.channel` | 該当なし（プッシュ送信やメール開封など、イベントタイプに固有のもの） |
| メッセージID | {% raw %}`{{campaign.${message_api_id}}}`{% endraw %} | `steps.message.message_variation_id` | `canvas_step_message_variation_api_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }