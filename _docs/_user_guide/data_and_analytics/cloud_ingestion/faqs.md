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
  - SQL error due to the table not being found. Update the integration with the correct database config or create matching resources (e.g., database/table) on the data warehouse.
  - Catalog not found. The catalog set up in the integration does not exist in the Braze catalog. A catalog can be removed after the integration was set up. To resolve the issue, either update the integration to use a different catalog or create a new catalog that matches the catalog name in the integration.

- **Row Errors in your CDI Sync**  
This indicates that some data cannot be processed in the sync. To find out what is causing the errors, navigate to the CDI page in Braze. Open the **Sync Log** tab to check the error details for the sync job.

### How can I update my email alert preferences for CDI integrations?
Each integration has its own notification preference. In the CDI UI, click on the integration name you want to update. Scroll to the "Notification Preferences" section, and you can update how you want to receive alerts regarding the selected integration.

### What to do if a future UPDATED_AT was synced in an integration?
CDI uses UPDATED_AT to decide what data is new. Once a future UPDATED_AT is synced, any data prior to that future date and time will not be processed.

Users will need to clean up the data by correcting the UPDATED_AT, removing old data that were already synced to Braze, then create a new integration to process the table again.