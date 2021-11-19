---
nav_title: Action-Based Delivery
article_title: Action-Based Delivery
page_order: 1
page_type: reference
description: "This reference article describes how to trigger campaigns to send after a user completes a certain event."
tool: Campaigns

---

# Action-based delivery

Action-based delivery campaigns or event-triggered campaigns are very effective for transactional or achievement-based messages. Instead of sending your campaign on certain days, you can trigger them to send after a user completes a certain event. Listed below are the steps for setting up an event-based schedule:

{% alert important %}
Action-based delivery is not available for [Canvas steps with in-app messages]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/in-app_messages_in_canvas). These steps must be scheduled.
{% endalert %}

## Setting up a triggered campaign

### Step 1: Select a trigger event

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

You can also further filter trigger events through Braze's [custom event properties][32], allowing for customizable event properties for custom events and in-app purchases. This feature allows you to further tailor which users receive a message based on the specific attributes of the custom event, allowing for greater campaign personalization and more sophisticated data collection. For example, in the following screenshot, an abandoned cart custom event is further targeted by the "cart value" property filter. This campaign will only reach users who've left between $100 and $200 worth of goods in their carts. 

![Custom Event Properties][34]

{% alert note %}
The trigger event "start session" can be the user's very first app open if your campaign's segment applies to new users (for instance, if your segment consists of those with no sessions).
{% endalert %}

Keep in mind that you can still send a triggered campaign to a specific segment of users, so users who aren't a part of the segment won't receive the campaign even if they complete the trigger event. If you notice users not receiving the campaign even though they qualified for the segment, please read our section on [reasons why a user might not have received a triggered campaign][49].

With respect to the trigger event for when a user adds an email address to their profile, the following rules apply:

- The trigger event will be fired after the user profile attribute updates. This means that the evaluation of the campaign's segments and filters will happen after any attribute updates. This is beneficial because it enables you to set up filters like "email address matches gmail.com" to create a trigger campaign that only sends to Gmail users and fires as soon as they add their email address.
- The trigger event will fire when an email address is added to a user profile. If you have multiple user profiles that you create with the same email address, the campaign may fire multiple times, once for each user profile.

In addition, triggered in-app messages still abide by in-app message delivery rules and appear at the beginning of an app session.

![Select Trigger][17]

### Step 2: Select delay length

Select how long to wait before sending the campaign after the trigger criteria are met. If the delay length chosen is longer than the message's duration for sending, no users will receive the campaign. 

Additionally, users who complete the trigger event after your campaign is launched will be the first to start receiving the message once the delay has passed. Users who have completed the trigger event before the campaign launches will not qualify to receive the campaign.

![Select Delay][19]

You may also elect to send the campaign on either a specific day of the week (by choosing "on the next" and then selecting a day) or a specific number of days (by selecting "in") in the future. Alternatively, you may choose to send your message using the [Intelligent Timing][8] feature instead of manually selecting a delivery time.

![Schedule Delay Intelligent Timing][41]
![Schedule Delay][50]

### Step 3: Select exception events

Select an exception event that will disqualify users from receiving this campaign. You can only do this if your triggered message sends after a time delay. Exception events can be making a purchase, starting a session, performing one of a campaign's designated [conversion events][18], or performing a custom event. If a user completes the trigger event but then completes your exception event before the message sends due to the time delay, they will not receive the campaign. Users who do not receive the campaign due to the exception event will automatically be eligible to receive it in the future, the next time they complete the trigger event, even if you do not elect for users to become [re-eligible]({{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/reeligibility/).

