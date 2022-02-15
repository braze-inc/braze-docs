---
nav_title: Microsoft Azure Blob Storage
article_title: Microsoft Azure Blob Storage
page_order: 3
alias: /partners/microsoft_azure_blob_storage_for_currents/
description: "This article outlines the partnership between Braze Currents and Microsoft Azure Blog Storage, a massively scalable object storage for unstructured data."
page_type: partner
tool: Currents
search_tag: Partner

---

# Microsoft Azure Blob Storage

> [Microsoft Azure Blob Storage](https://azure.microsoft.com/en-us/services/storage/blobs/) is a massively scalable object storage for unstructured data offered by Microsoft as part of the Azure product suite.

The Braze and Microsoft Azure Blob Storage integration allows you to stream Currents data. Later, you can use an ETL process (Extract, Transform, Load) to transfer your data to other locations.

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Microsft Azure and Azure storage account | A Microsft Azure and Azure storage account are required to take advantage of this partnership. |
{: .reset-td-br-1 .reset-td-br-2}

## Integration

To integrate with Microsoft Azure Blob Storage, you must have a storage account and a connection string to allow Braze to stream Currents data.

### Step 1: Create a storage account

In Microsoft Azure, navigate to **Storage Accounts** in the sidebar and click **+ Add** to create a new storage account. Next, provide a storage account name. Other default settings will not need to be updated. Lastly, select **Review + create**. 

Even if you already have a storage account, we recommend creating a new one specifically for your Braze data.

![Azure Blob]({% image_buster /assets/img/azure-currents-step-1.png %})

### Step 2: Get connection string

Once the storage account is deployed, navigate to the **Access Keys** menu from the storage account and take note of the connection string.

Microsoft provides two access keys to maintain connections using one key while regenerating the other. You only need the connection string from one of them.

{% alert note %}
Braze Currents uses the connection string from this menu, not the key.
{% endalert %}

![Azure Blob]({% image_buster /assets/img/azure-currents-step-2.png %})

### Step 3: Create a blob service container

Navigate to the **Blobs** menu under the **Blob Service** section of your storage account. Create a Blob Service Container within that storage account you created earlier. 

Provide a name for your Blob Service Container. Other default settings will not need to be updated.

![Azure Blob]({% image_buster /assets/img/azure-currents-step-3.png %})

### Step 4: Setting up Currents in Braze

In Braze, navigate to **Currents > + Create Current > Azure Blob Data Export** and provide your integration name and contact email.

Next, provide your connection string, container name, and BlobStorage prefix (optional).

{% alert important %}
It's important to keep your connection string up to date; if your connector's credentials expire, the connector will stop sending events. If this persists for more than **48 hours**, the connector's events will be dropped, and data will be permanently lost.
{% endalert %}

![Microsoft Azure Blob storage Currents in Braze][1]

Finally, scroll to the bottom of the page and select which message engagement events or customer behavior events you would like to export. Once completed, launch your Current.

[1]: {% image_buster /assets/img/maz.png %}