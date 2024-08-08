---
nav_title: "得る：ユーザーのサブスクリプショングループステータスを一覧表示する"
article_title: "得る：ユーザーのサブスクリプション グループのステータスを一覧表示する"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、リスト ユーザーのサブスクリプション グループ ステータス Braze エンドポイントの詳細について説明します。"

---
{% api %}
# ユーザーのサブスクリプション グループのステータスを一覧表示する
{% apimethod get %}
/subscription/status/get
{% endapimethod %}

> このエンドポイントを使用して、サブスクリプション グループ内のユーザーのサブスクリプション状態を取得します。

これらのグループは **、サブスクリプション グループ** ページで利用できるようになります。このエンドポイントからの応答には、API 呼び出しで要求された特定のサブスクリプション グループの外部 ID と、サブスクライブ済み、サブスクライブ解除済み、または不明のいずれかが含まれます。これを使用して、後続の API 呼び出しでサブスクリプション グループの状態を更新したり、ホストされた Web ページに表示したりできます。

**電子メールサブスクリプショングループ**の例を確認したり、このエンドポイントをテストしたりする場合は、次の手順に従ってください。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#488c8923-fa44-4124-9245-036d13c615f2 {% endapiref %}

**SMS サブスクリプション グループ**の例を確認したり、このエンドポイントをテストしたりする場合は、次の手順に従ってください。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#4b8515b8-067f-41fd-b213-8bb2d18b1557 {% endapiref %}

**WhatsApp グループ**の例を確認したり、このエンドポイントをテストしたりする場合は、次の手順に従ってください。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#4b8515b8-067f-41fd-b213-8bb2d18b1557 {% endapiref %}

## 前提条件

このエンドポイント [を]({{site.baseurl}}/api/basics#rest-api-key/) 使用するには、 `subscription.status.get` 許可。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエストパラメータ

| パラメータ | 必須 | データ型 | 説明 |
|---|---|---|---|
| `subscription_group_id`| 必須 | 文字列 | `id` サブスクリプション グループの。 |
| `external_id`| 必須* | 文字列 | `external_id` ユーザーの（少なくとも1つ、最大50個の `external_ids`）。<br><br>両方が `external_id` そして `email`/`phone` 提出された場合、 `external_id`提供された (s) は結果クエリに適用されます。 |
| `email`| 必須* | 文字列 | ユーザーの電子メール アドレス。最大 50 個の文字列の配列として渡すことができます。<br><br> メールアドレスと電話番号の両方を送信すると（ `external_id`) はエラーになります。 |
| `phone`| 必須* |[E.164](https://en.wikipedia.org/wiki/E.164) 形式の文字列 | ユーザーの電話番号。電子メールが含まれていない場合は、少なくとも 1 つの電話番号 (最大 50 個) を含める必要があります。<br><br> メールアドレスと電話番号の両方を送信すると（ `external_id`) はエラーになります。 |

{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

\*の一つ `external_id` または `email` または `phone` 各ユーザーごとに必要です。

- SMSおよびWhatsAppサブスクリプショングループの場合、 `external_id` または `phone` が必要です。 両方提出した場合、 `external_id` クエリに使用され、電話番号がそのユーザーに適用されます。
- メール購読グループの場合、 `external_id` または `email` が必要です。 両方提出した場合、 `external_id` クエリに使用され、そのユーザーに電子メール アドレスが適用されます。

## リクエスト例 

{% tabs %}
{% tab Multiple Users %}
{% raw %}
```
https://rest.iad-03.braze.com/subscription/status/get?subscription_group_id={{subscription_group_id}}&external_id[]=1&external_id[]=2
```
{% endraw %}
{% endtab %}
{% tab SMS and WhatsApp %}
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/subscription/status/get?subscription_group_id={{subscription_group_id}}&phone=+11112223333' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}
{% endtab %}
{% tab Email %}
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/subscription/status/get?subscription_group_id={{subscription_group_id}}&email=example@braze.com' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}
{% endtab %}
{% endtabs %}

## 応答

成功した応答はすべて返されます `Subscribed`、 `Unsubscribed`、 または `Unknown` サブスクリプション グループのステータスとユーザー履歴に応じて異なります。

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "status": {
    "1": "Unsubscribed",
    "2": "Subscribed"
  },
  "message": "success"
}
```

{% endapi %}
