---
nav_title: Rate limiting and frequency capping
article_title: Rate Limiting and Frequency Capping
page_order: 6
tool: Campaigns
page_type: reference
description: "This reference article discusses the concept of rate limiting and frequency capping in campaigns, and how you can manage marketing pressure to improve user experience."

---

# Rate limiting and frequency capping

> Rate limiting and frequency capping can be used together to make sure your users are getting the messages they need to, and none of the ones they don't.

## About rate limiting

Braze allows you to control marketing pressure by rate limiting your campaigns, regulating the amount of outgoing traffic from your platform. You can implement two different types of rate limiting for your campaigns: 

1. [**User-centric rate limiting:**](#user-centric-rate-limiting) Focuses on providing the best experience for the user.
2. [**Delivery speed rate limiting:**](#delivery-speed-rate-limiting) Takes into consideration the bandwidth of your servers.

Braze will try to evenly distribute the message sends throughout the minute, but can't guarantee this. For example, if you have a campaign with a rate limit of 5,000 messages per minute, we'll try to distribute the 5,000 requests evenly through the minute (about 84 messages per second), but there may be some variation in the per-second rate.

### User-centric rate limiting

As you create more segments, there are going to be cases where the membership of those segments overlaps. If you're sending out campaigns to those segments, you want to be sure that you are not messaging your users too often. If a user receives too many messages within a short time period, they will feel over-encumbered and either turn off push notifications or uninstall your app.

#### Relevant segment filters

Braze provides the following filters in order to help you limit the rate at which your users receive messages:

- Last Engaged With Message
- Last Received Any Message
- Last Received Push Campaign
- Last Received Email Campaign
- Last Received SMS

#### Implementing filters

Let's say we've created a segment named "Retargeting Filter Showcase" with a filter "Last used these apps more than 7 days ago" to target users. This would be a standard re-engagement segment.

If you have other more targeted segments receiving notifications recently, you may not want your users to be targeted by more generic campaigns directed at this segment. Appending the "Last Received Push Campaign" filter to this segment, the user has ensured that if they've received another notification in the past 24 hours, they will slide out of this segment for the next 24 hours. If they still meet the other criteria of the segment 24 hours later and haven't received any more notifications they will slide back into the segment.

![Segment Details section with the "Last Received Any Message" segment filter highlighted.]({% image_buster /assets/img_archive/rate_limit_daily.png %})

Appending this filter to all segments targeted by campaigns would cause your users to receive a maximum of one push every 24 hours. You could then prioritize your messaging by ensuring that your most important messages are delivered before less important messages.

#### Setting a maximum user cap

In the **Target Audiences** step of your campaign composer, you can also limit the total number of users that will receive your message. This serves as a check that's independent of your campaign filters, allowing you to freely segment users without worrying about over-spamming.

![Audience Summary with a selected checkbox for limiting the number of people who receive the campaign.]({% image_buster /assets/img_archive/total_limit.png %})

By selecting the maximum user limit, you can limit the rate at which your users receive notifications on a per-channel basis or globally across all message types.

##### Maximum user cap with optimizations

If you're using an optimization like Winning Variant or Personalized Variant, the campaign will consist of two sends: the initial experiment and the final send. 

To set up a maximum user cap in this scenario, select **Limit the number of people who will receive this campaign**, then select **In total this campaign should**, and enter an audience limit. Your audience limit will be split up by the percentages shown in the **A/B Testing** panel. 

If you select **Every time the campaign is scheduled**, those two phases will be separately limited to the number set. This is typically not desirable.

#### Setting a maximum impression cap

For in-app messages and Content Cards, you can control marketing pressure by setting a maximum number of impressions that will be displayed to your user base, after which Braze will not send down more messages to your users. However, it is important to note that this cap is not exact. 

New Content Cards and in-app message rules are sent down to an app on session start, meaning that Braze can send a message to the user before the cap is hit, but by the time the user triggers the message, the cap has now been hit. In this situation, the device will still display the message.

For example, let's say you have a game with an in-app message that triggers when a user beats a level, and you cap it at 100 impressions. There have been 99 impressions so far. Alice and Bob both open the game and Braze tells their devices that they are eligible to receive the message when they beat a level. Alice beats a level first and gets the message. Bob beats the level next, but because his device hasn't communicated with Braze servers since his session started, his device is unaware that the message has met its cap and he will also receive the message. However, when an impression cap has been hit, the next time any device requests the list of eligible in-app messages, that message will not be sent down and will be removed from that device.

### Rate limiting and A/B testing

When using rate limiting with an A/B test, the rate limit isn't applied to the control group in the same way as the test group, which is a potential source of time bias. To avoid this bias, use appropriate conversion windows.

### Delivery speed rate limiting

If you anticipate large campaigns driving a spike in user activity and overloading your servers, you can specify a per-minute rate limit for sending messages, which means Braze will send no more than your rate-limited setting within a minute.

When targeting users during campaign creation, you can navigate to **Target Audiences** (for campaigns) or **Send Settings** (for Canvas) to select a rate limit (in various increments from as low as 10 to as high as 500,000 messages per minute).

Note that non-rate-limited campaigns may exceed these delivery limits. However, be aware that messages will be aborted if they’re delayed 72 hours or more due to a low rate limit. If the rate limit is too low, the creator of the campaign will receive alerts in the dashboard and by email.

![Audience Summary with a selected checkbox for limiting the rate at which the campaign will end, and rate being 500,000 per minute.]({% image_buster /assets/img_archive/per_minute_rate_limit.png %})

#### Example

If you are trying to send out 75,000 messages with a 10,000-per-minute rate limit, the delivery will be spread out over eight minutes. Your campaign will deliver no more than 10,000 messages for each of the first seven minutes, and 5,000 over the last minute.

#### Number of sends

Note that rate-limited messages may not be sent evenly over the course of each minute. Using the example of a 10,000-per-minute rate limit, this means Braze makes sure no more than 10,000 messages are sent per minute. This could mean a higher percentage of the 10,000 messages are sent within the first half minute versus the last half minute.

The rate limit is applied at the start of the message send attempt. When there are fluctuations in the time it takes for the send to complete, the number of completed sends may slightly exceed the rate limit in some minutes. Over time, the number of sends per minute will average out to no more than the rate limit.

{% alert important %}
Be wary of delaying time-sensitive messages with this form of rate limiting in relation to the total number of users in a segment. For example, if the segment contains 30 million users but we set the rate limit to 10,000 per minute, a large portion of your user base won’t receive the message until the following day.
{% endalert %}

#### Single-channel campaigns

When sending a single-channel campaign with a speed rate limit, the rate limit is applied for all messages together.

#### Multichannel campaigns

When sending a multi-channel campaign with a speed rate limit, each channel is sent independently of the others. As a result, the following may occur:

- The total number of messages sent per minute could be more than the rate limit. 
    - For example, if your campaign has a rate limit of 10,000 per minute and uses email and SMS, Braze can send a max of 20,000 total messages each minute (10,000 email and 10,000 SMS).
- Users could receive the different channels at different times, and it is not predictable which channel they will get first. 
    - For example, if you send a campaign that contains an email and an SMS, you may have 10,000 users with valid phone numbers and 50,000 users with valid email addresses. If you set the campaign to send 100 messages per minute (a slow rate limit for the campaign size), a user could receive the SMS in the first batch of sends and the email in the last batch of sends, almost nine hours later.

#### Multi-platform push campaigns

For push campaigns delivering on multiple platforms, the selected rate limit will be equally distributed across platforms. A push campaign leveraging Android and iOS with a 10,000 rate-limit per minute will equally distribute the 10,000 messages across the two platforms.

#### Canvas delivery speed rate limiting {#canvas-delivery-speed}

When sending a Canvas with a speed rate limit, the rate limit is shared between channels. This means the total number of messages sent per minute from the Canvas will not exceed the rate limit. For example, if your Canvas has a rate limit of 10,000 per minute and uses email and SMS, Braze will send a total of 10,000 messages per minute across email and SMS.

#### Rate limiting and Connected Content retries

When the [Connected Content retry]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/connected_content_retries/) is turned on, Braze will retry call failures while respecting the rate limit you set for each resend. Let’s consider the scenario of sending 75,000 messages with a 10,000 per minute rate limit. Imagine that in the first minute, the call fails or is slow and only sends 4,000 messages.

Instead of trying to make up for the delay and send the remaining 6,000 messages in the second minute or add them to the 10,000 that are already set to send, Braze will move those 6,000 messages to the “back of the queue” and add a minute, if necessary, to the total minutes it would take to send your message.

| Minute | No Failure | 6,000 Failure in Minute 1 |
|--------|------------|---------------------------|
| 1      | 10,000     | 4,000                     |
| 2      | 10,000     | 10,000                    |
| 3      | 10,000     | 10,000                    |
| 4      | 10,000     | 10,000                    |
| 5      | 10,000     | 10,000                    |
| 6      | 10,000     | 10,000                    |
| 7      | 10,000     | 10,000                    |
| 8      | 5,000      | 10,000                    |
| 9      | 0          | 6,000                     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Connected Content requests are not rate limited independently and will follow the webhook rate limit. This means if there is one Connected Content call to a unique endpoint per webhook, you would expect 5,000 webhooks and also 5,000 Connected Content calls per minute. Note that caching may affect this and reduce the number of Connected Content calls. Additionally, retries may increase the Connected Content calls, so we recommend checking that the Connected Content endpoint can handle some fluctuation here.

## About frequency capping

As your user base continues to grow and your messaging scales to include lifecycle, triggered, transactional, and conversion campaigns, it's important to prevent your notifications from appearing "spammy" or disruptive. By providing greater control over your users' experience, frequency capping enables you to create the campaigns you desire without overwhelming your audience.

### Feature overview {#freq-cap-feat-over}

Frequency capping is applied at the campaign or Canvas component send level and can be set up for each workspace from **Settings** > **Frequency Capping Rules**.

By default, frequency capping is toggled on when new campaigns are created. From here, you can choose the following:

- Which messaging channel you would like to cap: push, email, SMS, webhook, WhatsApp, or any of those five.
- How many times each user should receive a campaign or Canvas component sends from a channel within a certain time frame.
- How many times each user should receive a campaign or Canvas component sends by [tag](#frequency-capping-by-tag) within a certain time frame.

This time frame can be measured in minutes, days, or weeks (seven days), with a maximum duration of 30 days.

Each line of frequency caps will be connected using the `AND` operator, and you can add up to 10 rules per workspace. In addition, you may include multiple caps for the same message types. For instance, you can cap users to no more than one push per day and no more than three pushes per week.

![Frequency capping section with lists of campaigns and Canvases that rules will and will not apply to.]({% image_buster /assets/img_archive/rate_limiting_overview_2.png %})

#### Behavior when users are frequency capped on a Canvas step

If a Canvas user is frequency capped because of global frequency capping settings, then the user will immediately advance to the next Canvas step. The user will not exit the Canvas because of the frequency cap.

### Delivery rules

There may be some campaigns, like transactional messages, that you want to always reach the user, even if they have already reached their frequency cap. For example, a delivery app may wish to send an email or push when an item is delivered regardless of how many campaigns the user has received.

If you want a particular campaign to override frequency capping rules, you can set this up in the Braze dashboard when scheduling that campaign's delivery by toggling **Frequency Capping** to **OFF**. 

After this, you will be asked if you still want this campaign to count toward your frequency cap. Messages that count toward frequency capping are included in calculations for the Intelligent Channel filter. When sending [API campaigns]({{site.baseurl}}/developer_guide/rest_api/messaging/#messaging), which are often transactional, you'll have the ability to specify that a campaign should ignore frequency capping rules [within the API request]({{site.baseurl}}/developer_guide/rest_api/api_campaigns/#api-campaigns) by setting `override_messaging_limits` to `true`.

By default, new campaigns and Canvases that do not obey frequency caps will also not count toward them. This is configurable for each campaign and Canvas.

{% alert note %}
This behavior changes the default behavior when you turn off frequency capping for a campaign or Canvas. The changes are backward compatible and do not impact messages that are currently live.
{% endalert %}

![Delivery Controls section with Frequency Capping turned on.]({% image_buster /assets/img_archive/frequencycappingupdate.png %})

Different channels within a multichannel campaign will individually count  the frequency cap. For instance, if you create a multichannel campaign with both push and email and have frequency capping set up for both of those channels, then the push will count toward one push campaign and the email message will count toward one email message campaign. The campaign will also count toward one "campaign of any type." If users are capped to one push and one email campaign per day and a user receives this multichannel campaign, then they will no longer be eligible for push or email campaigns for the rest of the day (unless a campaign ignores frequency capping rules).

In-app messages and Content Cards are not counted as or toward caps on campaigns or Canvas components of any type.

{% alert important %}
Global frequency capping is scheduled based on the user's time zone, and is calculated by calendar days, not 24-hour periods. For example, if you set up a frequency capping rule of sending no more than one campaign a day, a user may receive a message at 11 pm in their local time zone and they would be eligible to receive another message an hour later.
{% endalert %}

#### Use cases

{% tabs %}
{% tab Use case 1 %}

Let's say that you set a frequency capping rule which asks that your user receive no more than three push notification campaigns or Canvas components per week from all campaign or Canvas components.

If your user is slated to receive three push notifications, two in-app messages, and one Content Card this week, they will receive all of those messages.

{% endtab %}
{% tab Use case 2 %}

This scenario uses the following frequency capping rules:

**When following scenario occurs:**

- A user triggers the same campaign, `Campaign ABC` three times over the course of a week.
- This user triggers `Campaign ABC` once on Monday, once on Wednesday, and once on Thursday.

![Frequency Capping section with the rule of sending no more than 2 push notification campaigns/Canvas steps from all campaigns/Canvas steps to a user every 1 week.]({% image_buster /assets/img/standard_rules_fnfn.png %})

**Then, the expected behavior is that:**

- This user will receive the campaign sends that triggered on Monday and Wednesday.
- This user will not receive the third campaign send on Thursday because the user has already received two push campaign sends that week.

{% endtab %}
{% endtabs %}

### Frequency capping by tag

[Frequency capping rules](#delivery-rules) can be applied to workspaces using specific tags you have applied to your campaigns and Canvases, allowing you to essentially base your frequency capping on custom-named groups.

With frequency capping by tag, rules can be set on the main and nested tags, so Braze will take into account all tags. For example, if you've selected to use the main tag A to frequency cap, we'll also include information in all the nested tags (for example, tags B and C) when determining the limit.

You can also combine regular frequency capping with frequency capping by tags. Consider the following rules:

1. No more than three push notification campaigns or Canvas components per week from all campaign and Canvas steps. <br>**AND**
2. No more than two push notification campaign or Canvas components per week with the tag `promotional`.

![Frequency Capping section with two rules limiting how many push notification campaigns/Canvases can be sent to a user every 1 week.]({% image_buster /assets/img/tag_rule_fnfn.png %} "rules")

As a result, your users will receive no more than three campaign sends per week over all campaigns and Canvas steps and no more than two push notification campaigns or Canvas components with the tag `promotional`.

{% alert important %}
Canvases are tagged at the Canvas level, as opposed to tagging by component. So, each Canvas component will inherit all of the Canvas level tags.
{% endalert %}

#### Conflicting rules

When rules conflict, the most restrictive, applicable frequency capping rule will be applied to your users. For example, let's say you have the following rules:

1. No more than one push notification campaign or Canvas component per week from all campaign and Canvas components. <br>**AND**
2. No more than three push notification campaigns or Canvas components per week with the tag `promotional`.

![Frequency Capping section with conflicting rules to limit how many push notification campaigns/Canvas steps are sent to a user every 1 week.]({% image_buster /assets/img/global_rules.png %} "global rules")

In this example, your user will not receive more than one push notification campaign or Canvas components with the tag "promotional" in a given week, because you've specified that users should not receive more than one push notification campaign or Canvas component from all campaigns and Canvas components. In other words, the most restrictive applicable frequency rule is the rule that will be applied to a given user.

#### Tag count

Frequency capping by tag rules compute at the time a message sends. This means that frequency capping by tag only counts tags that are currently on the campaigns or Canvases that a user received in the past. It does not count the tags that were on the campaigns or Canvases during the time they were sent but have since been removed. It will count if a tag is later added to a message that a user received in the past, but before the newest tagged message is sent.

##### Use case

Consider the following campaigns and frequency capping by tag rule:

**Campaigns**:

- **Campaign A** is a push campaign tagged as `promotional`. It is slated to send at 9 am on Monday.
- **Campaign B** is a push campaign tagged as `promotional`. It is slated to send at 9 am on Wednesday.

**Frequency Capping by Tag Rule:**

- Your user should receive no more than one push notification campaign per week with the tag `promotional`.<br><br>

| Action | Result |
|---|---|
| The `promotional` tag is removed from **Campaign A** after your user received the message, but before **Campaign B has sent.** | Your user will receive **Campaign B**.|
| The `promotional` tag is mistakenly removed from **Campaign A** after your user received the message. <br> The tag is added back to **Campaign A** on Tuesday, before **Campaign B** is sent. | Your user will not receive **Campaign B**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Sending at large scales {#sending-at-large-scales}

Frequency capping by tag rules might not be applied properly at large scales, such as 100 messages per channel from campaigns or Canvas components.

For example, if your frequency capping by tag rule is:

> No more than two email campaigns or Canvas components with the tag `Promotional` to a user every week.

And you send the user more than 100 emails from campaigns and Canvas steps with frequency capping turned on over the course of a week, more than two emails may be sent to the user.

Because 100 messages per channel are more messages than most brands send to their users, it's unlikely that you will be impacted by this limitation. To avoid this limitation, you can set a cap for the maximum number of emails you'd like your users to receive over the course of a week.

For example, you might set up the following rule:

> No more than three email campaigns or Canvas components per week from all campaign and Canvas steps.

This rule will ensure that no users receive more than 100 emails per week because, at most, users will receive three emails per week from campaigns or Canvas components with frequency capping turned on.

