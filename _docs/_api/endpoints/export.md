---
nav_title: Export
page_order: 1
search_rank: 2
---

# Export

With this collection of endpoints, you will be able to access and export various levels of details on your users, segments, campaigns, and Canvases. Please be sure to reference the correct [Instance](https://www.braze.com/documentation/rest_api/#endpoints) when making API requests.

## User Export

### Users by Identifier Endpoint

This endpoint allows you to export data from any user profile by specifying a form of user identifier. Up to 50 `external_ids` or `user_aliases` can be included in a single request. Should you want to specify `device_id` or `email_address` only one of either identifier can be included per request.

| Instance | REST Endpoint                                    |
| -------- | ------------------------------------------------ |
| US-01    | `https://rest.iad-01.braze.com/users/export/ids` |
| US-02    | `https://rest.iad-02.braze.com/users/export/ids` |
| US-03    | `https://rest.iad-03.braze.com/users/export/ids` |
| US-04    | `https://rest.iad-04.braze.com/users/export/ids` |
| US-06    | `https://rest.iad-06.braze.com/users/export/ids` |
| EU-01    | `https://rest.fra-01.braze.eu/users/export/ids`  |

```json
POST https://YOUR_REST_API_URL/users/export/ids
Content-Type: application/json
{
    "api_key" : (required, string) App Group REST API Key,
    // Either "external_ids," "user_aliases," "device_id," "braze_id," or "email_address" are required. Requests must specify only one.
    "external_ids" : (optional, array of string) external ids for users to export,
    "user_aliases" : (optional, array of User Alias Object) user aliases for users to export,
    "device_id" : (optional, string) device id as returned by various SDK methods such as getDeviceId,
    "braze_id" : (optional, string) Braze ID for a particular user,
    "email_address" : (optional, string) email address of a user,
    "fields_to_export" : (optional, array of string) name of user data fields to export, e.g. ['first_name', 'email', 'purchases'], defaults to all if not provided
}
```

The following is a list of valid `fields_to_export`. Using `fields_to_export` to minimize the data returned can improve response time of this API endpoint:

* `apps`
* `attributed_campaign`
* `attributed_source`
* `attributed_adgroup`
* `attributed_ad`
* `braze_id`
* `campaigns_received`
* `canvases_received`
* `cards_clicked`
* `country`
* `created_at`
* `custom_attributes`
* `custom_events`
* `devices`
* `dob`
* `email`
* `email_subscribe`
* `external_id`
* `first_name`
* `gender`
* `home_city`
* `language`
* `last_coordinates`
* `last_name`
* `phone`
* `purchases`
* `push_subscribe`
* `push_tokens`
* `random_bucket`
* `time_zone`
* `total_revenue`
* `uninstalled_at`
* `user_aliases`

Please be aware that the `/users/export/ids` endpoint will pull together the entire user profile for this user, including data such as all campaigns and canvases received, all custom events performed, all purchases made, and all custom attributes. As a result, this endpoint is slower than other REST API endpoints.

Depending on the data requested, this API endpoint may have not be able to fulfill your hourly API rate limit. If you anticipate using this endpoint regularly to export users, instead consider exporting users by segment, which is asynchronous and more optimized for larger data pulls. Documentation on that endpoint is below.

#### Users by Identifier Endpoint API Response:

```json
Content-Type: application/json
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "users" : (array of object) the data for each of the exported users, may be empty if no users are found,
    "invalid_user_ids" : (optional, array of string) each of the identifiers provided in the request that did not correspond to a known user
}
```

For an example of the data that is accessible via this endpoint see the [Sample User Export Output section][14] of this documentation.

### Users by Segment Endpoint

This endpoint allows you to export all the users within a segment. User data is exported as multiple files of user JSON objects separated by new lines (i.e. one JSON object per line).

If you have added your S3 credentials to Braze, then each file will be uploaded in your bucket as a zip file with the key format that looks like `segment-export/SEGMENT_ID/YYYY-MM-dd/RANDOM_UUID-TIMESTAMP_WHEN_EXPORT_STARTED/filename.zip`. We will create 1 file per 5,000 users to optimize processing. You can then unzip the files and concatenate all of the `json` files to a single file if needed. If you specify an `output_format` of `gzip`, then the file extension will be `.gz` instead of `.zip`.

{% details Export Pathing Breakdown for ZIP File %}
ZIP file format:
`bucket-name/segment-export/SEGMENT_ID/YYYY-MM-dd/RANDOM_UUID-TIMESTAMP_WHEN_EXPORT_STARTED/filename.zip`

Example ZIP File:
`braze.docs.bucket/segment-export/abc56c0c-rd4a-pb0a-870pdf4db07q/2019-04-25/d9696570-dfb7-45ae-baa2-25e302r2da27-1556044807/114f0226319130e1a4770f2602b5639a.zip`

| Property | Details | Shown in Example as... |
|---|---|
| `bucket-name` | Fixed based on your bucket name. | `braze.docs.bucket`
| `segment-export` | Fixed. | `segment-export`
| `SEGMENT_ID` | Included in the export request. | `abc56c0c-rd4a-pb0a-870pdf4db07q`
| `YYYY-MM-dd` | The date the successful callback is received. | `2019-04-25`
| `RANDOM_UUID` | A random UUID generated by Braze at the time of the request. | `d9696570-dfb7-45ae-baa2-25e302r2da27`
| `TIMESTAMP_WHEN_EXPORT_STARTED` | Unix time (seconds since 2017-01-01:00:00:00Z) that the export was requested. | `1556044807`
| `filename` | Random per file. | `114f0226319130e1a4770f2602b5639a`

{% enddetails %}

<br>

If you do not have S3 credentials provided, the response to the request provides the URL where a zip file containing all the user files can be downloaded. The URL will only become a valid location once the export is ready. Please be aware that if you do not have S3 credentials, there is a limitation on the amount of data that you can export from this endpoint. In most cases this limit is about 5 gigabytes, which is usually around 500,000 to 1 million user profiles. In the event that you have not added S3 credentials and you attempt to export a segment that is too large, Braze will notify the person who last edited the segment that you must provide S3 credentials in order to export the segment.

In either scenario, you may optionally provide a `callback_endpoint` to be notified when the export is ready. If the `callback_endpoint` is provided, we will make a post request to the provided address when the download is ready. The body of the post will be "success":true. If you have not added S3 credentials to Braze, then the body of the post will additionally have the attribute `url` with the download url as the value.

Larger user bases will result in longer export times. For example, an app with 20 million users could take an hour or more.

| Instance | REST Endpoint                                        |
| -------- | ---------------------------------------------------- |
| US-01    | `https://rest.iad-01.braze.com/users/export/segment` |
| US-02    | `https://rest.iad-02.braze.com/users/export/segment` |
| US-03    | `https://rest.iad-03.braze.com/users/export/segment` |
| US-04    | `https://rest.iad-04.braze.com/users/export/segment` |
| US-06    | `https://rest.iad-06.braze.com/users/export/segment` |
| EU-01    | `https://rest.fra-01.braze.eu/users/export/segment`  |

```json
POST https://YOUR_REST_API_URL/users/export/segment
Content-Type: application/json
{
    "api_key" : (required, string) App Group REST API Key,
    "segment_id" : (required, string) identifier for the segment to be exported,
    "callback_endpoint" : (optional, string) endpoint to post a download url to when the export is available,
    "fields_to_export" : (optional, array of string) name of user data fields to export, e.g. ['first_name', 'email', 'purchases']. Defaults to all if not provided.
    "output_format" : (optional, string) When using your own S3 bucket, allows to specify file format as 'zip' or 'gzip'. Defaults to zip file format
}
```

The `segment_id` for a given segment can be found in your Developer Console within your Braze account or you can use the [Segment List Endpoint](#segment-list).

{% alert warning %}
Individual custom attributes cannot be exported. However, all custom attributes can be exported by including `custom_attributes` in the `fields_to_export` array (e.g. ['first_name', 'email', 'custom_attributes']).
{% endalert %}

#### Users by Segment Endpoint API Response

```json
Content-Type: application/json
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "object_prefix": (required, string) the filename prefix that will be used for the JSON file produced by this export, e.g. 'bb8e2a91-c4aa-478b-b3f2-a4ee91731ad1-1464728599',
    "url" : (optional, string) the url where the segment export data can be downloaded if you do not have your own S3 credentials
}
```

Once made available, the url will only be valid for a few hours. As such, we highly recommend that you add your own S3 credentials to Braze.

#### Sample User Export File Output

User export object (we will include the least data possible - if a field is missing from the object it should be assumed to be null, false, or empty):

```json
{
    "external_id" : (string),
    "user_aliases" : [
      {
        "alias_name" : (string),
        "alias_label" : (string)
      }
    ],
    "braze_id": (string),
    "first_name" : (string),
    "last_name" : (string),
    "email" : (string),
    "dob" : (string) date for the user's date of birth,
    "home_city" : (string),
    "country" : (string),
    "phone" : (string),
    "language" : (string) ISO-639 two letter code,
    "time_zone" : (string),
    "last_coordinates" : (array of float) [lon, lat],
    "gender" : (string) "M" | "F",
    "total_revenue" : (float),
    "attributed_campaign" : (string),
    "attributed_source" : (string),
    "attributed_adgroup" : (string),
    "attributed_ad" : (string),
    "push_subscribe" : (string) "opted_in" | "subscribed" | "unsubscribed",
    "email_subscribe" : (string) "opted_in" | "subscribed" | "unsubscribed",
    "custom_attributes" : (object) custom attribute key-value pairs,
    "custom_events" : [
        {
            "name" : (string),
            "first" : (string) date,
            "last" : (string) date,
            "count" : (int)
        },
        ...
    ],
    "purchases" : [
        {
            "name" : (string),
            "first" : (string) date,
            "last" : (string) date,
            "count" : (int)
        },
        ...
    ],
    "devices" : [
        {
            "model" : (string),
            "os" : (string),
            "carrier" : (string),
            "idfv" : (string) only included for iOS devices,
            "idfa" : (string) only included for iOS devices when IDFA collection is enabled,
            "ad_tracking_enabled" : (bool)
        },
        ...
    ],
    "push_tokens" : [
        {
            "app" : (string) app name,
            "platform" : (string),
            "token" : (string)
        },
        ...
    ],
    "apps" : [
        {
            "name" : (string),
            "platform" : (string),
            "version" : (string),
            "sessions" : (string),
            "first_used" : (string) date,
            "last_used" : (string) date
        },
        ...
    ],
    "campaigns_received" : [
        {
            "name" : (string),
            "last_received" : (string) date,
            "engaged" : {
                "opened_email" : (bool),
                "opened_push" : (bool),
                "clicked_email" : (bool),
                "clicked_in_app_message" : (bool)
            },
            "converted" : (bool),
            "api_campaign_id" : (string),
            "variation_name" : (optional, string) exists only if it is a multivariate campaign,
            "variation_api_id" : (optional, string) exists only if it is a multivariate campaign,
            "in_control" : (optional, bool) exists only if it is a multivariate campaign
        },
        ...
    ],
    "canvases_received": [
        {
            "name": (string),
            "api_canvas_id": (string),
            "last_received_message": (string) date,
            "last_entered": (string) date,
            "variation_name": (string),
            "in_control": (bool),
            "last_exited": (string) date,
            "steps_received": [
                {
                    "name": (string),
                    "api_canvas_step_id": (string),
                    "last_received": (string) date
                },
                {
                    "name": (string),
                    "api_canvas_step_id": (string),
                    "last_received": (string) date
                },
                {
                    "name": (string),
                    "api_canvas_step_id": (string),
                    "last_received": (string) date
                }
            ]
        },
        ...
    ],
    "cards_clicked" : [
        {
            "name" : (string)
        },
        ...
    ]
}
```

## Segment Export

### Segment List Endpoint

This endpoint allows you to export a list of segments, each of which will include its name, Segment API Identifier, and whether it has analytics tracking enabled. The segments are returned in groups of 100 sorted by time of creation (oldest to newest by default). Archived segments are not included.

`GET https://YOUR_REST_API_URL/segments/list`

| Instance | REST Endpoint                                 |
| -------- | --------------------------------------------- |
| US-01    | `https://rest.iad-01.braze.com/segments/list` |
| US-02    | `https://rest.iad-02.braze.com/segments/list` |
| US-03    | `https://rest.iad-03.braze.com/segments/list` |
| US-04    | `https://rest.iad-04.braze.com/segments/list` |
| US-06    | `https://rest.iad-06.braze.com/segments/list` |
| EU-01    | `https://rest.fra-01.braze.eu/segments/list`  |

| Parameter        | Required | Data Type | Description                                                                                                                                                                                     |
| ---------------- | -------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `api_key`        | Yes      | String    | App Group REST API Key                                                                                                                                                                          |
| `page`           | No       | Integer   | The page of segments to return, defaults to 0 (returns the first set of up to 100)                                                                                                              |
| `sort_direction` | No       | String    | Pass in the value `desc` to sort by creation time from newest to oldest. Pass in `asc` to sort from oldest to newest. If `sort_direction` is not included, the default order is oldest to newest. |

**Example URL:**
`https://rest.iad-01.braze.com/segments/list?api_key=75480f9a-4db8-4057-8b7e-4d59bfd73709&page=1`

#### Segment List Endpoint API Response:

```json
Content-Type: application/json
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "segments" : [
        {
            "id" : (string) Segment API Identifier,
            "name" : (string) segment name,
            "analytics_tracking_enabled" : (boolean) whether the segment has analytics tracking enabled,
            "tags" : (array) tag names associated with the segment
        },
        ...
    ]
}
```

### Segment Analytics Endpoint

This endpoint allows you to retrieve a daily series of the size of a segment over time for a segment.

`GET https://YOUR_REST_API_URL/segments/data_series`

| Instance | REST Endpoint                                        |
| -------- | ---------------------------------------------------- |
| US-01    | `https://rest.iad-01.braze.com/segments/data_series` |
| US-02    | `https://rest.iad-02.braze.com/segments/data_series` |
| US-03    | `https://rest.iad-03.braze.com/segments/data_series` |
| US-04    | `https://rest.iad-04.braze.com/segments/data_series` |
| US-06    | `https://rest.iad-06.braze.com/segments/data_series` |
| EU-01    | `https://rest.fra-01.braze.eu/segments/data_series`  |

| Parameter    | Required | Data Type                  | Description                                                                                                 |
| ------------ | -------- | -------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `api_key`    | Yes      | String                     | App Group REST API Key                                                                                      |
| `segment_id` | Yes      | String                     | Segment API Identifier                                                                                      |
| `length`     | Yes      | Integer                    | Max number of days before ending_at to include in the returned series - must be between 1 and 100 inclusive |
| `ending_at`  | No       | DateTime (ISO 8601 string) | Point in time when the data series should end - defaults to time of the request                             |

The `segment_id` for a given segment can be found in your Developer Console within your Braze account or you can use the [Segment List Endpoint](#segment-list).

**Example URL:**
`https://rest.iad-01.braze.com/segments/data_series?api_key=75480f9a-4db8-4057-8b7e-4d59bfd73709&segment_id=3bbc4555-8fa0-4c9b-a5c0-4505edf3e064&length=7&ending_at=2014-12-10T23:59:59-05:00`

#### Segment Analytics Endpoint API Response

```json
Content-Type: application/json
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "data" : [
        {
            "time" : (string) date as ISO 8601 date,
            "size" : (int) size of the segment on that date
        },
        ...
    ]
}
```

### Segment Details Endpoint

This endpoint allows you to retrieve relevant information on the segment, which can be identified by the `segment_id`.

`GET https://YOUR_REST_API_URL/segments/details`

| Instance | REST Endpoint                                    |
| -------- | ------------------------------------------------ |
| US-01    | `https://rest.iad-01.braze.com/segments/details` |
| US-02    | `https://rest.iad-02.braze.com/segments/details` |
| US-03    | `https://rest.iad-03.braze.com/segments/details` |
| US-04    | `https://rest.iad-04.braze.com/segments/details` |
| US-06    | `https://rest.iad-06.braze.com/segments/details` |
| EU-01    | `https://rest.fra-01.braze.eu/segments/details`  |

| Parameter    | Required | Data Type | Description            |
| ------------ | -------- | --------- | ---------------------- |
| `api_key`    | Yes      | String    | App Group REST API Key |
| `segment_id` | Yes      | String    | Segment API Identifier |

{% alert tip %}
The `segment_id` for a given segment can be found in your Developer Console within your Braze account or you can use the [Segment List Endpoint](#segment-list).
{% endalert %}

**Example URL:**
`https://rest.iad-01.braze.com/segments/details?api_key=75480f9a-4db8-4057-8b7e-4d59bfd73709&segment_id=3bbc4555-8fa0-4c9b-a5c0-4505edf3e064`

#### Segment Details Endpoint API Response

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

## Campaign Export

### Campaign List Endpoint

This endpoint allows you to export a list of campaigns, each of which will include its name, Campaign API Identifier, whether it is an API Campaign, and Tags associated with the campaign. The campaigns are returned in groups of 100 sorted by time of creation (oldest to newest by default).

{% alert important %}
Archived campaigns will not be included in the API response unless `include_archived` is specified. Paused campaigns, however, will be returned by default.
{% endalert %}

`GET https://YOUR_REST_API_URL/campaigns/list`

| Instance | REST Endpoint                                  |
| -------- | ---------------------------------------------- |
| US-01    | `https://rest.iad-01.braze.com/campaigns/list` |
| US-02    | `https://rest.iad-02.braze.com/campaigns/list` |
| US-03    | `https://rest.iad-03.braze.com/campaigns/list` |
| US-04    | `https://rest.iad-04.braze.com/campaigns/list` |
| US-06    | `https://rest.iad-06.braze.com/campaigns/list` |
| EU-01    | `https://rest.fra-01.braze.eu/campaigns/list`  |

| Parameter          | Required | Data Type | Description                                                                                                                                                                                     |
| ------------------ | -------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `api_key`          | Yes      | String    | App Group REST API Key                                                                                                                                                                          |
| `page`             | No       | Integer   | The page of campaigns to return, defaults to 0 (returns the first set of up to 100)                                                                                                             |
| `include_archived` | No       | Boolean   | Whether or not to include archived campaigns, defaults to false                                                                                                                                 |
| `sort_direction`   | No       | String    | Pass in the value `desc` to sort by creation time from newest to oldest. Pass in `asc` to sort from oldest to newest. If sort_direction is not included, the default order is oldest to newest. |

**Example URL:**
`https://rest.iad-01.braze.com/campaigns/list?api_key=75480f9a-4db8-4057-8b7e-4d59bfd73709&page=1&include_archived=true`

#### Campaign List Endpoint API Response:

```json
Content-Type: application/json
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "campaigns" : [
        {
            "id" : (string) Campaign API Identifier,
            "name" : (string) campaign name,
            "is_api_campaign" : (boolean) whether the campaign is an API Campaign,
            "tags" : (array) tag names associated with the campaign
        },
        ...
    ]
}
```

### Campaign Analytics Endpoint

This endpoint allows you to retrieve a daily series of various stats for a campaign over time.

`GET https://YOUR_REST_API_URL/campaigns/data_series`

| Instance | REST Endpoint                                         |
| -------- | ----------------------------------------------------- |
| US-01    | `https://rest.iad-01.braze.com/campaigns/data_series` |
| US-02    | `https://rest.iad-02.braze.com/campaigns/data_series` |
| US-03    | `https://rest.iad-03.braze.com/campaigns/data_series` |
| US-04    | `https://rest.iad-04.braze.com/campaigns/data_series` |
| US-06    | `https://rest.iad-06.braze.com/campaigns/data_series` |
| EU-01    | `https://rest.fra-01.braze.eu/campaigns/data_series`  |

| Parameter     | Required | Data Type                  | Description                                                                                                 |
| ------------- | -------- | -------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `api_key`     | Yes      | String                     | App Group REST API Key                                                                                      |
| `campaign_id` | Yes      | String                     | Campaign API Identifier                                                                                     |
| `length`      | Yes      | Integer                    | Max number of days before ending_at to include in the returned series - must be between 1 and 100 inclusive |
| `ending_at`   | No       | DateTime (ISO 8601 string) | Date on which the data series should end - defaults to time of the request                                  |

{% alert tip %}
The `campaign_id` for API campaigns can be found on the Developer Console page and the campaign details page within your dashboard; or you can use the [Campaign List Endpoint](#campaign-list-endpoint).
{% endalert %}

**Example URL:**
`https://rest.iad-01.braze.com/campaigns/data_series?api_key=75480f9a-4db8-4057-8b7e-4d59bfd73709&campaign_id=3bbc4555-8fa0-4c9b-a5c0-4505edf3e064&length=7&ending_at=2014-12-10T23:59:59-05:00`

#### Campaign Analytics Endpoint API Response

##### Multichannel Response

```json
Content-Type: application/json
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "data" : [
        {
            "time" : (string) date as ISO 8601 date,
            "messages" : {
                "ios_push" : [
                    {
                      "variation_name": "iOS_Push",
                      "sent" : (int),
                      "direct_opens" : (int),
                      "total_opens" : (int),
                      "bounces" : (int),
                      "body_clicks" : (int)
                      "revenue": 0,
                      "unique_recipients": 1,
                      "conversions": 0,
                      "conversions_by_send_time": 0,
                      "conversions1": 0,
                      "conversions1_by_send_time": 0,
                      "conversions2": 0,
                      "conversions2_by_send_time": 0,
                      "conversions3": 0,
                      "conversions3_by_send_time": 0,
                      "carousel_slide_[NUM]_[TITLE]_click": (optional, int),
                      "notif_button_[NUM]_[TITLE]_click": (optional, int)
                    }
                ],
                "android_push" : [
                    {
                      "sent" : (int),
                      "direct_opens" : (int),
                      "total_opens" : (int),
                      "bounces" : (int),
                      "body_clicks" : (int)
                    }
                ],
                "webhook": [
                    {
                      "sent": (int),
                      "errors": (int)
                    }
                ],
                "email" : [
                    {
                      "sent": (int),
                      "opens": (int),
                      "unique_opens": (int),
                      "clicks": (int),
                      "unique_clicks": (int),
                      "unsubscribes": (int),
                      "bounces": (int),
                      "delivered": (int),
                      "reported_spam": (int)
                    }
                ]
            },
           "conversions_by_send_time": (optional, int),
           "conversions1_by_send_time": (optional, int),
           "conversions2_by_send_time": (optional, int),
           "conversions3_by_send_time": (optional, int),
           "conversions": (int),
           "conversions1": (optional, int),
           "conversions2": (optional, int),
           "conversions3": (optional, int),
           "unique_recipients": (int),
           "revenue": (optional, float)
        },
        ...
    ],
    ...
}
```

##### Multivariate Response

```json
Content-Type: application/json
{
    "data" : [
        {
            "time" : (string) date as ISO 8601 date,
            "conversions" : (int),
            "revenue": (float),
            "conversions_by_send_time": (int),
            "messages" : {
               "trigger_in_app_message": [{
      				"variation_name": (optional, string),
      				"impressions": (int),
      				"clicks": (int),
      				"first_button_clicks": (int),
      				"second_button_clicks": (int),
      				"revenue": (optional, float),,
      				"unique_recipients": (int),
      				"conversions": (optional, int),
      				"conversions_by_send_time": (optional, int),
      				"conversions1": (optional, int),
      				"conversions1_by_send_time": (optional, int),
      				"conversions2": (optional, int),
      				"conversions2_by_send_time": (optional, int),
      				"conversions3": (optional, int),
      				"conversions3_by_send_time": (optional, int)
      			}, {
      				"variation_name": (optional, string),
      				"impressions": (int),
      				"clicks": (int),
      				"first_button_clicks": (int),
      				"second_button_clicks": (int),
      				"revenue": (optional, float),,
      				"unique_recipients": (int),
      				"conversions": (optional, int),
      				"conversions_by_send_time": (optional, int),
      				"conversions1": (optional, int),
      				"conversions1_by_send_time": (optional, int),
      				"conversions2": (optional, int),
      				"conversions2_by_send_time": (optional, int),
      				"conversions3": (optional, int).
      				"conversions3_by_send_time": (optional, int)
      			}, {
      				"variation_name": (optional, string),
      				"revenue": (optional, float),,
      				"unique_recipients": (int),
      				"conversions": (optional, int),
      				"conversions_by_send_time": (optional, int),
      				"conversions1": (optional, int),
      				"conversions1_by_send_time": (optional, int),
      				"conversions2": (optional, int),
      				"conversions2_by_send_time": (optional, int),
      				"conversions3": (optional, int),
      				"conversions3_by_send_time": (optional, int),
      				"enrolled": (optional, int)
      			}]
      		},
      		"conversions_by_send_time": (optional, int),
      		"conversions1_by_send_time": (optional, int),
      		"conversions2_by_send_time": (optional, int),
      		"conversions3_by_send_time": (optional, int),
      		"conversions": (optional, int,
      		"conversions1": (optional, int),
      		"conversions2": (optional, int),
      		"conversions3": (optional, int),
      		"unique_recipients": (int),
      		"revenue": (optional, float)
         }],
         ...
}
```

Possible message types are `email`, `in_app_message`, `webhook`, `android_push`, `apple_push`, `kindle_push`, `web_push`, `windows_phone8_push`, and `windows_universal_push`. All push message types will have the same statistics shown for `android_push` above.

### Send Analytics Endpoint

This endpoint allows you to retrieve a daily series of various stats for a tracked `send_id`. Braze stores send analytics for 14 days after the send.

{% alert tip %}
Campaign conversions will be attributed towards the most recent send id that a given user has received from the campaign.
{% endalert %}

`GET https://YOUR_REST_API_URL/sends/data_series`

| Instance | REST Endpoint                                     |
| -------- | ------------------------------------------------- |
| US-01    | `https://rest.iad-01.braze.com/sends/data_series` |
| US-02    | `https://rest.iad-02.braze.com/sends/data_series` |
| US-03    | `https://rest.iad-03.braze.com/sends/data_series` |
| US-04    | `https://rest.iad-04.braze.com/sends/data_series` |
| US-06    | `https://rest.iad-06.braze.com/sends/data_series` |
| EU-01    | `https://rest.fra-01.braze.eu/sends/data_series`  |

| Parameter     | Required | Data Type                  | Description                                                                                                 |
| ------------- | -------- | -------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `api_key`     | Yes      | String                     | App Group REST API Key                                                                                      |
| `campaign_id` | Yes      | String                     | Campaign API Identifier                                                                                     |
| `send_id`     | Yes      | String                     | Send API Identifier                                                                                         |
| `length`      | Yes      | Integer                    | Max number of days before ending_at to include in the returned series - must be between 1 and 100 inclusive |
| `ending_at`   | No       | DateTime (ISO 8601 string) | Date on which the data series should end - defaults to time of the request                                  |

{% alert important %}
The `send_id` is only generated for API campaign sends targeting segments, connected audiences or broadcasts. When relevant, the `send_id` is included in response for the `messages/send`, `messages/schedule`, `campaign/trigger/send` and campaign/trigger/schedule endpoints.
{% endalert %}

**Example URL:**
`https://rest.iad-01.braze.com/sends/data_series?api_key=75480f9a-4db8-4057-8b7e-4d59bfd73709&campaign_id=3bbc4555-8fa0-4c9b-a5c0-4505edf3e064&send_id=3456789&length=7&ending_at=2014-12-10T23:59:59-05:00`

#### Send Analytics Endpoint API Response

```json
Content-Type: application/json
{
            "variation_name": (string) variation name,
            "sent": (int) the number of sends,
            "direct_opens": (int) the number of direct opens,
            "total_opens": (int) the number of total opens,
            "bounces": (int) the number of bounces,
            "body_clicks": (int) the number of body clicks,
            "revenue": (float) the number of dollars of revenue (USD),
            "unique_recipients": (int) the number of unique recipients,
            "conversions": (int) the number of conversions,
            "conversions_by_send_time": (int) the number of conversions,
            "conversions1": (int, optional) the number of conversions for the second conversion event,
            "conversions1_by_send_time": (int, optional) the number of conversions for the second conversion event by send time,
            "conversions2": (int, optional) the number of conversions for the third conversion event,
            "conversions2_by_send_time": (int, optional) the number of conversions for the third conversion event by send time,
            "conversions3": (int, optional) the number of conversions for the fourth conversion event,
            "conversions3_by_send_time": (int, optional) the number of conversions for the fourth conversion event by send time
          }
        ]
      },
      "conversions_by_send_time": 0,
      "conversions1_by_send_time": 0,
      "conversions2_by_send_time": 0,
      "conversions3_by_send_time": 0,
      "conversions": 0,
      "conversions1": 0,
      "conversions2": 0,
      "conversions3": 0,
      "unique_recipients": 1,
      "revenue": 0
    }
  ],
  "message": "success"
}
```

### Campaign Details Endpoint

This endpoint allows you to retrieve relevant information on the campaign, which can be identified by the `campaign_id`.

`GET https://YOUR_REST_API_URL/campaigns/details`

| Instance | REST Endpoint                                     |
| -------- | ------------------------------------------------- |
| US-01    | `https://rest.iad-01.braze.com/campaigns/details` |
| US-02    | `https://rest.iad-02.braze.com/campaigns/details` |
| US-03    | `https://rest.iad-03.braze.com/campaigns/details` |
| US-04    | `https://rest.iad-04.braze.com/campaigns/details` |
| US-06    | `https://rest.iad-06.braze.com/campaigns/details` |
| EU-01    | `https://rest.fra-01.braze.eu/campaigns/details`  |

| Parameter     | Required | Data Type | Description             |
| ------------- | -------- | --------- | ----------------------- |
| `api_key`     | Yes      | String    | App Group REST API Key  |
| `campaign_id` | Yes      | String    | Campaign API Identifier |

{% alert tip %}
The `campaign_id` for API campaigns can be found on the Developer Console page and the campaign details page within your dashboard or you can use the [Campaign List Endpoint](#campaign-list-endpoint).
{% endalert %}

**Example URL:**
`https://rest.iad-01.braze.com/campaigns/details?api_key=75480f9a-4db8-4057-8b7e-4d59bfd73709&campaign_id=3bbc4555-8fa0-4c9b-a5c0-4505edf3e064`

#### Campaign Details Endpoint API Response

```json
Content-Type: application/json
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "created_at" : (string) date created as ISO 8601 date,
    "updated_at" : (string) date last updated as ISO 8601 date,
    "archived": (boolean) whether this Campaign is archived,
    "draft": (boolean) whether this Campaign is a draft,
    "name" : (string) campaign name,
    "schedule_type" : (string) type of scheduling action,
    "channels" : (array) list of channels to send via,
    "first_sent" : (string) date and hour of first sent as ISO 8601 date,
    "last_sent" : (string) date and hour of last sent as ISO 8601 date,
    "tags" : (array) tag names associated with the campaign,
    "messages": {
        "message_variation_id": (string) { // <=This is the actual id
            "channel": (string) channel type of the message (eg., "email", "ios_push", "webhook", "content_card", "in-app_message"),
            "name": (string) name of the message in the Dashboard (eg., "Variation 1")
            ... channel-specific fields for this message, see below ...
        }
    },
    "conversion_behaviors": (array) conversion event behaviors assigned to the campaign (see below)
}
```

##### Messages

The `messages` hash will contain information about each message. Example message responses for channels are below:

**Push Channels**

```json
{
    "channel": (string) description of the channel, such as "ios_push" or "android_push"
    "alert": (string) alert body text,
    "extras": (hash) any key-value pairs provided
}
```

**Email Channel**

```json
{
    "channel": "email",
    "subject": (string) subject,
    "body": (string) HTML body (truncated after 10kb),
    "from": (string) from address and display name,
    "reply_to": (string) reply-to for message, if different than "from" address,
    "title": (string) name of the email,
    "extras": (hash) any key-value pairs provided
}
```

**Content Card Channel**

```json
{
    "channel": "content_cards",
    "name": (string) name of variant,
    "extras": (hash) any key-value pairs provided, only present if at least one custom key-value pair has been set
}
```

**Webhook Channel**

```json
{
    "channel": "webhook",
    "url": (string) url for webhook,
    "body": (string) payload body,
    "type": (string) body content type,
    "headers": (hash) specified request headers,
    "method": (string) HTTP method (e.g., "POST" or "GET"),
}
```

**Control Messages**

```json
{
    "channel": (string) description of the channel that the control is for,
    "type": "control"
}
```

##### Conversion Behaviors

The `conversion_behaviors` array will contain information about each conversion event behavior set for the campaign. These behaviors are in order as set by the campaign. For example, Conversion Event A will be the first item in the array, Conversion Event B will be second, etc. Example conversion event behavior responses for are below:

**Clicks Email**

```json
{
    "type": "Clicks Email",
    "window": (integer) number of seconds during which the user can convert on this event, i.e. - 86400, which is 24 hours
}
```

**Opens Email**

```json
{
    "type": "Opens Email",
    "window": (integer) number of seconds during which the user can convert on this event, i.e. - 86400, which is 24 hours
}
```

**Makes Purchase (any purchase)**

```json
{
    "type": "Makes Any Purchase",
    "window": (integer) number of seconds during which the user can convert on this event, i.e. - 86400, which is 24 hours
}
```

**Makes Purchase (specific product)**

```json
{
    "type": "Makes Specific Purchase",
    "window": (integer) number of seconds during which the user can convert on this event, i.e. - 86400, which is 24 hours,
    "product": (string) name of the product, i.e. - "Feline Body Armor"
}
```

**Performs Custom Event**

```json
{
    "type": "Performs Custom Event",
    "window": (integer) number of seconds during which the user can convert on this event, i.e. - 86400, which is 24 hours,
    "custom_event_name": (string) name of the event, i.e. - "Used Feline Body Armor"
}
```

**Upgrades App**

```json
{
    "type": "Upgrades App",
    "window": (integer) number of seconds during which the user can convert on this event, i.e. - 86400, which is 24 hours,
    "app_ids": (array|null) array of app ids, i.e. - ["12345", "67890"], or `null` if "Track sessions for any app" is selected in the UI
}
```

**Uses App**

```json
{
    "type": "Starts Session",
    "window": (integer) number of seconds during which the user can convert on this event, i.e. - 86400, which is 24 hours,
    "app_ids": (array|null) array of app ids, i.e. - ["12345", "67890"], or `null` if "Track sessions for any app" is selected in the UI
}
```

## Canvas Data Export

### Canvas List Endpoint

This endpoint allows you to export a list of Canvases, including the name, Canvas API Identifier and associated Tags. The Canvases are returned in groups of 100 sorted by time of creation (oldest to newest by default).

> Archived Canvases will not be included in the API response unless the `include_archived` field is specified. Canvases that are stopped but not archived, however, will be returned by default.

#### Endpoint Details

`GET https://YOUR_REST_API_URL/canvas/list`

| Instance | REST Endpoint                               |
| -------- | ------------------------------------------- |
| US-01    | `https://rest.iad-01.braze.com/canvas/list` |
| US-02    | `https://rest.iad-02.braze.com/canvas/list` |
| US-03    | `https://rest.iad-03.braze.com/canvas/list` |
| US-04    | `https://rest.iad-04.braze.com/canvas/list` |
| US-06    | `https://rest.iad-06.braze.com/canvas/list` |
| EU-01    | `https://rest.fra-01.braze.eu/canvas/list`  |

| Parameter          | Required | Data Type | Description                                                                                                                                                                                     |
| ------------------ | -------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `api_key`          | Yes      | String    | App Group REST API Key                                                                                                                                                                          |
| `page`             | No       | Integer   | The page of Canvases to return, defaults to 0 (returns the first set of up to 100)                                                                                                              |
| `include_archived` | No       | Boolean   | Whether or not to include archived Canvases, defaults to false                                                                                                                                  |
| `sort_direction`   | No       | String    | Pass in the value `desc` to sort by creation time from newest to oldest. Pass in `asc` to sort from oldest to newest. If sort_direction is not included, the default order is oldest to newest. |

```json
{
  "canvases" : [
  	{
  		"id" : (string) Canvas API Identifier,
  		"name" : (string) Canvas name,
  		"tags" : (array) tag names associated with the Canvas,
  	},
    ... (more Canvases)
  ],
  "message": (required, string) the status of the export, returns 'success' when completed without errors
}
```

### Canvas Details Endpoint

This endpoint allows you to export metadata about a Canvas, such as its name, when it was
created, its current status, and more.

#### Endpoint Details

`GET https://YOUR_REST_API_URL/canvas/details`

| Instance | REST Endpoint                                  |
| -------- | ---------------------------------------------- |
| US-01    | `https://rest.iad-01.braze.com/canvas/details` |
| US-02    | `https://rest.iad-02.braze.com/canvas/details` |
| US-03    | `https://rest.iad-03.braze.com/canvas/details` |
| US-04    | `https://rest.iad-04.braze.com/canvas/details` |
| US-06    | `https://rest.iad-06.braze.com/canvas/details` |
| EU-01    | `https://rest.fra-01.braze.eu/canvas/details`  |

| Parameter   | Required | Data Type | Description            |
| ----------- | -------- | --------- | ---------------------- |
| `api_key`   | Yes      | String    | App Group REST API Key |
| `canvas_id` | Yes      | String    | Canvas API Identifier  |

```json
{
  "created_at": (string) date created as ISO 8601 date,
  "updated_at": (string) date updated as ISO 8601 date,
  "name": (string) Canvas name,
  "archived": (boolean) whether this Canvas is archived,
  "draft": (boolean) whether this Canvas is a draft,
  "schedule_type": (string) type of scheduling action,
  "first_entry": (string) date of first entry as ISO 8601 date,
  "last_entry": (string) date of last entry as ISO 8601 date,
  "channels": (array of strings) step channels used with Canvas,
  "variants": [
    {
      "name": (string) name of variant,
      "first_step_ids": (array of strings) API identifiers for first steps in variant,
      "first_step_id": (string) API identifier of first step in variant (deprecated in November 2017, only included if the variant has only one first step)
    },
    ... (more variations)
  ],
  "tags": (array of strings) tag names associated with the Canvas,
  "steps": [
    {
      "name": (string) name of step,
      "id": (string) API identifier of the step,
      "next_step_ids": (array of strings) API identifiers of steps following step,
      "channels": (array of strings) channels used in step,
      "messages": {
          "message_variation_id": (string) {  // <=This is the actual id
              "channel": (string) channel type of the message (eg., "email"),
              ... channel-specific fields for this message, see Campaign Details Endpoint API Response for example message responses ...
          }
      }
    },
    ... (more steps)
  ],
  "message": (required, string) the status of the export, returns 'success' when completed without errors
}
```

### Canvas Data Series Endpoint

This endpoint allows you to export time series data for a Canvas.

#### Endpoint Details

`GET https://YOUR_REST_API_URL/canvas/data_series`

| Instance | REST Endpoint                                      |
| -------- | -------------------------------------------------- |
| US-01    | `https://rest.iad-01.braze.com/canvas/data_series` |
| US-02    | `https://rest.iad-02.braze.com/canvas/data_series` |
| US-03    | `https://rest.iad-03.braze.com/canvas/data_series` |
| US-04    | `https://rest.iad-04.braze.com/canvas/data_series` |
| US-06    | `https://rest.iad-06.braze.com/canvas/data_series` |
| EU-01    | `https://rest.fra-01.braze.eu/canvas/data_series`  |

| Parameter                   | Required | Data Type                  | Description                                                                                                                                        |
| --------------------------- | -------- | -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `api_key`                   | Yes      | String                     | App Group REST API Key                                                                                                                             |
| `canvas_id`                 | Yes      | String                     | Canvas API Identifier                                                                                                                              |
| `ending_at`                 | Yes      | DateTime (ISO 8601 string) | Date on which the data export should end - defaults to time of the request                                                                         |
| `starting_at`               | No       | DateTime (ISO 8601 string) | Date on which the data export should begin (either length or starting_at are required)                                                             |
| `length`                    | No       | String                     | Max number of days before ending_at to include in the returned series - must be between 1 and 14 inclusive (either length or starting_at required) |
| `include_variant_breakdown` | No       | Boolean                    | Whether or not to include variant stats (defaults to false)                                                                                        |
| `include_step_breakdown`    | No       | Boolean                    | Whether or not to include step stats (defaults to false)                                                                                           |
| `include_deleted_step_data` | No       | Boolean                    | Whether or not to include step stats for deleted steps (defaults to false)                                                                         |

<h4 id="campaign-data-series-endpoint-response"></h4>

#### Canvas Data Series Endpoint Response

```json
{
  "data": {
    "name": (string) Canvas name,
    "stats": [
      {
        "time": (string) date as ISO 8601 date,
        "total_stats": {
          "revenue": (float),
          "conversions": (int),
          "conversions_by_entry_time": (int),
          "entries": (int)
        },
        "variant_stats": (optional) {
          "00000000-0000-0000-0000-0000000000000": (API identifier for variant) {
            "name": (string) name of variant,
            "revenue": (int),
            "conversions": (int),
            "conversions_by_entry_time": (int),
            "entries": (int)
          },
          ... (more variants)
        },
        "step_stats": (optional) {
          "00000000-0000-0000-0000-0000000000000": (API identifier for step) {
            "name": (string) name of step,
            "revenue": (float),
            "conversions": (int),
            "conversions_by_entry_time": (int),
            "messages": {
              "email": [
                {
                  "sent": (int),
                  "opens": (int),
                  "unique_opens": (int),
                  "clicks": (int),
                  ... (more stats)
                }
              ],
              ... (more channels)
            }
          },
          ... (more steps)
        }
      },
      ... (more stats by time)
    ]
  },
  "message": (required, string) the status of the export, returns 'success' when completed without errors
}
```

### Canvas Data Summary Endpoint

This endpoint allows you to export rollups of time series data for a Canvas, providing a concise summary
of a Canvas' results.

#### Endpoint Details

`GET https://YOUR_REST_API_URL/canvas/data_summary`

| Instance | REST Endpoint                                       |
| -------- | --------------------------------------------------- |
| US-01    | `https://rest.iad-01.braze.com/canvas/data_summary` |
| US-02    | `https://rest.iad-02.braze.com/canvas/data_summary` |
| US-03    | `https://rest.iad-03.braze.com/canvas/data_summary` |
| US-04    | `https://rest.iad-04.braze.com/canvas/data_summary` |
| US-06    | `https://rest.iad-06.braze.com/canvas/data_summary` |
| EU-01    | `https://rest.fra-01.braze.eu/canvas/data_summary`  |

| Parameter                   | Required | Data Type                  | Description                                                                                                                                        |
| --------------------------- | -------- | -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `api_key`                   | Yes      | String                     | App Group REST API Key                                                                                                                             |
| `canvas_id`                 | Yes      | String                     | Canvas API Identifier                                                                                                                              |
| `ending_at`                 | Yes      | DateTime (ISO 8601 string) | Date on which the data export should end - defaults to time of the request                                                                         |
| `starting_at`               | No       | DateTime (ISO 8601 string) | Date on which the data export should begin (either length or starting_at required)                                                                 |
| `length`                    | No       | String                     | Max number of days before ending_at to include in the returned series - must be between 1 and 14 inclusive (either length or starting_at required) |
| `include_variant_breakdown` | No       | Boolean                    | Whether or not to include variant stats (defaults to false)                                                                                        |
| `include_step_breakdown`    | No       | Boolean                    | Whether or not to include step stats (defaults to false)                                                                                           |
| `include_deleted_step_data` | No       | Boolean                    | Whether or not to include step stats for deleted steps (defaults to false)                                                                         |

```json
{
  "data": {
    "name": (string) Canvas name,
    "total_stats": {
      "revenue": (float),
      "conversions": (int),
      "conversions_by_entry_time": (int),
      "entries": (int)
    },
    "variant_stats": (optional) {
      "00000000-0000-0000-0000-0000000000000": (API identifier for variant) {
        "name": (string) name of variant,
        "revenue": (float),
        "conversions": (int),
        "entries": (int)
      },
      ... (more variants)
    },
    "step_stats": (optional) {
      "00000000-0000-0000-0000-0000000000000": (API identifier for step) {
        "name": (string) name of step,
        "revenue": (float),
        "conversions": (int),
        "conversions_by_entry_time": (int),
        "messages": {
          "android_push": (name of channel) [
            {
              "sent": (int),
              "opens": (int),
              "influenced_opens": (int),
              "bounces": (int)
              ... (more stats for channel)
            }
          ],
          ... (more channels)
        }
      },
      ... (more steps)
    }
  },
  "message": (required, string) the status of the export, returns 'success' when completed without errors
}
```

## News Feed Export

### News Feed List Endpoint

This endpoint allows you to export a list of News Feed cards, each of which will include it's name and Card API Identifier. The cards are returned in groups of 100 sorted by time of creation (oldest to newest by default).

`GET https://YOUR_REST_API_URL/feed/list`

| Instance | REST Endpoint                             |
| -------- | ----------------------------------------- |
| US-01    | `https://rest.iad-01.braze.com/feed/list` |
| US-02    | `https://rest.iad-02.braze.com/feed/list` |
| US-03    | `https://rest.iad-03.braze.com/feed/list` |
| US-04    | `https://rest.iad-04.braze.com/feed/list` |
| US-06    | `https://rest.iad-06.braze.com/feed/list` |
| EU-01    | `https://rest.fra-01.braze.eu/feed/list`  |

| Parameter          | Required | Data Type | Description                                                                                                                                                                                     |
| ------------------ | -------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `api_key`          | Yes      | String    | App Group REST API Key                                                                                                                                                                          |
| `page`             | No       | Integer   | The page of cards to return, defaults to 0 (returns the first set of up to 100)                                                                                                                 |
| `include_archived` | No       | Boolean   | Whether or not to include archived cards, defaults to false                                                                                                                                     |
| `sort_direction`   | No       | String    | Pass in the value `desc` to sort by creation time from newest to oldest. Pass in `asc` to sort from oldest to newest. If sort_direction is not included, the default order is oldest to newest. |

**Example URL:**
`https://rest.iad-01.braze.com/feed/list?api_key=75480f9a-4db8-4057-8b7e-4d59bfd73709&page=1&include_archived=true`

#### News Feed List Endpoint API Response:

```json
Content-Type: application/json
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "cards" : [
        {
            "id" : (string) Card API Identifier,
            "type" : (string) type of the card - NewsItem (classic cards), CaptionedImage, Banner or DevPick (cross-promotional cards),
            "title" : (string) title of the card,
            "tags" : (array) tag names associated with the card
        },
        ...
    ]
}
```

### News Feed Analytics Endpoint

This endpoint allows you to retrieve a daily series of engagement stats for a card over time.

`GET https://YOUR_REST_API_URL/feed/data_series`

| Instance | REST Endpoint                                    |
| -------- | ------------------------------------------------ |
| US-01    | `https://rest.iad-01.braze.com/feed/data_series` |
| US-02    | `https://rest.iad-02.braze.com/feed/data_series` |
| US-03    | `https://rest.iad-03.braze.com/feed/data_series` |
| US-04    | `https://rest.iad-04.braze.com/feed/data_series` |
| US-06    | `https://rest.iad-06.braze.com/feed/data_series` |
| EU-01    | `https://rest.fra-01.braze.eu/feed/data_series`  |

| Parameter   | Required | Data Type                  | Description                                                                                                                  |
| ----------- | -------- | -------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `api_key`   | Yes      | String                     | App Group REST API Key                                                                                                       |
| `card_id`   | Yes      | String                     | Card API Identifier                                                                                                          |
| `length`    | Yes      | Integer                    | Max number of units (days or hours) before ending_at to include in the returned series - must be between 1 and 100 inclusive |
| `unit`      | No       | String                     | Unit of time between data points - can be "day" or "hour" (defaults to "day")                                                |
| `ending_at` | No       | DateTime (ISO 8601 string) | Date on which the data series should end - defaults to time of the request                                                   |

{% alert tip %}
The `card_id` for a given card can be found in the Developer Console page and on the card details page within your dashboard or you can use the [News Feed List Endpoint](#news-feed-list).
{% endalert %}

**Example URL:**
`https://rest.iad-01.braze.com/feed/data_series?api_key=75480f9a-4db8-4057-8b7e-4d59bfd73709&card_id=3bbc4555-8fa0-4c9b-a5c0-4505edf3e064&length=24&unit=hour&ending_at=2014-12-10T23:59:59-05:00`

#### News Feed Analytics Endpoint API Response

```json
Content-Type: application/json
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "data" : [
        {
            "time" : (string) point in time - as ISO 8601 extended when unit is "hour" and as ISO 8601 date when unit is "day",
            "clicks" : (int) ,
            "impressions" : (int),
            "unique_clicks" : (int),
            "unique_impressions" : (int)
        },
        ...
    ]
}
```

### News Feed Details Endpoint

This endpoint allows you to retrieve relevant information on the card, which can be identified by the `card_id`.

`GET https://YOUR_REST_API_URL/feed/details`

| Instance | REST Endpoint                                |
| -------- | -------------------------------------------- |
| US-01    | `https://rest.iad-01.braze.com/feed/details` |
| US-02    | `https://rest.iad-02.braze.com/feed/details` |
| US-03    | `https://rest.iad-03.braze.com/feed/details` |
| US-04    | `https://rest.iad-04.braze.com/feed/details` |
| US-06    | `https://rest.iad-06.braze.com/feed/details` |
| EU-01    | `https://rest.fra-01.braze.eu/feed/details`  |

| Parameter | Required | Data Type | Description            |
| --------- | -------- | --------- | ---------------------- |
| `api_key` | Yes      | String    | App Group REST API Key |
| `card_id` | Yes      | String    | Card API Identifier    |

{% alert tip %}
The `card_id` for a given card can be found in the Developer Console page and on the card details page within your dashboard or you can use the [News Feed List Endpoint](#news-feed-list).
{% endalert %}

**Example URL:**
`https://rest.iad-01.braze.com/feed/details?api_key=75480f9a-4db8-4057-8b7e-4d59bfd73709&card_id=3bbc4555-8fa0-4c9b-a5c0-4505edf3e064`

#### News Feed Details Endpoint API Response

```json
Content-Type: application/json
{
    "message": (required, string) The status of the export, returns 'success' when completed without errors,
    "created_at" : (string) Date created as ISO 8601 date,
    "updated_at" : (string) Date last updated as ISO 8601 date,
    "name" : (string) Card name,
    "publish_at" : (string) Date card was published as ISO 8601 date,
    "end_at" : (string) Date card will stop displaying for users as ISO 8601 date,
    "tags" : (array) Tag names associated with the card,
    "title" : (string) Title of the card,
    "image_url" : (string) Image URL used by this card,
    "extras" : (dictionary) Dictionary containing key-value pair data attached to this card,
    "description" : (string) Description text used by this card,
    "archived": (boolean) whether this Card is archived,
    "draft": (boolean) whether this Card is a draft,
}
```

## KPI Export

### Monthly Active Users Endpoint

This endpoint allows you to retrieve a daily series of the total number of unique active users over a 30 day rolling window.

`GET https://YOUR_REST_API_URL/kpi/mau/data_series`

| Instance | REST Endpoint                                       |
| -------- | --------------------------------------------------- |
| US-01    | `https://rest.iad-01.braze.com/kpi/mau/data_series` |
| US-02    | `https://rest.iad-02.braze.com/kpi/mau/data_series` |
| US-03    | `https://rest.iad-03.braze.com/kpi/mau/data_series` |
| US-04    | `https://rest.iad-04.braze.com/kpi/mau/data_series` |
| US-06    | `https://rest.iad-06.braze.com/kpi/mau/data_series` |
| EU-01    | `https://rest.fra-01.braze.eu/kpi/mau/data_series`  |

| Parameter   | Required | Data Type                  | Description                                                                                                 |
| ----------- | -------- | -------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `api_key`   | Yes      | String                     | App Group REST API Key                                                                                      |
| `length`    | Yes      | Integer                    | Max number of days before ending_at to include in the returned series - must be between 1 and 100 inclusive |
| `ending_at` | No       | DateTime (ISO 8601 string) | Point in time when the data series should end - defaults to time of the request                             |
| `app_id`    | No       | String                     | App API Identifier; if excluded, results for all apps in app group will be returned                         |

**Example URL:**
`https://rest.iad-01.braze.com/kpi/mau/data_series?api_key=75480f9a-4db8-4057-8b7e-4d59bfd73709&length=7&ending_at=2014-12-10T23:59:59-05:00`

#### Monthly Active Users Endpoint API Response

```json
Content-Type: application/json
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "data" : [
        {
            "time" : (string) date as ISO 8601 date,
            "mau" : (int)
        },
        ...
    ]
}
```

### Daily Active Users Endpoint

This endpoint allows you to retrieve a daily series of the total number of unique active users on each date.

`GET https://YOUR_REST_API_URL/kpi/dau/data_series`

| Instance | REST Endpoint                                       |
| -------- | --------------------------------------------------- |
| US-01    | `https://rest.iad-01.braze.com/kpi/dau/data_series` |
| US-02    | `https://rest.iad-02.braze.com/kpi/dau/data_series` |
| US-03    | `https://rest.iad-03.braze.com/kpi/dau/data_series` |
| US-04    | `https://rest.iad-04.braze.com/kpi/dau/data_series` |
| US-06    | `https://rest.iad-06.braze.com/kpi/dau/data_series` |
| EU-01    | `https://rest.fra-01.braze.eu/kpi/dau/data_series`  |

| Parameter   | Required | Data Type                  | Description                                                                                                 |
| ----------- | -------- | -------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `api_key`   | Yes      | String                     | App Group REST API Key                                                                                      |
| `length`    | Yes      | Integer                    | Max number of days before ending_at to include in the returned series - must be between 1 and 100 inclusive |
| `ending_at` | No       | DateTime (ISO 8601 string) | Point in time when the data series should end - defaults to time of the request                             |
| `app_id`    | No       | String                     | App API Identifier; if excluded, results for all apps in app group will be returned                         |

**Example URL:**
`https://rest.iad-01.braze.com/kpi/dau/data_series?api_key=75480f9a-4db8-4057-8b7e-4d59bfd73709&length=7&ending_at=2014-12-10T23:59:59-05:00`

#### Daily Active Users Endpoint API Response

```json
Content-Type: application/json
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "data" : [
        {
            "time" : (string) date as ISO 8601 date,
            "dau" : (int)
        },
        ...
    ]
}
```

### New Users Endpoint

This endpoint allows you to retrieve a daily series of the total number of new users on each date.

`GET https://YOUR_REST_API_URL/kpi/new_users/data_series`

| Instance | REST Endpoint                                             |
| -------- | --------------------------------------------------------- |
| US-01    | `https://rest.iad-01.braze.com/kpi/new_users/data_series` |
| US-02    | `https://rest.iad-02.braze.com/kpi/new_users/data_series` |
| US-03    | `https://rest.iad-03.braze.com/kpi/new_users/data_series` |
| US-04    | `https://rest.iad-04.braze.com/kpi/new_users/data_series` |
| US-06    | `https://rest.iad-06.braze.com/kpi/new_users/data_series` |
| EU-01    | `https://rest.fra-01.braze.eu/kpi/new_users/data_series`  |

| Parameter   | Required | Data Type                  | Description                                                                                                 |
| ----------- | -------- | -------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `api_key`   | Yes      | String                     | App Group REST API Key                                                                                      |
| `length`    | Yes      | Integer                    | Max number of days before ending_at to include in the returned series - must be between 1 and 100 inclusive |
| `ending_at` | No       | DateTime (ISO 8601 string) | Point in time when the data series should end - defaults to time of the request                             |
| `app_id`    | No       | String                     | App API Identifier; if excluded, results for all apps in app group will be returned                         |

**Example URL:**
`https://rest.iad-01.braze.com/kpi/new_users/data_series?api_key=75480f9a-4db8-4057-8b7e-4d59bfd73709&length=7&ending_at=2014-12-10T23:59:59-05:00`

#### New Users Endpoint API Response

```json
Content-Type: application/json
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "data" : [
        {
            "time" : (string) date as ISO 8601 date,
            "new_users" : (int)
        },
        ...
    ]
}
```

### Uninstalls Endpoint

This endpoint allows you to retrieve a daily series of the total number of uninstalls on each date.

`GET https://YOUR_REST_API_URL/kpi/uninstalls/data_series`

| Instance | REST Endpoint                                              |
| -------- | ---------------------------------------------------------- |
| US-01    | `https://rest.iad-01.braze.com/kpi/uninstalls/data_series` |
| US-02    | `https://rest.iad-02.braze.com/kpi/uninstalls/data_series` |
| US-03    | `https://rest.iad-03.braze.com/kpi/uninstalls/data_series` |
| US-04    | `https://rest.iad-04.braze.com/kpi/uninstalls/data_series` |
| US-06    | `https://rest.iad-06.braze.com/kpi/uninstalls/data_series` |
| EU-01    | `https://rest.fra-01.braze.eu/kpi/uninstalls/data_series`  |

| Parameter   | Required | Data Type                  | Description                                                                                                 |
| ----------- | -------- | -------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `api_key`   | Yes      | String                     | App Group REST API Key                                                                                      |
| `length`    | Yes      | Integer                    | Max number of days before ending_at to include in the returned series - must be between 1 and 100 inclusive |
| `ending_at` | No       | DateTime (ISO 8601 string) | Point in time when the data series should end - defaults to time of the request                             |
| `app_id`    | No       | String                     | App API Identifier; if excluded, results for all apps in app group will be returned                         |

**Example URL:**
`https://rest.iad-01.braze.com/kpi/uninstalls/data_series?api_key=75480f9a-4db8-4057-8b7e-4d59bfd73709&length=7&ending_at=2014-12-10T23:59:59-05:00`

#### Uninstalls Endpoint API Response

```json
Content-Type: application/json
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "data" : [
        {
            "time" : (string) date as ISO 8601 date,
            "uninstalls" : (int)
        },
        ...
    ]
}
```

## Sessions Analytics Export

### Sessions Series Endpoint

This endpoint allows you to retrieve a series of the number of sessions for your app over a designated time period.

`GET https://YOUR_REST_API_URL/sessions/data_series`

| Instance | REST Endpoint                                        |
| -------- | ---------------------------------------------------- |
| US-01    | `https://rest.iad-01.braze.com/sessions/data_series` |
| US-02    | `https://rest.iad-02.braze.com/sessions/data_series` |
| US-03    | `https://rest.iad-03.braze.com/sessions/data_series` |
| US-04    | `https://rest.iad-04.braze.com/sessions/data_series` |
| US-06    | `https://rest.iad-06.braze.com/sessions/data_series` |
| EU-01    | `https://rest.fra-01.braze.eu/sessions/data_series`  |

| Parameter    | Required | Data Type                  | Description                                                                                                                  |
| ------------ | -------- | -------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `api_key`    | Yes      | String                     | App Group REST API Key                                                                                                       |
| `length`     | Yes      | Integer                    | Max number of units (days or hours) before ending_at to include in the returned series - must be between 1 and 100 inclusive |
| `unit`       | No       | String                     | Unit of time between data points - can be "day" or "hour" (defaults to "day")                                                |
| `ending_at`  | No       | DateTime (ISO 8601 string) | Point in time when the data series should end - defaults to time of the request                                              |
| `app_id`     | No       | String                     | App API Identifier retrieved from the Developer Console to limit analytics to a specific app                                 |
| `segment_id` | No       | String                     | Segment API Identifier indicating the analytics enabled segment for which sessions should be returned                        |

**Example URL:**
`https://rest.iad-01.braze.com/sessions/data_series?api_key=75480f9a-4db8-4057-8b7e-4d59bfd73709&length=24&unit=hour&ending_at=2014-12-10T23:59:59-05:00&app_id=3bbc4555-8fa0-4c9b-a5c0-4505edf3e064`

#### Sessions Series Endpoint API Response

```json
Content-Type: application/json
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "data" : [
        {
            "time" : (string) point in time - as ISO 8601 extended when unit is "hour" and as ISO 8601 date when unit is "day",
            "sessions" : (int)
        },
        ...
    ]
}
```

## Custom Events Analytics Export

### Custom Events List Endpoint

This endpoint allows you to export a list of custom events that have been recorded for your app. The event names are returned in groups of 250, sorted alphabetically.

`GET https://YOUR_REST_API_URL/events/list`

| Instance | REST Endpoint                               |
| -------- | ------------------------------------------- |
| US-01    | `https://rest.iad-01.braze.com/events/list` |
| US-02    | `https://rest.iad-02.braze.com/events/list` |
| US-03    | `https://rest.iad-03.braze.com/events/list` |
| US-04    | `https://rest.iad-04.braze.com/events/list` |
| US-06    | `https://rest.iad-06.braze.com/events/list` |
| EU-01    | `https://rest.fra-01.braze.eu/events/list`  |

| Parameter | Required | Data Type | Description                                                                           |
| --------- | -------- | --------- | ------------------------------------------------------------------------------------- |
| `api_key` | Yes      | String    | App Group REST API Key                                                                |
| `page`    | No       | Integer   | The page of event names to return, defaults to 0 (returns the first set of up to 250) |

**Example URL:**
`https://rest.iad-01.braze.com/events/list?api_key=75480f9a-4db8-4057-8b7e-4d59bfd73709&page=1`

#### Custom Events List Endpoint API Response:

```json
Content-Type: application/json
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "events" : [
        "Event A",
        "Event B",
        "Event C",
        ...
    ]
}
```

### Custom Events Series Endpoint

This endpoint allows you to retrieve a series of the number of occurrences of a custom event in your app over a designated time period.

`GET https://YOUR_REST_API_URL/events/data_series`

| Instance | REST Endpoint                                      |
| -------- | -------------------------------------------------- |
| US-01    | `https://rest.iad-01.braze.com/events/data_series` |
| US-02    | `https://rest.iad-02.braze.com/events/data_series` |
| US-03    | `https://rest.iad-03.braze.com/events/data_series` |
| US-04    | `https://rest.iad-04.braze.com/events/data_series` |
| US-06    | `https://rest.iad-06.braze.com/events/data_series` |
| EU-01    | `https://rest.fra-01.braze.eu/events/data_series`  |

| Parameter    | Required | Data Type                  | Description                                                                                                                  |
| ------------ | -------- | -------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `api_key`    | Yes      | String                     | App Group REST API Key                                                                                                       |
| `event`      | Yes      | String                     | The name of the custom event for which to return analytics                                                                   |
| `length`     | Yes      | Integer                    | Max number of units (days or hours) before ending_at to include in the returned series - must be between 1 and 100 inclusive |
| `unit`       | No       | String                     | Unit of time between data points - can be "day" or "hour" (defaults to "day")                                                |
| `ending_at`  | No       | DateTime (ISO 8601 string) | Point in time when the data series should end - defaults to time of the request                                              |
| `app_id`     | No       | String                     | App API Identifier retrieved from the Developer Console to limit analytics to a specific app                                 |
| `segment_id` | No       | String                     | Segment API Identifier indicating the analytics enabled segment for which event analytics should be returned                 |

**Example URL:**
`https://rest.iad-01.braze.com/events/data_series?api_key=75480f9a-4db8-4057-8b7e-4d59bfd73709&event=Event%20A&length=24&unit=hour&ending_at=2014-12-10T23:59:59-05:00&app_id=3bbc4555-8fa0-4c9b-a5c0-4505edf3e064`

#### Custom Events Series Endpoint API Response

```json
Content-Type: application/json
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "data" : [
        {
            "time" : (string) point in time - as ISO 8601 extended when unit is "hour" and as ISO 8601 date when unit is "day",
            "count" : (int)
        },
        ...
    ]
}
```

#### Fatal Error Response Codes {#fatal-export}

The following status codes and associated error messages will be returned if your request encounters a fatal error. Any of these error codes indicate that no data will be processed.

| Error Code       | Reason / Cause                                                   |
| ---------------- | ---------------------------------------------------------------- |
| 400 Bad Request  | Bad Syntax                                                       |
| 401 Unauthorized | Unknown or missing REST API Key                                  |
| 429 Rate Limited | Over rate limit                                                  |
| 5XX              | Internal server error, you should retry with exponential backoff |

[1]: #user-export
[2]: #user-id
[3]: #users-by-segment
[4]: {{ site.baseurl }}/partners/braze_currents/data_partner_integrations/dpi/#segment
[5]: #segment-list
[6]: #segment-analytics
[7]: #campaign
[8]: #campaign-list-endpoint
[9]: #campaign-analytics
[10]: {{ site.baseurl }}/developer_guide/platform_integration_guides/unity/x_news_feed/#news-feed
[11]: #news-feed-list
[12]: #news-feed-analytics
[14]: #sample-user-export-file-output
[15]: #kpi
[16]: #kpi-mau
[17]: #kpi-dau
[18]: #kpi-new-users
[19]: #sessions
[20]: #sessions-series
[21]: {{ site.baseurl }}/developer_guide/platform_wide/analytics_overview/#custom-events
[22]: #custom-events-list
[23]: #custom-events-series
[24]: #revenue
[25]: #revenue-products
[26]: #revenue-series
[27]: #revenue-quantity-series
[28]: {{ site.baseurl }}/partners/technology_partners/data_and_infrastructure_agility/data_warehouses/aws_s3/#aws-s3-integration
[29]: https://aws.amazon.com/documentation/s3/
[30]: {{ site.baseurl }}/hidden/res/#parameters
[31]: {{ site.baseurl }}/developer_guide/rest_api/basics/#basics
[32]: http://docs.aws.amazon.com/AmazonS3/latest/user-guide/download-objects.html
[33]: {{ site.baseurl }}/hidden/res/#events-and-event-properties-chart
[34]: {{ site.baseurl }}/hidden/res/#raw-event-utc-day-loaded-status-endpoint
[35]: {{ site.baseurl }}/partners/braze_currents/how_it_works/
