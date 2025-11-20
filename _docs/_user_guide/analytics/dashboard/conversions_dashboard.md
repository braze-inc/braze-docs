---
nav_title: Conversions dashboard
article_title: Conversions Dashboard
alias: "/conversions_dashboard_v2/"
description: "The conversions dashboard allows you to analyze conversions across campaigns, Canvases, and channels, using different attribution methods."
page_order: 3
page_type: reference
tool: 
  - Reports
---

# Conversions dashboard

> The conversions dashboard analyzes conversions across campaigns, Canvases, and channels, by using various [attribution methods](#attribution-methods). When measuring your conversions, you can specify the time frame, conversion event, and conversion window.

## Setting up your report

To set up your conversions dashboard report:

1. Go to **Analytics** > **Conversions**.
2. Select a **Date Range** for your report, up to a 90-day window.
3. Select the campaigns or Canvases (or both) to analyze. 
   - (optional) Filter campaigns and Canvases by selecting a tag.  
4. Select the **Channel(s)** to analyze for your messages.
5. Select a **Breakdown by** layer to view different dimensions of data, such as by variant, Canvas step, country, or language.
6. (Optional) If you want to calculate conversions of an event that wasn't set up as a conversion event on the campaign or Canvas, turn on [Use custom events](#using-custom-events).
7. Select an [attribution method](#attribution-methods) through which to analyze the selected messages.

{% alert note %}
If you're analyzing conversions for multiple channels, your **Attribution Method** will default to **Last-Touch Attribution**.
{% endalert %}

{:start="8"}
8. Select **Create** to run the report.

After the page loads, select a **Conversion Event** to filter the report for conversion data. The available selections will include the events that were pre-configured on the Canvases and campaigns. If you selected a custom event when setting up your report (step 6), this option isn't available.

### Using custom events

For custom event metrics to appear on the conversions dashboard, you must have a conversion event and a Canvas entry event in the date range specified on the page. 

To calculate conversions of an event that wasn't set up as a conversion event on the campaign or Canvas, select a specific custom event to use as a conversion event. 

1. When setting up your report, turn on **Use custom events**.
2. Select a custom event to use as the conversion event.
3. Select the conversion window within which that event should have occurred to be counted as a conversion.

{% alert note %}
If you select a custom event, you won't see the **Conversion Event** dropdown on the page and will have to re-run to report to view conversions for different custom events.
{% endalert %}

## Understanding your report

Your report is split into three sections:

- [Conversion details](#conversion-details)
- [Conversion funnel](#conversion-funnel)
- [Conversions over time](#conversions-over-time)

### Conversion details

The conversion details table always shows one column for *Recipients* and another for *Conversions* (rate and total). The remaining two table columns that appear depend on the options you selected when setting up your report. 

![Conversion details table showing Touches as the attribution method for columns three and four.]({% image_buster /assets/img_archive/conversions2_details.png %}){: style="border:none"}

The following table describes possible metrics.

| Metric shown | Description |
| --- | --- |
| Recipients | The number of users who received a message through the selected channel within the report's date range |
| Conversion Rate (Recipients) | Calculated as: (Number of conversions) / (Number of recipients) |
| Attribution method | Defined by the [attribution method](#attribution-methods) you selected when you set up the report. For Last Touch attribution or if multiple channels are selected, this appears as [Touches](#terms-to-know). |
| Conversion Rate (Attribution method) | Defined by the [attribution method](#attribution-methods) you selected when you set up the report. If multiple channels are selected, this defaults to last-touch attribution. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

If you selected breakdown-level details for campaigns or Canvases when [setting up your report](#setting-up-your-report) (step 5), you can click <i class="fas fa-angle-down"></i> to expand the table.

### Conversion funnel

This bar graph shows the absolute counts for each [engagement event]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) based on the selected channel. The conversions count will be defined as per the selected attribution method.

By default, all selected campaigns and Canvases are shown. To deselect a campaign or Canvas, select the name of the campaign or Canvas that you'd like to exclude. For additional details on the engagement event, you can hover over each bar.

To download the time series data, select a download option: PNG, JPEG, PDF, SVG, or CSV.

{% alert note %}
This graph only shows data for a single channel at a time. Use the **Channel** dropdown on the chart to select a single channel.
{% endalert %}

![Conversions funnel bar graph for two email campaigns showing similar results for Email Delivered, Email Opened, Email Clicked, and Conversions.]({% image_buster /assets/img_archive/conversions2_funnel.png %})

### Conversions over time

This time series graph includes a representation of the conversions per campaign or Canvas over time. By default, all selected campaigns and Canvases are shown. To deselect a campaign or Canvas, click on the name of the campaign or Canvas that you'd like to exclude.

To download the time series data, select <i class="fas fa-bars"></i> and then select your download option. Available options are PNG, JPEG, PDF, SVG, or CSV.

![Conversions over time time series graph for two email campaigns, showing conversions by day.]({% image_buster /assets/img_archive/conversions2_over_time.png %})

### Attribution methods

| Attribution method | Definition | Rate calculation | Channel-specific options |
| --- | --- | --- | --- |
| Upon Receipt | Total number of conversions that occurred after message receipt | Calculated as (Unique Received Conversions) / (Unique Recipients) | {::nomarkdown}<ul><li>Upon email delivery</li><li>Upon SMS delivery</li></ul>{:/} |
| Upon Send | Total number of conversions that occurred after message send | Calculated as (Unique Send Conversions) / (Unique Recipients) | {::nomarkdown}<ul><li>Upon push send</li><li>Upon Content Card send</li><li>Upon SMS send</li></ul>{:/} |
| Upon Open | Total number of conversions that occurred after message open | Calculated as (Unique Open Conversions) / (Unique Recipients) | {::nomarkdown}<ul><li>Upon email open</li><li>Upon push open</li></ul>{:/} |
| Upon Click | Total number of conversions that occurred message click | Calculated as (Unique Click Conversions) / (Unique Recipients) | {::nomarkdown}<ul><li>Upon email click</li><li>Upon Content Card click</li><li>Upon IAM click</li></ul>{:/} |
| Upon Impression | Total number of conversions that occurred after an impression | Calculated as (Unique Impression Conversions) / (Unique Recipients) | {::nomarkdown}<ul><li>Upon IAM impression</li><li>Upon Content Card impression</li></ul>{:/} |
| Upon Last-Touch | Conversions that give all credit to the last-touched or clicked message during the conversion window. | Calculated as (Number of Touches) / (Unique Recipients) | Last-touch attribution is automatically selected if multiple channels are added to the report.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Terms to know

| Term | Definition |
| --- | --- |
| Touch | A physical interaction or touchpoint with a message.<br><br>Touches can include:<br>{::nomarkdown}<ul><li>Email Click</li><li>Push Open</li><li>Content Card Click</li><li>In-App Message Click</li><li>SMS Click</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Troubleshooting

### Why do I have low campaign or Canvas conversions?

Your conversions might not be as high as you expect them to be when compared to previous campaigns or your expectations. Conversions are a tricky business, but they are dependent on a few simple functions in our platform: event tracking and conversion deadlines.

To troubleshoot why that is, we recommend checking your event tracking and conversion deadlines.

#### Event tracking

When a campaign triggers a session start or custom event, you want to ensure that this event, or session, is happening frequently enough to trigger the message. Check the [home dashboard]({{site.baseurl}}/user_guide/analytics/dashboard/home_dashboard/) for session data, or your [custom events]({{site.baseurl}}/user_guide/analytics/reporting/configuring_reporting/) report.

#### Conversion deadlines

For each conversion event that you select per campaign, you set the [deadline]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/#creating-a-campaign-with-conversion-tracking). This means you are setting a time limit within which a conversion must happen in order for it to count toward each respective campaign.

Check that you've reviewed information on [conversion tracking rules]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/#conversion-tracking-rules) to understand your campaign metrics. For user conversions in Canvas, refer to [Canvas FAQ]({{site.baseurl}}/user_guide/engagement_tools/canvas/faqs/#how-are-user-conversions-tracked-in-a-canvas). 