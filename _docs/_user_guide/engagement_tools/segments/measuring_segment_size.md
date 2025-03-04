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

Each segment displays the total number of users that are members of that segment. When filtering for **Users from all apps**, it also displays all of the different channels available to communicate with those users, such as web push or email. It is possible that the number of total users is different than the number of users reachable by each channel.

![A table displaying total reachable users broken down by users reachable by email, iOS push, Android push, web push, Kindle push, and Android China push.][3]

For a user to be listed as reachable through a certain channel, the user must have both:
* A valid email address or push token associated with their profile; and
* Opted in or subscribed to your app.

A single user may belong to different reachable user groups. For example, a user might have both a valid email address and valid Android push token and be opted in to both, but have no associated iOS push token. The gap between the total reachable users and the sum of the different channels are the number of users who qualified for the segment but they are not reachable through those communication channels.

## Statistics for segment size

Braze provides the following statistics on segment size. All estimated statistics are within 1% above or below the actual value, and the exact segment membership will always be calculated before a segment is affected by a message sent in a campaign or Canvas.

### Filter statistics

For each filter group, you can view estimated reachable users. Select **Expand extra funnel statistics** to see a breakdown across channels.

![A filter group with a filter for a gender that isn't unknown.][2]{: style="max-width:80%;"}

### Segment statistics

For an entire segment, you can view estimated reachable users, as well as estimated user counts for each channel, at the bottom of the page. You can also view an exact count of reachable users (for both the segment overall and a per channel basis) by selecting **Calculate exact statistics**.

Note that:
- Calculating exact statistics can take a few minutes to run. This function only calculates the exact statistics at the segment level, not at the filter or filter group level.
- For large segments, it is normal to see slight variation even when calculating exact statistics. The accuracy of this feature is expected to be 99.999% or greater.

## Viewing historical segment membership size

For all segments with [advanced analytics tracking]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking/#viewing-revenue-and-purchases-over-time) enabled, you can view a historical membership chart that shows the estimated segment membership for each day. This chart shows how the size of your segment changed over time. Use the dropdown to filter segment membership by date range. Note that this membership chart only begins populating after advance analytics tracking is turned on for that segment, and data does not populate retroactively for dates prior to when tracking gets turned on.

![Use the Historical Membership dropdown to filter segment membership by date range.][1]

Because the goal of this graph is to give you a sense of overall segment membership trends, the daily count is an estimate, similar to how the segment size is an estimate before you select **Calculate Exact Statistics**. 

{% alert note %}
All estimates may be higher or lower than the shown value by approximately 1% of your workspace’s entire population size. Larger workspaces with more users are more likely to have estimates that may differ from exact calculations by a higher numerical amount, even if the difference is still 1% of the workspace’s user population. This means that bigger differences between estimates and exact counts among large workspaces is to be expected.
{% endalert %}

Braze estimates the membership count by querying users in a random bucket range daily at 4 am in your company time zone and extrapolated to estimate the total count. This means that on one day, the membership count could be based on users with a random bucket number of 111–120, and on another day, users with a random bucket number of 8,452–8,455. Therefore, the graph might show slight fluctuations on each date due to different amounts of users landing within the random bucket ranges.

### Reasons for signficant changes

The membership count may significantly change for a number of reasons, such as those in this table.

| Reason | Example |
| --- | --- |
| Normal user behavior | Users subscribe after a particularly successful campaign. |
| Users are imported by CSV | A CSV file of users was imported that significantly increased segment membership. |
| Segment audience criteria is modified | An existing segment's audience rules (such as filters) were changed, causing significant changes in the segment membership. |
| Users are deleted | A signficant number of users were deleted. |
| A partner integration synced with Braze | A third-party sent data to Braze that significantly influenced segment membership. |
| Dormant users are archived | A significant number of inactive profiles were archived. For example, a large number of CSV-imported users never log activity and get archived at the same time. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

[1]: {% image_buster /assets/img_archive/historical_membership2.png %}
[2]: {% image_buster /assets/img_archive/segment_filter_stats.png %}
[3]: {% image_buster /assets/img_archive/segmenter_reachable_users.png %}