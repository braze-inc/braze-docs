---
nav_title: "取得:キャンペーンのリンクエイリアスを一覧表示"
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

description: "この記事では、リストリンクエイリアスBrazeエンドポイントの詳細について説明します。"
---

# キャンペーンのリンクエイリアスを一覧表示

/campaigns/url_info/details


> このエンドポイントを使用して、特定のキャンペーンメッセージバリアントに設定されたリンクエイリアスを一覧表示します。

{% apiref postman %} {% endapiref %}

## リクエストパラメータ

| パラメータ | required | データ型 | 説明 |
|---|---|---|---|
|   | 必須 | string | [キャンペーン API 識別子]({{site.baseurl}}/api/identifier_types/#campaign-api-identifier)|
|   |  必須 | string | メッセージバリアントAPI識別子。キャンペーンの詳細ページの**API識別子**セクションで見つけることができます。 |
|  | オプショナル | string | Braze によって割り当てられた特定のリンク識別子または `null`。これは特定の`link_id`で結果をフィルターするために使用されます。 |


## 例のリクエスト
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

次の表は、考えられるエラーとそれに関連するトラブルシューティング手順を示しています。

| エラー | トラブルシューティング |
| --- | --- |
|  | キャンペーンAPI IDはAPI識別子でなければなりません。エクスポートキャンペーンリストエンドポイント[}を使用するか、ダッシュボードにログインすることでこれを見つけることができます。]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns/) |
|  | メッセージバリアントAPI IDはAPI識別子でなければなりません。エクスポートキャンペーン詳細エンドポイントを使用するか、ダッシュボードにログインすることでこれを見つけることができます。 |




