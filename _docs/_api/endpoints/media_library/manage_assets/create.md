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

<table class="reset-td-br-1 reset-td-br-2 reset-td-br-3 reset-td-br-4" role="presentation" style="word-break: normal; overflow-wrap: normal; table-layout: fixed; width: 100%;">
  <colgroup>
    <col style="width: 20%;">
    <col style="width: 15%;">
    <col style="width: 15%;">
    <col style="width: 50%;">
  </colgroup>
  <thead>
    <tr>
      <th style="text-align: center;">Parameter</th>
      <th style="text-align: center;">Required</th>
      <th style="text-align: center;">Data Type</th>
      <th style="text-align: center;">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>asset_url</code></td>
      <td>Optional</td>
      <td>String</td>
      <td>A publicly accessible URL for the asset to be uploaded into Braze.</td>
    </tr>
    <tr>
      <td><code>asset_file</code></td>
      <td>Optional</td>
      <td>Binary</td>
      <td>Binary file data.</td>
    </tr>
    <tr>
      <td><code>name</code></td>
      <td>Optional</td>
      <td>String</td>
      <td>A name to appear in the media library for this asset.</td>
    </tr>
  </tbody>
</table>

{% alert important %}
`asset_url` and `asset_file` are mutually exclusive, you must only include one of them in your API request.
{% endalert %}

### Uploaded file names

This section explains how the endpoint assigns names to uploaded files based on whether you include the `name` parameter.

#### Single file uploads

<table style="word-break: normal; overflow-wrap: normal; word-wrap: normal; hyphens: none; table-layout: fixed; width: 100%;">
  <colgroup>
    <col style="width: 35%;">
    <col style="width: 65%;">
  </colgroup>
  <thead>
    <tr>
      <th style="word-break: normal; overflow-wrap: normal; word-wrap: normal; white-space: normal; hyphens: none; text-align: center;">Scenario</th>
      <th style="word-break: normal; overflow-wrap: normal; word-wrap: normal; white-space: normal; hyphens: none; text-align: center;">Result</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="word-break: normal; overflow-wrap: normal; word-wrap: normal; white-space: normal; hyphens: none;"><code>name</code> parameter provided</td>
      <td style="word-break: normal; overflow-wrap: normal; word-wrap: normal; white-space: normal; hyphens: none;">The <code>name</code> value is used as the asset name in the media library.</td>
    </tr>
    <tr>
      <td style="word-break: normal; overflow-wrap: normal; word-wrap: normal; white-space: normal; hyphens: none;"><code>name</code> parameter excluded</td>
      <td style="word-break: normal; overflow-wrap: normal; word-wrap: normal; white-space: normal; hyphens: none;">The original filename from the URL or uploaded file is used.</td>
    </tr>
  </tbody>
</table>

#### ZIP file uploads

<table style="word-break: normal; overflow-wrap: normal; word-wrap: normal; hyphens: none; table-layout: fixed; width: 100%;">
  <colgroup>
    <col style="width: 35%;">
    <col style="width: 65%;">
  </colgroup>
  <thead>
    <tr>
      <th style="word-break: normal; overflow-wrap: normal; word-wrap: normal; white-space: normal; hyphens: none; text-align: center;">Scenario</th>
      <th style="word-break: normal; overflow-wrap: normal; word-wrap: normal; white-space: normal; hyphens: none; text-align: center;">Result</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="word-break: normal; overflow-wrap: normal; word-wrap: normal; white-space: normal; hyphens: none;"><code>name</code> parameter provided</td>
      <td style="word-break: normal; overflow-wrap: normal; word-wrap: normal; white-space: normal; hyphens: none;">The <code>name</code> value is used as a prefix, with an incrementing number appended as a suffix (for example, "My File 1", "My File 2", "My File 3").</td>
    </tr>
    <tr>
      <td style="word-break: normal; overflow-wrap: normal; word-wrap: normal; white-space: normal; hyphens: none;"><code>name</code> parameter excluded</td>
      <td style="word-break: normal; overflow-wrap: normal; word-wrap: normal; white-space: normal; hyphens: none;">Each file retains its original filename from within the ZIP file.</td>
    </tr>
  </tbody>
</table>

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

