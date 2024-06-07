---
nav_title: "取得:セグメント詳細のエクスポート"
article_title: "取得:セグメント詳細のエクスポート"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、セグメントの詳細をエクスポートする Braze エンドポイントの詳細について説明します。"

---
{% api %}
# セグメント詳細をエクスポート
{% apimethod get %}
/segments/details
{% endapimethod %}

> このエンドポイントを使用して、で識別できるセグメントの関連情報を取得します`segment_id`。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#aab56ed9-0a28-476a-8b57-b79786dbb9c1 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`segments.details`権限のある [API キーが必要です]({{site.baseurl}}/api/basics#rest-api-key/)。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエストパラメーター

| パラメーター | 必須 | データ型 | 説明 |
| ------------ | -------- | --------- | ---------------------- |
| `segment_id` | 必須 | 文字列 | [セグメント API 識別子を参照してください]({{site.baseurl}}/api/identifier_types/)。<br><br> `segment_id`特定のセグメントのは、Braze アカウントの [API キーページにあります]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/)。また、[セグメントリストのエクスポートエンドポイントを使用することもできます]({{site.baseurl}}/api/endpoints/export/segments/get_segment/)。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## リクエスト例
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/segments/details?segment_id={{segment_identifier}}' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## 応答

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
      "message": (required, string) the status of the export, returns 'success' when completed without errors,
      "created_at" : (string) the date created as ISO 8601 date,
      "updated_at" : (string) the date last updated as ISO 8601 date,
      "name" : (string) the segment name,
      "description" : (string) a human-readable description of filters,
      "text_description" : (string) the segment description, 
      "tags" : (array) the tag names associated with the segment formatted as strings,
      "teams" : (array) the names of the Teams associated with the campaign
}
```

{% alert tip %}
CSV と API のエクスポートに関するヘルプは、「[エクスポートのトラブルシューティング」を参照してください]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/)。
{% endalert %}

{% endapi %}
