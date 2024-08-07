---
nav_title: "取得:ワークスペースアプリの一覧表示"
layout: api_page
page_type: reference
hidden: true
permalink: /get_app_group_apps/

platform: API
description: "List ワークスペース アプリ s Braze エンドポイントの概要について説明します。"
---
{% api %}
# 一覧ワークスペース アプリs
{% apimethod get %}
/アプリ_group/アプリs
{% endapimethod %}

> このエンドポイントを使用して、ワークスペース内のアプリs の名前と一意の識別子(`api_key`) を一覧表示します。 

このエンドポイントを押すと、`apps` というオブジェクト配列が返されます。`apps` の各オブジェクトには、アプリの名前と一意の識別子が含まれます。 

{% apiref postman %}  {% endapiref %}

## レートリミット

このエンドポイントには、1 日あたりレート制限100 件のリクエストがあります(24 時間)。

## 要求パラメータ

この要求はパラメータを取りません。

## リクエスト例

```
curl --location --request GET 'https://rest.iad-01.braze.com/app_group/apps' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## レスポンス

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

次のテーブルに、返されるエラーと関連するトラブルシューティングステップを示します。

| エラー | トラブルシューティング |
| --- | --- |
| `401: Unauthorized` | API キーに必要な権限がありません。API キーに`apps.get` 権限があることを確認します。 |
| `403: Forbidden` | この会社の機能フリッパーはオンになっていません。顧客のサクセスマネージャーにお問い合わせください。 |
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}
