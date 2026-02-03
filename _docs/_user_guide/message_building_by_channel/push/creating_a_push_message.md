---
nav_title: Create a push message
article_title: Create a Push Campaign
page_order: 4
page_type: tutorial
description: "This tutorial page covers the different components involved in creating a Push Message, including configuration, sending, targeting, and more."
channel: push
tool:
  - Campaigns
  
---

# Create a push message

> Push notifications are wonderful for time-sensitive calls to action, as well as re-engaging users who haven't come into the app in a while. Successful push campaigns drive the user directly to content and demonstrate the value of your app. To see examples of push notifications, check out our [case studies](https://www.braze.com/customers).

## Step 1: Choose where to build your message {#create-new-campaign-push}

{% alert tip %}
Not sure whether to use a campaign or a Canvas? Campaigns are better for single, targeted messaging campaigns, while Canvases are better for multi-step user journeys.
{% endalert %}

{% tabs %}
{% tab Campaign %}
1. Go to **Messaging** > **Campaigns**, then select **Create campaign**.
2. For campaigns targeting multiple channels, select **Multichannel**. Otherwise, select **Push notification**. If you're still not sure, refer to **Deciding between regular or multichannel push campaign** below.
3. Name your campaign something clear and meaningful.
4. Add [Teams]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) and [Tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) as needed. 

{% alert tip %} 
Tags make your campaigns easier to find and build reports out of. For example, when using the [Report Builder]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/), you can filter by particular tags.
{% endalert %}

{: start="5"}
5. Add and name as many variants as you need for your campaign. You can choose different platforms, message types, and layouts for each of your added variants. For more on this topic, refer to [Multivariate and A/B testing]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).

{% details Deciding between regular or multichannel push campaign %}

If you intend to target multiple devices and platforms, such as any combination of mobile, web, Kindle, iOS, and Android, your selection at this step can impact the availability of some features and settings later on.

Refer to the following decision chart before creating a multichannel or push notification campaign:

!["Flowchart for selecting campaign type. Starts by deciding if you're targeting multiple devices and platforms. If no, it leads to 'Select Push Notification.' If yes, it asks 'What type of push message?' and options are 'Standard push' leading to a decision point 'Do you need to use device-specific settings?' If no, it leads to 'Select Push Notification and use quick push.' If yes, it goes to 'Select Multichannel.' Back to 'What type of push message?', if the answer is 'Push Stories or Inline image,' it directs to 'Select Multichannel."]({% image_buster /assets/img_archive/flowchart_quickpush.png %})

If you select **Push Notification** and choose to target multiple devices and platforms, you’re automatically creating a quick push campaign. With quick push, certain device-specific settings are not available:

- Push action buttons
- Notification channels and groups
- Push time-to-live (TTL)
- Display priority
- Sounds

Before continuing, refer to [Quick push campaigns]({{site.baseurl}}/quick_push) to understand what's different for this editing experience.

{% enddetails %}

{% alert tip %}
If all of the messages in your campaign are going to be similar or have the same content, compose your message before adding additional variants. You can then choose **Copy from Variant** from the **Add Variant** dropdown.
{% endalert %}

{% endtab %}
{% tab Canvas %}
1. [Create your Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) using the Canvas composer.
2. After you've set up your Canvas, add a step in the Canvas builder. Name your step something clear and meaningful.
3. Choose a [step schedule]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay) and specify a delay as needed.
4. Filter your Audience for this step as necessary. You can further refine the recipients of this step by specifying segments and adding additional filters. Audience options will be checked after the delay at the time messages are sent.
5. Choose your [advancement behavior]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/).
6. Choose any other messaging channels which you would like to pair with your message.

{% endtab %}
{% endtabs %}

## Step 2: Select push platforms

Next, choose which platform and mobile device combination should receive the push. Use this selection to limit the delivery of a push notification to a specific set of apps.

There are a few different ways to do this depending on your previous selections:

| Previous selection | Options |
| --- | --- | 
| Push notification campaign | Select one or more platforms and devices. If you choose to target multiple devices and platforms, you’re automatically creating a quick push campaign. This provides an editing experience optimized for crafting one message for all selected platforms in a single editor. See [Quick push campaigns]({{site.baseurl}}/quick_push) to understand what's different in this editing experience. |
| Multichannel campaign | Select **Add Messaging Channel** to add additional push platforms. Because platform selections are specific to each variant, you can try testing message engagement per platform.
| Canvas | In your Message step, select **+ Add more** to add additional push platforms. Similar to multichannel campaigns, platform selections are specific to each variant. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Step 3: Select notification type (iOS and Android)

