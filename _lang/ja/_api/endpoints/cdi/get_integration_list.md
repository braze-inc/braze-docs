---
nav_title: "取得:リストの統合"
article_title: "取得:リスト統合"
search_tag: Endpoint
page_order: 1
alias: /api/cdi/get_integration_list/
layout: api_page
page_type: reference
description: "この記事では、「リスト統合」Braze エンドポイントの詳細について説明します。"

---
{% api %}
# リストの統合
{% apimethod get %}
/cdi/integrations
{% endapimethod %}

> 既存の統合のリストを返すには、このエンドポイントを使う。


{% alert note %}
このエンドポイントを使用するには、`cdi.integration_list` 権限を持つ API キーを生成する必要があります。
{% endalert %}

## レート制限

{% multi_lang_include rate_limits.md endpoint='cdi list integrations' %}

## クエリーパラメーター

このエンドポイントを呼び出すと、10個のアイテムが返される。10を超える統合のあるリストについては、応答の例に示すように、`Link` ヘッダーを使用して次のページのデータを取得します。

| パラメータ | required | データ型 | 説明 |
|---|---|---|---|
| `cursor` | オプション | 文字列 | 統合リストのページネーションを決定する。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## 例のリクエスト

### カーソルなし

```
curl --location --request GET 'https://rest.iad-03.braze.com/cdi/integrations' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

### カーソル付き

```
curl --location --request GET 'https://rest.iad-03.braze.com/cdi/integrations?cursor=c2tpcDow' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## 応答

### 成功応答の例

ステータスコード `200` は、次の応答本文を返す可能性があります。

{% alert note %}
`Link` ヘッダーは、統合の合計が10以下の場合は存在しません。カーソルのない呼び出しでは、`prev` は表示されません。項目の最後のページを見ると、`next` は表示されません。
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

次のテーブルに、返される可能性のあるエラーと、関連するトラブルシューティングステップを示します。

| エラー | トラブルシューティング |
| --- | --- |
| `400 Invalid cursor` | `cursor` が有効であることを確認します。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

その他のステータスコードと関連するエラーメッセージについては、[致命的エラー& レスポンスを]({{site.baseurl}}/api/errors/#fatal-errors)参照のこと。

{% endapi %}
