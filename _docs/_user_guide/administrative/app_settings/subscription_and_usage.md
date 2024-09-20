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

> Use this page as a self-serve tool to monitor and check your data consumption.

To navigate to the **Billing** page, go to **Settings** > **Billing**.

{% alert note %}
If you are using the [older navigation]({{site.baseurl}}/navigation), you can find this page by selecting your account icon, then select **Subscriptions and Usage**.
{% endalert %}

The **Billing** page includes the following tabs:

- [Subscriptions and Usage](#subscriptions-and-usage)
- [Most Used Events and Attributes by App](#most-used-events-and-attributes-by-app)
- [Total Data Points Usage](#total-data-points-dashboard)

## Subscriptions and Usage

The **Subscriptions and Usage** tab includes usage graphs and your contract details.

### Usage graphs

Here, you will find usage graphs that apply to your workspaces. You may find your own dashboard shows different usage metrics based on the products you have purchased.

![Usage graph showing Monthly Unique Visitors][3]{: style="max-width:90%;"}

These graphs can show monthly active users, monthly unique visitors, and email sends. Usage graphs like these are particularly helpful when trying to budget usage and gain a deeper understanding of what workspaces contribute to overall usage.

### Contract details

Contract details list the start and end date of your current contract with Braze.

## Most used events and attributes by app

The **Most Used Events and Attributes By App** tab is a useful tool to understand the drivers of your attribute and custom event data point consumption. For each app, you can find an estimated count of each specific custom attribute, profile attribute, and custom event for the selected time period as well as the percentage of that app's attribute and event updates that were driven by that attribute or event. 

Data breakdowns like these can help you understand what specific data points are taking up large percentages of your allotment. We recommend that you monitor this information from time to time to make sure you aren't spending data points in accidental and unnecessary ways. Your customer success manager can provide guidance to get the most out of your current plan or provide options for greater flexibility. 

![Most Used Events and Attributes By App][4]

## Total data points dashboard

The **Total Data Points Usage** tab provides an in-depth look at your data point consumption. You can view all data in this section aggregated by either weeks or months. Click **Update** to apply any changes.

![Filtering Data Point Usage by weeks][2]

### Contract details

Here, you'll find information on when your current Braze contract starts and ends, as well as allotted data points and a sum of all data points that have been used thus far in your current contract.

The fields in this section are defined as follows:

- **Contract Type:** Billing term structure, either Annual or Multi-Year.
- **Contract Start and End Date:** Start and end date of the entire contract.
- **Allotted Data Points:** The amount of data points allotted in the contract per billing term.
- **Contract Data Point Usage:** A cumulative total of all data points consumed over the contract's lifetime, and does not reset in the next billing term.

![Contract Details section of Total Data Point Usage tab][5]

### Current billing cycle

This section of the dashboard displays the data point usage for the current billing cycle. This includes the following information for the current billing cycle:

- Start date 
- End date  
- Allotted number of data points 
- Total data point usage 

![Current Billing Cycle section of Total Data Points Usage tab][6]{: style="max-width:90%;"}

### Company billing data

#### Usage across workspaces

This graph allows you to assess the total data point usage of a company by workspace. This graph gives you the ability to assess how each workspace is contributing to the company's data point usage.

![Workspace Data Point Usage graph for two workspaces][7]{: style="max-width:90%;"}

#### Data point usage over time

This graph gives you the ability to quickly see your total data point usage versus your allotted amount of data points. 

![Data Point Usage over time contrasting current billing cycle allotted data points with running total][8]{: style="max-width:90%;"}

### Workspace billing data

{% alert note %}
The workspace billing data and workspace charts only display for dates after October 1, 2021. 
{% endalert %}

#### Drill to workspaces

The **Drill to Workspaces** lets you view granular data point data for each of your workspaces. Click a workspace to see its data point details.

![Drill to workspaces for billable data points][9]{: style="max-width:90%;"}

##### Workspace level data point usage by category

Select the menu next to a workspace name and then **Billable Data Points For WORKSPACE_NAME** to view the **Workspace Level Data Point Usage by Category** table. This table shows you data point counts for each category of data points. For example, you can see the number of data points driven by sessions and custom events. You can use this table to identify the categories of data points that are driving data point consumption for the workspace.

![Workspace Level Data Point Usage by Category][10]{: style="max-width:90%;"}

##### Workspace level data point usage over time

The **Workspace Level Data Point Usage over Time** table shows you how that workspace's data point usage has changed throughout your billing cycle.

![Workspace Level Data Point Usage over Time][11]{: style="max-width:90%;"}

##### Appl level total data point usage

The **App Level Total Data Point Usage** table shows you data point usage for each of the apps in your workspace. You can use this table to identify which apps are driving data point consumption for the workspace.

![App Level Total Data Point Usage table for multiple apps][12]{: style="max-width:90%;"}


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