---
nav_title: Billing
article_title: Billing
alias: /subscription_and_usage/
page_order: 25
page_type: reference
description: "This reference article covers the Billing page, where you can monitor and check your data consumption."
tool: Dashboard
search_rank: 5
---

# Billing

> Learn how to use the **Billing** page to monitor and check your data consumption across workspaces, apps, and event sources. This article covers the different sections on the page and the information they can provide you.

To navigate to the **Billing** page, go to **Settings** > **Billing**.

{% alert note %}
If you're using the [older navigation]({{site.baseurl}}/navigation), you can find this page by selecting your account icon, then selecting **Subscriptions and Usage**.
{% endalert %}

The **Billing** page includes the following tabs:

- [Subscriptions and Usage](#subscriptions-and-usage)
- [Most Used Events and Attributes by App](#most-used-events-and-attributes-by-app)
- [Total Data Points Usage](#total-data-points-dashboard)

## Subscriptions and Usage

The **Subscriptions and Usage** tab includes usage graphs and your contract details.

### Usage graphs

Here, you'll find usage graphs that apply to your workspaces. You may find your own dashboard shows different usage metrics based on the products you have purchased. 

![Usage graph showing Monthly Unique Visitors][3]{: style="max-width:90%;"}

These graphs can show monthly active users, monthly unique visitors, and email sends. Usage graphs like these are particularly helpful when trying to budget usage and gain a deeper understanding of what workspaces contribute to overall usage.

### Contract details

Contract details list the start and end date of your current contract with Braze.

## Most used events and attributes by app

Under **Most Used Events and Attributes By App**,  you can check the drivers of your attribute and custom event data point consumption. 

![Most Used Events and Attributes By App][4]

For each app, you can select **See breakdown** to view an estimated count of each specific custom attribute, profile attribute, and custom event for the selected time period as well as the percentage of that app's attribute and event updates that were driven by that attribute or event. 

![Most Used Events and Attributes By App breakdown tab][1]

Data breakdowns like these can help you understand what specific data points are taking up large percentages of your allotment. We recommend that you monitor this information from time to time to make sure you aren't spending data points in accidental and unnecessary ways. Your customer success manager can provide guidance to get the most out of your current plan or provide options for greater flexibility. 

## Total data points dashboard

The **Total Data Points Usage** tab provides an in-depth look at your data point consumption. You can view all data in this section aggregated by either weeks or months.

![Filtering Data Point Usage by weeks][2]

### Contract details

Here, you'll find information on when your current Braze contract starts and ends, as well as allotted data points and a sum of all data points that have been used thus far in your current contract.

The fields in this section are defined as follows:

- **Contract Type:** Billing term structure, either Annual or Multi-Year.
- **Contract Start and End Date:** Start and end date of the entire contract.
- **Allotted Data Points:** The amount of data points allotted in the contract per billing term.
- **Contract Data Point Usage:** A cumulative total of all data points consumed over the contract's lifetime, and does not reset in the next billing term.

![Contract Details section of Total Data Point Usage tab][5]

### Company billing data

#### App level total data point usage

This graph shows your data point usage across apps.

![App Level Total Data Point Usage shows data points used for each app.][14]

Select one of the totals to view the **Data Point Usage Over Time** table, which shows your weekly data point totals for each workspace.  Rows that have a blank **App Name** column represent data points that aren't associated with any app (such as data points used in requests that don't specify an `app_id`).

![Data Point Usage Over Time showing total weekly data points for two workspaces.][15]

#### Workspace data point usage

This graph allows you to assess the total data point usage of a company by workspace. This graph gives you the ability to assess how each workspace is contributing to the company's data point usage.

![Workspace Data Point Usage graph for two workspaces][7]{: style="max-width:90%;"}

#### Billing cycle data point usage by event source

This graph allows you to view how data point usage is spread across different event sources, such as different API attributes, custom events, and sessions.

![Billing Cycle Data Point Usage by Event Source displaying the data point allocation among different event sources.][13]

#### Data point usage over time

This graph gives you the ability to quickly see your total data point usage versus your allotted amount of data points.

![Data Point Usage over time contrasting current billing cycle allotted data points with running total][8]{: style="max-width:90%;"}

[1]: {% image_buster /assets/img/most_used_events_attributes_2.png %}
[2]: {% image_buster /assets/img/subscription_and_billing2.png %}
[3]: {% image_buster /assets/img/subscription_and_billing4.png %}
[4]: {% image_buster /assets/img/most_used_events_attributes_time.png %}
[5]: {% image_buster /assets/img/contract_details.png %}
[6]: {% image_buster /assets/img/current_billing_cycle.png %}
[7]: {% image_buster /assets/img/appgroup_datapoint_usage.png %}
[8]: {% image_buster /assets/img/company_data_point_usage_time.png %}
[9]: {% image_buster /assets/img/appgroup_drilldown.png %}
[10]: {% image_buster /assets/img/appgroup_level_datapoint_usage_bycategory.png %}
[11]: {% image_buster /assets/img/appgroup_level_usage_time.png %}
[12]: {% image_buster /assets/img/app_level_stats.png %}
[13]: {% image_buster /assets/img/event_source_stats.png %}
[14]: {% image_buster /assets/img/app_level_total.png %}
[15]: {% image_buster /assets/img/data_point_usage_time.png %}