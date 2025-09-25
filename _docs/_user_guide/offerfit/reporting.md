---
nav_title: Viewing reports
article_title: Viewing OfferFit reports in Braze
page_order: 3
description: "DESCRIPTION."
---

# Viewing OfferFit reports in Braze

> Learn how to view OfferFit reports in Braze, so you can... (high-level one-liner highlighting the value)

## Prerequisites

Before you can view OfferFit reports in the Braze, you'll need to:

- Have an active contract for Braze and OfferFit. 
- Contact your CSM to enable OfferFit for you on your behalf.

## Viewing reports {#view}

To view metrics for an OfferFit use cases in Braze, go to **AI Decisioning** > **OfferFit by Braze**, then select a use case.

![ALT_TEXT]()

Here, you can view reports like performance, insights, diagnostics, and timelines. For more details, see [Available reports](#reports).

![ALT_TEXT]()

## Changing report dates

After [opening a report](#view), you can change the date range by selecting a new start and end date from the calendar dropdown.

![ALT_TEXT]()

You can also set a default start date or choose dates to always exclude. Excluded dates will be filtered out of all reports for that use case.

To set or exclude dates, select <i class="fa-solid fa-gear"></i> **Settings**, then change your default date or exclude dates as needed.

![ALT_TEXT]()

## Available reports {#reports}

### Performance

The performance report offers high-level use case metrics that compare treatment groups (from Braze) to one or more control groups, (like revenue). It supports two different views: **Trending** and **Driver Tree**.

By default, the report uses the **Trending** view, which compares how OfferFit performs over time compared to your control groups, and tracks the uplift evolution.

![ALT_TEXT]()

Alternatively, you can select **Driver Tree** to view how key value drivers are linked to target metrics, helping you better understand the relationship between them.

![ALT_TEXT]()

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

![ALT_TEXT]()

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
The **SHAPs** report uses the SHapley Additive exPlanations (SHAP) model to help you quantify how each feature or variable contributes to your recommendation model. Each point on the chart represents one SHAP and the distribution of the points represent a general sense of a feature's directional impact.

![ALT_TEXT]()
{% endtab %}
{% endtabs %}

### Diagnostics

The diagnostics report contains two different report types: **Outbound** and **Inbound**.

{% tabs local %}
{% tab outbound %}
The outbound diagnostics report... (high-level overview). You can... 

![ALT_TEXT]()
{% endtab %}

{% tab inbound %}
The inbound diagnostics report... (high-level overview). You can use the dropdown to select different chart metrics, like average file size or file count.

![ALT_TEXT]()

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

The timeline report... (high-level overview).

![ALT_TEXT]()

To compare performance between two groups, use the dropdowns to select your desired comparison criteria. Refer to the following table for more details:

| Field | Description |
|-------|-------------|
| Date | The date when the event occurred. |
| Type | The category of event, such as system update, model run, or configuration change. |
| Label | The name or identifier given to the event. |
| Details | Additional information that describes the event. |
| Visible in Charts | Indicates whether the event is displayed in related charts. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
