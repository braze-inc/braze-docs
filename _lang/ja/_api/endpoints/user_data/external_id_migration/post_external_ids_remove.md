---
nav_title: "POST:外部IDを削除する"
article_title: "POST:外部IDを削除する"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "この記事では、Remove external IDs エンドポイントについての詳細を概説する。"

---
{% api %}
# 外部IDを削除する
{% apimethod post %}
/users/external_ids/remove
{% endapimethod %}

> このエンドポイントを使用して、ユーザーの古い非推奨外部 ID を削除します。

1回のリクエストで送信できる外部 ID は50個までです。

{% alert warning %}
このエンドポイントは非推奨 ID を完全に削除し、元に戻すことはできません。このエンドポイントを使用して、システム内でまだユーザーに関連付けられている非推奨の`external_ids` を削除すると、それらのユーザーのデータを永久に見つけることができなくなる。
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#e16b5340-5f44-42b6-9033-2398faf8908e {% endapiref %}

## 前提条件

このエンドポイントを使用するには、[API キー]({{site.baseurl}}/api/api_key/)と`users.external_ids.remove`の権限が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='external id migration' %}

## 要求本文:

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "external_ids" : (required, array of external identifiers to remove)
}
```

### リクエストパラメーター

| パラメーター | required | データ型 | 説明 |
| --------- | ---------| --------- | ----------- |
| `external_ids` | 必須 | 文字列の配列 | ユーザーが削除する外部識別子。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## リクエスト例

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
削除できるのは非推奨 ID のみです。1次外部 ID を削除しようとするとエラーになります。
{% endalert %}

## 応答

この応答は、成功したすべての削除と、関連するエラーを伴って失敗した削除を確認します。`removal_errors` フィールドのエラーメッセージは、元のリクエストの配列のインデックスを参照する。

```
{
  "message" : (string) status message,
  "removed_ids" : (array of strings) successful remove operations,
  "removal_errors": (array of arrays) <minor error message>
}
```

`message` フィールドは、有効なリクエストに対しては`success` を返す。より具体的なエラーは、`removal_errors` の配列に収められている。`message` フィールドは、以下の場合にエラーを返す：
- 無効なAPIキー
- 空の`external_ids` 配列
- 50を超える項目を持つ `external_ids` 配列
- レート制限のヒット (1,000 リクエスト/分超)

{% endapi %}
