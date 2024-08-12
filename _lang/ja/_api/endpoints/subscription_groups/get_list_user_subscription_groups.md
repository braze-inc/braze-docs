---
nav_title: "GET：ユーザーの購読グループをリストする"
article_title: "GET：ユーザーの購読グループをリストする"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "List user's subscription groups Brazeエンドポイントの詳細について説明します。"

---
{% api %}
# ユーザーの購読グループ一覧
{% apimethod get %}
/subscription/user/status
{% endapimethod %}

> このエンドポイントを使用して、特定のユーザーのサブスクリプショングループをリストアップし、取得します。

**電子メール購読**グループの例を参照したり、このエンドポイントをテストしたい場合：

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#d1c3b617-22f1-47bf-9ee8-499526824470 {% endapiref %}

**SMS サブスクリプション・グループの**例を参照したり、このエンドポイントをテストしたい場合：

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#54bd7ca8-60d9-4654-aff5-406479f3c666 {% endapiref %}

**WhatsApp Groups**用のエンドポイントの例やテストをご覧になりたい場合は、こちらをクリックしてください：

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#54bd7ca8-60d9-4654-aff5-406479f3c666 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`subscription.groups.get` パーミッションを持つ[API キーが]({{site.baseurl}}/api/basics#rest-api-key/)必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエストパラメータ

| パラメータ｜必須｜データ型｜説明
|---|---|---|---|
|`external_id` | 必須 | String | ユーザーの`external_id` (最低1つ、最大50`external_ids` を含む必要がある)。|
|`email` | Required* | String | ユーザーのメールアドレス。文字列の配列として渡すことができます。少なくとも1つのEメールアドレスを含むこと（最大50個まで）。|
|`phone` ｜必須*｜[E.164](https://en.wikipedia.org/wiki/E.164)形式の文字列｜ユーザーの電話番号。少なくとも1つの電話番号を含むこと（最大50）。|
|`limit` ｜オプション｜整数｜返される結果の最大数の制限。デフォルト（最大）`limit` は100。|
|`offset` ｜任意｜整数｜検索条件に合う残りのテンプレートを返す前にスキップするテンプレートの数。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

{% alert tip %}
同じメールアドレスを共有する複数のユーザー（複数の`external_ids` ）が存在する場合、すべてのユーザーは別々のユーザーとして返されます（同じメールアドレスまたは購読グループを持っていても）。
{% endalert %}

## リクエスト例 

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
{% endapi %}
