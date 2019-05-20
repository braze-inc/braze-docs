---
nav_title: Messaging
page_order: 3
search_rank: 5
local_redirect: #parameter-definitions
  hashtag-name-here: '/docs/api/parameters/'
local_redirect: #app-group-rest-api-key
  hashtag-name-here: '/docs/api/parameters/'
local_redirect: #app-identifier
  hashtag-name-here: '/docs/api/parameters/'
local_redirect: #external-user-id
  hashtag-name-here: '/docs/api/parameters/'
local_redirect: #segment-identifier
  hashtag-name-here: '/docs/api/parameters/'
local_redirect: #campaign-identifier
  hashtag-name-here: '/docs/api/parameters/'
local_redirect: #canvas-identifier
  hashtag-name-here: '/docs/api/parameters/'
local_redirect: #send-identifier
  hashtag-name-here: '/docs/api/parameters/'
local_redirect: #trigger-properties
  hashtag-name-here: '/docs/api/parameters/'
local_redirect: #canvas-entry-properties
  hashtag-name-here: '/docs/api/parameters/'
local_redirect: #broadcast
  hashtag-name-here: '/docs/api/parameters/'
local_redirect: #server-responses
  hashtag-name-here: '/docs/api/errors/'
local_redirect: #messaging-queued
  hashtag-name-here: '/docs/api/errors/'
local_redirect: #responses-for-tracked-send-ids
  hashtag-name-here: '/docs/api/errors/'
local_redirect: #fatal-errors
  hashtag-name-here: '/docs/api/errors/'
---
# Messaging

## Overview

The Braze messaging API provides you with two distinct options for sending messages to your users. You can provide the message contents and configuration in the API request with the `/messages/send` and `/messages/schedule` endpoints. Alternatively, you can manage the details of your message with an API-Triggered Delivery campaign in the dashboard and just control when and to whom it is sent with the `campaigns/trigger/send` and `campaigns/trigger/schedule` endpoints. The following sections will detail the request specification for both methods.

The examples below contain the URL https://rest.iad-01.braze.com, but some customers will need to use a different endpoint URL, for example if you are hosted in Braze's EU data center or have a dedicated Braze installation. Your Success Manager will inform you if you should use a different endpoint URL.

>  Similarly to other campaigns, you can limit the number of times a particular user can receive a Messaging API campaign by configuring [re-eligibility settings][40] in the Braze Dashboard. Braze will not deliver API messages to users that haven't become re-eligible for the campaign regardless of how many API requests are sent.

##  Send Endpoints

The send endpoint allows you to send immediate, ad-hoc messages to designated users. If you are targeting a segment, a record of your request will be stored in the [Developer Console][41].

{% raw %}
### Sending Messages Immediately via API Only

Instance  | REST Endpoint
----------|------------------------------------------------
US-01 | `https://rest.iad-01.braze.com/messages/send`
US-02 | `https://rest.iad-02.braze.com/messages/send`
US-03 | `https://rest.iad-03.braze.com/messages/send`
US-04 | `https://rest.iad-04.braze.com/messages/send`
US-06 | `https://rest.iad-06.braze.com/messages/send`
EU-01 | `https://rest.fra-01.braze.eu/messages/send`

```json
POST https://YOUR_REST_API_URL/messages/send
Content-Type: application/json
{
   "api_key": (required, string) see App Group REST API Key,
   // You will need to include at least one of 'segment_id', 'external_user_ids', and 'audience'
   // Including 'segment_id' will send to members of that segment
   // Including 'external_user_ids' and/or 'user_aliases' will send to those users
   // Including both will send to the provided users if they are in the segment
   "broadcast": (optional, boolean) see Broadcast -- defaults to false on 8/31/17, must be set to true if no external_user_ids or aliases are provided,
   "external_user_ids": (optional, array of strings) see External User ID,
   "user_aliases": (optional, array of User Alias Object) see User Alias,
   "segment_id": (optional, string) see Segment Identifier,
   "audience": (optional, Connected Audience Object) see Connected Audience,
   "campaign_id": (optional, string) see Campaign Identifier,
   "send_id": (optional, string) see Send Identifier,
   "override_frequency_capping": (optional, bool) ignore frequency_capping for campaigns, defaults to false,
   "recipient_subscription_state": (optional, string) use this to send messages to only users who have opted in ('opted_in'), only users who have subscribed or are opted in ('subscribed') or to all users, including unsubscribed users ('all'), the latter being useful for transactional email messaging. Defaults to 'subscribed',
   "messages": {
     "apple_push": (optional, Apple Push Object),
     "android_push": (optional, Android Push Object),
     "windows_phone8_push": (optional, Windows Phone 8 Push Object),
     "windows_universal_push": (optional, Windows Universal Push Object),
     "kindle_push": (optional, Kindle/FireOS Push Object),
     "web_push": (optional, Web Push Object),
     "email": (optional, Email Object)
     "content_card": (optional, Content Card Object)
   }
 }
```
For more information on the "broadcast" flag, see [Broadcast][42] below.

### Sending Messages via API Triggered Delivery

API Triggered Delivery allows you to house message content inside of the Braze dashboard, while dictating when a message is sent, and to whom via your API. Please see this section of [Braze Academy for further details][39].

Instance  | REST Endpoint
----------|------------------------------------------------
US-01 | `https://rest.iad-01.braze.com/campaigns/trigger/send`
US-02 | `https://rest.iad-02.braze.com/campaigns/trigger/send`
US-03 | `https://rest.iad-03.braze.com/campaigns/trigger/send`
US-04 | `https://rest.iad-04.braze.com/campaigns/trigger/send`
US-06 | `https://rest.iad-06.braze.com/campaigns/trigger/send`
EU-01 | `https://rest.fra-01.braze.eu/campaigns/trigger/send`

