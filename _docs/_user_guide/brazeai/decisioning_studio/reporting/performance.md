---
nav_title: Performance
article_title: Performance report
page_order: 1
description: "Learn how to use the Performance report to compare treatment groups and control groups in BrazeAI Decisioning Studio."
---

# Performance report

The performance report offers high-level agent metrics that compare treatment groups (from Braze) to one or more control groups (like revenue). It supports two different views: **Trending** and **Driver Tree**.

By default, the report uses the **Trending** view, which compares how BrazeAI™ performs over time compared to your control groups, and tracks the uplift evolution.

![Performance report trending view showing a line chart comparing BrazeAI™ and control group performance over time. The chart displays two lines labeled BrazeAI™ and Control, with the y-axis labeled Uplift and the x-axis showing dates. A legend identifies each group by color.]({% image_buster /assets/img/decisioning_studio/reporting_agent_performance_trending.png %})

Alternatively, you can select **Driver Tree** to view how key value drivers are linked to target metrics, helping you better understand the relationship between them.

![Performance report driver tree view showing a hierarchical diagram that maps key value drivers to target metrics. The diagram displays several connected nodes, each labeled with a driver or metric name, illustrating how different factors contribute to overall performance.]({% image_buster /assets/img/decisioning_studio/reporting_performance_drivertree.png %})

To compare performance between two groups, use the dropdowns to select your desired comparison criteria. Refer to the following table for more details:

| Field | Description |
|-------|-------------|
| Comparison groups | The groups that you want to compare in your report. |
| Aggregation | The way the report groups data, such as totals, averages, or percentages. |
| Segments | The [audience segments]({{site.baseurl}}/user_guide/engagement_tools/segments/) that you created in Braze. |
| Timeline events | The specific events shown over time, such as message sends, opens, or conversions. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
