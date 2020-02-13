---
nav_title: Retention Reports
platform: Campaigns
subplatform: Testing and More
page_order: 8

tools: campaigns
page_type: reference
description: "This reference goes over how to measure user retention for users who received any message in a specific campaign."
---

# Retention Report

> This reference goes over how to measure user retention for users who received any message in a specific campaign.
> <br>
> <br>
> By knowing how your users are being retained after sending a message, you can measure the effectiveness of your campaign.

{% alert important %}
This report is not yet available to our clients deployed in our EU region, or on our HIPPA-compliant cluster. We will make this report available to those regions as we continue to deploy functionality across our entire platform.
{% endalert %}

User retention is one of the most important metrics to any marketer. Keeping engaged users coming back for more indicates that business is healthy.

Braze allows you to measure user retention right on the Campaign Analytics page.

Get started by visiting any campaign in your Braze Dashboard, and scrolling down to the Campaign Retention section. Currently, Campaign Retention shows you the rate at which any user who has received this specific campaign has performed a Retention Event (specified by you on the Retention Report) over the 30 days from the time they received the campaign

![Select a Retention event][1]

Once you've selected a Retention event, click "Run Report" to start the query

![Run Report][2]

This query may take a few minutes to run, depending on how much data needs to be retrieved to generate the results. If it takes too long, you'll see a notification asking you to Retry loading the report again (just by clicking the "Retry" button in the body of the report.) You may need to wait up to five minutes before the report will load.

![Retry][3]

Once the report is generated, it can't be re-run with the same Retention event for 24 hours. You will always see a timestamp of when the report was last generated, and an option to Regenerate, if it's been more than a day.

![Full Report][4]

The report will only show days down the left column on which the campaign was sending messages. For some campaigns, that may mean the report only shows one day if it was a one-and-done campaign. If it's recurring or triggered, you may/will see multiple days down the left.

Additionally, our Retention Report uses the Rolling Retention formula, which measures how many users come back and do the Retention event on or after any of the days listed across the top of the report. So, if a user, say, Started Session between day 3 and 7, the user will be counted as retained under the "3 days" column. Any user who is counted as retained aftere the 30-day mark from when the campaign was sent on the date in the left column will be counted under the "30 days" column in that row.


[1]: {% image_buster /assets/img/retention_report_select_retention.png %}
[2]: {% image_buster /assets/img/retention_report_run_report.png %}
[3]: {% image_buster /assets/img/retention_report_retry.png %}
[4]: {% image_buster /assets/img/retention_report_full_report.png %}
