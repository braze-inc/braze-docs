---
nav_title: "ポストだ：キャンバスの複製"
layout: api_page
page_type: reference
hidden: true
permalink: /api/endpoints/messaging/duplicate_canvases/
description: "この記事では、キャンバスの複製エンドポイントについての詳細を概説する。"
---

{% api %}
# API経由でキャンバスを複製する
APIMETHOD POST CORE_ENDPOINT| {% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/キャンバス/複製
{% endapimethod %}

> キャンバスを複製するには、このエンドポイントを使用する。このAPIエンドポイントは、[BrazeダッシュボードでCanvasesを複製する][1]のと似ている。

{% alert important %}
API経由でのキャンバスの複製は、現在早期アクセス中である。早期アクセスへの参加に興味がある方は、Brazeのアカウントマネージャーに連絡を。
{% endalert %}

## 前提条件

このエンドポイントを使用するには、`canvas.duplicate` パーミッションを持つAPIキーを生成する必要がある。

## レート制限

このエンドポイントは、1分間に100回のAPI呼び出しに制限されている。

## Request body

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "canvas_id": (required, string) The Canvas identifier,
  "name": (required, string) The name of the resulting Canvas,
  "description": (optional, string) The description of the resulting Canvas,
  "tag_names": (optional, string) The tags of the resulting Canvas,
}
```

## リクエストパラメーター

| パラメーター | required | データ型 | 説明 |
| --------- | ---------| --------- | ----------- |
|`canvas_id`| 必須 | string | [キャンバスの識別子を]({{site.baseurl}}/api/identifier_types/)参照のこと。 |
|`name`| 必須 | string | 結果のキャンバスの名前。 |
|`description`| オプション | string | 結果のキャンバスの説明フィールド。 |
|`tag_names` | オプション | string | 出来上がったキャンバスのタグ。これらは既存のタグでなければならない。リクエストに新しいタグを追加すると、オリジナルのキャンバスにあったタグは上書きされる。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## 応答

このエンドポイントは`202` ステータスコードを返し、Canvasの作成は非同期に行われる。[Securityイベントダウンロードを使って][2]、Canvasがいつ複製されたか、どのAPIキーによって複製されたかの記録を見ることができる。

[1]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/duplicating_segments_and_campaigns#duplicating-segments-campaigns-and-canvases
[2]: {{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/?redirected=true#security-event-download

{% endapi %}