##### Campaigns

```json
POST https://YOUR_REST_API_URL/campaigns/trigger/send
Content-Type: application/json
{
  "api_key": (required, string) see App Group REST API Key,
  "campaign_id": (required, string) see Campaign Identifier,
  "send_id": (optional, string) see Send Identifier,
  "trigger_properties": (optional, object) personalization key-value pairs that will apply to all users in this request,
  "broadcast": (optional, boolean) see Broadcast -- defaults to false on 8/31/17, must be set to true if "recipients" is omitted,
  "audience": (optional, Connected Audience Object) see Connected Audience,
  // Including 'audience' will only send to users in the audience
  "recipients": (optional, array; if not provided and broadcast is not set to 'false', message will send to entire segment targeted by the campaign) [
    {
      // Either "external_user_id" or "user_alias" is required. Requests must specify only one.
      "user_alias": (optional, User Alias Object) User Alias of user to receive message,
      "external_user_id": (optional, string) External Id of user to receive message,
      "trigger_properties": (optional, object) personalization key-value pairs that will apply to this user (these key-value pairs will override any keys that conflict with trigger_properties above)
    },
    ...
  ]
}
```
For more information on the "broadcast" flag, see [Broadcast][42] below.

##### Canvas

```json
POST https://YOUR_REST_API_URL/canvas/trigger/send
Content-Type: application/json
{
  "api_key": (required, string) see App Group REST API Key,
  "canvas_id": (required, string) see Canvas Identifier,
  "canvas_entry_properties": (optional, object) personalization key-value pairs that will apply to all users in this request,
  "broadcast": (optional, boolean) see Broadcast -- defaults to false on 8/31/17, must be set to true if "recipients" is omitted,
  "audience": (optional, Connected Audience Object) see Connected Audience,
  // Including 'audience' will only send to users in the audience
  "recipients": (optional, array; if not provided and broadcast is not set to 'false', message will send to the entire segment targeted by the Canvas) [
    {
      // Either "external_user_id" or "user_alias" is required. Requests must specify only one.
      "user_alias": (optional, User Alias Object) User Alias of user to receive message,
      "external_user_id": (optional, string) External Id of user to receive message,
      "canvas_entry_properties": (optional, object) personalization key-value pairs that will apply to this user (these key-value pairs will override any keys that conflict with canvas_entry_properties above)
    },
    ...
  ]
}
```
For more information on the "broadcast" flag, see [Broadcast][42] below.

>  The `recipients` array may contain up to 50 objects, with each object containing a single `external_user_id` string and `canvas_entry_properties` object.

>  Customers using the API for server-to-server calls may need to whitelist the appropriate API URL if they're behind a firewall.

>  If you include both specific users in your API call and a target segment in the dashboard, the message will send to specifically the user profiles that are in the API call *and* qualify for the segment filters.

##  Schedule Endpoints

The schedule endpoints allow you to send messages at a designated time and modify or cancel messages that you have already scheduled.

###  Create Schedule Endpoint

The create schedule endpoint allows you to schedule a Campaign, Canvas, or other message to be sent at a designated time and provides you with an identifier to reference that message for updates. If you are targeting a segment, a record of your request will be stored in the [Developer Console][41] after all scheduled messages have been sent.

Instance  | REST Endpoint
----------|-----------------------------------------------------------
US-01 | `https://rest.iad-01.braze.com/messages/schedule/create`
US-02 | `https://rest.iad-02.braze.com/messages/schedule/create`
US-03 | `https://rest.iad-03.braze.com/messages/schedule/create`
US-04 | `https://rest.iad-04.braze.com/messages/schedule/create`
US-06 | `https://rest.iad-06.braze.com/messages/schedule/create`
EU-01 | `https://rest.fra-01.braze.eu/messages/schedule/create`

#### Scheduling Messages

Use this endpoint to send messages directly from the API.

```json
POST https://YOUR_REST_API_URL/messages/schedule/create
Content-Type: application/json
{
  "api_key": (required, string) see App Group REST API Key,
  // You will need to include at least one of 'segment_id', 'external_user_ids', and 'audience'
  // Including 'segment_id' will send to members of that segment
  // Including 'external_user_ids' and/or 'user_aliases' will send to those users
  // Including both a Segment and users will send to the provided users if they are in the segment
  "broadcast": (optional, boolean) see Broadcast -- defaults to false on 8/31/17, must be set to true if users are not specified,
  "external_user_ids": (optional, array of strings) see External User ID,
  "user_aliases": (optional, array of User Alias Object) see User Alias,
  "audience": (optional, Connected Audience Object) see Connected Audience,
  "segment_id": (optional, string) see Segment Identifier,
  "campaign_id": (optional, string) see Campaign Identifier,
  "send_id": (optional, string) see Send Identifier,
  "override_messaging_limits": (optional, bool) ignore global rate limits for campaigns, defaults to false,
  "recipient_subscription_state": (optional, string) use this to send messages to only users who have opted in ('opted_in'), only users who have subscribed or are opted in ('subscribed') or to all users, including unsubscribed users ('all'), the latter being useful for transactional email messaging. Defaults to 'subscribed',
  "schedule": {
    "time": (required, datetime as ISO 8601 string) time to send the message,
    "in_local_time": (optional, bool),
    "at_optimal_time": (optional, bool),
  },
  "messages": {
    "apple_push": (optional, Apple Push Object),
    "android_push": (optional, Android Push Object),
    "windows_push": (optional, Windows Phone 8 Push Object),
    "windows8_push": (optional, Windows Universal Push Object),
    "kindle_push": (optional, Kindle/FireOS Push Object),
    "web_push": (optional, Web Push Object),
    "email": (optional, Email object)
    "webhook": (optional, Webhook object)
    "content_card": (optional, Content Card Object)
  }
}
```
For more information on the "broadcast" flag, see [Broadcast][42] below.

