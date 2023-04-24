---
nav_title: Rate Limiting and Frequency Capping
article_title: Rate Limiting and Frequency Capping
page_order: 6
tool: Campaigns
page_type: reference
description: "This reference article discusses the concept of rate limiting and frequency capping in campaigns, and how you can manage marketing pressure to improve user experience."

---

# Rate limiting and frequency capping

> This reference article discusses the concept of rate limiting and frequency capping in campaigns, and how you can apply that marketing pressure to improve user experience.
> <br>
> <br>
> We all want our users to have the best experience possible. With rate limiting and frequency capping, you can make sure your users are getting the message they need to, and none of the ones they don't.

## Rate limiting

Braze allows you to control marketing pressure by rate limiting your campaigns, regulating the amount of outgoing traffic from your platform. You can implement two different types of rate limiting for your campaigns. The first focuses on providing the best experience for the user, while the second takes into consideration the bandwidth of your servers.

### User centric rate limiting

As you create more segments, there are going to be cases where the membership of those segments overlaps. If you're sending out campaigns to those segments, you want to be sure that you are not messaging your users too often. If a user receives too many messages within a short time period, they will feel over-encumbered and either turn off push notifications or uninstall your app.

#### Relevant segment filters

Braze provides the following filters in order to help you limit the rate at which your users receive messages:

- Last Engaged With Message
- Last Received Any Message
- Last Received Push Campaign
- Last Received Email Campaign
- Last Received SMS
- Last Viewed News Feed

#### Implementing filters

Let's say we've created a segment named "Retargeting Filter Showcase" with a filter "Last used these apps more than 7 days ago" to target users. This would be a standard re-engagement segment.

If you have other more targeted segments receiving notifications recently, you may not want your users to be targeted by more generic campaigns directed at this segment. Appending the "Last Received Push Campaign" filter to this segment, the user has ensured that if they've received another notification in the past 24 hours, they will slide out of this segment for the next 24 hours. If they still meet the other criteria of the segment 24 hours later and haven't received any more notifications they will slide back into the segment.

![][1]

Appending this filter to all segments targeted by campaigns would cause your users to receive a maximum of one push every 24 hours. You could then prioritize your messaging by ensuring that your most important messages are delivered before less important messages.

#### Setting a max user cap

Additionally, in the **Target Users** step of your campaign composition, you can limit the total number of users that will receive your message. This feature serves as a check that is independent of your campaign filters, allowing you to freely segment users without needing to worry about over-spamming.

![][2]

By selecting the max user limit, you can limit the rate at which your users receive notifications on a per-channel basis or globally across all message types.

#### Setting a max impression cap

For in-app messages, you can control marketing pressure by setting a maximum number of impressions that will be displayed to your user base, after which Braze will not send down more messages to your users. However, it is important to note that this cap is not exact. New in-app message rules are sent down to an app on session start, meaning that Braze can send an in-app message down to the user before the cap is hit, but by the time the user triggers the message, the cap has now been hit. In this situation, the device will still display the message.

For example, let's say you have a game with an in-app message that triggers when a user beats a level, and you cap it at 100 impressions. There have been 99 impressions so far. Alice and Bob both open the game and Braze tells their devices that they are eligible to receive the message when they beat a level. Alice beats a level first and gets the message. Bob beats the level next, but since his device has not communicated with Braze's servers since his session start, his device is unaware that the message has met its cap and he will also receive the message. However, once an impression cap has been hit, the next time any device requests the list of eligible in-app messages, that message will not be sent down and will be removed from that device.

### Delivery speed rate limiting

If you anticipate large campaigns driving a spike in user activity and overloading your servers, you may specify a per-minute rate limit for sending messages. While targeting users during campaign creation, you can navigate to Advanced Options to select a rate limit (in various increments from as low as 50 to as high as 500,000 messages per minute). Note that non-rate-limited campaigns may exceed these delivery limits. Be aware, however, that messages will be aborted if they are delayed 72 hours or more due to a low rate limit. The user who created the campaign will receive alerts in the dashboard and via email if the rate limit is too low.

![][3]

For instance, if you are trying to send out 75,000 messages with a 10,000 per minute rate limit, the delivery will be spread out over 8 minutes. Your campaign will deliver 10k for each of the first seven minutes, and 5,000 over the last minute. Be wary of delaying time-sensitive messages, however, with this form of rate limiting. If the segment contains 30M users but we set the rate limit to 10K per minute, a large portion of the user base won't receive the message until the following day.

{% alert important %}
When sending a multichannel campaign with a speed rate limit, each channel is sent independently of the others. The effect is that users could receive the different channels at different times, and it is not predictable which channel they will get first. For example, if you send a campaign that contains an email and a push notification, you may have 10,000 users with valid push tokens but 50,000 users with valid email addresses. If you set the campaign to send 100 messages per minute (a slow rate limit for the campaign size), a user could receive the push notification in the first batch of sends and the email in the last batch of sends, almost nine hours later.
{% endalert %}

#### Rate limiting and Connected Content retries

