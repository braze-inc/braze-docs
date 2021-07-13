---
nav_title: "Creating a Push Message"
page_order: 4
page_type: tutorial
description: "This tutorial page covers the different components involved in creating a Push Message, including configuration, sending, targeting, and more."

channel: push
tool:
  - Dashboard
  - Campaigns
---

# Creating a Push Message

> Push notifications are wonderful for time-sensitive calls to action, as well as re-engaging users who haven't come into the app in a while. <br><br> Successful push campaigns drive the user directly to content and demonstrate the value of your app.

_To see examples of push notifications, check out our [Case Studies][8]._

## Step 1: Create a New Push Campaign {#create-new-campaign-push}

Click __Create Campaign__ in the top right corner of the __Campaigns__ page. <br><br>From there, select __Push Notification__ within Single Channel Options or __Multichannel Campaign__ if you want to include multiple channels in addition to Push. 

![newcampaign][1]

## Step 2a: Name Your Campaign, Choose Messaging Types, and Compose your Message

Next, you need to name your campaign and select the messaging types and notification style (rich ([iOS]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/) and [Android]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/rich_notifications/)) or standard) that will be included in the campaign. You select the platform(s) you're sending a push message to by clicking on the toggle buttons on the right-hand side.

![Push2][2]

Time to write your push message! Type it into the message box and watch a preview appear in the preview box to the left. Don't forget to use Liquid tools when writing your push messages to make them personalized and targeted.

### Additional Push Customization Steps

#### Languages

You also can Add Languages through the __Add Languages__ button. Braze offers the option to "Internationalize" your message by inserting the Liquid into your message to help set custom messages and fields in specific languages based on a user's language preferences. 

#### OnClick Behavior

Braze allows you to specify what happens when a user clicks the body of a push notification. Whether you want to do something as simple as open the application or redirect to a specified URL, we have many different ways to customize our push notifications, and therefore the user experience. Here, you can also find the option to set up button prompts within your push notification, for example: yes/no prompt, confirm/cancel, more button, etc. 

For more information on platform specific Notification Options, please see our [iOS Notification and Provisional Push documentation]({{site.baseurl}}/user_guide/message_building_by_channel/push/notification_options_ios/) or [Android Notification Options documentation]({{site.baseurl}}/user_guide/message_building_by_channel/push/notification_options_android/).

### Step 2b: Preview and Test Your Message

Arguably one of the most critical steps, testing! After you finish composing your perfect push message, you should test it before sending it out! Navigate to the test page by clicking the "Test" button denoted by the eye symbol. Use **Preview Message as User** to get a sense of how your message may view on mobile. Use **Send Test** to ensure that your message displays properly.

## Step 3: Schedule Your Push Messaging Campaign {#schedule-push-campaign}

![Schedule][3]

{% tabs %}
  {% tab Scheduled Delivery %}
Scheduled Delivery allows you to specify the time you want the message to send, either immediately or at a future time (you can also consider local time in your scheduling). You can also use Intelligent Timing to send the message when the user is most likely to engage. Braze makes this calculation based on a statistical analysis of the user's interactions with your app.

Messages can also be configured to recur on a daily, weekly (optionally on specific days), or monthly basis.

> __Intelligent Timing__: Braze allows you to define a window during which you would like a user to receive a notification, and Braze will send it to each individual user at the time we determine they are most likely to engage. We make this calculation based upon a statistical analysis of the user's past interactions with the app.

{% endtab %}
{% tab Action-Based Delivery %}

Action-Based Delivery allows you to specify the time a message will send after a user takes a particular action you are able to use [custom events]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-events) as a trigger action. (selected from the __New Trigger Action__ dropdown.)

