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

{% alert important %}
Push Primer campaigns require backend set up from your developers. <br>Check out the necessary Push Primer Integrations [here]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_primer/).
{% endalert %}


# Create a Push Primer Campaign

> This article will walk you through setting up and sending a Push Primer campaign to new or non-push enabled users. Push Primer campaigns encourage your users to enable push on their device for your app. Getting permission from users to send messages directly to their devices can be complex, but our guides can help!

![push_primer_example_3][push_primer5]{: style="float:right;max-width:30%;margin-left:15px;"} 

Push Primer campaigns are useful because they address the issue of the dreaded iOS notification opt-in prompt that users receive upon opening any new iOS application. These prompts are disruptive and uninformative, with users likely choosing to opt-out of push notifications. This prompt is only ever shown once, and unfortunately, once those notifications are turned off, there's very little we can do to get users to turn them back on. 

To address this, Braze offers steps on how to set up Push Primer campaigns. Push Primers allow you to hold off on delivering that initial disruptive push message as well as offer re-deliverability, letting you decide when and how you want to prompt your users for a push opt-in. These Push Primers should provide users valuable information on why notifications for your application are important.

For a user to qualify to receive your Push Messages, they must enable push at the app-level _and_ the device-level. Please note that these levels translate differently for iOS and Android. You can learn more about them here:
- [Android Push Enabled]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/#ios-android-details)
- [iOS Push Enabled]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/#ios-android-details)

{% alert note %}
__Should I be using Push Primers?__ Depends on your iOS version.<br><br>
- __iOS 12__: With the iOS 12 update offering [provisional authorization]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/#provisional-push-authentication--quiet-notifications), allowing this initial push prompt to be delivered silently to your notification center, some may find Push Primers no longer needed, while others may continue its use. We recognize not every iOS app will have its developers incorporate provisional authorization, so push primers are still a great approach for those applications. We recommend meeting with your Customer Success Manager to discuss if incorporating push primers are the right move.
- __iOS 11 and Later__: Because these iOS versions only allow foreground Push, the intrusive native iOS Push opt-in prompt will still get sent, in turn sacrificing your marketability to those users. We strongly suggest setting up Push Primers for these versions. 
{% endalert %}

## Step 1: Push Primer Integrations

We leverage in-app messages to drive Push Primer campaigns. Unlike many of our out-of-the-box features that come ready to use, this essential tool does require some backend setup from your developers. We have included the code snippets required here: [Push Primer Integrations][integrations].

## Step 2: Select your Channel of Choice

From the **Campaigns** pane within the Dashboard, select **In-App Messaging** as the messaging channel under **Create Campaign**.

## Step 3: Set Up Initial Campaign Options

![push_primer_message_type][push_primer7]

Once you have a blank in-app messaging campaign to work on, you must name your campaign, select where you would like your Push Primer to send to, select the message type, and pick the layout type. For your basic Push Primer campaign message type, we suggest either a full screen or modal message. Note that for a full-screen in-app message, an image is required.

## Step 4: Customize your Message

![push_primer][push_primer2]

After you have chosen the appropriate in-app message type, you can customize your message content and add buttons.

Here are some resources to get you started:
- Braze supports using [Font Awesome v4.3.0 icons](https://fontawesome.com/v4.7.0/cheatsheet/) for modal in-app message icons.

Remember that a push primer is supposed to prime the user to turn on push notifications. <br>In your message body, we suggest __highlighting the reasons your users should have push notifications turned on__. 

Here are some example Push Primer Messages:

![push_primer_example_1][push_primer3]{: height="225px"} ![push_primer_example_2][push_primer4]{: height="225px"} ![push_primer_example_3][push_primer5]{: height="225px"}

If you would like even further customization options, you can also set the message type to Custom code and provide the full HTML for your in-app message.

### Button Set-Up

To add buttons to your in-app message, you will find a Button 1 textbox and Button 2 textbox underneath the text body prompt. Here, you can choose the text that will show on these buttons. We recommend "Turn on Notifications" and "Not Now" as starter buttons, but there are many different button prompts you could assign. 

![push_primer][push_primer6]{: style="float:right;max-width:40%;margin-left:15px;"}

### On Click Behavior

After your push primer message has been set up, on-click behavior must be assigned. For the corresponding "Turn on Notifications" button you had assigned, you must select "Deep Link Into App". 

#### Deep Linking

Because Push Primer campaigns are not an out-of-the-box feature, the deep-link link that prompts the native push prompt must be set up by your developers before it becomes available. 

Documentation on push primer integrations and deep linking customization can be found [here][integrations].

## Step 5: Selecting the Delivery Method

To set your Push Primer to trigger when you want it to, you must set __Perform Custom Event__ as the trigger action. Your developers will set up a custom event that you can choose to trigger off of for your Push Primer campaign. To figure out how your company references this custom event, check with your developers. __This custom event counts as one data point toward your allotment.__ This customer event will check if a user has already been provided a native push prompt, and if not, it will trigger the push primer in-app message. 

## Step 6: Targeting Users

Generally, for Push Primer campaigns, we want the push primer to trigger off of a certain segment of users. In these Targeting Users Options, you can decide what segment you feel most appropriate. We suggest taking some time with your marketing team to pick a compelling segment. For example, users that have completed a second purchase, users that have just made an account to become a member, or even users that visit your app more than twice a week. Targeting users for these crucial segments increases the likelihood of users opting in and becoming push enabled.

If you are not sure the best way to segment, you may also select All Users. This option will send your push primer to any iOS device that has not yet opted in or out of push. 

## Step 7: Conversions
Braze suggests default settings for conversions, but you may want to set up conversion events surrounding push primers.

[integrations]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_primer/
[push_primer2]: {% image_buster /assets/img/push_primer/push_primer_2.jpg %}
[push_primer3]: {% image_buster /assets/img/push_primer/push_primer_3.png %}
[push_primer4]: {% image_buster /assets/img/push_primer/push_primer_4.png %}
[push_primer5]: {% image_buster /assets/img/push_primer/push_primer_5.png %}
[push_primer6]: {% image_buster /assets/img/push_primer/push_primer_6.jpg %}
[push_primer7]: {% image_buster /assets/img/push_primer/push_primer_7.jpg %}
