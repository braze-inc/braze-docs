---
nav_title: "Connected audience filter & object"
article_title: API Connected Audience Object
page_order: 3
page_type: reference
description: "This article explains the connected audience object, including how it works, use cases, and the different filters that create it."

---

# Connected audience object

> A connected audience is a dynamic audience filter you define inline within your API request, so you can target the right users at send time without creating or managing segments in the Braze dashboard.

Instead of pre-building a segment for every possible audience combination, you pass filter criteria directly in the `audience` parameter of your API call. Braze evaluates each user against those criteria in real time and delivers the message only to users who match. This means a single API-triggered campaign or Canvas can serve an unlimited number of audience variations, driven entirely by your business logic.

## How it works

1. **Create an API-triggered campaign or Canvas** in the Braze dashboard. Define the message content and channel, and use [trigger properties]({{site.baseurl}}/api/objects_filters/trigger_properties_object/) or [Canvas context]({{site.baseurl}}/api/objects_filters/context_object/) for dynamic personalization.
2. **Call a supported endpoint** and include the `audience` parameter with your filter criteria. You can filter on custom attributes, push subscription status, email subscription status, and last-used-app time.
3. **Braze evaluates the filters at send time**, delivering the message only to users who match your criteria.

Because the audience is defined per request, your back-end systems can trigger contextually relevant messages in response to any business event (a price change, a weather alert, a live score update) without dashboard intervention.

### Compatible endpoints

You can use the connected audience object with the `audience` parameter on these endpoints:

