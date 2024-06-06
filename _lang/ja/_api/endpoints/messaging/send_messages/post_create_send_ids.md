---
nav_title: "ポスト:送信IDの作成"
article_title: "ポスト:送信IDの作成"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、Create send IDs Braze エンドポイントの詳細について説明します。"

---
{% api %}
# 送信ID の作成
{% apimethod post %}
/sends/id/create
{% endapimethod %}

> このエンドポイントを使用して、メッセージの送信に使用できる送信ID を作成し、送信ごとにキャンペーンを作成せずにプログラムでメッセージパフォーマンスを追跡します。 

メッセージの追跡と送信に送信識別子を使用すると、プログラムでコンテンツを生成および送信する場合に便利です。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#74a04e53-659f-4473-abc5-0f6f735550ff {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`sends.id.create` 権限を持つAPI キーを生成する必要があります。

## レート制限

{% multi_lang_include rate_limits.md endpoint='sends id create' %}

## リクエスト本文

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "campaign_id": (required, string) see campaign identifier,
  "send_id": (optional, string) see send identifier
}
```

## 要求パラメータ

| パラメータ| 必須| データ型| 説明|
| --------- | ---------| --------- | ----------- |
| `campaign_id` | 必須| 文字列| [キャンペーン識別子]({{site.baseurl}}/api/identifier_types/) を参照|
|`send_id`| オプション| 文字列| [送信識別子]({{site.baseurl}}/api/identifier_types/)を参照|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## リクエスト例
```
curl --location --request POST 'https://rest.iad-01.braze.com/sends/id/create' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "campaign_id": "campaign_identifier",
  "send_id": "send_identifier"
}'
```

## レスポンス

### 成功応答の例

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "message": "success",
  "send_id" : (string) the send identifier
}
```

{% endapi %}
