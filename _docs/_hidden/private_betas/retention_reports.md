---
nav_title: Retention Report by Variant
page_type: reference
permalink: "/report_by_variant/"
hidden: true
---

{% alert note %}
This Performance by Variant feature is currently in Beta. Please reach out to your Braze account manager for more information.
{% endalert %}

# Retention Report - Performance by Variant

Viewing your Retention Report by variant allows you to compare rolling retention for each variant or message variation for the selected time period, as well as the Control Group. This report can be viewed by toggling the Retention Report from "Entire Campaign/Canvas" to "By Variant". 

Report by Variant Use Cases:
- Have some variants or experiments in which the results seem like a wash or have no statistical significance? Take another look and see if one or the other had a longer-tail impact.
- See what retention looks like if you didn’t send that message by digging into the Control group’s retention data.<br><br>

![View by Variant][5]

__Braze Retention Reports Components:__
- __Date Range__: Set on the Campaign/Canvas Details page, the date range includes all users who received the campaign during this window, and of those users, the data of those that performed their retention event during the date range will appear in the report. Each day the retention rate, percentage change from the control group, and confidence are measured.
- __Retention Rate__: Shows the retention rate by variant. The retention rate is equivalent to the number of users that performed the retention event divided by the total users that have received the campaign/canvas.
- __Recentage Change from Control__: Quantifies the percentage change per variant from the control group.
- __Confidence__: Braze compares each variant’s conversion rate against the control’s conversion rate with a statistical procedure called a Z Test to calculate a [confidence][3] percentage. This percentage signifies how confidently that variant is performing better than the control group.
- __Units__: You can adjust the units between the percentage of users and the number of users in the upper right-hand corner of the chart, specific units may prove to be more significant when judging the impact of a campaign/canvas.
- __Variant Graph__: This graph summarizes the results by variant for the selected date range.

To check out the rest of the Retention Report documentation, visit our [Campaign][1] and [Canvas][2] Retention Report pages. 


[1]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/retention_reports/
[2]: {{site.baseurl}}/user_guide/engagement_tools/canvas/retention_reports/
[3]: {{site.baseurl}}/user_guide/intelligence/multivariate_testing/#understanding-confidence
[5]: {% image_buster /assets/img/variant_view.png %}
