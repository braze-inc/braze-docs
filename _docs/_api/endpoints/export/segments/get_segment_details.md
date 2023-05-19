---
nav_title: "GET: Export Segment Details"
article_title: "GET: Export Segment Details"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "This article outlines details about the Export segment details Braze endpoint."

---
{% api %}
# Export segment details
{% apimethod get %}
/segments/details
{% endapimethod %}

> Use this endpoint to retrieve relevant information on a segment, which can be identified by the `segment_id`.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#aab56ed9-0a28-476a-8b57-b79786dbb9c1 {% endapiref %}

## Rate limit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Request parameters

| Parameter    | Required | Data Type | Description            |
| ------------ | -------- | --------- | ---------------------- |
| `segment_id` | Required | String | See [Segment API identifier]({{site.baseurl}}/api/identifier_types/).<br><br> The `segment_id` for a given segment can be found at **Developer Console** > **API Settings** within your Braze account or you can use the [Export segment list endpoint]({{site.baseurl}}/api/endpoints/export/segments/get_segment/).  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

{% alert note %}
If you are using our [updated navigation]({{site.baseurl}}/navigation), **API Settings** is now **API Keys** and can be found at **Settings** > **Setup and Testing** > **API Keys**.
{% endalert %}

## Example request
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/segments/details?segment_id={{segment_identifier}}' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## Response

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
      "tags" : (array) the tag names associated with the segment formatted as strings
}
```

{% alert tip %}
For help with CSV and API exports, visit [Export troubleshooting]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
