---
nav_title: Conversions Dashboard
article_title: Conversions Dashboard
alias: "/conversions_dashboard_v2/"
description: "The conversions dashboard allows you to analyze conversions across campaigns, Canvases, and channels, using different attribution methods."
page_order: 3
page_type: reference
tool: 
  - Reports
---

# Conversions dashboard

> The conversions dashboard allows you to analyze conversions across campaigns, Canvases, and channels, using different [attribution methods](#attribution-methods). When measuring your conversions, you can specify the time frame, conversion event, and conversion window.

## Setting up your report

To set up your conversions dashboard report:

1. Navigate to **Analytics** > **Conversions**.
2. Select a **Date Range** for your report, up to a 90-day window.
3. Select the campaigns or Canvases (or both) that you would like to analyze. 
   - If you would like to filter campaigns and Canvases by tag, select a **Tag**.  
4. Select the **Channel(s)** you would like to analyze for your messages.
5. (optional) If desired, select a **Breakdown** layer. This allows you to view different dimensions of data, such as by variant, Canvas step, country, or language.
6. (optional) If you are interested in calculating conversions of an event that was not set up as a conversion event on the campaign or Canvas, turn on [Use custom events](#using-custom-events).
7. Select an [Attribution Method](#attribution-methods) through which to analyze the selected messages.

{% alert note %}
If you are analyzing conversions for multiple channels, your **Attribution Method** will default to **Last-Touch Attribution**.
{% endalert %}

{:start="8"}
8. Click **Create** to run the report.

After the page has loaded, select a **Conversion Event** to filter the report for conversion data. The available selections will include the events that were pre-configured on the Canvases and campaigns. If you selected a custom event when setting up your report (step 6), this option is not available.

### Using custom events

If you are interested in calculating conversions of an event that was not set up as a conversion event on the campaign or Canvas, you can select a specific custom event to use as a conversion event. 

1. When setting up your report, turn on **Use custom events**.
2. Select a custom event that you would like to use as the conversion event.
3. Select the conversion window within which that event should have occurred to be counted as a conversion.

{% alert note %}
If you select a custom event, you will not see the **Conversion Event** dropdown on the page and will have to re-run to report to view conversions for different custom events.
{% endalert %}

## Understanding your results

Your report is split into three sections:

- [Conversion details](#conversion-details)
- [Conversion funnel](#conversion-funnel)
- [Conversions over time](#conversions-over-time)

### Conversion details

The conversion details table will always show one column for *Recipients* and another for *Conversions* (rate and total). The remaining two table columns that appear depend on the options you selected when setting up your report. The following table describes possible metrics.

| Metric shown | Description |
 | --- | --- |
| Recipients | The number of users who received a message through the selected channel within the report's date range |
| Conversion Rate (Recipients) | Calculated as: (Number of conversions) / (Number of recipients) |
| Attribution method | Defined by the [attribution method](#attribution-methods) you selected when you set up the report. For Last Touch attribution or if multiple channels are selected, this appears as [Touches](#terms-to-know). |
| Conversion Rate (Attribution method) | Defined by the [attribution method](#attribution-methods) you selected when you set up the report. If multiple channels are selected, this defaults to last-touch attribution. |
{: .reset-td-br-1 .reset-td-br-2 }

![]({% image_buster /assets/img_archive/conversions2_details.png %})

If you selected breakdown-level details for campaigns or Canvases when setting up your report (step 5), you can click <i class="fas fa-angle-down"></i> to expand the table.

### Conversion funnel

This bar graph shows the absolute counts for each [engagement event]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events) based on the selected channel. The conversions count will be defined as per the selected attribution method.

By default, all selected campaigns and Canvases are shown. To deselect a campaign or Canvas, click on the name of the campaign or Canvas that you'd like to exclude. For additional details on the engagement event, you can hover over each bar.

To download the time series data, click and select your download option. Available options are PNG, JPEG, PDF, SVG, or CSV.

{% alert note %}
This graph only shows data for a single channel at a time. Use the **Channel** dropdown on the chart to select a single channel.
{% endalert %}

![]({% image_buster /assets/img_archive/conversions2_funnel.png %}){: style="max-width:70%"}

### Conversions over time

This time series graph includes a representation of the conversions per campaign or Canvas over time. By default, all selected campaigns and Canvases are shown. To deselect a campaign or Canvas, click on the name of the campaign or Canvas that you'd like to exclude.

To download the time series data, click <i class="fas fa-bars"></i> and select your download option. Available options are PNG, JPEG, PDF, SVG, or CSV.

![]({% image_buster /assets/img_archive/conversions2_over_time.png %}){: style="max-width:70%"}

### Attribution methods

| Attribution method | Definition | Rate calculation | Channel-specific options |
| --- | --- | --- | --- |
| Upon Receipt | Total number of conversions that occurred after message receipt | Calculated as (Unique Received Conversions) / (Unique Recipients) | {::nomarkdown}<ul><li>Upon email delivery</li><li>Upon SMS delivery</li></ul>{:/} |
| Upon Send | Total number of conversions that occurred after message send | Calculated as (Unique Send Conversions) / (Unique Recipients) | {::nomarkdown}<ul><li>Upon push send</li><li>Upon Content Card send</li><li>Upon SMS send</li></ul>{:/} |
| Upon Open | Total number of conversions that occurred after message open | Calculated as (Unique Open Conversions) / (Unique Recipients) | {::nomarkdown}<ul><li>Upon email open</li><li>Upon push open</li></ul>{:/} |
| Upon Click | Total number of conversions that occurred message click | Calculated as (Unique Click Conversions) / (Unique Recipients) | {::nomarkdown}<ul><li>Upon email click</li><li>Upon Content Card click</li><li>Upon IAM click</li></ul>{:/} |
| Upon Impression | Total number of conversions that occurred after an impression | Calculated as (Unique Impression Conversions) / (Unique Recipients) | {::nomarkdown}<ul><li>Upon IAM impression</li><li>Upon Content Card impression</li></ul>{:/} |
| Upon Last-Touch | Conversions that give all credit to the last-touched or clicked message during the conversion window. | Calculated as (Number of Touches) / (Unique Recipients) | Last-touch attribution is automatically selected if multiple channels are added to the report.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## Terms to know

| Term | Definition |
| --- | --- |
| Touch | A physical interaction or touchpoint with a message.<br><br>Touches can include:<br>{::nomarkdown}<ul><li>Email Click</li><li>Push Open</li><li>Content Card Click</li><li>In-App Message Click</li><li>SMS Delivery</li></ul>{:/} |
