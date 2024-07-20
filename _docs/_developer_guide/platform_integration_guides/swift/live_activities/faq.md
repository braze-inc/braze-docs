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

Apple requires that the user initiates the Live Activity through some action in your app, for example, by placing an order. This Live Activity token expires after eight hours. 

### Do Live Activities require push primers?

[Push primers]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/) are a best practice to prompt your users to opt in to push notifications from your app. However, there is no system prompt to opt into Live Activities. Users are, by default, opted into Live Activities when they upgrade to iOS 16.1+.

## Technical topics and troubleshooting

### How do I know if Live Activities has errors?

Any Live Activity errors will be logged in the Braze dashboard in the [Message Activity Log]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/), where you can filter by "LiveActivity Errors".

### I am receiving an Access Denied response when I try to use the `live_activity/update` endpoint. Why?

The API keys you use need to be given the correct permissions to access the different Braze API endpoints. If you are using an API key that you previously created, it's possible that you neglected to update its permissions. Read our [API key security overview]({{site.baseurl}}/api/basics/#rest-api-key-security) for a refresher.

### Does the `messages/send` endpoint share rate limits with the `messages/live_activity/update` endpoint? 

By default, the rate limit for the `messages/live_activity/update` endpoint is 250,000 requests per hour, per workspace, and across multiple endpoints. See the [API rate limits]({{site.baseurl}}/api/api_limits/) for more information.

### Why aren't my push-to-start tokens being generated?

Starting with iOS 17.2 and later, Apple has limited their `pushToStartToken` and `pushToStartTokenUpdates` APIs. In practice, push-to-start tokens are only generated during the first app launch in `application(_:didFinishLaunchingWithOptions:)` after the first install. If this step needs to be repeated, tokens can only be generated again after rebooting and re-installing the app, or by manually creating a new instance of that Live Activity.

### What other things should I watch out for during troubleshooting?

- Check that you are using a `.p8` key for authentication.
- Check that your push provisioning profile matches the environment you’re testing. Universal certificates may be configured in the Braze dashboard to send to either the development or production Apple Push Notification service (APNs) environment. Using a development certificate for a production app or a production certificate for a development app will not work.


[1]: {{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/live_activities/live_activities/#prerequisites
[3]: {{site.baseurl}}/api/basics/#rest-api-key-security
[4]: {% image_buster /assets/img/push-vs-live-activities.png %}
[5]: {{site.baseurl}}/api/api_limits/