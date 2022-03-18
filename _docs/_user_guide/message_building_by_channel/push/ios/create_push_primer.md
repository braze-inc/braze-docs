---
nav_title: "Create a Push Primer Campaign"
article_title: Create a Push Primer Campaign
page_order: 5
page_type: tutorial
description: "This walkthrough will show you how to get your users qualified and ready to receive your push messages by sending out a push primer."
channel:
  - push
tool:
  - Campaigns

---

<br>
{% alert important %}
Push primer campaigns require backend set up from your developers. <br>Check out the necessary push primer integrations [here]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_primer/).
{% endalert %}


# Create a push primer campaign

> This article will walk you through setting up and sending a push primer campaign to new or non-push enabled users. Push primer campaigns encourage your users to enable push on their device for your app. Getting permission from users to send messages directly to their devices can be complex, but our guides can help!

![Push primer example that prompts users to enable push notifications to get alerts on future promotions. There are two buttons at the bottom of the prompt: No Thanks and Yes Please.][push_primer5]{: style="float:right;max-width:30%;margin-left:15px;"} 

Push primer campaigns are useful because they address the issue of the dreaded iOS notification opt-in prompt that users receive upon opening any new iOS application. These prompts are disruptive and uninformative, with users likely choosing to opt-out of push notifications. This prompt is only ever shown once, and unfortunately, once those notifications are turned off, there's very little we can do to get users to turn them back on. 

To address this, Braze offers steps on how to set up push primer campaigns. Push primers allow you to hold off on delivering that initial disruptive push message as well as offer re-deliverability, letting you decide when and how you want to prompt your users for a push opt-in. These push primers should provide users valuable information on why notifications for your application are important.

For a user to qualify to receive your push messages, they must enable push at the app-level and the device-level. Note that these levels translate differently for iOS and Android. You can learn more about them here:
- [Android push enabled]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/#ios-android-details)
- [iOS push enabled]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/#ios-android-details)

{% alert note %}
**Should I be using push primers?** Depends on your iOS version.<br><br>
- **iOS 12**: With the iOS 12 update offering [provisional authorization]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/#provisional-push-authentication--quiet-notifications), allowing this initial push prompt to be delivered silently to your notification center, some may find Push Primers no longer needed, while others may continue its use. We recognize not every iOS app will have its developers incorporate provisional authorization, so push primers are still a great approach for those applications. We recommend meeting with your Customer Success Manager to discuss if incorporating push primers are the right move.
- **iOS 11 and Later**: Because these iOS versions only allow foreground push, the intrusive native iOS push opt-in prompt will still get sent, in turn sacrificing your marketability to those users. we strongly suggest setting up push primers for these versions. 
{% endalert %}

## Step 1: Push primer integrations

We leverage in-app messages to drive push primer campaigns. Unlike many of our out-of-the-box features that come ready to use, this essential tool does require some backend setup from your developers. We have included the code snippets required here: [Push primer integrations][integrations].

## Step 2: Select your channel of choice

From the **Campaigns** pane within the dashboard, select **In-App Messaging** as the messaging channel under **Create Campaign**.

## Step 3: Set up initial campaign options

Once you have a blank in-app messaging campaign to work on, you must name your campaign, select where you would like your push primer to send to, select the message type, and pick the layout type. For your basic push primer campaign message type, we suggest either a full screen or modal message. Note that for a full-screen in-app message, an image is required.

![Push primer message type][push_primer7]

## Step 4: Customize your message

After you have chosen the appropriate in-app message type, you can customize your message content and add buttons in the **Compose** tab.

![][push_primer2]{: style="max-width:75%"}

Remember that a push primer is supposed to prime the user to turn on push notifications. In your message body, we suggest highlighting the reasons your users should have push notifications turned on. As an additional resource, Braze supports using [Font Awesome v4.3.0 icons](https://fontawesome.com/v4.7.0/cheatsheet/) for modal in-app message icons.

Refer to the following push primer messages that prompt users to enable their push notifications to receive future retail promotions.

![Push primer message for future promotions with two buttons: Not Now and Enable.][push_primer3]{: height="225px"} ![Push primer message for retail promotion with two buttons: Not Now and Enable.][push_primer4]{: height="225px"}

If you would like even further customization options, you can also set the message type to custom code and provide the full HTML for your in-app message.

### Button set-up

To add buttons to your in-app message, you will find a Button 1 textbox and Button 2 textbox underneath the text body prompt. Here, you can choose the text that will show on these buttons. We recommend "Turn on Notifications" and "Not Now" as starter buttons, but there are many different button prompts you could assign. 

![][push_primer6]{: style="float:right;max-width:40%;margin-left:15px;"}

### On-click behavior

After your push primer message has been set up, on-click behavior must be assigned. For the corresponding "Turn on Notifications" button you had assigned, you must select **Deep Link Into App**. 

#### Deep linking

Because push primer campaigns are not an out-of-the-box feature, the deep-link link that prompts the native push prompt must be set up by your developers before it becomes available. 

For more information on push primer integrations and deep linking customization, refer to [iOS push primer integration][integrations].

## Step 5: Selecting the delivery method

To set your push primer to trigger when you want it to, you must set **Perform Custom Event** as the trigger action. Your developers will set up a custom event that you can choose to trigger off of for your push primer campaign. To figure out how your company references this custom event, check with your developers. This custom event counts as one data point toward your allotment. This customer event will check if a user has already been provided a native push prompt, and if not, it will trigger the push primer in-app message. 

## Step 6: Targeting users

Generally, for push primer campaigns, we want the push primer to trigger off of a certain segment of users. In these Targeting Users options, you can decide what segment you feel most appropriate. We suggest taking some time with your marketing team to pick a compelling segment. For example, users that have completed a second purchase, users that have just made an account to become a member, or even users that visit your app more than twice a week. Targeting users for these crucial segments increases the likelihood of users opting in and becoming push enabled.

If you are not sure the best way to segment, you may also select **All Users**. This option will send your push primer to any iOS device that has not yet opted in or out of push. 

## Step 7: Conversions
Braze suggests default settings for conversions, but you may want to set up conversion events surrounding push primers.

[integrations]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_primer/
[push_primer2]: {% image_buster /assets/img/push_primer/push_primer_2.png %}
[push_primer3]: {% image_buster /assets/img/push_primer/push_primer_3.png %}
[push_primer4]: {% image_buster /assets/img/push_primer/push_primer_4.png %}
[push_primer5]: {% image_buster /assets/img/push_primer/push_primer_5.png %}
[push_primer6]: {% image_buster /assets/img/push_primer/push_primer_6.jpg %}
[push_primer7]: {% image_buster /assets/img/push_primer/push_primer_7.png %}