If you're creating a quick push campaign, the notification type is automatically set to **Standard push** and cannot be changed.

![Notification Type with Standard Push selected as an example.]({% image_buster /assets/img_archive/push_2.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Otherwise, for iOS and Android, select your notification type:

- Standard push
- [Push stories]({{site.baseurl}}/user_guide/message_building_by_channel/push/advanced_push_options/push_stories/)
- Inline image (Android only)

If you want to include images in your push campaign, refer to the following guides on creating a rich notification for [iOS]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/) or [Android]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/rich_notifications/).

## Step 4: Compose your push message

Now it's time to write your push message! The **Compose** tab allows you to edit all aspects of your message's content and behavior.

![Compose tab of creating a push notification.]({% image_buster /assets/img_archive/push_compose.png %})

The content of the **Compose** tab varies based on your chosen notification type in the previous step, but may include any of the following options:

#### Notification channel or group (iOS and Android)

For more information on platform-specific notification options, see [iOS Notification Options]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/) or [Android Notification Options]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/notification_options/).

#### Language

Add copy in multiple languages using the **Add Languages** button. We recommend selecting your languages before writing your content so you can fill in your text where it belongs in the Liquid. For our full list of available languages you can use, refer to [Languages supported]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization/#languages-supported).

If you're adding copy in a language that is written right-to-left, note that the final appearance of right-to-left messages depends largely on how service providers render them. For best practices on crafting right-to-left messages that display as accurately as possible, refer to [Creating right-to-left messages]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/).

#### Title and body

{% tabs local %}
{% tab ios %}
Start typing in the message box and watch a preview appear in the preview box to the left. Push messages must be formatted in plain text. 

Add a headline using the **Title** field. To make your push personalized and targeted, you can include [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/).
{% endtab %}

{% tab android %}
Start typing in the message box and watch a preview appear in the preview box to the left. Push messages must be formatted in plain text. 

To make your push personalized and targeted, you can include [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/).

{% alert important %}
You **cannot** send an Android push message without a title&#8212;however, you can enter a single space instead. Keep in mind, if your message only contains a single space, it will be sent as a silent push notification. For more information, refer to [Silent push notifications]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=android).
{% endalert %}
{% endtab %}
{% endtabs %}

{% alert tip %}
Need help creating awesome copy? Try using the [AI copywriting assistant]({{site.baseurl}}/user_guide/brazeai/generative_ai/copywriting/). Input a product name or description and the AI will generate human-like marketing copy for use in your messaging.

![Launch AI Copywriter button, located in the Body field of the push composer.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_push.png %}){: style="max-width:60%"}
{% endalert %}

#### Image

Where supported, your app icon is automatically added as the image for your push notification. You also have the option to send rich notifications, which allow for more customization in your push notifications by adding additional content beyond copy.

For additional guidance on using images in your push notifications, refer to the following articles:

- [Create rich notifications for iOS]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/)
- [Create rich notifications for Android]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/rich_notifications/)

#### On-click behavior

Specify what happens when a user selects the body of a push notification with **On-Click Behavior**. For example, you can prompt customers to open your application, redirect customers to a specified Web URL, or even open a specific page of your application with a [deep link]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/).

Here, you can also set up button prompts within your push notification, such as:

- Accept/Decline
- Yes/No
- Confirm/Cancel
- More 

#### Sending options

If a user has your app installed on multiple devices, by default, your push message is sent to all devices with a valid push token assigned. If desired, you can select **Most recently used device**.

