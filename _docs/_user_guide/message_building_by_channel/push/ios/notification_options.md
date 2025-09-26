---
nav_title: "Notification options"
article_title: iOS Notification Options
page_order: 2
page_layout: reference
description: "This reference article covers iOS notification options like critical alerts, quiet notifications, provisional push notifications, and more."

platform: iOS
channel:
  - push

---

# Notification options

> With the release of Apple's iOS 12, Braze offers support for several of its features, including [Notification Groups](#notification-groups), [Quiet Notifications/Provisional Authorization](#provisional-push-authentication--quiet-notifications), and [Critical Alerts](#critical-alerts).

## Notification groups

If you want to categorize your messages and group them in your user's notification tray, you can utilize iOS's Notification Groups feature through Braze.

Create your iOS push campaign, then to to the **Settings** tab and open the **Notification group** dropdown.

![The "Settings" tab with a "Notification group" dropdown that selected a value of "Coupons".]({% image_buster /assets/img_archive/notification_group_dropdown.png %}){: style="max-width:50%;" }

Select your Notification Groups from the dropdown. If your notification group settings malfunction or you select **None** from the dropdown, the message will automatically send as normal to all defined users in the workspace.

If you don't have any Notification Groups listed here, you can add one using the iOS Thread ID. You will need one iOS Thread ID for every Notification Group you want to add. Then, add it to your Notification Groups by clicking **Manage Notification Groups** in the dropdown and filling out the required fields in the **Manage iOS Push Notification Groups** window that appears.

![Window to manage iOS push notification groups.]({% image_buster /assets/img_archive/managenotgroups.png %}){: style="max-width:70%;" }

Create your iOS push campaign, then look to the top of the composer. There, you'll see a dropdown labeled **Notification Groups**.

### Summary arguments

In addition to grouping notifications by Thread IDs, Apple allows you to edit the summaries that appear when notifications are grouped. Braze Users can specify the summary category, summary count, and summary argument when composing a push campaign using our tool.

{% alert tip %}
Note that the way notifications with the same Thread ID are grouped in the notification tray is under the control of the OS. iOS may choose to display notifications with the same Thread ID separately or in groups depending on what it deems optimal.
{% endalert %}

Check the **Alert Options** box in the **Push Composer**.

Then, select `summary-arg` and `summary-arg-count` as keys and input those values in the corresponding column. If you do not set a value for `summary-arg`, it will default to 1.

### Summary categories

Summary Categories allow you to customize the entire summary that appears when notifications are grouped. You can create and apply multiple categories.

To use a category in your message, work with your developers to implement using the following example:

```
UNNotificationCategory *newsCategory = [UNNotificationCategory categoryWithIdentifier:@"news"
                                                      actions:@[likeAction, unlikeAction]
                                                      intentIdentifiers:@[]
                                                      hiddenPreviewsBodyPlaceholder:@""
                                                      categorySummaryFormat:@"%u more news articles from %@"
                                                       Options:0];
```

{% alert important %}
This will not require an SDK update.
{% endalert %}

{% alert tip %}
Note that `%u` and `%@` are formatting strings for the summary count and summary argument, respectively. When the summary is shown, these placeholders will be replaced with the values for `summary-count` and `summary-arg`.
{% endalert %}

Once this is set up on your app, use the summary category by checking the **Notification Buttons** box and selecting **Enter Pre-registered iOS Category**.

Then, input the summary category identifier that you set in your app.

### Provisional push authentication and quiet notifications {#provisional-push}

Apple allows brands the option to send quiet push notifications to their users' Notification Centers before they officially, explicitly opt-in, giving you a chance to demonstrate the value of your messages early. All you need to do is [set up provisional push notifications](#set-up-provisional-push-notifications) in your app, then any user who has a provisional push token will receive your messages.

Unlike a traditional iOS push token, a provisional push token acts as a "trial pass" that allows brands to reach out to new users before they've seen and clicked Apple's native push opt-in prompt. With this feature, your push notification will be delivered directly to your new user's notification tray with the option to "Keep" or "Turn Off" future notifications. Instead of experiencing an "opt-in" journey, users will experience something more akin to an "opt-out" journey.

