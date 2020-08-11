---
nav_title: "POST: Send Transactional Messages via API Triggered Delivery"
page_order: 4
layout: api_page
page_type: reference
platform: API
tool:
  - Campaigns
hidden: true
description: "This article outlines details about the Send Transactional Message via API Triggered Delivery Braze endpoint."
---
{% api %}
# Sending Transactional Messages via API Triggered Delivery
{% apimethod post %}
/v2/transactional/campaigns/YOUR_CAMPAIGN_ID_HERE/send/
{% endapimethod %}

API Triggered Delivery allows you to house message content inside of the Braze dashboard while dictating when a message is sent, and to whom via your API.

The Send Transactional Message endpoint allows you to send immediate, ad-hoc messages to designated users. Unlike the [Send triggered campaign endpoint]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/) which accepts an audience or segment to send a message too, a transactional send must specify a single user either by External User ID or by User Alias.

Please note that to send messages with this endpoint, you must have a Campaign ID, created when you build an [Transactional Campaign]({{site.baseurl}}/api/api_campaigns/transactional_campaigns).

The Transactional campaign type is only available for certain customers. Please contact your customer success manager for more information. 

{% alert important %}
__Looking for the `api_key` parameter?__<br>As of May 2020, Braze has changed how we read API keys to be more secure. Now API keys must be passed as a request header, please see `YOUR_REST_API_KEY` within the __Example Request__ below.
{% endalert %}

## Request Body

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "external_send_id": (optional, string) see External Send Identifier,
  "trigger_properties": (optional, object) personalization key-value pairs that will apply to the user in this request,
  "recipient": (required, object)
    {
      // Either "external_user_id" or "user_alias" is required. Requests must specify only one.
      "user_alias": (optional, User Alias Object) User Alias of the user to receive message,
      "external_user_id": (optional, string) External Id of user to receive message,
      "send_to_existing_only": (optional, boolean) defaults to false,
      "attributes": (optional, object) fields in the attributes object will create or update an attribute of that name with the given value on the specified user profile before the message is sent and existing values will be overwritten
    }
}
```

### Request Parameters

| Parameter | Required | Data Type | Description |
| --------- | ---------| --------- | ----------- |
|`external_send_id`| Optional | String | Your identifier for this particular send. Passing this ID will allow it to be used as a deduplication key. Passing the same ID in another request will not result in a new instance of a send by Braze  |
|`trigger_properties`|Optional|Object|Personalization key-value pairs that will apply to the user in this request|
|`recipient`|Required|Object|The user you are targeting this message to|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

### Request Components
- [Recipients]({{site.baseurl}}/api/objects_filters/recipient_object/)
- [User Alias Object]({{site.baseurl}}/api/objects_filters/user_alias_object/)
- [User Attributes Object]({{site.baseurl}}/api/objects_filters/user_attributes_object/)
- [API Parameters]({{site.baseurl}}/api/parameters)
<br><br>
When `send_to_existing_only` is `true`, Braze will only send the message to existing users. When `send_to_existing_only` is `false` and a user with the given `external_user_id` does not exist, Braze will create a user with that id and attributes before sending the message. Note that Braze will not create a user given a user alias that does not exist.

### Example Request
```
curl -X POST \
  -H 'Content-Type:application/json' \
  -H 'Authorization: Bearer YOUR-REST-API-KEY' \
  -d '{
        "trigger_properties": {
          "example_string_property": YOUR_EXAMPLE_STRING,
          "example_integer_property": YOUR_EXAMPLE_INTEGER
        },
        "recipient": {
          "external_user_id": TARGETED_USER_ID_STRING
        }
      }' \
  https://rest.iad-01.braze.com/v2/transactional/campaigns/YOUR_TRANSACTIONAL_CAMPAIGN_ID/send
```

## Response Details
The Transactional Message sending endpoint response will include the message's `send_id` for reference back to the send of the message. This `send_id` represents the transactional message sent to this particular user at this particular time. This identifier can be used along with events from the [Transactional Currents feed]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message/#transactional-currents) to trace the message as it makes its way to the user.

### Example response
```json
{
    "send_id": Unique GUID of the instance of this send
    "status": Current status of the message
}
```

## Transactional Currents
All Transactional Messages are complimented with event status postbacks sent as an HTTP request to your specified URL. To specify your target URL to receive these postback, you can create a new Transactional Currents connection by navigating to Currents -> New Connection -> HTTP Postback Export.  

### Example Postback

```json
{
  "send_id": Unique GUID that was returned upon making the request,
  "status": Current status of message from fields below,
  "external_send_id": If provided at the time of the request, Braze will pass your identifier for this instance of a send for all postbacks
}
```

| Event Status | Description |
| ------------ | ----------- |
| `Sent` | Indicated Braze has successfully dispatched the message |
| `Aborted` | Indicated Braze was unable to successfully dispatch the message due to the user not having a valid email or Liquid abort logic |
|`Email Delivered`| Indicates the user's email inbox provider has accepted the email |
|`Email Bounced`| Indicates the user's email inbox provider has rejected the email |
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}

[41]: https://dashboard-01.braze.com/app_settings/developer_console/activitylog/
[42]: {{site.baseurl}}/api/parameters/#broadcast
