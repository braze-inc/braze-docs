---
nav_title: "Creating a Push Message"
article_title: Creating a Push Campaign
page_order: 4
page_type: tutorial
description: "This tutorial page covers the different components involved in creating a Push Message, including configuration, sending, targeting, and more."
channel: push
tool:
  - Campaigns
  
---

# Creating a push message

> Push notifications are wonderful for time-sensitive calls to action, as well as re-engaging users who haven't come into the app in a while. Successful push campaigns drive the user directly to content and demonstrate the value of your app.

To see examples of push notifications, check out our [Case Studies][8].

## Step 1: Choose where to build your message {#create-new-campaign-push}

Not sure whether your message should be sent using a campaign or a Canvas? Campaigns are better for single, simple messaging campaigns, while Canvases are better for multi-step user journeys.

{% tabs %}
{% tab Campaign %}

**Steps:**

1. Go to the **Campaigns** page and click <i class="fas fa-plus"></i> **Create Campaign**.
2. Select **Push Notification**, or, for campaigns targeting multiple channels, select **Multichannel Campaign**.
3. Name your campaign something clear and meaningful.
4. Add [Teams]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/teams/) and [Tags]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/tags/) as needed.
   * Tags make your campaigns easier to find and build reports out of. For example, when using the [Report Builder]({{site.baseurl}}/user_guide/data_and_analytics/your_reports/report_builder/), you can filter by particular tags.
5. Add and name as many variants as you need for your campaign. You can choose different platforms, message types, and layouts for each of your added variants. For more on this topic, refer to [Multivariate and A/B testing]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).

{% alert tip %}
If all of the messages in your campaign are going to be similar or have the same content, compose your message before adding additional variants. You can then choose **Copy from Variant** from the **Add Variant** dropdown.
{% endalert %}

{% endtab %}
{% tab Canvas %}

**Steps:**

1. [Create your Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) using the Canvas wizard.
2. After you've set up your Canvas, add a step in the Canvas builder. Name your step something clear and meaningful.
3. Choose a [step schedule]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay) and specify a delay as needed.
4. Filter your Audience for this step as necessary. You can further refine the recipients of this step by specifying segments and adding additional filters. Audience options will be checked after the delay at the time messages are sent.
5. Choose your [advancement behavior]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/).
6. Choose any other messaging channels which you would like to pair with your message.

{% endtab %}
{% endtabs %}

## Step 2: Specify delivery platforms

Start by choosing which platform should receive the push: iOS, Android, or Web. Use this selection to limit the delivery of a push notification to a specific set of apps. For multichannel campaigns or Canvases, click **Add Messaging Channel** to add additional push platforms. 

Because platform selections are specific to each variant, you could try testing message engagement per platform!

## Step 3: Select notification type (iOS and Android)

For iOS and Android, select your notification type:

![Select notification type][3]{: style="float:right;max-width:40%;margin-left:15px;"}

- Standard Push
- [Push Stories]({{site.baseurl}}/user_guide/message_building_by_channel/push/advanced_push_options/push_stories/)
- Inline Image (Android only)

If you want to include images in your push campaign, refer to the following guides on creating a rich notification for [iOS]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/) or [Android]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/rich_notifications/).

## Step 4: Compose your push message

Now it's time to write your push message! The **Compose** tab allows you to edit all aspects of your message’s content and behavior.

![Compose tab of creating a push notification]({% image_buster /assets/img_archive/push_compose.png %})

The content of the **Compose** tab varies based on your chosen notification type in the previous step, but may include any of the following options:

#### Notification channel or group (iOS and Android)

For more information on platform-specific notification options, see [iOS Notification Options]({{site.baseurl}}/user_guide/message_building_by_channel/push/notification_options_ios/) or [Android Notification Options]({{site.baseurl}}/user_guide/message_building_by_channel/push/notification_options_android/).

#### Language

Add copy in multiple languages using the **Add Languages** button. We recommend selecting your languages before writing your content so you can fill in your text where it belongs in the Liquid. See our [full list of available languages][18].

#### Title and body

Start typing in the message box and watch a preview appear in the preview box to the left. Push messages must be formatted in plain text. To make your push personalized and targeted, you can include [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/).

#### Image

Where supported, your app icon is automatically added as the image for your push notification. You also have the option to send rich notifications, which allow for more customization in your push notifications by adding additional content beyond copy.

For additional guidance on using images in your push notifications, refer to the following articles:

- [Create rich notifications for iOS]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/)
- [Create rich notifications for Android]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/rich_notifications/)

#### On-click behavior

Specify what happens when a user clicks the body of a push notification with **On-Click Behavior**. For example, you can prompt customers to open your application, redirect customers to a specified Web URL, or even open a specific page of your application with a [deep link]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/).

Here, you can also set up button prompts within your push notification, such as:

- Accept/Decline
- Yes/No
- Confirm/Cancel
- More 

#### Device options

If desired, you can choose to only send your push to a user's most recently used device. If a user's most recently used device isn't [push enabled]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/#push-enabled), the message will not send.

