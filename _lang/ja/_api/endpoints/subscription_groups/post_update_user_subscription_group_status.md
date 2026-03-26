---
nav_title: "POST: ユーザーのサブスクリプショングループステータスを更新する"
article_title: "POST: ユーザーのサブスクリプショングループステータスを更新する"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、「ユーザーのサブスクリプショングループステータスの更新」Braze エンドポイントの詳細について説明します。"
---
{% api %}
# ユーザーのサブスクリプショングループステータスの更新
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/subscription/status/set
{% endapimethod %}

> このエンドポイントを使用して、Braze ダッシュボード上で最大50ユーザーのサブスクリプション状態を一括更新します。

サブスクリプショングループの `subscription_group_id` にアクセスするには、**サブスクリプショングループ**ページに移動します。

**メールサブスクリプショングループ**の例を確認したり、このエンドポイントをテストしたりする場合:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#8895e87e-6324-47a3-a833-adf29a258bb9 {% endapiref %}

**SMS と RCS サブスクリプショングループ**の例を確認したり、このエンドポイントをテストしたりする場合:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#72558b32-7dbe-4cba-bd22-a7ce513076dd {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`subscription.status.set` 権限を持つ [API キー]({{site.baseurl}}/api/basics#rest-api-key/)が必要です。

{% alert note %}
このエンドポイントを [LINE サブスクリプショングループ]({{site.baseurl}}/user_guide/message_building_by_channel/line/line_users/subscription_groups/)で使用することに興味がある場合は、カスタマーサクセスマネージャーにお問い合わせください。
{% endalert %}

## レート制限

{% multi_lang_include rate_limits.md endpoint='subscription status set' %}

## リクエスト本文

{% tabs %}
{% tab SMS and RCS %}
```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
   "subscription_group_id": (required, string) the id of your subscription group,
   "subscription_state": (required, string) available values are "unsubscribed" (not in subscription group) or "subscribed" (in subscription group),
   "external_id": (required*, array of strings) the external ID of the user or users, may include up to 50 IDs,
   "phone": (required*, array of strings in E.164 format) The phone number of the user (must include at least one phone number and at most 50 phone numbers),
   "use_double_opt_in_logic": (optional, boolean) defaults to `false`; when `subscription_state` is "subscribed", set to `true` to enter the user into the SMS double opt-in workflow,
   // SMS and RCS subscription group - you must include one of external_id or phone
 }
```
\* SMS と RCS のサブスクリプショングループ: Braze は `external_id` または `phone` のみを受け付けます。

{% endtab %}
{% tab Email %}
```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
   "subscription_group_id": (required, string) the id of your subscription group,
   "subscription_state": (required, string) available values are "unsubscribed" (not in subscription group) or "subscribed" (in subscription group),
   "external_id": (required*, array of strings) the external ID of the user or users, may include up to 50 IDs,
   "email": (required*, array of strings) the email address of the user (must include at least one email and at most 50 emails),
   // Email subscription group - you must include one of external_id or email
   // Note that sending an email address that is linked to multiple profiles updates all relevant profiles
 }
```
\* メールサブスクリプショングループ: `email` または `external_id` のどちらかを含める必要があります。
{% endtab %}
{% endtabs %}

このプロパティは、ユーザーのプロファイル情報の更新には使用しないでください。代わりに [/users/track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) プロパティを使用してください。

{% alert tip %}
**既存ユーザーをサブスクリプショングループに追加する:** このエンドポイントは、既存ユーザーのサブスクリプショングループメンバーシップをバックフィルまたは一括更新するための推奨方法です。1回のリクエストで最大50件の `external_id`、メールアドレス、または電話番号を渡すことができます。ユーザーは[メールユーザー設定センター]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/overview/)のリンクから、自分のサブスクリプションステータスを更新することもできます。

**サブスクリプショングループ付きで新規ユーザーを作成する:** [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) エンドポイントを使用して新規ユーザーを作成する際、ユーザー属性オブジェクト内にサブスクリプショングループを設定できます。これにより、1回の API コールでユーザーの作成とサブスクリプショングループの状態設定を同時に行えます。
{% endalert %}

## リクエストパラメーター

| パラメーター | 必須 | データタイプ | 説明 |
|---|---|---|---|
| [`subscription_group_id`]({{site.baseurl}}/api/identifier_types/?tab=subscription%20group%20ids) | 必須 | 文字列 | サブスクリプショングループの `id`。 |
| `subscription_state` | 必須 | 文字列 | 使用できる値は、`unsubscribed`（サブスクリプショングループに含まれない）または `subscribed`（サブスクリプショングループに含まれる）です。 |
| `external_id` | 必須* | 文字列の配列 | ユーザーの `external_id`。最大50件の `id` を含めることができます。 |
| `email` | 必須* | 文字列または文字列の配列 | ユーザーのメールアドレス。文字列の配列として渡すことができます。少なくとも1件のメールアドレス（最大50件）を含める必要があります。<br><br>同じワークスペース内の複数のユーザー（`external_id`）が同じメールアドレスを共有している場合、Braze はそのメールアドレスを共有しているすべてのユーザーのサブスクリプショングループを更新します。 |
| `phone` | 必須* | [E.164](https://en.wikipedia.org/wiki/E.164) 形式の文字列 | ユーザーの電話番号。文字列の配列として渡すことができます。少なくとも1件の電話番号（最大50件）を含める必要があります。<br><br>同じワークスペース内の複数のユーザー（`external_id`）が同じ電話番号を共有している場合、Braze はその電話番号を共有しているすべてのユーザーを同じサブスクリプショングループの変更で更新します。 |
| `use_double_opt_in_logic` | オプション | ブール値 | SMS サブスクリプショングループにのみ適用されます。メールやその他のサブスクリプショングループタイプでは無視されます。省略した場合のデフォルトは `false` です。SMS サブスクリプショングループの場合、サブスクリプションステータスが `subscribed` に設定されたときにユーザーを [SMS ダブルオプトイン]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/double_opt_in/)ワークフローに入れるには `true` に設定します。このパラメーターが省略されるか `false` に設定された場合、ユーザーはダブルオプトインワークフローを経ずに購読されます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## リクエスト例

### メール

```
curl --location --request POST 'https://rest.iad-01.braze.com/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "subscription_group_id": "subscription_group_identifier",
  "subscription_state": "unsubscribed",
  "external_id": "external_identifier",
  "email": ["example1@email.com", "example2@email.com"]
}
'
```

### SMS と RCS

```
curl --location --request POST 'https://rest.iad-01.braze.com/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "subscription_group_id": "subscription_group_identifier",
  "subscription_state": "unsubscribed",
  "external_id": "external_identifier",
  "phone": ["+12223334444", "+11112223333"]
}
'
```

## 成功応答の例

ステータスコード `201` は、次の応答本文を返す可能性があります。

```json
{
    "message": "success"
}
```

{% alert important %}
このエンドポイントは `email` または `phone` の値のみを受け付け、両方を同時に受け付けることはできません。両方を指定した場合、次の応答が返されます: `{"message":"Either an email address or a phone number should be provided, but not both."}`
{% endalert %}

{% endapi %}