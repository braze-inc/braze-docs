---
nav_title: Engagement reports
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

> Engagement Reports let you pull engagement statistics for specific messages from campaigns and Canvases to receive as an email at your preferred time.

{% alert note %}
You need "Export User Data" permissions to run Engagement Reports.
{% endalert %}

With Engagement Reports, you can manually select campaigns and Canvases to include in your email report, or specify rules to automatically select relevant campaigns and Canvases.

Regardless of the number of campaigns or Canvases you select, up to two CSV files are generated—one for all campaign data and one for all Canvas data. You can access these CSV files from the link embedded inside your report email. Engagement Reports are not saved in the Braze dashboard.

Certain data is aggregated at the campaign or Canvas level versus at the individual campaign variant or Canvas step level. If you [delete a Canvas step after launch]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/change_your_canvas_after_launch/#canvas-details), this will also remove the data from Engagement Reports.

{% alert tip %}
You can re-run the report to generate updated statistics.
{% endalert %}

## Creating a new report

### Step 1: Create a report

In your dashboard account, go to **Analytics** > **Engagement Reports**. Select **+ Create New Report**.

### Step 2: Add messages

Add the campaigns and Canvas messages that you would like to compile in your report. You can select your messages in two ways:

- Manually select campaigns and Canvases
- Automatically select campaigns and Canvases based on specific rules

![engagement_reports_message_selection]({% image_buster /assets/img_archive/engagement_report_add_messages.png %})

#### Manually select campaigns or Canvases

This option gives you the freedom to choose whichever campaigns or Canvases you would like in this report.

#### Automatically select campaigns or Canvases

This option lets you automatically include all messages that include a specific [tag]({{site.baseurl}}/user_guide/administrative/app_settings/tags/). You can target messages that have any one or all of the tags listed. This option is useful if you are setting up recurring reports and you regularly tag your engagement messages.

### Step 3: Add statistics {#add-statistics-to-your-reports}

The **Add Stats** step shows you statistics for the types of campaigns or Canvases you have selected. For example, if you selected email messages, you can only view relevant email statistics. If you picked a combination of email and push, you can view the statistics for those two channels.

![engagement_report_add_stats]({% image_buster /assets/img_archive/engagement_report_add_stats.png %})

| Channel | Available statistics |
| ------| --------------|
| Email | Sends, Opens, Unique Opens, Clicks, Unique Clicks, Click to Open, Unsubscribes, Bounces, Delivered, Reported Spam |
| Push  | Sends, Opens, Influenced Opens, Bounces, Body Clicks |
| Web Push | Sends, Opens, Bounces, Body Clicks |
| In-app message | Impressions, Clicks, First Button Clicks, Second Button Clicks |
| Webhook  |  Sends, Errors |
| SMS | Sends, Sends to Carrier, Confirmed Deliveries, Delivery Failures, Rejections |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
*Sends to Carrier* is deprecated, but will continue to be supported for users that already have it.
{% endalert %}

### Step 4: Complete report setup

Give your report a name, choose how your report will be formatted, and select your recipients. By default, Engagement Reports are sent as a ZIP file where data is comma-delimited (where each piece of data is separated by a comma).

You can select from the following compression and delimiter options:

- **Compression:** ZIP, Uncompressed, or gzip
- **Delimiter:** Comma (`,`), Colon (`:`), Semicolon (`;`), or Pipe (`|`)

{% alert note %}
Statistics are only collected for the date range specified by the report. To receive accurate open and click rate statistics, select a date range that includes when the Sends events were performed for your campaigns and Canvases.
{% endalert %}

#### Select time frame

By default, the data range shown is based on your company's time zone and will go from the earliest message selected until the present date. You can customize this by selecting the date dropdown and using the custom range selection OR by selecting the next radio button and defining your date range with the dropdown options available.

#### Select data display

By default, the data displayed in the engagement reports is daily (one day). To view this data across different intervals, choose an explicit number of days or weeks to aggregate the data for the report. So instead of seeing daily metrics, you can view your engagement by week, month, quarter, or similar. Should a time-centric aggregation not suffice, you can also elect to export data at the campaign or Canvas level.

![engagement_reports_data_coverage]({% image_buster /assets/img_archive/engagement_report_datacoverage.png %})

#### Schedule your report

There are two options when scheduling your report:

- **Send immediately:** After the report is launched, Braze will send this report immediately.
- **Send at a designated time:** This option gives you the flexibility to choose how frequently you receive this report. You can choose to send this report every set number of days, weeks or months. You can also define when to stop sending the report.

![engagement_reports_schedule_report]({% image_buster /assets/img_archive/engagement_report_reportschedule.png %}){: style="max-width:65%;" }

### Step 5: Review and launch

The final step of setting up your report shows a view-only overview of your configured options. Review your report, and when you're satisfied, select **Launch Report**.

### Step 6: Check your email  

You will receive an email with links to your reports at your chosen time or schedule. **These links expire 1 hour after the report was sent.** When you select the provided links you will automatically download a ZIP file containing your CSV files-one for all campaigns.

The report contains all statistics selected in the [Add Stats](#add-statistics-to-your-reports) section of the setup process.


