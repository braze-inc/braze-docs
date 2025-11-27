---
nav_title: "取得:カスタムイベントをエクスポート"
article_title: "取得:カスタムイベントのエクスポート"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、エクスポートカスタムイベントBrazeエンドポイントの詳細について説明します。"

---
{% api %}
# カスタムイベントをエクスポート
{% apimethod get %}
/events
{% endapimethod %}

> このエンドポイントを使用して、アプリ用に記録されたカスタムイベントのリストをエクスポートします。イベントはアルファベット順に並べ替えられ、50件ずつのグループで返されます。

## 前提条件

このエンドポイントを使用するには、[API キー]({{site.baseurl}}/api/basics#rest-api-key/)と`events.get`の権限が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='events' %}

## クエリーパラメーター

このエンドポイントへの各呼び出しは50のイベントを返すことに注意してください。50を超えるイベントについては、次の応答の例に示すように、`Link` ヘッダーを使用して次のページのデータを取得します。

| パラメータ | required | データ型 | 説明 |
|---|---|---|---|
| `cursor` | オプション | 文字列 | カスタムイベントのページネーションを決定します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## 例のリクエスト

### カーソルなし

```
curl --location --request GET 'https://rest.iad-01.braze.com/events' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

### カーソル付き

```
curl --location --request GET 'https://rest.iad-03.braze.com/events?cursor=c2tpcDow' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## 応答

```json
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "events" : [
        {
            "name": "The event name", (string) the event name,
            "description": "The event description", (string) the event description,
            "included_in_analytics_report": false, (boolean) the analytics report inclusion,
            "status": "Active", (string) the event status,
            "tag_names": ["Tag One", "Tag Two"] (array) the tag names associated with the event formatted as strings,
        },
        ...
    ]
}
```

### 致命的なエラーの応答コード {#fatal-export}

リクエストが致命的なエラーに遭遇した場合に返されるステータスコードと関連するエラーメッセージについては、[致命的なエラー]({{site.baseurl}}/api/errors/#fatal-errors)を参照してください。

{% alert tip %}
CSV および API のエクスポートに関するヘルプについては、「[エクスポートのトラブルシューティング]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/)」を参照してください。
{% endalert %}

{% endapi %}
