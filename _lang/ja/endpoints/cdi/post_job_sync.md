---
nav_title: "POST:トリガー同期"
article_title: "POST:トリガー同期"
search_tag: Endpoint
page_order: 2
alias: /api/cdi/post_trigger_sync/
layout: api_page
page_type: reference
description: "この記事では、「同期をトリガー」Braze エンドポイントの詳細について説明します。"

---
{% api %}
# 同期をトリガー
{% apimethod post %}
/cdi/integrations/{integration_id}/sync
{% endapimethod %}

> このエンドポイントを使用して、特定のインテグレーションのシンクをトリガーします。

{% alert note %}
このエンドポイントを使用するには、`cdi.integration_sync` 権限を持つ API キーを生成する必要があります。
{% endalert %}

## レート制限

{% multi_lang_include rate_limits.md endpoint='cdi job sync' %}

## パスパラメーター

| パラメータ | required | データ型 | 説明 |
|---|---|---|---|
| `integration_id` | 必須 | 文字列 | 統合 ID。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## 例のリクエスト

```
curl --location --request POST 'https://rest.iad-03.braze.com/cdi/integrations/00000000-0000-0000-0000-000000000000/sync' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## 応答

### 成功応答の例

ステータスコード `202` は、次の応答本文を返す可能性があります。

```json
{
  "message": "success"
}
```

## トラブルシューティング

次のテーブルに、返される可能性のあるエラーと、関連するトラブルシューティングステップを示します。

| エラー | トラブルシューティング |
| --- | --- |
| `400 Invalid integration ID` | `integration_id` が有効であることを確認します。 |
| `404 Integration not found` | 指定された統合 ID には統合が存在しません。統合ID が有効であることを確認します。 |
| `429 Another job is in progress` | この統合のために現在実行されている同期があります。同期が完了したら、もう一度試してください。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

その他のステータスコードと関連するエラーメッセージについては、[致命的なエラー& レスポンスを]({{site.baseurl}}/api/errors/#fatal-errors)参照のこと。

{% endapi %}