<table style="word-break: normal; overflow-wrap: normal; table-layout: fixed; width: 100%;">
  <colgroup>
    <col style="width: 15%;">
    <col style="width: 35%;">
    <col style="width: 50%;">
  </colgroup>
  <thead>
    <tr>
      <th style="word-break: normal; overflow-wrap: normal; white-space: normal; text-align: center;">HTTP Status</th>
      <th style="word-break: normal; overflow-wrap: normal; white-space: normal; text-align: center;">Message</th>
      <th style="word-break: normal; overflow-wrap: normal; white-space: normal; text-align: center;">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="word-break: normal; overflow-wrap: normal; white-space: normal;">400</td>
      <td style="word-break: normal; overflow-wrap: normal; white-space: normal;">"Either asset_url or asset_file must be provided."</td>
      <td style="word-break: normal; overflow-wrap: normal; white-space: normal;">No asset parameter was provided in the request.</td>
    </tr>
    <tr>
      <td style="word-break: normal; overflow-wrap: normal; white-space: normal;">400</td>
      <td style="word-break: normal; overflow-wrap: normal; white-space: normal;">"Both asset_url and asset_file cannot be provided. Please provide only one."</td>
      <td style="word-break: normal; overflow-wrap: normal; white-space: normal;">Both asset parameters were provided; only one is allowed.</td>
    </tr>
    <tr>
      <td style="word-break: normal; overflow-wrap: normal; white-space: normal;">403</td>
      <td style="word-break: normal; overflow-wrap: normal; white-space: normal;">"Media Library Public APIs are not enabled for this company."</td>
      <td style="word-break: normal; overflow-wrap: normal; white-space: normal;">Media library feature is not enabled for this workspace.</td>
    </tr>
  </tbody>
</table>

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

<table style="word-break: normal; overflow-wrap: normal; table-layout: fixed; width: 100%;">
  <colgroup>
    <col style="width: 30%;">
    <col style="width: 15%;">
    <col style="width: 55%;">
  </colgroup>
  <thead>
    <tr>
      <th style="word-break: normal; overflow-wrap: normal; white-space: normal; text-align: center;">Error Code</th>
      <th style="word-break: normal; overflow-wrap: normal; white-space: normal; text-align: center;">HTTP Status</th>
      <th style="word-break: normal; overflow-wrap: normal; white-space: normal; text-align: center;">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="word-break: normal; overflow-wrap: normal; white-space: normal;"><code>UNSUPPORTED_FILE_TYPE</code></td>
      <td style="word-break: normal; overflow-wrap: normal; white-space: normal;">400</td>
      <td style="word-break: normal; overflow-wrap: normal; white-space: normal;">The uploaded file type is not supported. The <code>meta</code> object includes the <code>file_type</code> that was rejected.</td>
    </tr>
    <tr>
      <td style="word-break: normal; overflow-wrap: normal; white-space: normal;"><code>ASSET_SIZE_EXCEEDS_LIMIT</code></td>
      <td style="word-break: normal; overflow-wrap: normal; white-space: normal;">400</td>
      <td style="word-break: normal; overflow-wrap: normal; white-space: normal;">The file exceeds the maximum allowed size. Images have a 5 MB limit.</td>
    </tr>
    <tr>
      <td style="word-break: normal; overflow-wrap: normal; white-space: normal;"><code>MEDIA_LIBRARY_LIMIT_REACHED</code></td>
      <td style="word-break: normal; overflow-wrap: normal; white-space: normal;">400</td>
      <td style="word-break: normal; overflow-wrap: normal; white-space: normal;">The workspace has reached its maximum number of assets (200 by default for free trial companies, unlimited otherwise). The <code>meta</code> object includes the current <code>limit</code>.</td>
    </tr>
    <tr>
      <td style="word-break: normal; overflow-wrap: normal; white-space: normal;"><code>ASSET_UPLOAD_FAILED</code></td>
      <td style="word-break: normal; overflow-wrap: normal; white-space: normal;">400</td>
      <td style="word-break: normal; overflow-wrap: normal; white-space: normal;">The asset failed to upload due to processing issues.</td>
    </tr>
    <tr>
      <td style="word-break: normal; overflow-wrap: normal; white-space: normal;"><code>GENERIC_ERROR</code></td>
      <td style="word-break: normal; overflow-wrap: normal; white-space: normal;">500</td>
      <td style="word-break: normal; overflow-wrap: normal; white-space: normal;">An unexpected error occurred during upload. The <code>meta</code> object includes the <code>original_error</code> message for debugging. Try again or contact <a href="{{site.baseurl}}/support_contact/">Support</a>.</td>
    </tr>
  </tbody>
</table>


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
