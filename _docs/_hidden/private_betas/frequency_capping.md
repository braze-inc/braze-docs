---
nav_title: Frequency Capping By Tag
permalink: "/frequency_capping_tag/"
---

# Updated Frequency Capping Rules

Frequency Capping can be set up for each app group by selecting Global Campaign Settings found underneath the Campaigns tab. From here, you can choose:

- Which [messaging channel](#rules-by-channel) you would like to cap.
- How many times each user should receive Campaign/Canvas step sends from channel within a certain time frame, which can be measured in minutes, days, weeks (7 days) and months.
- Beta users can choose how many times each user should receive Campaign/Canvas step sends by [Tag](#frequency-capping-by-tag) within a certain time frame, which can be measured in minutes, days, weeks (7 days) and months. 

{% alert important %} 
Frequency Capping by Tag is in beta - if you'd like beta access please reach out to your CSM or support@braze.com.
{% endalert %}

Each line of frequency caps will be connected using an “AND,” and you’re able to add as many as you wish. In addition, you may include multiple caps for the same message types. For instance, you can cap users to no more than one (1) push per day and no more than three (3) pushes per week.

Frequency Capping is applied at the Campaign/Canvas step send level.

__For example, if you've selected the below as your capping rules:__

![rule][3]{: height="70%" width="70%"}

**And the following scenario occurs:**

- A user triggers the same Campaign, Campaign ABC three times during the course of a week.
- This user triggers Campaign ABC once on Monday, once on Wednesday and once on Thursday.

__Then, the expected behavior is that:__

- This user will receive the Campaign sends that triggered on Monday and Wednesday.
- This user will not receive the third Campaign send on Thursday because the user has already received two push Campaign sends that week.

{% alert important %}
You can add up to ten (10) frequency capping rules per app group.
{% endalert %}

{% alert update %}
Prior to July 30, 2019, frequency capping was applied at the Campaign level, which meant that receiving the same Campaign twice would only count once towards the frequency capping rule.
{% endalert %}

## Rules by Channel
"Campaigns/Canvas Steps of any type" only apply to emails, webhooks, and push notifications.

Additionally, only emails, webhooks, and push notifications will count towards "Campaigns/Canvas Steps of any type" rules.

In-App Messages and Content Cards are not counted __as__ or __towards__ "Campaigns/Canvas Steps of any type".

{% alert update %}
Prior to July 30, 2019, In-App Messages counted towards "Campaigns/Canvas Steps of any type" rules when they were received but could not be frequency capped. 
{% endalert %}

### Example

Let's say that you set a Frequency Capping rule which asks that your user receive no more than three (3) push notification Campaigns/Canvas steps per week from __all__ Campaign/Canvas steps.

If your user is slated to receive three (3) push notifications, two (2) in-app messages, and one (1) Content Card this week, they will receive all of those messages.

# Frequency Capping by Tag

[Frequency Capping](#updated-frequency-capping-rules) rules can be applied to app groups using specific Tags you have applied to your Campaigns/Canvases, allowing you to, essentially, base your Frequency Capping on custom-named groups.

You can combine regular Frequency Capping with Frequency Capping by Tags, as shown below.

![rule][2]{: height="70%" width="70%"}

The rules above ask that users receive:
1. No more than three (3) push notification Campaigns/Canvas steps per week from __all__ Campaign/Canvas steps, __AND__
2. No more than two (2) push notification Campaign/Canvas steps per week with the tag `promotional`.

As a result, your users will receive no more than three (3) Campaign sends per week over all Campaigns/Canvas steps and no more than two (2) push notification Campaigns/Canvas steps with the tag `promotional`.

{% alert important %}
Canvases are tagged at the Canvas level, as opposed to tagging by Step. So, each Canvas Step will inherit __all__ of the Canvas level tags.
{% endalert %}

### Conflicting Rules

When rules conflict, the most restrictive, applicable frequency capping rule will be applied to your users.

![global][1]{: height="70%" width="70%"}

In this example, your user will not receive more than one (1) push notification Campaign/Canvas steps with the tag "promotional" in a given week, because you've specified that users should not receive more than one (1) push notification Campaign/Canvas step from all Campaign/Canvas steps. In other words, the most restrictive applicable frequency rule is the rule that will be applied to a given user.

### Tag Count
Frequency Capping by Tag rules compute at the time a message sends. This means that Frequency Capping by Tag only counts tags that are currently on the Campaigns/Canvases that a user received in the past. It does not count the tags that were on the Campaigns/Canvases during the time they were sent, but have since been removed. It will count if a Tag is later added to a message that a user received in the past, but before the newest tagged message is sent.

#### Example

Consider the following Campaigns and Frequency Capping by Tag rule:

__Campaigns:__
- __Campaign A__ is a push campaign tagged as `promotional`. It is slated to send at 9:00AM on Monday.
- __Campaign B__ is a push campaign tagged as `promotional`. It is slated to send at 9:00AM on Wednesday.

__Frequency Capping by Tag Rule:__
- Your user should receive no more than one (1) push notification Campaign per week with the tag `promotional`.

| Action | Result |
|---|---|
| The `promotional` tag is removed from __Campaign A__ _after_ your user received the message, but _before_ __Campaign B has sent.__ | Your user will receive __Campaign B__.|
| The `promotional` tag is mistakenly removed from __Campaign A__ after your user received the message. <br> The tag is added back to __Campaign A__ on Tuesday, before __Campaign B__ is sent. | Your user will not receive __Campaign B__. |



[1]: {% image_buster /assets/img/global_rules.png %} "global rules"
[2]: {% image_buster /assets/img/tag_rule_fnfn.png %} "rules"
[3]: {% image_buster /assets/img/standard_rules_fnfn.png %} "rules standard"
