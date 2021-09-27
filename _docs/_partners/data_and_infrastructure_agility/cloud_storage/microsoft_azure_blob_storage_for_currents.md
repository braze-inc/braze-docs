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

After transporting data into Azure Blob Storage, you can use ETL processes (Extract, Transform, Load) to transfer your data to other locations.

## Integration

Integration with Microsoft Azure Blob Storage requires a Storage Account and a Connection String to allow Braze to connect to stream Currents data.

### Step 1: Create Storage Account

Navigate to "Storage Accounts" in the sidebar, and click the **Add** button in the center column to create a new storage account. Even if you already have a storage account, we recommend creating a new one specifically for your Braze data.

All you need to do is give the Storage Account a name. You don't need to change any of the defaults.

![Azure Blob]({% image_buster /assets/img/azure-currents-step-1.png %})

### Step 2: Get Connection String

Once the Storage Account is deployed, navigate to the Access Keys menu from the center column. Take note of the Connection String. Microsoft provides two access keys so that you can maintain connections using one key while regenerating the other. You only need the connection string from one of them.

{% alert note %}
Braze Currents uses the Connection String from this menu, not the Key.
{% endalert %}

![Azure Blob]({% image_buster /assets/img/azure-currents-step-2.png %})

### Step 3: Create a Blob Service Container

Then, navigate to the "Blobs" menu under the "Blob Service" section of the center column. Create a Blob Service Container within that same Storage Account that you created earlier. All you need to do is give the Blob Service Container a name. You don't need to change any of the defaults. Take note of the name of the container.

![Azure Blob]({% image_buster /assets/img/azure-currents-step-3.png %})

### Step 4: Finish Up

Add this information to the Azure Blob Currents page on the dashboard, and press "Launch Current".

![Azure Blob]({% image_buster /assets/img_archive/currents-azure-blob-edit.png %})

{% alert important %}
It's important to keep your Connection String up to date; if your connector's credentials expire, the connector will stop sending events. If this persists for more than **48 hours**, the connector's events will be dropped and data will be permanently lost.
{% endalert %}

You can also add the following customizations, based on your needs:

-   Prefix (defaults to `currents`)

