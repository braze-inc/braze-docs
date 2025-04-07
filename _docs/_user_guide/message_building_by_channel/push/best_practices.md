---
page_order: 20
nav_title: Best Practices
article_title: Push Best Practices
description: "This page contains push best practices and use cases to make sure your push messages inspire engagement rather than annoyance."
channel: push
---

# Push best practices

Push notifications are powerful tools for engaging with your app's users, but they should be used with care to ensure they deliver timely and relevant messages. Before sending your push message, refer to the following best practices for things you should know and check for.

{% alert important %}
Your push messages must fall within the guidelines of the Apple App Store and Google's Play Store policies, specifically regarding using push messages as advertisements, spam, promotions, and more. Learn more about [Mobile push regulations]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/#mobile-push-regulations-for-apps).
{% endalert %}

## Compose your push message

As a best practice, Braze recommends keeping each line of text for both the optional title and message body to approximately 30-40 characters in a mobile push notification. Note that the character counter in the composer doesn't account for Liquid characters. This means the final character count of a message depends on how Liquid renders for each user. When in doubt, keep it short and sweet.

## Optimize targeting

### Collect relevant user data

Push notifications should be treated with care to target users with timely and relevant notifications. Braze will collect useful device and usage information that can be used to target relevant segments. This information should be supplemented with custom events and attributes specific to your app. Using that data, you can carefully target messages to increase open rates and decrease instances of users disabling push.

### Create a notification settings page

You can create a settings page in your app that lets users tell you which notifications they want to receive. A common approach is to create a boolean custom attribute in Braze corresponding to the app setting status. For example, a news app could have subscription settings for breaking news, sports news, or politics.

When the news app wants to create a campaign targeting only users interested in Politics, they add the `Subscribes to Politics` attribute filter to the segment. When set to true, only users who subscribe to notifications will receive them.

For more information on setting custom attributes, refer to the following articles for [iOS][6], [Android][7], or [REST API][8].

## Increase opt-ins and relevance

### Obtain user permission

The general stats for push enabled will relate to whether the user has approved notifications with their operating system. If users turn off notifications on iOS, they'll be automatically removed from our system since Apple won't allow the push token to be sent.

Android 13 and up requires obtaining permission before push notifications can be shown. Older versions of Android will subscribe users to notifications by default.

### Prime users for push

You only get one chance to ask a user for push permission, and after they decline, it's very hard to convince them to re-enable push in their device settings. For this reason, you should prime users for push using an in-app message before showing the system prompt. See [Push primer in-app messages][2] to learn more about increasing opt-ins.

### Add push subscription controls

To avoid users turning off notifications at the device level, which completely removes their foreground push token, let users control their push subscription directly within your app. See [Updating push subscription states][10] for more details.

### Understand push subscription states

Push subscription state does not guarantee that a push will be delivered—users must also be push enabled to receive notifications. This is because a user profile may have multiple devices with different foreground push permissions but only a single push subscription state.

If a user doesn't have a valid foreground push token for an app (that is, they turn off push tokens at the device level through settings, opting not to receive notifications), their subscription state can still be considered `subscribed` to push. However, this user would not be `Push Enabled for App` in Braze since the foreground push token is not valid.

Additionally, if a user profile has no valid or registered push token for any other apps, their `Push Enabled` filter in segmentation will also be false.

## Implement a sunset policy for unresponsive users

Even when you send only relevant, timely push notifications, some users may still be unresponsive to them and find them spammy. Suppose a user shows a history of repeatedly ignoring your push notifications. In that case, it's a good idea to stop sending them pushes before they become annoyed with your app's communications or uninstall it altogether. 

To do this, create a [sunset policy][9] that eventually stops sending push notifications to users who haven't had a direct or influenced open for a long time.

1. Identify unresponsive users based on direct or influenced opens.
2. Gradually stop sending push notifications to those users.
3. Before removing push notifications entirely, deliver one final notification explaining why they will no longer receive them. This gives users a chance to demonstrate their interest in continued pushes by opening that notification.
4. After the sunset policy goes into effect, use an [in-app message][13] to remind these users that while they will no longer receive pushes, in-app messaging channels will continue to deliver interesting, helpful information.

Although you may be reluctant to stop sending pushes to users who originally opted into them, remember that other messaging channels can more effectively reach these users, especially if they have previously ignored your pushes. If the user opens your emails, email campaigns are a good way to reach them outside your app. If not, then in-app messages are the best way to deliver content without risking the user uninstalling your app.

## Set conversion events for app opens

When assigning [conversion events][11] to a push campaign, you can track app opens for a certain period after the campaign is received. Setting a conversion event for app opens provides different insight from the results statistics you normally receive after a push campaign.

While all push campaign results break down a message's direct opens and opens (which includes both direct and [influenced opens][12]), conversion tracking will track any type of open, whether direct or influenced.

In addition, by using the conversion event "opens app," you are tracking app opens that occur before that conversion deadline (for instance, three days). This differs from an influenced open in that the time a user has to register an influenced open can vary from person to person, depending on each user's past engagement behavior.

## Related articles

Didn't find what you were looking for? Check out these additional best practices articles:

- [Push message and image formats][1]
- [Push primer in-app messages][2]
- [Deliverability for Chinese Android devices][3]
- [Know before you send: channels][4]

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/message_format/
[2]: {{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/
[3]: {{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/chinese_push_deliverability/
[4]: {{site.baseurl}}/help/help_articles/campaigns_and_canvas/know_before_send/

[6]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_custom_attributes/
[7]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_custom_attributes/#setting-custom-attributes
[8]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-attributes-object-specification
[9]: {{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/sunset_policies
[10]: {{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions#update-push-subscription-state
[11]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/
[12]: {{site.baseurl}}/user_guide/data_and_analytics/tracking/influenced_opens
[13]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about/