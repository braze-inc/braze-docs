---
nav_title: "ポスト:ユーザーのサブスクリプション グループの状態の更新 v2"
alias: /post_update_user_subscription_group_status_v2/
layout: api_page
page_type: reference
description: "この記事では、Update user's subscription group status Braze V2エンドポイントの詳細について説明します。"

platform: API
channel:
  - Email
---

{% api %}
# ユーザーのサブスクリプション グループの状態を更新する (V2)
{% apimethod post %}
/v2/subscription/status/set
{% endapimethod %}

> このエンドポイントを使用して、Brazeダッシュボードで最大50人のユーザーのサブスクリプション状態を一括更新します。 

サブスクリプション グループ `subscription_group_id` にアクセスするには、[ **サブスクリプション グループ** ] ページに移動します。

例を参照したり、このエンドポイントを **メールサブスクリプショングループ**でテストしたりする場合は、次のようにします。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#b1b9a0e0-6329-4df2-a465-53347f410662 {% endapiref %}

**SMS サブスクリプション グループ**についてこのエンドポイントの例を参照またはテストする場合は、次のようにします。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#81a5fe65-588b-4b61-82d8-5ce68b681409 {% endapiref %}

**WhatsApp Groups**でこのエンドポイントの例を確認したり、テストしたりする場合は、次のようにします。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#81a5fe65-588b-4b61-82d8-5ce68b681409 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、アクセス許可を持つ `subscription.status.set` [API キー]({{site.baseurl}}/api/basics#rest-api-key/)が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='subscription status set' %}

## リクエスト本文

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
\* と`phones`パラメータの両方`emails`を含めることはできませんのでご注意ください。また、`emails`、 `phones``external_ids`

{% alert tip %}
エンドポイントを介して[`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)新しいユーザーを作成する場合、ユーザー属性オブジェクト内にサブスクリプション グループを設定できるため、1 回の API 呼び出しでユーザーを作成し、サブスクリプション グループの状態を設定できます。
{% endalert %}

## 要求パラメーター

|パラメータ |必須項目 |データ型 |説明 |
|---|---|---|---|
|`subscription_group_id` |必須項目 |文字列 |サブスクリプション グループの |`id`
| `subscription_state` |必須項目 |文字列 |使用可能な値は、(サブスクリプション グループ内にない) または (サブスクリプション グループ内) です `unsubscribed` `subscribed` 。 |
| `external_ids` |必須項目* |文字列の配列 |ユーザー `external_id` またはユーザーの、最大50 `id`秒を含み得る。 |
| `emails` |必須項目* |文字列または文字列の配列 |ユーザーのメールアドレスは、文字列の配列として渡すことができます。少なくとも 1 つのメール アドレス (最大 50 個) を含める必要があります。<br><br>同じワークスペース内の複数のユーザー ()`external_id` が同じメール アドレスを共有している場合、メール アドレスを共有するすべてのユーザーは、サブスクリプション グループの変更で更新されます。 |
| `phones` |必須項目* | [E.164](https://en.wikipedia.org/wiki/E.164) 形式の文字列 |ユーザーの電話番号は、文字列の配列として渡すことができます。少なくとも 1 つの電話番号 (最大 50 個) を含める必要があります。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

{% alert note %}
パラメーター`phones`とパラメーターの両方`emails`を含めることはできません。また、`emails`、 `phones``external_ids`
{% endalert %}

### 要求の例

次の例では、を使用して `external_id` 、メールと SMS の API 呼び出しを 1 回行います。

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
