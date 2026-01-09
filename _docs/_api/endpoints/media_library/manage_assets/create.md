---
nav_title: "POST: Upload an asset to the media library"
article_title: "POST: Upload an asset to the media library"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "This article outlines details about the `POST /media_library/create` endpoint."
---

{% api %}
# Upload an asset to the media library
{% apimethod post %}
/media_library/create
{% endapimethod %}

> Use this endpoint to add an asset to the Braze media library from an externally hosted URL

{% alert important %}
It is not currently possible to upload a binary file via API. This endpoint requires an externally hosted URL as the source.
{% endalert %}

## Prerequisites

To use this endpoint, you'll need an [API key]({{site.baseurl}}/api/basics#rest-api-key/) with the `media_library.create` permission.

## Rate limit

{% multi_lang_include rate_limits.md endpoint='media library' %}

## Query parameters

| Parameter | Required | Data Type | Description |
| --------- | ---------| --------- | ----------- |
|`asset_url`| Required | String | A publicly accessible URL for the asset to be uploaded into Braze. |
|`name`| Required | String | A name to appear in the media library for this asset. |
|`app_group_id`| Required | String | The workspace (app_group_id) identifier to upload into. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Example request

```
curl -X POST --location 'http://api.dashboard-03.braze.com/media_library/create' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--header 'Content-Type: application/json' \
--data '{"asset_url": "https://cdn.example.com/assets/cat.jpg", "name": "Cat Graphic", "app_group_id": "APP_GROUP_ID"}'
```

## Response

There are four status code responses for this endpoint: `200`, `400`, `404`, and `429`.

{% endapi %}
