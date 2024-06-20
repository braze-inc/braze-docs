---
nav_title: Treasure Data
article_title: Treasure Data Cohort Import
description: "This reference article outlines the cohort import functionality of Treasure Data."
page_type: partner
search_tag: Partner

---
# Treasure Data cohort import

> This article describes how to import user cohorts from Treasure Data to Braze so you can send targeted campaigns based on data that may only exist in your warehouse.

{% alert important %}
This feature is currently in Beta. For more information, contact your Treasure Data and Braze representatives.
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

### Step 3: Define your cohort Audience

Cohorts can be synced to Braze through an **Activation** in the **Audience Studio** or through executing a **Query** in the **Data Workbench**

{% alert important %}
Only users who already exist within Braze will be added or removed from a Cohort. Cohort Import **will not** create new users in Braze.
{% endalert %}

{% tabs local %}
{% tab Data Workbench %}
### Step 3: Define your query

{% alert note %}
Query columns must be specified with the exact column names and data type. The query columns must include at least one of the columns: `user_ids`, `device_ids`, or braze alias column match with configuration on the UI. Only user profiles that exist within Braze will be added to a cohort. Cohort Import will not create new user profiles.
{% endalert %}

1. Navigate to **Data Workbench** > **Queries**.
2. Select **New Query**.
3. Run the query to validate the result set.

![Treasure Data Integrations Hub Catalog]({% image_buster /assets/img/treasure_data/cohort/cohort3.png %}) 

#### Use case: Syncing cohorts by identifier

{% tabs local %}
{% tab Syncing External IDs %}
Here's an example table in Treasure Data:

| external_id |	email	| device_ids |
| ----------- | ----------- | ----------- |
| `TDCohort1`	| `TDCohort1@gmail.com`	| `1a2b3c` |
| `TDCohort2`	| `TDCohort2@gmail.com`	| `4d5f6g` |
| `TDCohort3`	| `TDCohort3@gmail.com`	| `7h8j9k` |
| `TDCohort4`	| `TDCohort4@gmail.com`	| `1ab2cd` |

{% alert warning %}
The column name must be `user_ids` or the sync will fail.
{% endalert %}

To sync cohorts using the external ID, run the following query:

```sql
SELECT
  external_id as user_ids
FROM
  example_cohort_table
```

After running the query, these user aliases will be added to the cohort in Braze:

 - `TDCohort1`
 - `TDCohort2`
 - `TDCohort3`
 - `TDCohort4`
{% endtab %}

{% tab Syncing User Aliases %}
Here's an example table in Treasure Data:

| external_id |	email	| device_ids |
| ----------- | ----------- | ----------- |
| `TDCohort1`	| `TDCohort1@gmail.com`	| `1a2b3c` |
| `TDCohort2`	| `TDCohort2@gmail.com`	| `4d5f6g` |
| `TDCohort3`	| `TDCohort3@gmail.com`	| `7h8j9k` |
| `TDCohort4`	| `TDCohort4@gmail.com`	| `1ab2cd` |

To sync cohorts using the user alias, run the following query:

```sql
SELECT
  email
FROM
  example_cohort_table
```

After running the query, these user aliases will be added to the cohort in Braze:

 - `"alias_label":"email", "alias_name":"TDCohort1@gmail.com"`
 - `"alias_label":"email", "alias_name":"TDCohort2@gmail.com"`
 - `"alias_label":"email", "alias_name":"TDCohort3@gmail.com"`
 - `"alias_label":"email", "alias_name":"TDCohort4@gmail.com"`
{% endtab %}

{% tab Syncing Device IDs %}
Here's an example table in Treasure Data:

| external_id |	email	| device_ids |
| ----------- | ----------- | ----------- |
| `TDCohort1`	| `TDCohort1@gmail.com`	| `1a2b3c` |
| `TDCohort2`	| `TDCohort2@gmail.com`	| `4d5f6g` |
| `TDCohort3`	| `TDCohort3@gmail.com`	| `7h8j9k` |
| `TDCohort4`	| `TDCohort4@gmail.com`	| `1ab2cd` |

{% alert warning %}
The column name must be `device_ids` or the sync will fail.
{% endalert %}

To sync cohorts using the device ID, run the following query:

```sql
SELECT
  device_ids
FROM
  example_cohort_table
```

