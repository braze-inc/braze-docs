---
nav_title: Frequency Capping By Tag
permalink: "/frequency_capping_tag/"
---

# Frequency Capping by Tag

## Frequency Capping Rules

Frequency Capping can be set up for each app group by selecting Global Campaign Settings found underneath the Campaigns tab. From here, you can choose:

- Which message channel you would like to cap (push, email, webhook or any of those three).

- How many times each user should receive Campaign/Canvas step sends from channel within a certain time frame, which can be measured in minutes, days, weeks (7 days) and months.

Each line of frequency caps will be connected using an “AND,” and you’re able to add as many as you wish. In addition, you may include multiple caps for the same message types. For instance, you can cap users to no more than one (1) push per day and no more than 3 pushes per week.

Frequency Capping is applied at the Campaign/Canvas step send level. For example, if you've selected the below as your capping rules:

![rule][3]{: height="70%" width="70%"}

**And the following scenario occurs:**

- A user triggers the same Campaign, Campaign ABC three times during the course of a week
- This user triggers Campaign ABC once on Monday, once on Wednesday and once on Thursday

The expected behavior is that:

- This user will receive the Campaign sends that triggered on Monday and Wednesday
- This user will not receive the third Campaign send on Thursday because the user has already received two push Campaign sends that week

{% alert important %}
You can add up to ten (10) frequency capping rules per app group.
{% endalert %}

## Frequency Capping By Tag

Frequency capping rules can be applied to specific tags.

For example, if you wanted to allow users to receive no more than three (3) push notification Campaigns/ Canvas steps per week from all Campaign/Canvas steps and no more than 2 push notification Campaign/Canvas steps per week with the tag "promotional". When the below rules are applied, users will receive no more than three (3) Campaign sends per week over all Campaigns/Canvas steps and no more than two (2) push notification Campaigns/Canvas steps with the tag "promotional."

![rule][2]{: height="70%" width="70%"}

{% alert important %}
When rules conflict, the most restrictive, applicable frequency capping rule will be applied to your users.
{% endalert %}

 So, if you've added the following rules:

![global][1]{: height="70%" width="70%"}

 The customer will not receive more than one (1) push notification Campaign/Canvas steps with the tag "promotional" in a given week, because you've specified that customers should not receive more than one (1) push notification Campaign/Canvas step from all Campaign/Canvas steps.  In other words, the most restrictive applicable frequency rule is the rule that will be applied to a given user.

{% alert important %}
Canvases are tagged at the Canvas level, so each Canvas Step will inherit all of the Canvas level tags.
{% endalert %}

[1]: {% image_buster /assets/img/global_rules.png %} "global rules"
[2]: {% image_buster /assets/img/tag_rule_fnfn.png %} "rules"
[3]: {% image_buster /assets/img/standard_rules_fnfn.png %} "rules standard"
