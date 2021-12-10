---
nav_title: "POST: Send Transactional Emails via API-Triggered Delivery"
article_title: "POST: Send Transactional Emails via API-Triggered Delivery"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "This article outlines details about the Send Transactional Email Messages via API-Triggered Delivery Braze endpoint."
---

{% api %}
# Sending transactional email via API-triggered delivery
{% apimethod post %}
/transactional/v1/campaigns/YOUR_CAMPAIGN_ID_HERE/send
{% endapimethod %}

The Send Transactional Email endpoint allows you to send immediate, ad-hoc messages to designated users. This endpoint is used alongside the creation of a [Transactional Email Campaign]({{site.baseurl}}/api/api_campaigns/transactional_campaigns) and corresponding Campaign ID.

{% alert important %}
Transactional Email is currently available as part of select Braze packages. Please reach out to your Braze Customer Success Manager for more details.
{% endalert %}

Similar to the [Send Triggered Campaign endpoint]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/), this campaign type allows you to house message content inside of the Braze dashboard while dictating when and to whom a message is sent via your API. Unlike the Send Triggered Campaign Endpoint which accepts an audience or segment to send messages to, a request to this endpoint must specify a single user either by External User ID or User Alias as this campaign type is purpose-built for 1:1 messaging of alerts like order confirmations or password resets.

## Request body

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "external_send_id": (optional, string) see external_send_id below,
  "trigger_properties": (optional, object) personalization key-value pairs that will apply to the user in this request,
  "recipients": (required, object)
    [{
      // Either "external_user_id" or "user_alias" is required. Requests must specify only one.
      "user_alias": (optional, User alias object) User alias of the user to receive message,
      "external_user_id": (optional, string) External identifier of user to receive message,
      "attributes": (optional, object) fields in the attributes object will create or update an attribute of that name with the given value on the specified user profile before the message is sent and existing values will be overwritten
    }]
}
```

## Request parameters

| Parameter            | Required | Data Type | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| -------------------- | -------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `external_send_id`   | Optional | String    | A Base64 compatible string. Validated against the following regex:<br><br> `/^[a-zA-Z0-9-_+\/=]+$/` <br><br>This optional field allows you to pass an internal identifier for this particular send, which will be included in events sent from the Transactional HTTP event postback. When passed, this identifier will also be used as a deduplication key, which Braze will store for 24 hours. <br><br>Passing the same identifier in another request will not result in a new instance of a send by Braze for 24 hours.                                                                                                                                                                                                                                                        |
| `trigger_properties` | Optional | Object    | See [trigger properties]({{site.baseurl}}/api/objects_filters/trigger_properties_object/). Personalization key-value pairs that will apply to the user in this request.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `recipients`         | Required | Object    | See [recipients object]({{site.baseurl}}/api/objects_filters/recipient_object/). The user you are targeting this message to. <br><br>Note that if you provide an external user ID that doesn't already exist in Braze, passing any fields to the `attributes` object will create this user profile in Braze and send this message to the newly created user. <br><br>If you send multiple requests to the same user with different data in the `attributes` object, Braze will ensure that `first_name`, `last_name`, and `email` attributes will be updated synchronously and templated into your message. Custom attributes don't have this same protection, so proceed with caution when updating a user through this API and passing different custom attribute values in quick succession. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Example request

```
curl -X POST \
  -H 'Content-Type:application/json' \
  -H 'Authorization: Bearer YOUR-REST-API-KEY' \
  -d '{
        "external_send_id" : YOUR_BASE64_COMPATIBLE_ID
        "trigger_properties": {
          "example_string_property": YOUR_EXAMPLE_STRING,
          "example_integer_property": YOUR_EXAMPLE_INTEGER
        },
        "recipients": [{
          "external_user_id": TARGETED_USER_ID_STRING
        }]
      }' \
  https://rest.iad-01.braze.com/transactional/v1/campaigns/YOUR_CAMPAIGN_ID_HERE/send
