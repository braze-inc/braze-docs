---
nav_title: キャンペーンとキャンバスの属性は、ソースによってどのように異なるのか？
article_title: キャンペーンとキャンバスの属性は、Brazeのソースによってどのように異なるか。 
page_order: 1

page_type: reference
description: "このヘルプ記事では、Brazeのソース間でキャンペーンとキャンバスの属性名とIDを比較する。"
platform: API
---

# キャンペーンとキャンバスの属性は、Brazeのソースによってどのように異なるか。

キャンペーン、キャンバス、キャンバスステップの名前とIDはすべて、Liquid、REST API、Currentsで利用できる。これらの属性は、3つのソースすべてで同じ値にマッピングされるが、名前は異なる場合がある。このページは、この3つのつながりを描くためのものである。

## ユースケース

### Liquid

キャンペーンとキャンバスの属性は、ダッシュボードのLiquidタグとして利用できる{% raw %} （`{{campaign.${api_id}}}` ）{% endraw %} 。Liquidを使って、これらの属性をメッセージ自体、コネクテッドコンテンツの呼び出し、またはキーと値のペアとして渡すことができる。これは通常、トラッキング、追跡の目的で行われる。

### REST API

キャンペーンとキャンバスの属性は、[キャンペーンの詳細のエクスポートエンドポイント]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details/)または[キャンバスの詳細のエクスポートエンドポイントでも]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/)利用できる。REST APIを使ってマッピングを作成することができる。

### Currents

キャンペーンとキャンバスの属性は、Currentsの[メッセージエンゲージメントイベントに]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events)関連付けられる。これは、プッシュ送信やメール開封が、どのキャンペーンやキャンバス・コンポーネントに関連付けられているかを判断するために重要である。

## キャンペーン属性

| 属性 | Liquid | REST API | Currents |
| --- | --- | --- | --- |
| キャンペーン名 | {% raw %}`{{campaign.${name}}}`{% endraw %} | `name` | `campaign_name` |
| キャンペーン ID | {% raw %}`{{campaign.${api_id}}}`{% endraw %} | 該当なし（APIコール自体の入力として使用される） | campaign_id |
| バリアント名 | {% raw %}`{{campaign.${message_name}}}`{% endraw %} | `messages.message_variation_id.name` | 該当なし (Export campaign details エンドポイントを使ってバリアント名をバリアント ID にマップする) |
| バリアントID | {% raw %}`{{campaign.${message_api_id}}}`{% endraw %} | `messages.message_variation_id` | `message_variation_api_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## キャンバス属性

| 属性 | Liquid | REST API | Currents |
| --- | --- | --- | --- |
| キャンバス名 | {% raw %}`{{canvas.${name}}}`{% endraw %} | `name` | `canvas_name` |
| キャンバスID | {% raw %}`{{canvas.${api_id}}}`{% endraw %} | 該当なし（APIコール自体の入力として使用される） | canvas_id |
| バリアント名 | {% raw %}`{{canvas.${variant_name}}}`{% endraw %} | `variants.name` | `canvas_variation_name` |
| バリアントID | {% raw %}`{{canvas.${variant_api_id}}}`{% endraw %} | `variants.name.id` | `canvas_variation_id` |
| ステップ名 | {% raw %}`{{campaign.${name}}}`{% endraw %} | `steps.name` | `canvas_step_name` |
| ステップID | {% raw %}`{{campaign.${api_id}}}`{% endraw %} | `steps.id` | `canvas_step_id` |
| メッセージチャネル | 該当なし | `steps.messages.message_variation_id.channel` | 該当なし（プッシュ送信やメール開封など、イベントの種類によって異なる） |
| メッセージID | {% raw %}`{{campaign.${message_api_id}}}`{% endraw %} | `steps.message.message_variation_id` | `canvas_step_message_variation_api_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}