When the [Connected Content Retry][19] feature is enabled, Braze will retry call failures while respecting the rate limit you set for each resend. Let’s think again about the 75,000 messages with a 10,000 per minute rate limit. In the first minute, the call fails or is slow and only sends 4,000 messages.

Instead of attempting to make up for the delay and send the remaining 4,000 messages in the second minute or add it to the 10,000 it is already set to send, Braze will move those 6,000 failed messages to the "back of the queue" and add an additional minute, if necessary, to the total minutes it would take to send your message.

|Minute|No Failure|6,000 Failure in Minute 1|
|---|---|---|
|1|10,000|4,000|
|2|10,000|10,000|
|3|10,000|10,000|
|4|10,000|10,000|
|5|10,000|10,000|
|6|10,000|10,000|
|7|10,000|10,000|
|8|5,000|10,000|
|9|0|6,000|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

#### Multichannel campaigns

Keep in mind that the per-minute rate limit is adjusted on a per-campaign basis. If multiple channels are utilized within a campaign, the rate limit will apply to each of those channels. If your campaign utilizes email and in-app banners with a rate limit of 10,000 per minute, we will send 20,000 total messages each minute (10,000 email and 10,000 push).

#### Multi-platform push campaigns

For push campaigns delivering on multiple platforms, the rate limit selected will be equally distributed across platforms. A push campaign leveraging Android and iOS with a 10,000 rate-limit per minute will equally distribute the 10,000 messages across the two platforms.

## Frequency capping

As your user base continues to grow and your messaging scales to include lifecycle, triggered, transactional, and conversion campaigns, it’s important to prevent your notifications from appearing spammy or disruptive. By providing greater control over your users’ experience, frequency capping enables you to create the campaigns you desire without overwhelming your audience.

### Feature overview {#freq-cap-feat-over}

Frequency capping is applied at the campaign or Canvas component send level and can be set up for each app group by selecting **Global Message Settings** found in the **Engagement** tab. By default, frequency capping is toggled on when new campaigns are created. From here, you can choose the following:

- Which messaging channel you would like to cap: push, email, SMS, webhook, or any of those four.
- How many times each user should receive a campaign or Canvas component sends from a channel within a certain time frame.
- How many times each user should receive a campaign or Canvas component sends by [tag](#frequency-capping-by-tag) within a certain time frame.

This time frame can be measured in minutes, days, weeks (seven days), or months, with a maximum duration of 30 days.

Each line of frequency caps will be connected using the `AND` operator, and you can add up to 10 rules per app group. In addition, you may include multiple caps for the same message types. For instance, you can cap users to no more than one push per day and no more than three pushes per week.

![][14]

### Delivery rules

There may be some campaigns, like transactional messages, that you want to always reach the user, even if they have already reached their frequency cap. For example, a delivery app may wish to send an email or push when an item is delivered regardless of how many campaigns the user has received.

If you want a particular campaign to override frequency capping rules, you can set this up in the Braze dashboard when scheduling that campaign's delivery by toggling **Frequency Capping** to **OFF**. 

After this, you will be asked if you still want this campaign to count towards your Frequency Cap. Messages that count towards frequency capping are included in calculations for the Intelligent Channel filter. When sending [API campaigns][15], which are often transactional, you'll have the ability to specify that a campaign should ignore frequency capping rules [within the API request][16] by setting `override_messaging_limits` to `true`.

By default, new campaigns and Canvases that do not obey Frequency Caps will also not count towards them. This is configurable for each campaign and Canvas.

{% alert note %}
This behavior changes the default behavior when you turn off frequency capping for a campaign or Canvas. The changes are backward compatible and do not impact messages that are currently live.
{% endalert %}

![][18]

Different channels within a multichannel campaign will individually count towards the frequency cap. For instance, if you create a multichannel campaign with both push and email and have frequency capping set up for both of those channels, then the push will count toward one push campaign and the email message will count toward one email message campaign. The campaign will also count toward one "campaign of any type." If users are capped to one push and one email campaign per day and a user receives this multichannel campaign, then they will no longer be eligible for push or email campaigns for the rest of the day (unless a campaign ignores frequency capping rules).

In-app messages and Content Cards are not counted as or towards caps on campaigns or Canvas components of any type.

{% alert important %}
Global frequency capping is scheduled based on the user's time zone, and is calculated by calendar days, not 24-hour periods. For example, if you set up a frequency capping rule of sending no more than one campaign a day, a user may receive a message at 11 pm in their local time zone and they would be eligible to receive another message an hour later.
{% endalert %}

#### Examples

{% tabs %}
{% tab Example 1 %}

Let's say that you set a frequency capping rule which asks that your user receive no more than three push notification campaigns or Canvas components per week from all campaign or Canvas components.

If your user is slated to receive three push notifications, two in-app messages, and one Content Card this week, they will receive all of those messages.

{% endtab %}
{% tab Example 2 %}

This following example uses the following frequency capping rules:

**When following scenario occurs:**

- A user triggers the same campaign, `Campaign ABC` three times over the course of a week.
- This user triggers `Campaign ABC` once on Monday, once on Wednesday, and once on Thursday.

![]({% image_buster /assets/img/standard_rules_fnfn.png %})

**Then, the expected behavior is that:**

- This user will receive the campaign sends that triggered on Monday and Wednesday.
- This user will not receive the third campaign send on Thursday because the user has already received two push campaign sends that week.

{% endtab %}
{% endtabs %}

### Frequency capping by tag

[Frequency capping rules](#delivery-rules) can be applied to app groups using specific tags you have applied to your campaigns and Canvases, allowing you to essentially base your frequency capping on custom-named groups.

With frequency capping by tag, rules can be set on the main and nested tags, so Braze will take into account all tags. For example, if you've selected to use the main tag A to frequency cap, we'll also include information in all the nested tags (for example, tags B and C) when determining the limit.

You can also combine regular frequency capping with frequency capping by tags. Consider the following rules:

1. No more than three push notification campaigns or Canvas components per week from all campaign and Canvas steps. <br>**AND**
2. No more than two push notification campaign or Canvas components per week with the tag `promotional`.

![][12]

As a result, your users will receive no more than three campaign sends per week over all campaigns and Canvas steps and no more than two push notification campaigns or Canvas components with the tag `promotional`.

{% alert important %}
Canvases are tagged at the Canvas level, as opposed to tagging by component. So, each Canvas component will inherit all of the Canvas level tags.
{% endalert %}

#### Conflicting rules

When rules conflict, the most restrictive, applicable frequency capping rule will be applied to your users. For example, let's say you have the following rules:

1. No more than one push notification campaign or Canvas component per week from all campaign and Canvas components. <br>**AND**
2. No more than three push notification campaigns or Canvas components per week with the tag `promotional`.

![][11]

In this example, your user will not receive more than one push notification campaign or Canvas components with the tag "promotional" in a given week, because you've specified that users should not receive more than one push notification campaign or Canvas component from all campaigns and Canvas components. In other words, the most restrictive applicable frequency rule is the rule that will be applied to a given user.

#### Tag count

Frequency capping by tag rules compute at the time a message sends. This means that frequency capping by tag only counts tags that are currently on the campaigns or Canvases that a user received in the past. It does not count the tags that were on the campaigns or Canvases during the time they were sent but have since been removed. It will count if a tag is later added to a message that a user received in the past, but before the newest tagged message is sent.

##### Example

Consider the following campaigns and frequency capping by tag rule:

**Campaigns**:

- **Campaign A** is a push campaign tagged as `promotional`. It is slated to send at 9:00 AM on Monday.
- **Campaign B** is a push campaign tagged as `promotional`. It is slated to send at 9:00 AM on Wednesday.

**Frequency Capping by Tag Rule:**

- Your user should receive no more than one push notification Campaign per week with the tag `promotional`.<br><br>

| Action | Result |
|---|---|
| The `promotional` tag is removed from **Campaign A** after your user received the message, but before **Campaign B has sent.** | Your user will receive **Campaign B**.|
| The `promotional` tag is mistakenly removed from **Campaign A** after your user received the message. <br> The tag is added back to **Campaign A** on Tuesday, before **Campaign B** is sent. | Your user will not receive **Campaign B**. |
{: .reset-td-br-1 .reset-td-br-2}

#### Sending at large scales {#sending-at-large-scales}

Frequency capping by tag rules might not be applied properly at large scales, such as 100 messages per channel from campaigns or Canvas components.

For example, if your frequency capping by tag rule is:

> No more than two email campaigns or Canvas components with the tag `Promotional` to a user every week.

And you send the user more than 100 emails from campaigns and Canvas steps with frequency capping turned on over the course of a week, more than two emails may be sent to the user.

Because 100 messages per channel are more messages than most brands send to their users, it's unlikely that you will be impacted by this limitation. To avoid this limitation, you can set a cap for the maximum number of emails you'd like your users to receive over the course of a week.

For example, you might set up the following rule:

> No more than three email campaigns or Canvas components per week from all campaign and Canvas steps.

This rule will ensure that no users receive more than 100 emails per week because, at most, users will receive three emails per week from campaigns or Canvas components with frequency capping turned on.

[11]: {% image_buster /assets/img/global_rules.png %} "global rules"
[12]: {% image_buster /assets/img/tag_rule_fnfn.png %} "rules"
[13]: {% image_buster /assets/img/standard_rules_fnfn.png %} "rules standard"
[1]: {% image_buster /assets/img_archive/rate_limit_daily.png %}
[2]: {% image_buster /assets/img_archive/total_limit.png %}
[3]: {% image_buster /assets/img_archive/per_minute_rate_limit.png %}
[14]: {% image_buster /assets/img_archive/rate_limiting_overview_2.png %}
[15]: {{site.baseurl}}/developer_guide/rest_api/messaging/#messaging
[16]: {{site.baseurl}}/developer_guide/rest_api/api_campaigns/#api-campaigns
[18]: {% image_buster /assets/img_archive/frequencycappingupdate.png %}
[19]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/connected_content_retries/
