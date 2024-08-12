---
nav_title: "ポスト:外部ID の削除"
article_title: "ポスト:外部ID の削除"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "この記事では、外部ID の削除エンドポイントの詳細について説明します。"

---
{% api %}
# 外部ID の削除
{% apimethod post %}
/users/external_ids/remove
{% endapimethod %}

> このエンドポイントを使用して、ユーザーの古い非推奨の外部ID を削除します。 

リクエストごとに最大 50 個の外部 ID を送信できます。 

{% alert warning %}
このエンドポイントは、非推奨のID を完全に削除し、元に戻すことはできません。このエンドポイントを使用して、システム内のユーザーにまだ関連付けられている非推奨の`external_ids` を削除すると、ユーザーのデータが永続的に見つからなくなる可能性があります。
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#e16b5340-5f44-42b6-9033-2398faf8908e {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`users.external_ids.remove` 権限を持つ[API キー]({{site.baseurl}}/api/api_key/) が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='external id migration' %}

## リクエスト本文

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "external_ids" : (required, array of external identifiers to remove)
}
```

### 要求パラメータ

| パラメータ| 必須| データ型| 説明|
| --------- | ---------| --------- | ----------- |
| `external_ids` | 必須| 文字列の配列| 削除するユーザの外部識別子。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## 依頼例
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/external_ids/remove' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "external_ids" :[
    "existing_deprecated_external_id_string",
    ...
  ]
}'
```
{% alert important %}
非推奨のID のみを削除できます。プライマリ外部ID を削除しようとするとエラーが発生します。
{% endalert %}

## レスポンス 
レスポンスでは、すべての正常な削除と、関連するエラーによる不成功の削除が確認されます。`removal_errors` フィールドのエラーメッセージは、元のリクエストの配列のインデックスを参照します。

```
{
  "message" : (string) status message,
  "removed_ids" : (array of strings) successful remove operations,
  "removal_errors": (array of arrays) <minor error message>
}
```

`message` フィールドは、有効なリクエストに対して`success` を返します。より具体的なエラーは、`removal_errors` 配列にキャプチャされます。`message` フィールドは、次の場合にエラーを返します。
\- 無効なAPI キー
\- 空の`external_ids` 配列
- `external_ids` 50 項目以上の配列
\- レートリミットヒット(1000件/分以上)

{% endapi %}
