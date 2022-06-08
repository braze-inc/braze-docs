---
nav_title: "POST: User Profile Export by Identifier"
article_title: "POST: User Profile Export by Identifier"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "This article outlines details about the Users by ID Braze endpoint."

---
{% api %}
# Users by identifier endpoint
{% apimethod post %}
/users/export/ids
{% endapimethod %}

This endpoint allows you to export data from any user profile by specifying a form of user identifier. Up to 50 `external_ids` or `user_aliases` can be included in a single request. Should you want to specify `device_id` or `email_address` only one of either identifier can be included per request.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#b9750447-9d94-4263-967f-f816f0c76577 {% endapiref %}

## Rate limit

{% include rate_limits.md endpoint='users export ids' %}

## Request body

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "external_ids": (optional, array of strings) External identifiers for users you wish to export,
  "user_aliases": (optional, array of user alias objects) user aliases for users to export,
  "device_id": (optional, string) Device identifier as returned by various SDK methods such as `getDeviceId`,
  "braze_id": (optional, string) Braze identifier for a particular user,
  "email_address": (optional, string) Email address of user,
  "phone": (optional, string) Phone number of user,
  "fields_to_export": (optional, array of strings) Name of user data fields to export. Defaults to all if not provided
}
```

## Request parameters

| Parameter | Required | Data Type | Description |
|-----|-----|-----|-----|
|`external_ids` | Optional | Array of strings | External identifiers for users you wish export. |
|`user_aliases` | Optional | Array of user alias object | [User aliases]({{site.baseurl}}/api/objects_filters/user_alias_object/) for users to export. |
|`device_id` | Optional | String | Device identifier, as returned by various SDK methods such as `getDeviceId`. |
|`braze_id` | Optional | String | Braze identifier for a particular user. |
|`email_address` | Optional | String | Email address of user. |
|`phone` | Optional | String in [E.164](https://en.wikipedia.org/wiki/E.164) format | Phone number of user. |
|`fields_to_export` | Optional | Array of strings | Name of user data fields to export. Defaults to all if not provided. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Example request
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/export/ids' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "external_ids": ["user_identifier1", "user_identifier2"],
  "user_aliases": [{
    "alias_name": "example_alias",
    "alias_label": "example_label"
  }],
  "device_id": "1234567",
  "braze_id": "braze_identifier",
  "email_address": "example@braze.com",
  "phone": "+11112223333",
  "fields_to_export": ["first_name", "email", "purchases"]
}'
```

## Fields to export

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

Be aware that the `/users/export/ids` endpoint will pull together the entire user profile for this user, including data such as all campaigns and Canvases received, all custom events performed, all purchases made, and all custom attributes. As a result, this endpoint is slower than other REST API endpoints.

Depending on the data requested, this API endpoint may not be sufficient to meet your needs due to the 2,500 requests per minute rate limit. If you anticipate using this endpoint regularly to export users, instead consider exporting users by segment, which is asynchronous and more optimized for larger data pulls.

## Response

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "users" : (array of object) the data for each of the exported users, may be empty if no users are found,
    "invalid_user_ids" : (optional, array of string) each of the identifiers provided in the request that did not correspond to a known user
}
```

For an example of the data that is accessible via this endpoint see the following example.

### Sample user export file output

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
            "google_ad_id" : (string) only included for Android devices when Google Play Advertising Identifier collection is enabled,
            "roku_ad_id" : (string) only included for Roku devices,
            "windows_ad_id" : (string) only included for Windows devices,
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
            "sessions" : (integer),
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
                "clicked_triggered_in_app_message" : (bool)
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

{% alert tip %}
For help with CSV and API exports, visit [Export troubleshooting]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
