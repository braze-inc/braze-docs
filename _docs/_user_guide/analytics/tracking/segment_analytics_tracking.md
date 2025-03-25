---
nav_title: Segment Analytics Tracking
article_title: Segment Analytics Tracking
page_order: 8
page_type: reference
description: "This reference article covers segment analytics tracking and how to view revenue and purchases over time, sessions over time, and custom events over time."
tool: 
  - Segments
  - Reports
---

# Segment analytics tracking

> When analytics tracking is turned on for a segment, you can view sessions, custom events, and revenue over time for that segment.

If you don't turn analytics tracking on for a segment, you can still access [real-time statistics][11] for that segment and target its users with campaigns. The only difference is whether you can access the specific analysis tools mentioned on this page.

## Turning on segment analytics

In a segment's page **Segment Details** section, turn on **Analytics Tracking**.

![Analytics tracking toggle for a segment][16]

An app can have tracking turned on for up to 25 segments. Braze recommends tracking segments that are important for you to analyze when understanding your campaigns' effects on sessions, revenue, and purchases.

## Viewing revenue and purchases over time

Go to **Analytics** > **Revenue Report** to view data on [revenue and purchases over time for this segment][14].

![Revenue data by segment][17]

To visually compare segment data for any custom time range, add or remove segments from the graph. Select **By Segment** in the **Breakdown** dropdown, and then select your segments in **Breakdown values**.

Select any segment name above the graph to turn on or off visibility for that segment's metrics.

![Revenue for multiple segments][21]

## Sessions over time

Similarly, you can find data on [sessions over time for this particular segment][13] on the **Home** page.

![Session data by segment][18]

## View custom events over time

View data on [Custom events over time for segments][20] by going to **Analytics** > **Custom Events Report**.

## Using Query Builder templates

When analytics tracking is turned on, you can use Query Builder report templates to break down performance metrics for campaigns, Canvas, variants, and steps by segments. To learn more, check out [Segment data]({{site.baseurl}}/user_guide/data_and_analytics/reporting/viewing_and_understanding_segment_data/#performance-data-by-segment).

[11]: {{site.baseurl}}/user_guide/data_and_analytics/reporting/viewing_and_understanding_segment_data/#segment-statistics
[13]: {{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_app_usage_data/#exporting-app-usage-data
[14]: {{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/
[16]: {% image_buster /assets/img_archive/A_Tracking_2.png %}
[17]: {% image_buster /assets/img_archive/Revenue.png %}
[18]: {% image_buster /assets/img_archive/events_over_time2.png %}
[20]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#analytics
[21]: {% image_buster /assets/img_archive/segment_revenue_multiple.png %}
