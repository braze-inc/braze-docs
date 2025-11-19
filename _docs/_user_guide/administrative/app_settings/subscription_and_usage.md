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

The **Billing** page includes the following tabs:

- [Subscriptions and Usage](#subscriptions-and-usage)
- [Most Used Events and Attributes by App](#most-used-events-and-attributes-by-app)
- [Total Data Points Usage](#total-data-points-dashboard)

## Subscriptions and Usage

The **Subscriptions and Usage** tab includes usage graphs and your contract details. Data on this page is updated daily at 10 pm Eastern Time (ET). It does not reflect real-time activity.

### Usage graphs

Here, you'll find usage graphs that apply to your workspaces. You may find your own dashboard shows different usage metrics based on the products you have purchased. 

![Usage graph showing Monthly Unique Visitors]({% image_buster /assets/img/subscription_and_billing4.png %}){: style="max-width:90%;"}

These graphs can show monthly active users, monthly unique visitors, and email sends. Usage graphs like these are particularly helpful when trying to budget usage and gain a deeper understanding of what workspaces contribute to overall usage.

### Contract details

Contract details list the start and end date of your current contract with Braze.

## Most used events and attributes by app

Under **Most Used Events and Attributes By App**,  you can check the drivers of your attribute and custom event data point usage. 

![Most Used Events and Attributes By App]({% image_buster /assets/img/most_used_events_attributes_time.png %})

For each app, you can select **See breakdown** to view an estimated count of each specific custom attribute, profile attribute, and custom event for the selected time period as well as the percentage of that app's attribute and event updates that were driven by that attribute or event. 

![Most Used Events and Attributes By App breakdown tab]({% image_buster /assets/img/most_used_events_attributes_2.png %}){: style="max-width:60%"}

Data breakdowns like these can help you understand what specific data points are taking up large percentages of your allotment. We recommend that you monitor this information from time to time to make sure you aren't spending data points in accidental and unnecessary ways. Your customer success manager can provide guidance to get the most out of your current plan or provide options for greater flexibility. 

## Total data points dashboard

The **Total Data Points Usage** tab provides an in-depth look at your data point usage. You can view all data in this section aggregated by either weeks or months.

![Filtering Data Point Usage by weeks]({% image_buster /assets/img/subscription_and_billing2.png %})

### Contract details

Here, you'll find information on when your current Braze contract starts and ends, as well as allotted data points and a sum of all data points that have been used thus far in your current contract.

The fields in this section are defined as follows:

- **Contract Type:** Billing term structure, either Annual or Multi-Year.
- **Contract Start and End Date:** Start and end date of the entire contract.
- **Allotted Data Points:** The amount of data points allotted in the contract per billing term.
- **Contract Data Point Usage:** A cumulative total of all data points logged over the contract's lifetime, and does not reset in the next billing term.

![Contract Details section of Total Data Point Usage tab]({% image_buster /assets/img/contract_details.png %})

### Company billing data

#### App level total data point usage

This graph shows your data point usage across apps.

![App Level Total Data Point Usage shows data points used for each app.]({% image_buster /assets/img/app_level_total.png %})

Select one of the totals to view the **Data Point Usage Over Time** table, which shows your weekly data point totals for each workspace.  Rows that have a blank **App Name** column represent data points that aren't associated with any app (such as data points used in requests that don't specify an `app_id`).

![Data Point Usage Over Time showing total weekly data points for two workspaces.]({% image_buster /assets/img/data_point_usage_time.png %})

#### Workspace data point usage

This graph allows you to assess the total data point usage of a company by workspace. This graph gives you the ability to assess how each workspace is contributing to the company's data point usage.

![Workspace Data Point Usage graph for two workspaces]({% image_buster /assets/img/appgroup_datapoint_usage.png %}){: style="max-width:90%;"}

#### Billing cycle data point usage by event source

This graph allows you to view how data point usage is spread across different event sources, such as different API attributes, custom events, and sessions.

![Billing Cycle Data Point Usage by Event Source displaying the data point allocation among different event sources.]({% image_buster /assets/img/event_source_stats.png %})

#### Data point usage over time

This graph gives you the ability to quickly see your total data point usage versus your allotted amount of data points.

![Data Point Usage over time contrasting current billing cycle allotted data points with running total]({% image_buster /assets/img/company_data_point_usage_time.png %}){: style="max-width:90%;"}

