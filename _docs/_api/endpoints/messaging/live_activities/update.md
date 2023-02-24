---
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

Use this endpoint to LOREM IPSUM IPSUM LOREM.

## Rate limit

<!--What is the rate limit? -->

{% multi_lang_include rate_limits.md endpoint='default' category='message endpoints' %}

## Request parameters

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `app_id` | Required | apiKey | The API key for the app displaying the live activity must be included in your request. |
| `activity_id` | Required | string | Lorem ipsum. |
| `content_state` | Required | object | Lorem ipsum. |
| `end_activity` | Optional | boolean | Lorem ipsum. |
| `dismissal_date` | Optional | string in ISO 8601 format | Lorem ipsum. |
| `stale_date` | Optional | string in ISO 8601 format | Lorem ipsum. |
| `notification` | Optional | Apple push object | Lorem ipsum. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## Example Request

```javascript
curl --location --request POST 'https://rest.iad-03.braze.com/catalogs/restaurants/items/restaurant1' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {YOUR-REST-API-KEY}' \
--data-raw '{
  "app_id": (required, App API Key),
  "activity_id": (required, string),
  "content_state": (required, object) - shape should match the integrator’s app’s custom live activity integration,
  "end_activity": (optional, boolean) - if specified, end this activity for recipients,
  "dismissal_date": (optional, ISO 8601 date string) - if supplied, a custom time to remove the activity from the user's UI - if in the past, will remove immediately.
  "stale_date": (optional, ISO 8601 date string) - if supplied, a time to mark this update as outdated in the user's UI,
  "notification": (optional, Apple Push Object) - if supplied, a notification to display along with this update
}

```

## Response

There are three status code responses for this endpoint: `201`, `400`, and `404`.

### Example success response

The status code `201` could return the following response body.

```json
{
  "message": "success"
}
```

### Example error response

The status code `400` could return the following response body. Refer to the [API errors and responses article]({{site.baseurl}}/api/errors/) for more information about errors you may encounter.

```json

```

{% endapi %}