#### Schedule API Triggered Campaigns and Canvases

##### API Triggered Campaigns

Use this endpoint to trigger API Triggered Campaigns, which are created on the Dashboard and initiated via the API. You can pass in `trigger_properties` that will be templated into the message itself.

```json
POST https://YOUR_REST_API_URL/campaigns/trigger/schedule/create
Content-Type: application/json
{
  "api_key": (required, string) see App Group REST API Key,
  "campaign_id": (required, string) see Campaign Identifier,
  "send_id": (optional, string) see Send Identifier,
  // Including 'recipients' will send only to the provided user ids if they are in the campaign's segment
  "recipients": (optional, Array of Recipient Object),
  // for any keys that conflict between these trigger properties and those in a Recipient Object, the value from the
  // Recipient Object will be used
  "audience": (optional, Connected Audience Object) see Connected Audience,
  // Including 'audience' will only send to users in the audience
  // If 'recipients' and 'audience' are not provided and broadcast is not set to 'false',
  // the message will send to entire segment targeted by the campaign
  "broadcast": (optional, boolean) see Broadcast -- defaults to false on 8/31/17, must be set to true if "recipients" object is omitted,
  "trigger_properties": (optional, object) personalization key-value pairs for all users in this send; see Trigger Properties,
  "schedule": {
    "time": (required, datetime as ISO 8601 string) time to send the message,
    "in_local_time": (optional, bool),
    "at_optimal_time": (optional, bool),
  }
}
```
For more information on the "broadcast" flag, see [Broadcast][42] below.

##### API Triggered Canvases

Use this endpoint to trigger API Triggered Canvases, which are created on the Dashboard and initiated via the API. You can pass in `canvas_entry_properties` that will be templated into the messages sent by the first steps of the Canvas.

```json
POST https://YOUR_REST_API_URL/canvas/trigger/schedule/create
Content-Type: application/json
{
  "api_key": (required, string) see App Group REST API Key,
  "canvas_id": (required, string) see Canvas Identifier,
  // Including 'recipients' will send only to the provided user ids if they are in the campaign's segment
  "recipients": (optional, Array of Recipient Object),
  // for any keys that conflict between these trigger properties and those in a Recipient Object, the value from the
  // Recipient Object will be used
  "audience": (optional, Connected Audience Object) see Connected Audience,
  // Including 'audience' will only send to users in the audience
  // If 'recipients' and 'audience' are not provided and broadcast is not set to 'false',
  // the message will send to entire segment targeted by the Canvas
  "broadcast": (optional, boolean) see Broadcast -- defaults to false on 8/31/17, must be set to true if "recipients" object is omitted,
  "canvas_entry_properties": (optional, object) personalization key-value pairs for the first step for all users in this send; see Trigger Properties,
  "schedule": {
    "time": (required, datetime as ISO 8601 string) time to send the message,
    "in_local_time": (optional, bool),
    "at_optimal_time": (optional, bool),
  }
}
```
For more information on the "broadcast" flag, see [Broadcast][42] below.

##### The Schedule Object

The parameters for the Campaign and Canvas schedule creation endpoints mirror those of the sending endpoint and add the `schedule` parameter, which allows you to specify when you want your targeted users to receive your message. If you include only the `time` parameter in the `schedule` object, all of your users will be messaged at that time. If you set `in_local_time` to be true, your users will receive the message at the designated date and time in their respective timezones. If `in_local_time`is true, you will get an error response if the `time` parameter has passed in your company's time zone. If you set `at_optimal_time` to be true, your users will receive the message at the designated date at the [optimal time][33] for them (regardless of the time you provide). When using local or optimal time sending, do not provide time zone designators in the value of the time parameter (e.g. just give us `"2015-02-20T13:14:47"` instead of `"2015-02-20T13:14:47-05:00"`).

The response will provide you with a `schedule_id` that you should save in case you later need to cancel or update the message you schedule:

```json
Content-Type: application/json
{
  "schedule_id" : (required, string) identifier for the scheduled message that was created
}
```

>  Customers using the API for server-to-server calls may need to whitelist the appropriate API URL if they're behind a firewall.

###  Update Schedule Endpoint

The update schedule endpoint allows you to change the schedule or message contents of a scheduled message you previously created.

Instance  | REST Endpoint
----------|-----------------------------------------------------------
US-01 | `https://rest.iad-01.braze.com/messages/schedule/update`
US-02 | `https://rest.iad-02.braze.com/messages/schedule/update`
US-03 | `https://rest.iad-03.braze.com/messages/schedule/update`
US-04 | `https://rest.iad-04.braze.com/messages/schedule/update`
US-06 | `https://rest.iad-06.braze.com/messages/schedule/update`
EU-01 | `https://rest.fra-01.braze.eu/messages/schedule/update`

#### Update Message Schedule

The messages update schedule endpoint accepts updates to either the `schedule` or `messages` parameter or both. Your request must contain at least one of those two keys.

```json
POST https://YOUR_REST_API_URL/messages/schedule/update
Content-Type: application/json
{
  "api_key": (required, string) see App Group REST API Key,
  "schedule_id": (required, string) the schedule_id to update (obtained from the response to create schedule),
  "schedule": {
    // optional, see create schedule documentation
  },
  "messages": {
    // optional, see create schedule documentation
  }
}
```

#### Update API Triggered Campaign or Canvas Schedules

