---
nav_title: Rate-Limiting and Frequency Capping
platform:
  - iOS
  - Android
  - Web
subplatform: Testing and More
page_order: 1
tool:
  - Campaigns
  - Canvas
  - Segments
page_type: reference
description: "This reference article discusses the concept of rate limiting and frequency capping, and how you can apply marketing pressure to improve user experience."
---

# Rate-Limiting and Frequency Capping

> This reference article discusses the concept of rate limiting and frequency capping, and how you can apply that marketing pressure to improve user experience.
> <br>
> <br>
> We all want our users to have the best experience possible, with rate limiting and frequency capping, you can make sure your users are getting the message they need to, and none of the ones they don't.

## Rate-Limiting

Braze allows you to control marketing pressure by implementing two different types of rate limiting for your campaigns. The first focuses on providing the best experience for the end user, while the second takes into consideration the bandwidth of your servers.

### User Centric Rate-Limiting

As you create more segments, there are going to be cases where the membership of those segments overlaps. If you're sending out campaigns to those segments, you want to be sure that you are not messaging your users too often. If a user receives too many messages within a short time period, they will feel over-encumbered and either turn off push notifications or uninstall your app.

#### Relevant Segment Filters
Braze provides the following filters in order to help you limit the rate at which your users receive messages:

- Last Engaged With Message
- Last Received Any Message
- Last Received Push Campaign
- Last Received Email Campaign
- Last Received SMS
- Last Viewed News Feed

#### Implementing Filters
Consider the following example segment:

![Rate_Limit_Example][1]

This is a standard re-engagement segment. If you have other more targeted segments receiving notifications recently, you may not want your users to be targeted by more generic campaigns directed at this segment. Appending the "Last Received Push Campaign" filter to this segment, the user has ensured that if they've received another notification in the past 24 hours, they will slide out of this campaign for the next 24 hours. If they still meet the other criteria of the segment 24 hours later and haven't received any more notifications they will slide back into the segment.

Appending this filter to all segments targeted by campaigns would cause your users to receive a maximum of one push every 24 hours. You could then prioritize your messaging by ensuring that your most important messages are delivered before less important messages.


#### Setting a Max User Cap
Additionally, in the 'Target Users' section of your campaign composition, you can limit the total number of users that will receive your message. This feature serves as a check that is independent of your campaign filters, allowing you to freely segment users without needing to worry about over-spamming.

![Total Limit Example][2]

By using the max user cap checkbox, you'll be able to limit the rate at which your users receive notifications on a per-channel basis or globally across all message types.

#### Setting a Max Impression Cap

For in-app messages, you can control marketing pressure by setting a maximum number of impressions that will be displayed to your user base, after which Braze will not send down more messages to your users. However, it is important to note that this cap is not exact. New in-app message rules are sent down to an app on session start, meaning that Braze can send an in-app message down to the user before the cap is hit, but by the time the user triggers the message, the cap has now been hit. In this situation, the device will still display the message.

For example, let's say you have a game with an in-app message that triggers when a user beats a level, and you cap it at 100 impressions. There have been 99 impressions so far. Alice and Bob both open the game and Braze tells their devices that they are eligible to receive the message when they beat a level. Alice beats a level first and gets the message. Bob beats the level next, but since his device has not communicated with Braze's servers since his session start, his device is unaware that the message has met its cap and he will also receive the message. However, once an impression cap has been hit, the next time any device requests the list of eligible in-app messages, that message will not be sent down and will be removed from that device.

### Delivery Speed Rate-Limiting

If you anticipate large campaigns driving a spike in user activity and overloading your servers, you may specify a per-minute rate limit for sending messages. While targeting users during campaign creation, you can navigate to Advanced Options to select a rate limit (in various increments from as low as 50 to as high as 500K messages per minute). Note that non-rate-limited campaigns may exceed these delivery limits. Be aware, however, that messages will be aborted if they are delayed 72 hours or more due to a low rate limit. The user who created the campaign will receive alerts in the dashboard and via email if the rate limit is too low.

![Per Minute Rate Limit Example][3]

For instance, if you are trying to send out 75K messages with a 10K per minute rate limit, the delivery will be spread out over 8 minutes. Your campaign will deliver 10k for each of the first 7 minutes, and 5K over the last minute. Be wary of delaying time-sensitive messages, however, with this form of rate limiting. If the segment contains 30M users but we set the rate limit to 10K per minute, a large portion of the user base won't receive the message until the following day.

{% alert important %}
When sending a multichannel campaign with a speed rate limit, each channel is sent independently of the others. The effect is that users could receive the different channels at different times, and it is not predictable which channel they will get first. For example, if you send a campaign that contains an email and a push notification, you may have 10K users with valid push tokens but 50K users with valid email addresses. If you set the campaign to send 100 messages per minute (a slow rate limit for the campaign size), a user could receive the push notification in the first batch of sends and the email in the last batch of sends, almost 9 hours later.
{% endalert %}

