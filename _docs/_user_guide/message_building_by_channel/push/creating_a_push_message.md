---
nav_title: Creating a Push Message
platform: Message_Building_and_Personalization
subplatform: Push
page_order: 1
---
# Creating a Push Message

Push notifications are wonderful for time-sensitive calls to action, as well as re-engaging users who haven't come into the app in a while.

Successful Push Campaigns are going to drive the user directly to content or demonstrate the value of your app.

_Please note that your push messages must fall within the guidelines of the Apple App Store and Google's Play Store policies, specifically regarding using push messages as advertisements, spam, promotions, and more._

|Apple App Store Policies|
|---|
|[4.5.4][9] Push Notifications must not be required for the app to function, and should not be used for advertising, promotions, or direct marketing purposes or to send sensitive personal or confidential information.|
|[3.2.2][10] (i) Creating an interface for displaying third party apps, extensions, or plug-ins similar to the App Store or as a general-interest collection. (ii) Monetizing built-in capabilities provided by the hardware or operating system, such as Push Notifications, the camera, or the gyroscope; or Apple services, such as Apple Music access or iCloud storage.|

|Google Play Store Policy|
|---|
|[We don’t allow apps or ads that mimic or interfere with system functionality, such as notifications or warnings.][11] System level notifications may only be used for an app’s integral features, such as an airline app that notifies users of special deals, or a game that notifies users of in-game promotions.|




_To see examples of push notifications, check out our [Client Integration Gallery][8]._

## Step 1: Create a New Campaign {#create-new-campaign-push}

From the Messaging Page, click "Create Campaign."

![newcampaign][1]

## Step 2: Name Your Campaign, Choose Messaging Types, and Compose your Message

Next, you need to name your campaign and select the messaging types that will be included in the campaign. You select the platform(s) you're sending a Push message to by clicking on the toggle buttons on the right hand side.

![Push2][2]

Time to write your push message! Type it into the box and watch a preview appear on the device in the box.

### iOS Notification Options

With the release of Apple's iOS 12, Braze offers support for several of its features, including [Notification Groups](#notification-groups), [Quiet Notifications/Provisional Authorization](#provisional-authentication-quiet-notifications), and [Critical Alerts](#critical-alerts).

#### Notification Groups

If you want to categorize your messages and group them in your user's notification tray, you can utilize iOS's Notification Groups feature through Braze.

Create your iOS Push Campaign, then look to the top of the composer. There, you'll see a dropdown labeled Notification Groups.

![notificationgroupsdropdown][26]

From there, you can select any Notification Groups. If your notification group settings malfunction or you select __None__ from the dropdown, the message will automatically send as normal to all defined users in the app group.

If you don't have any Notification Groups listed here, you can add one using the iOS Thread ID. You will need one iOS Thread ID for every Notification Group you want to add. Then, add it to your Notification Groups by clicking __Manage Notification Groups__ in the dropdown and filling out the required fields in the __Manage iOS Push Notification Groups__ window that appears.

![managenotgroups][27]

##### Summary Arguments and Categories

__Summary Arguments__

In addition to grouping notifications by Thread IDs, Apple allows you to edit the summaries that appear when notifications are grouped. Braze Users can specify the summary category, summary count, and summary argument when composing a push campaign using our tool.

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

Once this is set up on your app, use the summary category by checking the __Notification Buttons__ box, and selecting __Enter Pre-registered iOS Category__.

Then, input the summary category identifier that you set in your app.

##### Provisional Authentication/Quiet Notifications

Apple allows brands the option to send quiet pushes to their users' Notification Centers before they officially opt in, giving you a chance to demonstrate the value of your messages early.

 Braze allows you to register for Provisional Authentication by updating your code in your _token registration snippet_ within your Braze iOS SDK implementation using the snippets below as an example (send these to your developers):

 __Swift__

  ```
  let notificationCenter = UNUserNotificationCenter.current()
  notificationCenter.requestAuthorization(options: [.alert, .badge, .sound, .provisional]) { ... }
  ```

__Objective-C__

```
	UNUserNotificationCenter *center = [UNUserNotificationCenter currentNotificationCenter];
 	UNAuthorizationOptions options = UNAuthorizationOptionAlert | UNAuthorizationOptionSound | UNAuthorizationOptionBadge | UNAuthorizationOptionProvisional;
```

 You will also be able to segment your users based on whether they are provisionally authorized or not.

 {% alert important %}
   If you utilize additional push prompts, please reach out to your account manager for additional guidance.
{% endalert %}

##### Critical Alerts
Apple will allow some brands to send notification that are considered extremely important, will ignore Do Not Disturb settings, and will always play a sound no matter the setting on a user's device.

