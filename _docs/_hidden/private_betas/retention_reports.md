---
nav_title: Retention Reports
platform: Campaigns
subplatform: Testing and More
page_order: 3

tools: campaigns
page_type: reference
description: "This reference goes over how to measure user retention for users who performed a selected retention event in a specific campaign."
---

# Retention Report

> This reference article goes over how to measure user retention for users who have performed a selected retention event in a specific campaign. <br>By knowing how your users are being retained after sending a message, you can measure the effectiveness of your campaign.

{% alert important %}
This report is not yet available to our clients deployed in our EU region, or on our HIPPA-compliant cluster. We will make this report available to those regions as we continue to deploy functionality across our entire platform.
{% endalert %}

![Full Report][4]{: style="float:right;max-width:40%;margin-left:15px;"}

User retention is one of the most important metrics for any marketer. Keeping engaged users coming back for more indicates that business is healthy.

Braze allows you to measure user retention right on the __Campaign Analytics__ page.

## Run a Retention Report

Get started by visiting any campaign in your Braze Dashboard, and scrolling down to the Campaign Retention section. Currently, Campaign Retention shows you the rate at which any user who has received this specific campaign has performed a Retention Event (specified by you on the Retention Report) over the 30 days from the time they received the campaign.

![Select a Retention event][1]

Once you've selected a Retention event, click "Run Report" to start the query.

![Run Report][2]

This query may take a few minutes to run, depending on how much data needs to be retrieved to generate the results. If it takes too long, you'll see a notification asking you to Retry loading the report again (just by clicking the "Retry" button in the body of the report.) You may need to wait up to five minutes before the report will load.

![Retry][3]

Once the report is generated, it can't be re-run with the same Retention event for 24 hours. You will always see a timestamp of when the report was last generated, and an option to Regenerate, if it's been more than a day. You can, however, change the Retention Event and re-run the report to look at the impact of the campaign on different KPIs. 

![Full Report][4]

The report will only show days down the left column on which the campaign was sending messages. For some campaigns, that may mean the report only shows one day if it was a one-and-done campaign. If it's recurring or triggered, you may/will see multiple days down the left. 

## Report Explanation

Our Retention Report uses the Rolling Retention formula, which measures how many users come back and do the retention event __on or after__ any of the days listed across the top of the report. So, if a user started a session between day 3 and 7, the user will be counted as retained under the "3 days", "1 day", and "0 days" columns. Any user who is counted as retained after the 30-day mark from when the campaign was sent on the date in the left column will be counted under the "30 days" column in that row.

__Braze Retention Reports Components:__
- __Users Column__: The value shown is the number of unique users that performed the start action within the selected time frame; the count of users for the present day will be excluded since it is being calculated. 
- __Date Z Rows__: Shows the days in which the campaign was sending messages.
- __Day X Columns__: Days spanning between 0 and 30 days at various increments.
- __Percentages/Numbers__: Shows the percentage/number of users who performed the event X or more days after receiving the campaign on Z day. These percentages are the weighted average percentages. Incomplete values will be denoted by an asterisk.
- __Units__: You can adjust the units between the percentage of users and the number of users in the upper right-hand corner of the chart, specific units may prove to be more significant when judging the impact of a campaign.
- __Color Mapping__: In your retention report, higher percentages/number of users are assigned darker shades of blue. Lower percentage/number of users, lighter shades of blue. This is done to help users visualize this data.<br><br>

The way to read the retention report chart for the day 3 column would be Y% or Y number of users (based on units chosen) performed the event 3 or more days after receiving the campaign on day Z. 

![Full Report][4]

As another example, referring to the table above, on January 28th, a total of 19 users performed the retention event. Day 0 retention was 73.68%, meaning that 73.68% of users performed the retention event 0 or more days (on Day 0 or later) after receiving the campaign. Day 1 retention was 68.42%, meaning 68.42% of users performed the event 1 or more days (on Day 1 or later) after receiving the campaign.

This information can be useful if you want to know the percentage of users who have and have not used your product 30+ days after first use. A percentage/number value in the day 30 column tells you the percentage of users who returned on day 30 or after. 

### Things to Look For in your Retention Reports

Retention Reports are easy to generate, yet challenging to interpret and act on. To help aid marketers, we have assembled a couple of topics/questions to consider when looking at your Retention Reports.

- Day-of-week trends for recurring campaigns (e.g Do Monday cohorts perform better than Saturday cohorts?)
- Where does the impact start to decline? This could be a signal that a new campaign that targets users at that point in time is needed as another boost to retention. 
- Am I seeing campaign fatigue? 
- Did that optimization to this campaign I made X days ago have a positive impact?


[1]: {% image_buster /assets/img/retention_report_select_retention.png %}
[2]: {% image_buster /assets/img/retention_report_run_report.png %}
[3]: {% image_buster /assets/img/retention_report_retry.png %}
[4]: {% image_buster /assets/img/retention_report_full_report.png %}
