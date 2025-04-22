---
nav_title: "POST:ユーザーを削除する"
article_title: "POST:ユーザーを削除する"
search_tag: Endpoint
page_order: 5
layout: api_page
page_type: reference
description: "この記事では、「ユーザーの削除」Braze エンドポイントの詳細について説明します。"

---
{% api %}
# ユーザーを削除する
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/users/delete
{% endapimethod %}

> 既知のユーザー識別子を指定してユーザー・プロファイルを削除するには、このエンドポイントを使用する。

1 つのリクエストには、最大 50 個の `external_ids`、`user_aliases`、`braze_ids`、`email_addresses`、または `phone_numbers` を含めることができます。単一のリクエストに含めることができるのは、`external_ids`、`user_aliases`、`braze_ids`、`email_addresses`、または`phone_numbers`のいずれか1つだけです。 

API を使用した一括ユーザ削除では解決できないユースケースがある場合は、[ブレーズサポートチーム]({{site.baseurl}}/user_guide/administrative/access_braze/support/) にお問い合わせください。

{% alert warning %}
ユーザープロファイルの削除は元に戻せません。ユーザーを完全に削除するため、データの矛盾が発生する可能性があります。[API を使用してユーザープロファイルを削除する]({{site.baseurl}}/help/help_articles/api/delete_user/)場合の詳細については、ヘルプドキュメントを参照してください。
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#22e91d00-d178-4b4f-a3df-0073ecfcc992 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、[API キー]({{site.baseurl}}/api/api_key/)と`users.delete`の権限が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='users delete' %}

## 要求本文:

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "external_ids" : (optional, array of string) External IDs to be deleted,
  "user_aliases" : (optional, array of user alias objects) User aliases to be deleted,
  "braze_ids" : (optional, array of string) Braze user identifiers to be deleted,
  "email_addresses": (optional, array of string) User emails to be deleted,
  "phone_numbers": (optional, array of string) User phone numbers to be deleted
}
```
### リクエストパラメーター

| パラメーター         | required | データ型                  | 説明                                                                                      |
|-------------------|----------|----------------------------|--------------------------------------------------------------------------------------------------|
| `external_ids`    | オプション | 文字列の配列           | 削除する外部識別子。                                                    |
| `user_aliases`    | オプション | ユーザー別名オブジェクトの配列 | [削除するユーザーエイリアス]({{site.baseurl}}/api/objects_filters/user_alias_object/)。 |
| `braze_ids`       | オプション | 文字列の配列           | 削除するブレーズユーザー識別子。                                                  |
| `email_addresses` | オプション | 文字列の配列           | 削除するユーザメール。詳細については、[電子メールによるユーザーの削除](#deleting-users-by-email)を参照してください。                                                             |
| `phone_numbers` | オプション | 文字列の配列 | 削除するユーザー電話番号。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### メールでユーザーを削除する

識別子として`email` が指定された場合、識別子にはさらに`prioritization` の値が必要となる。`prioritization` は順序付き配列で、複数のユーザーが見つかった場合、どのユーザーを削除するかを指定する。つまり、複数のユーザーが優先順位に一致する場合、ユーザーの削除は起こらない。

配列に使用できる値は、`identified`、`unidentified`、`most_recently_updated` です。`most_recently_updated` は、最も最近更新されたユーザーを優先することを意味します。

優先配列には、一度に以下のオプションのうち1つしか存在できません。

- `identified` を持つユーザーを優先することである。 `external_id`
- `unidentified` のないユーザーを優先することである。 `external_id`

## 例のリクエスト

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
  ],
  "email_addresses": [
    {
      "email": "john.smith@braze.com",
      "prioritization": ["unidentified", "most_recently_updated"]
    }
  ]
}'
```

## 応答

```json
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
{
  "deleted" : (required, integer) number of user IDs queued for deletion
}
```
{% endapi %}


