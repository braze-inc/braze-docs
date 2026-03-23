---
nav_title: "POST:キャンバスの複製"
article_title: "POST:キャンバスの複製"
search_tag: エンドポイント
page_order: 5
layout: api_page
page_type: reference
description: "この記事では、「キャンバスの複製」エンドポイントの詳細について説明します。"
---

{% api %}
# API を使用したキャンバスの複製
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/canvas/duplicate
{% endapimethod %}

> このエンドポイントを使用して、キャンバスを複製します。この API エンドポイントは、[Braze ダッシュボードでのキャンバスの複製][1]に似ています。

## 前提条件

このエンドポイントを使用するには、`canvas.duplicate` 権限を持つ API キーを生成する必要があります。

## レート制限

このエンドポイントは、1分あたり100回の API コールに制限されます。

## リクエスト本文

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

| パラメーター | 必須 | データタイプ | 説明 |
| --------- | ---------| --------- | ----------- |
|`canvas_id`| 必須 | 文字列 | [キャンバス識別子](https://www.braze.com/docs/api/identifier_types/)を参照してください。 |
|`name`| 必須 | 文字列 | 作成されるキャンバスの名前。 |
|`description`| オプション | 文字列 | 作成されるキャンバスの説明フィールド。 |
|`tag_names` | オプション | 文字列 | 作成されるキャンバスのタグ。これらは既存のタグである必要があります。リクエストに新しいタグを追加すると、元のキャンバスにあったすべてのタグが上書きされます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 応答

このエンドポイントは `202` ステータスコードを返し、キャンバスの作成は非同期で行われます。[セキュリティイベントのダウンロード][2]を使用すると、キャンバスがいつ複製され、どの API キーによって行われたかの記録を確認できます。

[1]: {{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/duplicating
[2]: {{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings

{% endapi %}