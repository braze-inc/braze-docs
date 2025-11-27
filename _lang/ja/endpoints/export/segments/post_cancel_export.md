---
nav_title: "POST:Segmentによるエクスポートの取り消し"
article_title: "POST:Segmentによるエクスポートの取り消し"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "ここでは、Segment Braze エンドポイント別のCancelエクスポートについて説明します。"

---
{% api %}
# Segmentによるエクスポートの取り消し
{% apimethod post %}
/export/Segment/キャンセル
{% endapimethod %}

> このエンドポイントを使用すると、指定したSegment ID で実行中のすべてのエクスポートがキャンセルされます。

## 前提条件

このエンドポイントを使用するには、[API キー]({{site.baseurl}}/api/basics#rest-api-key/)と`segments.list`の権限が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## 要求本文:

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "segment_id": (required, string) the `segment_id` to locate and cancel its ongoing exports
}
```

## リクエストパラメーター

| パラメーター | required | データ型 | 説明 |
| --------- | ---------| --------- | ----------- |
| `segment_id` | 必須 | string | 実行中のエクスポートをキャンセルするには、`segment_id`を使用します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 例のリクエスト
```
curl --location --request POST 'https://rest.iad-01.braze.com/export/segment/cancel' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "segment_id": "segment_identifier"
}'
```

{% endapi %}

