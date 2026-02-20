---
nav_title: "取得:ユーザー設定センターの詳細を表示する"
article_title: "取得:環境設定センターの詳細の表示"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
description: "この記事では、「ユーザー設定センターの詳細を表示」Braze エンドポイントの詳細について説明します。"

---
{% api %}
# ユーザー設定センターの詳細を表示する
{% apimethod get %}
/preference_center/v1/{preferenceCenterExternalID}
{% endapimethod %}

> このエンドポイントを使用して、ユーザー設定センターの詳細 (作成日時や更新日時など) を表示します。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#6a47fd7c-2997-4832-aedb-d101a2dd03a5 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、[API キー]({{site.baseurl}}/api/basics#rest-api-key/)と`preference_center.get`の権限が必要です。

## レート制限

このエンドポイントには、1 分あたり、ワークスペース あたり、レート制限 1,000 のリクエストがあります。

## パスパラメーター

| パラメータ | required | データ型 | 説明 |
| --------- | ---------| --------- | ----------- |
|`preferenceCenterExternalID`| 必須 | 文字列 | ユーザー設定センターの ID。 |
{: role="presentation" }

## リクエストパラメーター

このエンドポイントのリクエストパラメータはありません。

## 例のリクエスト

```
curl --location -g --request GET https://rest.iad-01.braze.com/preference_center/v1/preference_center_external_id \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## 応答
```json
{
  "name": "My Preference Center",
  "preference_center_api_id": "preference_center_api_id",
  "created_at": "example_time_created",
  "updated_at": "example_time_updated",
  "preference_center_title": "Example preference center title",
  "preference_center_page_html": "HTML for preference center here",
  "confirmation_page_html": "HTML for confirmation page here",
  "redirect_page_html": null,
  "preference_center_options": {
    "meta-viewport-content": "width=device-width, initial-scale=2"
  },
  "state": "active"
}
```

{% endapi %}
