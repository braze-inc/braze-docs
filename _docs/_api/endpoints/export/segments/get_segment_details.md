---
nav_title: "GET: Segment Details"
page_order: 4

layout: api_page

page_type: reference
platform: API
tool: Segments
description: "This article outlines details about and using the Segments Details endpoint to export a list of available Segments."
---
{% api %}
# Segment Details Endpoint
{% apimethod get %}
/segments/details
{% endapimethod %}

This endpoint allows you to retrieve relevant information on the segment, which can be identified by the `segment_id`.

{% apiref swagger %}https://www.braze.com/docs/api/interactive/#/Export/Segment%20export%20%20details%20example {% endapiref %}
{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#aab56ed9-0a28-476a-8b57-b79786dbb9c1 {% endapiref %}

## Parameters

| Parameter    | Required | Data Type | Description            |
| ------------ | -------- | --------- | ---------------------- |
| `api_key`    | Yes      | String    | App Group REST API Key |
| `segment_id` | Yes      | String    | Segment API Identifier |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

{% alert tip %}
The `segment_id` for a given segment can be found in your Developer Console within your Braze account or you can use the [Segment List Endpoint](#segment-list).
{% endalert %}

## Example URL
`https://rest.iad-01.braze.com/segments/details?api_key=75480f9a-4db8-4057-8b7e-4d59bfd73709&segment_id=3bbc4555-8fa0-4c9b-a5c0-4505edf3e064`

## Response

```json
Content-Type: application/json
{
      "message": (required, string) the status of the export, returns 'success' when completed without errors,
      "created_at" : (string) date created as ISO 8601 date,
      "updated_at" : (string) date last updated as ISO 8601 date,
      "name" : (string) segment name,
      "description" : (string) human-readable description of filters,
      "tags" : (array) tag names associated with the segment
}
```
{% endapi %}
