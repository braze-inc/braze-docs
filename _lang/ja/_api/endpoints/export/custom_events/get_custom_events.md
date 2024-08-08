---
nav_title: "取得:カスタムイベントリストのエクスポート"
article_title: "取得:カスタムイベントリストのエクスポート"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、カスタムイベントのエクスポートリストBraze エンドポイントの詳細について説明します。"

---
{% api %}
# カスタムイベントリストのエクスポート
{% apimethod get %}
/events/list
{% endapimethod %}

> このエンドポイントを使用して、アプリ用に記録されたカスタムイベントのリストをエクスポートします。イベント名は、アルファベット順にソートされた250 のグループで返されます。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#93ecd8a5-305d-4b72-ae33-2d74983255c1 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`events.list` 権限を持つ[API キー]({{site.baseurl}}/api/basics#rest-api-key/) が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='events list' %}

## 要求パラメータ

| パラメータ| 必須| データ型| 説明|
| -------- | -------- | --------- | ----------- |
| `page` | オプション| 整数| 返されるイベント名のページ。デフォルトは0 です(250 までの最初のセットを返します)。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## リクエスト例
```
curl --location --request GET 'https://rest.iad-01.braze.com/events/list?page=3' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## レスポンス

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "events" : [
        "Event A", (string) the event name,
        "Event B", (string) the event name,
        "Event C", (string) the event name,
        ...
    ]
}
```

### 致命的なエラー応答コード {#fatal-export}

リクエストで致命的なエラーが発生した場合に返されるステータスコードと関連するエラーメッセージについては、[Fatal errors & responses]({{site.baseurl}}/api/errors/#fatal-errors) を参照してください。

{% alert tip %}
CSV およびAPI エクスポートのヘルプについては、[トラブルシューティング]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/) をエクスポートしてください。
{% endalert %}

{% endapi %}
