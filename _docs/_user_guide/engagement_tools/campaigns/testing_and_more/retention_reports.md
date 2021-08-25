---
nav_title: Retention Reports
article_title: Retention Reports
page_order: 4
tool: 
  - Campaigns
  - Reports
page_type: reference
description: "This reference article goes over how to measure user retention for users who performed a selected retention event in a specific campaign."

---

> TO BE MERGED AND RELOCATED

# Retention Report

> This reference article goes over how to measure user retention for users who have performed a selected retention event in a specific campaign. By knowing how your users are being retained after sending a message, you can measure the effectiveness of your campaign.

User retention is one of the most important metrics for any marketer. Keeping engaged users coming back for more indicates that business is healthy. Braze allows you to measure user retention right on the __Campaign Analytics__ page. 

{% alert important %}
Please note that Retention Reports are available for both Canvases and campaigns, currently excluding SMS and API-triggered campaigns.
{% endalert %}

## Run a Retention Report

![Report Date][7]{: style="float:right;max-width:20%;margin-left:15px;"}

Get started by visiting any campaign in your Braze Dashboard, and select a date range for your report. Selecting an appropriate date range is crucial because of the way it affects the retention reports. This report will include all users who initially received the campaign __during this window__, and of those users, the data of those that __performed their retention event during the date range__ will appear in the report. To select a date range, you must navigate to the upper right-hand corner of the Campaign Analytics page, here, you may select various ranges or set a custom range for your report.

Next, scroll down to the Campaign Retention section. Currently, Campaign Retention shows you the rate at which any user who has received this specific campaign has performed a Retention Event (specified by you on the Retention Report) over the 30 days from the time they received the campaign.

![Select a Retention event][1]{: style="max-width:80%"}

Once you've selected a Retention event, click "Run Report" to start the query.

![Run Report][2]{: style="max-width:80%"}

This query may take a few minutes to run, depending on how much data needs to be retrieved to generate the results. If it takes too long, you'll see a notification asking you to Retry loading the report again (just by clicking the "Retry" button in the body of the report.) You may need to wait up to five minutes before the report will load.

Once the report is generated, it can't be re-run with the same Retention event for 24 hours. You will always see a timestamp of when the report was last generated, and an option to Regenerate, if it's been more than a day. You can, however, change the Retention Event and re-run the report to look at the impact of the campaign on different KPIs. 

![Full Report][6]

The report will only show days down the left column on which the campaign was sending messages. For some campaigns, that may mean the report only shows one day if it was a one-and-done campaign. If it's recurring or triggered, you may/will see multiple days down the left. 

## Report Explanation

Our Retention Report offers both a Rolling Retention and Range Retention formula. To view your campaign report with one of these retention types, select the __Rolling Retention__ or __Range Retention__ radio dial listed under the Type of Retention.

### Rolling Retention
Rolling retention measures how many users come back and do the retention event __on or after any of the days listed__ across the top of the report. So, if a user started a session between day 3 and 7, the user will be counted as retained under the "3 days", "1 day", and "0 days" columns. Any user who is counted as retained after the 30-day mark from when the campaign was sent on the date in the left column will be counted under the "30 days" column in that row.

### Range Retention
Range retention measures how many users come back __in the range of days listed__ across the top of the report. So, if a user started a session between days 3 and 7 and then again on day 13, they would be counted as retained under both "Day 3-7" and "Day 7-14" ranges.

__Braze Retention Reports Components:__
- __Users Column__: The value shown is the number of unique users that performed the start action within the selected time frame; the count of users for the present day will be excluded since it is being calculated. 
- __Cohort Z Rows__: Shows the days in which the campaign was sending messages.
- __Day X Columns__: Days spanning between 0 and 30 days at various increments.
- __All Users Row__: Also known as the Report Summary Row, summarizes the retention data for the entire time period. Note that if a user has received the campaign in multiple cohorts, their results will be counted twice here. 
- __Percentages/Numbers__: Shows the percentage/number of users who performed the event X or more days after receiving the campaign on Z day. These percentages are the weighted average percentages. Incomplete values will be denoted by an asterisk.
- __Date Range__: Set on the Campaign Details page, the date range includes all users who received the campaign during this window, and of those users, the data of those that performed their retention event during the date range will appear in the report.
- __Units__: You can adjust the units between the percentage of users and the number of users in the upper right-hand corner of the chart, specific units may prove to be more significant when judging the impact of a campaign.
- __Color Mapping__: In your retention report, higher percentages/number of users are assigned darker shades of blue. Lower percentage/number of users, lighter shades of blue. This is done to help users visualize this data.
- __Retention Report Graph__: This graph summarizes the results for all cohorts for the selected date range.<br><br>