Instance  | REST Endpoint
----------|-----------------------------------------------------------
US-01 | `https://rest.iad-01.braze.com/trigger/schedule/create`
US-02 | `https://rest.iad-02.braze.com/trigger/schedule/create`
US-03 | `https://rest.iad-03.braze.com/trigger/schedule/create`
US-04 | `https://rest.iad-04.braze.com/trigger/schedule/create`
US-06 | `https://rest.iad-06.braze.com/trigger/schedule/create`
EU-01 | `https://rest.fra-01.braze.eu/trigger/schedule/create`

##### API Triggered Campaigns

```json
POST https://YOUR_REST_API_URL/campaigns/trigger/schedule/update
Content-Type: application/json
{
  "api_key": (required, string) see App Group REST API Key,
  "campaign_id": (required, string) see Campaign Identifier,
  "schedule_id": (required, string) the schedule_id to update (obtained from the response to create schedule),
  "schedule": {
    // required, see create schedule documentation
  }
}
```

##### API Triggered Canvases

```json
POST https://YOUR_REST_API_URL/canvas/trigger/schedule/update
Content-Type: application/json
{
  "api_key": (required, string) see App Group REST API Key,
  "canvas_id": (required, string) see Canvas Identifier,
  "schedule_id": (required, string) the schedule_id to update (obtained from the response to create schedule),
  "schedule": {
    // required, see create schedule documentation
  }
}
```

##### Updating API Triggered Campaigns and Canvases

Any schedule will completely overwrite the one that you provided in the create schedule request or in previous update schedule requests. For example, if you originally provide `"schedule" : {"time" : "2015-02-20T13:14:47", "in_local_time" : true}` and then in your update you provide `"schedule" : {"time" : "2015-02-20T14:14:47"}`, your message will now be sent at the provided time in UTC, not in the user's local time. Scheduled triggers that are updated very close to or during the time they were supposed to be sent will be updated with best efforts, so last second changes could be applied to all, some, or none of your targeted users.

###  Delete Schedule Endpoint

The delete schedule endpoint allows you to cancel a message that you previously scheduled before it has been sent.

#### Delete Message Schedule

Instance  | REST Endpoint
----------|-----------------------------------------------------------
US-01 | `https://rest.iad-01.braze.com/messages/schedule/delete`
US-02 | `https://rest.iad-02.braze.com/messages/schedule/delete`
US-03 | `https://rest.iad-03.braze.com/messages/schedule/delete`
US-04 | `https://rest.iad-04.braze.com/messages/schedule/delete`
US-06 | `https://rest.iad-06.braze.com/messages/schedule/delete`
EU-01 | `https://rest.fra-01.braze.eu/messages/schedule/delete`

```json
POST https://YOUR_REST_API_URL/messages/schedule/delete
Content-Type: application/json
{
  "api_key": (required, string) see App Group REST API Key,
  "schedule_id": (required, string) the schedule_id to delete (obtained from the response to create schedule)
}
```

#### Delete Scheduled API Trigger Campaign

Instance  | REST Endpoint
----------|-----------------------------------------------------------
US-01 | `https://rest.iad-01.braze.com/trigger/schedule/delete`
US-02 | `https://rest.iad-02.braze.com/trigger/schedule/delete`
US-03 | `https://rest.iad-03.braze.com/trigger/schedule/delete`
US-04 | `https://rest.iad-04.braze.com/trigger/schedule/delete`
US-06 | `https://rest.iad-06.braze.com/trigger/schedule/delete`
EU-01 | `https://rest.fra-01.braze.eu/trigger/schedule/delete`

```json
POST https://YOUR_REST_API_URL/campaigns/trigger/schedule/delete
Content-Type: application/json
{
  "api_key": (required, string) see App Group REST API Key,
  "campaign_id": (required, string) see Campaign Identifier,
  "schedule_id": (required, string) the schedule_id to delete (obtained from the response to create schedule)
}
```

Scheduled messages or triggers that are deleted very close to or during the time they were supposed to be sent will be updated with best efforts, so last second deletions could be applied to all, some, or none of your targeted users.

## Create Send IDs For Message Send Tracking

Instance  | REST Endpoint
----------|-----------------------------------------------------------
US-01 | `https://rest.iad-01.braze.com/sends/id/create`
US-02 | `https://rest.iad-02.braze.com/sends/id/create`
US-03 | `https://rest.iad-03.braze.com/sends/id/create`
US-04 | `https://rest.iad-04.braze.com/sends/id/create`
US-06 | `https://rest.iad-06.braze.com/sends/id/create`
EU-01 | `https://rest.fra-01.braze.eu/sends/id/create`

```json
POST https://YOUR_REST_API_URL/sends/id/create
Content-Type: application/json
{
  "api_key": (required, string) see App Group REST API Key,
  "campaign_id": (required, string) see Campaign Identifier,
  "send_id": (required, string) see Send Identifier
}
```
Braze’s Send Identifier adds the ability to send messages and track message performance entirely programmatically, without campaign creation for each send. Using the Send Identifier to track and send messages is useful if you are planning to programmatically generate and send content.

The daily maximum number of custom send identifiers that can be created via this endpoint for a given app group is 100. Each send id - campaign id combination that you create will count towards your daily limit. The response headers for any valid request include the current rate limit status, see [API Limits][47]

Example response:

```json
{
  "message": "success",
  "send_id" : "example_send_id"
}
```

## Get Upcoming Scheduled Campaigns and Canvases

You can view a JSON list of upcoming and scheduled Campaigns and Canvases using the following information and parameters. The endpoint will return information about scheduled Campaigns and entry Canvases between now and the designated `end_time` specified in the request. Daily, recurring messages will only appear once with their next occurrence. Results returned in this endpoint are only for Campaigns and Canvases created and scheduled in Braze.

