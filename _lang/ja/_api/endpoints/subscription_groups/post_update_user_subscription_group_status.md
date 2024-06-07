---
nav_title: "ポスト:ユーザーのサブスクリプショングループステータスの更新"
article_title: "ポスト:ユーザーのサブスクリプショングループステータスの更新"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、ユーザーのサブスクリプショングループのステータスを更新する Braze エンドポイントの詳細について説明します。"
---
{% api %}
# ユーザーのサブスクリプショングループのステータスを更新
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/subscription/status/set
{% endapimethod %}

> このエンドポイントを使用して、Braze ダッシュボードで最大 50 人のユーザーのサブスクリプション状態を一括更新します。 

サブスクリプショングループページに移動すると、**サブスクリプショングループにアクセスできます**。`subscription_group_id`

**メール購読グループの例を確認したり**、このエンドポイントをテストしたりするには:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#8895e87e-6324-47a3-a833-adf29a258bb9 {% endapiref %}

**SMS サブスクリプショングループの例を確認したり**、このエンドポイントをテストしたりするには:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#72558b32-7dbe-4cba-bd22-a7ce513076dd {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`subscription.status.set`権限のある [API キーが必要です]({{site.baseurl}}/api/basics#rest-api-key/)。

## レート制限

{% multi_lang_include rate_limits.md endpoint='subscription status set' %}

## リクエスト本文

{% tabs %}
{% tab SMS %}
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
   // SMS subscription group - one of external_id or phone is required
 }
```
SMS サブスクリプショングループ`external_id``phone`またはのみ受け付けます。

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
\* メール購読グループ:`email``external_id`またはのいずれかが必須です。
{% endtab %}
{% endtabs %}

このプロパティは、ユーザーのプロファイル情報の更新には使用しないでください。[/users/track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)代わりにプロパティを使用してください。

{% alert tip %}
[/users/track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)エンドポイント経由で新しいユーザーを作成する場合、ユーザー属性オブジェクト内でサブスクリプショングループを設定できます。これにより、1 回の API 呼び出しでユーザーを作成し、サブスクリプショングループの状態を設定できます。
{% endalert %}

## リクエストパラメーター

| パラメーター | 必須 | データ型 | 説明 |
|---|---|---|---|
| `subscription_group_id` | 必須 | 文字列 | `id` サブスクリプショングループの。|
| `subscription_state` | 必須 | 文字列 | 使用可能な値は `unsubscribed` (サブスクリプショングループ以外) または `subscribed` (サブスクリプショングループ内)。|
| `external_id` | 必須* | 文字列の配列 | 1 `external_id` 人または複数のユーザーの、最大 50 `id` 秒まで含めることができます。|
| `email` | Required* | 文字列または文字列の配列 | ユーザーの電子メールアドレスは、文字列の配列として渡すことができます。少なくとも 1 つの電子メールアドレス (最大 50) を含める必要があります。<br><br>同じワークスペースの複数のユーザー (`external_id`) が同じメールアドレスを共有している場合、そのメールアドレスを共有するすべてのユーザーは、サブスクリプショングループの変更に応じて更新されます。|
| `phone` | 必須* | [E.164形式の文字列](https://en.wikipedia.org/wiki/E.164) | ユーザーの電話番号は、文字列の配列として渡すことができます。少なくとも 1 つの電話番号 (最大 50) を含める必要があります。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

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

### SMS

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

## 成功レスポンスの例

`201`ステータスコードは次のレスポンスボディを返す可能性があります。

```json
{
    "message": "success"
}
```

{% alert important %}
エンドポイントは `email` or `phone` 値のみを受け入れ、両方は受け付けません。両方を指定すると、次の応答が返されます。 `{"message":"Either an email address or a phone number should be provided, but not both."}`
{% endalert %}

{% endapi %}