{% tabs %}
{% tab Range Report %}
__How to Read a Range Retention Report__

Range Reports are some of the most intuitive reports to read. They clearly state, of all the users in a cohort, what percentage of those users performed the retention event within a given date range. For example, in the image shown below, referencing the All Users Cohort, on date range "Day 0 (0-24hrs)", 35.71% of the cohort performed the retention report. If a user performs multiple retention events within multiple date ranges, they will be counted as retained for each range. 

![Retention Report]({% image_buster /assets/img/range_retention.png %})

{% endtab %}

{% tab Rolling Retention %}
__How to Read a Rolling Retention Report__

The way to read the retention report chart for a day 3 column would be Y% or Y number of users (based on units chosen) performed the event 3 or more days after receiving the campaign on day Z. 

![Rolling Report]({% image_buster /assets/img/campaign_retention3.png %})

As another example, referring to the table above, on the 25th of March, a total of 38 users performed the retention event. Day 0 retention was 68.42%, meaning that 68.42% of users performed the retention event 0 or more days (on Day 0 or later) after receiving the campaign. Day 7 retention was 57.89%, meaning 57.89% of users performed the event 7 or more days (on Day 7 or later) after receiving the campaign.

This information can be useful if you want to know the percentage of users who have and have not used your product 30+ days after first use. A percentage/number value in the day 30 column tells you the percentage of users who returned on day 30 or after. 

{% endtab %}
{% endtabs %}

### Performance by Variant

Viewing your Retention Report by variant allows you to compare rolling retention for each variant or message variation for the selected time period, as well as the Control Group. This report can be viewed by toggling the Retention Report from "Entire Campaign" to "By Variant". 

Report by Variant Use Cases:
- Have some variants or experiments in which the results seem like a wash or have no statistical significance? Take another look and see if one or the other had a longer-tail impact.
- See what retention looks like if you didn’t send that message by digging into the Control group’s retention data.<br><br>

![View by Variant][8]

__Braze Retention Reports By Variant Components:__
- __Date Range__: Set on the Campaign Details page, the date range includes all users who received the campaign during this window, and of those users, the data of those that performed their retention event during the date range will appear in the report. Each day the retention rate, percentage change from the control group, and confidence are measured.
- __Retention Rate__: Shows the retention rate by variant. The retention rate is equivalent to the number of users that performed the retention event divided by the total users that have received the campaign.
- __Recentage Change from Control__: Quantifies the percentage change per variant from the control group.
- __Confidence__: Braze compares each variant’s conversion rate against the control’s conversion rate with a statistical procedure called a Z Test to calculate a [confidence][3] percentage. This percentage signifies how confidently that variant is performing better than the control group.
- __Units__: You can adjust the units between the percentage of users and the number of users in the upper right-hand corner of the chart, specific units may prove to be more significant when judging the impact of a campaign.
- __Variant Graph__: This graph summarizes the results by variant for the selected date range.

If you're looking for information on Canvas retention reports by variant, take a look at [this article][9]

### Things to Look For in your Retention Reports

Retention Reports are easy to generate, yet challenging to interpret and act on. To help aid marketers, we have assembled a couple of topics/questions to consider when looking at your Retention Reports.

- Day-of-week trends for recurring campaigns (e.g Do Monday cohorts perform better than Saturday cohorts?)
- Where does the impact start to decline? This could be a signal that a new campaign that targets users at that point in time is needed as another boost to retention. 
- Am I seeing campaign fatigue? 
- Did that optimization to this campaign I made X days ago have a positive impact?


[1]: {% image_buster /assets/img/retention_1.png %}
[2]: {% image_buster /assets/img/retention_2.png %}
[3]: {{site.baseurl}}/user_guide/intelligence/multivariate_testing/#understanding-confidence
[6]: {% image_buster /assets/img/campaign_retention3.png %})
[7]: {% image_buster /assets/img/date_select_retention.png %}
[8]: {% image_buster /assets/img/variant_view.png %}
[9]: {{site.baseurl}}/user_guide/engagement_tools/canvas/retention_reports/#performance-by-variant

