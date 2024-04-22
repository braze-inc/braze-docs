---
nav_title: CDI Segments
article_title: CDI Segments
page_order: 0
page_type: reference
tool: 
- Segments
description: "This how-to article will walk you through how to set up Location targeting, allowing you to segment users by location."

---

# CDI Segments

> With Braze [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/overview/) (CDI), you can set up a direct connection from your data warehouse or file storage system to Braze to sync relevant user or catalog data on a recurring basis.

{% alert note %}
CDI segments is currently in early access and is available only for customers with Snowflake CDI integrations.
{% endalert %}

To use your data warehouse data for segmentation within your Braze workspace, create a CDI segment within your [segment extensions]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/). CDI segments allow you to write SQL that directly queries your own data warehouse by using data made available via your CDI connections, and create a group of users that can be targeted within Braze.

This feature queries your data warehouse directly, so you will incur all costs associated with running these queries in your data warehouse. It won't consume [SQL segment credits]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/#monitoring-your-sql-segments-usage) or data points.

## Setting up CDI ingestion

Set up a new Connection Sync with Snowflake by following the steps in [Data warehouse integrations]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/).

## Creating a CDI segment

After your CDI integration is set up, create your CDI segment by doing the following. 

1. Create a new [Segment Extension]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/) and select the **Full refresh** option. <br>![]({% image_buster /assets/img/segment/segment_extension_modal.png %}){: style="max-width:50%;"}<br><br>

2. Select **CDI Data Tables** as your data source. <br>![]({% image_buster /assets/img/segment/cdi_data_tables.png %}){: style="max-width:50%;"}<br><br>

3. Select **Reference** to view the data tables available for use. As part of your CDI setup, you can select from different connections to use in CDI segments. Each connection has a specific set of data tables. Your team can configure your connections and data tables during CDI setup. <br><br>

4. Select a connection. <br>![]({% image_buster /assets/img/segment/connection_schema.png %}){: style="max-width:70%;"}<br><br>

5. Write the SQL for your segment using [our guidelines]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/#writing-sql). All CDI segments must use `external_user_id` as the selected column, and your `external_user_id` should match the one set in Braze for users. If your query results include users that don't exist in Braze, those users will be ignored. Braze will not create new users based on the output of your CDI segment. 

{% alert tip %}
Check out [SQL Segment Extensions]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/) for guidelines on previewing your segment, managing your segment, and running automated membership refreshes.
{% endalert %}

{: start="6"}
6. [Use this segment extension]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/#step-5-use-your-extension-in-a-segment) within a Braze segment to send a campaign or Canvas to this audience.

## Considerations

- A segment extension can reference data from only one connection, not multiple.    
- A segment extension can use one of the following as a data source: CDI data or Braze Snowflake (Currents) data. You cannot mix data sources within a segment extension, but you can create multiple segment extensions to reference together within a segment.

## Troubleshooting

- Your query might timeout when it reaches your maximum runtime, which is set up for each connection sync on the **Cloud Data Ingestion** page. The maximum runtime allowed is 60 minutes.
- Make sure your SQL is written using [Snowflake syntax](https://docs.snowflake.com/en/sql-reference/).