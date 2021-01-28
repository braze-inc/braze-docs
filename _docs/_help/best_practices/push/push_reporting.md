---
nav_title: Reporting
page_order: 7
---

# Push Reporting

The Braze SDK provides you with a detailed report of each of your push campaigns. Navigate to the 'Campaigns' tab on your dashboard and click on the 'Details' tab of your desired campaign as shown below:

![Campaign Details][29]

On this page, you will be able to comprehensively view and analyze the success of your campaign in an organized format. Please find definitions of the different push-specific metrics below

| Statistic | Description |
| --------- | --- |
| Bounces | The push notifications sent to these users were undeliverable. These users have been automatically unsubscribed from all future push notifications. See [Bounced Push Notifications][38]. |
| Direct Opens | Instances in which a user opened your app by interacting directly with a push notification. |
| Opens | Instances including both Direct Opens (defined above) and Influenced Opens in which the Braze SDK has determined, using a proprietary algorithm, that a push notification has caused a user to open the app. |
{: .reset-td-br-1 .reset-td-br-2}

> Delivery of notifications is a “best effort” by APNs. It is not intended to deliver data to your app, only to notify the user that there is new data available. The important distinction is that we will display how many messages we successfully delivered to APNs, not necessarily how many APNs successfully delivered to devices.

## Bounced Push Notifications

### Apple Push Notification Service

Bounces occur in the APNs when a push notification attempts delivery to a device that does not have the intended app installed. APNs also has the right to change tokens for devices arbitrarily. If you attempt to send to a user’s device in which their push token has changed in between when we previously registered their token (i.e. at the beginning of each session when we register a user for a push token) and the time of send, this would cause a bounce.

If a user disables push within their device settings on subsequent app open the SDK will detect that push has been disabled and notify Braze. At this point we will update the push enabled state to be disabled. When a disabled user receives a push campaign before having a new session, the campaign would successfully send and appear as delivered. The push will not bounce for this user. Following a subsequent session, when you attempt to send a push to the user Braze is already aware of whether we have a token as such no notification is sent.

Push notifications that expire before delivery are not considered as failed and will not be recorded as a bounce.

### Firebase Cloud Messaging

FCM bounces could occur in three cases:

- **Uninstalled Applications**

When a message attempts delivery to a device and the intended app is uninstalled on that device, the message will be discarded and the device's registration ID will be invalidated. Any future attempts at messaging the device will return a NotRegistered error.

- **Backed Up Applications**

When an application is backed up, its registration ID could become invalid before the application is restored. In this case, FCM will no longer store the application's registration ID and the application will no longer receive messages. As such, registration IDs should _not_ be saved when an application is backed up.

- **Updated Applications**

When an application is updated, the previous version's registration ID may no longer work. As such, an updated application should replace its existing registration ID.


[29]: {% image_buster /assets/img_archive/braze_campaignresults.png %}
[38]: #bounced-push-notifications
[46]:{% image_buster /assets/img_archive/Push_Window8_Toast.png %}
[47]:{% image_buster /assets/img_archive/Push_Windows_Universal_Toast.png %}
