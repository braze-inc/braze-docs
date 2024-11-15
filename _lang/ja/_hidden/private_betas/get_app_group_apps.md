---
nav_title: "取得:ワークスペースアプリのリスト"
layout: api_page
page_type: reference
hidden: true
permalink: /get_app_group_apps/

platform: API
description: "この記事では、リストワークスペースアプリBrazeエンドポイントの詳細について説明します。"
---
{% api %}
# ワークスペースアプリをリスト
{% apimethod get %}
/app_group/apps
{% endapimethod %}

> このエンドポイントを使用して、ワークスペース内のアプリの名前と一意の識別子（`api_key`）を一覧表示します。 

このエンドポイントにアクセスすると、`apps`というオブジェクト配列が返されます。`apps`の各オブジェクトには、アプリの名前と一意の識別子が含まれています。 

{% apiref postman %} {% endapiref %}

## レート制限

このエンドポイントには、1日（24時間）あたり100リクエストのレート制限があります。

## リクエストパラメーター

このリクエストはパラメータを取りません。

## 例のリクエスト

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

次のテーブルに、返される可能性のあるエラーと、関連するトラブルシューティングステップを示します。

| エラー | トラブルシューティング |
| --- | --- |
| `401: Unauthorized` | API キーには必要な権限がありません。API キーに`apps.get`の権限があることを確認してください。 |
| `403: Forbidden` | この会社では機能フリッパーがオンになっていません。サポートが必要な場合は、カスタマーサクセスマネージャーに連絡してください。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