For iOS, you can further limit messaging by only sending push notifications to iPad devices, or only sending to iPhone and iPod devices.

### Step 4a: Preview and test your message

![Test push message][7]{: style="float:right;max-width:30%;margin-left:15px;"}

Testing is arguably one of the most critical steps. After you finish composing your perfect push message, test it before sending it out. Select the **Test** tab and use **Preview Message as User** to get a sense of how your message may view on mobile. Use **Send Test** to send yourself a test push and ensure that your message displays properly.

## Step 5: Build the remainder of your campaign or Canvas

{% tabs %}
{% tab Campaign %}

Build the remainder of your campaign; see the sections below for further details on how to best utilize our tools to build push notifications.

#### Choose delivery schedule or trigger

Push messages can be delivered based on a scheduled time, an action, or based on an API trigger. For more, refer to [Scheduling your campaign]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

For action-based delivery, you can also set the campaign's duration and [Quiet Hours]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/time_based_campaign/#quiet-hours).

This step is also where you can specify delivery controls, such as allowing users to become [re-eligible]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/#campaigns) to receive the campaign, or enabling [frequency capping]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping) rules.

#### Choose users to target

Next, you need to [target users]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/targeting_users/) by choosing segments or filters to narrow down your audience. You'll automatically be given a snapshot of what that approximate segment population looks like right now. Detailed audience statistics for the channels targeted by your campaign are available in the footer. To see what percentage of your user base is being targeted and the Lifetime Value for this segment, click **Show Additional Stats**.

{% details Why does my Total Reachable Users metric not match the sum of all channels? %}

When you view the Total Reachable Users for your filtered audience, you may notice that the sum of the individual columns is smaller than the Total Reachable Users. This gap is usually because there are a number of users who qualify for the segment or filters in the campaign, but are not reachable through push (for example, because they don't have valid or active [push tokens]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/#push-tokens)).

{% enddetails %}

![Reachable Users Footer]({% image_buster /assets/img_archive/multi_channel_footer.png %})

Keep in mind that exact segment membership is always calculated just before the message is sent.

You can also choose to only send your campaign to users who have a specific [subscription status]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/), such as those who are subscribed and opted in to push.

Optionally, you can also limit delivery to a specified number of users within the segment, or allow users to receive the same message twice upon a recurrence of the campaign.

##### Multichannel campaigns with email and push

For multichannel campaigns targeting both email and push channels, you may want to limit your campaign so that only the users who are explicitly opted in will receive the message (excluding subscribed or unsubscribed users). For example, say you have three users of different opt-in statuses:

- **User A** is subscribed to email and is push enabled. This user doesn't receive the email but will receive the push.
- **User B** is opted-in to email but is not push enabled. This user will receive the email but doesn't receive the push.
- **User C** is opted-in to email and is push enabled. This user will receive both the email and the push.

To do so, under **Audience Summary**, select to send this campaign to "opted-in users only". This option will ensure that only opted-in users will receive your email, and Braze will only send your push to users who are push enabled by default.

{% alert important %}
With this configuration, don't include any filters in the **Target Users** step that limit the audience to a single channel (e.g., `Push Enabled = True` or `Email Subscription = Opted-In`).
{% endalert %}

#### Choose conversion events

Braze allows you to track how often users perform specific actions, [conversion events]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/), after receiving a campaign. You have the option of allowing up to a 30-day window during which a conversion will be counted if the user takes the specified action.

{% endtab %}

{% tab Canvas %}

If you haven't done so already, complete the remaining sections of your Canvas step. For further details on how build out the rest of your Canvas, implement multivariate testing and Intelligent Selection, and more, refer to the [Build your Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) step of our Canvas documentation.

{% endtab %}
{% endtabs %}

## Step 6: Review and deploy {#review-and-deploy-push}

After you’ve finished building the last of your campaign or Canvas, review its details. For campaigns, the final page will give you a summary of the campaign you've just designed. Confirm all the relevant details, make sure you've tested your message, then send it and watch the data roll in!

Next, check out [Push reporting]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_reporting/) to learn how you can access the results of your push campaign. For push notifications, you'll be able to view statistics for the number of messages sent, delivered, bounced, opened, and directly opened.

[1]: {% image_buster /assets/img_archive/new_campaign_push.png %}
[2]: {% image_buster /assets/img_archive/push_1.png %}
[3]: {% image_buster /assets/img_archive/push_2.png %}
[4]: {% image_buster /assets/img_archive/schedule.png %}
[5]: {% image_buster /assets/img_archive/confirmation_page.png %}
[6]: {% image_buster /assets/img_archive/push-results-statistics.png %}
[7]: {% image_buster /assets/img_archive/push_3.png %}
[8]: https://www.braze.com/customers
[15]: {% image_buster /assets/img_archive/conversion_event_selection.png %}
[18]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization/#languages-supported
[24]: {% image_buster /assets/img_archive/multi_channel_footer.png %}
[25]: {% image_buster /assets/img_archive/target_segmenter.png %} 
