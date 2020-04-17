---
nav_title: Attributes Object in Campaigns & Canvas
permalink: "/create_send/"
---

# Attributes Object in Campaigns & Canvas

> Braze has a new Messaging Object called `Attributes` that will allow you to add, create, or update attribute and values for a user before you send them an API Triggered Campaign using the `campaign/trigger/send` endpoint, as this API call will process the Attributes object before it processes and sends the campaign.

When user information is sent to Braze via the `users/track` endpoint, it may occasionally take a few seconds for the user to be created in Braze's system or for the data to propagate to the user's profile.

When requests are made to the `users/track` and `messaging` endpoints at around the same time, Braze cannot guarantee that the request to the `users/track` endpoint will be processed before the request to the `messaging` endpoint. This can result in race conditions that can impact messaging: for example, a user may not yet have been created in Braze's system when a request to the `campaigns/trigger/send` endpoint is processed, resulting in the user not receiving an API-triggered push campaign.

This is especially useful when you want to guarantee that a user has been created or that new data has populated to a user's profile before a message is sent to a user.

_For example, you might want to send an order confirmation to a customer that just registered. Because the user's email information is not yet in Braze, you'll want to make sure that Braze processes the user's email address before the order confirmation campaign is sent to them._

_Another example is ensuring that user attributes needed for campaign segmentation are processed before the campaign is sent. You might have a segment on your API triggered campaign that references an attribute value like gender, which is provided by the user during the registration process. If the attribute isn't updated on the user's profile before the campaign segmentation is evaluated, the user will not get the campaign._

Use the Attributes Object in this endpoint to guarantee that:

- Users are created before a request to the `campaigns/trigger/send` endpoint is processed.
- User attributes are updated before a request to the `campaign/trigger/send` endpoint is processed.

{% alert important %}
This attribute object will __not__ create anonymous users by user alias.
{% endalert %}

Attributes that are included in this object will be processed __before__ Braze begins to send the campaign. If the ```send_to_existing_only``` flag is set to false, and an `external_user_id` does not exist in Braze's database, Braze will create a user profile for the `external_user_id` and process the associated attributes to the user profile before Braze begins to send the campaign.

## Send Campaign Messages Immediately via API Triggered Delivery

API-Triggered Delivery allows you to house message content inside of the Braze dashboard, while dictating when a message is sent, and to whom via API.

Instance  | REST Endpoint
----------|------------------------------------------------
US-01 | `https://rest.iad-01.braze.com/campaigns/trigger/send`
US-02 | `https://rest.iad-02.braze.com/campaigns/trigger/send`
US-03 | `https://rest.iad-03.braze.com/campaigns/trigger/send`
US-04 | `https://rest.iad-04.braze.com/campaigns/trigger/send`
US-06 | `https://rest.iad-06.braze.com/campaigns/trigger/send`
EU-01 | `https://rest.fra-01.braze.eu/campaigns/trigger/send`

### Send API-Triggered Campaigns Sample Request Body

```json
POST https://YOUR_REST_API_URL/campaigns/trigger/send
Content-Type: application/json

{
  "api_key": (required, string) see App Group REST API Key,
  "campaign_id": (required, string) see Campaign Identifier,
  "send_id": (optional, string) see Send Identifier,
  "trigger_properties": (optional, object) personalization key-value pairs that will apply to all users in this request,
  "recipients": (optional, array) if not provided and broadcast is not set to 'false', message will send to entire segment targeted by the campaign [
    {
      "user_alias": (optional, User Alias Object) User Alias of user to receive message,
      "external_user_id": (optional, string) External Id of user to receive message,
      "trigger_properties": (optional, object) personalization key-value pairs that will apply to this user - these key-value pairs will override any keys that conflict with trigger_properties above,
      "send_to_existing_only": (optional, boolean) defaults to true,
      "attributes": (optional, object) fields in the attributes object will create or update an attribute of that name with the given value on the specified user profile before the message is sent and existing values will be overwritten
    },
    ...
  ]
}
```

The Attributes Object should be populated with fields listed [here]({{site.baseurl}}/api/endpoints/user_data/#user-attributes-object-specification).

{% alert important %}
- Either `external_user_id` or `user_alias` is required for this call. Requests must specify only one.
- When `send_to_existing_only` is `true`, Braze will only send the message to existing users. When `send_to_existing_only` is `false` and a user with the given `id` does not exist, Braze will create a user with that id and attributes before sending the message.
{% endalert %}



## Send Canvas Messages Immediately via API Triggered Delivery

API-Triggered Delivery allows you to house message content inside of the Braze dashboard, while dictating when a message is sent, and to whom via API.

Instance  | REST Endpoint
----------|------------------------------------------------
US-01 | `https://rest.iad-01.braze.com/canvas/trigger/send`
US-02 | `https://rest.iad-02.braze.com/canvas/trigger/send`
US-03 | `https://rest.iad-03.braze.com/canvas/trigger/send`
US-04 | `https://rest.iad-04.braze.com/canvas/trigger/send`
US-06 | `https://rest.iad-06.braze.com/canvas/trigger/send`
EU-01 | `https://rest.fra-01.braze.eu/canvas/trigger/send`
{: .reset-td-br-1 .reset-td-br-2}

### Send API-Triggered Canvas Sample Request Body

```json
POST https://YOUR_REST_API_URL/campaigns/trigger/send
Content-Type: application/json

{
  "api_key": (required, string) see App Group REST API Key,
  "canvas_id": (required, string) your Canvas Identifier,
  "canvas_entry_properties": (optional, string) sets of key value pairs which define your Canvas Entry,
  "broadcast": (optional, boolean) defaults to false,
  "recipients": (optional, array) if not provided and broadcast is not set to 'false', message will send to entire segment targeted by the campaign [
    {
      "external_user_id": (optional, string) External Id of user to receive message,
      "send_to_existing_only": (optional, boolean) defaults to true,
      "attributes": (optional, object) fields in the attributes object will create or update an attribute of that name with the given value on the specified user profile before the message is sent and existing values will be overwritten
    },
    ...
  ]
}
```

The Attributes Object should be populated with fields listed [here]({{site.baseurl}}/api/endpoints/user_data/#user-attributes-object-specification).

{% alert important %}
- Either `external_user_id` or `user_alias` is required for this call. Requests must specify only one.
- When `send_to_existing_only` is `true`, Braze will only send the message to existing users. When `send_to_existing_only` is `false` and a user with the given `id` does not exist, Braze will create a user with that id and attributes before sending the message.
{% endalert %}
