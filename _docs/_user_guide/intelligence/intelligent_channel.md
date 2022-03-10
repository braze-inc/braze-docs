---
nav_title: Intelligent Channel
article_title: Intelligent Channel Filter
page_order: 0
description: "The Intelligent Channel filter selects the portion of your audience for whom the selected messaging channel is their best channel. In this case, best means has the highest likelihood of engagement, given the user's history."

---

# Intelligent Channel filter

> This article describes the Intelligent Channel filter and provides best practices to effectively use this feature. For more on what the Intelligent Channel is, how it works, its benefits, refer to our [Intelligent Channel](https://lab.braze.com/most-engaged-channel) LAB course. 

The Intelligent or `Most Engaged` Channel filter selects the portion of your audience for whom the selected messaging channel is their "best" channel. In this case, "best" means the channel that has the highest likelihood of engagement, given the user's history. You can select email, web push, or mobile push (including any available mobile OS or device) as a channel.

![Intelligent Channel filter][1]{: style="float:right;max-width:50%;margin-left:10px;margin-top:10px;border:0"}

The Intelligent Channel computes the engagement rate for each user for each of the three channels by taking the ratio of message interactions (opens or clicks) to the number of messages received over the last six months of activity. The available channels are ranked according to their respective engagement ratios, and the channel with the highest ratio is the "Most Enagaged" for that user. 

Every time a message is sent to a user, or a user interacts with a message, the Intelligent Channel is recalculated within seconds. Any interaction with a message causes it to be considered "interacted with" only once (e.g., an open and click on the same email will cause that message to be marked as having been engaged with only once, not twice). 

To enable the Intelligent Channel filter, select the **Intelligent Channel** filter on the **Target Users** page when creating a email, web push, or mobile push campaign.

## The "Not enough data" option

For Braze to determine which channel is "best", there needs to be adequate data. This means that a user must have received at least three or more messages across at least two of the three available channels. The messages do not necessarily need to have been opened. 

If users haven't received enough messages across the channels, those users will fall into the "Not Enough Data" option of this filter. This allows you to use any of the three available messaging channels to target these users.

For example, suppose you want users who prefer push messages to receive a push and users who don't have enough data to receive the same push message. In that case, you could set the Intelligent Channel filter to **Mobile** and use **OR** to add a second Intelligent Channel filter set to **Not Enough Data**. A separate campaign with the Intelligent Channel filter set to email could address users who prefer email.<br>![Intelligent Channel example][2]

{% alert note %}
Campaigns and Canvas Steps that ignore [Frequency Capping]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#delivery-rules) will not be accounted for by Intelligent Channel and cannot contribute to the data requirements above.
{% endalert %}

## The "Mobile push" option

Mobile push incorporates Android, iOS, Windows, Kindle, and other mobile device channels available on Braze. When computing the Intelligent Channel, Braze looks at each kind of mobile device separately and then chooses the highest engagement rate among them to represent the "Mobile Push" category when comparing against email and Web push. 

For example, if a user has several mobile devices, their mobile engagement rate would be represented by the highest rate exhibited across the devices. This would not, however, force the user to receive push notifications exclusively on that device. This rate is only used when comparing rates against email and web push.

## Best practices and effective use strategy

### Tie-breaking

Because some users will have low numbers of messages received, it is not unusual to have "ties" in engagement rates across the available channels for a given user (i.e., a single user has a 0.2 engagement rate for **both** email and mobile push). In such cases, ties will be broken by prioritizing (giving a higher ranking to) the channel with the most recent open events.

### Unreachable channels

When the user has sufficient data for a ranking to be determined but becomes unreachable on their "Intelligent Channel", the user will "fall out" and not receive any messages. Users who are unreachable on specific channels should be targeted separately.

### Audience sizing

Intelligent Channel allows you to selectively target in advance the fraction of users who have a much higher likelihood of engaging with a message than the rest of your audience. This is not likely to represent a majority of users in a typical audience. Rather, you can expect this filter to find the 5-20% from your usual audience who have an established record of engaging on a particular channel.


[1]: {% image_buster /assets/img/intelligent_channel_filter.png %} "Intelligent Channel Filter"
[2]: {% image_buster /assets/img/intelligent_example.png %}