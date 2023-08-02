---
nav_title: Conversions Dashboard v2
article_title: Conversions Dashboard v2
permalink: "/conversions_dashboard_v2/"
hidden: true
description: "The conversions dashboard allows you to analyze conversions across campaigns, Canvases, and channels, using different attribution methods."
---

# Conversions Dashboard v2

The conversions dashboard allows you to analyze conversions across campaigns, Canvases, and channels, using different attribution methods*.

{% alert important %}
The Conversions Dashboard V2 is in early access. If you're interested in participating in the early access, reach out to your customer success manager.
{% endalert %}

<p><sup>* Coming soon</sup></p>

## Setting up your report

1. Navigate to **Analytics** > **Conversions**.
2. Select a **Date Range** for your report, up to a 90-day window.
3. Select the campaigns or Canvases (or both) that you would like to analyze. 
   - If you would like to filter campaigns and Canvases by tag, select a **Tag**.  
4. Select a **Channel** that you would like to analyze for your messages. For now, you can select a single channel. We are working on adding multi-channel support.
5. (Optional) Select a **Breakdown** layer to view different dimensions of data.
6. If you are interested in calculating conversions of an event that was not set up as a conversion event on the campaign or Canvas, turn on **Use custom events**.
   1. Select a custom event that you would like to use as the conversion event.
   2. Select the conversion window within which that event should have occurred to be counted as a conversion.

{% alert note %}
If you select a custom event, you will not see the **Conversion Event** dropdown on the page and will have to re-run to report to view conversions for different custom events.
{% endalert %}

{:start="7"}
7. Select an [Attribution Method](#attribution-methods) through which to analyze the selected messages. We are working to add additional attribution methods.
8. Click **Create** to run the report. 

After the page has loaded, select a **Conversion Event** to filter the report for conversion data. The available selections will include the events that were pre-configured on the Canvases and campaigns. If you selected a custom event when setting up your report (step 6), this option is not available.

## Understanding your results

Your report is split into three sections:

- [Conversion details](#conversion-details)
- [Conversion funnel](#conversion-funnel)
- [Conversions over time](#conversions-over-time)

### Conversion details

The conversion details table includes one column for *Unique Recipients* and another for *Conversions* (rate and total count)

- *Unique Recipients* is defined as the number of users who received a message through the selected channel within the report's date range.
- *Conversions* are defined by the attribution method you selected when you set up the report. See the following sections for additional details on the attribution methods.

![]({% image_buster /assets/img_archive/conversions2_details.png %}){: style="max-width:70%"}

If you selected breakdown-level details for campaigns or Canvases when setting up your report (step 5), you can click <i class="fas fa-angle-down"></i> to expand the table.

### Conversion funnel

Coming soon

### Conversions over time

This time series graph includes a representation of the conversions per campaign or Canvas over time. By default, all selected campaigns and Canvases are shown. To deselect a campaign or Canvas, click on the name of the campaign or Canvas that you'd like to exclude.

To download the time series data, click <i class="fas fa-bars"></i> and select your download option.

![]({% image_buster /assets/img_archive/conversions2_over_time.png %}){: style="max-width:70%"}

### Attribution methods

- Upon Receipt:
   - Total number of conversions that occurred after message receipt. 
   - Rate: Unique Received Conversions / Unique Recipients
- Upon Open:
   - Total number of conversions that occurred after message open.
   - Rate: Unique Open Conversions / Unique Recipients
- Upon Click:
   - Total number of conversions that occurred message email click. 
   - Rate: Unique Click Conversions / Unique Recipients
