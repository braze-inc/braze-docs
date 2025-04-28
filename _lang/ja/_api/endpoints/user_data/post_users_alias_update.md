---
nav_title: "POST:ユーザーエイリアスを更新する"
article_title: "POST:ユーザーエイリアスを更新する"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "この記事では、「ユーザーエイリアスの更新」Braze エンドポイントの詳細について説明します。"
---
{% api %}
# ユーザーエイリアスを更新する
{% apimethod post %}
/users/alias/update
{% endapimethod %}

> このエンドポイントを使用して、既存のユーザーエイリアスを更新する。

ユーザーエイリアスはリクエストごとに50個まで指定できます。

ユーザーエイリアスを更新するには、`alias_label`、`old_alias_name`、`new_alias_name` をユーザーエイリアスの更新オブジェクトに含める必要があります。`alias_label` と`old_alias_name` に関連するユーザーエイリアスがない場合、エイリアスは更新されない。所定の `alias_label` と`old_alias_name` が見つかった場合、`old_alias_name` は `new_alias_name` に更新されます。

{% alert note %}
このエンドポイントは、`alias_updates` オブジェクトの更新順序を保証するものではない。
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#a084b843-b3cd-43f0-bfb1-ef7bada839c5 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、[API キー]({{site.baseurl}}/api/api_key/)と`users.alias.update`の権限が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='users alias update' %}

## 要求本文:

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "alias_updates" : (required, array of update user alias object)
}
```

### リクエストパラメーター

| パラメーター | required | データ型 | 説明 |
| --------- | --------- | --------- | ----------- |
| `alias_updates` | 必須 | 更新ユーザーエイリアスオブジェクトの配列 | [ユーザー別名オブジェクト]({{site.baseurl}}/api/objects_filters/user_alias_object/)を参照してください。<br><br> `old_alias_name`、`new_alias_name`、`alias_label` の詳細については、「[ユーザーエイリアス]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases)」を参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### 更新ユーザーエイリアスオブジェクト指定のエンドポイントリクエスト本体

```json
{
  "alias_label" : (required, string),
  "old_alias_name" : (required, string),
  "new_alias_name" : (required, string)
}
```

## 例のリクエスト
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/alias/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "alias_updates" :[
    {
      "alias_label": "example_alias_label",
      "old_alias_name" : "example_old_alias_name",
      "new_alias_name" : "example_new_alias_name"
    }
  ]
}'
```

{% endapi %}

