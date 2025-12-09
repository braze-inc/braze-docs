---
nav_title: Measuring segment size
article_title: Measuring Segment Size
page_order: 5
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

![A table displaying total reachable users broken down by users reachable by email, iOS push, Android push, web push, and Kindle push.]({% image_buster /assets/img_archive/segmenter_reachable_users.png %})

For a user to be listed as reachable through a certain channel, the user must have both:
* A valid email address or push token associated with their profile, and
* Opted-in or subscribed to your app.

A single user may belong to different reachable user groups. For example, a user might have both a valid email address and valid Android push token and be opted in to both, but have no associated iOS push token. The gap between the total reachable users and the sum of the different channels are the number of users who qualified for the segment but they are not reachable through those communication channels.

## Statistics for segment size

Estimated statistics are approximated by sampling only a portion of your segment, so you should expect to see estimated sizes that are larger or smaller than the actual value, with larger workspaces seeing potentially larger margins of error. To get an accurate count of users in your segment, select **Calculate Exact Statistics**. The exact segment membership will always be calculated before a segment is affected by a message sent in a campaign or Canvas. 

Braze provides the following statistics on segment size. 

### Filter statistics

For each filter group, you can view estimated reachable users. Select **Expand extra funnel statistics** to see a breakdown across channels.

![A filter group with a filter for users who had exactly one session count.]({% image_buster /assets/img_archive/segment_filter_stats.png %}){: style="max-width:80%;"}

## Reachable users estimate

You can view an entire segment's estimated reachable users, including estimated user counts for each channel, in the **Reachable users** side panel. This **estimation** shows you an approximate range for your segment size, and an estimate of what percentage of your overall user base falls into this segment. Note that estimated statistics are cached for 15 minutes unless you make edits to your segment, in which case estimated statistics will automatically update. You can also view an exact count of reachable users (for both the segment overall and per channel) by selecting **Calculate exact statistics**. 


![The "Reachable users" panel stating there are 2.3M—2.4M estimated users.]({% image_buster /assets/img_archive/reachable_users_side_panel.png %})

### Considerations for estimate counts

Braze measures the number of estimated users by querying a subset of your users, and then extrapolates those results to your entire audience. Because the subset of users that Braze queries may differ each time we calculate this estimate, the estimate may also change in cases where your audience membership technically should have stayed the same. For example, if you re-order your filters or re-check the same segment at a different time, it’s possible that the estimated count changes (even though **Calculate exact stats** would reveal the same results if your segment didn't change).

If you have a large user population in your workspace, you may see more variation between your estimated counts compared to your exact calculation counts, especially in cases where your segment is a very small percentage of your overall workspace population. This is because Braze measures the estimate by querying a subset of your users and extrapolating the results to your entire user base. For larger user bases, larger differences between estimated and exact counts are to be expected.

Very small segments will have an estimated range that includes 0, meaning the percentage of total users may round to 0. In these cases, **Calculate exact stats** will help you see an accurate count of your segment size, which may not actually be 0.

![The "Reachable users" side panel.]({% image_buster /assets/img_archive/reachable_users_panel.png %})

### Reachable users by channel

To view the number of users that are reachable for each message channel, select **Show breakdown** in the **Reachable users** panel. This displays some of the most frequently used messaging channels (such as web push or email) and the number of reachable users for those specific channels. 

The _Total_ metric represents unique users. For example, if a user has both Android push and iOS push, they will get counted for both of those rows, but will only count as 1 user in the _Total_ row.

However, it's possible that the number of total users is different than the sum of users reachable by each channel, as a single user may belong to different reachable user groups. For example, a user might have both a valid email address and valid Android push token and be opted in to both, but have no associated iOS push token. 

Keep in mind, not all channels are listed in the **Reachable users** table (such as Content Cards, webhooks, and WhatsApp). For example, if you have users only reachable through Whatsapp, they will be reflected in the _Total_ but not in any of the channel-specific rows. This means that the total reachable users count can be different from the sum of the users for each displayed channel.

In cases where the _Total_ is higher than the sum of the channels, the gap represents the number of users who qualified for the segment but aren't reachable through those communication channels.

For a user to be listed as reachable through a certain channel, the user must have:
- A valid email address or push token associated with their profile, and
- Opted-in or subscribed to your app.

#### Applied filters for channel-specific reachable users

The following filters are applied for each channel when determining reachable users.

| Channel | Filter |
| --- | --- |
| Email | **Email Available** is true. |
| Push | **Foreground Push Enabled** is true. |
| SMS | **Subscription Group** is any SMS subscription group. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Calculating exact statistics 

To view an accurate count of the number of users in your segment, select **Calculate exact stats** in the **Reachable users** pane.

To update the stats for a calculation you've previously run, select **Refresh exact statistics**. The date this calculation was last ran will automatically be updated.

Note that a calculation's accuracy is only 99.999% or greater. So for large segments, you may notice slight variations&#8212;even when calculating exact statistics&#8212;which is normal behavior. In addition, exact statistics results are cached for 24 hours unless you make edits to your segment, in which case you can re-calculate the exact statistics.

{% alert note %}
Segments divided evenly by [random bucket numbers]({{site.baseurl}}/user_guide/engagement_tools/testing/random_bucket_numbers/) won't be the same size. For example, if you create one segment with the filter **Random Bucket # less than 5000** and one segment with the filter **Random Bucket # at least 5000**, it is possible and expected for the segment sizes to vary by up to a few percentage points. This is because of situations such as inactive users getting deleted and users being unreachable.
{% endalert %}

![The "Reachable users" panel with an option to show the breakdown.]({% image_buster /assets/img_archive/reachable_users_breakdown.png %})

The statistics on a per-filter level will always be estimated, even if you calculate exact stats. **Calculate exact stats** only calculates the exact statistics at the segment level, not at the filter or filter group level. This calculation may take a few minutes to run. Larger workspaces in particular may require longer periods to complete calculations. You can track your progress on the progress bar in the **Reachable users** panel. When a calculation is expected to run more than five minutes, Braze will email you the results. 

Braze prioritizes one calculation at a time per workspace, so running multiple calculations at once will cause delays. You can select **View calculation queue** to see what segments are ahead of yours, their progress, and their initiator, and get an idea of when your calculation may be prioritized.

![A calculation queue with one calculation.]({% image_buster /assets/img_archive/calculation_queue.png %})

You can cancel an exact statistics calculation by selecting **Cancel**. This can be beneficial if there are multiple calculations in the queue and you want to prioritize another calculation first. 

![An active calculation with the option to cancel]({% image_buster /assets/img_archive/cancel_calculation.png %}){: style="max-width:25%"}

## Viewing historical segment membership size

For all segments, you can view a historical membership chart that shows the estimated segment membership for each day. This chart shows how the size of your segment changed over time. Use the dropdown to filter segment membership by date range.

![Use the Historical Membership dropdown to filter segment membership by date range.]({% image_buster /assets/img_archive/historical_membership2.png %})

Because the goal of this chart is to give you a sense of overall segment membership trends, the daily count is an estimate, similar to how the segment size is an estimate before you select **Calculate Exact Statistics**. And because this graph shows estimates, it's possible that your segment’s size appears as "0" in this chart, even though its actual size (which can be determined after selecting **Calculate Exact Stats**) is not "0". It is especially likely for the chart to show an estimate of "0" if your segment is very small relative to the size of your workspace population.

For example, let's say your workspace contains 100 million users and your segment has about 700 users. It's possible that on some days, no users are in the segment, and no users land in the random bucket range used for the historical membership estimate, resulting in a one-day membership count of 0.

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
