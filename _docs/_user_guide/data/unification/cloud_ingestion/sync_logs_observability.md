---
nav_title: Sync Logs and Observability
article_title: Sync Logs and Observability
page_order: 10
page_type: reference
description: "This page provides an overview of the observability features available in CDI."
---

# Sync Logs and Observability

Cloud Data Ingestion (CDI) Sync Logs allow you to monitor all data processed by CDI, verify whether data was synced successfully, and diagnose any issues with "incorrect" or missing data.

Access the logs by navigating to **Data Settings \> Cloud Data Ingestion** and selecting the **Sync logs** tab.

## Sync Logs Dashboard

The main **Sync logs** page provides a high-level overview of all your sync runs.

### Sync Status Overview

At the top of the page, see a summary of recent syncs by their current or final status:

* **Running:** Sync jobs that are currently in progress.  
* **Success:** Sync jobs that completed, and all rows were processed successfully.  
* **Partial Success:** Sync jobs that completed, but one or more rows encountered an error.  
* **Error:** Sync jobs that failed to complete.  
* **Limit Exceeded:** Sync jobs that stopped processing because a data limit was exceeded.

### Sync Logs Digest

See individual historical sync runs, including the following details for each:

* **Sync name:** The name of the sync configuration.  
* **Run ID:** A unique identifier for a specific execution of the sync. Click this ID to see more details. This can also be used in the CDI API endpoints, or to reference a sync run with Braze support.   
* **Status:** The status of the run (e.g., Success, Partial success, Error, Running).  
* **New rows read from source:** The number of new rows pulled from your data warehouse for this run.  
* **Results:** A breakdown of how many rows succeeded or failed within the run.  
* **Last "UPDATED\_AT":** The timestamp of the most recent record processed in this sync run.  
* **Run start time:** When the sync job began.  
* **Run duration:** The total time the sync job took to complete.

### Filtering Sync Logs

You can filter the Sync logs table to find specific runs. The available filters include:

* **Job start date:** Select a predefined range (like "Last 30 days") or a custom date range.  
* **Status:** Filter by one or more sync statuses (e.g., show only Error and Partial success).  
* **Sync name:** Search for a specific sync by its name.

## Run Details

To investigate a specific sync, click its **Run ID** from the Sync logs table. This will take you to the **Run details** page, which provides a granular, row-by-row log of the sync.

### Run Overview

This section summarizes the selected run, including its start time, end time, duration, and the total number of rows read from the source. It also provides a count of how many rows **succeeded** and how many resulted in an **error**.

### Rows Processed in This Run

This table provides row-level visibility into the data processed during the sync, allowing you to validate individual records.

* **Search:** You can search for a specific user within the run's results using the **Search by user ID** bar.  
* **Available details:**   
  * **UPDATED\_AT:** The timestamp from the UPDATED\_AT column for that specific row.  
  * **ID:** The user identifiers (such as external\_id, email, or alias\_name) used to match the record to a Braze user profile.  
  * **Status:** The individual processing status for that row (Success or Error).  
  * **Source payload:** A link to view the data payload.  
  * **Error reason:** If the status is Error, this column provides a message explaining why the row failed to sync.

#### Viewing Payloads

To see the exact data sent to Braze for a specific row, click **View payload** in the Source payload column. This will display the raw JSON payload that was processed for that user.

#### Exporting Logs

You can export the row-level logs for a sync run using the **Export rows** button. Braze provides two export options:

* **Export all logs:** Downloads a file containing every row processed in the run.  
* **Export error logs only:** Downloads a file containing only the rows that had an Error status.

Logs can’t be exported directly from the dashboard. After the export is generated, you’ll receive an email with a link to download the log export file. 

## Notifications
You can configure email notifications to stay informed about the status of your CDI syncs. These settings are configured when you create a sync and can be updated at any time.

### Sync Error Notifications
At least one email address contact is required to receive notifications for sync-level errors. These alerts are sent when an entire sync job fails to run or complete, or if the sync runs into an error that requires user intervention to change (e.g., expired credentials or a missing source table).

### Additional Notifications (Optional)
**Row Error:** Toggle this option to receive alerts when a certain percentage of rows fail to update within a sync.

**Failure threshold (%):** If enabled, specify the percentage of row failures that should trigger an alert. For example, setting it to 1 would send a notification if 1% or more of the rows in a sync run result in an error.

**Sync success:** Toggle this option to receive a notification upon the successful completion of a sync.

**Alert even if no rows change:** If Sync success is enabled, check this box if you wish to be notified even when a successful sync run processes 0 new or updated rows.

## Data Retention

Sync log data, including all row-level payloads and error details, is retained for a maximum of **30 days**. Logs older than 30 days will be automatically purged.

Sync run metadata such as the number of rows processed is retained for at least 12 months. 

