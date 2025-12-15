---
nav_title: "取得:カスタム・イベントのリストをエクスポートする"
article_title: "取得:カスタムイベントリストのエクスポート"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、カスタムイベントリストBrazeエンドポイントのエクスポートに関する詳細を概説する。"

---
{% api %}
# カスタム・イベントのリストをエクスポートする
{% apimethod get %}
/events/list
{% endapimethod %}

> アプリに記録されたカスタム・イベントのリストをエクスポートするには、このエンドポイントを使用する。イベント名はアルファベット順に並べられ、250のグループで返される。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#93ecd8a5-305d-4b72-ae33-2d74983255c1 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、[API キー]({{site.baseurl}}/api/basics#rest-api-key/)と`events.list`の権限が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='events list' %}

## リクエストパラメーター

| パラメーター| required | データ型 | 説明 |
| -------- | -------- | --------- | ----------- |
| `page` | オプション | 整数 | 返されるイベント名のページ。デフォルトは0です (最大250の最初のセットを返す)。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 例のリクエスト
```
curl --location --request GET 'https://rest.iad-01.braze.com/events/list?page=3' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## 応答

```json
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

### 致命的なエラーの応答コード {#fatal-export}

リクエストが致命的なエラーに遭遇した場合に返されるステータスコードと関連するエラーメッセージについては、[致命的なエラー& レスポンスを]({{site.baseurl}}/api/errors/#fatal-errors)参照のこと。

{% alert tip %}
CSV および API のエクスポートに関するヘルプについては、「[エクスポートのトラブルシューティング]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/)」を参照してください。
{% endalert %}

{% endapi %}
