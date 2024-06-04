---
nav_title: キャンペーンとキャンバスの属性がソース間でどのように異なるか
article_title: キャンペーンとキャンバスの属性がブレーズのソース間でどのように異なるか 
page_order: 1

page_type: reference
description: "このヘルプ記事では、Braze のソース間でキャンペーン属性名とキャンバス属性名およびID を比較します。"
platform: API
---

# キャンペーンとキャンバスの属性がブレーズのソース間でどのように異なるか

キャンペーン、キャンバス、およびキャンバスのステップ名とID はすべて、Liquid、REST API、およびCurrents で使用できます。これらの属性は、3 つのソースすべてで同じ値にマップされますが、名前は異なる場合があります。このページは、3 つの間の接続を描くのに役立ちます。

## 使用例

### 液体

キャンペーンおよびキャンバス属性は、ダッシュボード{% raw %} (`{{campaign.${api_id}}}` など){% endraw %} でLiquid タグとして使用できます。Liquid を使用して、メッセージ自体、Connected Content 呼び出し、またはキーと値のペアでこれらの属性を渡すことができます。これは通常、トラッキングの目的で行われます。

### REST API

キャンペーンおよびキャンバス属性は、[エクスポートキャンペーン詳細エンドポイント]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details/) または[エクスポートキャンバス詳細エンドポイント]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/) でも使用できます。REST API を使用してマッピングを構築できます。つまり、すべてのキャンバス名と対応するID のリストです。

### Currents

Campaign およびCanvas 属性は、Currents からの[メッセージエンゲージメントイベント]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events) に関連付けられます。これは、プッシュ送信またはメールオープンが関連付けられているキャンペーンまたはキャンバスコンポーネントを判断するために重要です。

## キャンペーン属性

| 属性| 液体| REST API | 現在|
| --- | --- | --- | --- |
| キャンペーン名|{% raw %}`{{campaign.${name}}}`{% endraw %}|`name`|`campaign_name`|
| キャンペーンID | {% raw %}`{{campaign.${api_id}}}`{% endraw %} | N/A (API 呼び出し自体の入力として使用) | campaign_id |
| Variant name | {% raw %}`{{campaign.${message_name}}}`{% endraw %} | `messages.message_variation_id.name` | N/A (エクスポートキャンペーン詳細エンドポイントを使用したバリアントIDへのバリアント名のマップ) |
| バリアントID | {% raw %}`{{campaign.${message_api_id}}}`{% endraw %} | `messages.message_variation_id` | `message_variation_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## キャンバス属性

| 属性| 液体| REST API | 現在|
| --- | --- | --- | --- |
| キャンバス名|{% raw %}`{{canvas.${name}}}`{% endraw %}|`name`|`canvas_name`|
| キャンバスID | {% raw %}`{{canvas.${api_id}}}`{% endraw %} | N/A (API 呼び出し自体の入力として使用) | canvas_id |
| バリアント名|{% raw %}`{{canvas.${variant_name}}}`{% endraw %}|`variants.name`|`canvas_variation_name`|
| バリアントID | {% raw %}`{{canvas.${variant_api_id}}}`{% endraw %} | `variants.name.id` | `canvas_variation_id` |
| ステップ名  | {% raw %}`{{campaign.${name}}}`{% endraw %} | `steps.name` | `canvas_step_name` |
| ステップID | {% raw %}`{{campaign.${api_id}}}`{% endraw %} | `steps.id` | `canvas_step_id` |
| メッセージチャネル| N/A | `steps.messages.message_variation_id.channel` | N/A (プッシュ送信やメールオープンなどのイベントタイプに固有)|
| メッセージID | {% raw %}`{{campaign.${message_api_id}}}`{% endraw %} | `steps.message.message_variation_id` | `message_variation_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}