{% alert tip %}
Provisional Authorization has the potential dramatically increase your opt-in rate, but only if users see value in your messages. Be sure to use our [user segmentation]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/), [location targeting]({{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences/), and [personalization]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/) features to ensure that the appropriate users are getting these "trial" notifications at the right time. Then, you can encourage users to fully opt-in to your push notifications, knowing that they add value to your users' experience with your app.
{% endalert %}

Whichever option the user chooses will add the appropriate token or [subscription status]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/) to their [Contact Settings]({{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/#engagement-tab) under the **Engagement** tab in their user profile.

![Contact settings with a push subscribed status.]({% image_buster /assets/img/profile-push-prov-auth.png %}){: width="50%"}

You will be able to target your users based on whether they are provisionally authorized or not using our [segmentation filters]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/).

![Segment Details panel with the sample segment filter "Provisionally Authorized on iOS Stopwatch (iOS) is true" to target users.]({% image_buster /assets/img/segment-push-prov-auth.png %})

{% alert tip %}
If users choose to "Turn Off" provisional push from you, they won't see any more provisional push messages from you. Be thoughtful about the message content and cadence sent using this functionality!
{% endalert %}

{% alert important %}
If you use additional push prompts or [in-app push primers](https://www.braze.com/resources/glossary/priming-for-push/) (an in-app message that encourages users to opt-in to push notifications), reach out to your Braze representative for additional guidance.
{% endalert %}

#### Set up provisional push notifications

Braze allows you to register for Provisional Authentication by updating your code in your token registration snippet within your Braze iOS SDK implementation using the following snippets as an example (send these to your developers or ensure they [implement provisional push authentication during the integration process]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#using-usernotification-framework-ios-10)).

{% alert warning %}
The implementation of provisional push authentication only supports iOS 12+ and will error out if the deployment target is before that. You can learn more about this [in our more detailed implementation documentation here]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#using-usernotification-framework-ios-10).
{% endalert %}

{% tabs local %}
  {% tab Swift %}
**Swift**

```
var options: UNAuthorizationOptions = [.alert, .sound, .badge]
if #available(iOS 12.0, *) {
  options = UNAuthorizationOptions(rawValue: options.rawValue | UNAuthorizationOptions.provisional.rawValue)
}
```
  {% endtab %}
  {% tab Objective-C %}

**Objective-C**

```
UNUserNotificationCenter *center = [UNUserNotificationCenter currentNotificationCenter];
center.delegate = self;
UNAuthorizationOptions options = UNAuthorizationOptionAlert | UNAuthorizationOptionSound | UNAuthorizationOptionBadge;
if (@available(iOS 12.0, *)) {
    options = options | UNAuthorizationOptionProvisional;
}
```
  {% endtab %}
{% endtabs %}

### Interruption level (iOS 15+) {#interruption-level}

With iOS 15's new Focus Mode, users are more in control over when app notifications can "interrupt" them with a sound or vibration.

![iOS Notification Settings page that shows notifications enabled for immediate delivery and with time sensitive notifications enabled.]({% image_buster /assets/img/ios/ios15-notification-settings.png %}){: style="max-width:40%"}

Apps can now specify what level of interruption a notification should include, based on its urgency.

To change the interruption level for an iOS push notification, select the **Settings** tab and choose the desired level from the **Interruption Level** dropdown menu.

![Dropdown for selecting the interruption level.]({% image_buster /assets/img/ios/interruption_level.png %}){: style="max-width:50%"}

This feature does not have minimum SDK version requirements, but is only applied for devices running iOS 15+.

Keep in mind that users are ultimately the ones in control of their focus, and even if a Time Sensitive notification is delivered, they can specify which apps are not allowed to break through their focus.

Refer to the following table for interruption levels and their descriptions.

|Interruption Level|Description|When To Use|Break Through Focus Mode|
|--|--|--|--|
|[Passive](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/passive)|Sends a notification without sound, vibration, or turning on the screen.|Notifications that do not require immediate attention.|No|
|[Active](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/active) (default)|Will only make a sound, vibration, and turn on the screen if the user is not in Focus Mode.|Notifications that require immediate attention, unless the user has Focus Mode enabled.|No|
|[Time Sensitive](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/timesensitive)|Will make a sound, vibrate, and turn on the screen even while in Focus Mode. This requires that the **Time Sensitive Notifications capability** is added your app in Xcode|Timely notifications that should disturb users regardless of their Focus mode, such as a ride share or delivery notification.|Yes|
|[Critical](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/critical)|Will make a sound, vibrate, and turn on the screen even if the phone's **Do Not Disturb** switch is enabled. This [requires explicit approval by Apple](https://developer.apple.com/contact/request/notifications-critical-alerts-entitlement/).|Emergencies such as severe weather or safety alerts|Yes|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### Relevance score (iOS 15+) {#relevance-score}

![A notification summary for iOS titled "Your Evening Summary" with three notifications.]({% image_buster /assets/img/ios/ios15-notification-summary.png %}){: style="float:right;max-width:25%;margin-left:15px;border:0"}

iOS 15 also introduces a new way for users to optionally schedule a digest grouping of multiple notifications at designated times throughout the day. This is done to prevent constant interruptions throughout the day for notifications which don't need immediate attention.

Apps can specify which push notifications are most relevant by setting a **Relevance Score**. Apple will use this score to determine which notifications should be showcased in the scheduled Notification Summary while others are made available when users click into the summary. 

All notifications will still be accessible in the user's notification center.

To set an iOS Notification's Relevance Score, enter a value between `0.0` and `1.0` within the **Settings** tab. For example, the most important message should be sent with `1.0`, whereas a medium-importance message can be sent with `0.5`.

![Relevance score of "0.5".]({% image_buster /assets/img/ios/relevance-score.png %}){: style="max-width:80%;"}

This feature does not have minimum SDK version requirements, but is only applied for devices running iOS 15+.

For more information on maximum message lengths for different message types, refer to the following resources:

- [Image and text specifications]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/#image-and-text-specifications)
- [iOS character count guidelines]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/#character-count)