Instance  | REST Endpoint
----------|-----------------------------------------------------------
US-01 | `https://rest.iad-01.braze.com/messages/scheduled_broadcasts`
US-02 | `https://rest.iad-02.braze.com/messages/scheduled_broadcasts`
US-03 | `https://rest.iad-03.braze.com/messages/scheduled_broadcasts`
US-04 | `https://rest.iad-04.braze.com/messages/scheduled_broadcasts`
US-06 | `https://rest.iad-06.braze.com/messages/scheduled_broadcasts`
EU-01 | `https://rest.fra-01.braze.eu/messages/scheduled_broadcasts`

| Parameter | Required | Data Type | Description |
| ---------------------| --------------- |
| `api_key` | Yes | String | see App Group REST API Key in Parameter Definitions |
| `end_time` | Yes | String in ISO 8601 format | End date of the range to retrieve upcoming scheduled Campaigns and Canvases. This is treated as midnight in UTC time by the API. |

Example Request:

```json
https://rest.iad-01.braze.com/messages/scheduled_broadcasts?api_key=X&end_time=2017-09-01T00:00:00-04:00
```

Example Response:

```json
{
    "scheduled_broadcasts": [
      # Example Canvas
      {
        "name" => String,
        "id" => String,
        "type" => "Canvas",
        "tags" => [String tag names],
        "next_send_time" => "YYYY-MM-DD HH:mm:ss" (may also include time zone if not local/intelligent delivery)
        "schedule_type" => one of "local_time_zones", "intelligent_delivery", or the name of your company's time zone
      },
      # Example Campaign
      {
        "name" => String,
        "id" => String,
        "type" => "Campaign",
        "tags" => [String tag names],
        "next_send_time" => "YYYY-MM-DD HH:mm:ss" (may also include time zone if not local/intelligent delivery)
        "schedule_type" => one of "local_time_zones", "intelligent_delivery", or the name of your company's time zone
      },
    ]
}
```

{% endraw %}

##  Messaging Objects & Filters

### User Alias Object

{% raw %}

The User Alias Object consists of two parts: an `alias_name` for the identifier itself, and an `alias_label` indicating the type of alias. Users can have multiple aliases with _different_ labels, but only one `alias_name` per `alias_label`.

```json
{
  "alias_name" : (required, string),
  "alias_label" : (required, string)
}
```

### Recipient Object
```json
{
  // Either "external_user_id" or "user_alias" is required. Requests must specify only one.
  "user_alias": (optional, User Alias Object) User Alias of user to receive message,
  "external_user_id": (optional, string) see External User Id,
  "trigger_properties": (optional, object) personalization key-value pairs for this user when sending a Campaign or message; see Trigger Properties,
  "canvas_entry_properties": (optional, object) personalization key-value pairs for this user when triggering a Canvas; see Canvas Entry Properties
}
```

### Connected Audience Object

A Connected Audience is a selector that identifies the audience to send the message to. It is composed of either a single Connected Audience Filter, or several Connected Audience Filters in a logical expression using either "AND" or "OR" operators.

Multiple filter example:

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

### Connected Audience Filter

These filters are used to create an Connected Audience Object.

#### Custom Attribute Filter

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

The custom attribute's type determines the comparisons that are valid for a given filter.

| Custom Attribute Type | Allowed Comparisons |
| ---------------------| --------------- |
| String | `equals`, `not_equal`, `matches_regex`, `does_not_match_regex`, `exists`, `does_not_exist` |
| Array | `includes_value`, `does_not_include_value`, `exists`, `does_not_exist` |
| Numeric | `equals`, `not_equal`, `greater_than`, `greater_than_or_equal_to`, `less_than`, `less_than_or_equal_to`, `exists`, `does_not_exist` |
| Boolean | `equals`, `does_not_equal`, `exists`, `does_not_exist` |
| Time | `less_than_x_days_ago`, `greater_than_x_days_ago`, `less_than_x_days_in_the_future`, `greater_than_x_days_in_the_future`, `after`, `before`, `exists`, `does_not_exist`

>  `value` is not required when using the `exists` or `does_not_exist` comparisons. `value` must be an ISO 8601 DateTime string when using the `before` and `after` comparisons.

Examples:

```json
{
  "custom_attribute":
    {
      "custom_attribute_name": "eye_color",
      "comparison": "equals",
      "value": "blue"
    }
}

{
  "custom_attribute":
  {
    "custom_attribute_name": "favorite_foods",
    "comparison": "includes_value",
    "value": "pizza"
  }
}

{
  "custom_attribute":
  {
    "custom_attribute_name": "last_purchase_time",
    "comparison": "less_than_x_days_ago",
    "value": 2
  }
}
```

#### Push Subscription Filter

This filter allows you to segment based on a user's push subscription status. These filters contain two fields:

```json
{
  "push_subscription_status":
  {
    "comparison": (String) one of the two allowed comparisons listed below,
    "value": (String) one of the three allowed values listed below
  }
}
```

| Allowed Comparisons | Allowed Values |
| ---------------------| --------------- |
| `is`, `is_not` | `opted_in`, `subscribed`, `unsubscribed` |

#### Email Subscription Filter

This filter allows you to segment based on a user's email subscription status. These filters contain two fields:

```json
{
  "email_subscription_status":
  {
    "comparison": (String) one of the two allowed comparisons listed below,
    "value": (String) one of the three allowed values listed below
  }
}
```

| Allowed Comparisons | Allowed Values |
| ---------------------| --------------- |
| `is`, `is_not` | `opted_in`, `subscribed`, `unsubscribed` |

#### Last Used App Filter

This filter allows you to segment based on when was the last time user used the App. These filters contain two fields:

```json
{
  "last_used_app":
  {
    "comparison": (String) one of the allowed comparisons listed below,
    "value": (String) the value to be compared using the provided comparison
  }
}
```

