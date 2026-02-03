---
nav_title: Sync logs and observability
article_title: Sync logs and observability
page_order: 10
page_type: reference
description: "This page provides an overview of the observability features available in CDI."
---

# Sync logs and observability

> The Cloud Data Ingestion (CDI) **Sync Log** dashboard allows you to monitor all data processed by CDI, verify whether data was synced successfully, and diagnose any issues with "incorrect" or missing data.

To access the sync logs, go to **Data Settings** > **Cloud Data Ingestion** and select the **Sync Log** tab.

## Understanding the Sync Log dashboard

The main **Sync Log** page provides a high-level overview of all your sync runs, including an overview of recent syncs by their current or final status.

* **Running:** Sync jobs that are currently in progress.  
* **Success:** Sync jobs that completed, and all rows were processed successfully.  
* **Partial Success:** Sync jobs that completed, but one or more rows encountered an error.  
* **Error:** Sync jobs that failed to complete.  
* **Limit Exceeded:** Sync jobs that stopped processing because a data limit was exceeded.

![An example of sync logs with 6,576 total successes.]({% image_buster /assets/img/cloud_ingestion/sync_logs1.png %}){: style="max-width:80%"}

Sync logs also provide the following details for each sync:

* **Sync name:** The name of the sync configuration.  
* **Run ID:** A unique identifier for a specific execution of the sync. Select this ID to view more details. This can also be used in the [CDI API endpoints]({{site.baseurl}}/api/endpoints/cdi), or to reference a sync run with Braze Support.   
* **Status:** The status of the run (success, partial success, error, running).  
* **New rows read from source:** The number of new rows pulled from your data warehouse for this run.  
* **Results:** A breakdown of how many rows succeeded or failed within the run.  
* **Last "UPDATED_AT":** The timestamp of the most recent record processed in this sync run.  
* **Run start time:** When the sync job began.  
* **Run duration:** The total time the sync job took to complete.

![Details for a sync log.]({% image_buster /assets/img/cloud_ingestion/sync_logs3.png %}){: style="max-width:80%"}

### Data retention

Sync log data, including all row-level payloads and error details, is retained for up to **30 days**. Logs older than 30 days will be automatically purged.

Sync run metadata such as the number of rows processed is retained for at least 12 months.

### Filtering sync logs

You can filter the sync logs table to find specific runs. The available filters include:

* **Job start date:** Select a predefined range (like "Last 30 days") or a custom date range.  
* **Status:** Filter by one or more sync statuses (like showing only **Error** and **Partial success** statuses).  
* **Sync name:** Search for a specific sync by its name.

To investigate a specific sync, select the relevant **Run ID** from the Sync logs table. In the **Run details** page, you'll find a granular, row-by-row log of the sync.

### Run overview

This section summarizes the selected run, including its start time, end time, duration, and the total number of rows read from the source. It also provides a count of how many rows succeeded and how many resulted in an error.

### Rows processed in this run

This table provides row-level visibility into the data processed during the sync, allowing you to validate individual records.

* **Search:** You can search for a specific user within the run's results using the **Search by user ID** bar.  
* **Available details:**   
  * **UPDATED_AT:** The timestamp from the `UPDATED_AT` column for that specific row.  
  * **ID:** The user identifiers (such as `external_id`, `email`, or `alias_name`) used to match the record to a Braze user profile.  
  * **Status:** The individual processing status for that row (**Success** or **Error**).  
  * **Source payload:** A link to view the data payload.  
  * **Error reason:** If the status is **Error**, this column provides a message explaining why the row failed to sync.

#### Viewing payloads

To see the exact data sent to Braze for a specific row, select **View payload** in the **Source** payload column. This displays the raw JSON payload that was processed for that user.

![Payload example for a specific row in a sync log.]({% image_buster /assets/img/cloud_ingestion/sync_logs2.png %}){: style="max-width:80%"}

#### Exporting sync logs

Select **Export rows** to export the row-level logs for a sync run. Then, choose to export by:

* **Rows with errors:** Downloads a file containing only the rows that had an **Error** status.
* **All rows:** Downloads a file containing every row processed in the run.

{% alert important %}
Exporting sync logs for all rows is currently in early access. Contact your Braze account manager if you're interested in participating in the early access.
{% endalert %}

Logs can't be exported directly from the dashboard. After the export is generated, you’ll receive an email with a link to download the log export file. 

## Notifications

You can configure email notifications to stay informed about the status of your CDI syncs. These settings are configured when you create a sync and can be updated at any time.

### Error notifications

At least one email address contact is required to receive notifications for sync-level errors. These alerts are sent when an entire sync job fails to run or complete, or if the sync runs into an error that requires user intervention to change, such as expired credentials or a missing source table.

Additional notifications include:

- **Row error:** Receive alerts when a certain percentage of rows fail to update within a sync.
- **Failure threshold (%):** Specify the percentage of row failures that should trigger an alert. For example, setting this to **1** would send a notification if 1% or more of the rows in a sync run result in an error.
- **Sync success:** Receive a notification upon the successful completion of a sync.
- **Alert even if no rows change:** Receive a notification even when a successful sync run processes zero new or updated rows.