---
nav_title: Email Performance Dashboard
article_title: Email Performance Dashboard
page_order: 2
page_type: reference
description: "This reference article..."
tool: 
  - Reports

---

# Email performance dashboard

The email performance dashboard allows you to view aggregate performance metrics for your entire email channel from both campaigns and Canvases. 

To use your email performance dashboard, go to **Overview** > **Email Performance Dashboard**, and select the date range for the period you want to view data for. Your date range can be up to one year in the past.

## Metrics calculations

The calculations for different metrics in this dashboard is the same as those on an individual message level (i.e., Campaign Analytics). On this dashboard, the metrics are aggregated across all campaigns and Canvases for the date range you’ve selected. To learn more about these definitions, refer to [Email metrics]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting#email-metrics).

| Metric | Type | Calculation |
| --- | --- | ---- |
| Sends | Count | Total sum of number of sends from each day in the date range |
| Delivery rate | Rate | (sum of number of deliveries from each day in the date range) / (sum of number of sends from each day in the date range) |
| Bounce rate | Rate | (sum of number of bounces from each day in the date range) / (sum of number of sends from each day in the date range) |
| Unsubscribe rate | Rate | (sum of number of unique unsubscribes across each day in the date range) / (sum of number of deliveries for date range)<br><br>This uses unique unsubscribes, which is also used in Campaign Analytics, Overview, and Report Builder. |
| Unique open rate | Rate | (sum of number of unique opens from each day in the date range) / (sum of number of deliveries for date range) |
| Other opens rate | Rate | (sum of number of total other opens across each day in the date range) / (sum of number of deliveries for date range)<br><br>Other opens is non-unique and is a sub-metric of total opens. |
| Unique click rate | Rate | (sum of number of unique clicks across each day in the date range) / (sum of number of deliveries for date range) |
| Unique click to open rate | Rate | (sum of number of unique clicks from each day in the date range) / (sum of number of unique opens from each day in the date range) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Empty values in your data

#### If a metric displays "0%" or "0"

This means Braze recorded zero for that particular metric during the time frame you’ve selected.

#### If a metric displays "N/A"

This means that while Braze recorded positive counts for a particular metric for the time frame you’ve selected, the denominator for the rate calculation (either sends or deliveries in most cases) was zero. This can occur when emails are sent out on one day and opens and clicks are recorded the following days, if your selected time frame does not include the date the emails were sent.

#### If a metric displays “--”

This means Braze hasn't recorded any data for that metric during the time period you selected. If you haven’t set up or sent any emails yet, learn more about how to do so in our dedicated [Email]({{site.baseurl}}/user_guide/message_building_by_channel/email) section.