---
nav_title: "取得:環境設定センターURL の生成"
article_title: "取得:環境設定センターURL の生成"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "この記事では、Generate preference center URL Braze エンドポイントの詳細について説明します。"

---
{% api %}
# 環境設定センターURL の生成
{% apimethod get %}
/preference_center/v1/{preferenceCenterExternalID}/url/{userID}
{% endapimethod %}

> このエンドポイントを使用して、プリファレンスセンターのURL を生成します。 

各プリファレンスセンターのURL は、ユーザーごとに一意です。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#0bc750ff-068e-4391-897e-6eddca2561cd {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`preference_center.user.get` 権限を持つ[API キー]({{site.baseurl}}/api/basics#rest-api-key/) が必要です。

## レート制限

このエンドポイントには、ワークスペースあたり1 分あたり1000 件のリクエストのレート制限があります。

## パスパラメータ

| パラメータ| 必須| データ型| 説明|
| --------- | ---------| --------- | ----------- |
|`preferenceCenterExternalID`| 必須| 文字列| お好みのセンターのID。|
|`userID`| 必須| 文字列| ユーザID。|

## 要求パラメータ

| パラメータ| 必須| データ型| 説明|
| --------- | ---------| --------- | ----------- |
|`preference_center_api_id`| 必須| 文字列| お好みのセンターのID。|
|`external_id`| 必須| 文字列| ユーザの外部ID。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## リクエスト例

```
curl --location --request GET 'https://rest.iad-01.braze.com/preference_center/v1/$preference_center_external_id/url/$user_external_id' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## レスポンス 

```json
{
  "preference_center_url": "https://www.example.com/preferences"
}
```

{% endapi %}

{% alert note %}
このエンドポイントは、新しいプリファレンスセンター(API またはドラッグアンドドロップエディタを使用して作成されたプリファレンスセンターなど) のURL のみを生成します。
{% endalert %}