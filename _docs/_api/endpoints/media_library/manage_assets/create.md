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

> Use this endpoint to add an asset to the [Braze media library](https://www.braze.com/docs/user_guide/engagement_tools/templates_and_media/media_library) using either an externally hosted URL (`asset_url`) or binary file data sent in the request body (`asset_file`). This endpoint supports images and ZIP files that contain images.

## Prerequisites

To use this endpoint, you'll need an [API key]({{site.baseurl}}/api/basics#rest-api-key/) with the `media_library.create` permission.

## Rate limit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Request body

When you include `asset_url`, the endpoint downloads the file from the URL. When you include `asset_file`, the endpoint uses the binary data in the request body.

Example request body for `asset_url`:

```json
{
  "asset_url": "https://cdn.example.com/assets/cat.jpg",
  "name": "Cat Graphic"
}
```

Example request body for `asset_file`:

```json
{
  "asset_file": <BINARY FILE DATA>,
  "name": "Cat Graphic"
}
```

The request body includes the following parameters:

| Parameter | Required | Data Type | Description |
| --------- | -------- | --------- | ----------- |
| `asset_url` | Optional | String | A publicly accessible URL for the asset to be uploaded into Braze. |
| `asset_file` | Optional | Binary | Binary file data. |
| `name` | Optional | String | A name to appear in the media library for this asset. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert important %}
`asset_url` and `asset_file` are mutually exclusive, you must only include one of them in your API request.
{% endalert %}

### Uploaded file names

This section explains how the endpoint assigns names to uploaded files based on whether you include the `name` parameter.

#### Single file uploads

| Scenario | Result |
| --- | --- |
| `name` provided | The `name` value is used as the asset name in the media library. |
| `name` excluded | The original filename from the URL or uploaded file is used. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" style="table-layout: fixed; width: 100%;" }

#### ZIP file uploads

| Scenario | Result |
| --- | --- |
| `name` provided | The `name` value is used as a prefix, with an incrementing number appended as a suffix (for example, "My File 1", "My File 2", "My File 3"). |
| `name` excluded | Each file retains its original filename from within the ZIP file. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" style="table-layout: fixed; width: 100%;" }

## Example request

This section includes two example `curl` requests, one for adding an asset using a URL and another using binary file data.

This request shows an example of adding an asset to the media library using an `asset_url`.

```
curl -X POST --location 'http://api.dashboard-03.braze.com/media_library/create' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--header 'Content-Type: application/json' \
--data '{"asset_url": "https://cdn.example.com/assets/cat.jpg", "name": "Cat Graphic"}'
```

This request shows an example of adding an asset to the media library using an `asset_file`.

```
curl -X POST --location 'http://api.dashboard-03.braze.com/media_library/create' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--header 'Content-Type: application/json' \
--data '{"asset_file":<BINARY FILE DATA>, "name":"Cat Graphic"}'
```

### Error responses

This section lists potential errors and their corresponding messages and descriptions. 

#### Validation errors

Validation errors return a structure like this:

```json
{
  "message": (String) Human-readable error description
}
```

This table lists possible validation errors.

| HTTP Status | Message | Description |
| --- | --- | --- |
| 400 | "Either asset_url or asset_file must be provided." | No asset parameter was provided in the request. |
| 400 | "Both asset_url and asset_file cannot be provided. Please provide only one." | Both asset parameters were provided; only one is allowed. |
| 403 | "Media Library Public APIs are not enabled for this company." | Media library feature is not enabled for this workspace. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

#### Processing errors

Processing errors return a different response with error codes:

```json
{
  "message": (String) Human-readable error description,
  "error_code": (String) error code,
  "meta": { }
}
```

This table lists possible processing errors.

| Error Code | HTTP Status | Description |
| --- | --- | --- |
| `UNSUPPORTED_FILE_TYPE` | 400 | The uploaded file type is not supported. The `meta` object includes the `file_type` that was rejected. |
| `ASSET_SIZE_EXCEEDS_LIMIT` | 400 | The file exceeds the maximum allowed size. Images have a 5 MB limit. |
| `MEDIA_LIBRARY_LIMIT_REACHED` | 400 | The workspace has reached its maximum number of assets (200 by default for free trial companies, unlimited otherwise). The `meta` object includes the current `limit`. |
| `ASSET_UPLOAD_FAILED` | 400 | The asset failed to upload due to processing issues. |
| `GENERIC_ERROR` | 500 | An unexpected error occurred during upload. The `meta` object includes the `original_error` message for debugging. Try again or contact [Support]({{site.baseurl}}/support_contact/). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


## Response

There are five status code responses for this endpoint: `200`, `400`, `403`, `429`, and `500`.

The following JSON shows the expected shape of the response.

```json
{ 
    "new_assets": [
        {
            "name": (String) the name of the asset,
            "size": (Integer) the byte size of the asset,
            "url": (String) the URL to access the asset,
            "ext": (String) the file extension (e.g., "png", "jpg", "gif")
        }
    ],
    "errors": [
        {
            "name": (String) the name of the asset,
            "size": (Integer) the byte size of the asset,
            "ext": (String) the file extension (e.g., "png", "jpg", "gif"),
            "error": (String) the error that occurred
        }
    ],
    "dashboard_url": (String) the URL to view this asset in the Braze dashboard
}
```

{% endapi %}
