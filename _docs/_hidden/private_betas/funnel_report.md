---
nav_title: Funnel Report
title: Funnel Report
description: ""
permalink: "/funnel_report/"
hidden: true
---
{% alert note %}
This Funnel Report feature is currently in Beta. Please reach out to your Braze account manager for more information.
{% endalert %}

# Funnel Report

> Customer Retention is an important metric to understand because, with the proper tools, you can use customer data to optimize your marketing strategies and increase customer's lifetime value. The best part is that Braze already has tools to handle this. With campaigns, your company can run multiple variants, gaining data on what is most effective for your customers. And now, with Braze's new feature, Funnel Reporting, we can offer a visual reporting metric alongside those multivariant campaigns, making data-driven solutions easier to understand and implement. 

![Funnel Report 2][2]{: style="float:right;max-width:25%;margin-left:15px;margin-bottom:15px"}

Funnel Reporting offers a visual report for campaigns with a control group and/or multiple variants, allowing you to directly compare these variables with dynamic tables and stats for each variant pair. Companies can now use this information to help them understand how the different variants have impacted the conversion funnel at a more granular level, and optimize based on this data. 

![Funnel Report 1][1]{:height="500px"}

# Funnel Report Set Up

The funnel reporting feature is available through the Campaigns page in the Dashboard. Funnel Reports can be made for existing active campaigns and should be set up soon after the campaign is launched. These reports show a series of events that a campaign recipient progresses through over a period of one (1) to thirty (30) days from the date they received the message. A user is considered converted through a step in the funnel if they perform the event in the specified order.

## Select Events for Funnel Steps

From the Campaigns page, with your active campaign selected, you will be able to scroll past campaign details and see the Funnel Report option.

![Funnel Report 3][3]{:height="400px"} 

For every funnel report, the first event will be when the user receives your message. From there, the subsequent events you choose will funnel the number of users who performed those events, as well as the previous events. While building the funnel report, you must also choose the time window you would like the report to span. 

For example, if you select a 7-day report time window, followed by the events "added to cart" and "made a purchase", you will see the number of users who both added to cart within 7 days of receiving the message, as well as the number of users who added to cart and then made a purchase within seven days of receiving the campaign. 

Once you have selected Build Report, generating the funnel report may take several minutes. 

## Interpreting your Funnel Report

![Funnel Report 1][1]{:height="500px"}

The horizontal axis on the chart displays the percentage of message recipients who performed those actions. 
The grey arrow showing a percentage between two actions (currently only viewable in campaigns with 1 variant), represents the percentage of users who satisfied the previous step and went on to perform the next action.

__For campaigns with multiple variants__: Braze will show a table that displays metrics for each event and variant, the conversion rate is the number of users who performed the event (and subsequent ones) per message recipients.

__For campaigns with re-eligibility__: If a user receives the campaign more than once in the report time window, Braze will determine whether the user should be included in the funnel based on what happened after on the first time they received the campaign within the time window.

__For multi-variant campaigns with re-eligibility__: If a user receives multiple variants from the campaign during the report time window, Braze will determine whether they should be included in the variant funnel based on what happened after the first time they received the campaign variant - this means that the same user could count towards multiple different variants if they received multiple variants during the time window for the funnel

[1]:{% image_buster /assets/img/funnel_report/funnel_report1.jpg %}
[2]:{% image_buster /assets/img/funnel_report/funnel_report2.png %}
[3]:{% image_buster /assets/img/funnel_report/funnel_report3.png %}

