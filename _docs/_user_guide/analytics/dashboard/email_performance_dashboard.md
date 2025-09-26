---
nav_title: Channel Performance Dashboard
article_title: Channel Performance Dashboard
page_order: 2
page_type: reference
description: "This reference article covers the Channel Performance Dashboard, which allows you to view performance metrics for entire channels across both campaigns and Canvases."
tool: 
  - Reports

---

# Channel performance dashboard

> Channel performance dashboards show aggregate performance metrics for an entire channel, from both campaigns and Canvases. These dashboards are currently available for email and SMS.

![Email performance dashboard displaying email channel engagement from the last thirty days.]({% image_buster /assets/img_archive/email_performance_dashboard_1.png %})

You can view the following dashboards:
- [Email performance dashboard](#email-performance-dashboard)
- [Email insights dashboard](#email-insights-dashboard)
- [SMS performance dashboard](#sms-performance-dashboard)

## Email performance dashboard

View your email performance dashboard by going to **Analytics** > **Email Performance**, and selecting the date range for the period you want to view data. Your date range can be up to one year in the past.

### How metrics are calculated

![An example email campaign with 335,630 sends, with an average of 11,187.667 per day.]({% image_buster /assets/img_archive/email_performance_dashboard_2.png %}){: style="max-width:40%;float:right;margin-left:15px;border:none;"}

The calculations for different metrics in the email performance dashboard are the same as those on an individual message level (such as campaign analytics). On this dashboard, the metrics are aggregated across all campaigns and Canvases for the date range you've selected. To learn more about these definitions, refer to [Email metrics]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting#email-metrics).

Each tile shows the rate metric first, followed by the count metric (with the exception of *Sends*, which displays the count metric followed by the average per day). For example, the unique clicks tile contains the *Unique click rate* from your selected time period and the count of the total number of unique clicks from that time period. Each tile also shows the [comparison to the last period](#comparing-time-periods).

| Metric | Type | Calculation |
| --- | --- | ---- |
| Sends | Count | Total number of sends across each day in the date range |
| Delivery rate | Rate | (Total number of deliveries across each day in the date range) / (Total number of sends across each day in the date range) |
| Bounce rate | Rate | (Total number of bounces across each day in the date range) / (Total number of sends across each day in the date range) |
| Unsubscribe rate | Rate | (Total number of unique unsubscribes across each day in the date range) / (Total number of deliveries for a date range)<br><br>This uses unique unsubscribes, which is also used in Campaign Analytics, Overview, and Report Builder. These unsubscribes are logged across all sources (such as the SDK, REST API, CSV imports, emails, and list unsubscribes). The unsubscribe rates in Campaign and Canvas analytics are unsubscribes that occur as a result of an unsubscribe click on a Braze-delivered email.  |
| Unique open rate | Rate | (Total number of unique opens across each day in the date range) / (Total number of deliveries for a date range) |
| Other opens rate | Rate | (Total number of total other opens across each day in the date range) / (Total number of deliveries for date range)<br><br>Other opens includes emails that haven't been identified as machine opens, such as when a user opens an email. This metric is non-unique and is a sub-metric of total opens.  |
| Unique click rate | Rate | (Total number of unique clicks across each day in the date range) / (Total number of deliveries for a date range) |
| Unique click to open rate | Rate | (Total number of unique clicks across each day in the date range) / (Total number of unique opens across each day in the date range) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Email insights dashboard 

The email insights dashboard tracks where and when your customers are interacting with your emails. These reports can provide rich and granular data on how to optimize your emails to drive greater engagement. The email insights dashboard includes up to the last six months of data. To access the dashboard, go to **Analytics** > **Email Performance** > **Email Insights**.

### Engagement by Device

The **Engagement by Device** report provides a breakdown of what devices your users are using to engage with your email. This data tracks email engagement across mobile, desktop, tablet, and other device types. This data is based on the user agent string passed from your users' devices.

{% alert note %}
If you use CloudFront as your CDN, make sure your users' user agent is passed along to the ESP. Otherwise, every user agent will be "Amazon Cloudfront".
{% endalert %}

The “Other” category includes any user string that cannot be identified as desktop, mobile, or tablet. For example, television, car, video game console, OTT (over-the-top or streaming), and similar. This may also include null or empty values.

To better understand what is in this "Other" category, you can extract the user agents using either of these options:

1. [Currents]({{site.baseurl}}/user_guide/data/braze_currents) will send you the exact user agent string that was retrieved from your users' devices.
2. Leverage our [Query Builder]({{site.baseurl}}/user_guide/analytics/query_builder) to use SQL or our [AI Query Builder]({{site.baseurl}}/user_guide/analytics/query_builder#generating-sql-with-the-ai-query-builder) to view the user agents.

![Engagement by Device report that shows the number of clicks for mobile, desktop, tablet, and other devices. The most number of clicks occurs on mobile devices.]({% image_buster /assets/img/engagement_by_device_type.png %}){: style="max-width:70%;"}

For email opens, Braze will separate Google Image Proxy, Apple Image Proxy, and Yahoo Mail Proxy. These services will cache and load all embedded images in an email before it’s delivered to the recipient. As a result, this will trigger an email open from the mailbox provider’s servers rather than the recipient’s server, which can lead to inflated email opens. These services are meant to enhance privacy, security, performance, and efficiency when loading images. This can also contain real opens from recipients, as these proxy services mask the user agent, and we categorize proxy data using the user agent.

![Engagement by Device report that shows the number of clicks for Mobile, Desktop, Tablet, Apple Privacy Proxy, Google Image Proxy, Yahoo Mail Proxy, and Other. The most number of opens occurs on mobile devices.]({% image_buster /assets/img/engagement_by_device_type_proxy.png %}){: style="max-width:70%;"}

### Engagement by Mailbox Provider

The **Engagement by Mailbox Provider** report displays the top mailbox providers contributing to your clicks or opens. You can click into specific premier mailbox providers to drill down into specific receiving domains. For example, if Microsoft is listed on this report as one of your top mailbox provider metrics, you can further view details for their receiving domains, such as “outlook.com”, “hotmail.com”, “live.com”, and more.

![An example Engagement by Mailbox Provider report with Google, Apple iCloud, Yahoo, Microsoft, and Mail.Ru Group and their corresponding number of clicks.]({% image_buster /assets/img_archive/mailbox_provider_time_engagement.png %}){: style="max-width:70%;"}

### Time of Engagement

The **Time of Engagement** report displays data on when users are engaging with your emails. This can help answer questions such as which weekday or what time sees the highest engagement from your customers. With these insights, you can experiment with the best day or time to send your messages to drive higher engagement. Note that these times are based on your company’s time zone.

The **Day of the week** engagement report breaks down opens or clicks by day of the week. 

![An example Day of the week engagement report with the most clicks on Monday and Wednesday.]({% image_buster /assets/img_archive/time_engagement.png %})

The **Time of the day** engagement report breaks down opens or clicks by each hour in a 24-hour time window.

![An example Time of the day engagement report with the opens or clicks from 12 am to 11 pm.]({% image_buster /assets/img_archive/time_engagement_day.png %})

For more information on analytics for your emails, check out [Email reporting]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting/).

## SMS performance dashboard

To use your SMS performance dashboard, go to **Analytics** > **SMS Performance**, and select the date range for the period you want to view data. Your date range can be up to one year in the past.

### How metrics are calculated

![An example SMS campaign with 335,630 sends, with an average of 11,187.667 per day.]({% image_buster /assets/img_archive/email_performance_dashboard_2.png %}){: style="max-width:40%;float:right;margin-left:15px;border:none;"}

The calculations for different metrics in the SMS performance dashboard are the same as those on an individual message level (such as campaign analytics). On this dashboard, the metrics are aggregated across all campaigns and Canvases for the date range you've selected. To learn more about these definitions, refer to [SMS metrics]({{site.baseurl}}/sms_mms_rcs_reporting/).

Each tile shows the rate metric first, followed by the count metric (with the exception of _Sends_, which displays the count metric followed by the average per day). Each tile also shows the [comparison to the last period](#comparison-to-last-period-change-in-totals-or-rates).

| Metric | Type | Calculation |
| --- | --- | ---- |
| Sends | Count | Total number of sends across each day in the date range |
| Confirmed deliveries rate | Rate | (Total number of deliveries across each day in the date range) / (Total number of sends across each day in the date range) |
| Delivery failures rate | Rate | (Total number of failures across each day in the date range) / (Total number of sends across each day in the date range) |
| Rejections rate | Rate | (Total number of rejections across each day in the date range) / (Total number of sends across each day in the date range) |
| Click rate | Rate | (Total number of clicks across each day in the date range) / (Total number of deliveries across each day in the date range) |
| Total opt-ins | Rate | Total number of inbound message opt-ins across each day in the date range |
| Total opt-outs | Rate | Total number of inbound message opt-outs across each day in the date range |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Dashboard filters

You can filter the data on your dashboard using the following filter options:

- **Tag:** Choose one tag. When applied, your dashboard will show metrics for only your selected tag.
- **Canvas:** Choose up to 10 Canvases. When applied, your dashboard will show metrics for only your selected Canvases. If you select a tag filter first, then your options for Canvas filters will only include Canvases that have your selected tag.
- **Campaign:** Choose up to 10 campaigns. When applied, your dashboard will show metrics for only your selected campaigns. If you select a tag filter first, then your options for campaign filters will only include campaigns that have your selected tag.

![Filter options on the Channel Performance Dashboard where you can select a tag and list of Canvases to filter by.]({% image_buster /assets/img_archive/dashboard_filters.png %})

## Comparing time periods

The channel performance dashboard automatically compares the time period you have selected in the date range versus the prior time period, totaling the same number of days. For example, if you choose "Last 7 Days" as your date range in the dashboard, the comparison to the last period will compare the metrics from the last seven days against the seven days prior. If you select a custom date range—let's say May 10 to May 15, which is six days' worth of data—the dashboard will compare the metrics from across those days to the metrics from May 4 to May 9.

The comparison is the percentage change between the last and current periods, calculated by taking the difference between the two periods and dividing it by the metric from the last period.

### Viewing changes in total counts and rates

You can switch between **Show Change in Totals**—which compares the total counts (such as the number of emails delivered) between the two periods—and **Show Change in Rates**—which compares the rates (such as the delivery rate).

![Radio buttons to switch between showing change in totals or change in rates for the Channel Performance Dashboard.]({% image_buster /assets/img_archive/email_performance_dashboard_3.png %}){: style="max-width:60%"}

## Frequently asked questions

### Why is my dashboard displaying empty values?

There are a few scenarios that could lead to empty values for a metric:

- Braze recorded zeros for that particular metric in your selected date range.
- You haven't sent any messages during the selected date range.
- While there were metrics such as opens, clicks, or unsubscribes for a selected date range, there were no deliveries or sends. In this case, Braze will not calculate a rate metric.

To see more metrics, try expanding the date range.

### Why does my email dashboard display more Other Opens than Unique Opens?

For the _Unique Opens_ metric, Braze will deduplicate any repeat opens registered by a given user (whether they include _Machine Opens_ or _Other Opens_) so that only a single _Unique Open_ is incremented if a user opens multiple times. For _Other Opens_, Braze does not de-deduplicate.

<!---Temporarily hidden until functionality is added

## Empty values in your data

#### If a metric displays "0%" or "0"

This means Braze recorded zero for that particular metric during the time frame you've selected.

#### If a metric displays "N/A"

This means that while Braze recorded positive counts for a particular metric for the time frame you've selected, the denominator for the rate calculation (either sends or deliveries in most cases) was zero. This can occur when emails are sent out on one day and opens and clicks are recorded the following days if your selected time frame does not include the date the messages were sent.

#### If a metric displays "--"

This means Braze hasn't recorded any data for that metric during the time you selected. If you haven't set up or sent any emails yet, learn more about how to do so in our dedicated [Email]({{site.baseurl}}/user_guide/message_building_by_channel/email) section.

--->

