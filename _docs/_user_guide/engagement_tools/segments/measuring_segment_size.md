---
nav_title: Measuring Segment Size
article_title: Measuring Segment Size
page_order: 9
page_type: reference
tool: 
- Segments
description: "This page covers how you can monitor your segment’s membership and size."
---

# Measuring segment size

> This page covers how you can monitor your segment’s membership and size.

## Segment membership calculation

Braze updates the user's segment membership as data is sent back to our servers and processed, typically instantaneously. A user's segment membership will not change until that session has been processed. For example, a user who falls into a lapsed user segment when the session first starts will be immediately moved out of the lapsed user segment when the session is processed.

### Total reachable users calculation

Each segment displays the total number of users that are members of that segment. When filtering for **Users from all apps**, it also displays some of the most frequently used messaging channels (such as web push or email) and the number of reachable users for those specific channels. 

It is possible that the number of total users is different than the number of users reachable by each channel. In addition, not all channels are listed in the reachable users table. For example, Content Cards, webhooks, and WhatsApp aren't shown in the breakdown. This means that the total reachable users count could be greater than the sum of the users for each displayed channel.

![A table displaying total reachable users broken down by users reachable by email, iOS push, Android push, web push, Kindle push, and Android China push.][3]

For a user to be listed as reachable through a certain channel, the user must have both:
* A valid email address or push token associated with their profile; and
* Opted in or subscribed to your app.

A single user may belong to different reachable user groups. For example, a user might have both a valid email address and valid Android push token and be opted in to both, but have no associated iOS push token. The gap between the total reachable users and the sum of the different channels are the number of users who qualified for the segment but they are not reachable through those communication channels.

## Statistics for segment size

Estimated statistics are approximated by sampling only a portion of your segment, so you should expect to see estimated sizes that are larger or smaller than the actual value, with larger workspaces seeing potentially larger margins of error. To get an accurate count of users in your segment, select **Calculate Exact Statistics**. The exact segment membership will always be calculated before a segment is affected by a message sent in a campaign or Canvas.

Braze provides the following statistics on segment size. 

### Filter statistics

For each filter group, you can view estimated reachable users. Select **Expand extra funnel statistics** to see a breakdown across channels.

![A filter group with a filter for users who had exactly one session count.][2]{: style="max-width:80%;"}

### Segment statistics

For an entire segment, you can view estimated reachable users, as well as estimated user counts for each channel, at the bottom of the page. You can also view an exact count of reachable users (for both the segment overall and a per channel basis) by selecting **Calculate exact statistics**.

Note that:
- Calculating exact statistics can take a few minutes to run. This function only calculates the exact statistics at the segment level, not at the filter or filter group level.
- For large segments, it is normal to see slight variation even when calculating exact statistics. The accuracy of this feature is expected to be 99.999% or greater.

## Viewing historical segment membership size

For all segments, you can view a historical membership chart that shows the estimated segment membership for each day. This chart shows how the size of your segment changed over time. Use the dropdown to filter segment membership by date range.

![Use the Historical Membership dropdown to filter segment membership by date range.][1]

Because the goal of this chart is to give you a sense of overall segment membership trends, the daily count is an estimate, similar to how the segment size is an estimate before you select **Calculate Exact Statistics**. And because this graph shows estimates, it's possible that your segment’s size appears as "0" in this chart, even though its actual size (which can be determined after selecting **Calculate Exact Stats**) is not "0". It is especially likely for the chart to show an estimate of "0" if your segment is very small relative to the size of your workspace population.

Braze estimates the segment membership count by querying a subset of your users, and then extrapolating those results to your entire audience. This means that the chart's results provide only an estimate of what segment membership might be on that day, and is expected to also fluctuate from day-to-day because a different sample of users may get queried for this estimate each day.

{% alert note %}
All estimates may be higher or lower than the shown value by approximately 1% of your workspace’s entire population size. Larger workspaces with more users are more likely to have estimates that may differ from exact calculations by a higher numerical amount, even if the difference is still 1% of the workspace’s user population. This means that bigger differences between estimates and exact counts among large workspaces are to be expected.
{% endalert %}

### Reasons for significant changes

The membership count may significantly change for a number of reasons, such as those in this table.

| Reason | Example |
| --- | --- |
| Normal user behavior | Users subscribe after a particularly successful campaign. |
| Users are imported by CSV | A CSV file of users was imported that significantly increased segment membership. |
| Segment audience criteria is modified | An existing segment's audience rules (such as filters) were changed, causing significant changes in the segment membership. |
| Users are deleted | A significant number of users were deleted. |
| A partner integration synced with Braze | A third party sent data to Braze that significantly influenced segment membership. |
| Dormant users are archived | A significant number of inactive profiles were archived. For example, a large number of CSV-imported users never log activity and get archived at the same time. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

[1]: {% image_buster /assets/img_archive/historical_membership2.png %}
[2]: {% image_buster /assets/img_archive/segment_filter_stats.png %}
[3]: {% image_buster /assets/img_archive/segmenter_reachable_users.png %}