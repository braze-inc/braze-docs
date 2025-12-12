---
nav_title: Channel filter
article_title: Intelligent Channel Filter
page_order: 1.5
description: "This article cover the The Intelligent Channel filter, a filter that selects the portion of your audience for whom the selected messaging channel is their best channel. In this case, best means has the highest likelihood of engagement, given the user's history."
search_rank: 11
---

# [![Braze Learning course]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/most-engaged-channel){: style="float:right;width:120px;border:0;" class="noimgborder"}Intelligent Channel filter

> The `Intelligent Channel` filter (previously `Most Engaged`) selects the portion of your audience for whom the selected messaging channel is their "best" channel. 

## About the Channel Filter

![The Intelligent Channel filter with a dropdown for the different channels that can be selected.]({% image_buster /assets/img/intelligent_channel_filter.png %}){: style="float:right;max-width:40%;margin-left:10px;margin-top:10px;border:0"}

In this case, best means the channel that has the highest likelihood of engagement, given the user's history. You can select email, SMS, WhatsApp, web push, or mobile push (including any available mobile OS or device) as a channel.

The Intelligent Channel computes the engagement rate for each user for each of the available channels by taking the ratio of message interactions (opens or clicks) to the number of messages received over the last six months of activity. The available channels are ranked according to their respective engagement ratios, and the channel with the highest ratio is the "Most Engaged" for that user. 

Every time a message is sent to a user, or a user interacts with a message, the engagement ratio is recalculated within seconds. A user can only be counted as interacting with a message once (for example, an open and click on the same email will cause that message to be marked as having been engaged with only once, not twice). 

To enable the Intelligent Channel filter, select the **Intelligent Channel** filter on the **Target Audiences** page when creating a email, web push, or mobile push campaign.

{% alert important %}
To compute the engagement rate of the SMS channel, turn on [SMS link shortening]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/link_shortening/#overview/) with advanced tracking and click tracking. Without this tracking, SMS may be selected as the Intelligent Channel for a 0% engagement rate because of our [tie-breaking behavior]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_channel/#tie-breaking).
{% endalert %}

## The "Not enough data" option

For Braze to determine which channel is "best", there needs to be enough data. This means that a user must have received at least three or more messages per channel across at least two of the three available channels. The messages don't necessarily need to have been opened. 

If users haven't received enough messages across the channels, those users will fall into the "Not Enough Data" option of this filter. This allows you to use any of the three available messaging channels to target these users.

For example, let's say you want users who prefer push messages to receive a push and users who don't have enough data to receive the same push message. In that case, you could set the Intelligent Channel filter to **Mobile push** and use **OR** to add a second Intelligent Channel filter set to **Not Enough Data**. A separate campaign with the Intelligent Channel filter set to email could address users who prefer email.

![Intelligent Channel filters for mobile push or not enough data.]({% image_buster /assets/img/intelligent_example.png %}){:style="border:none"}

{% alert note %}
Campaigns and Canvas Steps that ignore [frequency capping]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#delivery-rules) will not be accounted for by Intelligent Channel and cannot contribute to the data requirements.
{% endalert %}

## The "Mobile push" option

Mobile push incorporates Android, iOS, Kindle, and other mobile device channels available on Braze. When calculating the Intelligent Channel, Braze looks at each kind of mobile device separately and then chooses the highest engagement rate among them to represent the "Mobile Push" category when comparing against email and Web push. 

For example, if a user has several mobile devices, their mobile engagement rate would be represented by the highest rate exhibited across the devices. This would not, however, force the user to receive push notifications exclusively on that device. This rate is only used when comparing rates against email and web push.

## Individual channels

Rather than let Braze choose the single best channel for a user, you may also want to simply filter users based on whether or not they're likely to open a message on a specific channel you choose. For that you can use the Message Open Likelihood filter in [Segmentation filters]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#message-open-likelihood).

## Best practices and effective use strategy

### Tie-breaking

Because some users will have low numbers of messages received, it's not unusual to have ties in engagement rates across the available channels for a given user (such as a single user has a 0.2 engagement rate for **both** email and mobile push). In such cases, ties will be broken by prioritizing (giving a higher ranking to) the channel with the most recent open events.

### Unreachable channels

When the user has sufficient data for a ranking to be determined but becomes unreachable on their most engaged channel, the user will "fall out" and not receive any messages. Users who are unreachable on specific channels should be targeted separately.

### Audience sizing

Intelligent Channel allows you to selectively target in advance the fraction of users who have a much higher likelihood of engaging with a message than the rest of your audience. This is not likely to represent a majority of users in a typical audience. Rather, you can expect this filter to find the 5-20% from your usual audience who have an established record of engaging on a particular channel.