#### Rate Limiting and Connected Content Retries
When the [Connected Content Retry][19] feature is enabled, Braze will retry call failures while respecting the rate limit you set for each resend. Let’s think again about the 75K messages with a 10K per minute rate limit. In the first minute, the call fails or is slow and only sends 4K messages.

Instead of attempting to make up for the delay and send the remaining 4K messages in the second minute or add it to the 10K it is already set to send, Braze will move those 6K failed messages to the "back of the queue" and add an additional minute, if necessary, to the total minutes it would take to send your message.

|Minute|No Failure|6K Failure in Minute 1|
|---|---|---|
|1|10K|4K|
|2|10K|10K|
|3|10K|10K|
|4|10K|10K|
|5|10K|10K|
|6|10K|10K|
|7|10K|10K|
|8|5K|10K|
|9|0K|6K|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

#### Multi-Channel Campaigns
Keep in mind that the per-minute rate limit is adjusted on a per-campaign basis. If multiple channels are utilized within a campaign, the rate limit will apply to each of those channels. If your campaign utilizes email and in-app banners with a rate limit of 10K per minute, we will send 20K total messages each minute (10K email, 10K push).

#### Multi-Platform Push Campaigns
For push campaigns delivering on multiple platforms, the rate limit selected will be equally distributed across platforms. A push campaign leveraging Android, iOS, and Windows with a 10K rate-limit per minute will equally distribute the 10K messages across the 3 platforms.

## Frequency Capping

As your user base continues to grow and your messaging scales to include life cycle, triggered, transactional, and conversion campaigns, it’s important to prevent your notifications from appearing spammy or disruptive. By granting greater control over your users’ experience, Frequency Capping enables you to create the campaigns you desire without overwhelming your audience.

### Feature Overview {#freq-cap-feat-over}

Frequency Capping is applied at the campaign or Canvas step send level and can be set up for each app group by selecting __Global Message Settings__ found underneath the **Engagement** tab. From here, you can choose:

- Which messaging channel you would like to cap: push, email, SMS, webhook, or any of those four.
- How many times each user should receive a campaign or Canvas step sends from a channel within a certain time frame, which can be measured in minutes, days, weeks (7 days), and months.
- Users can choose how many times each user should receive a campaign or Canvas step sends by [Tag](#frequency-capping-by-tag) within a certain time frame, which can be measured in minutes, days, weeks (7 days), and months. 

Each line of frequency caps will be connected using an “AND,” and you’re able to add up to ten (10) rules per app group. In addition, you may include multiple caps for the same message types. For instance, you can cap users to no more than one (1) push per day and no more than three (3) pushes per week.

![Frequency Capping][14]

### Delivery Rules

There may be some campaigns - transactional messages, in particular - that you wish to always reach the user, even if they have already reached their frequency cap. For example, a delivery app may wish to send an email or push when an item is delivered regardless of how many campaigns the user has received.

If you want a particular campaign to override Frequency Capping rules, you can set this up in the Braze dashboard when scheduling that campaign's delivery by toggling Frequency Capping to "Off". After this, you will be asked if you still want this campaign to count towards your Frequency Cap. Messages that count towards frequency capping are included in calculations for the Intelligent Channel filter. When sending [API campaigns][15], which are often transactional, you'll have the ability to specify that a campaign should ignore Frequency Capping rules [within the API request][16] by setting "override_messaging_limits" to "true."

By default, new campaigns and Canvases that do not obey Frequency Caps will also not count towards them. This is configurable for each campaign and Canvas.

{% alert note %}
Please note that this behavior changes the default behavior when you turn off Frequency Capping for a campaign or Canvas; the changes are backward compatible and do not impact messages that are currently live right now.
{% endalert %}

![Frequency Capping Update][18]

Different channels within a multichannel campaign will individually count towards the frequency cap. For instance, if you create a multichannel campaign with, say, both push and email, and have Frequency Capping set up for both of those channels, then the push will count toward 1 push campaign and the email message will count toward 1 email message campaign. The campaign will also count toward 1 "campaign of any type." If users are capped to 1 push and 1 email campaign per day and someone receives this multichannel campaign, then she will no longer be eligible for push or email campaigns for the rest of the day (unless a campaign ignores Frequency Capping rules).

In-app messages and Content Cards are __not__ counted as or towards caps on campaigns or Canvas steps of any type.

{% alert important %}
Please note that global frequency capping is based in the user's time zone, and are based on calendar days, not 24-hour periods. For example, if I set up a frequency capping rule of sending no more than 1 campaign a day, a user may receive a message at 11 pm in their local time zone, and they would be eligible to receive another message an hour later.
{% endalert %}

#### Examples
{% tabs %}
{% tab Example 1 %}

Let's say that you set a Frequency Capping rule which asks that your user receive no more than three (3) push notification campaigns or Canvas steps per week from __all__ campaign or Canvas steps.

If your user is slated to receive three (3) push notifications, two (2) in-app messages, and one (1) Content Card this week, they will receive all of those messages.

{% endtab %}
{% tab Example 2 %}

Using the following frequency capping rules:

![rule]({% image_buster /assets/img/standard_rules_fnfn.png %})

**And the following scenario occurs:**

- A user triggers the same campaign, Campaign ABC three times over the course of a week.
- This user triggers Campaign ABC once on Monday, once on Wednesday, and once on Thursday.

__Then, the expected behavior is that:__

- This user will receive the campaign sends that triggered on Monday and Wednesday.
- This user will not receive the third campaign send on Thursday because the user has already received two push campaign sends that week.

{% endtab %}
{% endtabs %}

### Frequency Capping by Tag

[Frequency Capping](#updated-frequency-capping-rules) rules can be applied to app groups using specific Tags you have applied to your Campaigns/Canvases, allowing you to, essentially, base your Frequency Capping on custom-named groups.

You can combine regular Frequency Capping with Frequency Capping by Tags, as shown below.

![rule][12]

The rules above ask that users receive:
1. No more than three (3) push notification campaigns or Canvas steps per week from __all__ campaign and Canvas steps, __AND__
2. No more than two (2) push notification campaign or Canvas steps per week with the tag `promotional`.

As a result, your users will receive no more than three (3) campaign sends per week over all campaigns and Canvas steps and no more than two (2) push notification campaigns or Canvas steps with the tag `promotional`.

{% alert important %}
Canvases are tagged at the Canvas level, as opposed to tagging by Step. So, each Canvas Step will inherit __all__ of the Canvas level tags.
{% endalert %}

#### Conflicting Rules

When rules conflict, the most restrictive, applicable frequency capping rule will be applied to your users.

![global][11]

In this example, your user will not receive more than one (1) push notification campaign or Canvas steps with the tag "promotional" in a given week, because you've specified that users should not receive more than one (1) push notification campaign or Canvas step from all campaigns and Canvas steps. In other words, the most restrictive applicable frequency rule is the rule that will be applied to a given user.

#### Tag Count
Frequency Capping by Tag rules compute at the time a message sends. This means that Frequency Capping by Tag only counts tags that are currently on the campaigns or Canvases that a user received in the past. It does not count the tags that were on the campaigns or Canvases during the time they were sent but have since been removed. It will count if a Tag is later added to a message that a user received in the past, but before the newest tagged message is sent.

##### Example

Consider the following campaigns and Frequency Capping by Tag rule:

__Campaigns:__
- __Campaign A__ is a push campaign tagged as `promotional`. It is slated to send at 9:00 AM on Monday.
- __Campaign B__ is a push campaign tagged as `promotional`. It is slated to send at 9:00 AM on Wednesday.

__Frequency Capping by Tag Rule:__
- Your user should receive no more than one (1) push notification Campaign per week with the tag `promotional`.<br><br>

| Action | Result |
|---|---|
| The `promotional` tag is removed from __Campaign A__ _after_ your user received the message, but _before_ __Campaign B has sent.__ | Your user will receive __Campaign B__.|
| The `promotional` tag is mistakenly removed from __Campaign A__ after your user received the message. <br> The tag is added back to __Campaign A__ on Tuesday, before __Campaign B__ is sent. | Your user will not receive __Campaign B__. |
{: .reset-td-br-1 .reset-td-br-2}

#### Sending at Large Scales
 
If you send __more than one hundred (100) messages per channel__ from campaigns or Canvas Steps with frequency capping turned on to a specific user over the duration of your frequency capping by tag rule (for example, over 1 week), the frequency capping by tag rule may not always be applied properly. 

For example, if your frequency capping by tag rule is: 

> No more than two (2) email campaigns or Canvas Steps with the tag `Promotional` to a user every week.

And you send the user more than one hundred (100) emails from campaigns and Canvas Steps with frequency capping turned on over the course of a week, more than two emails may be sent to the user. 

Because 100 messages per channel are more messages than most brands send to their users, it's unlikely that you will be impacted by this limitation. To avoid this limitation, you can simply set a cap for the maximum number of emails you'd like your users to receive over the course of a week. 

For example, you might set up the following rule: 

> No more than three (3) email campaigns or Canvas steps per week from __all__ campaign and Canvas Steps.

This rule will ensure that no users receive more than 100 emails per week because, at most, users will receive 3 emails per week from campaigns or Canvas Steps with frequency capping turned on.



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
