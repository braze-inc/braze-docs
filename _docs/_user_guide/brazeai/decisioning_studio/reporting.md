---
nav_title: Viewing reports
article_title: Viewing decisioning studio reporting
page_order: 3
description: "Learn how to view BrazeAI Decisioning Studio™ reports in Braze, so you can understand how AI-powered decisions impact your campaigns."
---

# Viewing decisioning studio reports

> Learn how to view BrazeAI Decisioning Studio™ reports in Braze, so you can understand how AI-powered decisions impact your campaigns. From performance metrics to data health and system changes, these reports help you understand results, troubleshoot issues, and make informed decisions with confidence.

## Prerequisites

Before you can view decisioning studio reports in the Braze, you'll need to:

- Have an active contract for Braze and BrazeAI Decisioning Studio™. 
- Contact your CSM to enable BrazeAI Decisioning Studio™ for you on your behalf.
- Have a live BrazeAI Decisioning Studio™ agent.

## Viewing reports {#view}

To view metrics for a decisioning studio agents in Braze, go to **AI Decisioning** > **BrazeAI Decisioning Studio™**, then select an agent.

![BrazeAI Decisioning Studio™ reporting home screen showing a dashboard with multiple report cards. Each card displays a report type such as Performance, Insights, Diagnostics, and Timeline, with brief descriptions and icons for each.]( {% image_buster /assets/img/decisioning_studio/reporting_home.png %} )

Here, you can view reports like performance, insights, diagnostics, and timelines. For more details, see [Available reports](#reports).

## Changing report dates

After [opening a report](#view), you can change the date range by selecting a new start and end date from the calendar dropdown.

![BrazeAI Decisioning Studio™ date range selector open with a calendar dropdown. The calendar displays selectable start and end dates for customizing the report view.]({% image_buster /assets/img/decisioning_studio/reporting_change_date_range.png %}){: style="max-width:50%;"}

You can also set a default start date or choose dates to always exclude. Excluded dates will be filtered out of all reports for that agent.

To set or exclude dates, select <i class="fa-solid fa-gear"></i> **Settings**, then change your default date or exclude dates as needed.

![Settings panel open in BrazeAI Decisioning Studio™ showing options to set a default start date and exclude specific dates from reports. The panel displays two sections labeled Default start date and Exclude dates. Under Exclude dates, several dates are listed with checkboxes next to each.]({% image_buster /assets/img/decisioning_studio/reporting_set_exclude_dates.png %})

## Available reports {#reports}

### Performance

The performance report offers high-level agent metrics that compare treatment groups (from Braze) to one or more control groups, (like revenue). It supports two different views: **Trending** and **Driver Tree**.

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

### Insights

Insights show you how the various recommendation options in your action bank are generated, like SL or block selection. There's two different insights reports: **Agent preferences** and **SHAPs**.

{% tabs local %}
{% tab agent preferences %}
The **Agent preferences** report helps you identify seasonal trends and assess the relevance of the choices in the action bank, guiding informed decisions for updates.

![Agent preferences report showing a bar chart comparing how often different recommendation options were selected over a specific time period. The chart displays several colored bars, each representing a recommendation option from the action bank, with the y-axis labeled as percent of time chosen and the x-axis listing option names.]({% image_buster /assets/img/decisioning_studio/reporting_insights_agent_preferences.png %})

Refer to the following table for more details about this report:

| Field | Description |
|-------|-------------|
| Dimension | The attribute used to organize results, such as channel, campaign, or platform. |
| Comparison group | The groups that you want to compare in your report. You can select multiple comparison groups, up to NUM. |
| Parameter | The metric applied to that attribute, such as opens, clicks, or conversion rate. |
| Segment | The [audience segment]({{site.baseurl}}/user_guide/engagement_tools/segments/) that you created in Braze. |
| Option             | The specific recommendation option selected from the action bank. |
| Description        | A short explanation of what the option represents.            |
| # of times chosen  | The total count of how often the option was selected.         |
| % of time chosen   | The percentage of total selections where this option was chosen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
{% endtab %}

{% tab shaps %}
The **SHAPs** report uses the Shapley Additive exPlanations (SHAP) model to help you quantify how each feature or variable contributes to your recommendation model. Each point on the chart represents one SHAP and the distribution of the points represent a general sense of a feature's directional impact.

![SHAPs report chart displaying a horizontal bar graph with multiple colored bars representing different features or variables. Each bar shows the impact of a feature on the recommendation model, with the x-axis labeled SHAP value and the y-axis listing feature names such as Recency, Frequency, and Channel. The chart visualizes how each feature contributes positively or negatively to the model's predictions.]({% image_buster /assets/img/decisioning_studio/reporting_insights_shaps.png %})

{% endtab %}
{% endtabs %}

### Diagnostics

The diagnostics report contains two different report types: **Outbound** and **Inbound**.

{% tabs local %}
{% tab outbound %}
The outbound diagnostics report shows the daily volume of recommendations generated and activated across your audiences. Use it to spot delivery issues, track spikes or drops in activations, and confirm that messages are reaching the right groups as expected.

![Outbound diagnostics report showing a line chart tracking the daily volume of recommendations generated and activated for different audience groups. The chart displays two lines labeled Generated and Activated, with the y-axis representing the number of recommendations and the x-axis showing dates. A legend identifies each line by color. The interface includes dropdown filters for date range and audience selection above the chart.]({% image_buster /assets/img/decisioning_studio/reporting_diagnostics_outbound.png %})

{% endtab %}

{% tab inbound %}

The inbound diagnostics report monitors the health of your data feeds into BrazeAI™. It tracks details like file counts, sizes, and row volumes for each asset, helping you confirm that data is flowing in as expected and troubleshoot issues before they affect your models or campaigns.

You can use the dropdown to select different chart metrics, like average file size or file count.

![Inbound diagnostics report showing a line chart tracking the daily file count and average file size for data assets delivered to BrazeAI™. The chart displays two lines labeled File count and Average file size MBs with the y-axis representing values and the x-axis showing dates. Above the chart are dropdown filters for date range and data asset selection.]( {% image_buster /assets/img/decisioning_studio/reporting_diagnostics_inbound.png %} )

Refer to the following table for more details about each metric in the inbound report:

| Field | Description |
|-------|-------------|
| Data asset | The name of the dataset or file delivered. |
| Date | The date when the data was received. |
| Last delivery time | The most recent time the data was delivered. |
| File count | The total number of files received. |
| Max file size (MBs) | The size of the largest file received, in megabytes. |
| Average file size (MBs) | The average size of all files received, in megabytes. |
| File row count | The total number of rows contained in the delivered files. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% endtab %}
{% endtabs %}

### Timeline

The timeline report provides a visual record of key events alongside your performance metrics. These events include model runs, configuration changes, guardrail updates, and more. Annotations appear directly on uplift charts and in a dedicated timeline tab, giving you instant context for shifts in results without needing to track down historical changes.

![Timeline report showing a chart with performance metrics over time. Key events such as model runs, configuration changes, and guardrail updates are marked as icons along the timeline. Below the chart, a table lists events with columns for date, type, label, details, and visibility in charts.]({% image_buster /assets/img/decisioning_studio/reporting_timeline.png %})

To compare performance between two groups, use the dropdowns to select your desired comparison criteria. Refer to the following table for more details:

| Field | Description |
|-------|-------------|
| Date | The date when the event occurred. |
| Type | The category of event, such as system update, model run, or configuration change. |
| Label | The name or identifier given to the event. |
| Details | Additional information that describes the event. |
| Visible in Charts | Indicates whether the event is displayed in related charts. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
