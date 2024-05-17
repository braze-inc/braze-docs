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
This type of email usually includes an error message that CDI encountered during the sync process. Often, it is due to a setup error. Some common issues are as follows:
  - CDI cannot access the data warehouse/table with the credentials set up in the integration. This could mean the credentials in CDI are incorrect, or they are misconfigured on the data warehouse. Check out [Data Warehouse Integrations]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/) for more details.
  - SQL error due to the table not found. Update the integration with a correct database config or create the database / table on the data warehouse.
  - Catalog not found, meaning the catalog setup in the integration does not exist in Braze catalog. A catalog can be removed after the integration was setup. To resolve the issue, either update the integration to use a different catalog or create a new catalog that match the catalog name in the integration.


- **Row Errors in your CDI Sync**  
This indicates that some data cannot be processed in the sync. To find out Navigate to CDI page in Braze. Open Sync Log tab to check the error details for the sync job, which should show you what kind of errors are there in the job run.

### How can I update my email alert preferences for CDI integrations?
Each integration has its own notification preference. In the CDI UI, click on the integration name you want to update. Scroll to the "Notification Preferences" section, and you can update how you want to receive alerts regarding the selected integration.

### What to do if a future UPDATED_AT was synced in an integration?
CDI use UPDATED_AT to decide what data is new. Once a future UPDATED_AT is synced, any data prior to that furture date time will not be processed.

User will need to clean up the data by correcting the UPDATED_AT, remove old data that were already synced to Braze then create a new integration to process the table again.