| Allowed Comparisons | Allowed Values |
| ---------------------| --------------- |
| `after`, `before` | DateTime (ISO 8601 string) |

### Apple Push Object

```json
{
   "badge": (optional, int) the badge count after this message,
   "alert": (required unless content-available is true, string or Apple Push Alert Object) the notification message,
   // Specifying "default" in the sound field will play the standard notification sound
   "sound": (optional, string) the location of a custom notification sound within the app,
   "extra": (optional, object) additional keys and values to be sent,
   "content-available": (optional, boolean) if set, Braze will add the "content-available" flag to the push payload,
   "expiry": (optional, ISO 8601 date string) if set, push messages will expire at the specified datetime,
   "custom_uri": (optional, string) a web URL, or Deep Link URI,
   "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under (must be an iOS Push Message),
   "notification_group_thread_id": (optional, string) the notification group thread ID the notification will be sent with,
   "asset_url": (optional, string) content URL for rich notifications for devices using iOS 10 or higher,
   "asset_file_type": (required if asset_url is present, string) file type of the asset - one of "aif", "gif", "jpg", "m4a", "mp3", "mp4", "png", or "wav",
   "collapse_id": (optional, string) To update a notification on the user's device once you've issued it, send another notification with the same collapse ID you used previously
   "mutable_content": (optional, boolean) if true, Braze will add the mutable-content flag to the payload and set it to 1. The mutable-content flag is automatically set to 1 when sending a rich notification, regardless of the value of this parameter.
   "send_to_most_recent_device_only": (optional, boolean) defaults to false, if set to true, Braze will only send this push to a user's most recently used iOS device, rather than all eligible iOS devices,
   "category": (optional, string) the iOS notification category identifier for displaying push action buttons,
   "buttons" : (optional, array of Apple Push Action Button Objects) push action buttons to display
}
```

>  You must include an Apple Push Object in `messages` if you want users you have targeted to receive a push on their iOS Devices. The total number of bytes in your `alert` string, `extra` object, and other optional parameters should not exceed 1912. The Messaging API will return an error if you exceed the message size allowed by Apple. Messages that include the keys `ab` or `aps` in the `extra` object will be rejected.

##### Apple Push Alert Object

>  In most cases, `alert` can just be specified in an `apple_push` object as a string. You should specify `alert` as an object only in cases where you need specific localization or Apple Watch customization.

```json
{
   "body": (required unless content-available is true in the Apple Push Object, string) the text of the alert message,
   "title": (optional, string) a short string describing the purpose of the notification, displayed as part of the Apple Watch notification interface,
   "title_loc_key": (optional, string) the key to a title string in the `Localizable.strings` file for the current localization,
   "title_loc_args": (optional, array of strings) variable string values to appear in place of the format specifiers in title_loc_key,
   "action_loc_key": (optional, string) if a string is specified, the system displays an alert that includes the Close and View buttons, the string is used as a key to get a localized string in the current localization to use for the right button’s title instead of "View",
   "loc_key": (optional, string) a key to an alert-message string in a Localizable.strings file for the current localization,
   "loc_args": (optional, array of strings) variable string values to appear in place of the format specifiers in loc_key
}
```

#### Apple Push Action Button Object

You _must_ include the `category` field in the Apple Push Object to use iOS push action buttons. Including the `category` field will display any associated push action buttons; only include the `buttons` field if you want to additionally define the buttons' individual click actions. The Braze SDK provides a set of default push action buttons for you to use (see the table below). You can also use your own buttons if they have been registered in your app.

##### Apple Push Action Button Object for Braze Default Buttons

| Category Identifier   | Button Text | Button Action Identifier | Allowed Actions         |
|-----------------------|-------------|--------------------------|-------------------------|
| `ab_cat_accept_decline` | Accept      | `ab_pb_accept`             | OPEN_APP, URI, or DEEP_LINK |
| `ab_cat_accept_decline` | Decline     | `ab_pb_decline`            | CLOSE                   |
| `ab_cat_yes_no`         | Yes         | `ab_pb_yes`                | OPEN_APP, URI, or DEEP_LINK |
| `ab_cat_yes_no`         | No          | `ab_pb_no`                 | CLOSE                   |
| `ab_cat_confirm_cancel` | Confirm     | `ab_pb_confirm`            | OPEN_APP, URI, or DEEP_LINK |
| `ab_cat_confirm_cancel` | Cancel      | `ab_pb_cancel`             | CLOSE                   |
| `ab_cat_more`           | More        | `ab_pb_more`               | OPEN_APP, URI, or DEEP_LINK |

```json
{
  "action_id": (required, string) the button's action identifier,
  "action": (optional, string) one of "OPEN_APP", "URI", "DEEP_LINK", or "CLOSE". Defaults to either "OPEN_APP" or "CLOSE" depending on the button,
  "uri": (optional, string) a web URL or Deep Link URI,
  "use_webview": (optional, boolean) whether to open the web URL inside the app if the action is "URI", defaults to true
}
```

##### Apple Push Action Button Object for Categories Defined by Your App

```json
{
  "action_id": (required, string) the button's action identifier,
  "action": (required, string) one of "URI" or "DEEP_LINK",
  "uri": (required, string) a web URL or Deep Link URI,
  "use_webview": (optional, boolean) whether to open the web URL inside the app if the action is "URI", defaults to true
}
```

###  Android Push Object

