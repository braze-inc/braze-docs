---
nav_title: "POST: Send transactional emails using API-triggered delivery"
article_title: "POST: Send Transactional Emails Using API-Triggered Delivery"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "This article outlines details about the Send transactional email messages using API-triggered delivery Braze endpoint."

---

{% api %}
# Send transactional emails using API-triggered delivery
{% apimethod post %}
/transactional/v1/campaigns/{campaign_id}/send
{% endapimethod %}

> Use this endpoint to send immediate, one-off transactional messages to a designated user.

This endpoint is used alongside the creation of a Braze [Transactional Email campaign]({{site.baseurl}}/api/api_campaigns/transactional_campaigns) and corresponding campaign ID.

{% alert important %}
Transactional Email is currently available as part of select Braze packages. Contact your Braze customer success manager for more details.
{% endalert %}

Similar to the [Send triggered campaign endpoint]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/), this campaign type allows you to house message content inside of the Braze dashboard while dictating when and to whom a message is sent via your API. Unlike the Send triggered campaign endpoint, which accepts an audience or segment to send messages to, a request to this endpoint must specify a single user either by `external_user_id` or `user_alias`, as this campaign type is purpose-built for 1:1 messaging of alerts like order confirmations or password resets.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#cec874e1-fa51-42a6-9a8d-7fc57d6a63bc {% endapiref %}

## Prerequisites

To use this endpoint, you'll need to generate an API key with the `transactional.send` permission.

## Rate limit

{% multi_lang_include rate_limits.md endpoint='transactional email' %}

## Path parameters

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `campaign_id` | Required | String | ID of the campaign |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Request body

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "external_send_id": (optional, string) see the following request parameters,
  "trigger_properties": (optional, object) personalization key-value pairs that apply to the user in this request,
  "recipient": (required, object)
    {
      // Either "external_user_id" or "user_alias" is required. Requests must specify only one.
      "user_alias": (optional, User alias object) User alias of the user to receive message,
      "external_user_id": (optional, string) External identifier of user to receive message,
      "attributes": (optional, object) fields in the attributes object create or update an attribute of that name with the given value on the specified user profile before the message is sent and existing values are overwritten
    }
}
```

## Request parameters

| Parameter | Required | Data Type | Description |
| --------- | ---------| --------- | ----------- |
|`external_send_id`| Optional | String |  A Base64 compatible string. Validated against the following regex:<br><br> `/^[a-zA-Z0-9-_+\/=]+$/` <br><br>This optional field allows you to pass an internal identifier for this particular send, which is included in events sent from the Transactional HTTP event postback. When passed, this identifier is also used as a deduplication key, which Braze stores for 24 hours. <br><br>Passing the same identifier in another request does not result in a new instance of a send by Braze for 24 hours.|
|`trigger_properties`|Optional|Object|See [trigger properties]({{site.baseurl}}/api/objects_filters/trigger_properties_object/). Personalization key-value pairs that apply to the user in this request. |
|`recipient`|Required|Object| The user you are targeting this message to. Can contain `attributes` and a single `external_user_id` or `user_alias`.<br><br>Note that if you provide an external user ID that doesn't already exist in Braze, passing any fields to the `attributes` object creates this user profile in Braze and sends this message to the newly created user. <br><br>If you send multiple requests to the same user with different data in the `attributes` object, `first_name`, `last_name`, and `email` attributes are updated synchronously and templated into your message. Custom attributes don't have this same protection, so proceed with caution when updating a user through this API and passing different custom attribute values in quick succession.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

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
        "recipient": {
          "external_user_id": TARGETED_USER_ID_STRING
        }
      }' \
  https://rest.iad-01.braze.com/transactional/v1/campaigns/{campaign_id}/send
```

## Response

The Send transactional email endpoint responds with the message's `dispatch_id` which represents the instance of this message send. This identifier can be used along with events from the Transactional HTTP event postback to trace the status of an individual email sent to a single user.

### Example responses

```json
{
    "dispatch_id": A randomly-generated unique ID of the instance of this send
    "status": Current status of the message
    "metadata" : Object containing additional information about the send instance
}
```

## Troubleshooting

The endpoint may also return an error code and a human-readable message in some cases, most of which are validation errors. Here are some common errors you may get when making invalid requests.

| Error | Troubleshooting |
| ----- | --------------- |
| `The campaign is not a transactional campaign. Only transactional campaigns may use this endpoint` | The campaign ID provided is not for a transactional campaign. |
| `The external reference has been queued.  Please retry to obtain send_id.` | The external_send_id has been created recently, try a new external_send_id if you are intending to send a new message. |
| `Campaign does not exist` | The campaign ID provided does not correspond to an existing campaign. |
| `The campaign is archived. Unarchive the campaign in order for trigger requests to take effect.` | The campaign ID provided corresponds to an archived campaign. |
| `The campaign is paused. Resume the campaign in order for trigger requests to take effect.` | The campaign ID provided corresponds to a paused campaign. |
| `campaign_id must be a string of the campaign api identifier` | The campaign ID provided is not a valid format. |
| `Error authenticating credentials` | The API key provided is invalid |
| `Invalid whitelisted IPs `| The IP address sending the request is not on the IP whitelist (if it is being used) |
| `You do not have permission to access this resource` | The API key used does not have permission to take this action |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Most endpoints at Braze have a rate limit implementation that returns a 429 response code if you have made too many requests. The transactional sending endpoint works differently—if you exceed your allotted rate limit, our system continues to ingest the API calls, return success codes, and send the messages; however, those messages may not be subject to the contractual SLA for the feature. Contact Braze Support if you need more information about this functionality.

## Transactional HTTP event postback

{% multi_lang_include http_event_postback.md %}

{% endapi %}