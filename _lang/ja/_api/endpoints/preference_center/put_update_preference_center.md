---
nav_title: "PUT:ユーザー設定センターを更新"
article_title: "PUT:ユーザー設定センターを更新"
search_tag: Endpoint
page_order: 5
layout: api_page
page_type: reference
description: "この記事では、「ユーザー設定センターの更新」Braze エンドポイントの詳細について説明します。"

---
{% api %}
# ユーザー設定センターを更新
{% apimethod put %}
/preference_center/v1/{preferenceCenterExternalID}
{% endapimethod %}

> このエンドポイントを使用して、ユーザー設定センターを更新します。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#bf1b43db-3f1b-461f-ad9a-2fbe35b804d7 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、[API キー]({{site.baseurl}}/api/basics#rest-api-key/)と`preference_center.update`の権限が必要です。

## レート制限

このエンドポイントには、1分あたり、ワークスペースあたり、10件のリクエストというレート制限があります。

## パスパラメータ

| パラメータ | required | データ型 | 説明 |
| --------- | ---------| --------- | ----------- |
|`preferenceCenterExternalID`| 必須 | string | ユーザー設定センターの ID。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}


## Request body

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

| パラメータ | required | データ型 | 説明 |
| --------- | ---------| --------- | ----------- |
|`preference_center_page_html`| 必須 | string | ユーザー設定センターページのHTML。 |
|`preference_center_title`| オプション | string | ユーザー設定センターと確認ページのタイトル。タイトルが指定されていない場合、ページのタイトルはデフォルトで「ユーザー設定センター」になります。 |
|`confirmation_page_html`| 必須 | string | 確認ページのHTML。 |
|`state` | オプション | string | `active` または `draft` を選択してください。|
|`options` | オプション | オブジェクト | 属性: `meta-viewport-content`.存在する場合、`viewport`メタタグが`content= <value of attribute>`と共にページに追加されます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## 例のリクエスト

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

## 応答の例
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
