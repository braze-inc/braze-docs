---
nav_title: Revenue Report
article_title: Revenue Report
page_type: reference
description: "This reference article covers the the Revenue Report page."
tool: Reports
---

# Revenue Report

> The Revenue Report page allows you to view data on revenue over specific periods of time, a specific product revenue, and your app’s total revenue.

To view a report for your revenue from the dashboard, go to **Analytics** > **Revenue Report**. 

{% alert note %}
If you are using the [older navigation]({{site.baseurl}}/navigation), this page can be found under **Data**.
{% endalert %}

## Customizing your revenue report

You can customize your revenue report by selecting a date range, the apps to report on, and parameters.

![The "Revenue Report" page showing the "Performance Over Time" graph with "Revenue" set as the parameter.][1]

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

- *Lifetime revenue* is the total `PurchaseEvents` `price` value (in USD) received since inception. 
- *Lifetime value per user* is the *Lifetime revenue* divided by your total *Users* (located on your **Home** page).
- Average *Daily revenue* is the average of the sum of the campaign and Canvas revenue for a given day.
- *Daily Purchases* is the average of the total unique `PurchaseEvents` over the time period.
- *Daily revenue per user* is the average daily revenue per daily active user.

## Viewing the product breakdown

Refer to the **Product Breakdown** table for a list of the products purchased during your selected date range, how many of each product were purchased, and how much revenue each product generated.

![The "Product Breakdown" table showing the columns "Product Name", "Purchased", and "Revenue".][2]


[1]: {% image_buster /assets/img/revenue_report.png %}
[2]: {% image_buster /assets/img/revenue_report_product_breakdown.png %}
