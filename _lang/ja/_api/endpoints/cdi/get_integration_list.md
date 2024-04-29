---
nav_title: "取得:リストの統合"
article_title: "取得:リストの統合"
search_tag: Endpoint
page_order: 1
alias: /api/cdi/get_integration_list/
layout: api_page
page_type: reference
description: "この記事では、List integrations Brazeエンドポイントの詳細について説明します。"

---
{% api %}
# リスト統合
{% apimethod get %}
/cdi/integrations
{% endapimethod %}

> このエンドポイントを使用して、既存の統合のリストを返します。


{% alert note %}
このエンドポイントを使用するには、`cdi.integration_list`権限でAPIキーを生成する必要があります。
{% endalert %}

## レート制限

{% multi_lang_include rate_limits.md endpoint='cdi list integrations' %}

## クエリパラメーター

このエンドポイントの呼び出しごとに10個のアイテムが返されます。10個以上の連動があるリストの場合は、応答例に示すように、`Link`ヘッダーを使用して次のページのデータを取得します。

|パラメータ|必須|データ型|説明|
|---|---|---|---|
| `cursor` | オプション | 文字列 | 連動リストのページネーションを決定します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## リクエストの例

### カーソルなし

```
curl --location --request GET 'https://rest.iad-03.braze.com/cdi/integrations' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

### カーソルあり

```
curl --location --request GET 'https://rest.iad-03.braze.com/cdi/integrations?cursor=c2tpcDow' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## 応答

### 成功時の応答の例

ステータスコード`200`は次のレスポンスボディを返す可能性があります。

{% alert note %}
`Link`ヘッダーは、合計で10個以下の統合がある場合、存在しません。カーソルのないコールの場合、`prev`は表示されません。アイテムの最後のページを見ると、`next`は表示されません。
{% endalert %}

```
Link: </cdi/integrations?cursor=c2tpcDow>; rel="prev",</cdi/integrations?cursor=c2tpcDoxMDA=>; rel="next"
```

```json
{
  "results": [
    {
      "integration_id": (string) integration ID,
      "app_group_id": (string) app group ID,
      "integration_name": (string) integration name,
      "integration_type": (string) integration type,
      "integration_status": (string) integration status,
      "contact_emails": (string) contact email(s),
      "last_updated_at": (string) last timestamp that was synced in ISO 8601,
      "warehouse_type": (string) data warehouse type,
      "last_job_start_time": (string) timestamp of the last sync run in ISO 8601,
      "last_job_status": (string) status of the last sync run,
      "next_scheduled_run": (string) timestamp of the next scheduled sync in ISO 8601,
    },
  ],
  "message": "success"
}
```

## トラブルシューティング

次の表に、返される可能性のあるエラーとそれに関連するトラブルシューティング手順を示します。

|エラー|トラブルシューティング|
| --- | --- |
| `400 Invalid cursor` | `cursor`が有効かどうか確認してください。 |
{: .reset-td-br-1 .reset-td-br-2}

その他のステータスコードおよび関連するエラーメッセージについては、「[致命的エラー&応答]({{site.baseurl}}/api/errors/#fatal-errors)」を参照してください。

{% endapi %}
