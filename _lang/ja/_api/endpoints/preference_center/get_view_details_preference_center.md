---
nav_title: "取得:環境設定センターの詳細の表示"
article_title: "取得:環境設定センターの詳細の表示"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
description: "この記事では、プリファレンスセンターのBrazeエンドポイントのビューの詳細について説明します。"

---
{% api %}
# 環境設定センターの詳細を表示する
{% apimethod get %}
/preference_center/v1/{preferenceCenterExternalID}
{% endapimethod %}

> このエンドポイントを使用して、いつ作成および更新されたかを含め、プリファレンスセンターの詳細を表示します。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#6a47fd7c-2997-4832-aedb-d101a2dd03a5 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`preference_center.get` 権限を持つ[API キー]({{site.baseurl}}/api/basics#rest-api-key/) が必要です。

## レート制限

このエンドポイントには、ワークスペースあたり1 分あたり1000 件のリクエストのレート制限があります。

## パスパラメータ

| パラメータ| 必須| データ型| 説明|
| --------- | ---------| --------- | ----------- |
|`preferenceCenterExternalID`| 必須| 文字列| お好みのセンターのID。|

## 要求パラメータ

このエンドポイントにはリクエストパラメータはありません。

## リクエスト例

```
curl --location -g --request GET https://rest.iad-01.braze.com/preference_center/v1/preference_center_external_id \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## レスポンス 
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