![Action]({% image_buster /assets/img_archive/action_delivery_new.png %}){: height="80%"" width="80%"}

{% endtab %}
{% tab API-Triggered Delivery %}
Check out our [API-Triggered section of the Developer Guide]({{site.baseurl}}/developer_guide/rest_api/messaging/#sending-messages-via-api-triggered-delivery) for more on API-Triggered Delivery.

![API]({% image_buster /assets/img_archive/api_delivered_new.png %}){: height="80%"" width="80%"}
  {% endtab %}
{% endtabs %}

{% alert warning %}
Unless you check the box titled "Allow users to become re-eligible to receive campaign" under the __Schedule__ portion of the campaign wizard, each user will only receive the contents of a campaign once, and only new users that meet the criteria will receive the campaign on subsequent deliveries.
{% endalert %}

## Step 4: Target Users

On the "Target Users" step of the campaign setup, you can choose the target audience for your campaign.  Braze now provides all the detailed audience statistics on the footer.  The footer will provide only the channels that are targeted by the campaign.  Additionally, you will be able to see a breakdown of the 'Push' messages as Braze will provide details on how many will receive a Web Push versus an Android Push. In order to see what percentage of your user base is being targeted or the Lifetime Value for this segment, click the "Show Additional Stats" located below the stats footer.

Keep in mind that exact segment membership is always calculated just before the message is sent.

![Multi-Channel Footer][25]

Under the Targeting Options section, you'll find a few options for who you can send your campaign to:

1. __Members of a previously created segment.__ To do this, select one segment from the dropdown under "Target Users By Segment."
<br><br>
2. __Users that fall into multiple previously created segments.__ To do this, add multiple segments from the dropdown under "Target Users By Segment." The resulting target audience will be users in the first segment *and* the second segment *and* the third segment, etc.
<br><br>
3. __Users of one or more previously created segments that also fall under additional filters.__ After first selecting your segment(s), you can further refine your audience under the "Additional Filters" section. This is demonstrated in the screenshot below, which targets users that are in the 10 Unread Messages segment *and* are in the Active Users segment *, and* made a purchase less than 30 days ago.
<br><br>
4. __Users that fall under a series of filters (and are not defined by pre-existing segments).__ This means you do not need to target a campaign at a pre-existing segment - you can make an ad hoc audience during campaign creation by just using the additional filters, and not selecting any segments under "Target Users By Segment. This will allow you to skip segment creation when sending campaigns to one-off audiences.

![Segmenter][24]

Above the Audience Statistics chart, there will be an Audience Summary that spells out which users you're targeting.

## Step 5: Choose Conversion Events

Braze allows you to track whether users perform specific actions (Conversion Events) after receiving a campaign. You can specify any of the following actions as a "Conversion Event":

- Opens App
- Makes Purchase
  - This can be a generic purchase or a specific item
- Performs specific custom event

You have the option of allowing a conversion event within a time frame that is relevant for your campaign. The conversion window for a conversion event can range from 5 minutes to 30 days. The event will count as a conversion if it takes place during the specified time.

![Conversion Event][15]

## Step 6: Review and Deploy {#review-and-deploy-push}

The final page will give you a summary of the campaign you've just designed. Clicking "Launch Campaign" will enable it to send. Confirm all the relevant details and watch the data roll in!

![Confirmation Page][5]

## Results Data {#results-data-push}

Braze will show you the number of messages sent and opened over time for each push campaign you deploy, as shown below:

![Results][6]

For push notifications, you'll be able to view statistics for the number of messages sent, delivered, bounced, opened, and directly opened.

[1]: {% image_buster /assets/img_archive/newcampaign_new.png %}
[2]: {% image_buster /assets/img_archive/push2.png %}
[3]: {% image_buster /assets/img_archive/schedule.png %}
[5]: {% image_buster /assets/img_archive/confirmation_page.png %}
[6]: {% image_buster /assets/img_archive/push-results-statistics.png %}
[8]: https://www.braze.com/customers
[15]: {% image_buster /assets/img_archive/conversion_event_selection.png %}
[24]: {% image_buster /assets/img_archive/multi_channel_footer.png %}
[25]: {% image_buster /assets/img_archive/target_segmenter.png %}