Brands [must be approved by Apple](https://developer.apple.com/contact/request/notifications-critical-alerts-entitlement/) to use Critical Alerts. Good candidates for this feature could be apps with medical and other health-related information, home security, and public safety features. You must do this before using the feature in Braze.

_Users will still be able to turn off Critical Alerts on a per-app basis, separately from other notifications._

Braze will give you the ability to select __Send Critical Alert__ under __Alert Options__ in the iOS Push Composer, which will then allow you to specify the notification as a Critical Alert.

> Please note that this feature is still in beta. Additionally, if you attempt to use this feature without pre-approval by Apple, your message will not be allowed to send. Contact your account manager before attempting to use this feature.


### Android Notification Options

If you want to categorize your messages and group them in your user's notification tray, you can utilize Androids's Notification Channels feature through Braze.

Create your Android Push Campaign, then look to the top of the composer. There, you'll see a dropdown labeled Notification Channels.

![notificationchanneldropdown][28]

From there, you can select any Notification Channels. You must select a Fallback channel in the event that your notification channel settings malfunction.

If you don't have any Notification Channels listed here, you can add one using the Notification Channel ID. Contact your developers to identify what your Notification Channel IDs are or to create new IDs as needed. Then, add it to your Notification Channels by clicking __Manage Notification Channel__ in the dropdown and filling out the required fields in the __Manage Android Push Notification Channels__ window that appears. Notification Channels must be defined on the app before they may be used in the Braze platform.

![managenotchannel][29]

## Step 3: Schedule Your Messaging Campaign {#schedule-push-campaign}

![Schedule][3]

Message scheduling features include:

- Schedule messages to send immediately, at a specific time, using "Intelligent Delivery".
- __Intelligent Delivery__: Braze allows you to define a window during which you would like a user to receive a notification and Braze will send it to each individual user at the time we determine they are most likely to engage. We make this calculation based upon a statistical analysis of the user's past interactions with the app.

![Optimized Push Scheduling][7]

- Automatically schedule campaigns to send at a certain time with respect to the local time of each of your users.
- Messages can also be configured to recur on a daily, weekly (optionally on specific days), or monthly basis.

{% alert warning %}
Unless you check the box titled "Allow users to become re-eligible to receive campaign" under the __Schedule__ portion of the campaign wizard, each user will only receive the contents of a campaign once, and only new users that meet the criteria will receive the campaign on subsequent deliveries.
{% endalert %}

## Step 4: Target Users

On the “Target Users” step of campaign setup, you can choose the target audience for your campaign.  Braze now provides all the detailed audience statistics on the footer.  The footer will provide only the channels that are targeted by the campaign.  Additionally you will be able to see a breakdown of the ‘Push’ messages as Braze will provide details on how many will receive a Web Push versus an Android Push. In order to see what percentage of your userbase is being targeted or the LTV for this segment, simply click the “Show Additional Stats” located below the stats footer.

Keep in mind that exact segment membership is always calculated just before the message is sent.

![Multi-Channel Footer][24]

Under the Targeting Options section, you'll find a few options for who you can send your campaign to:

1. __Members of a previously created segment.__ To do this, simply select one segment from the dropdown under "Target Users By Segment."

2. __Users that fall into multiple previously created segments.__ To do this, add multiple segments from the dropdown under "Target Users By Segment." The resulting target audience will be users that are in the first segment *and* the second segment *and* the third segment, etc.

3. __Users of one or more previously created segments that also fall under additional filters.__ After first selecting your segment(s), you can further refine your audience under the "Additional Filters" section. This is demonstrated in the screenshot below, which targets users that are in the 10 Unread Messages segment *and* are in the Active Users segment *and* have made a purchase less than 30 days ago.

4. __Users that fall under a series of filters (and are not defined by pre-existing segments).__ This means you do not need to target a campaign at a pre-existing segment - you can make an ad hoc audience during campaign creation by just using the additional filters, and not selecting any segments under "Target Users By Segment. This will allow you to skip segment creation when sending campaigns to one-off audiences.

![Segmenter][25]

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

Braze will show you the number of messages sent and opened over time for each push campaign you deploy as shown below:

![Results][6]

For push notifications, you'll be able to view statistics for the number of messages sent, delivered, bounced, opened and directly opened.

[1]: {% image_buster /assets/img_archive/newcampaign.png %}
[2]: {% image_buster /assets/img_archive/push2.png %}
[3]: {% image_buster /assets/img_archive/schedule.png %}
[5]: {% image_buster /assets/img_archive/confirmation_page.png %}
[6]: {% image_buster /assets/img_archive/push-results-statistics.png %}
[7]: {% image_buster /assets/img_archive/intelligent_delivery.png %}
[8]: {{ site.baseurl }}/help/best_practices/client_integration_gallery/#client-integration-push
[9]: https://developer.apple.com/app-store/review/guidelines/#apple-sites-and-services
[10]: https://developer.apple.com/app-store/review/guidelines/#unacceptable
[11]: https://play.google.com/about/privacy-security-deception/deceptive-behavior/unauthorized-system-functionality/
[15]: {% image_buster /assets/img_archive/conversion_event_selection.png %}
[24]: {% image_buster /assets/img_archive/multi_channel_footer.png %}
[25]: {% image_buster /assets/img_archive/target_segmenter.png %}
[26]: {% image_buster /assets/img_archive/notgroupclickdropdown.gif %}
[27]: {% image_buster /assets/img_archive/managenotgroups.png %}
[28]: {% image_buster /assets/img_archive/notchannclickdropdown.gif %}
[29]: {% image_buster /assets/img_archive/notchannels.png %}
