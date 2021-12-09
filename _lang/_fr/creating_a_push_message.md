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

> Push notifications are wonderful for time-sensitive calls to action, as well as re-engaging users who haven't come into the app in a while. <br><br> Successful push campaigns drive the user directly to content and demonstrate the value of your app.

_To see examples of push notifications, check out our [Case Studies][8]._

## Step 1: Create a new push campaign {#create-new-campaign-push}

!\[Create new push campaign\]\[1\]{: style="float:right;max-width:25%;margin-left:15px;"}

Navigate to the **Campaigns** page and create a new push campaign. Click __Create Campaign__ and select __Push Notification__. Or, if you want to include multiple channels in addition to Push, select **Multichannel Campaign**.

## Step 2a: Name your campaign, choose messaging types, and compose your message

Give your campaign a name and select the platform you want to target. For multichannel campaigns, click **Add Messaging Channel** to add additional push platforms.

!\[Select push platform\]\[2\]

!\[Select notification type\]\[3\]{: style="float:right;max-width:50%;margin-left:15px;"}

For iOS or Android, select your notification type:

- Standard Push
- [Push Stories]({{site.baseurl}}/user_guide/message_building_by_channel/push/advanced_push_options/push_stories/)
- Inline Image (Android only)

If you want to include images in your push campaign, refer to the following guides on creating a rich notification for [iOS]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/) or [Android]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/rich_notifications/).

Now it's time to write your push message! Start typing in the message box and watch a preview appear in the preview box to the left. Push messages must be formatted in plain text, but can include [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) to make your push personalized and targeted.

### Additional push customization steps

#### Languages

Add copy in multiple languages using the __Add Languages__ button. Insert Liquid into your message to set custom messages and fields in specific languages based on a customer's language preferences. Check out example use cases in our [Liquid Use Case Library]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/liquid_use_cases/#language).

#### On click behavior

Specify what happens when a user clicks the body of a push notification with **On Click Behavior**. For example, you can prompt customers to open your application, redirect customers to a specified Web URL, or even open a specific page of your application with a [deep link]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/).

Here, you can also set up button prompts within your push notification, such as:

- Yes/No
- Confirm/Cancel
- More

{% alert note %}
For more information on platform-specific notification options, see [iOS Notification Options]({{site.baseurl}}/user_guide/message_building_by_channel/push/notification_options_ios/) or [Android Notification Options]({{site.baseurl}}/user_guide/message_building_by_channel/push/notification_options_android/).
{% endalert %}

### Step 2b: Preview and test your message

!\[Test push message\]\[7\]{: style="float:right;max-width:30%;margin-left:15px;"}

Testing is arguably one of the most critical steps. After you finish composing your perfect push message, test it before sending it out. Select the **Test** tab and use **Preview Message as User** to get a sense of how your message may view on mobile. Use **Send Test** to send yourself a test push and ensure that your message displays properly.

## Step 3: Schedule your push messaging campaign {#schedule-push-campaign}

Choose between sending your campaign at a scheduled time, after users complete an action, or via an API request.

!\[Schedule\]\[4\]

{% tabs %}
  {% tab Scheduled Delivery %}
