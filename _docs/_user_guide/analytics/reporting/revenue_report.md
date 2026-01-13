---
nav_title: Revenue report
article_title: Revenue Report
page_type: reference
description: "This page describes how to use the Revenue Report page to view data on revenue over specific periods of time, a specific product revenue, and your app’s total revenue."
tool: Reports
---

# Revenue Report

> The Revenue Report page allows you to view data on revenue over specific periods of time, a specific product revenue, and your app’s total revenue.

To view a report for your revenue from the dashboard, go to **Analytics** > **Revenue Report**. 

## Customize your revenue report

You can customize your revenue report by selecting a date range, the apps to report on, and parameters.

![The "Revenue Report" page showing the "Performance Over Time" graph with "Revenue" set as the parameter.]({% image_buster /assets/img/revenue_report.png %})

### Filter by date and apps

Select the date range for your revenue report and, if you like, a specific app or selection of apps.

### Filter by parameters

The **Performance Over Time** graph shows the data for different parameters, which can be selected in the **Statistics for** dropdown. You can optionally breakdown the data of certain parameters in the **Breakdown** dropdown.

You can view the following data in the **Performance Over Time Graph**:
- KPI Formulas
- Purchases
    - (Optional) Purchases By Product
- Revenue
    - (Optional) Revenue By Segment
    - (Optional) Revenue By Product
- Revenue per Hour
    - (Optional) Revenue per Hour By Segment
- Revenue per User

## View the product breakdown

Refer to the **Product Breakdown** table for a list of the products purchased during your selected date range, how many of each product were purchased, and how much revenue each product generated.

![The "Product Breakdown" table showing the columns "Product Name", "Purchased", and "Revenue".]({% image_buster /assets/img/revenue_report_product_breakdown.png %})

## Metrics and calculations

{% alert note %}
When you record revenue for a currency without an exchange rate, Braze records it as a purchase of US $0.00.
{% endalert %}

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>Metric</th>
            <th>Definition</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#lifetime-revenue">Lifetime Revenue</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Lifetime Revenue' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#lifetime-value-per-user">Lifetime Value Per User</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Lifetime Value Per User' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#average-daily-revenue">Average Daily Revenue</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Average Daily Revenue' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#daily-purchases">Daily Purchases</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Daily Purchases' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#daily-revenue-per-user">Daily Revenue Per User</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Daily Revenue Per User' %}</td>
        </tr>
    </tbody>
</table>

## Export revenue and total revenue data

Use the [Revenue Report]({{site.baseurl}}/user_guide/analytics/reporting/revenue_report/) page of the dashboard to view data on revenue over specific periods of time, a specific product revenue, and your app's total revenue.

You can find the **Revenue Report** under **Analytics**.

{% alert tip %}
Looking for more ways to get revenue data? Try adding purchase behavior (as well as purchase of a product) to campaigns or Canvases as [conversion events]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/).
{% endalert %}

To export your revenue data, select <i class="fas fa-bars" title="Chart context menu"></i> in the **Performance Over Time** graph and select your export option.

### Performance Over Time graph

The following data can be viewed in the **Performance Over Time** graph:

- KPI Formulas
- Purchases
    - (Optional) Purchases By Product
- Revenue
    - (Optional) Revenue By Segment
    - (Optional) Revenue By Product
- Revenue per Hour
    - (Optional) Revenue per Hour By Segment
- Revenue per User

![Revenue graph]({% image_buster /assets/img_archive/Export_revenue_graph.png %})

### Total revenue

You can view revenue statistics on a case-by-case basis on the [Campaign Analytics]({{site.baseurl}}/user_guide/analytics/reporting/campaign_analytics/) or [Canvas Analytics]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/) pages. 

{% multi_lang_include analytics/metrics.md metric='Total Revenue' %}

{% alert tip %}
Revenue reports cannot be exported through API. For help with CSV exports, refer to [export troubleshooting]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %}

{% comment %}

### Direct revenue

You can view the following additional revenue metrics by generating a Campaign Comparison Report using the [Report Builder]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/):

- [Total Direct Revenue]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/#total-direct-revenue)
- [Total Direct Purchases]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/#total-direct-purchases)
- [Unique Direct Purchases]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/#unique-direct-purchases)
- [Revenue per Recipient]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/#revenue-per-recipient)

These metrics are based on last-click attribution, which means that revenue will be attributed to a campaign if that campaign:

1. Is the last campaign the user clicked prior to purchasing
    <br>**AND**<br>
2. Was clicked by the user less than 3 days prior to purchasing

{% endcomment %}
