---
nav_title: Regal
article_title: Regal
description: "Integrate Regal and Braze for a more consistent and personalized customer experience."
permalink: /partners/regal/
page_type: partner
search_tag: Regal
layout: dev_guide

---

# Regal

> [Regal.io][6] is the phone and SMS sales solutions built to drive more conversations so you can hit your growth goals way faster.

By integrating Regal and Braze, you can create a more consistent and personalized experience across all your customer touch points.
- Send the right next best email or push notification from Braze based on what's said in a phone conversation on Regal.
- Trigger a call in Regal when a high value customer clicks through a marketing email from Braze, but doesn't convert.

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Regal account | A Regal account is required to take advantage of this partnership. |
| Regal API key | A Regal API key will allow to send event from Braze to Regal. Email support@regal.io to get this key. |
| Braze Data Transformation | Data transformation is currently in early access. Contact your Braze customer success manager if you are interested in participating in the early access. This is necessary to receive data from Regal. |
{: .reset-td-br-1 .reset-td-br-2}

## Integration

### Sending data from Braze to Regal

Thie following section describes how to use Braze as a source for sending your customer profile and event data to Regal using Braze Canvas webhooks.

#### Step 1: Create new contacts in Regal

Build a Canvas that webhooks out to Regal every time a new contact is created in Braze who you want to be available for calls and texts in Regal. 

Below is an example Canvas for how to accomplish this, though the logic for the trigger of your Canvas may differ depending on what constitutes a relevant contact for your company to send to Regal.

1. Create a Canvas titled "Create New Contact for Regal" and select **Action-Based** as the entry type.

2. Set the trigger logic as **Custom Event** and select the event that is fired when a contact with a phone number is created. Regal also recommends adding an extra filter on the phone field that ensures it's set.

3. In your new Webhook template, fill out the following fields:<br>
**Webhook URL**: <https://events.regalvoice.com/events><br>
**Request Body**: Raw Text

##### Request headers and method

Regal.io also requires an HTTP Header for authorization and an HTTP method. The following will already be included within the template as a key-value pair, but in the **Settings** tab:
{% raw %}
- **HTTP Method**: POST
- **Request Headers**:
    - **Authorization**: `{{<REGAL_API_KEY>}}`
    - **Content-Type**: application/json
{% endraw %}
##### Request body

The only required field below is the `traits.phone` property. The rest is optional. However, if you include `optIn`, you must include `optIn.channel` and `optIn.subscribed`.

```json
{
    "userId": "<uniqueIdentifier>", //this is optional
    "traits": {
        "phone": "<phoneNumber>",
        "email": "<email>",
        "firstName": "<firstName>",
        "lastName": "<lastName>",
        "optIn": [
            {
                "channel": "voice",
                "source": "<leadSource>",
                "subscribed": true
            },
            {
                "channel": "sms",
                "source": "<leadSource>",
                "subscribed": true
            }
        ],
        "custom1": "<custom1>",
        "custom2": "<custom2>"
    },
    "eventSource": "braze"
}
```

The above payload example assumes all of your contacts have accepted opt in for voice and SMS. If that's not true, you can remove the `optIn` property from the above and set up a separate Canvas to update a contact in Regal when `optIn` is collected.

### Step 2: Update OptIn Information 

If opt in and out can happen at different parts of your user experience on your app, it's important to update Regal as users opt in or out. Below is a recommended Canvas for how to send up to date opt in information to Regal. It assumes you save this as a Braze profile field, but if not, the trigger can just as easily be an event in your Braze account that represents a user opting in or unsubscribing. (The example below is for phone opt in, but you can set up a similar Canvas for SMS opt in if you collect those separately).

1. Create a new Canvas titled "Send Opt In or Out to Regal"

2. Set the trigger node logic as "User Profile Field Updated" and select whatever field represents the user's opt in status. If instead you fire an event to Braze to represent opt in or out, use that event as the trigger instead.

