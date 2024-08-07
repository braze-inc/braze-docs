---
nav_title: "取得:キャンバスのリンクエイリアスの一覧表示"
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

description: "ここでは、キャンバスエンドポイントのリストリンクエイリアスについて説明します。"
---
{% api %}
# キャンバスのリンクエイリアスを一覧表示する
{% apimethod get %}
/canvas/url_info/details
{% endapimethod %}

> このエンドポイントを使用して、特定のメールキャンバスステップで設定されたリンクエイリアスを一覧表示します。

{% apiref postman %}  {% endapiref %}

## 要求パラメータ

| パラメータ | required | データ型 | 説明 |
|---|---|---|---|
| `canvas_step_id` | 必須 | string | [キャンバスステップ API 識別子]({{site.baseurl}}/api/identifier_types/#canvas-api-identifier)を参照してください。 |
| `message_variation_id ` | 必須 | string | Message バリアント API 識別子(メッセージバリアントをメールするステップ)。これは、**Canvas Details** ページで**Analyze Variants** をクリックすることで確認できます。 |
| `includes_link_id` | オプション | string | 具体的なリンク識別子(Brazeによって割り当てられる) または`null`。これは、指定した`link_id` によって結果をフィルターするために使用されます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 }

## リクエスト例

```
curl --location --request GET 'https://rest.iad-01.braze.com/canvas/url_info/details?campaign_id=4615a404-b2c2-421e-9a04-2233bb3ec4f9&message_variation_id=0ea708fe-36b4-43f7-9f5c-a0650ea2a7a0&includes_link_id=014tk4e0kg97' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## レスポンス

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

次のテーブルに、返されるエラーと関連するトラブルシューティングステップを示します。

| エラー | トラブルシューティング |
| --- | --- |
| `Missing/Invalid Canvas ID` | キャンバスAPI ID はAPI 識別子である必要があります。これは、[エクスポートキャンバスリストエンドポイント]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases/)を使用するか、ダッシュボードにログインして確認できます。 |
| `Missing/Invalid Message Variant ID` | メッセージバリアント API ID はAPI 識別子である必要があります。これは、[キャンバス詳細のエクスポートエンドポイント]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/)を使用するか、ダッシュボードにログインして確認できます。 |
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}