![Device options checkbox to only send this push to the user's most recently used device.]({% image_buster /assets/img_archive/push_recent_device.png %}){: style="max-width:70%;" }

There is some nuance for this setting. If this option is selected, Braze will limit multiple sends from occurring except when a campaign targets multiple platforms, such as both iOS and Android. If the user has your app on both an iOS and an Android device, they'll receive a push for both platforms. If a user's most recently used device isn't [push enabled]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/#foreground-push-enabled), the message will not send.

For iOS, you can further limit messaging by only sending push notifications to iPad devices, or only sending to iPhone and iPod devices.

## Step 5: Preview and test your message (optional)

Testing is arguably one of the most critical steps. After you finish composing your perfect push message, test it before sending it out. Select the **Test** tab to choose from options on how to test your push message. In **Test Recipients**, you can select a content test group or individual users. You can also use **Preview message as user** to get a sense of how your message may view on mobile for a random user, existing user, custom user, or multi-language user.

## Step 6: Build the remainder of your campaign or Canvas

{% tabs %}
{% tab Campaign %}

Build the remainder of your campaign; see the following sections for further details on how to best use our tools to build push notifications.

#### Choose delivery schedule or trigger

Push messages can be delivered based on a scheduled time, an action, or based on an API trigger. For more, refer to [Scheduling your campaign]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

For action-based delivery, you can also set the campaign's duration and [Quiet Hours]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/time_based_campaign/#quiet-hours).

This step is also where you can specify delivery controls, such as allowing users to become [re-eligible]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/#campaigns) to receive the campaign, or enabling [frequency capping]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping) rules.

#### Choose users to target

Next, you must [target users]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/) by choosing segments or filters to narrow your audience. You automatically receive a preview of what that approximate segment population looks like. Detailed audience statistics for the channels targeted by your campaign are available in the footer. To see what percentage of your user base is being targeted and the Lifetime Value for this segment, select **Show Additional Stats**.

{% multi_lang_include target_audiences.md %}

{% details Why does my Total Reachable Users metric not match the sum of all channels? %}

When you view the Total Reachable Users for your filtered audience, you may notice that the sum of the individual columns is smaller than the Total Reachable Users. This gap is usually because there are a number of users who qualify for the segment or filters in the campaign, but are not reachable through push (for example, because they don't have valid or active [push tokens]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/#push-tokens)).

{% enddetails %}

![Table of detailed audience statistics for Reachable Users.]({% image_buster /assets/img_archive/multi_channel_footer.png %})

Keep in mind that exact segment membership is always calculated before the message is sent.

You can also choose to only send your campaign to users who have a specific [subscription status]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/), such as those who are subscribed and opted in to push.

Optionally, you can also limit delivery to a specified number of users within the segment, or allow users to receive the same message twice upon a recurrence of the campaign.

##### Multichannel campaigns with email and push

For multichannel campaigns targeting both email and push channels, you may want to limit your campaign so that only the users who are explicitly opted in will receive the message (excluding subscribed or unsubscribed users). For example, say you have three users of different opt-in statuses:

- **User A** is subscribed to email and is push enabled. This user doesn't receive the email but will receive the push.
- **User B** is opted-in to email but is not push enabled. This user will receive the email but doesn't receive the push.
- **User C** is opted-in to email and is push enabled. This user will receive both the email and the push.

To do so, under **Audience Summary**, select to send this campaign to "opted-in users only". This option will ensure that only opted-in users will receive your email, and Braze will only send your push to users who are push enabled by default.

{% alert important %}
With this configuration, don't include any filters in the **Target Audiences** step that limit the audience to a single channel (for example, `Foreground Push Enabled = True` or `Email Subscription = Opted-In`).
{% endalert %}

#### Choose conversion events

Braze allows you to track how often users perform specific actions, [conversion events]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/), after receiving a campaign. You have the option of allowing up to a 30-day window during which a conversion will be counted if the user takes the specified action.

{% endtab %}

{% tab Canvas %}

If you haven't done so already, complete the remaining sections of your Canvas component. For further details on how build out the rest of your Canvas, implement multivariate testing and Intelligent Selection, and more, refer to the [Build your Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) step of our Canvas documentation.

{% endtab %}
{% endtabs %}

## Step 7: Review and deploy {#review-and-deploy-push}

After you've finished building the last of your campaign or Canvas, review its details. For campaigns, the final page gives you a summary of the campaign you designed. Confirm all the relevant details, make sure you've tested your message, then send it and watch the data roll in!

Next, check out [Push reporting]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_reporting/) to learn how you can access the results of your push campaign. For push notifications, you'll be able to view statistics for the number of messages sent, delivered, bounced, opened, and directly opened.