3. In your new Webhook template, fill out the following fields:<br>
**Webhook URL**: <https://events.regalvoice.com/events><br>
**Request Body**: Raw Text

##### Request headers and method

Regal.io also requires an HTTP Header for authorization and an HTTP method. The following will already be included within the template as a key-value pair, but in the **Settings** tab:
{% raw %}
- **HTTP Method**: POST
- **Request Headers**:
    - **Authorization**: `{{<REGAL_API_KEY>}}`
    - **Content-Type**: application/json
{% endraw %}

##### Request body

You are welcome to add additional user profile attributes in this payload as well, if you want to ensure more attributes are up to date at the same time.

```json
{
    "userId": "<uniqueIdentifier>", //this is optional
    "traits": {
        "phone": "<phoneNumber>",
        "optIn": [
            {
                "channel": "voice",
                "source": "<leadSource>",
                "subscribed": "<voice_optin_subscribed>"
            },
            {
                "channel": "sms",
                "source": "<leadSource>",
                "subscribed": "<voice_optin_subscribed>"
            }
        ]
    },
    "eventSource": "braze"
}
```

### Step 3: Send Custom Events

Finally, set up a Canvas for each of the key events you want to send Regal - we recommend sending any events that are important for triggering SMS and Calls in Regal (such as an event at each step of the sign up or purchase flow) or will that be used as exit criteria for contacts to fall out of Regal campaigns.

For example, below is a workflow for sending Regal an event for when a user completes the first step of an Application.

1. Create a new Canvas titled "Send Application Step 1 Completed Event to Regal"
2. Set the trigger node logic as "Custom Event" and select the name of the event you want to send to Regal, such as "_Application Step 1 Completed_".
3. In your new Webhook template, fill out the following fields:<br>
**Webhook URL**: <https://events.regalvoice.com/events><br>
**Request Body**: Raw Text

##### Request headers and method

Regal.io also requires an HTTP Header for authorization and an HTTP method. The following will already be included within the template as a key-value pair, but in the **Settings** tab:
{% raw %}
- **HTTP Method**: POST
- **Request Headers**:
    - **Authorization**: `{{<REGAL_API_KEY>}}`
    - **Content-Type**: application/json
{% endraw %}

##### Request body

You are welcome to add additional user profile attributes in this payload as well, if you want to ensure more attributes are up to date at the same time.

```json
{
    "userId": "<uniqueIdentifier>", //this is optional
    "traits": {
        "phone": "<phoneNumber>",
        "firstName": "<firstName>",
        "lastName": "<lastName>",
        "custom1": "<custom1>",
        "custom2": "<custom2>",
        "custom3": "<custom3>"
    },
    "name": "Application Step 1 Completed",
    "properties": {
      "educationalLevel": "<educationalLevel>",
      "preferredLocation": "<preferredLocation>",
      "preferredSubject": "<preferredSubject>",
      "readytoCommit": true
    },
    "eventSource": "braze"
}
```

Up to Date Contact Attributes

While it's not necessary, we recommend also sending any key user profile data fields on the event payloads of your event workflows to ensure Regal has access to the most up to date contact attributes at the time key events become available.

{% alert note %}
If you have any questions about which events are important to send to Regal or how best to set up these Canvases, reach out to support@regal.io.
{% endalert %}

### Sending Data from Regal to Braze

This section describes how to get Regal reporting events like `SMS.sent` and `call.completed` into Braze so they can appear on your Braze profiles and be available for use in the Braze segmentation tool, Canvas and Campaigns. This integration uses Regal Reporting Webhooks and Braze Data Transformation to automate data flow.

### Step 1: Create a Data Transformation in Braze

{% alert note %}
Data transformation is currently in early access. Contact your Braze customer success manager if you are interested in participating in the early access.
{% endalert %}

Braze recommends creating a transformation per Regal webhook you plan to send to Braze. 

