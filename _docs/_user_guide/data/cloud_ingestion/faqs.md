---
nav_title: FAQs
article_title: Cloud Data Ingestion FAQs
page_order: 100
page_type: FAQ
description: "This page answers frequently asked questions about Cloud Data Ingestion."
toc_headers: h2
---

# Frequently asked questions

> This page contains answers to some frequently asked questions for Cloud Data Ingestion.

## Why was I emailed: "Error in CDI Sync"?

This type of email usually means there's an issue with your CDI setup. Here are some common issues and how to fix them:

### CDI can't access the data warehouse or table using your credentials

This could mean the credentials in CDI are incorrect or are misconfigured on the data warehouse. For more information, refer to [Data Warehouse Integrations]({{site.baseurl}}/user_guide/data/cloud_ingestion/integrations/).

### The table cannot be found

Try updating your integration with the correct database configuration or create matching resources on the data warehouse, such as `database/table`.

### The catalog cannot be found

The catalog set up in the integration doesn't exist in the Braze catalog. A catalog can be removed after the integration was set up. To resolve the issue, either update the integration to use a different catalog or create a new catalog that matches the catalog name in the integration.

## Why was I emailed: "Row errors in your CDI sync"?

This type of email means that some of your data could not be processed during the sync. To find out the specific error, you can review the logs in Braze by going to **CDI** > **Sync Log**.

## How do I fix errors for Test Connection and support emails?

{% tabs %}
{% tab Snowflake %}
### Test Connection runs slow

Test Connection is running on your data warehouse, so increasing warehouse capacity may improve its speed. Using a serverless SQL instance will minimize warmup time and improve query throughput, but may result in slightly higher integration costs.

### Error connecting to Snowflake instance: Incoming request with IP is not allowed to access Snowflake

Try adding the official Braze IPs to your IP allowlist. For more information, refer to [Data Warehouse Integrations]({{site.baseurl}}/user_guide/data/cloud_ingestion/integrations/), or allow the relevant IPs:

{% multi_lang_include data_centers.md datacenters='ips' %}

### Error executing SQL due to customer config: 002003 (42S02): SQL compilation error: does not exist or not authorized

If the table doesn't exist, create the table. If the table does exist, verify that the user and role have permissions to read from the table.

### Could not use schema

If you receive this error, grant access to that schema for the specified user or role.

### Could not use role

If you receive this error, allow that user to use the specified role.

### User access disabled

If you receive this error, allow that user access to your Snowflake account.

### Error connecting to Snowflake instance with current and old key

If you receive this error, make sure the user is using the current public key as displayed in your Braze dashboard.
{% endtab %}

{% tab Redshift %}
### Test Connection runs slow

Test Connection is running on your data warehouse, so increasing warehouse capacity may improve its speed. Using a serverless SQL instance will minimize warmup time and improve query throughput, but may result in slightly higher integration costs.

### Permission denied for relation {table_name}

If you receive this error:

  - Grant the `usage` permission on the schema for that user.
  - Grant the `select` permission on the table for that user.

### Create Connection Error

If you receive this error, verify the Redshift endpoint and port are correct.

### Create SSH Tunnel Error

If you receive this error:

  - Verify the public key on your braze dashboard is on ec2 host used for SSH tunneling.
  - Verify your username is correct.
  - Verify the SSH Tunnel is correct.
{% endtab %}

{% tab BigQuery %}
### Test Connection runs slow

Test Connection is running on your data warehouse, so increasing warehouse capacity may improve its speed. Using a serverless SQL instance will minimize warmup time and improve query throughput, but may result in slightly higher integration costs.

### User does not have permission to query table

If you receive this error, add user permissions to query the table.

### Your usage exceeded the custom quota

If you receive this error, your quota needs to be updated so you can continue syncing at your current rate.

### Table was not found in location {region} Location

If you receive this error, verify your table is in the correct project and dataset.

### Invalid JWT Signature

If you receive this error, check that the BigQuery API service is enabled for your account.
{% endtab %}

{% tab Databricks %}
### Test Connection runs slow

Test Connection is running on your data warehouse, so increasing warehouse capacity may improve its speed. For Databricks, there may be two to five minutes of warm-up time when Braze connects to Classic and Pro SQL instances, which will lead to delays during connection setup and testing, as well as at the beginning of scheduled syncs. Using a serverless SQL instance will minimize warmup time and improve query throughput, but may result in slightly higher integration costs.

### Command failed because warehouse was stopped

If you receive this error, ensure Databricks warehouse is running.

### Service: Amazon S3; Status Code: 403; Error Code: 403 Forbidden

If you receive this error, see [Databricks: Forbidden error while accessing S3 data](https://kb.databricks.com/security/forbidden-access-to-s3-data).
{% endtab %}
{% endtabs %}

## How do I update my email alert preferences for CDI integrations?

Each integration has its own notification preference. Go to the CDI page and select the integration name you want to update. In the **Notification preferences** section you can update how you receive alerts regarding the selected integration.

## What happens if a future UPDATED_AT gets synced with an integration?

CDI uses `UPDATED_AT` to decide what data is new. After a future `UPDATED_AT` is synced, any data prior to that future date and time will not be processed. To fix this:

1. Correct `UPDATED_AT`.
2. Remove any old data that's already synced with Braze
3. Create a new integration to process that table again.

## Why doesn't "Rows Synced" match the number in my warehouse?

CDI uses `UPDATED_AT` to decide which records to pick up during a sync. Check out [this illustration]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/overview/#what-gets-synced) to see how it works. At the beginning of a sync run, CDI queries your warehouse to get all records with `UPDATED_AT` equal to or later than the previously processed `UPDATED_AT` timestamp. Any record picked up at the time when the query executes will be synced into Braze. Here are common cases when a record might not be synced:

- You're adding records to the table with an `UPDATED_AT` value that has already been processed.
- You're updating record values after they have been processed by a sync, but leaving `UPDATED_AT` unchanged. 
- You're adding or updating records while a sync is in progress. Depending on when the CDI query executes, there could be race conditions that lead to records not being picked up.

{% alert tip %}
To avoid these behaviors in the future, we recommend using monotonically increasing `UPDATED_AT` values and not updating the table during your scheduled sync run. 
{% endalert %}

## During a sync, is the order preserved if multiple records share the same ID?

The processing order is not 100% predictable. For example, if there are multiple rows with the same `EXTERNAL_ID` in the table during a sync, we cannot guarantee which value will end up in the final profile. If you're updating the same `EXTERNAL_ID` with different attributes in the payload column, all changes are reflected when the sync is completed.

## What are the security measures for CDI?

### Our measures

Braze has the following measures in place for CDI:

- All credentials are encrypted within our database, and only certain employees have authenticated access to them.
- We use encrypted connections to get data to customer warehouses.
- We make requests to the Braze API endpoints using the same API keys and TLS connections that we recommend our customers use.
- We regularly update our libraries and get any security patches.

### Your measures

We recommend you and your team set up the following security measures on your side: 

- Restrict credential access to the minimum required for CDI to operate. This is because we need to be able to run select (and count) on the specific tables and views.
- Restrict the IPs that can access the tables to officially published [Braze IPs]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/.#step-1-set-up-tables-or-views).