- [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/)
- [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/)
- [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)
- [`/messages/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages/)
- [`/campaigns/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns/)
- [`/canvas/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases/)

## Use cases

Connected audiences are well-suited for scenarios where your back-end systems detect an event and need to notify a dynamically determined set of users, such as the following:

| Category | Example |
| --- | --- |
| Weather alerts | A weather data provider detects a severe weather event and sends push notifications to users whose `preferred_city` attribute matches the affected area. |
| Sports and live events | A sports app sends real-time score updates or match alerts to users whose `favorite_team` attribute matches one of the teams playing. |
| Content and entertainment | A streaming service notifies users whose `favorite_shows` array includes a series title whenever a new episode is released. |
| E-commerce | An online retailer sends price-drop or back-in-stock alerts to users whose `wishlisted_products` array includes the relevant product ID. |
| Travel | A travel app sends flight-delay notifications to users whose `booked_flight` attribute matches the affected flight number. |
| Financial services | A trading platform alerts users whose `watchlist` array includes a stock ticker that has crossed a price threshold. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

In each case, a single API-triggered campaign handles all variations. Your back end determines the filter values and passes them in the API request, so you don't need to create a separate segment or campaign for each product, show, team, or location.

## Example request

The following example uses the [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/) endpoint to target users who have favorited a specific show and are opted in to push notifications:

```json
{
  "campaign_id": "YOUR_CAMPAIGN_ID",
  "audience": {
    "AND": [
      {
        "custom_attribute": {
          "custom_attribute_name": "favorite_shows",
          "comparison": "includes_value",
          "value": "Example Show"
        }
      },
      {
        "push_subscription_status": {
          "comparison": "is",
          "value": "opted_in"
        }
      }
    ]
  },
  "trigger_properties": {
    "show_title": "Example Show",
    "episode_title": "Season 3, Episode 1",
    "deep_link": "https://example.com/shows/example-show/s3e1"
  },
  "broadcast": true
}
```

## Object body

The connected audience object is composed of either a single connected audience filter or several connected audience filters combined with `AND` and `OR` operators.

**Multiple filter example:**

```json
{
  "AND":
    [
      Connected Audience Filter,
      {
        "OR" :
          [
            Connected Audience Filter,
            Connected Audience Filter
          ]
      },
      Connected Audience Filter
    ]
}
```

## Connected audience filters

Combine multiple filters with `AND` and `OR` operators to create a connected audience filter.

### Custom attribute filter

This filter allows you to segment based on a user's custom attribute. These filters contain up to three fields:

```json
{
  "custom_attribute":
    {
      "custom_attribute_name": (String) the name of the custom attribute to filter on,
      "comparison": (String) one of the allowed comparisons to make against the provided value,
      "value": (String, Numeric, Boolean) the value to be compared using the provided comparison
    }
}
```

#### Allowed comparisons by data type

The custom attribute's data type determines the comparisons that are valid for a given filter.

| Custom Attribute Type | Allowed Comparisons |
| ---------------------| --------------- |
| String | `equals`, `not_equal`, `matches_regex`, `does_not_match_regex`, `exists`, `does_not_exist` |
| Array | `includes_value`, `does_not_include_value`, `exists`, `does_not_exist` |
| Numeric | `equals`, `not_equal`, `greater_than`, `greater_than_or_equal_to`, `less_than`, `less_than_or_equal_to`, `exists`, `does_not_exist` |
| Boolean | `equals`, `not_equal`, `exists`, `does_not_exist` |
| Time | `less_than_x_days_ago`, `greater_than_x_days_ago`, `less_than_x_days_in_the_future`, `greater_than_x_days_in_the_future`, `after`, `before`, `exists`, `does_not_exist` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Attribute comparison caveats

| Comparison | Additional considerations |
| --- | --- |
| `value` | The `value` is not required when using the `exists` or `does_not_exist` comparisons. `value` must be an ISO 8601 datetime string when using the `before` and `after` comparisons. |
|`matches_regex` | When using the `matches_regex` comparison, the value passed must be a string. To read more about using regular expressions with Braze, refer to [Regular expressions]({{site.baseurl}}/user_guide/engagement_tools/segments/regex/#regex-with-braze) and [Custom attribute data types]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#custom-attribute-data-types). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Custom attribute example

```json
{
  "custom_attribute":
    {
      "custom_attribute_name": "eye_color",
      "comparison": "equals",
      "value": "blue"
    }
}
```

```json
{
  "custom_attribute":
  {
    "custom_attribute_name": "favorite_foods",
    "comparison": "includes_value",
    "value": "pizza"
  }
}
```

```json
{
  "custom_attribute":
  {
    "custom_attribute_name": "last_purchase_time",
    "comparison": "less_than_x_days_ago",
    "value": 2
  }
}
```
### Push subscription filter

This filter allows you to segment based on a user's push subscription status.

#### Filter body

```json
{
  "push_subscription_status":
  {
    "comparison": (String) one of the following allowed comparisons,
    "value": (String) one of the following allowed values
  }
}
```

- **Allowed comparisons:** `is`, `is_not`
- **Allowed values:** `opted_in`, `subscribed`, `unsubscribed`

### Email subscription filter

This filter allows you to segment based on a user's email subscription status.

#### Filter body

```json
{
  "email_subscription_status":
  {
    "comparison": (String) one of the following allowed comparisons,
    "value": (String) one of the following allowed values
  }
}
```

- **Allowed comparisons:** `is`, `is_not`
- **Allowed values:** `opted_in`, `subscribed`, `unsubscribed`

### Last used app filter

This filter allows you to segment based on when the user last used the app. These filters contain two fields:

#### Filter body
```json
{
  "last_used_app":
  {
    "comparison": (String) one of the allowed comparisons listed,
    "value": (String) the value to be compared using the provided comparison
  }
}
```

- **Allowed comparisons:** `after`, `before`
- **Allowed values:** datetime (ISO 8601 string)

### Considerations

Connected audiences cannot filter users by default attributes, custom events, segments, or message engagement events. To use these filters, we recommend incorporating them into an audience segment and then specifying that segment in the `segment_id` parameter for the [`/messages/send` endpoint]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages#request-parameters). When using other endpoints, you'll need to add the segment to the API-triggered campaign or Canvas in the Braze dashboard first.