To create a Data Transformation:
- Navigate to the Transformations page in your Braze dashboard
- Give your transformation a name and click **Create transformation**
- Use the vertical menu icon to copy webhook URL

![copy_webhook_url][4]

### Step 2: Enable Reporting Webhooks in Regal

To set up Reporting Webhooks:
1. Go to Regal app and open the **Setting** page.
2. In the **Reporting Webhooks** section, click **Create Webhooks**.
3. In the webhook endpoint input, add the Braze Data Transformation webhook URL for the associated Data Transformation.

![edit_webhook][5]

Updating an endpoint
When you edit an endpoint, it can take up to 5 minutes for the cache to refresh and start sending events to your new endpoint instead.

Retries
Currently there are no retries on these events. If a response is not received within 5 seconds, the event is dropped and not retried. We will be adding retries in a future release.

#### Events

Regal's [Reporting Webhooks guide][7] includes the complete list of Reporting events that we publish. There you can see definitions of properties and sample payloads as well.

### Step 3: Transform Regal Events into Braze Events

Braze's Data Transformation feature allows you to map incoming Regal events into the format necessary to be added as attributes, events, or purchases in Braze.

To set up your data transformations in Braze, follow this documentation: <https://www.braze.com/docs/data_transformation>.

1. Name your Data Transformation. It is recommended to set up a Data Transformation per event webhook.
2. To test the connection, create an outbound call from the Regal Agent Desktop to your cell phone and submit the Conversation Summary form to create a call.completed event.
3. Determine what identifiers you will use to map your contacts in Regal to your profiles in Braze. The available identifiers in Regal events include:
   1. `userId` - only set on events if you've previously sent this identifier for a contact
   2. `traits.phone`
   3. `traits.email` - only set on events if you've previously sent this identifier for a contact

Braze supported identifiers<br>
- Braze does not support phone numbers as an identifier. To use this as an identifier the phone number can be set as a User Alias. To learn more about Braze User Aliases, please refer to this [documentation][8].
- When using Braze Data Transformation email address can be used as an identifier. If the email address already exists as a profile within Braze, the existing profile will be updated. If the email address does not yet exist within Braze an email-only profile will be created.

## Use cases

{% tabs %}
{% tab Trigger an email from based on a call %}

#### Trigger an email from Braze based on a call disposition in Regal

Below is a sample payload for a call.completed event in Regal. 

```json
{
  "userId": "123",
  "traits": {
    "phone": "+17625555555",
    "email": "xxx@gmail.com"
  },
  "name": "call.completed",
  "properties": {
    "agent_firstname": "Rebecca",
    "agent_fullname": "Rebecca Greene",
    "agent_id": "xxxx@yourbrand.com",
    "direction": "OUTBOUND",
    "regal_voice_phone": "+19545558563",
    "regal_voice_phone_internal_name": "Sales Line",
    "contact_phone": "+17625555555",
    "call_id": "WTxxxxx9",
    "type": "Outbound Call",
    "disposition": "Converted During Convo",
    "notes": null,
    "objections": null,
    "campaign_name": "Life Insurance Quote Follow Up",
    "campaign_friendly_id": "445",
    "started_at": 1657855046,
    "ended_at": 1657855053,
    "completed_at": 1657855059,
    "talk_time": 7,
    "wrapup_time": 6,
    "handle_time": 13,
    "journey_uuid": null,
    "journey_name": null,
    "journey_friendly_id": null
  },
  "originalTimestamp": "1657855059",
  "eventSource": "Regal Voice"
}
```

Below is a sample Data Transformation to map this to a custom event in Braze.

