---
nav_title: Export Revenue & Total Revenue Data
page_order: 4

page_type: reference
description: "This reference article covers revenue data and statistics."
tool: 
- Dashboard
- Reports
---

# Revenue Data

On the Revenue page of the Dashboard, you can view data on revenue or purchases over specific periods of time, or your app's total revenue or purchases.

## Detailed Statistics Graph
![Revenue graph][9]

The following data can be accessed via the Detailed Statistics graph:
- Revenue by Date
    - (Optional) Revenue for Different Segments
    - (Optional) Revenue for Different Products
- Purchases by Date
    - (Optional) Purchases for Different Products
- Revenue by Hour
    - (Optional) Hourly Revenue for Different Segments
- Revenue per User

## Total Revenue

You can view revenue statistics on a case-by-case basis on the Analytics pages for your campaigns. The Total Revenue statistic is generated from campaign recipients who have made a purchase within the campaign's primary conversion period.

{% alert tip %}
For help with CSV and API exports, visit our troubleshooting article [here]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/).
{% endalert %}

## Direct Revenue

You can view the following additional revenue metrics by generating a Campaign Comparison Report using the [Report Builder][1]:

- [Total Direct Revenue][2]
- [Total Direct Purchases][3]
- [Unique Direct Purchases][4]
- [Revenue per Recipient][5]

These metrics are based on last-click attribution, which means that in order for revenue to be attributed to a campaign, that campaign must:

1. Be the last campaign the user clicked prior to purchasing, and
2. Be clicked by the user less than 3 days prior to purchasing.

[1]: {{site.baseurl}}/user_guide/data_and_analytics/your_reports/report_builder/
[2]: {{site.baseurl}}/user_guide/data_and_analytics/report_metrics/#total-direct-revenue
[3]: {{site.baseurl}}/user_guide/data_and_analytics/report_metrics/#total-direct-purchases
[4]: {{site.baseurl}}/user_guide/data_and_analytics/report_metrics/#unique-direct-purchases
[5]: {{site.baseurl}}/user_guide/data_and_analytics/report_metrics/#revenue-per-recipient



[9]: {% image_buster /assets/img_archive/Export_revenue_graph.png %}
