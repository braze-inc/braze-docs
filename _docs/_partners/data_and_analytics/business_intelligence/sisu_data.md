---
nav_title: Sisu Data
article_title: Sisu Data
description: "This reference article outlines the partnership between Braze and Sisu Data, a  leader in cloud decision intelligence, that allow you to understand across all campaigns or at a campaign level why metrics are changing and what drives the most optimal outcomes."
alias: /partners/sisu_data
page_type: partner
search_tag: Partner
---

# Sisu Data

> [Sisu Data][2] is the leader in cloud decision intelligence that uses machine learning to automatically decompose metric performance and deliver fast, comprehensive, and actionable insights.

The Sisu Data and Braze integration allows you to understand across all campaigns or at a campaign level why metrics (for example, open rate, click-through rate, conversion rate, etc.) are changing and what drives the most optimal outcomes. After these segments are identified, Braze users can materialize the outputs in their data warehouse or send them directly from Sisu to Braze to retarget and re-engage users.

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Sisu account | A [Sisu][3] account is required to take advantage of this partnership. |
| Cloud warehouse | This integration assumes your Braze data is stored in a cloud warehouse (for example, Snowflake, BigQuery). To streamline this integration process, we recommend utilizing Braze native functionality via [Currents][4]. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Step 1: Prepare a dataset

The dataset should indicate the KPI you want Sisu to analyze. For instance, if you want to better understand why conversion rates dropped week-over-week, the reach record should represent a weekly conversion. The columns in the dataset should be potential reasons why the conversion rate could drop.

### Step 2: Create a metric  

Once the dataset is prepped, you will need to create a metric that references an aggregated column. Since a dataset can power multiple metrics, the user can also curate a set of dimensions that should or shouldn't be part of all analyses by default. Note that users can always continue to curate at the analysis level.

![][6]

### Step 3: Create an analysis  

There are different analyses that users can create in Sisu depending on the use case. One of the most common analyses is a period-over-period analysis to understand which segments have changed the most. Users can decide whether to analyze daily, weekly, monthly, or custom time periods by selecting the relative time periods.

For example, the user can create a month-over-month conversion rate analysis for a particular ad group and engagement channel and understand the top positive and negative drivers.

{% tabs %}
{% tab Top positive drivers %}

![]({% image_buster /assets/img/sisudata/kda_result_positive.png %})

{% endtab %}
{% tab Top negative drivers %}

![]({% image_buster /assets/img/sisudata/kda_result_negative.png %})

{% endtab %}
{% endtabs %}

From here, you can hone in on cohorts they may want to engage in or modify campaigns. For instance, Sisu has automatically identified that push notifications sent on Tuesdays and emails sent in large volumes severely affect the conversion rate.

![][9]

### Step 4: Write back the results to the data warehouse

Users can extract the results from Sisu using [Sisu's API][10] and materialize the segments in a data warehouse. Snowflake customers can activate these segments in Braze via [Cloud Data Ingestion][5].

For other data warehouses, users can leverage an existing activation solution or contact Sisu for additional help.

## Support

For questions about this integration, contact Sisu at partners@sisudata.com.

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: https://sisudata.com/
[3]: https://sisudata.com/
[4]: {{site.baseurl}}/user_guide/data_and_analytics/braze_currents/setting_up_currents/
[5]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/cloud_ingestion/overview/
[6]: {% image_buster /assets/img/sisudata/metric_creation.png %}
[9]: {% image_buster /assets/img/sisudata/segment.png %}
[10]: https://docs.sisudata.com/docs/api/#tag/AnalysesService/operation/AnalysesService_AnalysisRunResults
