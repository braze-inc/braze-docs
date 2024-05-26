---
nav_title: "得る：キャンバスのリンクエイリアスを一覧表示する"
layout: api_page
page_type: reference
hidden: true
permalink: /get_canvas_link_alias/

platform: API
channel:
  - Email
tool:
  - Canvas
  - Campaigns

description: "この記事では、Canvas エンドポイントのリスト リンク エイリアスについて詳しく説明します。"
---
{% api %}
# Canvas のリストリンクエイリアス
{% apimethod get %}
/canvas/url_info/details
{% endapimethod %}

> このエンドポイントを使用して、特定の電子メール Canvas ステップで設定されたリンク エイリアスを一覧表示します。

{% apiref postman %}

## リクエストパラメータ

| パラメータ | 必須 | データ型 | 説明 |
|---|---|---|---|
| `canvas_step_id`| 必須 | 文字列 |[Canvas ステップ API 識別子を]({{site.baseurl}}/api/identifier_types/#canvas-api-identifier)参照してください。 |
| `message_variation_id `| 必須 | 文字列 | メッセージ バリアント API 識別子 (そのステップの電子メール メッセージ バリアント用)。これは、 **キャンバスの詳細** ページで **[バリアントを分析] を** クリックすると見つかります。 |
| `includes_link_id`| オプション | 文字列 | 特定のリンク識別子（Brazeによって割り当てられる）または `null`。これは特定の条件で結果をフィルタリングするために使用されます `link_id`。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 }

## リクエスト例

```
curl --location --request GET 'https://rest.iad-01.braze.com/canvas/url_info/details?campaign_id=4615a404-b2c2-421e-9a04-2233bb3ec4f9&message_variation_id=0ea708fe-36b4-43f7-9f5c-a0650ea2a7a0&includes_link_id=014tk4e0kg97' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## 応答

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "channel": "email",
  "name": "Variant 1",
  "link_data": [
    {
      "link_URL": "https://www.braze.com?lid=014tk4e0kg97",
      "link_id": "014tk4e0kg97",
      "content_block_path_info": [],
      "link_alias": "link5"
    }
  ],
  "message": "success"
}
```

### トラブルシューティング

次の表に、返される可能性のあるエラーとそれに関連するトラブルシューティング手順を示します。

| エラー | トラブルシューティング |
| --- | --- |
| `Missing/Invalid Canvas ID`| Canvas API ID は API 識別子である必要があります。これは、 [エクスポート キャンバス リスト エンドポイント]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases/) を使用するか、ダッシュボードにログインすることで見つけることができます。 |
| `Missing/Invalid Message Variant ID`| メッセージバリアント API ID は API 識別子である必要があります。これは、 [キャンバスの詳細をエクスポートするエンドポイント]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/) を使用するか、ダッシュボードにログインすることで確認できます。 |
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}
