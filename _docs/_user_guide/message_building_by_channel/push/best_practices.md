---
page_order: 20
nav_title: Best practices
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

## Reduce push notification payload size

The maximum payload size depend on the platform.

| Platform | Maximum payload size |
| --- | --- |
| Web | 3,807 bytes |
| Android | 3,930 bytes |
| iOS | 3,960 bytes |
| Kindle | 5,985 bytes |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

If your push exceeds the maximum payload size, the message may not be sent. As a best practice, keep your payload to a few hundred bytes.

### What is a push payload?

Push service providers calculate whether your push notification can be displayed to a user by looking at the byte size of the entire push payload. The payload is limited to **4KB (4,096 bytes)** for most push services, including:

- Apple Push Notification service (APNs)
- Android’s Firebase Cloud Messaging (FCM)
- Web push
- Huawei push

These push services will refuse any notification that exceeds this limit.

Braze reserves a portion of the push payload for integration and analytics purposes. Given that, our maximum payload size is **3,807 bytes**. If your push exceeds this size, the message may not be sent. As a best practice, keep your payload to a few hundred bytes.

The following elements in your push make up your push payload:

- Copy, such as the title and message body
- Final render of any Liquid personalization
- URLs for images (but not the size of the image itself)
- URLs for click targets
- Button names
- Key-value pairs

### Tips to reduce payload size

To reduce payload size:

- Keep your message brief. A good general guideline is to make it actionable and beneficial in less than 40 characters.
- Omit whitespace and line breaks from your copy.
- Consider how Liquid will render on send. Because the final render of any Liquid personalization will vary from user to user, Braze can't determine if a push payload will exceed the size limit when Liquid is included. If your Liquid renders a shorter message, you might be fine. However, if your Liquid results in a longer message, your push may exceed the payload size limit. Always test your push message on a real device before sending it to users.
- Consider shortening URLs using a URL shortener.

## Optimize targeting

### Collect relevant user data

Push notifications should be treated with care to target users with timely and relevant notifications. Braze will collect useful device and usage information that can be used to target relevant segments. This information should be supplemented with custom events and attributes specific to your app. Using that data, you can carefully target messages to increase open rates and decrease instances of users disabling push.

### Create a notification settings page

You can create a settings page in your app that lets users tell you which notifications they want to receive. A common approach is to create a boolean custom attribute in Braze corresponding to the app setting status. For example, a news app could have subscription settings for breaking news, sports news, or politics.

When the news app wants to create a campaign targeting only users interested in Politics, they add the `Subscribes to Politics` attribute filter to the segment. When set to true, only users who subscribe to notifications will receive them.

For more information on setting custom attributes, refer to the following articles for [iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=swift), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_custom_attributes/#setting-custom-attributes), or [REST API]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-attributes-object-specification).

## Increase opt-ins and relevance

### Obtain user permission

The general stats for push enabled will relate to whether the user has approved notifications with their operating system. If users turn off notifications on iOS, they'll be automatically removed from our system since Apple won't allow the push token to be sent.

Android 13 and up requires obtaining permission before push notifications can be shown. Older versions of Android will subscribe users to notifications by default.

### Prime users for push

You only get one chance to ask a user for push permission, and after they decline, it's very hard to convince them to re-enable push in their device settings. For this reason, you should prime users for push using an in-app message before showing the system prompt. See [Push primer in-app messages]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/) to learn more about increasing opt-ins.

### Add push subscription controls

To avoid users turning off notifications at the device level, which completely removes their foreground push token, let users control their push subscription directly within your app. See [Updating push subscription states]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions#update-push-subscription-state) for more details.

### Understand push subscription states

Push subscription state does not guarantee that a push will be delivered—users must also be push enabled to receive notifications. This is because a user profile may have multiple devices with different foreground push permissions but only a single push subscription state.

If a user doesn't have a valid foreground push token for an app (that is, they turn off push tokens at the device level through settings, opting not to receive notifications), their subscription state can still be considered `subscribed` to push. However, this user would not be `Foreground Push Enabled for App` in Braze since the foreground push token is not valid.

Additionally, if a user profile has no valid or registered push token for any other apps, their `Foreground Push Enabled` filter in segmentation will also be false.

## Implement a sunset policy for unresponsive users

Even when you send only relevant, timely push notifications, some users may still be unresponsive to them and find them spammy. Suppose a user shows a history of repeatedly ignoring your push notifications. In that case, it's a good idea to stop sending them pushes before they become annoyed with your app's communications or uninstall it altogether. 

To do this, create a [sunset policy]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/sunset_policies) that eventually stops sending push notifications to users who haven't had a direct or influenced open for a long time.

1. Identify unresponsive users based on direct or influenced opens.
2. Gradually stop sending push notifications to those users.
3. Before removing push notifications entirely, deliver one final notification explaining why they will no longer receive them. This gives users a chance to demonstrate their interest in continued pushes by opening that notification.
4. After the sunset policy goes into effect, use an [in-app message]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about/) to remind these users that while they will no longer receive pushes, in-app messaging channels will continue to deliver interesting, helpful information.

Although you may be reluctant to stop sending pushes to users who originally opted into them, remember that other messaging channels can more effectively reach these users, especially if they have previously ignored your pushes. If the user opens your emails, email campaigns are a good way to reach them outside your app. If not, then in-app messages are the best way to deliver content without risking the user uninstalling your app.

## Set conversion events for app opens

When assigning [conversion events]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/) to a push campaign, you can track app opens for a certain period after the campaign is received. Setting a conversion event for app opens provides different insight from the results statistics you normally receive after a push campaign.

While all push campaign results break down a message's direct opens and opens (which includes both direct and [influenced opens]({{site.baseurl}}/user_guide/analytics/tracking/influenced_opens/)), conversion tracking will track any type of open, whether direct or influenced.

In addition, by using the conversion event "opens app," you are tracking app opens that occur before that conversion deadline (for instance, three days). This differs from an influenced open in that the time a user has to register an influenced open can vary from person to person, depending on each user's past engagement behavior.

## Related articles

Didn't find what you were looking for? Check out these additional best practices articles:

- [Push message and image formats]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/message_format/)
- [Push primer in-app messages]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/)
- [Deliverability for Chinese Android devices]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/chinese_push_deliverability/)
- [Know before you send: channels]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/know_before_send/)
