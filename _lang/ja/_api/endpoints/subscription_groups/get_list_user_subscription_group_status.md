---
nav_title: "取得:ユーザのサブスクリプショングループステータスの一覧表示"
article_title: "取得:ユーザのサブスクリプショングループのステータスの一覧表示"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "本稿では、List ユーザー のサブスクリプショングループ ステータス Braze エンドポイントの概要について説明します。"

---
{% api %}
# ユーザーのサブスクリプショングループ ステータスの一覧表示
{% apimethod get %}
/subscription/status/get
{% endapimethod %}

> このエンドポイントを使用して、サブスクリプショングループ内のユーザーのサブスクリプションステートを取得します。

これらのグループは、**サブスクリプショングループ**ページで使用できます。このエンドポイントからの応答には、外部ID と、API 呼び出しで要求された固有のサブスクリプショングループの配信登録済み、配信停止済み、または不明のいずれかが含まれます。これは、後続のAPI 呼び出しでサブスクリプショングループステートを更新したり、ホストWeb ページに表示したりするために使用できます。

**メールサブスクリプショングループ**のサンプルまたはテストエンドポイントを表示する場合:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#488c8923-fa44-4124-9245-036d13c615f2 {% endapiref %}

**SMS Subscription Groups** のサンプルまたはテストエンドポイントを表示する場合:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#4b8515b8-067f-41fd-b213-8bb2d18b1557 {% endapiref %}

** WhatsApp Groups** のサンプルまたはテストエンドポイントを表示するには:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#4b8515b8-067f-41fd-b213-8bb2d18b1557 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`subscription.status.get` 権限を持つ[API キー]({{site.baseurl}}/api/basics#rest-api-key/) が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエストパラメーター

| パラメータ | required | データ型 | 説明 |
|---|---|---|---|
| [`subscription_group_id`]({{site.baseurl}}/api/identifier_types/?tab=subscription%20group%20ids)  | required | string | サブスクリプショングループの`id`。 |
| `external_id`  |  必須* | string | ユーザーの `external_id` (少なくとも 1 つ、最大 50 の `external_ids` を含める必要があります)。<br><br>`external_id` と `email`/`phone` の両方が送信されると、指定された `external_id` (s) のみが結果クエリに適用されます。 |
| `email` | 必須* | string | ユーザーのメールアドレス。これは、最大50個の文字列の配列として渡すことができます。<br><br> メールアドレスと電話番号(`external_id` なし)の両方をサブミットすると、エラーが発生します。 |
| `phone` | 必須* | [E.164](https://en.wikipedia.org/wiki/E.164)形式の文字列 | ユーザーの電話番号。メールが含まれていない場合は、少なくとも1 つの電話番号を含める必要があります(最大50)。<br><br> メールアドレスと電話番号 (`external_id` なし) の両方を送信すると、エラーが発生します。 |

{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

\* ユーザーごとに`external_id` または`email` または`phone` のいずれかが必要です。

- SMS およびWhatsApp サブスクリプショングループ s の場合、`external_id` または`phone` のいずれかが必要です。 両方が送信されると、`external_id` のみがクエリに使用され、電話番号はそのユーザーに適用されます。
- メール サブスクリプショングループs の場合、`external_id` または`email` のいずれかが必要です。 両方が送信されると、`external_id` のみがクエリに使用され、メールアドレスはそのユーザーに適用されます。

## リクエスト例 

{% tabs %}
{% tab 複数のユーザー %}
{% raw %}
```
https://rest.iad-03.braze.com/subscription/status/get?subscription_group_id={{subscription_group_id}}&external_id[]=1&external_id[]=2
```
{% endraw %}
{% endtab %}
{% tab SMSとWhatsApp %}
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/subscription/status/get?subscription_group_id={{subscription_group_id}}&phone=+11112223333' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}
{% endtab %}
{% tab メール %}
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/subscription/status/get?subscription_group_id={{subscription_group_id}}&email=example@braze.com' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}
{% endtab %}
{% endtabs %}

## 応答

すべての成功したレスポンスは、サブスクリプショングループのステータスとユーザー履歴に応じて、`Subscribed`、`Unsubscribed`、または`Unknown` を返します。

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
