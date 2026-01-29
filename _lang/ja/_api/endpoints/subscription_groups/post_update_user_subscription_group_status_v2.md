---
nav_title: "POST:ユーザーサブスクリプショングループのステータスを更新する v2"
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

> このエンドポイントを使用して、Braze ダッシュボード上で最大50ユーザーのサブスクリプション状態を一括更新します。

サブスクリプショングループの`subscription_group_id`にアクセスするには、**サブスクリプショングループ**ページに移動します。

**メールサブスクリプショングループの**例を見たり、このエンドポイントをテストするには：

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#b1b9a0e0-6329-4df2-a465-53347f410662 {% endapiref %}

**SMS サブスクリプショングループの**例を見たり、このエンドポイントをテストする：

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#81a5fe65-588b-4b61-82d8-5ce68b681409 {% endapiref %}

**WhatsApp Groups**用のエンドポイントの例を見る、またはテストする：

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#81a5fe65-588b-4b61-82d8-5ce68b681409 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`subscription.status.set` 権限を持つ[API キーが]({{site.baseurl}}/api/basics#rest-api-key/)必要である。

{% alert note %}
このエンドポイントを[LINEサブスクリプショングループで]({{site.baseurl}}/user_guide/message_building_by_channel/line/line_users/subscription_groups/)使用することに興味がある場合は、カスタマーサクセスマネージャーに連絡すること。
{% endalert %}

## V1との違い

V2エンドポイントは[V1エンド]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/)ポイントと以下の点で異なる：

- **複数のサブスクリプショングループ**：V2では、1回のAPIリクエストで複数のサブスクリプショングループを更新できるが、V1では1回のリクエストで1つのサブスクリプショングループしかサポートしない。
- **1回の通話でメールとSMSの両方を更新**：`external_ids` を使用する場合、1回のAPIコールで同じユーザーのメールとSMSの両方のサブスクリプショングループを更新することができる。V1では、メールとSMSのサブスクリプショングループ用に別々のAPIコールを行う必要がある。
- **メールや電話の識別子を使用する**こと：`external_ids` の代わりに`emails` または`phones` を使用する場合、同じリクエストでメールと SMS の両方のサブスクリプショングループを更新することはできない。メールサブスクリプショングループ用とSMSサブスクリプショングループ用に、それぞれ別のAPIコールを行う必要がある。

{% alert important %}
**電話番号の形式**電話番号は、[E.164 形式](https://en.wikipedia.org/wiki/E.164)でなければならない（例えば、`+12223334444` ）。E.164 形式でない電話番号は拒否される。
{% endalert %}

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

{% alert tip %}
[`/users/track`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)を使用して新しいユーザーを作成する場合、ユーザー属性オブジェクト内にサブスクリプショングループを設定することができ、1回のAPI呼び出しでユーザーを作成し、サブスクリプショングループの状態を設定することができます。
{% endalert %}

## リクエストパラメーター

| パラメーター | 必須 | データ型 | 説明 |
|---|---|---|---|
| [`subscription_group_id`]({{site.baseurl}}/api/identifier_types/?tab=subscription%20group%20ids) | 必須 | 文字列 | サブスクリプショングループの`id`。 |
| `subscription_state` | 必須 | 文字列 | 使用できる値は、`unsubscribed` (サブスクリプショングループに含まれない) または `subscribed` (サブスクリプショングループに含まれる) です。 |
| `external_ids` | 必須* | 文字列の配列 | ユーザーの `external_id` には、最大で50個の `id` を含めることができます。 |
| `emails` | 必須* | 文字列または文字列の配列 | ユーザーのメールアドレスは、文字列の配列として渡すことができます。少なくとも 1 件のメールアドレス (最大 50件 まで) を含める必要があります。<br><br>同じワークスペース内の複数のユーザー (`external_id`) が同じメールアドレスを共有している場合、そのメールアドレスを共有するすべてのユーザーは、サブスクリプショングループの変更で更新されます。 |
| `phones` | 必須* | [E.164](https://en.wikipedia.org/wiki/E.164)形式の文字列 | ユーザーの電話番号を文字列の配列として渡すことができる。少なくとも 1 つの電話番号を含める必要があります（最大 50 件）。電話番号は、E.164 形式でなければならない（例えば、`+12223334444` ）。<br><br>同じワークスペース内の複数のユーザー (`external_id`) が同じ電話番号を共有している場合、その電話番号を共有しているすべてのユーザーは同じ購読グループの変更で更新されます。|
| `use_double_opt_in_logic` | オプション | ブール値 | このパラメータが省略されるか、または`false` に設定された場合、ユーザーはSMSダブルオプトインワークフローに入力されない。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert important %}
**識別子を選択する**： 
- 1回のAPIコールでメールとSMSの両方のサブスクリプショングループを更新するには、`external_ids` を使用する。同じリクエストに`emails` と`phones` の両方を含めることはできない。
- `external_ids` の代わりに`emails` または`phones` を使用する場合、メールサブスクリプショングループ用と SMS サブスクリプショングループ用にそれぞれ別の API 呼び出しを行う。
- `emails` 、`phones` 、`external_ids` を個別に送ることができる。
{% endalert %}

### 例のリクエスト

以下の例では、`external_ids` 、1回のAPIコールでメールとSMSの両方のサブスクリプショングループを更新している。これは、`external_ids`を使用する場合にのみ可能である。`emails` または`phones` を使用する場合、1回の通話でメールとSMSの両方のサブスクリプショングループを更新することはできない。

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