```
// Braze's /users/track endpoint expects timestamps in an ISO 8601 format. To use the Unix timestamp within Regal's call.completed event payload as the event timestamp in Braze it must first be converted to ISO 8601. This can be done with the following code:
let unixTimestamp = payload.originalTimestamp;
let dateObj = new Date(unixTimestamp * 1000);
let isoString = dateObj.toISOString();

// This is a default template that you can use as a starting point. Feel free to delete this entirely to start from scratch, or to delete specific components as you see fit.

// First, this code defines a variable, "brazecall", to build up a /users/track request
// Everything from the incoming webhook is accessible via the special variable "payload". As such, you can template in desired values in your /users/track request with JS dot notation, such as payload.x.y.z

let brazecall = {
 "events": [
   {
     "external_id": payload.userId,
     "name": "Call Completed",
     "time": isoString,
     "_update_existing_only": false,
     "properties": {
       "agent_firstname": payload.properties.agent_firstname,
       "agent_fullname": payload.properties.agent_fullname,
       "agent_id": payload.properties.agent_id,
       "direction": payload.properties.direction,
       "regal_voice_phone": payload.properties.regal_voice_phone,
       "regal_voice_phone_internal_name": payload.properties.regal_voice_phone_internal_name,
       "contact_phone": payload.properties.contact_phone,
       "call_id": payload.properties.call_id,
       "type": payload.properties.type,
       "disposition": payload.properties.disposition,
       "notes": payload.properties.notes,
       "objections": payload.properties.objections,
       "campaign_name": payload.properties.campaign_name,
       "campaign_friendly_id": payload.properties.campaign_friendly_id,
       "started_at": payload.properties.started_at,
       "ended_at": payload.properties.ended_at,
       "completed_at": payload.properties.completed_at,
       "talk_time": payload.properties.talk_time,
       "wrapup_time": payload.properties.wrapup_time,
       "handle_time": payload.properties.handle_time,
       "journey_uuid": payload.properties.journey_uuid,
       "journey_name": payload.properties.journey_name,
       "journey_friendly_id": payload.properties.journey_friendly_id
     }
   }
 ]
};

// After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;
```

{% endtab %}
{% tab Update profile attributes in Braze %}

#### Update profile attributes in Braze based on contact.attribute.edited events from Regal

Below is a sample payload for a `contact.attribute.edited` event in Regal. This event is fired each time one of your agents learns something new in a conversation and updates an attribute on the contact's profile.

```json
{
  "userId": "123",
  "traits": {
    "phone": "+17625555555",
    "email": "xxx@gmail.com",
  },
  "name": "contact.attribute.edited",
  "properties": {
    "agent_email": "xxxx@yourbrand.com",
    "contact_phone": "+17625555555",
    "changes": {
      "custom_properties": {
        "annual_income": {
          "old_value": "150,000",
          "new_value": "300,000"
        }
      }
    },
    "created_at": "1657855462"
  },
  "originalTimestamp": "1657855462",
  "eventSource": "Regal Voice"
}
```

Below is a sample Data Transformation to map the new custom property values to the relevant attributes on your Braze profiles:

```
// This is an example template that you can use as a starting point. Feel free to delete this entirely to start from scratch, or to delete specific components as you see fit

// Capture the key's updated property value within the 'changes' object and store this in an attributes variable that can be used in the /users/track request

const changes = payload.properties.changes.custom_properties;

const attributes = {};
for (const key in changes) {
 attributes[key] = changes[key].new_value;
}

// First, this code defines a variable, "brazecall", to build up a /users/track request
// Everything from the incoming webhook is accessible via the special variable "payload". As such, you can template in desired values in your /users/track request with JS dot notation, such as payload.x.y.z

const brazecall = {
 "attributes": [
   {
     "external_id": payload.userId,
     "_update_existing_only": false,
     ...attributes
   }
 ]
};

// After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;
```

{% endtab %}
{% tab Keep your experiments in Braze %}

#### Keep your experiments in Braze and Regal in sync using `contact.experiment.assigned` events

Below is a sample payload for a contact.experiment.assigned event in Regal.

