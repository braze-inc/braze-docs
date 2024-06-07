---
nav_title: "ポスト:重複キャンペーン"
article_title: "ポスト:重複キャンペーン"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、重複キャンペーンエンドポイントの詳細について説明します。"

---
{% api %}
# API 経由でキャンペーンを複製
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/campaigns/duplicate
{% endapimethod %}

> このエンドポイントを使用してキャンペーンを複製します。このAPIエンドポイントは、[Brazeダッシュボードでキャンペーンを複製するのと似ています][1]。

{% alert note %}
このエンドポイントを使用するには、`campaigns.duplicate`権限のある API キーを生成する必要があります。
{% endalert %}

{% alert important %}
API によるキャンペーンの複製は、現在先行アクセス中です。早期アクセスへの参加に興味がある場合は、Braze アカウントマネージャーにお問い合わせください。
{% endalert %}

## レート制限

このエンドポイントは、1 分あたり 100 回の API 呼び出しに制限されています。

## リクエスト本文

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

| パラメーター | 必須 | データ型 | 説明 |
| --------- | ---------| --------- | ----------- |
| `campaign_id` | 必須 | 文字列 | [キャンペーン識別子を参照してください]({{site.baseurl}}/api/identifier_types/)。|
| `name` | 必須 | 文字列 | 結果のキャンペーンの名前。|
| `description` | オプション | 文字列 | 結果のキャンペーンの説明フィールド。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}


## 応答

`202`このエンドポイントはステータスコードを返し、キャンペーンの作成は非同期で行われます。[セキュリティイベントのダウンロードを使用して][2]、キャンペーンがいつどのAPIキーで複製されたかの記録を確認できます。



[1]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/duplicating_segments_and_campaigns#duplicating-segments-campaigns-and-canvases
[2]: {{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/?redirected=true#security-event-download

{% endapi %}
