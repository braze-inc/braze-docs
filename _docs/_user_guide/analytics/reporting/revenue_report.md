---
nav_title: Revenue Report
article_title: Revenue Report
page_type: reference
description: "This page describes how to use the Revenue Report page to view data on revenue over specific periods of time, a specific product revenue, and your app’s total revenue."
tool: Reports
---

# Revenue Report

> The Revenue Report page allows you to view data on revenue over specific periods of time, a specific product revenue, and your app’s total revenue.

To view a report for your revenue from the dashboard, go to **Analytics** > **Revenue Report**. 

## Customizing your revenue report

You can customize your revenue report by selecting a date range, the apps to report on, and parameters.

![The "Revenue Report" page showing the "Performance Over Time" graph with "Revenue" set as the parameter.]({% image_buster /assets/img/revenue_report.png %})

### Filtering by date and apps

Select the date range for your revenue report and, if you like, a specific app or selection of apps.

### Filtering by parameters

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

## Understanding revenue calculations

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

## Viewing the product breakdown

Refer to the **Product Breakdown** table for a list of the products purchased during your selected date range, how many of each product were purchased, and how much revenue each product generated.

![The "Product Breakdown" table showing the columns "Product Name", "Purchased", and "Revenue".]({% image_buster /assets/img/revenue_report_product_breakdown.png %})