```

## Response

The Send Transactional Email endpoint will respond with the message's `dispatch_id` which represents the instance of this message send. This identifier can be used along with events from the Transactional HTTP event postback to trace the status of an individual email sent to a single user.

### Example response

```json
{
    "dispatch_id": Out-of-the-box generated Unique ID of the instance of this send
    "status": Current status of the message
    "metadata" : Object containing additional information about the send instance
}
```

### Transactional HTTP event postback

All Transactional Emails are complemented with event status postbacks sent as an HTTP request back to your specified URL. This will allow you to evaluate the message status in real-time and take action to reach the user on another channel if the message goes undelivered, or fallback to an internal system if Braze is experiencing latency.

In order to associate the incoming events to a particular instance of send, you can choose to either capture and store the Braze Dispatch ID returned in the API response as detailed above, or pass your own identifier to the `external_send_id` field. An example of a value you may choose to pass to that field may be an order ID, where after completing order 1234, an order confirmation message is triggered to the user through Braze, and `external_send_id : 1234` is included in the request. All following event postbacks such as `Sent` and `Delivered` will include `external_send_id : 1234` in the payload allowing you to confirm that user successfully received their order confirmation email.

To get started using the Transactional HTTP Event Postback, navigate to Manage Settings > Email Settings > Transactional WebPush URL in your Braze dashboard and input your desired URL to receive postbacks.

![Transactional Webhook URL Update]({% image_buster /assets/img/transactional_webhook_url.png %})


### Postback body

```json
{
  "dispatch_id": (string, Out-of-the-box generated Unique ID of the instance of this send),
  "status": (string, Current status of message from fields below)
  "metadata" : (object, additional information relating to the execution of an event)
   {
     "external_send_id" : (string, If provided at the time of the request, Braze will pass your internal identifier for this send for all postbacks),
     "campaign_api_id" : (string, API identifier of this transactional campaign),
     "received_at": (ISO 8601 DateTime string, Timestamp of when the request was received by Braze, only included for events with "sent" status),
     "enqueued_at": (ISO 8601 DateTime string, Timestamp of when the request was enqueued by Braze, only included for events with "sent" status),
     "executed_at": (ISO 8601 DateTime string, Timestamp of when the request was processed by Braze, only included for events with "sent" status),
     "sent_at": (ISO 8601 DateTime string, Timestamp of when the request was sent to the ESP by Braze, only included for events with "sent" status),
     "processed_at" : (ISO 8601 DateTime string, Timestamp the event was processed by the ESP, only included for events with "processed" status),
     "delivered_at" : (ISO 8601 DateTime string, Timestamp the event was delivered to the user's inbox provider, only included for events with "processed" status),
     "bounced_at" : (ISO 8601 DateTime string, Timestamp the event was bounced by the user's inbox provider, only included for events with "bounced" status),
     "aborted_at" : (ISO 8601 DateTime string, Timestamp the event was Aborted by Braze, only included for events with "aborted" status),
     "reason" : (string, The reason Braze or the Inbox provider was unable to process this message to the user, only included for events with "aborted" or "bounced" status),
   }
}
```

| Status      | Description                                                                                                                                                                                                                                                                |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `sent`      | Message successfully dispatched to Braze's email sending partner                                                                                                                                                                                                           |
| `processed` | Email sending partner has successfully received and prepared the message for sending to the user's inbox provider                                                                                                                                                          |
| `aborted`   | Braze was unable to successfully dispatch the message due to the user not having an emailable address, or Liquid abort logic was called in the message body. All aborted events include a `reason` field within the metadata object indicating why the message was aborted |
| `delivered` | Message was accepted by the user's email inbox provider                                                                                                                                                                                                                    |
| `bounced`   | Message was rejected by the user's email inbox provider. All bounced events include a `reason` field within the metadata object reflecting the bounce error code provided by the inbox provider                                                                            |
{: .reset-td-br-1 .reset-td-br-2}

### Example postback
```json

// Sent Event
{
    "dispatch_id": "acf471119f7449d579e8089032003ded",
    "status": "sent",
    "metadata": {
      "received_at": "2020-08-31T18:58:41.000+00:00",
      "enqueued_at": "2020-08-31T18:58:41.000+00:00",
      "executed_at": "2020-08-31T18:58:41.000+00:00",
      "sent_at": "2020-08-31T18:58:42.000+00:00",
      "campaign_api_id": "417220e4-5a2a-b634-7f7d-9ec891532368",
      "external_send_id" : "34a2ceb3cf6184132f3d816e9984269a"
    }
}

// Processed Event
{
    "dispatch_id": "acf471119f7449d579e8089032003ded",
    "status": "processed",
    "metadata": {
      "processed_at": "2020-08-31T18:58:42.000+00:00",
      "campaign_api_id": "417220e4-5a2a-b634-7f7d-9ec891532368",
      "external_send_id" : "34a2ceb3cf6184132f3d816e9984269a"
    }
}

// Aborted
{
    "dispatch_id": "acf471119f7449d579e8089032003ded",
    "status": "aborted",
    "metadata": {
      "reason": "User not emailable",
      "aborted_at": "2020-08-31T19:04:51.000+00:00",
      "campaign_api_id": "417220e4-5a2a-b634-7f7d-9ec891532368",
      "external_send_id" : "34a2ceb3cf6184132f3d816e9984269a"
    }
}

// Delivered Event
{
    "dispatch_id": "acf471119f7449d579e8089032003ded",
    "status": "delivered",
    "metadata": {
      "delivered_at": "2020-08-31T18:27:32.000+00:00",
      "campaign_api_id": "417220e4-5a2a-b634-7f7d-9ec891532368",
      "external_send_id" : "34a2ceb3cf6184132f3d816e9984269a"
    }
}

// Bounced Event
{
    "dispatch_id": "acf471119f7449d579e8089032003ded",
    "status": "bounced",
    "metadata": {
      "bounced_at": "2020-08-31T18:58:43.000+00:00",
      "reason": "550 5.1.1 The email account that you tried to reach does not exist",
      "campaign_api_id": "417220e4-5a2a-b634-7f7d-9ec891532368",
      "external_send_id" : "34a2ceb3cf6184132f3d816e9984269a"
    }
}

```


{% endapi %}

