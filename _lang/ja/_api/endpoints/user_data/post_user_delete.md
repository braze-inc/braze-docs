---
nav_title: "ポスト:ユーザーの削除"
article_title: "ポスト:ユーザーの削除"
search_tag: Endpoint
page_order: 5
layout: api_page
page_type: reference
description: "この記事では、Delete users Braze エンドポイントの詳細について説明します。"

---
{% api %}
# ユーザーの削除
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/users/delete
{% endapimethod %}

> このエンドポイントを使用して、既知のユーザー識別子を指定してユーザープロファイルを削除します。

1 つのリクエストには、最大 50 個の `external_ids`、`user_aliases`、または `braze_ids` を含めることができます。単一のリクエストに含めることができるのは、`external_ids`、`user_aliases`、または`braze_ids` のいずれか1つだけです。

{% alert warning %}
ユーザープロファイルの削除は取り消せません。これにより、データの不一致を引き起こす可能性のあるユーザーが永久的に削除されます。ヘルプのドキュメントで、[API]({{site.baseurl}}/help/help_articles/api/delete_user/) を使用してユーザープロファイルを削除した場合の動作について詳しく説明します。
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#22e91d00-d178-4b4f-a3df-0073ecfcc992 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`users.delete` 権限を持つ[API キー]({{site.baseurl}}/api/api_key/) が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='users delete' %}

## リクエスト本文

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "external_ids" : (optional, array of string) External ids for the users to delete,
  "user_aliases" : (optional, array of user alias objects) User aliases for the users to delete,
  "braze_ids" : (optional, array of string) Braze user identifiers for the users to delete
}
```
### 要求パラメータ

| パラメータ| 必須| データ型| 説明|
| --------- | ---------| --------- | ----------- |
| `external_ids` | オプション| 文字列の配列| 削除するユーザの外部識別子。|
| `user_aliases` | オプション| 削除するユーザのユーザエイリアスオブジェクトの配列| [ユーザエイリアス]({{site.baseurl}}/api/objects_filters/user_alias_object/)
| `braze_ids` | オプション| 文字列の配列| 削除するユーザのユーザ識別子をろう付け|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## リクエスト例
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/delete' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "external_ids": ["external_identifier1", "external_identifier2"],
  "braze_ids": ["braze_identifier1", "braze_identifier2"],
  "user_aliases": [
    {
      "alias_name": "user_alias1", "alias_label": "alias_label1"
    },
    {
      "alias_name": "user_alias2", "alias_label": "alias_label2"
    }
  ]
}'
```

## レスポンス

```json
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
{
  "deleted" : (required, integer) number of user ids queued for deletion
}
```
{% endapi %}


