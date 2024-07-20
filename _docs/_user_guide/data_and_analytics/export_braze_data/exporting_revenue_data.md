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

> On the [Revenue Report]({{site.baseurl}}/user_guide/data_and_analytics/reporting/revenue_report/) page of the dashboard you can view data on revenue over specific periods of time, a specific product revenue, and your app's total revenue.

You can find the **Revenue Report** under **Analytics**.

{% alert note %}
If you are using the [older navigation]({{site.baseurl}}/navigation), you can find **Revenue** under **Data**.
{% endalert %}

{% alert tip %}
Looking for more ways to get revenue data? Try adding purchase behavior (as well as purchase of a product) to campaigns or Canvases as [conversion events]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/).
{% endalert %}

To export your revenue data, click <i class="fas fa-bars" title="Chart context menu"></i> in the **Performance Over Time** graph and select your export option.

## Performance Over Time graph

The following data can be accessed via the **Performance Over Time** graph:

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

You can view revenue statistics on a case-by-case basis on the [Campaign Analytics]({{site.baseurl}}/user_guide/data_and_analytics/reporting/campaign_analytics/) or [Canvas Analytics]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/) pages. The Total Revenue statistic is generated from campaign recipients who have made a purchase within the campaign's primary conversion period.

{% alert tip %}
Revenue reports cannot be exported via API. For help with CSV exports, refer to [export troubleshooting]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/).
{% endalert %}

{% comment %}

## Direct revenue

You can view the following additional revenue metrics by generating a Campaign Comparison Report using the [Report Builder]({{site.baseurl}}/user_guide/data_and_analytics/reporting/report_builder/):

- [Total Direct Revenue]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/#total-direct-revenue)
- [Total Direct Purchases]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/#total-direct-purchases)
- [Unique Direct Purchases]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/#unique-direct-purchases)
- [Revenue per Recipient]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/#revenue-per-recipient)

These metrics are based on last-click attribution, which means that in order for revenue to be attributed to a campaign, that campaign must:

1. Be the last campaign the user clicked prior to purchasing
    <br>**AND**<br>
2. Be clicked by the user less than 3 days prior to purchasing

{% endcomment %}

[1]: {{site.baseurl}}/user_guide/data_and_analytics/reporting/report_builder/
[2]: {{site.baseurl}}/user_guide/data_and_analytics/report_metrics/#total-direct-revenue
[3]: {{site.baseurl}}/user_guide/data_and_analytics/report_metrics/#total-direct-purchases
[4]: {{site.baseurl}}/user_guide/data_and_analytics/report_metrics/#unique-direct-purchases
[5]: {{site.baseurl}}/user_guide/data_and_analytics/report_metrics/#revenue-per-recipient



[9]: {% image_buster /assets/img_archive/Export_revenue_graph.png %}
