---
nav_title: Conversions Dashboard v2
article_title: Conversions Dashboard v2
permalink: "/conversions_dashboard_v2/"
hidden: true
description: "The conversions dashboard allows you to analyze conversions across campaigns, Canvases, and channels, using different attribution methods."
---

# Conversions dashboard updates

> The conversions dashboard allows you to analyze conversions across campaigns, Canvases, and channels, using different [attribution methods](#attribution-methods)*. When measuring your conversions, you can specify the time frame, conversion event, and conversion window.

{% alert important %}
This page describes early access updates to the Conversions dashboard. If you're interested in participating in the early access, reach out to your customer success manager.
{% endalert %}

<p><sup>* Coming soon</sup></p>

## Setting up your report

1. Navigate to **Analytics** > **Conversions**.
2. Select a **Date Range** for your report, up to a 90-day window.
3. Select the campaigns or Canvases (or both) that you would like to analyze. 
   - If you would like to filter campaigns and Canvases by tag, select a **Tag**.  
4. Select which **Channel(s)** you would like to analyze for your messages.
5. (Optional) If desired, select a **Breakdown** layer. This allows you to view different dimensions of data, such as by variant, Canvas step, country, or language.
6. (Optional) If you are interested in calculating conversions of an event that was not set up as a conversion event on the campaign or Canvas, turn on [Use custom events](#using-custom-events).
7. Select an [Attribution Method](#attribution-methods) through which to analyze the selected messages.
   - Note: if you are analyzing conversions for multiple channels, you will only be able to use Last Touch Attribution.
9. Click **Create** to run the report.

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

The conversion details table includes one column for *Unique Recipients* and another for *Conversions* (rate and total count).

- *Recipients* is defined as the number of users who received a message through the selected channel within the report's date range.
- *Conversions* are defined by the attribution method you selected when you set up the report. See the following sections for additional details on the [attribution methods](#attribution-methods).
- *Conversion Rate (Recipients)* Calculated as: (Number of conversions) / (Number of recipients)
- *Touches* are defined as the number of physical interactions or touchpoints with a message. Touches can include: Email Open and Email Click, Push Open, Content Card Click, In-App Message Click, SMS Delivery.
- *Conversion Rate (Last Touch)* Conversions that give all credit to the last-touched or clicked message during the conversion window. Calculated as: (Number of conversions) / (Number of Touches)



![]({% image_buster /assets/img_archive/conversions2_details.png %}){: style="max-width:70%"}

If you selected breakdown-level details for campaigns or Canvases when setting up your report (step 5), you can click <i class="fas fa-angle-down"></i> to expand the table.

### Conversion funnel

This bar graph shows the absolute counts for each [engagement event]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events) based on the selected channel. The conversions count will be defined as per the selected attribution method.

By default, all selected campaigns and Canvases are shown. To deselect a campaign or Canvas, click on the name of the campaign or Canvas that you'd like to exclude. For additional details on the engagement event, you can hover over each bar.

To download the time series data, click and select your download option. Available options are PNG, JPEG, PDF, SVG, or CSV.

{% alert note %}
This graph only shows data for a single channel at a time, please use the **Channel** dropdown on the chart to select a single channel.
{% endalert %}

![]({% image_buster /assets/img_archive/conversions2_funnel.png %}){: style="max-width:70%"}

### Conversions over time

This time series graph includes a representation of the conversions per campaign or Canvas over time. By default, all selected campaigns and Canvases are shown. To deselect a campaign or Canvas, click on the name of the campaign or Canvas that you'd like to exclude.

To download the time series data, click <i class="fas fa-bars"></i> and select your download option. Available options are PNG, JPEG, PDF, SVG, or CSV.

![]({% image_buster /assets/img_archive/conversions2_over_time.png %}){: style="max-width:70%"}

### Attribution methods

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;}
.leftHeader{font-size: 12px; font-weight: bold; background-color: #f4f4f7; text-transform: uppercase; color: #212123; font-family: "Sailec W00 Bold",Arial,Helvetica,sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky"></th>
    <th class="tg-0pky">Definition</th>
    <th class="tg-0pky">Rate calculation</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="leftHeader">Upon Receipt</td>
    <td class="tg-0pky">Total number of conversions that occurred after message receipt</td>
    <td class="tg-0pky">Calculated as (Unique Received Conversions) / (Unique Recipients)</td>
  </tr>
  <tr>
    <td class="leftHeader">Upon Open</td>
    <td class="tg-0pky">Total number of conversions that occurred after message open.</td>
    <td class="tg-0pky">Calculated as (Unique Open Conversions) / (Unique Recipients)</td>
  </tr>
  <tr>
    <td class="leftHeader">Upon Click</td>
    <td class="tg-0pky">Total number of conversions that occurred message email click.</td>
    <td class="tg-0pky">Calculated as (Unique Click Conversions) / (Unique Recipients)</td>
  </tr>
     <tr>
    <td class="leftHeader">Last Touch Attribution</td>
    <td class="tg-0pky">Conversions that give all credit to the last-touched or clicked message during the conversion window.</td>
    <td class="tg-0pky">Calculated as (Number of Touches) / (Unique Recipients)</td>
  </tr>
</tbody>
</table>

