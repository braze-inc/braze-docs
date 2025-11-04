---
nav_title: Lob
article_title: Lob 
alias: /partners/lob/
description: "This reference article outlines the partnership between Braze and Lob.com, which allows you to send direct mail-like letters, postcards, and checks through the mail."
page_type: partner
search_tag: Partner

---

# Lob

> [Lob.com](https://lob.com) is an online service that allows you to send direct mail to your users.

_This integration is maintained by Lob._

## About the integration

With this integration, you can:

- Send mail-like letters, postcards, and checks through the mail using Braze webhooks and the Lob API.
- Share Lob events with Braze as custom attributes and events using Braze Data Transformation and Lob webhooks.

## Prerequisites

|Requirement| Description|
| ---| ---|
|Lob account | A Lob account is required to take advantage of this partnership. |
| Lob API key | You Lob API key can be found under the settings section under your name in the Lob dashboard. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Sending mail using Braze webhooks

### Step 1: Choose a Lob endpoint

Depending on what you'd like to do you in Lob, you'll need to use the corresponding endpoint in your webhook's HTTP request. For detailed information on each endpoint, see [Lob's API reference documentation](https://lob.com/docs#intro).

| Base URL | Available endpoints |
| ------------ | ------------------- |
| `https://api.lob.com/` | `/v1/addresses<br>/v1/addresses/{id}`<br>`/v1/verify`<br>`/v1/postcards`<br>`/v1/postcards/{id}`<br>`/v1/letter`<br>`/v1/letter/{id}`<br>`/v1/checks<br>/v1/checks/{id}`<br>`/v1/bank_accounts`<br>`/v1/bank_accounts/{id}`<br>`/v1/bank_accounts/{id}/verify`<br>`/v1/areas<br>/v1/areas/{id}`<br>`/v1/routes/{zip_code}`<br>`/v1/routes`<br>`/v1/countries<br>/v1/states`|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Step 2: Create your Braze webhook template

To create a Lob webhook template to use in future campaigns or Canvases, go to **Templates** > **Webhook Templates** in the Braze dashboard. 

If you'd like to make a one-off Lob webhook campaign or use an existing template, select **Webhook** in Braze when creating a new campaign.

In your new Webhook template, fill out the following fields:

- **Webhook URL**: `<LOB_API_ENDPOINT>`
- **Request Body**: Raw Text

#### Request headers and method

Lob requires an HTTP Header for authorization and an HTTP method. The following will already be included within the template as a key-value pair, but in the **Settings** tab, you must replace the `<LOB_API_KEY>` with your Lob API key. This key must include a ":" directly after the key and be encoded in base 64. 

- **HTTP Method**: POST
- **Request Headers**:
  - **Authorization**: Basic `{{'<LOB_API_KEY>:' | base64_encode}}`
  - **Content-Type**: application/json

![Request body code and webhook URL shown in the Braze webhook builder compose tab.]({% image_buster /assets/img_archive/lob_full_request.png %})

#### Request body

The following is an example request body for the Lob postcards endpoint. While this request body is provided in the base Lob template in Braze, if you wish to use other endpoints, you must adjust your Liquid fields accordingly.

{% raw %}
```json
"description": "Demo Postcard",
"to": {
    "name": "{{${first_name}}} {{${last_name}}}",
    "address_line1": "{{custom_attribute.${address_line1}}}",
    "address_city": "{{custom_attribute.${address_city}}}"
    "address_zip": "{{custom_attribute.${address_zip}}}",
    "address_country": "{{custom_attribute.${address_country}}}"
},
"front": "https://lob.com/postcardfront.pdf",
"back": "https://lob.com/postcardback.pdf"
```
{% endraw %}

### Step 3: Preview your request

At this point, your campaign should be ready to test and send. Check the Lob dashboard and the Braze developer console error message logs if you run into errors. For example, the following error was caused by an incorrectly formatted authentication header. 

{% alert important %}
Remember to save your template before leaving the page! <br>Updated webhook templates can be found in the **Saved Webhook Templates** list when creating a new [webhook campaign]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/).
{% endalert %}

![A message error log showing the time, app name, channel, and error message. The error message includes the message alert and the status code.]({% image_buster /assets/img_archive/error_log.png %})

## Sharing events using Lob webhooks 

[Braze Data Transformation]({{site.baseurl}}/user_guide/data/data_transformation/overview) lets you build and manage webhooks for automating data flow from external platforms into Braze. Each transformation is given a unique endpoint, which other platforms can use for their webhook's destination.

{% alert important %}
Lob's Data Transformation template sends events using your [`/users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track), which consumes data points in Braze. We recommend setting a rate limit in your Lob webhook settings, so you can avoid over-consuming data.
{% endalert %}

### Step 1: Create a transformation in Braze

1. In the Braze Dashboard, go to **Data Settings** > **Data Transformations**, then select **Create Transformation**.
2. Enter a short, descriptive name for your transformation.
3. Under **Editing experience**, select **Use a template**, then search for Lob and check the box.
4. When you're finished, select **Create Transformation**. You'll be redirected to the transformation editor, which you'll use in the next step.

### Step 2: Fill out the Lob template

With this template, you can transform one of your Lob events into a custom event or attribute that can be used in Braze. Follow the in-line comments to finish building out the template.

{% alert tip %}
For detailed information about Lob's webhook payload structure, see [Lob: Using webhooks](https://help.lob.com/print-and-mail/getting-data-and-results/using-webhooks).
{% endalert %}

```json
// First, this code defines a variable, "brazecall", to build up a /users/track request
// Everything from the incoming webhook is accessible via the special variable "payload". As such, you can template in desired values in your /users/track request with JavaScript dot notation, such as payload.x.y.z

// In this example, this function removes the periods and underscores of the event_type.id sent in the Lob payload so that an event id that is formatted like: `letter.processed_for_delivery` will log an event to Braze with the name `letter processed for delivery`.

function formatString(input) {
    return input.replace(/[._]/g, ' ');
}

let braze_event = formatString(payload.event_type.id);

// In this example, a metadata value passed in the Lob Webhook called 'external_ID' is being used to match the Event to the corresponding Braze user.

let brazecall = {
  "attributes": [
    {
      "external_id": payload.body.metadata.external_id,
      "_update_existing_only": true,
      "Most Recent Mailer": payload.body.description
    }
  ],
  "events": [
    {
      "external_id": payload.body.metadata.external_id,
      "_update_existing_only": true,
      "name": braze_event,
      "time": new Date().toISOString(),
// Customize the properties to the Lob event you are syncing. Our example below pulls in the Tracking Events array of objects associated with certain Lob events.
      "properties": {
        "tracking_events": payload.body.tracking_events
      }
    }
  ]
};
// After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;
```

### Step 3: Create a webhook in Lob

1. When you're finished building your template, select **Activate**, then copy the **Webhook URL** to your clipboard.
2. In Lob, [create a new webhook](https://help.lob.com/print-and-mail/getting-data-and-results/using-webhooks#receiving-a-webhook-1), then use your webhook URL from Braze to receive the webhook.