```json
{
   "alert": (required, string) the notification message,
   "title": (required, string) the title that appears in the notification drawer,
   "extra": (optional, object) additional keys and values to be sent in the push,
   "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under (must be an Android Push Message),
   "notification_channel_id": (optional, string) the channel ID the notification will be sent with,
   "priority": (optional, integer) the notification priority value,
   "send_to_sync": (optional, if set to true we will throw an error if "alert" or "title" is set),
   "collapse_key": (optional, string) the collapse key for this message,
   // Specifying "default" in the sound field will play the standard notification sound
   "sound": (optional, string) the location of a custom notification sound within the app,
   "custom_uri": (optional, string) a web URL, or Deep Link URI,
   "summary_text": (optional, string),
   "time_to_live": (optional, integer (seconds)),
   "notification_id": (optional, integer),
   "push_icon_image_url": (optional, string) an image URL for the large icon,
   "accent_color": (optional, integer) accent color to be applied by the standard Style templates when presenting this notification, an RGB integer value,
   "send_to_most_recent_device_only": (optional, boolean) defaults to false, if set to true, Braze will only send this push to a user's most recently used Android device, rather than all eligible Android devices,
   "buttons" : (optional, array of Android Push Action Button Objects) push action buttons to display
}
```

>  You can send "Big Picture" notifications by specifying the key `appboy_image_url` in the `extra` object. The value for `appboy_image_url` should be a URL that links to where your image is hosted. Images need to be cropped to a 2:1 aspect ratio and should be at least 600x300. Images used for notifications will only display on devices running Jelly Bean (Android 4.1) or higher.

>  `priority` will accept values from -2 to 2, where -2 represents "MIN" priority and 2 represents "MAX". 0 is the "DEFAULT" value. Any values sent that outside of that integer range will default to 0. For more information on which priority level to use, please see our section on [Android Notification Priority][29].

>  The value for the large icon `push_icon_image_url` should be a URL that links to where your image is hosted. Images need to be cropped to a 1:1 aspect ratio and should be at least 40x40. Images used for custom notification icons will only display on devices running Honeycomb MR1 (Android 3.1) or higher.

>  If `notification_channel` is not specified, Braze will attempt to send the notification payload with the [dashboard fallback][45] channel ID. For more information on `notification_channel` please see our [developer documentation][43] and our [academy article][44].

For more information on collapsing notifications using the `collapse_key` please see the [Android Developer Docs][35]

For more information on `send_to_sync` messages please see our section on ["Silent Android Notifications"][28]

You must include an Android Push Object in `messages` if you want users you have targeted to receive a push on their Android devices. The total number of bytes in your `alert` string and `extra` object should not exceed 4000. The Messaging API will return an error if you exceed the message size allowed by Google.

#### Android Push Action Button Object

```json
{
  "text": (required, string) the button's text,
  "action": (optional, string) one of "OPEN_APP", "URI", "DEEP_LINK", or "CLOSE", defaults to "OPEN_APP",
  "uri": (optional, string) a web URL or Deep Link URI,
  "use_webview": (optional, boolean) whether to open the web URL inside the app if the action is "URI", defaults to true
}
```

### Content Card Object

```json
{
  "type": (required, string) one of "CLASSIC", "CAPTIONED_IMAGE", or "BANNER",
  "title": (required, string) the card's title,
  "description": (required, string) the card's description,
  "pinned": (optional, boolean) whether the card is pinned. Defaults to false,
  "image_url": (optional, string) the card's image URL. Required for "CAPTIONED_IMAGE" and "BANNER",
  "time_to_live": (optional, integer) the number of seconds before the card expires. You must include either "time_to_live" or "expire_at",
  "expire_at": (optional, string) ISO 8601 date when the card expires. You must include either "time_to_live" or "expire_at",
  "expire_in_local_time": (optional, boolean) if using "expire_at", determines whether the card should expire in users' local time. Defaults to false,
  "ios_uri": (optional, string) a web URL, or Deep Link URI,
  "android_uri": (optional, string) a web URL, or Deep Link URI,
  "web_uri": (optional, string) a web URL, or Deep Link URI,
  "ios_use_webview": (optional, boolean) whether to open the web URL inside the app, defaults to true,
  "android_use_webview": (optional, boolean) whether to open the web URL inside the app, defaults to true,
  "uri_text": (optional, string) the card's link text,
  "extra": (optional, object) additional keys and values sent with the card,
}
```

### Kindle/FireOS Push Object

```json
{
   "alert": (required, string) the notification message,
   "title": (required, string) the title that appears in the notification drawer,
   "extra": (optional, object) additional keys and values to be sent in the push,
   "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under (must be an Kindle/FireOS Push Message),
   "priority": (optional, integer) the notification priority value,
   "collapse_key": (optional, string) the collapse key for this message,
   // Specifying "default" in the sound field will play the standard notification sound
   "sound": (optional, string) the location of a custom notification sound within the app,
   "custom_uri": (optional, string) a web URL, or Deep Link URI
}
```

>  `priority` will accept values from -2 to 2, where -2 represents "MIN" priority and 2 represents "MAX". 0 is the "DEFAULT" value. Any values sent that outside of that integer range will default to 0.

### Web Push Object

```json
{
   "alert": (required, string) the notification message,
   "title": (required, string) the title that appears in the notification drawer,
   "extra": (optional, object) additional keys and values to be sent in the push,
   "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under (must be an Kindle/FireOS Push Message),
   "custom_uri": (optional, string) a web URL,
   "image_url": (optional, string) url for image to show,
   "large_image_url": (optional, string) url for large image, supported on Chrome Windows/Android,
   "require_interaction": (optional, boolean) whether to require the user to dismiss the notification, supported on Mac Chrome,
   "time_to_live": (optional, integer (seconds)),
   "send_to_most_recent_device_only" : (optional, boolean) defaults to false, if set to true, Braze will only send this push to a user's most recently used browser, rather than all eligibles browsers,
   "buttons" : (optional, array of Web Push Action Button Objects) push action buttons to display
}
```

>  The value for `image_url` should be a URL that links to where your image is hosted. Images need to be cropped to a 1:1 aspect ratio.

