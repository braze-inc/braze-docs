---
nav_title: "取得:リストインテグレーション"
article_title: "取得:リストインテグレーション"
search_tag: Endpoint
page_order: 1
alias: /api/cdi/get_integration_list/
layout: api_page
page_type: reference
description: "この記事では、List インテグレーション Braze エンドポイントの詳細について説明します。"

---
{% api %}
# インテグレーションを一覧表示
{% apimethod get %}
/cdi/integrations
{% endapimethod %}

> このエンドポイントを使用して、既存のインテグレーションのリストを返します。


{% alert note %}
このエンドポイントを使用するには、`cdi.integration_list`権限のある API キーを生成する必要があります。
{% endalert %}

## レート制限

{% multi_lang_include rate_limits.md endpoint='cdi list integrations' %}

## クエリパラメーター

このエンドポイントを呼び出すたびに、10 個の項目が返されます。インテグレーションが 10 個を超えるリストの場合は、レスポンス例に示すように、`Link`ヘッダーを使用して次のページのデータを取得します。

| パラメーター | 必須 | データ型 | 説明 |
|---|---|---|---|
| `cursor` | オプション | 文字列 | 統合リストのページネーションを決定します。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## リクエスト例

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

### 成功レスポンスの例

`200`ステータスコードは次のレスポンスボディを返す可能性があります。

{% alert note %}
合計でインテグレーションの数が 10 以下の場合、`Link`ヘッダーは存在しません。`prev`カーソルのない呼び出しでは表示されません。商品の最終ページを見ても、`next`表示されません。
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

次の表は、返される可能性のあるエラーとそれに関連するトラブルシューティング手順を示しています。

| エラー | トラブルシューティング |
| --- | --- |
| `400 Invalid cursor` | `cursor` あなたのが有効であることを確認してください。|
{: .reset-td-br-1 .reset-td-br-2}

その他のステータスコードおよび関連するエラーメッセージについては、「[致命的なエラーとレスポンス]({{site.baseurl}}/api/errors/#fatal-errors)」を参照してください。

{% endapi %}
