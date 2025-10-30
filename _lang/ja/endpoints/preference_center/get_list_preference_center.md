---
nav_title: "取得:ユーザー設定センターのリスト"
article_title: "取得:ユーザー設定センターのリスト"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "この記事では、「ユーザー設定センターのリスト」Braze エンドポイントの詳細について説明します。"

---
{% api %}
# ユーザー設定センターのリスト
{% apimethod get %}
/preference_center/v1/list
{% endapimethod %}

> このエンドポイントを使用して、使用可能なユーザー設定センターを一覧表示します。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#dd8f6667-5eba-4e19-a29e-ba74644c0b8e {% endapiref %}

## 前提条件

このエンドポイントを使用するには、[API キー]({{site.baseurl}}/api/basics#rest-api-key/)と`preference_center.list`の権限が必要です。

## レート制限

このエンドポイントには、1 分あたり、ワークスペース あたり、レート制限 1,000 のリクエストがあります。

## パスとリクエストのパラメータ

このエンドポイントには、パスまたはリクエストパラメータはありません。

## 例のリクエスト

```
curl --location -g --request GET https://rest.iad-01.braze.com/preference_center/v1/list \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## 応答

```json
{
  "preference_centers": [
    {
      "name": "My Preference Center 1",
      "preference_center_api_id": "preference_center_api_id",
      "created_at": "2022-08-17T15:46:10Z",
      "updated_at": "2022-08-17T15:46:10Z"
    },
    {
      "name": "My Preference Center 2",
      "preference_center_api_id": "preference_center_api_id",
      "created_at": "2022-08-19T11:13:06Z",
      "updated_at": "2022-08-19T11:13:06Z"
    },
    {
      "name": "My Preference Center 3",
      "preference_center_api_id": "preference_center_api_id",
      "created_at": "2022-08-19T11:30:50Z",
      "updated_at": "2022-08-19T11:30:50Z"
    },
    {
      "name": "My Preference Center 4",
      "preference_center_api_id": "preference_center_api_id",
      "created_at": "2022-09-13T20:41:34Z",
      "updated_at": "2022-09-13T20:41:34Z"
    }
  ]
}
```

{% endapi %}