#### Web Push Action Button Object

```json
{
  "text": (required, string) the button's text,
  "action": (optional, string) one of "OPEN_APP", "URI", or "CLOSE", defaults to "OPEN_APP",
  "uri": (optional, string) a web URL
}
```

### Windows Phone 8 Push Object

```json
{
   "push_type": (optional, string) must be "toast",
   "toast_title": (optional, string) the notification title,
   "toast_content": (required, string) the notification message,
   "toast_navigation_uri": (optional, string) page uri to send user to,
   "toast_hash": (optional, object) additional keys and values to send,
   "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under (must be a Windows Phone 8 Push Message)
}
```

###  Windows Universal Push Object

See the Windows Universal [toast template catalog][32] for details on the options for `push_type` below.

```json
{
   "push_type": (required, string) one of: "toast_text_01", "toast_text_02", "toast_text_03", "toast_text_04", "toast_image_and_text_01", "toast_image_and_text_02", "toast_image_and_text_03", or "toast_image_and_text_04",
   "toast_text1": (required, string) the first line of text in the template,
   "toast_text2": (optional, string) the second line of text (for templates with > 1 line of text),
   "toast_text3": (optional, string) the third line of text (for the *_04 templates),
   "toast_text_img_name": (optional, string) the path for the image for the templates that include an image,
   "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under (must be a Windows Universal Push Message),
   "extra_launch_string": (optional, string) used to add deep linking functionality by passing extra values to the launch string
}
```

>  For more information on using the `extra_launch_string` parameter for deep linking, see [Deep Linking with Windows Universal.] [37] For information regarding what a deep link is, please see our [FAQ Section][38].

### Email Object Specification

```json
{
  "app_id": (required, string) see App Identifier above,
  "subject": (optional, string),
  "from": (required, valid email address in the format "Display Name <email@address.com>"),
  "reply_to": (optional, valid email address in the format "email@address.com" - defaults to your app group's default reply to if not set),
  "body": (required unless email_template_id is given, valid HTML),
  "plaintext_body": (optional, valid plaintext, defaults to autogenerating plaintext from "body" when this is not set),
  "preheader"*: (optional, string) Recommended length 50-100 characters.
  "email_template_id": (optional, string) If provided, we will use the subject/body/should_inline_css values from the given email template UNLESS they are specified here, in which case we will override the provided template,
  "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under,
  "extras": (optional, valid Key-Value Hash), extra hash - for SendGrid customers, this will be passed to SendGrid as Unique Arguments,
  "headers": (optional, valid Key-Value Hash), hash of custom extensions headers. Currently, only supported for SendGrid customers,
  "should_inline_css": (optional, boolean), whether to inline css on the body. If not provided, falls back to the default css inlining value for the App Group,
  "attachments": (optional, array), array of json objects like [{"file_name","url"}] that define the files you need attached. Your file name's extension will be detected automatically from the URL, which should return the appropriate `Content-Type` as a response header.
}
```

**\*** For more information and best practices, see [here][46].

>  An `email_template_id` can be retrieved from the bottom of any Email Template created within the dashboard. Below is an example of what this ID looks like:

![Email Template ID][31]

### Webhook Object Specification

```json
{
  "url": (required, string),
  "request_method": (required, string) one of "POST", "PUT", "DELETE", or "GET",
  "request_headers": (optional, Hash) key-value pairs to use as request headers,
  "body": (optional, string) if you want to include a JSON object, make sure to escape quotes and backslashes,
  "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under
}
```

{% endraw %}

[18]: https://dashboard-01.braze.com/app_settings/api_settings/
[19]: {{ site.baseurl }}/developer_guide/rest_api/user_data/#user-attributes-object-specification
[23]: https://rubygems.org/gems/multi_json "multiJSON"
[24]: https://rubygems.org/gems/rest-client "Rest Client"
[25]: #email-object
[26]: {{ site.baseurl }}/developer_guide/rest_api/api_campaigns/#api-campaigns
[27]: #sample-requests
[28]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/push_notifications/silent_push_notifications/#silent-push-notifications
[29]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/advanced_use_cases/deep_linking_to_in-app_resources/
[31]: {% image_buster /assets/img_archive/email_template_id.png %}
[32]: https://msdn.microsoft.com/en-us/library/windows/apps/hh761494.aspx
[33]: {{ site.baseurl }}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/scheduling_your_campaign/#option-3-intelligent-delivery
[34]: #campaign-id
[35]: https://firebase.google.com/docs/cloud-messaging/concept-options#collapsible_and_non-collapsible_messages "collapse key documentation"
[36]: {{ site.baseurl }}/help/best_practices/in-app_messages/
[37]: {{ site.baseurl }}/developer_guide/platform_integration_guides/windows_universal/push_notifications/integration/#step-4-deep-linking-from-push-into-your-app
[38]: {{ site.baseurl }}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#what-is-deep-linking
[39]: {{ site.baseurl }}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/scheduling_your_campaign/#api-triggered-campaigns-server-triggered-campaigns
[40]: {{ site.baseurl }}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/scheduling_your_campaign/#re-eligibility-with-api-triggered-campaigns
[41]: https://dashboard-01.braze.com/app_settings/developer_console/activitylog/
[42]: #broadcast
[44]: {{ site.baseurl }}/user_guide/message_building_by_channel/push/notification_channels/#notification-channels
[43]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/push_notifications/integration/#step-4-define-notification-channels
[45]: {{ site.baseurl }}/user_guide/message_building_by_channel/push/notification_channels/#notification-channels
[46]: {{ site.baseurl }}/help/best_practices/email/#body-styling
[47]: {{ site.baseurl }}/developer_guide/rest_api/basics/#api-limits
