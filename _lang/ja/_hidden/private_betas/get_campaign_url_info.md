---
nav_title: "取得:キャンペーン用リストリンクエイリアス"
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

description: "この記事では、List link alias Brazeエンドポイントの詳細について概説する。"
---
{% api %}
# キャンペーンのリンクエイリアスをリストアップする
{% apimethod get %}
/campaigns/url_info/details
{% endapimethod %}

> 特定のキャンペーンメッセージバリアントに設定されているリンクエイリアスを一覧表示するには、このエンドポイントを使用する。

{% apiref postman %}  {% endapiref %}

## リクエストパラメーター

| パラメーター | required | データ型 | 説明 |
|---|---|---|---|
| `campaign_id`  | 必須 | string | [キャンペーンAPI識別子を]({{site.baseurl}}/api/identifier_types/#campaign-api-identifier)参照のこと。|
| `message_variation_id `  |  必須 | string | メッセージバリアントAPI識別子。これはキャンペーンの詳細ページの**API Identifier**セクションで確認できる。 |
| `includes_link_id` | オプション | string | 特定のリンク識別子（Brazeによって割り当てられる）または`null` 。これは、特定の`link_id` によって結果をフィルタリングするために使用される。 |
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

以下の表は、返される可能性のあるエラーと、それに関連するトラブルシューティングの手順を示したものである。

| エラー | トラブルシューティング |
| --- | --- |
| `Missing/Invalid Campaign ID` | キャンペーンAPI IDはAPI識別子でなければならない。これは、[キャンペーンリストのエクスポートエンドポイントを]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns/)使用するか、ダッシュボードにログインすることで確認できる。 |
| `Missing/Invalid Message Variant ID` | メッセージバリアントAPI IDはAPI識別子でなければならない。これは、[キャンペーン詳細のエクスポートエンドポイントを]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details/)使用するか、ダッシュボードにログインすることで確認できる。 |
{: .reset-td-br-1 .reset-td-br-2}


{% endapi %}
