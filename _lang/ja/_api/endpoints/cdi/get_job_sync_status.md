---
nav_title: "取得:ジョブの同期ステータスの一覧表示"
article_title: "取得:ジョブの同期ステータスの一覧表示"
search_tag: Endpoint
page_order: 1
alias: /api/cdi/get_job_sync/
layout: api_page
page_type: reference
description: "この記事では、ジョブの同期ステータスを一覧表示するBrazeエンドポイントの詳細について説明します。"

---
{% api %}
# ジョブの同期状態を一覧表示する
{% apimethod get %}
/cdi/integrations/{integration_id}/job_sync_status
{% endapimethod %}

> このエンドポイントを使用して、特定の統合の過去の同期ステータスのリストを返します。

{% alert note %}
このエンドポイントを使用するには、アクセス許可を持つ `cdi.integration_job_status` API キーを生成する必要があります。
{% endalert %}

## レート制限

{% multi_lang_include rate_limits.md endpoint='cdi job sync status' %}

## パス パラメーター

|パラメータ |必須項目 |データ型 |説明 |
|---|---|---|---|
| `integration_id` |必須項目 |文字列 |インテグレーション ID。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## クエリパラメーター

このエンドポイントを呼び出すたびに、10 個の項目が返されます。同期が 10 回を超える統合の場合は、次の応答例に示すように、ヘッダーを使用して `Link` 次のページのデータを取得します。

|パラメータ |必須項目 |データ型 |説明 |
|---|---|---|---|
| `cursor` |オプション |文字列 |同期ステータスのページネーションを決定します。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## 要求の例

### カーソルなし

```
curl --location --request GET 'https://rest.iad-03.braze.com/cdi/integrations/00000000-0000-0000-0000-000000000000/job_sync_status' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

### カーソルあり

```
curl --location --request GET 'https://rest.iad-03.braze.com/cdi/integrations/00000000-0000-0000-0000-000000000000/job_sync_status?cursor=c2tpcDow' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## 応答

### 成功応答の例

状態コード `200` は、次の応答本文を返す可能性があります。

{% alert note %}
`Link`同期の合計が 10 個以下の場合、ヘッダーは存在しません。カーソルのない呼び出しの場合、 `prev` は表示されません。アイテムの最後のページを見ると、 `next` 表示されません。
{% endalert %}

```
Link: </cdi/integrations/00000000-0000-0000-0000-000000000000/job_sync_status?cursor=c2tpcDow>; rel="prev",</cdi/integrations00000000-0000-0000-0000-000000000000/job_sync_status?cursor=c2tpcDoxMDA=>; rel="next"
```

```json
{
  "results": [
    {
        "job_status": (string) status of the sync, see below for explanation of different statuses,
        "sync_start_time": (string) time the sync started in ISO 8601,
        "sync_finish_time": (string) time the sync finished in ISO 8601,
        "last_timestamp_synced": (string) last UPDATED_AT timestamp processed by the sync in ISO 8601,
        "rows_synced": (integer) number of rows successfully synced to Braze,
        "rows_failed_with_errors": (integer) number of rows failed because of errors,
    },
  ],
  "message": "success"
}
```

|job\_status |解説 |
| --- | --- |
| `running` |ジョブは現在実行中です。|
| `success` |すべての行が正常に同期されました。|
| `partial` |エラーのため、一部の行が同期に失敗しました。|
| `error` |行は同期されませんでした。|
| `config_error` |統合構成でエラーが発生しました。統合の設定を確認してください。|
{: .reset-td-br-1 .reset-td-br-2}

## トラブルシューティング

次の表に、返される可能性のあるエラーと、それに関連するトラブルシューティング手順を示します。

|エラー |トラブルシューティング |
| --- | --- |
| `400 Invalid cursor` |Ur `cursor` が有効であることを確認してください。 |
| `400 Invalid integration ID` |Ur `integration_id` が有効であることを確認してください。 |
{: .reset-td-br-1 .reset-td-br-2}

その他のステータスコードと関連するエラーメッセージについては、 [致命的なエラーと応答]({{site.baseurl}}/api/errors/#fatal-errors)を参照してください。

{% endapi %}