```json
{
  "userId": "123",
  "traits": {
    "phone": "+17625555555",
    "email": "xxx@gmail.com",
  },
  "name": "contact.experiment.assigned",
  "properties": {
    "experiment_name": "Post Call Offer Test",
    "experiment_id": "xxxx-xxxx-xxxx-xxxx",
    "experiment_variant": "Aggressive Offer - 50%",
    "journey_uuid": "xxxx-xxxx-xxxx-xxxx",
    "journey_friendly_id": 220,
    "journey_name": "Post Call Follow Up"
  },
  "originalTimestamp": "1657855118",
  "eventSource": "Regal Voice"
}
```

Below is a sample Data Transformation to map this to a custom event in Braze.

```
// Braze's /users/track endpoint expects timestamps in an ISO 8601 format. To use the Unix timestamp within Regal's call.completed event payload as the event timestamp in Braze it must first be converted to ISO 8601. This can be done with the following code:
let unixTimestamp = payload.originalTimestamp;
let dateObj = new Date(unixTimestamp * 1000);
let isoString = dateObj.toISOString();

// This is an example template that you can use as a starting point. Feel free to delete this entirely to start from scratch, or to delete specific components as you see fit

// First, this code defines a variable, "brazecall", to build up a /users/track request
// Everything from the incoming webhook is accessible via the special variable "payload". As such, you can template in desired values in your /users/track request with JS dot notation, such as payload.x.y.z
let brazecall = {
 "events": [
   {
     "external_id": payload.userId,
     "_update_existing_only": false,
     "name": "Contact Experiment Assigned",
     "time": isoString,
     "properties": {
       "experiment_name": payload.properties.experiment_name,
       "experiment_id": payload.properties.experiment_id,
       "experiment_variant": payload.properties.experiment_variant,
       "journey_uuid": payload.properties.journey_uuid,
       "journey_friendly_id": payload.properties.journey_friendly_id,
       "journey_name": payload.properties.journey_name
     }
   }
 ]
};

// After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;

```
{% endtab %}
{% tab Unsubscribe a contact %}

#### Unsubscribe a contact in Braze based on a `contact.unsubscribed` from Regal

Below is a sample payload for a `contact.unsubscribed` event in Regal.

```json
{
  "userId": "123",
  "traits": {
    "phone": "+17625555555",
    "email": "xxx@gmail.com",
    "ip": "78.97.213.166"
  },
  "name": "contact.unsubscribed",
  "properties": {
    "new_subscription": true,
    "channel": "voice",
    "text": null,
    "ip": "207.38.149.143",
    "source": "regalvoice.agent_desktop",
    "timestamp": "1657855229"
  },
  "originalTimestamp": "1657855230",
  "eventSource": "Regal Voice"
}
```

Below is a sample Data Transformation to unsubscribe the contact in Braze.

```
// This is an example template that you can use as a starting point. Feel free to delete this entirely to start from scratch, or to delete specific components as you see fit

// First, this code defines a variable, "brazecall", to build up a /users/track request
// Everything from the incoming webhook is accessible via the special variable "payload". As such, you can template in desired values in your /users/track request with JS dot notation, such as payload.x.y.z

let brazecall = {
 "attributes": [
   {
     "external_id": payload.userId,
     "_update_existing_only": true,
     "subscription_groups" : [{
       "subscription_group_id": "YOUR SUBSCRIPTION GROUP ID",
       "subscription_state": "unsubscribed"
     }]
   }
 ]
};

// After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;
```

{% endtab %}
{% endtabs %}

[2]: {% image_buster /assets/img/regal/webhook_rawtext.png %}
[3]: {% image_buster /assets/img/regal/request_header.png %}
[4]: {% image_buster /assets/img/regal/copy_webhook_url.png %}
[5]: {% image_buster /assets/img/regal/edit_webhook.png %}
[6]: https://regal.io
[7]: https://developer.regal.io/docs/reporting-webhooks#events
[8]: https://www.braze.com/docs/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases