---
hidden: true
nav_title: "POST: Update Live Activity"
article_title: "POST: Update Live Activity"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "This article outlines details about the Update Live Activity endpoint."

---
{% api %}
# Update Live Activity
{% apimethod post %}
/messages/live_activity/update
{% endapimethod %}

Use this endpoint to handle updates for Live Activities displayed by your iOS app.

Before using this endpoint, you must register an activity with the Braze Swift SDK using the [`launchActivity`](braze-swift-sdk/documentation/brazekit/braze/liveactivities-swift.class/launchactivity(pushtokentag:activity:fileid:line:)) method. Required request parameters will be defined during this step. See the [Live Activities article]({{site.baseurl}}/docs/developer_guide/platform_integration_guides/swift/live_activities/) for more information on registration.

## Rate limit

<!--What is the rate limit? -->

{% multi_lang_include rate_limits.md endpoint='default' category='message endpoints' %}

## Request parameters

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `app_id` | Required | String | App [API identifier]({{site.baseurl}}/api/identifier_types/#the-app-identifier) retrieved from the **Developer Console**.  |
| `activity_id` | Required | String | Lorem ipsum. |
| `content_state` | Required | Object | Lorem ipsum. |
| `end_activity` | Optional | Boolean | If `true`, this request ends the Live Activity. |
| `dismissal_date` | Optional | Datetime <br>([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) string) | This parameter defines the time to remove the Live Activity from the user's UI. If this time is in the past, the Live Activity will be removed immediately. |
| `stale_date` | Optional | Datetime <br>([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) string) | This parameter tells the system when the Live Activity content is marked as outdated in the user's UI. |
| `notification` | Optional | Object | Include an [`apple_push`]({{site.baseurl}}/api/objects_filters/messaging/apple_object/) object to define a push notification that will also be displayed with this update. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## Example Request

<!--Is "apple_push" needed or helpful in the sample request below, or is it just clutter?-->

```javascript
curl --location --request POST 'https://rest.iad-01.braze.com/messages/live_activity/update \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {YOUR-REST-API-KEY}' \
--data-raw '{
    "app_id": "{YOUR-APP-API-IDENTIFIER}",
    "activity_id": "halftimeScore",
    "content_state": {
        "team1Score": 2,
        "team2Score": 4
    },
    "end_activity": false,
    "dismissal_date": "2023-02-28T00:00:00+0000",
    "stale_date": "2023-02-27T16:55:49+0000",
    "notification": {
        "apple_push": {
            "alert": "Halftime!",
            "badge": 1
        }
    }
}
```

## Response

<!--What are the status codes that can be returned for this endpoint? What troubleshooting is available for customers? -->

There are XX status code responses for this endpoint: `201`, XX, and XX.

### Response parameters

<!--Are there any response params worth mentioning, or are they all messages from the server?-->

### Example success response

The status code `201` could return the following response body.

```json
{
  "message": "success"
}
```

### Example error response

The status code `400` could return the following response body. Refer to the [API errors and responses article]({{site.baseurl}}/api/errors/) for more information about errors you may encounter.

<!--Can you please include an example error response here? -->

```json

```

{% endapi %}