After running the query, these device IDs will be added to the cohort in Braze:

- `1a2b3c`
- `4d5f6g`
- `7h8j9k`
- `1ab2cd`
{% endtab %}
{% endtabs %}

### Step 4: Specify the result export target

Once the query has been built, select **Export Results**. You can select an existing authentication, such as the one created in the last steps, or create a new authentication to be used for output. 

![Treasure Data Integrations Hub Catalog]({% image_buster /assets/img/treasure_data/cohort/cohort5.png %}) 


| Export Result Mapping |	Description	| 
| ----------- | ----------- |
| Cohort ID	| This is the backend cohort identifier that will be sent to Braze. 	|
| Cohort Name (Optional)	| This is the name that will appear within the Cohort Filter in Braze's Segmentation tool. If this is not set, the **Cohort ID** will be used as the **Cohort Name**	|
| Operation	| Used to determine whether the query should add or remove profiles from the Cohort in Braze	| 
| Aliases (Optional) | When defined, the name of the corresponding column within your Query will be sent as the `alias_label`, and the values of each row in the column will be sent as the `alias_name`	| 
| Thread Count | Number of concurrent API calls |

Follow [Treasure Data's steps](https://docs.treasuredata.com/articles/#!int/braze-cohort-export-integration/a/ExportIntegrationTemplate-SpecifytheResultExportTarget) for configuring your export to meet your use case.

### Step 5: Execute the query

Save the query with a name and run, or just run the query. Upon successful completion of the query, the query result is automatically exported to Braze.

{% endtab %}
{% tab Audience Studio %}
### Step 3: Create an activation

Create a new Segment or choose an existing Segment to sync to Braze as a Cohort. Within the Segment, choose **Create activation**

#### Activation Details

![Treasure Data Integrations Activation Details]({% image_buster /assets/img/treasure_data/cohort/cohort7.png %}) 

| Activation Detail Setting |	Description	| 
| ----------- | ----------- |
| Activation Name	| The name of your Activation	|
| Activation Description| A brief description of the Activation	|
| Authentication	| Choose the Braze Cohort authentication created in Step 2	| 
| Cohort ID	| This is the backend cohort identifier that will be sent to Braze. 	|
| Cohort Name (Optional)	| This is the name that will appear within the Cohort Filter in Braze's Segmentation tool. If this is not set, the **Cohort ID** will be used as the **Cohort Name**	|
| Operation	| Used to determine whether the query should add or remove profiles from the Cohort in Braze	| 
| Aliases (Optional) | When defined, the name of the corresponding column within your Query will be sent as the `alias_label`, and the values of each row in the column will be sent as the `alias_name`	| 
| Thread Count | Number of concurrent API calls |


#### Activation Output Mapping

![Treasure Data Integrations Activation Output Mapping]({% image_buster /assets/img/treasure_data/cohort/cohort6.png %}) 

| Activation Output Mapping |	Description	| 
| ----------- | ----------- |
| Attribute Columns	| Determine the Columns from your Segment Database that will be mapped as Identifiers when syncing profiles to a Braze Cohort.	|
| String Builder| The String Builder is not necessary for this integration.	|

{% alert important %}
 - When using `device_id` as the identifier the **Output Column Name** must be named `device_ids`
 - When using aliases as the identifier, the **Output Column Name** must be the name of the corresponding column within your Query will be sent as the `alias_label`, and the values of each row in the column will be sent as the `alias_name`
 - When using `external_id` as the identifier the **Output Column Name** must be named `user_ids`
{% endalert %}

All non-relevant or misnamed column names will be ignored. You may choose to use more than one identifier in your syncs.

#### Activation Schedule

Define your desired sync schedule and save your Activation.

![Treasure Data Integrations Activation Schedule]({% image_buster /assets/img/treasure_data/cohort/cohort8.png %}) 

{% endtab %}
{% endtabs %}

### Step 6: Create a Braze segment from the Treasure Data Export

In Braze, navigate to **Segments**, create a new segment, and select **Treasure Data Cohorts** as your filter. From here, you can choose which Treasure Data cohort you wish to include. After your Treasure Data cohort segment is created, you can select it as an audience filter when creating a campaign or Canvas.

![Treasure Data Integrations Hub Catalog]({% image_buster /assets/img/treasure_data/cohort/cohort4.png %}) 
