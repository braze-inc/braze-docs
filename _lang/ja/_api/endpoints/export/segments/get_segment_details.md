---
nav_title: "取得:セグメントの詳細をエクスポート"
article_title: "取得:セグメントの詳細のエクスポート"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "この記事では、「セグメントの詳細をエクスポート」Braze エンドポイントの詳細について説明します。"

---
{% api %}
# セグメントの詳細をエクスポート
{% apimethod get %}
/segments/details
{% endapimethod %}

> このエンドポイントを使用して、`segment_id` で識別できるセグメントの関連情報を取得します。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#aab56ed9-0a28-476a-8b57-b79786dbb9c1 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、[API キー]({{site.baseurl}}/api/basics#rest-api-key/)と`segments.details`の権限が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエストパラメーター

| パラメーター    | required | データ型 | 説明            |
| ------------ | -------- | --------- | ---------------------- |
| `segment_id` | 必須 | 文字列 | [セグメントAPI 識別子]({{site.baseurl}}/api/identifier_types/)を参照してください。<br><br> 特定のSegmentの`segment_id` は、Braze アカウントの[API Keys]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/) ページにあります。または、[エクスポートSegment一覧エンドポイント]({{site.baseurl}}/api/endpoints/export/segments/get_segment/) を使用できます。  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 例のリクエスト
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/segments/details?segment_id={{segment_identifier}}' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## 応答

```json
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
CSV および API のエクスポートに関するヘルプについては、「[エクスポートのトラブルシューティング]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/)」を参照してください。
{% endalert %}

{% endapi %}
