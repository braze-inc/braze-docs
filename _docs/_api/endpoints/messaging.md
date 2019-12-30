---
nav_title: Messaging
page_order: 2
search_rank: 5
local_redirect: #parameter-definitions #app-group-rest-api-key #app-identifier #external-user-id #segment-identifier #campaign-identifier #canvas-identifier #trigger-properties #canvas-identifier #server-responses #fatal-errors #responses-for-tracked-send-ids #messaging-queued #canvas-entry-properties
  parameter-definitions: '/docs/api/parameters/'
  app-group-rest-api-key: '/docs/api/parameters/'
  app-identifier: '/docs/api/parameters/'
  external-user-id: '/docs/api/parameters/'
  segment-identifier: '/docs/api/parameters/'
  campaign-identifier: '/docs/api/parameters/'
  canvas-identifier: '/docs/api/parameters/'
  send-identifier: '/docs/api/parameters/'
  trigger-properties: '/docs/api/parameters/'
  canvas-entry-properties: '/docs/api/parameters/'
  server-responses: '/docs/api/errors/'
  messaging-queued: '/docs/api/errors/'
  responses-for-tracked-send-ids: '/docs/api/errors/'
  fatal-errors: '/docs/api/errors/'

---
# Messaging

## Overview

The Braze messaging API provides you with two distinct options for sending messages to your users. You can provide the message contents and configuration in the API request with the `/messages/send` and `/messages/schedule` endpoints. Alternatively, you can manage the details of your message with an API-Triggered Delivery campaign in the dashboard and just control when and to whom it is sent with the `campaigns/trigger/send` and `campaigns/trigger/schedule` endpoints. The following sections will detail the request specification for both methods.

Similarly to other campaigns, you can limit the number of times a particular user can receive a Messaging API campaign by configuring [re-eligibility settings][40] in the Braze Dashboard. Braze will not deliver API messages to users that haven't become re-eligible for the campaign regardless of how many API requests are sent.


{% raw %}



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
    "email": (optional, Email object),
    "webhook": (optional, Webhook object),
    "content_card": (optional, Content Card Object),
    "sms": (optional, SMS Object)
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

This endpoint uses the [Schedule Object][55].

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

Any schedule will completely overwrite the one that you provided in the create schedule request or in previous update schedule requests. For example, if you originally provide `"schedule" : {"time" : "2015-02-20T13:14:47", "in_local_time" : true}` and then in your update you provide `"schedule" : {"time" : "2015-02-20T14:14:47"}`, your message will now be sent at the provided time in UTC, not in the user's local time. Scheduled triggers that are updated very close to or during the time they were supposed to be sent will be updated with best efforts, so last-second changes could be applied to all, some, or none of your targeted users.

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

Scheduled messages or triggers that are deleted very close to or during the time they were supposed to be sent will be updated with best efforts, so last-second deletions could be applied to all, some, or none of your targeted users.

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
[55]:
