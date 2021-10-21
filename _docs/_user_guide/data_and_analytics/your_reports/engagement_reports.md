---
nav_title: Engagement Reports
article_title: Engagement Reports
page_order: 3
local_redirect:
  report-glossary: '/docs/user_guide/data_and_analytics/report_metrics/'
page_type: tutorial
description: "This how-to article walks you through creating, personalizing, and scheduling Engagement Reports for campaigns and Canvases."
tool:
  - Campaigns
  - Canvas
  - Reports
---
# Engagement reports

Engagement Reports are Braze's custom reporting tool, where you can pull engagement statistics for specified messages from campaigns and Canvases.

- The report is exported as a link embedded inside of a triggered email.
- Regardless of the number of campaigns or Canvases selected, only a maximum of two `.csv` files will be generated - one for all of the campaign data, and one for all of the Canvas data.
- Certain data is aggregated at the ‘campaign’ or 'Canvas' level versus at the individual 'variant' or 'step' level.

{% alert tip %}
Reports are not saved in the dashboard, and re-running the report can result in updated statistics.
{% endalert %}

## Create a new report

![GIF of creating an engagement report]({% image_buster /assets/img/engagement_reports.gif %}){: style="float:right;max-width:50%;border:0px;"}

1. In your dashboard account, navigate to **Engagement Reports**, under **Data**.
2. Click **+ Create New Report**.
3. Add the [campaigns and Canvas messages](#manually-select-campaigns-or-canvases) (individually or [by tag](#automatically-select-campaigns-or-canvases)) that you would like to compile in your report.
4. [Add statistics](#add-statistics-to-your-report) to your report.
5. Select the compression and deliminator for your report.
6. Enter the email addresses of Braze users who should receive this report.
7. Select the [time frame](#time-frame) from which you would like your report to run data.
8. Select the [intervals (daily, weekly, etc.)](#data-display) at which would like to see the breakdown of your data.
9. Schedule your report to [send immediately](#send-immediately) or at a [future, specified time](#send-at-designated-time).
10. Run the report, then open it in your email when it arrives!

{% alert note %}
Your Braze user account must have ‘Export User Data’ access to utilize Engagement Reports.
{% endalert %}

---

## Add messages to your report

The Add Messages tab allows you to select your messages in two ways:

![engagement_reports_message_selection][2]

### Manually select campaigns or canvases

This option gives you the freedom to choose whichever campaigns or Canvases you would like in this report.

### Automatically select campaigns or canvases

This option gives you the ability to automatically include all messages based on a specific tag. You can target messages that have any one or all of the tags listed.  This option is useful if you are setting up recurring reports and utilize our tagging system.


## Add statistics to your report

The Stats tab will automatically show you stats for the types of campaigns or Canvases you have selected.  For instance, if you picked Email messages, you will only see the Email Stats.  If you picked a combination of Email and Push, you will see the stats for those two channels.

![engagement_report_add_stats][3]

| channel| stats available|
| ------| --------------|
| Email | Sends, Opens, Unique Opens, Clicks, Unique Clicks, Unsubscribes, Bounces, Delivered, Reported Spam |
| Push  | Sends, Opens, Influenced Opens, Bounces, Body Clicks |
| Web Push | Sends, Opens, Bounces, Body Clicks |
| In-App Message | Impressions, Clicks, First Button Clicks, Second Button Clicks |
| Webhook  |  Sends, Errors |
| SMS | Sends, Sends to Carrier, Confirmed Deliveries, Delivery Failures, Rejections |
{: .reset-td-br-1 .reset-td-br-2}

## Set up report data coverage & distribution

The Set Up Report tab allows you to enter your report name, select the compression and delimiter of the report and include whom you would like to send this report to.  

![engagement_reports_data_coverage][4]

### Time frame

By default, the data range shown will go from the earliest message selected until the present date.  You can customize this by selecting the date dropdown and using the custom range selection OR by selecting the next radio button and defining your date range with the dropdown options available.

### Data display

By default, the data displayed in the engagement reports is daily (1 day). Should you like to view this data across different intervals, you can choose an explicit number of days or weeks to aggregate the data for the report. So instead of seeing daily metrics, you can look at your engagement by week, month, quarter, etc. Should a time-centric aggregation not suffice, you can also elect to export data at the campaign or Canvas level.

## Schedule your report

There are two options when scheduling your report:

![engagement_reports_schedule_report][5]{: style="max-width:65%;" }

### Send immediately

After the report is saved, Braze will send this report Immediately

### Send at a designated time

This option gives you the flexibility to choose how frequently you would like to receive this report.  You can choose to send this report every X days, weeks or months.  Additionally, you can define when to stop sending the report.

## Open report  

You will receive an email with links to your reports. When you click on the provided links you will automatically download a `.zip` file containing your `.csv` files - one for all Campaigns.

The report, when opened, will contain all the statistics selected in the [Add Stats](#add-statistics-to-your-reports) section of the setup process.



[2]: {% image_buster /assets/img_archive/engagement_report_add_messages.png %}
[3]: {% image_buster /assets/img_archive/engagement_report_add_stats.png %}
[4]: {% image_buster /assets/img_archive/engagement_report_datacoverage.png %}
[5]: {% image_buster /assets/img_archive/engagement_report_reportschedule.png %}
