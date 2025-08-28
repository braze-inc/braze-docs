---
nav_title: Creating a formula
article_title: Creating a Formula
page_order: 1.2
page_type: reference
description: "This reference article covers creating and managing formulas, which help you easily understand complex relationships that exist in your data."
tool: Reports

---
# Creating a formula

> When viewing analytics in Braze, you can combine multiple data points to get valuable insights into your user data. These are referred to as formulas. Use formulas to normalize your time series data based on your total number of monthly active users (MAU) and daily active users (DAU). 

Formulas help you understand complex relationships that exist in your data. For example, you can compare how many custom events were completed by daily active users that qualify for a particular segment versus the general population (or against another segment).

## Use cases

Formulas, especially when combined with custom events, can help you understand user behaviors within your app. Formulas can also lend deeper insight into segment purchasing patterns, even if your company uses paid media in conjunction with Braze, such as Google Ads or TV. 

The following are some examples of the kinds of behavior patterns that can be detected using formulas:

- **Ride-sharing apps:** If you have a custom event for when the user cancels a ride, you can configure a function for Canceled Rides / DAU to find if certain user segments tend to cancel more rides than others.
- **eCommerce apps:** By configuring a function for purchases of a certain product ID / MAU, you can compare the popularity of a recently promoted product between segments, even if all the promotions couldn't be tracked using Braze.
- **Media apps using ads:** If the users' experience is interrupted by ads between video or audio clips, recording mid-ad exits as a custom event and calculating the ratio of mid-ad exits / DAU can help find the best segments to target with a campaign for ad-free premium subscriptions.

## Creating formulas

Formulas can be accessed in the statistics panels on the [Home]({{site.baseurl}}/user_guide/analytics/dashboard/home_dashboard/), [Revenue Report]({{site.baseurl}}/user_guide/data/export_braze_data/exporting_revenue_data/), and [Custom Events Report]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) pages in the dashboard. To view this panel, go to the **Performance Over Time** chart, change the **Statistics For** dropdown to **KPI Formulas**, and then select at least one KPI formula to populate the chart.

![View statistics for KPI formulas in the Braze dashboard]({% image_buster /assets/img_archive/kpi_forms.png %})

To create a new formula:

1. Go to the appropriate dashboard (**Home**, **Revenue Report**, or **Custom Events Report**).
2. Select **Manage KPI Formulas**.
3. Enter a name for your formula.
4. Select the relevant numerators and denominators.
5. Select **Save**.

## Available numerators and denominators

<style>
  div.small_table + table {
    max-width: 50%;
  }
  div.large_table + table {
    max-width: 75%;
  }
table th:nth-child(1),
table th:nth-child(2),
table th:nth-child(3),
table td:nth-child(1),
table td:nth-child(2),
table td:nth-child(3) {
    width:25%;
}
table td {
    word-break: break-word;
}
</style>

<div class="small_table"></div>

### Overview dashboard

| Numerators | Denominators |
| --- | --- |
| DAU | MAU |
| Sessions | DAU |
| | Segment size |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Revenue dashboard

| Numerators | Denominators |
| --- | --- |
| Purchases (all) | DAU |
| Select purchases (such as a gift card or product ID) | MAU |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Custom event dashboard

| Numerators | Denominators |
| --- | --- |
| Custom event count | MAU |
|  | DAU |
|  | Segment size (only segments that have [analytics tracking]({{site.baseurl}}/viewing_and_understanding_segment_data/) enabled can be used) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

