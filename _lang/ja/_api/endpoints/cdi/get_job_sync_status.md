---
nav_title: "GET：リストジョブの同期ステータス"
article_title: "GET：リストジョブの同期ステータス"
search_tag: Endpoint
page_order: 1
alias: /api/cdi/get_job_sync/
layout: api_page
page_type: reference
description: "この記事では、List job sync status Brazeエンドポイントの詳細について概説します。"

---
{% api %}
# ジョブの同期状況を一覧表示
{% apimethod get %}
/cdi/integrations/{integration_id}/job_sync_status
{% endapimethod %}

> このエンドポイントを使用して、指定した統合の過去の同期ステータスのリストを返します。

{% alert note %}
このエンドポイントを使用するには、`cdi.integration_job_status` パーミッションを持つ API キーを生成する必要があります。
{% endalert %}

## レート制限

{% multi_lang_include rate_limits.md endpoint='cdi job sync status' %}

## 経路パラメータ

| パラメータ｜必須｜データ型｜説明
|---|---|---|---|
|`integration_id` | 必須 | 文字列 | 統合 ID。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## クエリパラメーター

このエンドポイントを呼び出すと、10個のアイテムが返される。10回以上の同期がある統合では、次の応答例に示すように、`Link` ヘッダーを使用して、次のページのデータを取得します。

| パラメータ｜必須｜データ型｜説明
|---|---|---|---|
|`cursor` ｜オプション｜文字列｜同期ステータスのページ分割を決定します。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## リクエスト例

### カーソルなし

```
curl --location --request GET 'https://rest.iad-03.braze.com/cdi/integrations/00000000-0000-0000-0000-000000000000/job_sync_status' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

### カーソル付き

```
curl --location --request GET 'https://rest.iad-03.braze.com/cdi/integrations/00000000-0000-0000-0000-000000000000/job_sync_status?cursor=c2tpcDow' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## 応答

### 成功応答例

ステータスコード`200` 、以下のレスポンスボディを返すことができる。

{% alert note %}
`Link` ヘッダーは、シンクの合計が10以下の場合は存在しない。カーソルのない通話では、`prev` 。アイテムの最後のページを見るとき、`next` は表示されません。
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

｜job\_status｜ジョブステータス
| --- | --- |
|`running` | ジョブは現在実行中です。|
|`success` ｜すべての行が正常に同期されました。|
|`partial` | エラーにより一部の行の同期に失敗しました。|
|`error` | 同期された行はありません。|
|`config_error` ｜統合設定にエラーが発生しました。統合設定を確認してください。|
{: .reset-td-br-1 .reset-td-br-2}

## トラブルシューティング

次の表は、返される可能性のあるエラーと、それに関連するトラブルシューティングの手順を示したものです。

| トラブルシューティング
| --- | --- |
|`400 Invalid cursor` ｜`cursor` ｜が有効であることを確認する。|
|`400 Invalid integration ID` ｜`integration_id` ｜が有効であることを確認する。|
{: .reset-td-br-1 .reset-td-br-2}

その他のステータスコードと関連するエラーメッセージについては、[致命的なエラーと]({{site.baseurl}}/api/errors/#fatal-errors)応答を参照してください。

{% endapi %}
