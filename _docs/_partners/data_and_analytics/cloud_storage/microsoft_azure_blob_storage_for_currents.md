---
nav_title: Microsoft azure blob storage
article_title: Microsoft Azure Blob Storage
alias: /partners/microsoft_azure_blob_storage_for_currents/
description: "This reference article outlines the partnership between Braze Currents and Microsoft Azure Blog Storage, a massively scalable object storage for unstructured data."
page_type: partner
tool: Currents
search_tag: Partner

---

# Microsoft Azure Blob Storage

> [Microsoft Azure Blob Storage](https://azure.microsoft.com/en-us/services/storage/blobs/) is a massively scalable object storage for unstructured data offered by Microsoft as part of the Azure product suite.

{% alert important %}
If you're switching between cloud storage providers, reach out to your Braze customer success manager for further assistance on setting up and validating your new integration.
{% endalert %}

The Braze and Microsoft Azure Blob Storage integration allows you to export data back to Azure and stream Currents data. Later, you can use an ETL process (Extract, Transform, Load) to transfer your data to other locations.

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Microsoft Azure and Azure storage account | A Microsoft Azure and Azure storage account are required to take advantage of this partnership. |
| Currents | To export data to Currents, you must have [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) set up for your account. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

To integrate with Microsoft Azure Blob Storage, you must have a storage account and a connection string to allow Braze to either export data back to Azure or stream Currents data.

### Step 1: Create a storage account

In Microsoft Azure, navigate to **Storage Accounts** in the sidebar and click **+ Add** to create a new storage account. Next, provide a storage account name. Other default settings will not need to be updated. Lastly, select **Review + create**. 

Even if you already have a storage account, we recommend creating a new one specifically for your Braze data.

![]({% image_buster /assets/img/azure-currents-step-1.png %})

### Step 2: Get the connection string

Once the storage account is deployed, navigate to the **Access Keys** menu from the storage account and take note of the connection string.

Microsoft provides two access keys to maintain connections using one key while regenerating the other. You only need the connection string from one of them.

{% alert note %}
Braze uses the connection string from this menu, not the key.
{% endalert %}

![]({% image_buster /assets/img/azure-currents-step-2.png %})

### Step 3: Create a blob service container

Navigate to the **Blobs** menu under the **Blob Service** section of your storage account. Create a Blob Service Container within that storage account you created earlier. 

Provide a name for your Blob Service Container. Other default settings will not need to be updated.

![]({% image_buster /assets/img/azure-currents-step-3.png %})

### Step 4: Set up Currents

In Braze, navigate to **Currents > + Create Current > Azure Blob Data Export** and provide your integration name and contact email.

Next, provide your connection string, container name, and BlobStorage prefix (optional).

![The Microsoft Azure Blob storage Currents page in Braze. On this page exist fields for integration name, contact email, connection string, container name, and prefix.]({% image_buster /assets/img/maz.png %})

Finally, scroll to the bottom of the page and select which message engagement events or customer behavior events you would like to export. When completed, launch your Current.

### Step 5: Set up Azure data export

The following configures credentials that are used for:
1. Segment exports through the API
2. CSV exports (campaign, segment, Canvas user data export via the dashboard)
3. Engagement reports

In Braze, navigate to **Partner Integrations** > **Technology Partners** > **Microsoft Azure** and provide your connection string, Azure storage container name, and Azure storage prefix.

Next, make sure the **Make this the default data export destination** box is checked, this will make sure your exported data is sent to Azure. When completed, save your integration.

![The Microsoft Azure data export page in Braze. On this page exist fields for connection string, container name, and prefix.]({% image_buster /assets/img/azure_data_export.png %})

{% alert important %}
It's important to keep your connection string up to date; if your connector's credentials expire, the connector will stop sending events. If this persists for more than **48 hours**, the connector's events will be dropped, and data will be permanently lost.
{% endalert %}

## Export behavior

Users that have integrated a cloud data storage solution, and are trying to export APIs, dashboard reports, or CSV reports will experience the following:

- All API exports will not return a download URL in the response body and must be retrieved through data storage.
- All dashboard reports and CSV reports will be sent to the user's email for download (no storage permissions required) and backed up on data storage. 
