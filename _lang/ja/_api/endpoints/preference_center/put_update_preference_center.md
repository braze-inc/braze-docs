---
nav_title: "設置:ユーザー設定センターを更新しますか?"
article_title: "設置:ユーザー設定センターを更新しますか?"
search_tag: Endpoint
page_order: 5
layout: api_page
page_type: reference
description: "この記事では、プリファレンスセンターの Braze エンドポイントの更新について詳しく説明します。"

---
{% api %}
# ユーザー設定センターを更新しますか?
{% apimethod put %}
/preference_center/v1/{preferenceCenterExternalID}
{% endapimethod %}

> このエンドポイントを使用してプリファレンスセンターを更新します。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#bf1b43db-3f1b-461f-ad9a-2fbe35b804d7 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`preference_center.update`権限のある [API キーが必要です]({{site.baseurl}}/api/basics#rest-api-key/)。

## レート制限

このエンドポイントのレート制限は、ワークスペースごとに 1 分あたり 10 リクエストです。

## パスパラメーター

| パラメーター | 必須 | データ型 | 説明 |
| --------- | ---------| --------- | ----------- |
| `preferenceCenterExternalID` | 必須 | 文字列 | プリファレンスセンターのID。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}


## リクエスト本文

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```
{
  "name": "preference_center_name",
  "preference_center_title": "string",
  "preference_center_page_html": "string",
  "confirmation_page_html": "string",
  "options": {
    "meta-viewport-content": "string", (optional) Only the `content` value of the meta tag
  }
}
```

## リクエストパラメーター

| パラメーター | 必須 | データ型 | 説明 |
| --------- | ---------| --------- | ----------- |
| `preference_center_page_html` | 必須 | 文字列 | プリファレンスセンターページのHTML。|
| `preference_center_title` | オプション | 文字列 | プリファレンスセンターと確認ページのタイトル。タイトルが指定されていない場合、ページのタイトルはデフォルトで「プリファレンスセンター」になります。|
| `confirmation_page_html` | 必須 | 文字列 | 確認ページのHTML。|
| `state` | オプション | 文字列 | `active` `draft` または.| を選択
| `options` | オプション | オブジェクト | 属性:`meta-viewport-content`.存在する場合、`viewport``content= <value of attribute>`メタタグがでページに追加されます。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## リクエスト例

{% raw %}
```
curl --location --request POST 'https://rest.iad-01.braze.com/preference_center/v1/{preferenceCenterExternalId}' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "name": "Example",
  "preference_center_title": "Example Preference Center Title",
  "preference_center_page_html": "HTML for preference center here",
  "confirmation_page_html": "HTML here with a message to users here",
  "state": "active"
}
'
```
{% endraw %}

## レスポンス例
{% raw %}
```
{
  "preference_center_api_id": "8efc52aa-935e-42b7-bd6b-98f43bb9b0f1",
  "created_at": "2022-09-22T18:28:07Z",
  "updated_at": "2022-09-22T18:32:07Z",
  "message": "success"
}
```
{% endraw %}

{% endapi %}
