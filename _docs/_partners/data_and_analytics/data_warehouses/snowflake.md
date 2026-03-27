---
nav_title: Snowflake
article_title: Snowflake
alias: /partners/snowflake/
description: "This article outlines the partnership between Braze and Snowflake, covering both Data Sharing (Braze to Snowflake) and Cloud Data Ingestion (Snowflake to Braze)."
page_type: partner
search_tag: Partner

---

# Snowflake

> [Snowflake](https://docs.snowflake.net/manuals/user-guide/intro-key-concepts.html) is a purpose-built SQL cloud data warehouse provided as Software-as-a-Service (SaaS). Snowflake provides a data warehouse that is faster, easier to use, and far more flexible than traditional data warehouse offerings. With Snowflake's unique and patented architecture, it's easy to amass all of your data, enable rapid analytics, and derive data-driven insights for all of your users.

Braze offers two integrations with Snowflake. Together, they provide a complete, bidirectional data pipeline between your Braze and Snowflake environments.

## Choosing an integration

### Data Sharing (Braze to Snowflake)

Snowflake [Secure Data Sharing]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/data_sharing/) gives you secure, real-time access to Braze engagement and campaign data directly in your Snowflake instance. No data is copied or transferred between accounts—all sharing is accomplished through Snowflake's unique services layer and metadata store.

**Use Data Sharing when you want to:**
- Query Braze event and campaign data using Snowflake SQL
- Create complex reports and perform attribution modeling
- Join Braze data with other data in your Snowflake warehouse
- Benchmark your engagement data across channels, industries, and device platforms

For setup instructions, see [Snowflake Data Sharing]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/data_sharing/).

### Cloud Data Ingestion (Snowflake to Braze)

[Cloud Data Ingestion (CDI)]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/) lets you sync data from your Snowflake instance directly into Braze. This allows you to keep user attributes, events, and purchases in Braze up to date with your source-of-truth data warehouse.

**Use Cloud Data Ingestion when you want to:**
- Sync user attributes from Snowflake to Braze user profiles
- Send event or purchase data from Snowflake into Braze
- Keep Braze in sync with data transformations happening in your warehouse
- Avoid building and maintaining custom ETL pipelines from Snowflake to Braze

To learn more about Snowflake's data sharing, see [Introduction to Secure Data Sharing](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#how-does-secure-data-sharing-work).

## Prerequisites

Before you can use this feature, you'll need to complete the following:

| Requirement | Description |
| ----------- | ----------- |
| Braze access | To access this feature in Braze, you'll need to contact your Braze account or customer success manager. |
| Snowflake account | A Snowflake account with `admin` permissions. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Setting up Secure Data Sharing

For Snowflake, data sharing happens between a [data provider](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#providers) and [data consumer](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#consumers). Within this context, your Braze account is the data provider because it creates and sends the datashare&#8212;whereas your Snowflake account is the data consumer because it uses the datashare to create a database. For more details, see [Snowflake: Consuming Shared Data](https://docs.snowflake.com/en/user-guide/data-share-consumers).

### Step 1: Send the datashare from Braze

1. In Braze, go to **Partner Integrations** > **Data Sharing**.
2. Enter your Snowflake account details and locator. To get your account locator, run `SELECT CURRENT_ACCOUNT()` in the destination account.
3. If you're using a CRR share, specify the cloud provider and region.
4. When you're finished, select **Create Datashare**. This will send the datashare to your Snowflake account.

### Step 2: Create the database in Snowflake

1. After a few minutes, you should receive the inbound datashare in your Snowflake account.
2. Using the inbound datashare, create a database to view and query the tables. For example:
    ```sql
    CREATE DATABASE <name> FROM SHARE <provider_account>.<share_name>
    ```
3. Grant privileges to query the new database.

{% alert warning %}
If you delete and recreate a share in the Braze dashboard, you must drop the previously-created database and recreate it using `CREATE DATABASE <name> FROM SHARE <provider_account>.<share_name>` to query the inbound share.
If you have multiple workspaces sharing data to the same Snowflake account, see the [Snowflake Data Sharing FAQs]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/faqs/) for guidance on managing multi-workspace configurations.
{% endalert %}

