---
nav_title: "POST: Export user profile by identifier"
article_title: "POST: Export User Profile by Identifier"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "This article outlines details about the Export users by identifier Braze endpoint."

---
{% api %}
# Export user profile by identifier
{% apimethod post %}
/users/export/ids
{% endapimethod %}

> Use this endpoint to export data from any user profile by specifying a user identifier.

Up to 50 `external_ids` or `user_aliases` can be included in a single request. Should you want to specify `device_id`, `email_address`, or `phone`, only one of these identifiers can be included per request.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#b9750447-9d94-4263-967f-f816f0c76577 {% endapiref %}

## Prerequisites

To use this endpoint, you'll need an [API key]({{site.baseurl}}/api/basics#rest-api-key/) with the `users.export.ids` permission.

## Rate limit

{% multi_lang_include rate_limits.md endpoint='users export ids' %}

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
  "fields_to_export": (optional, array of strings) Name of user data fields to export
}
```

{% alert note %}
For customers who have onboarded with Braze on or after August 22, 2024, the request parameter `fields_to_export` is required.
{% endalert %}

## Request parameters

| Parameter          | Required | Data Type                                                     | Description                                                                                  |
| ------------------ | -------- | ------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `external_ids`     | Optional | Array of strings                                              | External identifiers for users you wish export.                                              |
| `user_aliases`     | Optional | Array of user alias object                                    | [User aliases]({{site.baseurl}}/api/objects_filters/user_alias_object/) for users to export. |
| `device_id`        | Optional | String                                                        | Device identifier, as returned by various SDK methods such as `getDeviceId`.                 |
| `braze_id`         | Optional | String                                                        | Braze identifier for a particular user.                                                      |
| `email_address`    | Optional | String                                                        | Email address of user.                                                                       |
| `phone`            | Optional | String in [E.164](https://en.wikipedia.org/wiki/E.164) format | Phone number of user.                                                                        |
| `fields_to_export` | Optional* | Array of strings                                              | Name of user data fields to export.<br><br>*This field is required to use the faster rate limit of 40 requests per second. If omitted, the default rate limit of 250 requests per min will be used instead. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

*Required for customers who have onboarded with Braze on or after August 22, 2024.

## Example request
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/export/ids' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "external_ids": ["user_identifier1", "user_identifier2"],
  "user_aliases": [
    {
      "alias_name": "example_alias",
      "alias_label": "example_label"
    }
  ],
  "device_id": "1234567",
  "braze_id": "braze_identifier",
  "email_address": "example@braze.com",
  "phone": "11112223333",
  "fields_to_export": ["first_name", "email", "purchases"]
}'
```

## Fields to export

The following is a list of valid `fields_to_export`. Using `fields_to_export` to minimize the data returned can improve response time of this API endpoint:

| Field to export       | Data type       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| --------------------- | --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `apps`                | Array           | Apps this user has logged sessions for, which includes the fields:<br><br>- `name`: app name<br>- `platform`: app platform, such as iOS, Android, or Web<br>- `version`: app version number or name <br>- `sessions`: total number of sessions for this app<br>- `first_used`: date of first session<br>- `last_used`: date of last session<br><br>All fields are strings.                                                                                                                                                                                                                                                                                       |
| `attributed_campaign` | String          | Data from [attribution integrations]({{site.baseurl}}/partners/message_orchestration/), if set up. Identifier for a particular ad campaign.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `attributed_source`   | String          | Data from [attribution integrations]({{site.baseurl}}/partners/message_orchestration/), if set up. Identifier for the platform the ad was on.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `attributed_adgroup`  | String          | Data from [attribution integrations]({{site.baseurl}}/partners/message_orchestration/), if set up. Identifier for an optional sub-grouping below campaign.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `attributed_ad`       | String          | Data from [attribution integrations]({{site.baseurl}}/partners/message_orchestration/), if set up. Identifier for an optional sub-grouping below campaign and ad group.                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `push_subscribe`      | String          | User's push subscription status.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `email_subscribe`     | String          | User's email subscription status.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `braze_id`            | String          | Device-specific unique user identifier set by Braze for this user.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `country`             | String          | User's country using [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) standard.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `created_at`          | String          | Date and time for when the user profile was created, in ISO 8601 format.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `custom_attributes`   | Object          | Custom attribute key-value pairs for this user.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `custom_events`       | Array           | Custom events attributed to this user in the last 90 days.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `devices`             | Array           | Information about the user's device, which could include the following depending on platform:<br><br>- `model`: Device's model name<br>- `os`: Device's operating system<br>- `carrier`: Device's service carrier, if available<br>- `idfv`: (iOS) Braze device identifier, the Apple Identifier for Vendor, if exists<br>- `idfa`: (iOS) Identifier for Advertising, if exists<br>- `device_id`: (Android) Braze device identifier<br>- `google_ad_id`: (Android) Google Play Advertising Identifier, if exists<br>- `roku_ad_id`: (Roku) Roku Advertising Identifier<br>- `ad_tracking_enabled`: If ad tracking is enabled on the device, can be true or false |
| `dob`                 | String          | User's date of birth in the format `YYYY-MM-DD`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `email`               | String          | User's email address.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `external_id`         | String          | Unique user identifier for identified users.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `first_name`          | String          | User's first name.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `gender`              | String          | User's gender. Possible values are:<br><br>- `M`: male<br>- `F`: female<br>- `O`: other<br>- `N`: not applicable<br>- `P`: prefer not to say<br>- `nil`: unknown                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `home_city`           | String          | User's home city.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `language`            | String          | User's language in ISO-639-1 standard.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `last_coordinates`    | Array of floats | User's most recent device location, formatted as `[longitude, latitude]`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `last_name`           | String          | User's last name.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `phone`               | String          | User's telephone number in E.164 format.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `purchases`           | Array           | Purchases this user has made in the last 90 days.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `push_tokens`         | Array           | Unique anonymous identifier that specifies where to send an app's notifications.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `random_bucket`       | Integer         | User's [random bucket number]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/customer_behavior_events#random-bucket-number-event), used to create uniformly distributed segments of random users.                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `time_zone`           | String          | User's time zone in the same format as the IANA Time Zone Database.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `total_revenue`       | Float           | Total revenue attributed to this user. Total revenue is calculated based on purchases the user made during conversion windows for the campaigns and Canvases they received.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `uninstalled_at`      | Timestamp       | Date and time the user uninstalls the app. Omitted if the app has not been uninstalled.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `user_aliases`        | Object          | [User aliases object]({{site.baseurl}}/api/objects_filters/user_alias_object#user-alias-object-specification) containing the `alias_name` and `alias_label`, if exists.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Be aware that the `/users/export/ids` endpoint will pull together the entire user profile for this user, including data such as all campaigns and Canvases received, all custom events performed, all purchases made, and all custom attributes. As a result, this endpoint is slower than other REST API endpoints.

Depending on the data requested, this API endpoint may not be sufficient to meet your needs due to the 250 requests per minute rate limit. If you anticipate using this endpoint regularly to export users, instead consider exporting users by segment, which is asynchronous and more optimized for larger data pulls.

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

For an example of the data that is accessible through this endpoint see the following example.

### Example user export file output

User export object (we will include the least data possible - if a field is missing from the object it should be assumed to be null or empty):

{% tabs %}
{% tab All fields %}

```json
{
    "created_at": (string),
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
    "country" : (string) ISO-3166-1 alpha-2 standard,
    "phone" : (string),
    "language" : (string) ISO-639-1 standard,
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
        "idfv" : (string) only included for iOS devices when IDFV collection is enabled,
        "idfa" : (string) only included for iOS devices when IDFA collection is enabled,
        "google_ad_id" : (string) only included for Android devices when Google Play Advertising Identifier collection is enabled,
        "roku_ad_id" : (string) only included for Roku devices,
        "ad_tracking_enabled" : (boolean)
      },
      ...
    ],
    "push_tokens" : [
      {
        "app" : (string) app name,
        "platform" : (string),
        "token" : (string),
        "device_id": (string),
        "notifications_enabled": (boolean) whether the user's push notifications are turned on or turned off
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
        "engaged" :
         {
           "opened_email" : (boolean),
           "opened_push" : (boolean),
           "clicked_email" : (boolean),
           "clicked_triggered_in_app_message" : (boolean)
          },
          "converted" : (boolean),
          "api_campaign_id" : (string),
          "variation_name" : (optional, string) exists only if it is a multivariate campaign,
          "variation_api_id" : (optional, string) exists only if it is a multivariate campaign,
          "in_control" : (optional, boolean) exists only if it is a multivariate campaign
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
        "in_control": (boolean),
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

{% endtab %}
{% tab Sample output %}

```json
{
    "created_at" : "2020-07-10 15:00:00.000 UTC",
    "external_id" : "A8i3mkd99",
    "user_aliases" : [
      {
        "alias_name" : "user_123",
        "alias_label" : "amplitude_id"
      }
    ],
    "braze_id": "5fbd99bac125ca40511f2cb1",
    "random_bucket" : 2365,
    "first_name" : "Jane",
    "last_name" : "Doe",
    "email" : "example@braze.com",
    "dob" : "1980-12-21",
    "home_city" : "Chicago",
    "country" : "US",
    "phone" : "+442071838750",
    "language" : "en",
    "time_zone" : "Eastern Time (US & Canada)",
    "last_coordinates" : [41.84157636433568, -87.83520818508256],
    "gender" : "F",
    "total_revenue" : 65,
    "attributed_campaign" : "braze_test_campaign_072219",
    "attributed_source" : "braze_test_source_072219",
    "attributed_adgroup" : "braze_test_adgroup_072219",
    "attributed_ad" : "braze_test_ad_072219",
    "push_subscribe" : "opted_in",
    "push_opted_in_at": "2020-01-26T22:45:53.953Z",
    "email_subscribe" : "subscribed",
    "custom_attributes":
    {
      "loyaltyId": "37c98b9d-9a7f-4b2f-a125-d873c5152856",
      "loyaltyPoints": "321",
       "loyaltyPointsNumber": 107
    },
    "custom_events": [
      {
        "name": "Loyalty Acknowledgement",
        "first": "2021-06-28T17:02:43.032Z",
        "last": "2021-06-28T17:02:43.032Z",
        "count": 1
      },
      ...
    ],
    "purchases": [
      {
        "name": "item_40834",
        "first": "2021-09-05T03:45:50.540Z",
        "last": "2022-06-03T17:30:41.201Z",
        "count": 10
      },
      ...
    ],
    "devices": [
      {
        "model": "Pixel XL",
        "os": "Android (Q)",
        "carrier": null,
        "device_id": "312ef2c1-83db-4789-967-554545a1bf7a",
        "ad_tracking_enabled": true
      },
      ...
    ],
    "push_tokens": [
      {
        "app": "MovieCanon",
        "platform": "Android",
        "token": "12345abcd",
        "device_id": "312ef2c1-83db-4789-967-554545a1bf7a",
        "notifications_enabled": true
      },
      ...
    ],
    "apps": [
      {
        "name": "MovieCannon",
        "platform": "Android",
        "version": "3.29.0",
        "sessions": 1129,
        "first_used": "2020-02-02T19:56:19.142Z",
        "last_used": "2021-11-11T00:25:19.201Z"
      },
      ...
    ],
    "campaigns_received": [
      {
        "name": "Email Unsubscribe",
        "api_campaign_id": "d72fdc84-ddda-44f1-a0d5-0e79f47ef942",
        "last_received": "2022-06-02T03:07:38.105Z",
        "engaged":
        {
           "opened_email": true
        },
        "converted": true,
        "multiple_converted":
        {
          "Primary Conversion Event - A": true
        },
        "in_control": false,
        "variation_name": "Variant 1",
        "variation_api_id": "1bddc73a-a134-4784-9134-5b5574a9e0b8"
      },
      ...
    ],
    "canvases_received": [
      {
        "name": "Non Global  Holdout Group 4/21/21",
        "api_canvas_id": "46972a9d-dc81-473f-aa03-e3473b4ed781",
        "last_received_message": "2021-07-07T20:46:24.136Z",
        "last_entered": "2021-07-07T20:45:24.000+00:00",
        "variation_name": "Variant 1",
        "in_control": false,
        "last_entered_control_at": null,
        "last_exited": "2021-07-07T20:46:24.136Z",
        "steps_received": [
          {
            "name": "Step",
            "api_canvas_step_id": "43d1a349-c3c8-4be1-9fbe-ce708e4d1c39",
            "last_received": "2021-07-07T20:46:24.136Z"
          },
          ...
        ]
      }
      ...
    ],    
    "cards_clicked" : [
      {
        "name" : "Loyalty Promo"
      },
      ...
    ]
}
```

{% endtab %}
{% endtabs %}

{% alert tip %}
For help with CSV and API exports, visit [Export troubleshooting]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
