---
nav_title: "取得:ユーザー設定センターの URL の生成"
article_title: "取得:ユーザー設定センターの URL の生成"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "この記事では、「ユーザー設定センターの URL の生成」Braze エンドポイントの詳細について説明します。"

---
{% api %}
# ユーザー設定センターの URL の生成
{% apimethod get %}
/preference_center/v1/{preferenceCenterExternalID}/url/{userID}
{% endapimethod %}

> このエンドポイントを使用して、ユーザー設定センターの URL を生成します。 

ユーザー設定センター URL はユーザーごとに一意です。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#0bc750ff-068e-4391-897e-6eddca2561cd {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`preference_center.user.get` 権限を持つ[API キー]({{site.baseurl}}/api/basics#rest-api-key/) が必要です。

## レート制限

このエンドポイントには、1分あたり、ワークスペースあたり、1,000件のリクエストというレート制限があります。

## パスパラメータ

| パラメータ | required | データ型 | 説明 |
| --------- | ---------| --------- | ----------- |
|`preferenceCenterExternalID`| 必須 | string | ユーザー設定センターの ID。 |
|`userID`| 必須 | string | ユーザー ID。 |

## リクエストパラメーター

| パラメータ | required | データ型 | 説明 |
| --------- | ---------| --------- | ----------- |
|`preference_center_api_id`| 必須 | string | ユーザー設定センターの ID。 |
|`external_id`| 必須 | string | ユーザーの外部ID。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## リクエスト例

```
curl --location --request GET 'https://rest.iad-01.braze.com/preference_center/v1/$preference_center_external_id/url/$user_external_id' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## 応答 

```json
{
  "preference_center_url": "https://www.example.com/preferences"
}
```

{% endapi %}

{% alert note %}
このエンドポイントは、新しいユーザー設定センター (API またはドラッグアンドドロップエディタを使用して作成されたユーザー設定センターなど) のURL のみを生成します。
{% endalert %}