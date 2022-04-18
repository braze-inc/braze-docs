---
nav_title: Email Performance Dashboard
article_title: Email Performance Dashboard
page_order: 2
page_type: reference
description: "This reference article covers the Email Performance Dashboard, which allows you to view performance metrics for your entire email channel from both campaigns and Canvases."
tool: 
  - Reports

---

# Email performance dashboard

The email performance dashboard allows you to view aggregate performance metrics for your entire email channel from both campaigns and Canvases. 

To use your email performance dashboard, go to **Overview** > **Email Performance**, and select the date range for the period you want to view data for. Your date range can be up to one year in the past.

![][1]

## Metrics calculations

The calculations for different metrics in the email performance dashboard is the same as those on an individual message level (i.e., Campaign Analytics). On this dashboard, the metrics are aggregated across all campaigns and Canvases for the date range you’ve selected. To learn more about these definitions, refer to [Email metrics]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting#email-metrics).

Each tile (except _Sends_, which is a count metric), shows the rate metric first, followed by the count metric. For example, the unique clicks tile contains the _Unique click rate_ from your selected time period and the count of the total number of unique clicks from that time period.

| Metric | Type | Calculation |
| --- | --- | ---- |
| Sends | Count | Total number of sends across each day in the date range |
| Delivery rate | Rate | (Total number of deliveries across each day in the date range) / (Total number of sends across each day in the date range) |
| Bounce rate | Rate | (Total number of bounces across each day in the date range) / (Total number of sends across each day in the date range) |
| Unsubscribe rate | Rate | (Total number of unique unsubscribes across each day in the date range) / (Total number of deliveries for date range)<br><br>This uses unique unsubscribes, which is also used in Campaign Analytics, Overview, and Report Builder. |
| Unique open rate | Rate | (Total number of unique opens across each day in the date range) / (Total number of deliveries for date range) |
| Other opens rate | Rate | (Total number of total other opens across each day in the date range) / (Total number of deliveries for date range)<br><br>Other opens includes emails that haven’t been identified as machine opens, such as when a user opens an email. This metric is non-unique and is a sub-metric of total opens.  |
| Unique click rate | Rate | (Total number of unique clicks across each day in the date range) / (Total number of deliveries for date range) |
| Unique click to open rate | Rate | (Total number of unique clicks across each day in the date range) / (Total number of unique opens across each day in the date range) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Frequently asked questions

### Why is my dashboard displaying empty values?

There are a few scenarios that could lead to empty values for a metric:

- Braze recorded zeros for that particular metric in your selected date range.
- You haven't sent any emails during the selected date range.
- While there were opens, clicks, or unsubscribes for a selected date range, there were no deliveries or sends. In this case, Braze will not calculate a rate metric.

To see more metrics, try expanding the date range.

### Why does my dashboard display more Other Opens than Unique Opens?

For the _Unique Opens_ metric, Braze will de-duplicate any repeat opens registered by a given user (whether they include _Machine Opens_ or _Other Opens_), so that only a single _Unique Open_ is incremented if a user opens multiple times. For _Other Opens_, Braze does not de-deduplicate.

<!---Temporarily hidden until functionality is added

## Empty values in your data

#### If a metric displays "0%" or "0"

This means Braze recorded zero for that particular metric during the time frame you’ve selected.

#### If a metric displays "N/A"

This means that while Braze recorded positive counts for a particular metric for the time frame you’ve selected, the denominator for the rate calculation (either sends or deliveries in most cases) was zero. This can occur when emails are sent out on one day and opens and clicks are recorded the following days, if your selected time frame does not include the date the emails were sent.

#### If a metric displays “--”

This means Braze hasn't recorded any data for that metric during the time period you selected. If you haven’t set up or sent any emails yet, learn more about how to do so in our dedicated [Email]({{site.baseurl}}/user_guide/message_building_by_channel/email) section.

--->

[1]: {% image_buster /assets/img_archive/email_performance_dashboard_1.png %}