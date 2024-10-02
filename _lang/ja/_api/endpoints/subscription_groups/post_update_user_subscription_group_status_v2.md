---
nav_title: "POST:ユーザーのサブスクリプション・グループ・ステータスを更新する V2"
alias: /post_update_user_subscription_group_status_v2/
layout: api_page
page_type: reference
description: "この記事では、「ユーザーのサブスクリプショングループステータスの更新」Braze V2エンドポイントの詳細について説明します。"

platform: API
channel:
  - Email
---

{% api %}
# ユーザーのサブスクリプショングループステータスの更新 (V2)
{% apimethod post %}
/v2/subscription/status/set
{% endapimethod %}

> このエンドポイントを使用して、Brazeダッシュボード上の最大50ユーザーのサブスクリプション状態を一括更新する。 

**サブスクリプショングループ**ページに移動すると、サブスクリプショングループの `subscription_group_id` にアクセスできます。

**メールサブスクリプショングループ**に対してこのエンドポイントをテストしたり、例を見たりしたい場合：

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#b1b9a0e0-6329-4df2-a465-53347f410662 {% endapiref %}

**SMSサブスクリプション・グループの**例を見たい、またはこのエンドポイントをテストしたい場合：

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#81a5fe65-588b-4b61-82d8-5ce68b681409 {% endapiref %}

**WhatsApp Groups**用のエンドポイントの例を見たい、またはテストしたい：

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#81a5fe65-588b-4b61-82d8-5ce68b681409 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`subscription.status.set` 権限を持つ [API キー]({{site.baseurl}}/api/basics#rest-api-key/)が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='subscription status set' %}

## Request body

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "subscription_groups":[
    {
      "subscription_group_id": (required, string),
      "subscription_state": (required, string)
      "external_ids": (required*, array of strings),
      "emails": (required*, array of strings),
      "phones": (required*, array of strings in E.164 format),
    }
  ]
}
```
*`emails` と `phones` の両方のパラメーターを含めることはできません。また、`emails`、`phones`、`external_ids` はすべて個別に送信できます。

{% alert tip %}
[`/users/track` エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)経由で新規ユーザーを作成する際、ユーザー属性オブジェクト内にサブスクリプショングループを設定することができる。これにより、1回のAPIコールでユーザーを作成し、サブスクリプショングループの状態を設定することができる。
{% endalert %}

## リクエストパラメーター

| パラメーター | required | データ型 | 説明 |
|---|---|---|---|
| [`subscription_group_id`]({{site.baseurl}}/api/identifier_types/?tab=subscription%20group%20ids) | required | string | サブスクリプション・グループの`id` 。 |
| `subscription_state` | 必須 | string | 使用できる値は、`unsubscribed` (サブスクリプショングループに含まれない) または `subscribed` (サブスクリプショングループに含まれる) です。 |
| `external_ids` | 必須 | 文字列の配列 | ユーザーの `external_id` には、最大で50個の `id` を含めることができます。 |
| `emails` | 必須 | 文字列または文字列の配列 | ユーザーのメールアドレス。文字列の配列として渡すことができます。少なくとも1件のメールアドレス (最大50件まで) を含める必要があります。<br><br>同じワークスペース内の複数のユーザー (`external_id`) が同じメールアドレスを共有している場合、そのメールアドレスを共有するすべてのユーザーは、サブスクリプショングループの変更で更新されます。 |
| `phones` | 必須 | 文字列 [E.164](https://en.wikipedia.org/wiki/E.164)形式 | ユーザーの電話番号。文字列の配列として渡すことができます。少なくとも1件の電話番号 (最大50件まで) を含める必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

{% alert note %}
*`emails` と `phones` の両方のパラメーターを含めることはできません。また、`emails`、`phones`、`external_ids` はすべて個別に送信できます。
{% endalert %}

### リクエスト例

以下の例では、`external_id` を使って、EメールとSMSのAPIコールを1回行っている。

```
curl --location --request POST 'https://rest.iad-01.braze.com/v2/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "subscription_groups":[
    {
      "subscription_group_id":"subscription_group_identifier",
      "subscription_state":"subscribed",
      "external_ids":["example-user","example1@email.com"]
    },
    {
      "subscription_group_id":"subscription_group_identifier",
      "subscription_state":"subscribed",
      "external_ids":["example-user","example1@email.com"]
    }
  ]
}
```

## メール

```
curl --location --request POST 'https://rest.iad-01.braze.com/v2/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "subscription_groups":[
    {
      "subscription_group_id":"subscription_group_identifier",
      "subscription_state":"subscribed",
      "emails":["example1@email.com","example2@email.com"]
    }
  ]
}
'
```

## SMSとWhatsApp

```
curl --location --request POST 'https://rest.iad-01.braze.com/v2/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "subscription_groups":[
    {
      "subscription_group_id":"subscription_group_identifier",
      "subscription_state":"subscribed",
      "phones":["+12223334444","+15556667777"]
    }
  ]
}
'
```

{% endapi %}
