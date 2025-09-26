---
nav_title: Segment data
article_title: Viewing and Understanding Segment Data
page_order: 4
page_type: reference
description: "This page explains the segments section of your Braze dashboard, and includes a summary of the statistics provided."
alias: /viewing_and_understanding_segment_data/
tool: 
  - Segments
  - Reports
  
---
# Segment data

> This page explains the segments section of your Braze dashboard, and includes a summary of the statistics provided.

## Accessing data about your segments and membership

The **Segments** page of your Braze dashboard contains a summary of all of your segments and allows you to examine detailed data for each one. On this page, search for and select the name of a segment to edit and view its data. To learn how to create a segment, check out [Creating a Segment]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#creating-a-segment).

![Segments page]({% image_buster /assets/img_archive/segments.png %})

After selecting the name of a segment, you can view segment statistics and filters, and edit the segment by adding or deleting filters. Be sure to save any changes!

When you turn on [analytics tracking for a segment]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking/), you can view sessions, custom events, and revenue over time for this segment.

![Analytics tracking toggle for a segment]({% image_buster /assets/img_archive/A_Tracking_2.png %})

### Segment statistics

You can view the following segment statistics, which update in real-time as you add or delete filters:

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>Statistic</th>
            <th>Definition</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split">Total Users</td>
            <td class="no-split">How many users your app has in total.</td>
        </tr>
        <tr>
            <td class="no-split">Selected Users</td>
            <td class="no-split">How many users are in your segment and what percentage of your total user base they are.</td>
        </tr>
        <tr>
            <td class="no-split">LTV (Paying Users)</td>
            <td class="no-split">The lifetime value per user (LTV) in this segment and the lifetime value per paying user in this segment. The LTV is calculated by dividing your lifetime revenue by lifetime users.</td>
        </tr>
        <tr>
            <td class="no-split">Emailable (Opted-In)</td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Emailable' %} Due to <a href="/docs/help/best_practices/spam_regulations/#spam-regulationsspam regulations">spam regulations</a> it's a good idea to ask your users to explicitly opt-in by implementing a double opt-in policy where users must click a link in an initial confirmation email. To encourage more users to opt-in, you can target a message at <a href="/docs/user_guide/message_building_by_channel/email/managing_user_subscriptions/#segmenting-by-user-subscriptions">those who have neither opted in nor out</a>.</td>
        </tr>
        <tr>
            <td class="no-split">Push Enabled (Opted-In)</td>
            <td class="no-split">Push enabled refers to the number of users with at least one push token. Some users may have multiple push tokens (for example, if they own an iPhone and iPad), so the number of push notifications you send to this segment may be greater than the number of "push enabled" users. "Opted In" refers to the number of users who have explicitly opted in to push notifications. Users must always explicitly opt-in for you to send them pushes.</td>
        </tr>
    </tbody>
</table>

### Segment Insights

You can see how one segment is performing compared to another across a set of pre-selected KPIs by visiting the [Segment Insights]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_insights/) page of your dashboard.

### Messaging use
The **Messaging Use** section shows which segments, currently enabled campaigns, and currently enabled canvases are targeting your segment.

### Historical membership

The **Historical Membership** section shows how the size of your segment changed over time. Use the dropdown to filter segment membership by date range.

To learn more about monitoring your segment’s membership and size, refer to [Measuring segment size]({{site.baseurl}}/user_guide/engagement_tools/segments/measuring_segment_size/).

### User preview

To view detailed, user-specific information about your segments, click **User Data** and select **User Preview**.

On this page, you can view a number of user-specific attributes, such as gender, age, number of sessions, and whether they have opted into push and email.

Note that in cases where your segment is very small relative to your workspace size, it's possible for the User Preview to return zero users. This doesn't necessarily mean that there are zero users in your segment; run [Calculate Exact Stats]({{site.baseurl}}/user_guide/engagement_tools/segments/measuring_segment_size/#statistics-for-segment-size) to determine your segment's exact size.

![User Preview]({% image_buster /assets/img_archive/user_preview.png %})

## Viewing performance data by segment

Use [Query Builder report templates]({{site.baseurl}}/user_guide/analytics/reporting/data_by_segments/) to break down performance metrics for campaigns, Canvas, variants, and steps by segments.

## Creating a segment breakdown report using Query Builder

To create a report from a [Query Builder]({{site.baseurl}}/user_guide/analytics/query_builder/) template, go to **Query Builder** and do the following:

1. Select **Create SQL Query** > **Query Template**.
2. Filter templates for those that have metrics that include “segment breakdowns”.
3. Select the template you want to use.
4. Fill the variables in your SQL template in the [Variables](#variables) tab.
5. (Optional) Directly edit the SQL in the template.
6. Select **Run Query**. Your results will display in a table.

## Variables {#variables}

Before generating your report, go to the **Variables** tab to provide information for the Report Builder template, including required variables that will vary based on report. 

The variables include:

- **Campaign or Canvas:** You can include one or multiple campaigns or Canvases (there is no maximum for how many campaigns or Canvases you can specify). If you do not specify any campaigns or Canvases, the report will include all campaigns or Canvases from your chosen time frame.
- **Variant:** If using a template that offers variant-level break downs, after selecting a campaign or Canvas, you can select variants from within that campaign or Canvas. If you select multiple variants, your results will be grouped by variant.
- **Step:** If you select a Canvas variant, you can select a Canvas step. You cannot select a step without first selecting a Canvas variant. 
- **Time range:** Identify the time period you want to pull data from. If no time range is specified, the time range will default to the past 30 days.
- **Product name:** If running a report for purchase data, you can identify a specific product to pull data for.
- **Conversion window:** Always required for reports with revenue and purchase data. The number of days after email receipt or click that Braze should attribute purchases or revenue to.
- **Segments:** Identify the segments to break down data by. If not specified, the report will run for all segments that have analytics tracking turned on.
- **Tags:** Specify tags in **Variables** to run your report for all campaigns or Canvases with certain tags. You may include multiple tags. If you add both tags and specific campaigns or Canvases to a report, your report will include data from your tags and the specified campaigns or Canvases. 

## Data availability

Data is available for time periods where both of these conditions are met:

1. [Segment analytics tracking]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking/) is turned on for the segments that you want to see data for.
2. The performance data by segment feature is turned on.

You can't access data from time periods prior to when this feature is turned on for your company. For example, if analytics tracking is turned on for Segment A on October 1 and this feature is turned on for your company on October 2, then you can only view data for Segment A for the campaigns and Canvases that recorded metrics after October 2. 

If your company turned on this feature on October 2, and turned on analytics tracking for Segment B on October 3, then you can only see data for Segment B for the campaigns and Canvases that recorded metrics after October 3.


