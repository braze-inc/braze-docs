---
nav_title: Retention Reports
platform: Canvas
subplatform: Testing and More
page_order: 3

tools: canvas
page_type: reference
description: "This reference goes over how to measure user retention for users who performed a selected retention event in a specific canvas."
---

{% alert important %}
This report is not yet available to our clients deployed in our EU region, or on our HIPPA-compliant cluster. We will make this report available to those regions as we continue to deploy functionality across our entire platform.
{% endalert %}

# Retention Report

> This reference article goes over how to measure user retention for users who have performed a selected retention event in a specific Canvas. By knowing how your users are being retained after sending a message, you can measure the effectiveness of your Canvases.

User retention is one of the most important metrics for any marketer. Keeping engaged users coming back for more indicates that business is healthy.

Braze allows you to measure user retention right on the __Canvas Analytics__ page.

## Run a Retention Report

![Report Date][7]{: style="float:right;max-width:20%;margin-left:15px;"}

Get started by visiting any Canvas in your Braze Dashboard, and select a date range for your report.
This report will include all users who have __both__ entered the canvas and performed their retention event during this time period. To select a date range, you must navigate to the upper right-hand corner of the Canvas Analytics page, here, you may select various ranges or set a custom ranges for your report.

Next, select the Analyze Variants button at the bottom of the page. From here, you can analyze your variants, check out your funnel report, and view your retention report. Canvas Retention shows you the rate at which any user who has received this specific Canvas has performed a Retention Event (specified by you on the Retention Report) over the 30 days from the time they received the Canvas.

![Select a Retention event][1]{: style="max-width:80%"}

Once you've selected a Retention event, click "Run Report" to start the query.

![Run Report][2]{: style="max-width:80%"}

This query may take a few minutes to run, depending on how much data needs to be retrieved to generate the results. If it takes too long, you'll see a notification asking you to Retry loading the report again (just by clicking the "Retry" button in the body of the report.) You may need to wait up to five minutes before the report will load.

Once the report is generated, it can't be re-run with the same Retention event for 24 hours. You will always see a timestamp of when the report was last generated, and an option to Regenerate, if it's been more than a day. You can, however, change the Retention Event and re-run the report to look at the impact of the Canvas on different KPIs. 

![Full Report][6]{: style="max-width:70%"}

The report will only show days down the left column on which the Canvas was sending messages. For some Canvases, that may mean the report only shows one day if it was a one-and-done Canvas. If it's recurring or triggered, you may/will see multiple days down the left. 

## Report Explanation

Our Retention Report uses the Rolling Retention formula, which measures how many users come back and do the retention event __on or after__ any of the days listed across the top of the report. So, if a user started a session between day 3 and 7, the user will be counted as retained under the "3 days", "1 day", and "0 days" columns. Any user who is counted as retained after the 30-day mark from when the Canvas was sent on the date in the left column will be counted under the "30 days" column in that row.

__Braze Retention Reports Components:__
- __Users Column__: The value shown is the number of unique users that performed the start action within the selected time frame; the count of users for the present day will be excluded since it is being calculated. 
- __Cohort Z Rows__: Shows the days in which the Canvas was sending messages.
- __Day X Columns__: Days spanning between 0 and 30 days at various increments.
- __All Users Row__: Also known as the Report Summary Row, summarizes the retention data for the entire time period. Note that if a user has entered the canvas in multiple cohorts, their results will be counted twice here. 
- __Percentages/Numbers__: Shows the percentage/number of users who performed the event X or more days after receiving the Canvas on Z day. These percentages are the weighted average percentages. Incomplete values will be denoted by an asterisk.
- __Date Range__: Set on the Canvas Details page, the date range includes all users who have __both__ entered the canvas and performed their retention event during this time period.
- __Units__: You can adjust the units between the percentage of users and the number of users in the upper right-hand corner of the chart, specific units may prove to be more significant when judging the impact of a Canvas.
- __Color Mapping__: In your retention report, higher percentages/number of users are assigned darker shades of blue. Lower percentage/number of users, lighter shades of blue. This is done to help users visualize this data.
- __Retention Report Graph__: This graph summarizes the results for all cohorts for the selected date range.<br><br>

The way to read the retention report chart for the day 3 column would be Y% or Y number of users (based on units chosen) performed the event 3 or more days after receiving the Canvas on day Z. 

![Full Report][3]{: style="border:0"}

As another example, referring to the table above, on March 25th, a total of 38 users performed the retention event. Day 0 retention was 68.42%, meaning that 68.42% of users performed the retention event 0 or more days (on Day 0 or later) after receiving the Canvas. Day 7 retention was 57.89%, meaning 57.89% of users performed the event 7 or more days (on Day 7 or later) after receiving the Canvas.

This information can be useful if you want to know the percentage of users who have and have not used your product 30+ days after first use. A percentage/number value in the day 30 column tells you the percentage of users who returned on day 30 or after. 

### Things to Look For in your Retention Reports

Retention Reports are easy to generate, yet challenging to interpret and act on. To help aid marketers, we have assembled a couple of topics/questions to consider when looking at your Retention Reports.

- Day-of-week trends for recurring Canvases (e.g Do Monday cohorts perform better than Saturday cohorts?)
- Where does the impact start to decline? This could be a signal that a new Canvas that targets users at that point in time is needed as another boost to retention. 
- Am I seeing Canvas fatigue? 
- Did that optimization to this Canvas I made X days ago have a positive impact?


[1]: {% image_buster /assets/img/retention_1.png %}
[2]: {% image_buster /assets/img/retention_2.png %}
[3]: {% image_buster /assets/img/campaign_retention2.png %}
[4]: {% image_buster /assets/img/retention_report_full_report.png %}
[6]: {% image_buster /assets/img/canvas_retention_report.png %}
[7]: {% image_buster /assets/img/date_select_retention.png %}
