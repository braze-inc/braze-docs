---
nav_title: "取得:ユーザーサブスクリプショングループを一覧表示する。"
article_title: "取得:ユーザーのサブスクリプショングループをリストする"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、リストユーザーのサブスクリプショングループBrazeエンドポイントに関する詳細を説明します。"

---
{% api %}
# ユーザーのサブスクリプショングループをリストする
{% apimethod get %}
/subscription/user/status
{% endapimethod %}

> このエンドポイントを使用して、特定のユーザーの履歴を持つサブスクリプショングループをリストアップし、取得する。

例を見たり、このエンドポイントをテストしたりする場合は、**メールサブスクリプショングループ**をご覧ください。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#d1c3b617-22f1-47bf-9ee8-499526824470 {% endapiref %}

**SMSサブスクリプショングループ**用のこのエンドポイントをテストするか例を見たい場合:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#54bd7ca8-60d9-4654-aff5-406479f3c666 {% endapiref %}

このエンドポイントの例を見たり、**WhatsAppグループ**をテストしたりする場合:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#54bd7ca8-60d9-4654-aff5-406479f3c666 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、[API キー]({{site.baseurl}}/api/basics#rest-api-key/)と`subscription.groups.get`の権限が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエストパラメーター

| パラメーター | required | データ型 | 説明 |
|---|---|---|---|
| `external_id`  | 必須 | 文字列 | ユーザーの `external_id` (少なくとも 1 つ、最大 50 の `external_ids` を含める必要があります)。 |
| `email`  |  必須* | 文字列 | ユーザーのメールアドレスは、文字列の配列として渡すことができます。少なくとも 1 件のメールアドレス (最大 50件 まで) を含める必要があります。 |
| `phone` | 必須* | [E.164](https://en.wikipedia.org/wiki/E.164)形式の文字列 | ユーザーの電話番号。少なくとも1つの電話番号を含める必要があります（最大50まで）。 |
| `limit` | オプション | 整数 | 返される結果の最大数の制限。デフォルト (および最大) の `limit` は 100 です。 |
| `offset`  |  オプション | 整数 | 検索条件に一致するテンプレートの残りを返す前にスキップするテンプレートの数。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert tip %}
同じメールアドレスを共有する複数のユーザー（複数の`external_ids`）がいる場合、すべてのユーザーは別々のユーザーとして返されます（たとえ同じメールアドレスやサブスクリプショングループを持っていても）。
{% endalert %}

## 例のリクエスト 

{% tabs %}
{% tab Multiple Users %}
{% raw %}
`https://rest.iad-03.braze.com/subscription/user/status?external_id[]=1&external_id[]=2`
{% endraw %}
{% endtab %}
{% tab SMS and WhatsApp %}
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/subscription/user/status?external_id={{external_id}}&limit=100&offset=1&phone=+11112223333' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}
{% endtab %}
{% tab Email %}
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/subscription/user/status?external_id={{external_id}}&email=example@braze.com&limit=100&offset=0' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}
{% endtab %}
{% endtabs %}

## 回答例

ユーザーの履歴にサブスクリプションステータスの更新があったサブスクリプショングループのみが、成功したレスポンスに含まれる。つまり、新しく作成されたサブスクリプショングループはリストされない。

```json
{
  "success": true,
  "subscription_groups": [
    {
      "subscription_group_id": "group_id_1",
      "subscription_status": "subscribed"
    },
    {
      "subscription_group_id": "group_id_2",
      "subscription_status": "unsubscribed"
    }
  ]
}
```

{% endapi %}
