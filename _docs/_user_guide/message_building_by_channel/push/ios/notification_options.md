---
nav_title: "Notification Options (iOS)"
page_order: 2
page_layout: reference
description: "This reference article covers iOS notification options like critical alerts, quiet notifications, provisional push notifications, and more."

platform: iOS
channel:
  - push
tool:
  - Dashboard
  - Campaigns
---

# iOS Notification Options

> With the release of Apple's iOS 12, Braze offers support for several of its features, including [Notification Groups](#notification-groups), [Quiet Notifications/Provisional Authorization](#provisional-push-authentication--quiet-notifications), and [Critical Alerts](#critical-alerts).

## Notification Groups

If you want to categorize your messages and group them in your user's notification tray, you can utilize iOS's Notification Groups feature through Braze.

Create your iOS push campaign, then look to the top of the composer. There, you'll see a dropdown labeled Notification Groups.

![notificationgroupsdropdown][26]

From there, you can select any Notification Groups. If your notification group settings malfunction or you select __None__ from the dropdown, the message will automatically send as normal to all defined users in the app group.

If you don't have any Notification Groups listed here, you can add one using the iOS Thread ID. You will need one iOS Thread ID for every Notification Group you want to add. Then, add it to your Notification Groups by clicking __Manage Notification Groups__ in the dropdown and filling out the required fields in the __Manage iOS Push Notification Groups__ window that appears.

![managenotgroups][27]

### Summary Arguments and Categories

__Summary Arguments__

In addition to grouping notifications by Thread IDs, Apple allows you to edit the summaries that appear when notifications are grouped. Braze Users can specify the summary category, summary count, and summary argument when composing a push campaign using our tool.

{% alert tip %}
Note that the way notifications with the same Thread ID are grouped in the notification tray is under the control of the OS. iOS may choose to display notifications with the same Thread ID separately or in groups depending on what it deems optimal.
{% endalert %}

Check the __Alert Options__ box in the __Push Composer__.

Then, select `summary-arg` and `summary-arg-count` as keys and input those values in the corresponding column. If you do not set a value for `summary-arg`, it will default to 1.

__Summary Categories__

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
Please note that `%u` and `%@` are formatting strings for the summary count and summary argument, respectively. When the summary is shown, these placeholders will be replaced with the values for `summary-count` and `summary-arg`.
{% endalert %}

Once this is set up on your app, use the summary category by checking the __Notification Buttons__ box and selecting __Enter Pre-registered iOS Category__.

Then, input the summary category identifier that you set in your app.

### Provisional Push Authentication & Quiet Notifications

Apple allows brands the option to send quiet push notifications to their users' Notification Centers _before_ they officially, explicitly opt-in, giving you a chance to demonstrate the value of your messages early. All you need to do is [set up](#set-up-provisional-push-notifications) provisional push notifications in your app, then any user who has a provisional push token will receive your messages.

Unlike a traditional iOS push token, a provisional push token acts as a "trial pass" that allows brands to reach out to new users before they've seen and clicked Apple's native push opt-in prompt. With this feature, your push notification will be delivered directly to your new user's notification tray with the option to "Keep" or "Turn Off" future notifications. Instead of experiencing an "opt-in" journey, users will experience something more akin to an "opt-out" journey.

{% alert tip %}
Provisional Authorization has the potential dramatically increase your opt-in rate, but only if users see value in your messages. Be sure to use our [user segmentation]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/), [location targeting]({{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences/about/), and [personalization]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/) features to ensure that the appropriate users are getting these "trial" notifications at the right time. Then, you can encourage users to fully opt-in to your push notifications, knowing that they add value to your users' experience with your app.
{% endalert %}

Whichever option the user chooses will add the appropriate token or [subscription status]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/) to their [Contact Settings (under the Engagement Tab in their user profile)]({{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/#engagement-tab) (shown below).

![User Profile Provisionally Authorized]({% image_buster /assets/img/profile-push-prov-auth.png %}){: width="50%"}

You will be able to target your users based on whether they are provisionally authorized or not using our [segmentation filters]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/) (shown below).

![Provisionally Authorized Segment]({% image_buster /assets/img/segment-push-prov-auth.png %})

{% alert tip %}
If users choose to "Turn Off" provisional push from you, they won't see any more provisional push messages from you. Be thoughtful about the message content and cadence sent using this functionality!
{% endalert %}

{% alert important %}
If you utilize additional push prompts or [in-app push primers](https://www.braze.com/resources/glossary/priming-for-push/) (an in-app message that encourages users to opt-in to push notifications), please reach out to your Braze representative for additional guidance.
{% endalert %}

#### Set Up Provisional Push Notifications
Braze allows you to register for Provisional Authentication by updating your code in your _token registration snippet_ within your Braze iOS SDK implementation using the snippets below as an example (send these to your developers or ensure they [implement provisional push authentication during the integration process]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/#using-usernotification-framework-ios-10)).

{% alert warning %}
The implementation of Provisional Push Authentication only supports iOS 12+ and will error out if the deployment target is before that. You can learn more about this [in our more detailed implementation documentation here]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/#using-usernotification-framework-ios-10).
{% endalert %}

{% tabs local %}
  {% tab Swift %}
__Swift__

```
var options: UNAuthorizationOptions = [.alert, .sound, .badge]
if #available(iOS 12.0, *) {
  options = UNAuthorizationOptions(rawValue: options.rawValue | UNAuthorizationOptions.provisional.rawValue)
}
```
  {% endtab %}
  {% tab Objective-C %}

__Objective-C__

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

### Critical Alerts
Apple will allow some brands to send notifications that are considered extremely important, will ignore Do Not Disturb settings, and will always play a sound no matter the setting on a user's device.

Brands [must be approved by Apple](https://developer.apple.com/contact/request/notifications-critical-alerts-entitlement/) to use Critical Alerts. Good candidates for this feature could be apps with medical and other health-related information, home security, and public safety features. You must do this before using the feature in Braze.

_Users will still be able to turn off Critical Alerts on a per-app basis, separately from other notifications._

Braze will give you the ability to select __Send Critical Alert__ under __Alert Options__ in the iOS Push Composer, which will then allow you to specify the notification as a Critical Alert.

{% alert warning %}
This feature is still in beta. Additionally, if you attempt to use this feature without pre-approval by Apple, your message will not be allowed to send. Contact your account manager before attempting to use this feature.
{% endalert %}


[26]: {% image_buster /assets/img_archive/notgroupclickdropdown.gif %}
[27]: {% image_buster /assets/img_archive/managenotgroups.png %}
