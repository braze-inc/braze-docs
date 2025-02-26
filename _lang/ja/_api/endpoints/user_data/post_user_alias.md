---
nav_title: "POST:新しいユーザーエイリアスを作成する"
article_title: "POST:新しいユーザーエイリアスを作成する"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "この記事では、「新しいユーザーエイリアスの作成」Braze エンドポイントの詳細について説明します。"

---
{% api %}
# 新しいユーザーエイリアスを作成する
{% apimethod post %}
/users/alias/new
{% endapimethod %}

> このエンドポイントを使用して、既存の識別されたユーザーに新しいユーザーエイリアスを追加するか、新しい識別されていないユーザーを作成する。

ユーザーエイリアスはリクエストごとに50個まで指定できます。

**既存のユーザーのユーザーエイリアスを追加**するには、新しいユーザーエイリアスオブジェクトに `external_id` を含める必要があります。オブジェクトに`external_id` が存在しても、その`external_id` を持つユーザーがいない場合、エイリアスはどのユーザーにも追加されない。`external_id` が存在しない場合、ユーザーは作成されますが、後で識別する必要があります。これは、「Identifying Users」と `users/identify` エンドポイントを使用して行うことができます。

**エイリアスのみの新規ユーザーを作成**するには、新規ユーザーエイリアスオブジェクトから `external_id` を省略する必要があります。ユーザーが作成されたら、`/users/track` エンドポイントを使用して、エイリアスのみのユーザーに属性、イベント、購入を関連付け、`/users/identify` エンドポイントを使用して、`external_id` でユーザーを識別します。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5cf18e64-fd02-452f-8c90-9a0f7c4d0487 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、[API キー]({{site.baseurl}}/api/api_key/)と`users.alias.new`の権限が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='users alias new' %}

## 要求本文:

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "user_aliases" : (required, array of new user alias object)
}
```

### リクエストパラメーター

| パラメーター | required | データ型 | 説明 |
| --------- | ---------| --------- | ----------- |
| `user_aliases` | 必須 | 新しいユーザーエイリアスオブジェクトの配列 | [ユーザー別名オブジェクト]({{site.baseurl}}/api/objects_filters/user_alias_object/)を参照してください。<br><br> `alias_name` と`alias_label` の詳細については、[User Aliasesの]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases)ドキュメントを参照のこと。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### 新しいユーザーエイリアスオブジェクトを指定したエンドポイントリクエスト本文

```json
{
  "external_id" : (optional, string),
  "alias_name" : (required, string),
  "alias_label" : (required, string)
}
```

## 例のリクエスト
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/alias/new' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "user_aliases" :[
    {
      "external_id": "external_identifier",
      "alias_name" : "example_name",
      "alias_label" : "example_label"
    }
  ]
}'
```

## 応答

```json
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
{
    "aliases_processed": 1,
    "message": "success"
}
```


{% endapi %}

