---
nav_title: Subscriptions and Usage
article_title: Dashboard Subscription and Usage
alias: /subscription_and_usage/
page_order: 4.1
page_type: reference
description: "This reference article covers the Subscriptions and Usage page, where you can monitor and check your data consumption."
tool: Dashboard

---

# Subscriptions and usage

To navigate to the **Subscriptions and Usage** page, select your account icon on the dashboard and select **Subscriptions and Usage** from the dropdown menu. Customers are encouraged to use this page as a self-serve tool to monitor and check their data consumption. 

## Page contents

### Usage graphs

Here, you will find usage graphs that apply to your app groups. You may find your own dashboard shows different usage metrics based on the products you have purchased.

![Usage graphs showing Monthly Active Users, Monthly Unique Visitors, and email sends][3]{: style="max-width:90%;"}

Usage graphs like these are particularly helpful when trying to budget usage and gain a deeper understanding of what app groups contribute to overall usage.

### Contract details

Contract details list the start and end date of your current contract with Braze.

## Total data points dashboard

Your **Data Points Usage** can be found under the **Total Data Points Usage** tab. You can view all data in this section aggregated by either weeks or months. Click **Run** to apply any changes.

![Filtering Data Point Usage by weeks][2]{: style="max-width:80%;"}

### Contract details

Here, you’ll find information on when your current Braze contract starts and ends, as well as allotted data points and a sum of all data points that have been used thus far in your current contract.

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

#### Usage across app groups

This graph allows you to assess the total data point usage of a company by app group. This graph gives you the ability to assess how each app group is contributing to the company's data point usage.

![App Group Data Point Usage graph for two app groups][7]{: style="max-width:90%;"}

#### Data point usage over time

This graph gives you the ability to quickly see your total data point usage versus your allotted amount of data points. 

![Data Point Usage over time contrasting current billing cycle alloted data points with running total][8]{: style="max-width:90%;"}

### App group billing data

{% alert note %}
The app group billing data and app group charts only display for dates after October 1, 2021. 
{% endalert %}

#### Drill to app groups

The **Drill to App Groups** lets you view granular data point data for each of your app groups. Click an app group to see its data point details.

![Drill to app groups for billable data points][9]{: style="max-width:90%;"}

The **App Group Level Data Point Usage by Category** table enables you to see data point counts for each category of data points. For example, you can see the number of data points driven by sessions and custom events. You can use this table to identify the categories of data points that are driving data point consumption for the app group.

![App Group Level Data Point Usage by Category][10]{: style="max-width:90%;"}

The **App Group Level Data Point Usage over Time** table enables you to see how that app group’s data point usage has changed throughout your billing cycle.

![App Group Level Data Point Usage over Time][11]{: style="max-width:90%;"}

The **App Level Total Data Point Usage** table enables you to see data point usage for each of the apps in your app group. You can use this table to identify which apps are driving data point consumption for the app group.

![App Level Total Data Point Usage table for multiple apps][12]{: style="max-width:90%;"}

## Most used events and attributes by app

The **Most Used Events and Attributes By App** page is a useful tool to understand the drivers of your attribute and custom event data point consumption. For each app, you can find an estimated count of each specific custom attribute, profile attribute, and custom event for the selected time period as well as the percentage of that app’s attribute and event updates that were driven by that attribute or event. 

Data breakdowns like these can help customers understand what specific data points are taking up large percentages of your allotment. We recommend customers monitor this information from time to time to make sure they aren’t spending data points in accidental and unnecessary ways. 

![Most Used Events and Attributes By App][4]



[2]: {% image_buster /assets/img/subscription_and_billing2.png %}
[3]: {% image_buster /assets/img/subscription_and_billing3.png %}
[4]: {% image_buster /assets/img/most_used_events_attributes_time.png %}
[5]: {% image_buster /assets/img/contract_details.png %}
[6]: {% image_buster /assets/img/current_billing_cycle.png %}
[7]: {% image_buster /assets/img/appgroup_datapoint_usage.png %}
[8]: {% image_buster /assets/img/company_data_point_usage_time.png %}
[9]: {% image_buster /assets/img/appgroup_drilldown.png %}
[10]: {% image_buster /assets/img/appgroup_level_datapoint_usage_bycategory.png %}
[11]: {% image_buster /assets/img/appgroup_level_usage_time.png %}
[12]: {% image_buster /assets/img/app_level_stats.png %}