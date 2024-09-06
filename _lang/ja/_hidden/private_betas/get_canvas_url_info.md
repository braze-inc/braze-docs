---
nav_title: "取得:キャンバスのリンク・エイリアスをリストする"
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

description: "この記事では、CanvasエンドポイントのListリンクエイリアスについての詳細を概説する。"
---
{% api %}
# キャンバスのリンクエイリアスをリストする
{% apimethod get %}
/canvas/url_info/details
{% endapimethod %}

> このエンドポイントを使用して、特定の電子メール・キャンバスのステップで設定されたリンク・エイリアスをリストする。

{% apiref postman %}  {% endapiref %}

## リクエストパラメーター

| パラメーター | required | データ型 | 説明 |
|---|---|---|---|
| `canvas_step_id` | 必須 | string | [キャンバスステップAPI識別子を]({{site.baseurl}}/api/identifier_types/#canvas-api-identifier)参照のこと。 |
| `message_variation_id ` | 必須 | string | メッセージバリアントAPI識別子（そのステップのEメールメッセージバリアント用）。これは、**キャンバスの詳細**ページで**バリアントの分析を**クリックすることで見つけることができる。 |
| `includes_link_id` | オプション | string | 特定のリンク識別子（Brazeによって割り当てられる）または`null` 。これは、特定の`link_id` によって結果をフィルタリングするために使用される。 |
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

以下の表は、返される可能性のあるエラーと、それに関連するトラブルシューティングの手順を示したものである。

| エラー | トラブルシューティング |
| --- | --- |
| `Missing/Invalid Canvas ID` | キャンバスAPI IDはAPI識別子でなければならない。これは、[キャンバス・リストのエクスポート・エンドポイントを]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases/)使うか、ダッシュボードにログインすることで確認できる。 |
| `Missing/Invalid Message Variant ID` | メッセージバリアントAPI IDはAPI識別子でなければならない。これは、[キャンバスの詳細をエクスポートするエンドポイントを]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/)使用するか、ダッシュボードにログインすることで確認できる。 |
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}
