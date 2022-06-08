---
nav_title: Push Primer In-App Messages
article_title: Push Primer In-App Messages
page_order: 8
page_type: reference
description: "Optimize your push opt-in rate using a Push Primer In-App Message"
channel: push

---

# Push primer in-app messages

![Push primer in-app message for streaming app. The notification reads "Get push notifications from Movie Cannon? Notifications may include new movies, TV shows, or other notices and can be turned off at any time."][1]{: style="float:right;max-width:40%;margin-left:15px;border:none;"}

You only get one chance to ask users for push permission, so optimizing your push registration is crucial to maximize the reach of your push messages.

To help achieve this, you can use in-app messages to explain what type of messages your users can expect to receive if they choose to opt in, before showing them the native push prompt. This is referred to as a push primer.

To create a push primer in-app message in Braze, you can use the button on-click behavior "Request Push Permission" when creating an in-app message for iOS or Web.

## Prerequisites

This guide uses a button [on-click behavior](#button-actions) that is only supported on newer SDK versions:

{% sdk_min_versions ios:5.1.0 android:20.1.0 web:4.0.3 %}

## Step 1: Create an in-app message

[Create an in-app message][2] as you usually would. You can choose to send to mobile apps, web browsers, or both, however the button on-click behavior to request push permissions is only available for iOS and Web. 

Next, select a message type and layout. To give you enough space to explain what push notifications your users can expect (and to allow for buttons), Braze suggests either a full screen or modal message. Note that for a full-screen in-app message, an image is required. 

## Step 2: Build your message

Now it's time to add your copy! Remember that a push primer is supposed to prime the user to turn on push notifications. In your message body, we suggest highlighting the reasons your users should have push notifications turned on. Be specific about what type of notifications you want to send and what value they can provide.

For example, a news app might use the following push primer:

> Breaking news on the go! Enable push notifications to get alerts for major stories and topics that matter to you.

While a streaming app might use the following:

> Get push notifications from Movie Cannon? Notifications may include new movies, TV shows, or other notices and can be turned off at any time.

For best practices and additional resources, refer to [Creating custom opt-in prompts][3].

## Step 3: Specify button behavior {#button-actions}

To add buttons to your in-app message, add text to the **Button 1** and **Button 2** text fields, which are the secondary and primary buttons in your in-app message respectively. We recommend “Allow notifications” and “Not now” as starter buttons, but there are many different button prompts you could assign.

After you've added button copy, specify the on-click behavior for each button:

- **Button 1:** Set this to "Close Message". This is your secondary button, or the "Not now" option.
- **Button 2:** Set this to "Request Push Permission". This is your primary button, or the "Allow notifications" option.

![][4]

## Step 4: Schedule delivery

To set your push primer to send at a relevant time, you must schedule your in-app message as an action-based message with **Perform Custom Event** as the trigger action.

While the ideal time will vary, Braze suggests waiting until a user completes some sort of [high-value action](https://www.braze.com/resources/videos/mapping-high-value-actions), indicating that they're starting to see value in your app or site, or when there's a compelling need that push notifications can address (such as after they've placed an order and you want to offer them shipping tracking information). This way, the prompt is beneficial to the customer rather than only to your brand.

![][5]

## Step 5: Target users

Since the goal of a push primer campaign is to prompt users to opt in to push messaging, you don't want to target users who are already opted in. To do so, add a segment or filter where `Push Subscription Status is not Opted In`.

Beyond that, you can decide what additional segments you feel are most appropriate. For example, you might target users that have completed a second purchase, users that have just made an account to become a member, or even users that visit your app more than twice a week. Targeting users for these crucial segments increases the likelihood of users opting in and becoming push enabled.

## Step 6: Conversion events

Braze suggests default settings for conversions, but you may want to set up [conversion events]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/) surrounding push primers.

[1]: {% image_buster /assets/img_archive/push_primer_iam.png %}
[2]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/
[3]: {{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/creating_custom_opt-in_prompts/
[4]: {% image_buster /assets/img_archive/push_primer_button_behavior.png %}
[5]: {% image_buster /assets/img_archive/push_primer_trigger.png %}
