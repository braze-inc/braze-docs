---
nav_title: Live Activities Frequently Asked Questions
article_title: Live Activities Frequently Asked Questions
page_order: 2
description: "This page provides answers to frequently asked questions about live activities."
tool: Live Activities
platform:
  - iOS
---

# Frequently asked questions

## Functionality and support

### How can I join the Live Activities early access program? 

Live Activities are currently in early access. Contact your Braze account manager if you're interested in participating. There is no additional pricing or paperwork required to join this early access program.

### What platforms support Live Activities?

Live Activities are currently a feature specific to iOS. The Live Activities article covers the [prerequisites][2] for managing Live Activities through the Braze Swift SDK.

### Does Braze support Live Activities as a campaign or Canvas step?

No, this is not currently supported.

### Does Braze keep analytics on Live Activity bounces?

Bounce metrics don't make sense in a Live Activity context because users explicitly initiate the activity.

<!-- Question: But are there any analytics on "Customer sends out a notification for a live activity and X users in the segment joined" or similar? -->

## Push notifications and Live Activities

### If Live Activities leverage push message functionality, do push notifications need to be enabled to receive Live Activities?

Whereas Live Activities function similarly to push notifications, they are controlled by different user settings. A user can opt into Live Activities but out of push notifications, and vice versa. 

Apple requires that the user needs to initiate the Live Activity for every new activity. A Live Activity token expires after eight hours. 

<!-- Question: What does it mean that "the user needs to initiate the Live Activity for every new activity"? I'm not sure I understand this workflow. -->

### Do Live Activities require push primers?

[Push primers][1] are a best practice to prompt your users to opt in to push notifications from your app. However, there is no system prompt to opt into Live Activities. Users are, by default, opted into Live Activities when they upgrade to iOS 16.1+.

### What happens if a push notification is sent while a Live Activity is active? 

Live Activities and push notifications occupy different screen real estate and won't conflict on a user's screen.

![A phone screen with a Bulls vs Bears sports game live activity towards the middle of the screen and push notification lorem ipsum text at the bottom of the screen.][4]{: style="max-width:40%;float:right;margin-left:15px;"}

## Technical topics and troubleshooting

### I am receiving an Access Denied response when I try to use the `live_activity/update` endpoint. Why?

The API keys you use need to be given the correct permissions to access the different Braze API endpoints. If you are using an API key that you previously created, it's possible that you neglected to update its permissions. Read our [API key security overview][3] for a refresher.

### Does the `messages/send` endpoint share rate limits with the `messages/live_activity/update` endpoint? 

The `messages/live_activity/update` endpoint has a separate rate limit from any other Braze endpoint. By default, the rate limit for the `messages/live_activity/update` endpoint is 250,000 requests per hour per app group. See the [rate limit article][5] for more information.

<!-- Question: Am I correct in understanding that the basic rate limits of the Messages endpoint (https://www.braze.com/docs/api/api_limits/#batching-messaging-endpoint-requests) is true for the live activity/update endpoint as well? -->

<!-- Question: Is the "250k per hour per app group" accurate? I hadn't understood the default was a per-app group limit and want to double check this wording.-->


[1]: {{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/live_activities/#prerequisites
[3]: {{site.baseurl}}/api/basics/#rest-api-key-security
[4]: {% image_buster /assets/img/push-vs-live-activities.png %}
[5]: {{site.baseurl}}/api/api_limits/