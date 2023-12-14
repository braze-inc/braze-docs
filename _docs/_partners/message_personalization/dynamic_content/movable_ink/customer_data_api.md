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
- [Connect to the Customer Data API](https://support.movableink.com/hc/en-us/articles/10252591570071)
- [FAQ: Customer Data API](https://support.movableink.com/hc/en-us/articles/12423178752279-FAQ-Customer-Data-API)

## Prerequisites

| Requirement | Description |
|---|---|
| Movable Ink account | A Movable Ink account is required to take advantage of this partnership. |
| Movable Ink API credentials | Movable Ink's Solutions team will generate API credentials for you. The API credentials consist of:{::nomarkdown}<ul><li>An endpoint URL (where the data will be sent to)</li><li>Username and password (used to authenticate the API)</li></ul>{:/} If desired, Movable Ink can supply the username and password as a base64-encoded value to be used as a basic authorization header value. |
| Behavioral event payloads | |
| Creative assets | |
| Business logic | |
{: .reset-td-br-1 .reset-td-br-2}

## Integration

### Step 1: Create a webhook campaign in Braze

#### Step 1a: Create a new campaign

1. In Braze, [create a webhook campaign][1].
2. Give your campaign a name and optional description.
3. Select **Blank Template** as your template.

#### Step 1b: Add your Customer Data API credentials

1. In the **Webhook URL** field, enter the Movable Ink endpoint URL.

![][img1]{: style="max-width:75%" }

{:start="2"}
2. Select the **Settings** tab.
3. Add the following request headers as key-value pairs:

| Key | Value |
| --- | --- |
| Content-Type | application/json |
| Authorization | Enter the Basic Authentication you received from Movable Ink. |
{: .reset-td-br-1 .reset-td-br-2}

![][img2]{: style="max-width:75%" }

#### Step 1c: Configure your payload

1. Return to the **Compose** tab.
2. For your **Request Body**, either create your own request body with JSON key-value pairs, or enter your event payload as raw text. Refer to the [sample payloads](#sample-payloads) for examples of standard eCommerce events.

![][img3]{: style="max-width:75%" }

#### Step 1d: Test your webhook

You will need to share a sample payload with your Movable Ink Client Experience team. You can generate this payload in the **Test** tab based on the payload that you have constructed.

{% alert important %}
Movable Ink recommends waiting to test your webhook in Braze until your Movable Ink Client Experience team has confirmed that they have completed the mapping and are ready to receive a test. If this mapping is not complete, you will likely receive an error when testing.
{% endalert %}

To test your webhook, do the following:

1. Select the **Test** tab.
2. Preview the message as a user to view a sample event payload for that user. You can choose between previewing as a random user, specific user, or custom user.
3. If everything looks good, click **Send test** to send a test request.

![][img4]{: style="max-width:75%" }

### Step 2: Finalize your campaign setup



## Considerations

### Aligning on a UUID

### Sharing event payloads with Movable Ink

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/
[img1]: {% image_buster /assets/img/movable_ink/cd_api_webhook_url.png %}
[img2]: {% image_buster /assets/img/movable_ink/cd_api_webhook_settings.png %}
[img3]: {% image_buster /assets/img/movable_ink/cd_api_webhook_kvp.png %}
[img4]: {% image_buster /assets/img/movable_ink/cd_api_webhook_response.png %}