## Usage and visualization

After the data share is provisioned, you will need to create a database from the incoming data share, making all the tables shared appear in your Snowflake instance and be queryable just like any other data you're storing in your instance. However, keep in mind that the shared data is read-only and can only be queried but not modified or deleted in any way.

Similar to Currents, you can use your Snowflake Secure Data Sharing to:

- Create complex reports
- Perform attribution modeling
- Secure sharing within your own company
- Map raw event or user data to a CRM (like Salesforce)
- And more

For a full list of available tables and columns, refer to the [SQL table reference]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables/). Snowflake Data Sharing includes all tables in that reference, plus additional Snowflake-exclusive tables for snapshots, campaign and Canvas changelogs, agent console events, and message retry events.

You can also [download the raw table schemas]({% image_buster /assets/download_file/data-sharing-raw-table-schemas.txt %}) as a text file.

### User ID schema

Note the following differences between Braze and Snowflake naming conventions for user IDs.

| Braze schema | Snowflake schema | Description |
| ----------- | ----------- | ----------- |
| `braze_id` | `"USER_ID"` | The unique identifier that is automatically assigned by Braze. |
| `external_id` | `"EXTERNAL_USER_ID"` | The unique identifier of a user's profile that is set by the customer. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Important information and limitations

### Breaking versus non-breaking changes

#### Non-breaking changes

Non-breaking changes can happen at any time and generally provide additional functionality. Examples of non-breaking changes:
- Adding a new table or view
- Adding a column to an existing table or view

{% alert important %}
Because new columns are considered non-breaking, Braze strongly recommends explicitly listing the columns of interest in each query instead of using `SELECT *` queries. Alternately, you might want to create views that explicitly name columns and then query those views instead of the tables directly.
{% endalert %}

#### Breaking changes

When possible, breaking changes will be preceded by an announcement and a migration period. Examples of breaking changes include:
- Removing a table or view
- Removing a column from an existing table or view
- Changing the type or nullability of an existing column

### Snowflake regions

Braze currently hosts all user-level data in the Snowflake AWS US East-1, EU-Central (Frankfurt), AP-Southeast-2 (Sydney) and AP-Southeast-3 (Jakarta) regions. For users outside of those regions, Braze can provide data sharing to joint customers who are hosting their Snowflake infrastructure across any AWS, Azure, or GCP region.

### Data retention

#### Retention policy

Any data older than two years will be archived and moved to long term storage. As part of the archival process, all events are anonymized and any personal identifiable information (PII) sensitive fields are stripped out (this includes optionally PII fields like `properties`). Archived data still contains the `user_id` field, which allows for per-user analytics across all events data.

You will be able to query against the most recent two years of data for each event in the corresponding `USERS_*_SHARED` view. Additionally, each event will have a `USERS_*_SHARED_ALL` view which can be queried against to return both anonymized and non-anonymized data.

#### Historical data

The archive of historical event data in Snowflake goes back to April 2019. In the first few months of Braze storing data in Snowflake, product changes were made that may have resulted in some of that data looking slightly different or having some null values (as we weren't passing data into every available field at this time). It's best to assume that any results that include data before August 2019 may look slightly different from expectations.

### General Data Protection Regulation (GDPR) compliance

{% multi_lang_include partners/snowflake_pii_gdpr.md %}

### Speed, performance, cost of queries

The speed, performance, and cost of any query run on top of the data are determined by the warehouse size you use to query the data. In some cases, depending on how much data you're accessing for analytics, you may find that you need to use a larger warehouse size for the query to be successful. Snowflake has excellent resources available about how to best determine which size to use including [Overview of warehouses](https://docs.snowflake.net/manuals/user-guide/warehouses-overview.html) and [Warehouse considerations](https://docs.snowflake.net/manuals/user-guide/warehouses-considerations.html)

> For a set of example queries to reference when setting up snowflake, check out our [sample queries]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/sample_queries/) and [ETL event pipeline setup]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/etl_pipline_setup/) examples.

For setup instructions, see [Cloud Data Ingestion: Data warehouse integrations]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/).
