---
nav_title: Google Cloud Storage
article_title: Google Cloud Storage
page_order: 2
alias: /partners/google_cloud_storage_for_currents/
description: "This article outlines the partnership between Braze and Google Cloud Storage, a massively scalable object storage for unstructured data."
page_type: partner
tool: Currents
search_tag: Partner

---

# Google Cloud Storage

> [Google Cloud Storage](https://cloud.google.com/storage/) is massively scalable object storage for unstructured data offered by Google as part of the Cloud Computing product suite.

The Braze and Google Cloud Storage integration allows you to stream Currents data to Google Cloud Storage. You can later use an ETL process (Extract, Transform, Load) to transfer your data to other locations, such as Google Bigquery.

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Google Cloud Storage account | A Google Cloud Storage account is required to take advantage of this partnership. |
| Currents | In order to export data back into Google Cloud Storage, you need to have [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) set up for your account. |
{: .reset-td-br-1 .reset-td-br-2}

## Integration

To integrate with Google Cloud Storage, you must set up the appropriate credentials that allow Braze to get information about the storage buckets being written to (`storage.buckets.get`) and create objects within that bucket (`storage.objects.create`). 

This can be done using the following instructions, which will walk you through creating a role and service account that will generate a private key to use in your Currents integration.

### Step 1: Create role

Create a new role in your Google Cloud Platform Console by navigating to **IAM & admin > Roles > Create Role**.

![Google cloud storage role creation][2]

Next, give the role a name, add `storage.buckets.get` and `storage.objects.create` permissions, and click **Create**.

![Google cloud storage role permissions][3]

### Step 2: Create a service account

Create a new service account in your Google Cloud Platform Console by navigating to **IAM & admin > Service Accounts** and selecting **Create Service Account**.

![Google cloud storage service account creation][4]

Next, give the service account a name and grant it access to your newly created custom role.

![Google cloud storage service account access][5]

#### Create a key

At the bottom of the page, use the **Create Key** button to create a **JSON** private key to use in Braze. Once created, this key will download onto your machine.

![Google cloud storage private key creation][6]

### Step 3: Set up Currents in Braze

In Braze, navigate to **Currents > + Create Current > Google Cloud Storage Data Export** and provide your integration name and contact email.

Next, upload your JSON private key under **GCS JSON Credentials** and provide your CGS bucket name and GCS prefix (optional). 

{% alert important %}
It's important to keep your credentials file up to date; if your connector's credentials expire, the connector will stop sending events. If this persists for more than **48 hours**, the connector's events will be dropped, and data will be permanently lost.
{% endalert %}

![GCS Currents in Braze][7]

Finally, scroll to the bottom of the page and select which message engagement events or customer behavior events you would like to export. Once completed, launch your Current.

[2]: {% image_buster /assets/img/gcs1.png %}
[3]: {% image_buster /assets/img/gcs2.png %}
[4]: {% image_buster /assets/img/gcs3.png %}
[5]: {% image_buster /assets/img/gcs4.png %}
[6]: {% image_buster /assets/img/gcs5.png %}
[7]: {% image_buster /assets/img/gcs6.png %}
