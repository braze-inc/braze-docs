---
nav_title: Action-Based Delivery
page_order: 1

tools: campaigns
page_type: reference
description: "This reference article gives an overview of different ways to go about scheduling a campaign."
---

# Action-Based Delivery (Event Triggered Campaigns)

Instead of sending your campaign on certain days, you can trigger them to send after a user completes a certain event. Here are the steps for setting up an event-based schedule:

{% alert important %}
  Action-based delivery is not available for [Canvas steps with in-app messages]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/in-app_messages_in_canvas). Canvas steps with in-app messages must be scheduled.
{% endalert %}

## Setting Up a Triggered Campaign

### Step 1: Select a Trigger Event

Select a trigger event, which can be:
- Starting a session
- Purchasing an item
- Interacting with News Feed cards (see [Braze's Campaign Connector][33])
- Interacting with other campaigns
- Entering a location
- Completing any custom event
- Performing the campaign's primary conversion event
- Performing the exception event for another campaign
- Adding an email address to a user profile

You can also further filter trigger events through Braze's [Custom Event Properties][32] which allows for customizable event properties for both custom events and in-app purchases. This feature allows you to further tailor which users receive a message based on the specific attributes of the custom event, allowing for greater campaign personalization and more sophisticated data collection. For example, in the following screenshot, an Abandoned Cart custom event is further targeted by the "cart value" property filter. This campaign will only reach users who've left between $100 and $200 worth of goods in their carts. 

![Custom Event Properties Pic][34]

{% alert note %}
The trigger event "start session" can be the user's very first app open if your campaign's segment applies to new users (for instance, if your segment consists of those with no sessions).
{% endalert %}

Keep in mind that you can still send a triggered campaign to a specific segment of users, so users who aren't a part of the segment won't be able to receive the campaign even if they complete the trigger event. If you notice users not receiving the campaign even though they qualified for the segment, please read our section on [reasons why a user might not have received a triggered campaign][49].

With respect to the trigger event for when a user adds an email address to their profile, the following rules apply:

- The trigger event will be fired after the user profile attribute updates. This means that the evaluation of the campaign's segments and filters will happen after the attribute updates. This is beneficial because it enables you to do things like set up a filter of "email address matches gmail.com" to create a trigger campaign that only sends to Gmail users and fires as soon as they add their email address.
- The trigger event will fire when an email address is added to a user profile. If you have multiple user profiles that you create that have the same email address, the campaign may fire multiple times, once for each user profile.

In addition, triggered in-app messages still abide by in-app message delivery rules and will appear at the beginning of an app session.

![triggered 1][17]

### Step 2: Select Delay Length

Select how long to wait before sending the campaign, after the trigger criteria are met. Choose how long to delay your message after the user completes the trigger event.

{% alert important %}
In choosing your delay length, note that if you set a delay that is longer than the message's duration for sending (see Step 4), no users will receive your campaign.
{% endalert %}

Additionally, users who complete the trigger event after your campaign is launched will be the first to start receiving the message once the delay has passed. Users who have completed the trigger event prior to the campaign launching will not qualify to receive the campaign.

![triggered 2][19]

You may also elect to send the campaign on either a specific day of the week (by choosing "on the next" and then selecting a day) or a specific number of days (by selecting "in") in the future. Choose the time you wish the user to receive your message on that day. Alternatively, you may choose to send your message using the [Intelligent Timing][8] feature instead of manually selecting a delivery time.

![triggered 7][41]
![triggered 8][50]

### Step 3: Select Exception Events

Select an exception event that will disqualify users from receiving this campaign. You can only do this if your triggered message sends after a time delay. Exception events can be making a purchase, starting a session, performing one of a campaign's designated [conversion events][18], or performing a custom event. If a user completes the trigger event but then completes your exception event before the message sends due to the time delay, she will not receive the campaign. Users who do not receive the campaign due to the exception event will automatically be eligible to receive it in the future, the next time they complete the trigger event, even if you do not elect for users to become [re-eligible]({{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/reeligibility/).

You can read more about how to employ exception events in our section on [use cases]({{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/triggered_delivery/#use-cases).

![triggered 3][20]

> If you are sending out a campaign with the trigger event equalling the same exception event, the initial campaign will be canceled. Instead of sending out both campaigns, your user's first campaign will be canceled and we will automatically re-schedule a new campaign based on the exception event's message delivery time.
>
>For example, if your first trigger event starts at 5 minutes and the exception event's time starts at 10 minutes, you would rely on the exception event's 10 minutes as the official campaign's message delivery time).

{% alert note %}
You cannot make a "session start"  both the trigger event and exception event for a campaign (however, you always have the choice to select any other custom event outside of this option).
{% endalert %}

### Step 4: Assign Duration

Assign the campaign's duration by specifying a start time and optional end time. If a user completes a trigger event during the specified time frame, but actually qualifies for the message outside of the time frame due to a scheduled delay, then she will not receive the campaign. Therefore, if you set a time delay that is longer than the message's time frame, no users will receive your campaign. In addition, you can elect to send the message in users' [local time zones]({{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/scheduled_delivery/#local-time-zone-campaigns).

![triggered 4][21]

### Step 5: Select Time Frame

Select whether the user will receive the campaign during a specific portion of the day. If you give the message a time frame and the user either completes the trigger event outside the time frame or the message delay causes them to miss the time frame, then by default the user will not receive your message.

![triggered 5][27]

In the case where a user completes the trigger event within the time frame, but the message delay causes the user to fall out of the time frame, you can check the box below so that these users will still receive the campaign:

![triggered next available][31]

If a user doesn't receive the message because she misses the time frame, then she will still be qualified to get it the next time she completes the trigger event, even if you did not elect for users to become [re-eligible]({{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/reeligibility/). If you do elect for users to become re-eligible, then users can receive the campaign each time they complete the trigger event, assuming they qualify during the specified time frame.

If you have also assigned the campaign a certain duration, then in order to receive the message, a user must qualify within both the duration and the specific portion of the day.

### Step 6: Determine Re-Eligibility

Determine whether users can become [re-eligible][24] for the campaign. If you allow users to become re-eligible, you may specify a time delay before the user can receive the campaign again. This will prevent your triggered campaigns from becoming spammy.

![triggered 6][28]

## Use Cases

Triggered campaigns are very effective for transactional or achievement-based messages.

Transactional campaigns include messages sent after the user completes a purchase or adds an item to their cart. The latter case is a great example of a campaign that would benefit from an exception event. Say your campaign reminds users of items in their cart that they haven't purchased. The exception event, in this case, would be the user buying the products in their cart. For achievement-based campaigns, you can send a message 5 minutes after the user completes a conversion or beats a game level.

In addition, when creating welcome campaigns, you can trigger messages to send after the user registers or sets up an account. Staggering messages to be sent on different days following registration will allow you to create a thorough [onboarding process][30].

## Why Did a User Not Receive My Triggered Campaign?

Any of these things will prevent a user who has completed the trigger event from receiving the campaign:

- The user completed the exception event before the time delay had fully elapsed.
- The time delay caused the user to become qualified to receive the campaign after the duration has ended.
- The time delay caused the user to become qualified to receive the campaign outside of the specified portion of the day.
- The user has already received the campaign, and users do not become re-eligible.
- While users are re-eligible to receive the campaign, they can only re-trigger it after a certain period of time, and that period of time has not yet elapsed.

[Segmenting]({{site.baseurl}}/user_guide/engagement_tools/segments/) a triggered campaign on user data recorded at the time of the event may cause a _race condition_. This happens when a change in the user attribute on which the campaign is segmented hasn't yet been processed for the user at the time that segment membership is determined and the campaign is sent and can lead to the user not receiving the campaign.

For example, imagine you want to send an event-triggered campaign to male users who just registered. When the user registers, you record a custom event `registration`, and simultaneously set the user's `gender` attribute. The event may trigger the campaign before Braze has processed the user's gender, preventing them from receiving the campaign.

It is a best practice to make sure that the attribute on which the campaign is segmented is flushed to Braze's servers before the event. In cases where this is not possible, the best way to guarantee delivery is to use [Custom Event Properties][48] to attach the relevant user properties to the event and apply a property filter for the specific event property instead of a segmentation filter. In the example above, you would add a `gender` property to the custom event `registration` so that Braze is guaranteed to have the data you need at the time your campaign is triggered.

[5]: #local-time-zone-campaigns
[8]: {{site.baseurl}}/user_guide/intelligence/intelligent_timing/
[17]: {% image_buster /assets/img_archive/schedule_triggered1.png %}
[18]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/#conversion-events
[19]: {% image_buster /assets/img_archive/schedule_triggered22.png %}
[20]: {% image_buster /assets/img_archive/schedule_triggered32.png %}
[21]: {% image_buster /assets/img_archive/schedule_triggered43.png %}
[22]: #use-cases-2
[24]: {% image_buster /assets/img_archive/ReEligible.png %}
[27]: {% image_buster /assets/img_archive/schedule_triggered5.png %}
[28]: {% image_buster /assets/img_archive/schedule_triggered6.png %}
[29]: {{site.baseurl}}/help/best_practices/in-app_messages/in-app_message_behavior/#in-app-message-delivery-rules
[30]: {{site.baseurl}}/help/best_practices/user_onboarding/#user-onboarding
[31]: {% image_buster /assets/img_archive/schedule_triggered_next_available.png %}
[32]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/
[33]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/campaign_connector/#campaign-connector
[34]: {% image_buster /assets/img_archive/customEventProperties.png %}
[34]: {% image_buster /assets/img_archive/customEventProperties.png %}
[41]: {% image_buster /assets/img_archive/schedule_triggered7.png %}
[47]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/triggered_delivery/#why-did-a-user-not-receive-my-triggered-campaign
[48]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties
[49]: {{site.baseurl}}/help/help_articles/campaigns_and_canvas/not_triggering/
[50]: {% image_buster /assets/img_archive/schedule_triggered8.png %}