You can read more about how to employ exception events in our section on [use cases]({{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/triggered_delivery/#use-cases).

![Schedule Delay Exception][20]

> If you send out a campaign with the trigger event that matches the exception event, the initial campaign will be canceled. Instead of sending out both campaigns, your user's first campaign will be canceled and Braze will automatically re-schedule a new campaign based on the exception event's message delivery time.<br><br>For example, if your first trigger event starts at 5 minutes and the exception event's time starts at 10 minutes, you would rely on the exception event's 10 minutes as the official campaign's message delivery time.

{% alert note %}
You cannot make a "session start" both the trigger event and exception event for a campaign. However, you always have the choice to select any other custom event outside of this option.
{% endalert %}

### Step 4: Assign duration

Assign the campaign's duration by specifying a start time and optional end time. If a user completes a trigger event during the specified time frame but qualifies for the message outside of the time frame due to a scheduled delay, then they will not receive the campaign. Therefore, if you set a time delay longer than the message's time frame, no users will receive your campaign. In addition, you can elect to send the message in users' [local time zones]({{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/scheduled_delivery/#local-time-zone-campaigns).

![Campaign Duration][21]

### Step 5: Select time frame

Select whether the user will receive the campaign during a specific portion of the day. If you give the message a time frame and the user either completes the trigger event outside the time frame or the message delay causes them to miss the time frame, then by default, the user will not receive your message.

![Sepcific Time Frame][27]

In the case where a user completes the trigger event within the time frame, but the message delay causes the user to fall out of the time frame, you can check the box below so that these users will still receive the campaign:

![Triggered Next Available][31]

If a user doesn't receive the message because they miss the time frame, then they will still be qualified to receive it the next time they complete the trigger event, even if you did not elect for users to become [re-eligible]({{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/reeligibility/). If you do elect for users to become re-eligible, then users can receive the campaign each time they complete the trigger event, assuming they qualify during the specified time frame.

If you have also assigned the campaign a certain duration, then a user must qualify within both the duration and the specific portion of the day to receive the message.

### Step 6: Determine re-eligibility

Determine whether users can become [re-eligible][24] for the campaign. If you allow users to become re-eligible, you may specify a time delay before the user can receive the campaign again. This will prevent your triggered campaigns from becoming "spammy".

![Campaign Re-eligibility][28]

## Use cases

Triggered campaigns are very effective for transactional or achievement-based messages.

Transactional campaigns include messages sent after the user completes a purchase or adds an item to their cart. The latter case is a great example of a campaign that would benefit from an exception event. Say your campaign reminds users of items in their cart that they haven't purchased. The exception event, in this case, would be the user buying the products in their cart. For achievement-based campaigns, you can send a message 5 minutes after the user completes a conversion or beats a game level.

In addition, when creating welcome campaigns, you can trigger messages to send after the user registers or sets up an account. Staggering messages to be sent on different days following registration will allow you to create a thorough onboarding process.

## Why did a user not receive my triggered campaign?

Any of these things will prevent a user who has completed the trigger event from receiving the campaign:

- The user completed the exception event before the time delay had fully elapsed.
- The time delay caused the user to become qualified to receive the campaign after the duration has ended.
- The time delay caused the user to become qualified to receive the campaign outside of the specified portion of the day.
- The user has already received the campaign, and users do not become re-eligible.
- While users are re-eligible to receive the campaign, they can only re-trigger it after a certain period of time, and that period of time has not yet elapsed.

[Segmenting]({{site.baseurl}}/user_guide/engagement_tools/segments/) a triggered campaign on user data recorded at the time of the event may cause a [race condition]({{site.baseurl}}/help/best_practices/race_conditions/#race-conditions). This happens when the user attribute on which the campaign is segmented gets changed, but the change hasn't been processed for the user when the campaign is sent. Since campaigns check for segment membership on entry, this can lead to the user not receiving the campaign.

For example, imagine you want to send an event-triggered campaign to male users who just registered. When the user registers, you record a custom event `registration` and simultaneously set the user's `gender` attribute. The event may trigger the campaign before Braze has processed the user's gender, preventing them from receiving the campaign.

It is a best practice to ensure that the attribute on which the campaign is segmented is flushed to Braze's servers before the event. In cases where this is not possible, the best way to guarantee delivery is to use [custom event properties][48] to attach the relevant user properties to the event and apply a property filter for the specific event property instead of a segmentation filter. In the example above, you would add a `gender` property to the custom event `registration` so that Braze is guaranteed to have the data you need when your campaign is triggered.

Additionally, if a campaign is action-based and has a delay, you can check the option to **Re-evaluate segment membership at send-time** to ensure users are still part of the target audience when the message is sent.

![reevaluate segment membership][51]

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
[29]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/in-app_message_behavior/#in-app-message-delivery-rules
[30]: {{site.baseurl}}/help/best_practices/user_onboarding/#user-onboarding
[31]: {% image_buster /assets/img_archive/schedule_triggered_next_available.png %}
[32]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/
[33]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/campaign_connector/#campaign-connector
[34]: {% image_buster /assets/img_archive/customEventProperties.png %}
[41]: {% image_buster /assets/img_archive/schedule_triggered7.png %}
[47]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/triggered_delivery/#why-did-a-user-not-receive-my-triggered-campaign
[48]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties
[49]: {{site.baseurl}}/help/help_articles/campaigns_and_canvas/not_triggering/
[50]: {% image_buster /assets/img_archive/schedule_triggered8.png %}
[51]: {% image_buster /assets/img_archive/reevaluate_segment_membership.png %}
