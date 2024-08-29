---
nav_title: "POST:重複キャンペーン"
article_title: "POST:重複キャンペーン"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、Duplicate campaigns（キャンペーンの重複）エンドポイントについての詳細を概説する。"

---
{% api %}
# API を介したキャンペーンの複製
{% apimethod post core_endpoint|{1} %}
/campaigns/duplicate
{% endapimethod %}

> キャンペーンを複製するには、このエンドポイントを使用する。このAPIエンドポイントは、[Brazeダッシュボードでキャンペーンを複製する][1]のと似ている。

{% alert important %}
API を介したキャンペーンの複製は、現在、早期アクセスの段階です。早期アクセスへの参加に興味がある方は、Brazeのアカウントマネージャーに連絡を。
{% endalert %}

## 前提条件

このエンドポイントを使用するには、`campaigns.duplicate` 権限を持つ API キーを生成する必要があります。

## レート制限

このエンドポイントは、1分間に100回のAPI呼び出しに制限されている。

## Request body

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "campaign_id": (required, string) The campaign identifier,
  "name": (required, string) The name of the resulting campaign,
  "description": (optional, string) The description of the resulting campaign,
}
```

## リクエストパラメーター

| パラメーター | required | データ型 | 説明 |
| --------- | ---------| --------- | ----------- |
|`campaign_id`| 必須 | string | [キャンペーン識別子]({{site.baseurl}}/api/identifier_types/)を参照してください。 |
|`name`| 必須 | string | 結果のキャンペーン名。 |
|`description`| オプション | string | 結果のキャンペーンの説明フィールド。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}


## 応答

このエンドポイントは `202` ステータスコードを返し、キャンペーン作成は非同期に行われます。[セキュリティイベントのダウンロード][2]を使えば、キャンペーンがいつ複製されたか、どの API キーによって複製されたかの記録を見ることができます。



[1]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/duplicating_segments_and_campaigns#duplicating-segments-campaigns-and-canvases
[2]: {{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/?redirected=true#security-event-download

{% endapi %}
