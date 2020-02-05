---
nav_title: "Create a Push Primer Campaign"
page_order: 5
page_type: tutorial
description: "This walkthrough will show you how to get your users qualified and ready to receive your push messages."

channel:
  - Push
tool:
  - Docs
  - Dashboard
  - Campaigns
---

# Create a Push Primer Campaign

> This article will walk you through setting up and sending a Push Primer campaign to new or non-push enabled users. Push Primer campaigns encourage your users to enable push on their device for your app. Getting permission from users to send messages directly to their device can be complex, but our guides can help!

![push_primer_example_3][push_primer5]{: style="float:right;max-width:30%;margin-left:15px;"} 

Push Primer campaigns are useful because they address the issue of the dreaded iOS notification opt-in/opt-out prompt that users receive upon opening any new iOS application. These prompts are disruptive and uninformative, with users likely choosing to opt-out of push notifications. This prompt is only ever shown once, and unfortunately, once those notifications are turned off, there's very little we can do to get users to turn them back on. This becomes a problem when we want to use our Push Channel for marketing, but not many users are push enabled. 

To address this, Braze offers steps on how to set up Push Primers Campaigns. Push Primers allow you to hold off on delivering that initial disruptive push message as well as offer re-deliverability, letting you decide when and how you want to prompt your users for a push opt-in. These Push Primers should provide users valuable information on why notifications for your application are important.

For a user to qualify to receive your Push Messages, they must enable Push at the app-level _and_ the device-level. Please note that these levels translate differently for iOS and Android. You can learn more about them here:
- [Android Push Enabled]({{ site.baseurl }}/user_guide/message_building_by_channel/push/users_and_subscriptions/#ios-android-details)
- [iOS Push Enabled]({{ site.baseurl }}/user_guide/message_building_by_channel/push/users_and_subscriptions/#ios-android-details)

{% alert note %}
__Should I be using Push Primers?__ Depends on your iOS version.<br><br>
- __iOS 12__: With the iOS 12 update adding provisional authorization, allowing this initial push prompt to be delivered silently to your notification center, some may find Push Primers not needed, others may and choose to still use Push Primers. We recommend meeting with your Customer Success Manager to discuss if this is the right move.
- __iOS 11 and Later__: Because these iOS versions only allow foreground Push, the intrusive native iOS Push message prompt will still get sent, in turn sacrificing your marketability to those users. We strongly suggest setting up Push Primers for these versions. 
{% endalert %}

## Step 1: Push Primer Integrations

Push Primer Campaigns are not an out-of-the-box feature and should be viewed as a repurposed in-app messaging campaign. Unlike many of our out-of-the-box features that come ready to use, this essential tool does require some backend setup from your developers. We have included the code snippets required here: [Push Primer Integrations][integrations].

## Step 2: Select your Channel of Choice

From the Campaigns pane within the Dashboard, select In-App Messaging as the messaging channel under Create Campaign.

## Step 3: Set Up Initial Campaign Options

![push_primer_message_type][push_primer7]

Once you have a blank In-App Messaging campaign to work on, you must name your campaign, select where you would like your Push Primer campaign to send to, select the message type, and pick the layout type (text and image or image only). For your basic Push Primer campaign message type, we suggest either a full screen or modal message. 

## Step 4: Customize your Message

![push_primer][push_primer2]

After you have chosen the appropriate in-app message type, you can customize your message content and add buttons.

Here are some resources to get you started:
- Braze supports using [Font Awesome v4.3.0 icons](https://fontawesome.com/v4.7.0/cheatsheet/) for modal in-app message icons.
- [iOS Rich Push Notification Requirements][ioslink]
- [Android Rich Push Notification Requirements][androidlink]

Remember that a push primer is supposed to prime the user to turn on push notifications. <br>In your message body, we suggest __highlighting the reasons your users should have push notifications turned on__. 

Here are some example Push Primer Messages:

![push_primer_example_1][push_primer3]{: height="250px"} ![push_primer_example_2][push_primer4]{: height="250px"} ![push_primer_example_3][push_primer5]{: height="250px"}

If you would like even further customization options, you can also set the message type to Custom code, and provide the full HTML for your in-app message.

### Button Set-Up

To add buttons to your in-app message, you will find a Button1 textbox and Button2 textbox underneath the text body prompt. Here, you can choose the text that will show on these buttons. We recommend "Turn on Notifications" and "Not Now" as starter buttons, but there are many different button prompts you could assign. 

![push_primer][push_primer6]{: style="float:right;max-width:40%;margin-left:15px;"}

### On Click Behavior

After your push primer message has been set up, on-click behavior must be assigned. For the corresponding "Turn on Notifications" button, you must select "Deep Link Into App". 

Because Push Primer Campaigns are not an out-of-the-box feature, the deep-link link that prompts the native push prompt must be set up by your developers before it becomes available. 

Documentation for this can be found here: [Push Primer Integrations][integrations].

## Step 5: Selecting the Delivery Method

To set your Push Primer to trigger when you want it to, you must set __Perform Custom Event__ as the trigger action, choosing the custom event you want the push primer to trigger from. We suggest taking some time to pick a compelling trigger action, for example, after a user's second purchase.

## Step 6: Targeting Users

For Push Primer Campaigns, you must target all users. For users that have already opt-ed out of Push, these push primer campaign messages will not show.

## Step 7: Conversions
Do we want conversions? Is this relevant?

[deeplink]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/advanced_use_cases/linking/#deep-links
[integrations]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/push_primer/
[push_primer1]: {% image_buster /assets/img/push_primer/push_primer_1.jpg %}
[push_primer2]: {% image_buster /assets/img/push_primer/push_primer_2.jpg %}
[push_primer3]: {% image_buster /assets/img/push_primer/push_primer_3.png %}
[push_primer4]: {% image_buster /assets/img/push_primer/push_primer_4.png %}
[push_primer5]: {% image_buster /assets/img/push_primer/push_primer_5.png %}
[push_primer6]: {% image_buster /assets/img/push_primer/push_primer_6.jpg %}
[push_primer7]: {% image_buster /assets/img/push_primer/push_primer_7.jpg %}
[ioslink]: {{ site.baseurl }}/user_guide/message_building_by_channel/push/ios/rich_notifications/#requirements
[androidlink]: {{ site.baseurl }}/user_guide/message_building_by_channel/push/android/rich_notifications/#requirements
