---
nav_title: Treasure Data
article_title: Treasure Data Cohort Import
description: "This reference article outlines the cohort import functionality of Treasure Data."
page_type: partner
search_tag: Partner

---
# Treasure Data cohort import

> This article describes how to import user cohorts from Treasure Data to Braze so you can send targeted campaigns based on data that may only exist in your warehouse. 
{% alert note %}
This feature is a BETA release. For more information, contact your Treasure Data and Braze Customer Success Representatives. 
{% endalert %}

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Treasure Data account | A [Treasure Data](https://www.treasuredata.com/) account is required to take advantage of this partnership. |
| Braze Data Import key | This can be captured in the Braze dashboard from **Partner Integrations** > **Technology Partners** and then select **Heap**. |
| Braze REST endpoint | [Your REST endpoint URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Your endpoint will depend on the Braze URL for your instance. |
| Static IP Address of Treasure Data | The static IP address of Treasure Data is the access point and source of the linkage for this Integration. To determine the static IP address, contact your Treasure Data Customer Success representative or Treasure Data Technical support. |
{: .reset-td-br-1 .reset-td-br-2}

## Data import integration

### Step 1: Get your Braze data import key

In Braze, navigate to **Partner Integrations** > **Technology Partners** and select **Treasure Data**. Here, you will find your REST endpoint and generate your Braze data import key. After the key is generated, you can create a new key or invalidate an existing one.

### Step 2: Create a data connection

Before you create your data connection within Treasure Data, you'll need to authenticate. First, select **Integrations Hub**, then **Catalog**.

![Treasure Data Integrations Hub Catalog]({% image_buster /assets/img/treasure_data/cohort/cohort1.png %}) 

Search for the Braze Integration in the **Catalog**, then hover over the icon and select **Create Authentication**. Enter your credentials, name your authentication, then select **Done**.

![Treasure Data Integrations Hub Catalog]({% image_buster /assets/img/treasure_data/cohort/cohort2.png %}) 

### Step 3: Define your Query

{% alert note %}
Query columns must be specified with the exact column names and data type. The query columns must present at least one of the columns: `user_ids`, `device_ids`, or braze alias column match with configuration on the UI.
{% endalert %}

1. Navigate to **Data Workbench** > **Queries**.
2. Select **New Query**.
3. Run the query to validate the result set.

![Treasure Data Integrations Hub Catalog]({% image_buster /assets/img/treasure_data/cohort/cohort3.png %}) 

### Step 4: Specify the Result Export Target

Once the query has been built, select **Export Results**. You can select an existing authentication, such as the one created in the last steps, or create a new authentication to be used for output. 

Follow [Treasure Data's steps](https://docs.treasuredata.com/articles/#!int/braze-cohort-export-integration/a/ExportIntegrationTemplate-SpecifytheResultExportTarget) for configuring your export to meet your use case.

### Step 5: Execute the Query

Save the query with a name and run, or just run the query. Upon successful completion of the query, the query result is automatically exported to Braze.

### Step 6: Create a Braze segment from the Treasure Data Export

In Braze, navigate to **Segments**, create a new segment, and select **Treasure Data Cohorts** as your filter. From here, you can choose which Treasure Data cohort you wish to include. After your Treasure Data cohort segment is created, you can select it as an audience filter when creating a campaign or Canvas.

![Treasure Data Integrations Hub Catalog]({% image_buster /assets/img/treasure_data/cohort/cohort4.png %}) 
