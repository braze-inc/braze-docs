---
nav_title: Export Revenue & Total Revenue Data
article_title: Export Revenue & Total Revenue Data
page_order: 4
page_type: reference
description: "This reference article covers revenue data and statistics."
tool: 
  - Reports

---

# Revenue data

On the **Revenue** page of the dashboard, you can view data on revenue or purchases over specific periods of time, for a specific product, or your app's total revenue or purchases.

{% alert tip %}
Looking for more ways to get revenue data? Try adding purchase behavior (as well as purchase of a product) to campaigns or Canvases as [conversion events]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/).
{% endalert %}

## Detailed statistics graph

The following data can be accessed via the **Detailed Statistics** graph:

- Purchases by Date
    - (Optional) Purchases for Different Products
- Revenue by Date
    - (Optional) Revenue for Different Segments
    - (Optional) Revenue for Different Products
- Revenue by Hour
    - (Optional) Hourly Revenue for Different Segments
- Revenue per User

![Revenue graph][9]

## Total revenue

You can view revenue statistics on a case-by-case basis on the [Campaign Analytics]({{site.baseurl}}/user_guide/data_and_analytics/your_reports/campaign_analytics/) or [Canvas Analytics]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/) pages. The Total Revenue statistic is generated from campaign recipients who have made a purchase within the campaign's primary conversion period.

{% alert tip %}
For help with CSV and API exports, refer to [Export troubleshooting]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/).
{% endalert %}

{% comment %}

## Direct revenue

You can view the following additional revenue metrics by generating a Campaign Comparison Report using the [Report Builder][1]:

- [Total Direct Revenue][2]
- [Total Direct Purchases][3]
- [Unique Direct Purchases][4]
- [Revenue per Recipient][5]

These metrics are based on last-click attribution, which means that in order for revenue to be attributed to a campaign, that campaign must:

1. Be the last campaign the user clicked prior to purchasing
    <br>**AND**<br>
2. Be clicked by the user less than 3 days prior to purchasing

{% endcomment %}

[1]: {{site.baseurl}}/user_guide/data_and_analytics/your_reports/report_builder/
[2]: {{site.baseurl}}/user_guide/data_and_analytics/report_metrics/#total-direct-revenue
[3]: {{site.baseurl}}/user_guide/data_and_analytics/report_metrics/#total-direct-purchases
[4]: {{site.baseurl}}/user_guide/data_and_analytics/report_metrics/#unique-direct-purchases
[5]: {{site.baseurl}}/user_guide/data_and_analytics/report_metrics/#revenue-per-recipient



[9]: {% image_buster /assets/img_archive/Export_revenue_graph.png %}
