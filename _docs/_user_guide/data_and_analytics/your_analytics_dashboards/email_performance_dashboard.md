---
nav_title: Channel Performance Dashboard
article_title: Channel Performance Dashboard
page_order: 2
page_type: reference
description: "This reference article covers the Channel Performance Dashboard, which allows you to view performance metrics for entire channels across both campaigns and Canvases."
tool: 
  - Reports

---

# Channel performance dashboards

Channel performance dashboards allow you to view aggregate performance metrics for an entire channel, from both campaigns and Canvases. These dashboards are currently available for email and SMS.

![Email performance dashboard displaying email channel engagement from the last thirty days.][1]

## Email performance dashboard

To use your email performance dashboard, go to **Overview** > **Email Performance**, and select the date range for the period you want to view data. Your date range can be up to one year in the past.

### Metrics calculations

![][2]{: style="max-width:40%;float:right;margin-left:15px;border:none;"}

The calculations for different metrics in the email performance dashboard are the same as those on an individual message level (i.e., Campaign Analytics). On this dashboard, the metrics are aggregated across all campaigns and Canvases for the date range you’ve selected. To learn more about these definitions, refer to [Email metrics]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting#email-metrics).

Each tile shows the rate metric first, followed by the count metric (with the exception of _Sends_, which displays the count metric followed by the average per day). For example, the unique clicks tile contains the _Unique click rate_ from your selected time period and the count of the total number of unique clicks from that time period. Each tile also shows the [comparison to the last period](#comparison-to-last-period).

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

## SMS performance dashboard

To use your SMS performance dashboard, go to **Overview** > **SMS Performance**, and select the date range for the period you want to view data. Your date range can be up to one year in the past. 

### Metrics calculations

![][2]{: style="max-width:40%;float:right;margin-left:15px;border:none;"}

The calculations for different metrics in the SMS performance dashboard is the same as those on an individual message level (i.e., Campaign Analytics). On this dashboard, the metrics are aggregated across all campaigns and Canvases for the date range you’ve selected. To learn more about these definitions, refer to [SMS metrics]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_campaign_analytics/).

Each tile shows the rate metric first, followed by the count metric (with the exception of _Sends_, which displays the count metric followed by the average per day). Each tile also shows the [comparison to the last period](#comparison-to-last-period).

| Metric | Type | Calculation |
| --- | --- | ---- |
| Sends | Count | Total number of sends across each day in the date range |
| Confirmed deliveries rate | Rate | (Total number of deliveries across each day in the date range) / (Total number of sends across each day in the date range) |
| Delivery failures rate | Rate | (Total number of failures across each day in the date range) / (Total number of sends across each day in the date range) |
| Rejections rate | Rate | (Total number of rejections across each day in the date range) / (Total number of sends across each day in the date range) |
| Click rate | Rate | (Total number of clicks across each day in the date range) / (Total number of deliveries across each day in the date range) |
| Total opt-ins | Rate | Total number of inbound message opt-ins across each day in the date range |
| Total opt-outs | Rate | Total number of inbound message opt-outs across each day in the date range |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Dashboard filters

You can filter the data on your dashboard using the following filter options:

- **Tag:** Choose one tag; once applied, your dashboard will show metrics for only your selected tag.
- **Canvas:** Choose up to 10 Canvases; once applied, your dashboard will show metrics for only your selected Canvases. If you select a tag filter first, then your options for Canvas filters will only include Canvases that have your selected tag.
- **Campaign:** Choose up to 10 campaigns; once applied, your dashboard will show metrics for only your selected campaigns. If you select a tag filter first, then your options for campaign filters will only include campaigns that have your selected tag.

![Filter options on the Channel Performance Dashboard where you can select a tag and list of Canvases to filter by.][3]

## Comparison to last period: Change in totals or rates

The channel performance dashboard automatically compares the time period you have selected in the date range versus the prior time period totaling the same number of days. For example, if you choose "Last 7 Days" as your date range in the dashboard, the comparison to the last period will compare the metrics from the last seven days against the seven days prior. If you select a custom date range—let's say May 10 to May 15, which is six days' worth of data—the dashboard will compare the metrics from across those days to the metrics from May 4 to May 9.

The comparison is the percentage change between the last and current periods, calculated by taking the difference between the two periods and dividing it by the metric from the last period.

You can switch between **Show Change in Totals**—which compares the total counts (i.e., number of emails delivered) between the two periods—and **Show Change in Rates**—which compares the rates (i.e., delivery rate).

![Radio buttons to switch between showing change in totals or change in rates for the Channel Performance Dashboard.][4]

## Frequently asked questions

### Why is my dashboard displaying empty values?

There are a few scenarios that could lead to empty values for a metric:

- Braze recorded zeros for that particular metric in your selected date range.
- You haven't sent any messages during the selected date range.
- While there were metrics such as opens, clicks, or unsubscribes for a selected date range, there were no deliveries or sends. In this case, Braze will not calculate a rate metric.

To see more metrics, try expanding the date range.

### Why does my email dashboard display more Other Opens than Unique Opens?

For the _Unique Opens_ metric, Braze will de-duplicate any repeat opens registered by a given user (whether they include _Machine Opens_ or _Other Opens_), so that only a single _Unique Open_ is incremented if a user opens multiple times. For _Other Opens_, Braze does not de-deduplicate.

<!---Temporarily hidden until functionality is added

## Empty values in your data

#### If a metric displays "0%" or "0"

This means Braze recorded zero for that particular metric during the time frame you’ve selected.

#### If a metric displays "N/A"

This means that while Braze recorded positive counts for a particular metric for the time frame you’ve selected, the denominator for the rate calculation (either sends or deliveries in most cases) was zero. This can occur when emails are sent out on one day and opens and clicks are recorded the following days, if your selected time frame does not include the date the messages were sent.

#### If a metric displays “--”

This means Braze hasn't recorded any data for that metric during the time period you selected. If you haven’t set up or sent any emails yet, learn more about how to do so in our dedicated [Email]({{site.baseurl}}/user_guide/message_building_by_channel/email) section.

--->

[1]: {% image_buster /assets/img_archive/email_performance_dashboard_1.png %}
[2]: {% image_buster /assets/img_archive/email_performance_dashboard_2.png %}
[3]: {% image_buster /assets/img_archive/dashboard_filters.png %}
[4]: {% image_buster /assets/img_archive/email_performance_dashboard_3.png %}
