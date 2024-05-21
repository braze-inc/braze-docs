---
nav_title: "ポスト:トリガ同期"
article_title: "ポスト:トリガ同期"
search_tag: Endpoint
page_order: 2
alias: /api/cdi/post_trigger_sync/
layout: api_page
page_type: reference
description: "この記事では、トリガ同期Brazeエンドポイントの詳細について説明します。"

---
{% api %}
# 同期のトリガ
{% apimethod post %}
/cdi/integrations/{integration_id}/sync
{% endapimethod %}

> このエンドポイントを使用して、特定の統合の同期をトリガします。

{% alert note %}
このエンドポイントを使用するには、`cdi.integration_sync` 権限を持つAPI キーを生成する必要があります。
{% endalert %}

## レート制限

{% multi_lang_include rate_limits.md endpoint='cdi job sync' %}

## パスパラメータ

| パラメータ| 必須| データ型| 説明|
|---|---|---|---|
| `integration_id` | 必須| 文字列| 統合ID. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## リクエスト例

```
curl --location --request POST 'https://rest.iad-03.braze.com/cdi/integrations/00000000-0000-0000-0000-000000000000/sync' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## レスポンス

### 成功応答の例

ステータスコード`202` は、以下のレスポンスボディを返す可能性があります。

```json
{
  "message": "success"
}
```

## トラブルシューティング

次の表に、返される可能性のあるエラーと関連するトラブルシューティング手順を示します。

| エラー| トラブルシューティング|
| --- | --- |
| `400 Invalid integration ID` | `integration_id` が有効であることを確認します。|
| `404 Integration not found` | 指定された統合ID には統合が存在しません。統合ID が有効であることを確認します。|
| `429 Another job is in progress` | この統合のために現在実行中の同期があります。同期が完了したら、再試行します。|
{: .reset-td-br-1 .reset-td-br-2}

その他のステータスコードと関連するエラーメッセージについては、[Fatal errors & responses]({{site.baseurl}}/api/errors/#fatal-errors)を参照してください。

{% endapi %}
