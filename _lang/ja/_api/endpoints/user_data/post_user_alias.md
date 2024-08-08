---
nav_title: "ポスト:新規ユーザーエイリアスの作成"
article_title: "ポスト:新規ユーザーエイリアスの作成"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "この記事では、Create new user alias Braze エンドポイントの詳細について説明します。"

---
{% api %}
# 新しいユーザーエイリアスを作成する
{% apimethod post %}
/users/alias/new
{% endapimethod %}

> このエンドポイントを使用して、既存の識別されたユーザーの新しいユーザー別名を追加したり、新しい識別されていないユーザーを作成したりします。

要求ごとに最大 50 のユーザーエイリアスを指定できます。

** 既存のユーザ** にユーザエイリアスを追加するには、新しいユーザエイリアスオブジェクトに`external_id` を含める必要があります。`external_id` がオブジェクトに存在するが、その`external_id` を持つユーザが存在しない場合、エイリアスはどのユーザにも追加されません。`external_id` が存在しない場合でも、ユーザは作成されますが、後で識別する必要があります。これを行うには、"Identifying Users"および`users/identify` エンドポイントを使用します。

**新しいエイリアスのみのユーザ**を作成するには、新しいユーザエイリアスオブジェクトから`external_id` を省略する必要があります。ユーザーが作成されたら、`/users/track` エンドポイントを使用して、エイリアスのみのユーザーを属性、イベント、購入に関連付け、`/users/identify` エンドポイントを使用して、`external_id` でユーザーを識別します。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5cf18e64-fd02-452f-8c90-9a0f7c4d0487 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`users.alias.new` 権限を持つ[API キー]({{site.baseurl}}/api/api_key/) が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='users alias new' %}

## リクエスト本文

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "user_aliases" : (required, array of new user alias object)
}
```

### 要求パラメータ

| パラメータ| 必須| データ型| 説明|
| --------- | ---------| --------- | ----------- |
| `user_aliases` | 必須| 新しいユーザエイリアスオブジェクトの配列| [ユーザエイリアスオブジェクト]({{site.baseurl}}/api/objects_filters/user_alias_object/) を参照してください。<br><br> `alias_name` および`alias_label` の詳細については、[User Aliases]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases) documentation.| を参照してください。
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

### 新しいユーザーエイリアスオブジェクト指定を持つエンドポイントリクエストボディ

```json
{
  "external_id" : (optional, string),
  "alias_name" : (required, string),
  "alias_label" : (required, string)
}
```

## リクエスト例
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

## レスポンス

```json
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
{
    "aliases_processed": 1,
    "message": "success"
}
```


{% endapi %}

