---
nav_title: "取得：ワークスペース アプリの一覧表示"
layout: api_page
page_type: reference
hidden: true
permalink: /get_app_group_apps/

platform: API
description: "この記事では、ワークスペースアプリの一覧表示Brazeエンドポイントについて詳しく説明します。"
---
{% api %}
# ワークスペース アプリを一覧表示する
{% apimethod get %}
/app_group/apps
{% endapimethod %}

> このエンドポイントを使用して、ワークスペース内のアプリの名前と一意の識別子 ()`api_key` を一覧表示します。 

このエンドポイントをヒットすると、 という `apps`オブジェクト配列が返されます。の各 `apps` オブジェクトには、アプリの名前と一意の識別子が含まれています。 

{% apiref postman %}

## レート制限

このエンドポイントには、1 日あたり 100 リクエスト (24 時間) のレート制限があります。

## 要求パラメーター

この要求はパラメーターを受け取りません。

## 要求の例

```
curl --location --request GET 'https://rest.iad-01.braze.com/app_group/apps' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## 応答

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "apps": [
        {
          "name": "App Name",
          "api_key": 00000000-0000-0000-0000-000000000000
        }
    ],
    "message": "success"
}
```

### トラブルシューティング

次の表に、返される可能性のあるエラーと、それに関連するトラブルシューティング手順を示します。

|エラー |トラブルシューティング |
| --- | --- |
| `401: Unauthorized` |APIキーに必要な権限がありません。APIキーに権限がある `apps.get` ことを確認してください。 |
| `403: Forbidden` |この会社では機能フリッパーがオンになっていません。カスタマーサクセスマネージャーにお問い合わせください。|
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}
