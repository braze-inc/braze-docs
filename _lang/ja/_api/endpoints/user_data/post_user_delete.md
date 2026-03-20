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

> 既知のユーザー識別子を指定してユーザープロファイルを削除するには、このエンドポイントを使用します。

1 つのリクエストには、最大 50 個の `external_ids`、`user_aliases`、`braze_ids`、`email_addresses`、または `phone_numbers` を含めることができます。単一のリクエストに含めることができるのは、`external_ids`、`user_aliases`、`braze_ids`、`email_addresses`、または `phone_numbers` のいずれか1つだけです。

API 経由でユーザーを一括削除しても解決できないユースケースがある場合は、[Braze サポートチーム]({{site.baseurl}}/user_guide/administrative/access_braze/support/)にお問い合わせください。

{% alert warning %}
ユーザープロファイルの削除は元に戻せません。ユーザーを完全に削除するため、データの矛盾が発生する可能性があります。[API を使用してユーザープロファイルを削除する]({{site.baseurl}}/help/help_articles/api/delete_user/)場合の詳細については、ヘルプドキュメントを参照してください。
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#22e91d00-d178-4b4f-a3df-0073ecfcc992 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`users.delete` 権限を持つ [API キー]({{site.baseurl}}/api/api_key/)が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='users delete' %}

## リクエスト本文

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

| パラメーター         | 必須 | データタイプ                  | 説明                                                                                      |
|-------------------|----------|----------------------------|--------------------------------------------------------------------------------------------------|
| `external_ids`    | オプション | 文字列の配列           | 削除する外部識別子。                                                    |
| `user_aliases`    | オプション | ユーザーエイリアスオブジェクトの配列 | 削除する[ユーザーエイリアス]({{site.baseurl}}/api/objects_filters/user_alias_object/)。 |
| `braze_ids`       | オプション | 文字列の配列           | 削除する Braze ユーザー識別子。                                                  |
| `email_addresses` | オプション | 文字列の配列           | 削除するユーザーのメール。詳細については、[メールによるユーザーの削除](#deleting-users-by-email)を参照してください。                                                             |
| `phone_numbers` | オプション | 文字列の配列 | 削除するユーザーの電話番号。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### メールアドレスと電話番号によるユーザーの削除

メールアドレスまたは電話番号が識別子として指定されている場合、識別子に追加の `prioritization` 値が必要です。`prioritization` は順序付けされた配列である必要があり、複数のユーザーが一致する場合に削除するユーザーを指定します。つまり、優先順位に一致するユーザーが複数いる場合、ユーザーの削除は実行されません。

配列に指定できる値は次のとおりです。

- `identified`
- `unidentified`
- `most_recently_updated`（最近更新されたユーザーを優先することを意味します）

`prioritization` 配列には、一度に次のオプションのいずれか1つのみを含めることができます。

- `identified` は `external_id` を持つユーザーを優先することを意味します
- `unidentified` は `external_id` を持たないユーザーを優先することを意味します

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
{
  "deleted" : (required, integer) number of user IDs queued for deletion
}
```

## トラブルシューティング

### 成功応答が返されたがユーザーがまだ表示される

成功応答はリクエストがキューに入れられたことを確認するものであり、削除が完了したことを意味するものではありません。削除は通常1秒以内に完了しますが、すべてのキャッシュに変更が反映されるまでに最大5分かかる場合があります。削除直後にダッシュボードでユーザーを検索したり、API 経由でデータをエクスポートしたりすると、この反映時間枠中はまだ結果が表示される場合があります。

数分経ってもユーザーがまだ存在する場合は、リクエスト内の識別子がユーザーの実際のプロファイルと一致しているか確認してください。

- **`external_ids` 配列:** 各値がユーザーの external ID と正確に一致していることを確認してください。
- **`braze_id`:** ユーザーの `braze_id` は、[`/users/export/ids` エンドポイント]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/)でデータをエクスポートするか、Segment を CSV にエクスポートすることで確認できます（`braze_id` は「Appboy ID」として表示されます）。
- **エイリアスのみまたはメールのみのプロファイル:** プロファイルに `external_id` がない場合は、**External User ID が空白**でフィルターし、既知のメールまたは電話番号と組み合わせた Segment を作成してから、CSV にエクスポートして `braze_id` を取得してください。

ユーザーが削除されたかどうかを確認するには、削除リクエストで使用したのと同じ識別子タイプを使用して [`/users/export/ids` エンドポイント]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/)を呼び出します（例えば、`external_ids`、`braze_id`、または `user_aliases` に値を含めます）。ユーザーが存在しなくなった場合、応答には `"users": []` が含まれ、その識別子をリストする `"invalid_user_ids"` が含まれる場合があります。

{% endapi %}