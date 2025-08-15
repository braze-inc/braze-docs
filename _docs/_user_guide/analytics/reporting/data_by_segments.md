---
nav_title: Metrics by segments
article_title: Metrics by Segments
page_order: 2.5
page_type: reference
description: "This page describes how you can use Query Builder report templates to break down performance metrics for campaigns, Canvas, variants, and steps by segments."
tool: 
  - Segments
  - Reports
  
---

# Metrics by segments

> Use [Query Builder]({{site.baseurl}}/user_guide/analytics/query_builder/) report templates to break down performance metrics for campaigns, Canvas, variants, and steps by segments.

[Analytics tracking]({{site.baseurl}}/user_guide/data_and_analytics/tracking/segment_analytics_tracking#segment-analytics-tracking) must be turned on for the segments you want to access metrics for.

To run these reports, do the following:
1. In **Query Builder**, choose to create a new SQL report with a template. 
2. Select **Segment breakdowns** for the metric, which filters templates for those where the metrics include breakdowns of segment, which are:
- Email performance metrics by segment
- Email engagement metrics for variants or steps, by segment
- Purchases and revenue by segment
- Purchases and revenue for variants or steps, by segment
- Push performance by segment

![The Segment breakdown page contains a SQL editor, a side panel with tabs for Variables, Available Data Tables, Query History, and the AI Query Builder, and a results section.]({% image_buster /assets/img_archive/segment_breakdown.png %})

## Report templates

{% tabs %}
{% tab Email engagement metrics by segment %}

### Viewing metrics for campaigns or Canvases {#campaign-canvas-email}

To view email performance metrics broken down by segment at the campaign or Canvas level, use the [Variables](#variables) tab to specify the campaigns or Canvases and a time frame for pulling data. If no campaigns or Canvases are specified, the report will include emails from all campaigns and Canvases from the specified time frame. You can also opt to view all campaigns and Canvases with certain tags.

The following email metrics are available in this report:
- Sends
- Deliveries
- Complaints
- Unique opens
- Unique machine opens
- Unique non-machine opens
- Unique clicks
- Unsubscribes
- Bounces
- Soft bounces
- Deferred

#### Results

Your results will show email engagement metrics by segment for the campaigns or Canvases you selected. If you didn't select specific campaigns or Canvases, your report will show the email metrics for each segment across all email campaigns and Canvases within your report’s time frame. 

- **Rows:** Segments
- **Columns:** Email engagement metrics

### Viewing metrics for variants or steps

To view email performance broken down by segment at the campaign variant level, Canvas variant level, or Canvas step level, first choose a variant or step-level report (these are reports that have “for variants or steps” in the title), and then use the **Variables** tab to specify the following:

- Specific campaign or Canvas (required if using a variant or step-level report) 
- Variants (required if using a variant or step-level report)
- Canvas step (optional)

The metrics are the same as those offered for the [campaign or Canvas level](#campaign-canvas-email) template. If you choose multiple variants, your results will be grouped by variant.

#### Results

Your results will show email engagement metrics by segment for your selected variants or steps. 

- **Rows:** Segments
- **Columns:** Email engagement metrics

{% endtab %}

{% tab Purchases and revenue by segment %}
### Viewing metrics for campaigns or Canvases

To view purchase and revenue metrics broken down by segment for a specific campaign or Canvas, use the [Variables](#variables) tab to specify the following:

- Conversion window (the number of days after email receipt or click that Braze should attribute purchases or revenue to)
- Specific product (optional) 

In addition, use the **Variables** tab to specify whether to run the report for one or more campaigns or Canvases, or one or more tags. If no campaigns, Canvases, or tags are chosen, then the report will run for all emails from campaigns or Canvases during your chosen time frame.

Currently, this report pulls metrics from only the email channel. Any revenue or purchase data from channels besides emails won't be reflected in the report. 

The following metrics are available for emails:

- Unique purchases upon receipt
- Revenue upon receipt
- Unique purchases upon click
- Revenue upon click
- Unique recipients
- Unique email clicks

All rate metrics use unique email recipients as the denominator.

#### Definitions

- “Upon receipt” refers to purchase events or revenue that occurred within your specified conversion window, after users received the specified campaigns or Canvases. 
- “Upon click” refers to the purchase events or revenue that occurred after the purchase events, within your specified conversion window, after users clicked the specified campaigns or Canvases.

For example, let's say a segment contains 10 users and five of them made a purchase after receiving your email. If one of those five made a purchase after clicking your email, your "Unique purchases upon receipt rate" would be 50% and your "Unique purchases upon click rate" would be 10%.

![The report shows email metrics including unique purchases upon receipt, revenue upon receipt, unique purchases upon click, revenue upon click, unique recipients, and unique email clicks.]({% image_buster /assets/img_archive/segment_breakdown_results.png %})

#### Results

Your results will show purchase metrics by segment for your selected campaigns or Canvases. If you didn't select specific campaigns or Canvases, your report will show the purchase metrics for each segment across all email campaigns or Canvases within your report’s time frame. 

- **Rows:** Segments
- **Columns:** Purchase metrics


### Viewing metrics for variants or steps

To view purchase and revenue metrics broken down by segment for a specific campaign variant, Canvas variant, or Canvas step, use the [Variables](#variables) tab to specify the following:

- Specific campaign or Canvas
- Variants 
- Canvas step (optional) 
- Time range
- Specific product (optional) 

#### Results

Your results will show purchase metrics by segment for the variants or steps you selected.

- **Rows:** Segments
- **Columns:** Purchase metrics

{% endtab %}
{% tab Top or bottom messaging for email engagement %}

### Viewing metrics for the top or bottom performers

This report in the [Variables](#variables) tab displays the campaigns, Canvases, or Canvas steps that were the highest or lowest performers for a specified email engagement metric. 

Use cases include: 
- 10 campaigns with the highest unique email open rates
- 25 Canvases with the most email unsubscribes
- 50 Canvas steps with the highest unique clicks

The following email metrics are available in this report:
- Sends
- Deliveries
- Complaints
- Unique opens
- Unique machine opens
- Unique non-machine opens
- Unique clicks
- Unsubscribes
- Bounces
- Soft bounces
- Complaints

To view this report, you must specify the following variables in the **Variables** tab:
- **Metrics:** Select one of the metrics by which to rank your results
- **Number of reports:** Select top or bottom results and the number of results, such as top 10 or bottom 15
- **Message type:** Specify if your results are campaigns, Canvases, or Canvas steps

#### Results

Your results will show the top (or bottom) campaigns, Canvases, or Canvas steps that you selected. For example, if you selected the top 10 campaigns for click rate, your results will show the top 10 campaigns ordered from highest to lowest click rate. Your columns will display all of the email engagement metrics for each row (campaigns, Canvases, or Message steps).

{% endtab %}
{% tab Top or bottom messaging for purchases %}

### Viewing metrics for the top or bottom performers

This report in the [Variables](#variables) tab displays the campaigns, Canvases, or Canvas steps that were the highest or lowest performers for a specified purchase or revenue metric.

Use cases include:
- 20 campaigns with the highest purchase rates for a specific product
- 25 Canvases with the most generated revenue
- 10 Canvas steps with the lowest product purchase rate

The following email metrics are available in this report:
- Unique purchases upon receipt
- Revenue upon receipt
- Unique purchases upon click
- Revenue upon click
- Unique recipients
- Unique email clicks

To view this report, you must specify the following variables in the **Variables** tab:
- **Metrics:** Select one of the metrics by which to rank your results
- **Number of reports:** Select top or bottom results and the number of results, such as top 10 or bottom 15
- **Message type:** Specify if your results are campaigns, Canvases, or Canvas steps
- **Conversion window:** The number of days after email receipt or click to which Braze will attribute purchases or revenue 

#### Definitions

- “Upon receipt” refers to purchase events or revenue that occurred within your specified conversion window, after users received the specified campaigns or Canvases. 
- “Upon click” refers to the purchase events or revenue that occurred after the purchase events, within your specified conversion window, after users clicked the specified campaigns or Canvases.

For example, let's say a segment contains 10 users and five of them made a purchase after receiving your email. If one of those five made a purchase after clicking your email, your "unique purchases upon receipt" rate would be 50% and your "unique purchases upon click" rate would be 10%.

#### Results

Your results will show the top (or bottom) campaigns, Canvases, or Canvas steps that you selected. For example, if you selected the top 10 campaigns for "revenue upon click", your results will show the top 10 campaigns ordered from highest to lowest "revenue upon click". Your columns will display all of the purchase metrics for each row (campaigns, Canvases, or Message steps).

{% endtab %}
{% tab Push performance by segment %}

### Viewing push metrics for segments

This report in the [Variables](#variables) tab displays push metrics broken down by segments. 

In the **Variables** tab, specify the campaigns or Canvases to view metrics for and a time frame for pulling data. If you don't select any campaigns or Canvases, the report will show pushes from all campaigns and Canvases in your specified time frame. You can also view all campaigns and Canvases with certain tags.

The following push metrics are available in this report:

- Sends
- Bounces
- Deliveries
- Direct opens

#### Results

Your report will display the following results:

- **Rows:** Segments
- **Columns:** Push metrics
{% endtab %}
{% endtabs %}