---
nav_title: Sisu Data
article_title: Sisu Data
page_order: 1

description: "Sisu Data is the leader in Cloud Decision Intelligence that uses ML to automatically segment metric performance and deliver fast, comprehensive, and actionable insights."
alias: /partners/sisudata

page_type: partner
search_tag: Partner
hidden: true

---

# Sisu Data

> [Sisu Data][2] is the leader in Cloud Decision Intelligence that uses ML to automatically decompose metric performance and deliver fast, comprehensive, and actionable insights.

Sisu Data and Braze empower organizations to create relevant and meaningful interactions with comprehensive data segmentation and diagnostic analytics. By combining Braze’s Customer Engagement Platform and Sisu’s Decision Intelligence engine, business leaders can focus on taking action — resulting in improved revenue, reduced risk, and more efficient business operations.

Braze users can leverage the Sisu platform to automatically monitor and diagnose why metrics (e.g. open rate, click-through rate, conversion rate, etc) change. Once these segments are identified, Braze users can materialize the outputs in their data warehouse or send them directly from Sisu to Braze to retarget and reengage users.

## Prerequisites

Sisu will need read-only access to the data warehouse that stores the Braze data. We recommend sending Braze data to the warehouse via [Currents][4].

| Requirement | Description |
| ----------- | ----------- |
| Sisu account | A [Sisu][3] account is required to take advantage of this partnership. |
| Braze REST API key | A Braze REST API key with `users.track` permissions. <br><br> This can be created within the **Braze Dashboard > Developer Console > REST API Key > Create New API Key**. |
| Braze REST endpoint | [Your REST endpoint URL][1]. Your endpoint will depend on the Braze URL for your instance. |
{: .reset-td-br-1 .reset-td-br-2}

## Use cases

Understand whether across all campaigns or at a campaign level, why metrics are changing and what drives the most optimal outcomes. This allows users to decompose what type of engagement your customers are best responding to and then automate actions via Braze powered by Sisu’s generated segments.

## Integration

As aforementioned, in order to leverage Sisu to diagnose and decompose why metrics revolving around retention, conversion, etc are changing, it’s assumed the Braze data is stored in a cloud warehouse (e.g. Snowflake, BigQuery…etc). To streamline this ingestion process, we recommend utilizing Braze’s native functionality via [Currents][4].

*Note: The best use case for Sisu is where the data is rich in both volume & breadth (e.g. columns).*


### Step 1: Prepare a dataset

The dataset should be indicative of the KPI the user wants Sisu to analyze. For instance, if the user wants to better understand why Conversion Rate dropped week-over-week then reach record should represent a weekly conversion. The columns in the dataset should be potential levers or reasons why conversion rate could drop. 

### Step 2: Create a Metric  

Once the dataset is prepped, the user will need to create a metric which simply is a reference to a column that is aggregated. Since a dataset can power multiple metrics, the user can also curate a set of dimensions that should or shouldn't be part of all analysis by default.

![metric_creation][6]

*Note: Users can always continue to curate at the analysis level* 

### Step 3: Create an analysis  

There are different analysis that users can create in Sisu depending on the use case. One of the most common analysis is a Period-over-Period analysis to understand which segments have changed the most. Users can decide whether to analyze daily, weekly, monthly or a custom time period by selected the relative time periods. 

For example, the user can create a month over month conversion rate analysis for a particular ad-group and engagement channel and understand the top positive & negative drivers.

###### Top Positive Drivers:
![kda_positive][7]

###### Top Negative Drivers:
![kda_positive][8]

From here, the user can hone in on cohorts that they may want to rengnage or modify campaigns. For instance, Sisu has automatically identified on Tuesdays, push notifications and large volume of emails is detrmential to conversion rate.

![segment_output][9]

### Step 4: Write back the results to data warehouse

Users can extract the results from Sisu via [Sisu's API][10] and materialize the segments in a data warehouse. Snowflake customers can activate these segments in Braze via [Cloud Data Ingestion][5]. For other data warehouses, users can leveage existing activation solutions or reach out to Sisu (*partners@sisudata.com*) for additional help. 

## Support

For any questions about this integration, feel free to reach out Sisu (*partners@sisudata.com*).


[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: https://sisudata.com/
[3]: https://sisudata.com/
[4]: https://www.braze.com/docs/user_guide/data_and_analytics/braze_currents/setting_up_currents/
[5]: https://www.braze.com/docs/user_guide/data_and_analytics/user_data_collection/cloud_ingestion/overview/
[6]: {% image_buster /assets/img/sisudata/metric_creation.png %}
[7]: {% image_buster /assets/img/sisudata/kda_result_positive.png %}
[8]: {% image_buster /assets/img/sisudata/kda_result_negative.png %}
[9]: {% image_buster /assets/img/sisudata/segment.png %}
[10]: https://docs.sisudata.com/docs/api/#tag/AnalysesService/operation/AnalysesService_AnalysisRunResults
