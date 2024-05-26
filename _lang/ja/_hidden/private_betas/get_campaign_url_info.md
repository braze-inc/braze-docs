---
nav_title: "GET：キャンペーン用リストリンクエイリアス"
layout: api_page
page_type: reference
hidden: true
permalink: /get_campaign_link_alias/

platform: API
channel:
  - Email
tool:
  - Canvas
  - Campaigns

description: "この記事では、List link alias Brazeエンドポイントの詳細について概説します。"
---
{% api %}
# キャンペーンのリンクエイリアスを一覧表示
{% apimethod get %}
/campaigns/url_info/details
{% endapimethod %}

> このエンドポイントを使用して、特定のキャンペーンメッセージバリアントに設定されているリンクエイリアスを一覧表示します。

{% apiref postman %}

## リクエストパラメータ

| パラメータ｜必須｜データ型｜説明
|---|---|---|---|
|`campaign_id` ｜必須｜文字列｜[キャンペーンAPI識別子を]({{site.baseurl}}/api/identifier_types/#campaign-api-identifier)参照してください。
|`message_variation_id ` | Required | String | Message variant API identifier.これはキャンペーンの詳細ページの**API Identifier**セクションで確認できます。|
|`includes_link_id` ｜任意｜文字列｜特定のリンク識別子（Brazeによって割り当てられる）または`null` 。これは、特定の`link_id` によって結果をフィルタリングするために使用されます。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## リクエスト例
```
curl --location --request GET 'https://rest.iad-01.braze.com/campaigns/url_info/details?campaign_id=4615a404-b2c2-421e-9a04-2233bb3ec4f9&message_variation_id=0ea708fe-36b4-43f7-9f5c-a0650ea2a7a0&includes_link_id=014tk4e0kg97' \
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

次の表は、返される可能性のあるエラーと、それに関連するトラブルシューティングの手順を示したものです。

| トラブルシューティング
| --- | --- |
`Missing/Invalid Campaign ID` | キャンペーンAPI IDはAPI識別子でなければなりません。[キャンペーンリストのエクスポートエンドポイントを]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns/)使用するか、ダッシュボードにログインすることで確認できます。|
|`Missing/Invalid Message Variant ID` | メッセージバリアントのAPI IDはAPI識別子でなければならない。[キャンペーン詳細のエクスポートエンドポイントを]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details/)使用するか、ダッシュボードにログインすることで確認できます。|
{: .reset-td-br-1 .reset-td-br-2}


{% endapi %}
