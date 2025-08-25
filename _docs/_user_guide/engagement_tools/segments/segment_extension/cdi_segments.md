---
nav_title: CDI Segment Extensions
article_title: CDI Segment Extensions
page_order: 0
page_type: reference
tool: 
- Segments
description: "This how-to article will walk you through how to set up Location targeting, allowing you to segment users by location."

---

# CDI Segment Extensions

> With Braze [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/cloud_ingestion/overview/) (CDI), you can set up a direct connection from your data warehouse or file storage system to Braze to sync relevant user or catalog data on a recurring basis.

{% alert warning %}
CDI Segment Extensions query your data warehouse directly, so you will incur all costs associated with running these queries in your data warehouse. CDI Segment Extensions won't consume [SQL segment credits]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/#monitoring-your-sql-segments-usage), don't count towards your Segment Extension limit, and do not log data points.
{% endalert %}

## Prerequisites

To use your data warehouse data for segmentation within your Braze workspace, you'll need to create a [connected source]({{site.baseurl}}/user_guide/data/cloud_ingestion/connected_sources/), then create a CDI segment within your [Segment Extensions]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/). CDI Segment Extensions allow you to write SQL that directly queries your own data warehouse by using data made available through your CDI connections, and create a group of users that can be targeted within Braze.

## Creating a CDI segment

### Step 1: Set up your source

Before creating your first CDI Segment Extension, set up a new connected source with your data warehouse by following the steps in [Connected sources]({{site.baseurl}}/user_guide/data/cloud_ingestion/connected_sources/).

### Step 2: Create a segment

First, create a new [Segment Extension]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/), then select **Full refresh**.

![]({% image_buster /assets/img/segment/segment_extension_modal.png %}){: style="max-width:60%;"}

For your data source, choose **CDI Data Tables**.

![]({% image_buster /assets/img/segment/cdi_data_tables.png %}){: style="max-width:60%;"}

As part of your CDI setup, you can select from different connections to use in CDI Segment Extensions. Each connection has a specific set of data tables. Your development team can configure your connections and data tables during CDI setup.

To view the available data tables, including their schema and any available descriptions, select **Reference**. When you're ready, select a connection.

![]({% image_buster /assets/img/segment/connection_schema_with_descriptions.png %}){: style="max-width:100%;"}

Next, write the SQL for your segment using [the Braze SQL syntax]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/#writing-sql).

Keep in mind, all CDI Segment Extensions must use `external_user_id` as the selected column, and your `external_user_id` should match the one set in Braze for users. If your query results include users that don't exist in Braze, those users will be ignored. Braze will not create new users based on the output of your CDI Segment Extension.

{% alert tip %}
To learn how you can preview your Segment Extensions, manage your Segment Extensions, and run automated membership refreshes, see [SQL Segment Extensions]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/).
{% endalert %}

Finally, you can [use this Segment Extension]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/#step-5-use-your-extension-in-a-segment) within a Braze segment to send a campaign or Canvas to this audience.

## Considerations

- A Segment Extension can reference data from only one connection, not multiple.    
- A Segment Extension can use one of the following as a data source: CDI data or Braze Snowflake (Currents) data. You cannot mix data sources within a Segment Extension, but you can create multiple Segment Extensions to reference together within a segment.

## Troubleshooting

- Your query might timeout when it reaches your maximum runtime, which is set up for each connection sync on the **Cloud Data Ingestion** page. The maximum runtime allowed is 60 minutes.
- Make sure your SQL is written using appropriate syntax for your data warehouse. 
