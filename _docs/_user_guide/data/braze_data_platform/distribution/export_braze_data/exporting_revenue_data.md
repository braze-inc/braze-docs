---
nav_title: Export Revenue & Total Revenue Data
article_title: Export Revenue & Total Revenue Data
page_order: 4
page_type: reference
description: "This reference article covers how to export revenue data and statistics."
tool: 
  - Reports

---

# Export revenue and total revenue data

> This page covers the [Revenue Report]({{site.baseurl}}/user_guide/analytics/reporting/revenue_report/) page of the dashboard, where you can view data on revenue over specific periods of time, a specific product revenue, and your app's total revenue.

You can find the **Revenue Report** under **Analytics**.

{% alert tip %}
Looking for more ways to get revenue data? Try adding purchase behavior (as well as purchase of a product) to campaigns or Canvases as [conversion events]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/).
{% endalert %}

To export your revenue data, select <i class="fas fa-bars" title="Chart context menu"></i> in the **Performance Over Time** graph and select your export option.

## Performance Over Time graph

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

## Total revenue

You can view revenue statistics on a case-by-case basis on the [Campaign Analytics]({{site.baseurl}}/user_guide/analytics/reporting/campaign_analytics/) or [Canvas Analytics]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/) pages. 

{% multi_lang_include analytics/metrics.md metric='Total Revenue' %}

{% alert tip %}
Revenue reports cannot be exported through API. For help with CSV exports, refer to [export troubleshooting]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %}

{% comment %}

## Direct revenue

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




