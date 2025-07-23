---
nav_title: Connecting to the Customer Data API
article_title: Connecting to the Movable Ink Customer Data API
description: "This reference article outlines how to connect to activate customer event data stored in Braze to generate personalized content within Movable Ink using the Customer Data API."
page_type: partner
search_tag: Partner
---

# Connecting to the Movable Ink Customer Data API

> Braze and Movable Ink’s Customer Data API integration allows marketers to activate customer event data stored in Braze to generate personalized content within Movable Ink.

Movable Ink is able to ingest behavioral events from Braze through their Customer Data API. The events will be stored on the user profiles based on the unique user ID (UUID) that is passed to Movable Ink.

For more information on Stories, the Movable Ink Customer Data API, and how Movable Ink leverages behavioral data, please visit the following support center articles:

- [Power content with behavioral data](https://support.movableink.com/hc/en-us/sections/360001239453-Power-content-with-behavioral-data)
- [Customer Data API Introduction and Guide](https://support.movableink.com/hc/en-us/articles/13815957200663-Customer-Data-API-introduction-and-guide)
- [FAQ: Customer Data API](https://support.movableink.com/hc/en-us/articles/12423178752279-FAQ-Customer-Data-API)

## Prerequisites

| Requirement | Description |
|---|---|
| Movable Ink account | A Movable Ink account is required to take advantage of this partnership. |
| Movable Ink API credentials | Movable Ink's Solutions team will generate API credentials for you. The API credentials consist of:{::nomarkdown}<ul><li>An endpoint URL (where the data will be sent to)</li><li>Username and password (used to authenticate the API)</li></ul>{:/} If desired, Movable Ink can supply the username and password as a base64-encoded value to be used as a basic authorization header value. |
| Behavioral event payloads | You will need to share your event payloads with your Movable Ink Client Experience team. See [Sharing event payloads](#event-payloads) with Movable Ink for details. |
| Creative assets and business logic | You will need to share creative assets with Movable Ink, including Adobe Photoshop (PSD) files directing Movable Ink on how to build the block and a fallback image. You will also need to provide business logic for how and when to display the partner-activated Content Block. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Step 1: Create a webhook campaign in Braze

#### Step 1a: Create a new campaign

1. In Braze, [create a webhook campaign]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/).
2. Give your campaign a name and optional description.
3. Select **Blank Template** as your template.

#### Step 1b: Add your Customer Data API credentials

1. In the **Webhook URL** field, enter the Movable Ink endpoint URL.

![Compose tab of the webhook composer in Braze with the Movable Ink endpoint URL and Request Body set to JSON Key/Value Pairs.]({% image_buster /assets/img/movable_ink/cd_api_webhook_url.png %}){: style="max-width:75%" }

{:start="2"}
2. Select the **Settings** tab.
3. Add the following request headers as key-value pairs:

| Key | Value |
| --- | --- |
| Content-Type | application/json |
| Authorization | Enter the Basic Authentication you received from Movable Ink. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Settings tab of the webhook composer in Braze with key-value pairs for Content-Type and Authorization.]({% image_buster /assets/img/movable_ink/cd_api_webhook_settings.png %}){: style="max-width:75%" }

#### Step 1c: Configure your payload

1. Return to the **Compose** tab.
2. For your **Request Body**, either create your own request body with JSON key-value pairs or enter your event payload as raw text. Refer to the [sample payloads](#sample-payloads) for examples of standard eCommerce events.

![Compose tab of the webhook composer in Braze with JSON key-value pairs for ID, timestamp, user ID, and event type.]({% image_buster /assets/img/movable_ink/cd_api_webhook_kvp.png %}){: style="max-width:75%" }

#### Step 1d: Test your webhook {#step-1d}

You will need to share a sample payload with your Movable Ink Client Experience team. You can generate this payload in the **Test** tab based on the payload that you have constructed.

{% alert important %}
Movable Ink recommends waiting to test your webhook in Braze until your Movable Ink Client Experience team has confirmed that they have completed the mapping and are ready to receive a test. If this mapping is not complete, you will likely receive an error when testing.
{% endalert %}

To test your webhook, do the following:

1. Select the **Test** tab.
2. Preview the message as a user to view a sample event payload for that user. You can choose between previewing as a random user, specific user, or custom user.
3. If everything looks good, click **Send test** to send a test request.

![Webhook response message in Braze showing a 200 OK response.]({% image_buster /assets/img/movable_ink/cd_api_webhook_response.png %}){: style="max-width:75%" }

### Step 2: Finalize your campaign setup

#### Step 2a: Schedule your campaign

When you're done composing and testing the webhook, [schedule your campaign]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types). 

Braze supports scheduled, action-based, and API-triggered deliveries. [Action-based delivery]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/) is usually the best fit for most behavioral event use cases. For questions about what makes sense for your use case, connect with your Braze and Movable Ink customer success managers.

For action-based delivery:

1. Specify the trigger action. This is the event that will trigger the webhook to Movable Ink.
2. Make sure the **Schedule Delay** is set to **Immediately**. Event data should be sent to Movable Ink immediately after the event occurs, without a delay.
3. Set the campaign duration by specifying a start time. An end time is likely not be applicable, however this can be set if required for the use case.

{% alert note %}
To make sure data is streamed to Movable Ink in real time, don't select **Send campaign to users in their local time zone**.
{% endalert %}

#### Step 2b: Specify your audience

Next, determine which users you want to target for this campaign. For details, refer to [Targeting users]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/targeting_users/).

Make sure not to use A/B testing in your campaign by clearing the **Control Group** checkbox. If a control group is included, a percentage of users will not have data sent to Movable Ink. All of your audience should go to the variant rather than the control group.

![A/B Testing panel in a Braze campaign with 100% variant distrubtion assigned to Variant 1, and no control group.]({% image_buster /assets/img/movable_ink/cd_api_webhook_ab.png %})

#### Step 2c: Choose conversion events (optional)

If desired, you can assign conversion events to this campaign within Braze.

However, given that the webhook is only intended to stream data, attribution at this level is likely less useful than looking at attribution at the campaign level after the behavioral data from Braze is used to personalize content.

### Step 3: Launch the campaign

Review your webhook setup and launch your campaign.

## Considerations

### Aligning on a unique user identifier

Make sure the unique user identifier (UUID) value that you're using as your `mi_u`, is available within Braze and can be included in the event payloads sent to Movable Ink.

This ensures that the behavioral events Movable Ink references when generating an image are associated with the same customer they received the behavioral events for. If the UUID value is not the same as the Braze `external_id`, the UUID must be captured and passed to Braze as an attribute or in the event properties of a Braze event to leverage this identifier.

Braze tracks user behavior across multiple platforms (such as web and mobile app), so a single user may have several distinct anonymous IDs. These IDs can be merged into the single known Stories user profile when an `identify` event is sent to Movable Ink, as long as the `identify` event includes both an anonymous identifier and the single known identifier.

Once Movable Ink receives a `user_id` for a single user, all future events for that user must include that same `user_id`.

### Sharing event payloads with Movable Ink {#event-payloads}

Before setting up the connector to Movable Ink’s Customer Data API, make sure to share your event payloads with your Movable Ink Client Experience team. This allows Movable Ink to map your events to their event schema and will prevent any rejected or failed API calls.

You can generate an event payload within Braze using any event properties. Generate a sample payload for a random user or by searching a specific user ID. Refer to [Step 1d](#step-1d) above for details.

Share this sample payload with your Movable Ink Client Experience team. Make sure that there is no sensitive personally identifiable information in the sample payload (such as email address, phone number, or full birth dates). 

To learn more about custom event properties and the expected format of data contained within properties, refer to [Custom event properties]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties).

### Known versus anonymous users

In Braze, events can be recorded under an anonymous user profile. Which identifiers are linked to the user profile during event logging depends on how the user was created (through Braze SDK or APIs) and their current stage in the user lifecycle.

#### Only forwarding Braze events for known users

In your webhook campaign, use the `External User ID` filter to target only users that have an `external_id` with the filter `External User ID` `is not blank`.

#### Forwarding Braze events for anonymous and known users

If you want to forward Braze events from anonymous users (users before an `external_id` is assigned to their profile), you'll need to decide which identifier to use as the `anonymous_id` for Movable Ink until an `external_id` becomes available. Choose an `anonymous_id` that will remain constant on your Braze user profile. You can use Liquid logic in the webhook body to decide whether to pass an `anonymous_id` or a `user_id`.

For more, refer to the example webhooks under [sample payloads](#sample-payloads).

## Example payloads

### Product view event

{% tabs local %}
{% tab Example Braze Trigger Event %}

{% raw %}

```json
{
  "events": [
    {
      "email": "test@braze.com",
      "name": "Product Viewed",
      "time": "2023-12-06T19:20:45+01:00",
      "properties": {
        "categories": [
          {
            "id": "Bathroom",
            "url": "https://example.com/cat/bathroom"
          }
        ],
        "meta": {
          "color": "green"
        },
        "title": "All-Purpose Cleaning Wipes",
        "price": 1.99,
        "id": "56544",
        "url": "https://www.example.com/variants_id/5f08cb918dcc595aa74b0fbc"
      }
    }
  ]
}
```

{% endraw %}

{% endtab %}
{% tab Expected Movable Ink Request Payload %}

{% raw %}

```
curl --location --request POST 'https://collector.movableink-dmz.com/behavioral/{{key}}' \
--header 'Authorization: Basic {{authorization}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "anonymous_id": "123-abc-678",
  "event": "product_viewed",
  "properties": {
    "categories": [
      {
        "id": "Bathroom",
        "url": "https://example.com/cat/bathroom"
      }
    ],
    "meta": {
      "color": "green"
    },
    "title": "All-Purpose Cleaning Wipes",
    "price": 1.99,
    "id": "56544",
    "url": "https://www.example.com/variants_id/5f08cb918dcc595aa74b0fbc"
  },
  "timestamp": 1257894000000,
  "timezone": "America/New_York",
  "type": "track",
  "user_id": "5c3aa83113dd490100d3d8d7"
}'

```

{% endraw %}
{% endtab %}
{% tab Example webhook %}

In this example, a hashed email address is used as the `anonymous_id` for users who do not have an `external_id`.

{% raw %}

```liquid
// Converts the timestamp of "now" to seconds since 1970 and assigns it to a local variable "timestamp"
{% assign timestamp = "now" | date: "%s" %}

// Example of md5 hashing the email address to use as the anonymous_id
{% assign anon_id = {{${email_address}}} | md5 %}

// Condition logic to determine which identifier to use. If an external_id is available use that, otherwise use the anonymous_id
{% if {{${user_id}}} %}
{% capture user_identifier %}"user_id": "{{${user_id}}}"{% endcapture %}
{% else %}
{% capture user_identifier %}"anonymous_id": "{{anon_id}}"{% endcapture %}
{% endif %}

{
  {{user_identifier}}
  "event": "product_viewed",
  "properties": {
    "categories": [
      {
        "id": "{{event_properties.${categories}[0].id}}",
        "url": "{{event_properties.${categories}[0].url}}"
      }
    ],
    "meta": {
      "color": "{{event_properties.${meta}.color}}"
    },
    "title": "{{event_properties.${title}}}",
    "price": "{{event_properties.${price}}}",
    "id": "{{event_properties.${id}}}",
    "url": "{{event_properties.${url}}}"
  },
  "timestamp": "{{timestamp}}",
  "timezone": "{{${time_zone}}}",
  "type": "track",
}

```

{% endraw %}
{% endtab %}
{% endtabs %}

### Category view event

{% tabs local %}
{% tab Example Braze Trigger Event %}

{% raw %}

```json
{
  "events": [
    {
      "external_id": "123456789",
      "name": "Category Viewed",
      "time": "2023-12-06T19:20:45+01:00",
      "properties": {
        "id": "bathroom-1",
        "title": "Bathroom Stuff",
        "url": "https://www.example.com/categories/bathroom"
      }
    }
  ]
}
```

{% endraw %}

{% endtab %}
{% tab Expected Movable Ink Request Payload %}

{% raw %}

```
curl --location --request POST 'https://collector.movableink-dmz.com/behavioral/{{key}}' \
--header 'Authorization: Basic {{authorization}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "anonymous_id": "123-abc-678",
  "event": "category_viewed",
  "properties": {
    "id": "bathroom-1",
    "title": "Bathroom Stuff",
    "url": "https://www.example.com/categories/bathroom"
  },
  "timestamp": 1257894000000,
  "timezone": "America/New_York",
  "type": "track",
  "user_id": "5c3aa83113dd490100d3d8d7"
}'
```

{% endraw %}

{% endtab %}
{% tab Example webhook %}

This example shows a webhook tracking events for only known users (users with an `external_id`).

{% raw %}

```liquid
// Converts the timestamp of "now" to seconds since 1970 and assigns it to a local variable "timestamp"
{% assign timestamp = "now" | date: "%s" %}

{
  "event": "category_viewed",
  "properties": {
    "id": "{{event_properties.${id}}}",
    "title": "{{event_properties.${title}}}",
    "url": "{{event_properties.${url}}}"
  },
  "timestamp": "{{timestamp}}",
  "timezone": "{{${time_zone}}}",
  "type": "track",
  "user_id": "{{${user_id}}}"
}

```

{% endraw %}

{% endtab %}
{% endtabs %}

### Identify event

{% tabs local %}
{% tab Example Braze Trigger Event %}

{% raw %}

```json
{
  "events": [
    {
      "external_id": "123456789",
      "name": "Account Created",
      "time": "2023-12-06T19:20:45+01:00"
    }
  ]
}
```

{% endraw %}
{% endtab %}
{% tab Expected Movable Ink Request Payload %}

{% raw %}

```
curl --location --request POST 'https://collector.movableink-dmz.com/behavioral/{{key}}' \
--header 'Authorization: Basic {{authorization}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "anonymous_id": "jg0iq5gd30dqpwn8zmx05p06mzjmjir4r8",
  "timestamp": 1257894000000,
  "timezone": "America/New_York",
  "type": "identify",
  "user_id": "mycustomerid123"
}'
```

{% endraw %}
{% endtab %}
{% tab Example webhook %}

In this example, a hashed email address is used as the `anonymous_id` for users who do not have an `external_id`.

{% raw %}

```liquid
// Converts the timestamp of "now" to seconds since 1970 and assigns it to a local variable "timestamp"
{% assign timestamp = "now" | date: "%s" %}

// Example of md5 hashing the email address to use as the anonymous_id
{% assign anon_id = {{${email_address}}} | md5 %}

{
  "anonymous_id": "{{anon_id}}",
  "timestamp": "{{timestamp}}",
  "timezone": "{{${time_zone}}}",
  "type": "identify",
  "user_id": "{{${user_id}}}"
}

```

{% endraw %}

{% endtab %}
{% endtabs %}



