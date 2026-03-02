---
nav_title: Insights
article_title: Insights report
page_order: 2
description: "Learn how to use the Insights report to understand how recommendation options in your action bank are generated in BrazeAI Decisioning Studio."
---

# Insights report

Insights show you how the various recommendation options in your action bank are generated, like block selection. There are two different insights reports: **Agent preferences** and **SHAPs**.

{% tabs local %}
{% tab agent preferences %}
The **Agent preferences** report helps you identify seasonal trends and assess the relevance of the choices in the action bank, guiding informed decisions for updates.

![Agent preferences report showing a bar chart comparing how often different recommendation options were selected over a specific time period. The chart displays several colored bars, each representing a recommendation option from the action bank, with the y-axis labeled as percent of time chosen and the x-axis listing option names.]({% image_buster /assets/img/decisioning_studio/reporting_insights_agent_preferences.png %})

Refer to the following table for more details about this report:

| Field | Description |
|-------|-------------|
| Dimension | The attribute used to organize results, such as channel, campaign, or platform. |
| Comparison group | The groups that you want to compare in your report. You can select multiple comparison groups. |
| Parameter | The metric applied to that attribute, such as opens, clicks, or conversion rate. |
| Segment | The [audience segment]({{site.baseurl}}/user_guide/engagement_tools/segments/) that you created in Braze. |
| Option             | The specific recommendation option selected from the action bank. |
| Description        | A short explanation of what the option represents.            |
| # of times chosen  | The total count of how often the option was selected.         |
| % of time chosen   | The percentage of total selections where this option was chosen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
{% endtab %}

{% tab shaps %}
The **SHAPs** report uses the Shapley Additive exPlanations (SHAP) model to help you quantify how each feature or variable contributes to your recommendation agent. Each point on the chart represents one SHAP and the distribution of the points represent a general sense of a feature's directional impact.

![SHAPs report chart displaying a horizontal bar graph with multiple colored bars representing different features or variables. Each bar shows the impact of a feature on the recommendation agent, with the x-axis labeled SHAP value and the y-axis listing feature names such as Recency, Frequency, and Channel. The chart visualizes how each feature contributes positively or negatively to the agent's predictions.]({% image_buster /assets/img/decisioning_studio/reporting_insights_shaps.png %})

{% endtab %}
{% endtabs %}
