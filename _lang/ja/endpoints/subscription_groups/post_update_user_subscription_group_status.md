---
nav_title: "POST:アップデートユーザーs サブスクリプショングループ ステータス"
article_title: "POST:ユーザーのサブスクリプション・グループ・ステータスを更新する"
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

サブスクリプショングループの`subscription_group_id` にアクセスするには、**サブスクリプショングループ** ページに移動します。

例を見たり、このエンドポイントをテストしたりする場合は、**メールサブスクリプショングループ**をご覧ください。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#8895e87e-6324-47a3-a833-adf29a258bb9 {% endapiref %}

**SMS と RCS 購読グループ**用のこのエンドポイントをテストするか例を見たい場合:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#72558b32-7dbe-4cba-bd22-a7ce513076dd {% endapiref %}

## 前提条件

このエンドポイントを使用するには、[API キー]({{site.baseurl}}/api/basics#rest-api-key/)と`subscription.status.set`の権限が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='subscription status set' %}

## Request body

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
   // SMS and RCS subscription group - one of external_id or phone is required
 }
```
\* SMS と RCS の購読グループ：`external_id` または`phone` のみが受け入れられます。

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
   // Email subscription group - one of external_id or email is required
   // Note that sending an email address that is linked to multiple profiles will update all relevant profiles
 }
```
\* 電子メールサブスクリプショングループ:`email` または`external_id` のいずれかが必要です。
{% endtab %}
{% endtabs %}

このプロパティは、ユーザーのプロファイル情報の更新には使用しないでください。代わりに、[/users/track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)プロパティを使用します。

{% alert tip %}
[users/track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)エンドポイントを使用して新規ユーザーを作成する際、ユーザー属性オブジェクト内にサブスクリプショングループを設定することができる。これにより、1回のAPIコールでユーザーを作成し、サブスクリプショングループの状態を設定することができる。
{% endalert %}

## リクエストパラメーター

| パラメーター | required | データ型 | 説明 |
|---|---|---|---|
| [`subscription_group_id`]({{site.baseurl}}/api/identifier_types/?tab=subscription%20group%20ids) | 必須 | 文字列 | サブスクリプショングループの`id`。 |
| `subscription_state` | 必須 | 文字列 | 使用できる値は、`unsubscribed` (サブスクリプショングループに含まれない) または `subscribed` (サブスクリプショングループに含まれる) です。 |
| `external_id` | 必須* | 文字列の配列 | ユーザーの `external_id` には、最大で 50 個の `id` を含めることができます。 |
| `email` | 必須* | 文字列または文字列の配列 | ユーザーのメールアドレスは、文字列の配列として渡すことができます。少なくとも 1 件のメールアドレス (最大 50件 まで) を含める必要があります。<br><br>同じワークスペース内の複数のユーザー (`external_id`) が同じメールアドレスを共有している場合、そのメールアドレスを共有するすべてのユーザーは、サブスクリプショングループの変更で更新されます。 |
| `phone` | 必須* | [E.164](https://en.wikipedia.org/wiki/E.164)形式の文字列 | ユーザーの電話番号は文字列の配列として渡すことができます。少なくとも 1 つの電話番号を含める必要があります（最大 50 件）。<br><br>同じワークスペース内の複数のユーザー (`external_id`) が同じ電話番号を共有している場合、その電話番号を共有しているすべてのユーザーは同じ購読グループの変更で更新されます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 例のリクエスト

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
エンドポイントは、`email` または`phone` 値のみを受け入れ、両方を受け入れません。両方を指定した場合、次のレスポンスが返されます。 `{"message":"Either an email address or a phone number should be provided, but not both."}`
{% endalert %}

{% endapi %}

