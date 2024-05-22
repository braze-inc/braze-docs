---
nav_title: FAQ
article_title: Cloud Data Ingestion FAQ
page_order: 100
page_type: FAQ
description: "This article covers some frequently asked questions for Cloud Data Ingestion"

---

# Frequently Asked Questions

### What should I do if I receive an email from Braze Support about errors in my CDI Sync?
Here are the common types of emails you might receive regarding errors in CDI sync:
- **Error in CDI Sync [NAME]**  
This type of email usually includes an error message that CDI encountered during the sync process. Often, it is due to a setup error. Some common issues include:
  - CDI cannot access the data warehouse or table with the credentials set up in the integration. This could mean the credentials in CDI are incorrect or are misconfigured on the data warehouse. Check out [Data Warehouse Integrations]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/) for more details.
  - SQL error due to the table not being found. Update the integration with the correct database config or create matching resources (e.g., database/table) on the data warehouse.
  - Catalog not found. The catalog set up in the integration does not exist in the Braze catalog. A catalog can be removed after the integration was set up. To resolve the issue, either update the integration to use a different catalog or create a new catalog that matches the catalog name in the integration.

- **Row Errors in your CDI Sync**  
This indicates that some data cannot be processed in the sync. To find out what is causing the errors, navigate to the CDI page in Braze. Open the **Sync Log** tab to check the error details for the sync job.

### How can I update my email alert preferences for CDI integrations?
Each integration has its own notification preference. Go to the CDI page and select the integration name you want to update. In the **Notification preferences** section you can update how you receive alerts regarding the selected integration.

### What to do if a future `UPDATED_AT` was synced in an integration?
CDI uses `UPDATED_AT` to decide what data is new. After a future `UPDATED_AT` is synced, any data prior to that future date and time will not be processed.

Users will need to clean up the data by correcting the `UPDATED_AT`, removing old data that were already synced to Braze, then create a new integration to process the table again.

### `Rows Synced` reported on the CDI dashboard is different from the number of records in my warehouse, or the value synced does not match what I have in my warehouse.
CDI uses `UPDATED_AT` field to decide which records to be picked up during a sync, [here]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/overview/#what-gets-synced) is an illustration of how it works. At the beginning of a sync run, CDI queries your warehouse to get all records with `UPDATED_AT` later than the previously processed value. Any record picked up at the time when the query executes will be synced into Braze. Here are some common cases when a record might not be picked up by a sync:
- Records are added to the table with an `UPDATED_AT` value that’s already been processed.
- Updating record values after it’s been processed by a sync, but leaving UPDATED_AT unchanged. 
- Records are being added or updated while a sync is in progress. Depending on when the CDI query executes, there could be race conditions that lead to records not being picked up.

To avoid such undesired behaviors, we recommend using monotonically increasing `UPDATED_AT` value, and avoid updating the table during your scheduled sync run. 

### Is order preserved when there are multiple records for the same ID in a sync?
The processing order is not 100% predictable. For example, if there are multiple rows with the same `EXTERNAL_ID` in the table during a sync, we cannot guarantee which value would end up in the final profile. 

### What security measures are there in CDI?
On CDI side: 
- All credentials are encrypted within our database, and only certain employees have authenticated access to them.
- We use encrypted connections to get data to customer warehouses.
- We make requests to the braze api endpoints using the same api keys and tls connections as we recommend our customers use.
- We regularly update our libraries and get any security patches.

From the customers side:
- We highly recommend that you restrict the credential access to the minimum required for CDI to operate. we simply need to be able to run select (and count) on the specific tables and views.
- You can restrict the IPs that can access the tables to the officially published [braze IPs]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/.#step-1-set-up-tables-or-views)
