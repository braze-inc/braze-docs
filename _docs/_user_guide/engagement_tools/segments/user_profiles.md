---
nav_title: User profiles
article_title: User Profiles
page_order: 9
page_type: reference
tool: 
  - Dashboard
description: "This reference article describes how to access a user's profile in the dashboard, profile use cases, and what each profile contains."

---

# User profiles

> User profiles are a great way to find information about specific users. All persistent data associated with a user is stored in their user profile.

## Access profiles

To access a user's profile, go to the **Search Users** page and search for a user by any of the following:

- External user ID
- Braze ID
- Email
- Phone number
- Push token
- User alias with the format "[user_alias]:[alias_name]", such as "amplitude_id:user_123"

If a match is found, you can view the information you've recorded for this user with the Braze SDK. Otherwise, if your search returns multiple user profiles, you can merge each profile individually or perform a bulk user merge. For a full walkthrough, see [Duplicate Users]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users/).

{% alert important %}
When a phone number is used in the search, it is changed into [`E.164`](https://en.wikipedia.org/wiki/e.164) format. Users whose phone numbers cannot be changed into `E.164` format (for example, because the phone number has an invalid country code or area code) cannot be searched by phone number.
{% endalert %}

![Search results with a banner that reads "Multiple users match your search criteria" and two buttons labeled Previous and Next.]({% image_buster /assets/img_archive/User_Search_Nonunique.png %}){: style="max-width:60%;"}

## Use cases

User profiles are a great resource for troubleshooting and testing because you can easily access information about a user's engagement history, segment membership, device, and operating system.

For example, if a user reports a problem and you aren't sure what device and operating system they are using, you can use the [Overview tab](#overview-tab) to find this information (as long as you have their email or user ID). You can also view a user's language, which could be helpful if you're troubleshooting a [multi-lingual campaign]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/campaigns_in_multiple_languages/#campaigns-in-multiple-languages) that didn't behave as expected.

You can use the [Engagement tab](#engagement-tab) to verify whether a certain user received a campaign. In addition, if this particular user did receive the campaign, you can see when they received it. You can also verify whether a user is in a certain segment and whether a user is opted in to push, email, or both. This information is useful for troubleshooting purposes. For example, you should check this information if a user doesn't receive a campaign that you expected them to receive or receives a campaign that you did not expect them to receive.

## Elements of user profile

There are four main sections of a user's profile.

- **Overview:** Basic information about the user, session data, custom attributes, custom events, purchases, and the most recent device that the user logged into.
- **Engagement:** Information about the user's contact settings, campaigns received, segments, communication stats, install attribution, and random bucket number.
- **Messaging History:** Recent messaging-related events for this user from the past 30 days.
- **Feature Flags Eligibility:** Validate which feature flags a user is currently eligible for across rollouts, canvas steps, and experiments. 

### Overview tab {#overview-tab}

The **Overview** tab contains basic information about a user and their interactions with your app or website.

| Overview category | Contains |
| --- | --- |
| Profile | Gender, age group, location, language, locale, time zone, and birthday. |
| Sessions overview | How many sessions they had, when their first and last sessions were, and on which apps. |
| Custom attributes | Which custom attributes are attributed to this user and their associated value, including nested custom attributes. |
| Recent devices | How many devices they logged in on, details on each device, and their associated advertising IDs (if any). |
| Custom events | Which custom events this user has performed, how many times, and when they last performed each event. |
| Purchases | Lifetime revenue attributed to this user, their last purchase, total number of purchases, and a list of each purchase. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

For more information on this data, see [SDK data collection]({{site.baseurl}}/user_guide/data/unification/user_data/sdk_data_collection/).

![The Overview tab of a user profile.]({% image_buster /assets/img_archive/user_profile2.png %})

### Engagement tab {#engagement-tab}

The **Engagement** tab contains information about a user's interactions with the messages you sent them using Braze.

| Engagement category | Contains |
| --- | --- |
| Contact settings | Subscription status for email, SMS, and push, and the subscription groups this user is associated with for these three channels. This section also includes changelog information for push tokens. Refer to [email]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/), [SMS]({{site.baseurl}}/sms_rcs_subscription_groups/), and [push]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/) for information on how subscriptions and opt-ins are set. |
| Campaigns received | Campaigns received are marked when the user receives the campaign, or when we first detect interaction data for a user. Select a campaign from the list to view it. |
| Segments | Segments this user is included in. Select a segment from the list to view it. |
| Communication stats | When this user last received messages from you from each channel. |
| Install attribution | Information about how and when a user installed your app. Learn more about [understanding user installs]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/install_attribution/). |
| Miscellaneous | The user's [random bucket number]({{site.baseurl}}/user_guide/engagement_tools/testing/random_bucket_numbers/). |
| Canvas messages received | Canvas messages this user has received and when. Select a message from the list to view it. |
| Predictions | [Churn prediction]({{site.baseurl}}/user_guide/brazeai/predictive_churn/) and [event prediction]({{site.baseurl}}/user_guide/brazeai/predictive_events/) scores for this user. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![The Engagement tab of a user profile displaying their contact settings and communication statistics.]({% image_buster /assets/img_archive/profiles_engagement_tab.png %})

