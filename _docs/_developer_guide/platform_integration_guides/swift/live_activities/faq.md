---
nav_title: FAQ
article_title: Live Activities FAQ
page_order: 20
description: "This page provides answers to frequently asked questions about live activities for the Swift SDK."
tool: Live Activities
platform:
  - iOS
---

# Frequently asked questions

> This article provides answers to some frequently asked questions about Live Activities.

## Functionality and support

### What platforms support Live Activities?

Live Activities are currently a feature specific to iOS. The Live Activities article covers the [prerequisites]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/live_activities/live_activities/#prerequisites) for managing Live Activities through the Braze Swift SDK.

### Do React Native apps support Live Activities?

Yes, React Native SDK 3.0.0+ supports Live Activities via the Braze Swift SDK. That is, you need to write React Native iOS code directly on top of the Braze Swift SDK. 

There isn't a React Native-specific JavaScript convenience API for Live Activities because the Live Activities features provided by Apple use languages untranslatable in JavaScript (for example, Swift concurrency, generics, SwiftUI).

### Does Braze support Live Activities as a campaign or Canvas step?

No, this is not currently supported.

## Push notifications and Live Activities

### What happens if a push notification is sent while a Live Activity is active? 

![A phone screen with a Bulls versus Bears sports game live activity toward the middle of the screen and push notification lorem ipsum text at the bottom of the screen.]({% image_buster /assets/img/push-vs-live-activities.png %}){: style="max-width:30%;float:right;margin-left:15px;"}

Live Activities and push notifications occupy different screen real estate and won't conflict on a user's screen.

### If Live Activities leverage push message functionality, do push notifications need to be enabled to receive Live Activities?

While Live Activities rely on push notifications for updates, they are controlled by different user settings. A user can opt into Live Activities but out of push notifications, and the other way around.

Live Activity update tokens expire after eight hours.

### Do Live Activities require push primers?

[Push primers]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/) are a best practice to prompt your users to opt in to push notifications from your app. However, there is no system prompt to opt into Live Activities. By default, users are opted into Live Activities for an individual app when the user installs that app on iOS 16.1 or later. This permission can be disabled or re-enabled in the device settings on a per-app basis.

## Technical topics and troubleshooting

### How do I know if Live Activities has errors?

Any Live Activity errors will be logged in the Braze dashboard in the [Message Activity Log]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/), where you can filter by "LiveActivity Errors".

### After sending a push-to-start notification, why haven't I received my Live Activity?

First, verify that your payload includes all the required fields described in the [`messages/live_activity/start`]({{site.baseurl}}/api/endpoints/messaging/live_activity/start) endpoint. The `activity_attributes` and `content_state` fields should match the properties defined in your project's code. If you're certain that the payload is correct, its possible you may be rate-limited by APNs. This limit is imposed by Apple and not by Braze.

To verify that your push-to-start notification successfully arrived at the device but was not displayed due to rate limits, you can debug your project using the Console app on your Mac. Attach the recording process for your desired device, then filter the logs by `process:liveactivitiesd` in the search bar.

### I am receiving an Access Denied response when I try to use the `live_activity/update` endpoint. Why?

The API keys you use need to be given the correct permissions to access the different Braze API endpoints. If you are using an API key that you previously created, it's possible that you neglected to update its permissions. Read our [API key security overview]({{site.baseurl}}/api/basics/#rest-api-key-security) for a refresher.

### Does the `messages/send` endpoint share rate limits with the `messages/live_activity/update` endpoint? 

By default, the rate limit for the `messages/live_activity/update` endpoint is 250,000 requests per hour, per workspace, and across multiple endpoints. See the [API rate limits]({{site.baseurl}}/api/api_limits/) for more information.

### Why aren't my push-to-start tokens being generated?

Apple has limited their `pushToStartToken` and `pushToStartTokenUpdates` APIs, which were introduced in iOS 17.2. In practice, push-to-start tokens are only generated during the first app launch in `application(_:didFinishLaunchingWithOptions:)` after the first install. If this step needs to be repeated, tokens can only be generated again by manually creating a new instance of that Live Activity, or after rebooting and re-installing the app.

### How many Live Activities can I start for my app?

The limits are defined by Apple and can vary based on a number of factors. They may also be subject to change in the future. In practice, there is a limit of five concurrent activity instances that can be launched per app at a given time. Any subsequent attempts to launch a new instance beyond that limit will be ignored by the system.

### What other things should I watch out for during troubleshooting?

- Ensure that you are using a `.p8` key for authentication instead of a `.p12` or `.pem` file.
- Check that your push provisioning profile matches the environment you’re testing. Universal certificates may be configured in the Braze dashboard to send to either the development or production Apple Push Notification service (APNs) environment. Using a development certificate for a production app or a production certificate for a development app will not work.