Use [Scheduled Delivery]({{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/scheduled_delivery/) to specify the time you want your campaign to send, either immediately or at a future time (you can also consider a user's local time in your scheduling).

Not sure what the best time is to send your campaign? Use [Intelligent Timing]({{site.baseurl}}/user_guide/intelligence/intelligent_timing/) to send your campaign when a user is most likely to engage. Braze makes this calculation based on a statistical analysis of the user's interactions with your app.

Messages can also be configured to recur on a daily, weekly (optionally on specific days), or monthly basis.

{% endtab %}
{% tab Action-Based Delivery %}

Use [Action-Based Delivery]({{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/triggered_delivery/) to specify the time a message will send after a user takes a particular action. Configure messages to send immediately or after a delay (you can also consider a user's local time in your scheduling).

{% endtab %}
{% tab API-Triggered Delivery %}
Use [API-Triggered Delivery]({{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/api_triggered_delivery/) for more advanced transactional use cases.

{% endtab %}
{% endtabs %}

{% alert warning %}
Unless you check the box titled "Allow users to become re-eligible to receive campaign" under the __Schedule__ portion of the campaign wizard, each user will only receive the contents of a campaign once, and only new users that meet the criteria will receive the campaign on subsequent deliveries.
{% endalert %}

## Step 4: Target users

On the **Target Users** step of the campaign setup, choose the target audience for your campaign.

!\[Targeting Options\]\[25\]

Under the Targeting Options section, you'll find a few options for who you can send your campaign to:

1. __Members of a previously created segment.__ To do this, select one segment from the dropdown under **Target Users By Segment**. <br><br>
2. __Users that fall into multiple previously created segments.__ To do this, add multiple segments from the dropdown under **Target Users By Segment**. The resulting target audience will be users in the first segment *and* the second segment *and* the third segment, etc. <br><br>
3. __Users of one or more previously created segments that also fall under additional filters.__ After first selecting your segments, further refine your audience under the **Additional Filters** section. This is demonstrated in the screenshot below, which targets users that are in the 10 Unread Messages segment *and* are in the Active Users segment, *and* made a purchase less than 30 days ago. <br><br>
4. __Users that fall under a series of filters (and are not defined by pre-existing segments).__ This means you do not need to target a campaign at a pre-existing segment. Instead, make an ad hoc audience during campaign creation by only using the additional filters and not selecting any segments under **Target Users By Segment**. This will allow you to skip segment creation when sending campaigns to one-off audiences.

Detailed audience statistics for the channels targeted by your campaign are available in the footer. To see what percentage of your user base is being targeted and the Lifetime Value for this segment, click **Show Additional Stats**.

{% details Why does my Total Reachable Users metric look smaller than it should be? %}

When you click **Show Additional Stats** and view the Total Reachable Users for your filtered audience, you may notice that it's smaller than the sum of the other columns. This gap is usually because there are a number of users who qualify for the segment or filters in the campaign, but are not reachable through push (for example, because they don't have valid or active [push tokens]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/#push-tokens)).

{% enddetails %}

!\[Reachable Users Footer\]\[24\]

Keep in mind that exact segment membership is always calculated right before the message is sent.

### Multichannel campaigns with push and email

For multichannel campaigns targeting both push and email channels, you may want to limit your campaign so that only the users who are explicitly opted in will receive the message (excluding subscribed or unsubscribed users). For example, say you have three users of different opt-in status:

- **User A** is subscribed to email and is push enabled. This user doesn't receive the email but will receive the push.
- **User B** is opted-in to email but is not push enabled. This user will receive the email but doesn't receive the push.
- **User C** is opted-in to email and is push enabled. This user will receive both the email and the push.

To do so, under **Audience Summary**, select to send this campaign to "opted-in users only". This option will ensure that only opted-in users will receive your email, and Braze will only send your push to users who are push enabled by default.

{% alert important %}
With this configuration, don't include any filters in the **Target Users** step that limit the audience to a single channel (e.g., `Push Enabled = True` or `Email Subscription = Opted-In`).
{% endalert %}

## Step 5: Choose conversion events

Braze allows you to track whether users perform specific actions (Conversion Events) after receiving a campaign. You can specify any of the following actions as a "Conversion Event":

- Opens App
- Makes Purchase
  - This can be a generic purchase or a specific item
- Performs specific custom event

You have the option of allowing a conversion event within a time frame that is relevant for your campaign. The conversion window for a conversion event can range from 5 minutes to 30 days. The event will count as a conversion if it takes place during the specified time.

!\[Conversion Event\]\[15\]

## Step 6: Review and deploy {#review-and-deploy-push}

The final page will give you a summary of the campaign you've just designed. Clicking **Launch Campaign** will enable it to send. Confirm all the relevant details and watch the data roll in!

!\[Confirmation Page\]\[5\]

## Results data {#results-data-push}

Braze will show you the number of messages sent and opened over time for each push campaign you deploy, as shown below:

!\[Results\]\[6\]

For push notifications, you'll be able to view statistics for the number of messages sent, delivered, bounced, opened, and directly opened.
[1]: {% image_buster /assets/img_archive/new_campaign_push.png %} [2]: {% image_buster /assets/img_archive/push_1.png %} [3]: {% image_buster /assets/img_archive/push_2.png %} [4]: {% image_buster /assets/img_archive/schedule.png %} [5]: {% image_buster /assets/img_archive/confirmation_page.png %} [6]: {% image_buster /assets/img_archive/push-results-statistics.png %} [7]: {% image_buster /assets/img_archive/push_3.png %} [15]: {% image_buster /assets/img_archive/conversion_event_selection.png %} [24]: {% image_buster /assets/img_archive/multi_channel_footer.png %} [25]: {% image_buster /assets/img_archive/target_segmenter.png %}

[8]: https://www.braze.com/customers 