### Messaging History tab

The **Message History** tab of the user profile shows recent messaging-related events (about 40) for an individual user from the past 30 days. These events include the messages that the user was sent, received, interacted with, and more. Note that the data in this tab isn't updated after a user is merged.

{% alert note %}
If you have feedback on this table or would like to see specific events, please email [user-targeting@braze.com](mailto:user-targeting@braze.com?subject=Messaging%20History%20Tab%20Feedback) with the subject line "Messaging History Tab Feedback".
{% endalert %}

![The Messaging History tab showing which campaigns and Canvases a user has received.]({% image_buster /assets/img_archive/profiles_messaging_history_tab.png %})

#### Viewing and understanding events

For each event in the **Messaging History** table, you can see the messaging channel, event type, timestamp the event occurred, the associated campaign or Canvas message, and the user's device data. To filter for specific events, click **Filters** and select events from the list.

##### Message engagement events

The following message engagement events are available for email, SMS, push, in-app messages, Content Cards, and webhooks. To learn more about how specific events are tracked, refer to the [Message engagement event glossary]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/).

| Channel | Engagement events available |
| --- | --- |
| Email | Bounce<br>Click<br>Deferral events<br>Delivery<br>Mark as spam<br>Open (see [note on email open event](#note-on-email-open-event))<br>Send<br>Soft bounce<br>Unsubscribe |
| SMS | Carrier send<br>Delivery<br>Delivery failure<br>Inbound receive<br>Rejection<br>Send |
| Push | Bounce<br>Influenced open<br>iOS Foreground<br>Open<br>Send |
| In-app message | Click<br>Impression |
| Content Cards | Click<br>Dismiss<br>Impression<br>Send |
| Webhooks | Send |
| WhatsApp | Abort<br>Delivery<br>Failure<br>Frequency capped<br>Inbound receive<br>Read<br>Send |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

##### Message abort events

Message abort events occur when a message sent to a user was aborted due to conditional logic in [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/) or [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/aborting_connected_content#aborting-messages), or from Liquid rendering timeouts.

Abort events are available for the following channels:

- Email
- SMS
- Push
- Webhooks

Abort events are currently not available for in-app messages and Content Cards.

##### Frequency cap events

A frequency cap event occurs when a user is qualified to receive a message, but doesn't actually receive it due to [frequency capping]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping) settings. You can customize frequency capping settings from **Settings** > **Frequency Capping Rules**.

##### Blank destinations

Some message sends may appear in the Messaging History with blank destinations (signified by "—"). This is because some channels, such as Content Cards and webhooks, do not gather device data on message send.

Content Cards sends are logged when the card is available to be viewed. Because Content Cards can be viewed on multiple devices, device data is not logged for a send. Instead, this information is logged upon impression (when the card is actually viewed). Webhooks are sent to a system endpoint (not a device) so device data is not applicable.

#### Note on email open event {#note-on-email-open-event}

Email open tracking is error-prone in any tool, including Braze. With a variety of privacy protection features offered by different email clients that either block the automatic loading of images or load them proactively on the server, email open events are susceptible to both false positives and false negatives.

While email open statistics can be useful in aggregate, for example, to compare the effectiveness of different subject lines, you should not assume an individual open event for an individual user is meaningful.

#### Why are certain fields blank in the Message History tab?

Some fields may be absent in a user's **Message History** tab in the following scenarios:

- When an event is missing data for **Message Sent**, this indicates that the campaign doesn't have any message variations.
- When an event is missing data for **Campaign/Canvas** and **Message Sent**, this indicates that this message was sent from an API campaign (not API-triggered campaigns) that didn't specify the `campaign_id` and `message_variation_id`. These fields are optional and may be left out of the request body. When these fields are specified, that information is populated into the message history logs.
   - If a particular message is missing entirely from the messaging history but appears in the **Campaigns Received** log, it's likely the user received the campaign before being identified as the current user. If an existing profile is orphaned, the **Campaigns Received** log is transferred, but the messaging history is not. 
- When data is missing for **Campaign/Canvas**, a manual test may have been sent. Manual tests are logged in the **Messaging History** tab, but the campaign or Canvas that was sent won't be logged.


