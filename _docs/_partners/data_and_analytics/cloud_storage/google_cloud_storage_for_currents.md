---
nav_title: Google Cloud Storage
article_title: Google Cloud Storage
alias: /partners/google_cloud_storage_for_currents/
description: "This reference article outlines the partnership between Braze and Google Cloud Storage, a massively scalable object storage for unstructured data."
page_type: partner
tool: Currents
search_tag: Partner

---

# Google Cloud Storage

> [Google Cloud Storage](https://cloud.google.com/storage/) is massively scalable object storage for unstructured data offered by Google as part of the Cloud Computing product suite.

{% alert important %}
If you're switching between cloud storage providers, reach out to your Braze customer success manager for further assistance on setting up and validating your new integration.
{% endalert %}

The Braze and Google Cloud Storage integration allows you to stream Currents data to Google Cloud Storage. You can later use an ETL process (Extract, Transform, Load) to transfer your data to other locations, such as Google BigQuery.

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Google Cloud Storage account | A Google Cloud Storage account is required to take advantage of this partnership. |
| Currents | In order to export data back into Google Cloud Storage, you need to have [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) set up for your account. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

To integrate with Google Cloud Storage, you must set up the appropriate credentials that allow Braze to get information about the storage buckets being written to (`storage.buckets.get`) and create objects within that bucket (`storage.objects.create`). 

This can be done using the following instructions, which will walk you through creating a role and service account that will generate a private key to use in your Currents integration.

### Step 1: Create role

Create a new role in your Google Cloud Platform Console by navigating to **IAM & admin** > **Roles** > **+ Create Role**.

![]({% image_buster /assets/img/gcs1.png %})

Give the role a name, then select **+Add Permissions** and choose the following:

- `storage.objects.create`
- `storage.objects.delete`
- `storage.objects.list`
- `storage.objects.get`
- `storage.buckets.get`

{% alert note %}
The `storage.objects.delete` permission is optional. It allows Braze to clean up incomplete files.<br><br>In rare circumstances, Google Cloud may terminate connections early, resulting in Braze writing incomplete files to Google Cloud Storage. In most cases, Braze will retry and create a new file with the correct data, leaving the old file in Google Cloud Storage.
{% endalert %}

When you're finished, select **Create**.

![]({% image_buster /assets/img/gcs2.png %})

### Step 2: Create a new service account

#### Step 2.1: Create the service account

Create a new service account in your Google Cloud Platform Console by navigating to **IAM & admin** > **Service Accounts** and selecting **Create Service Account**.

![]({% image_buster /assets/img/gcs3.png %})

Next, give the service account a name and grant it access to your newly created custom role.

![In the Google Cloud Platform, on the create services page, type the name of your role in the "Select a Role" field.]({% image_buster /assets/img/gcs4.png %})

#### Step 2.2: Create a key

At the bottom of the page, use the **Create Key** button to create a **JSON** private key to use in Braze. After the key is created, it will download onto your machine.

![]({% image_buster /assets/img/gcs5.png %})

### Step 3: Set up Currents in Braze

In Braze, navigate to **Currents** > **+ Create Current** > **Google Cloud Storage Data Export** and provide your integration name and contact email.

Next, upload your JSON private key under **GCS JSON Credentials** and provide your CGS bucket name and GCS prefix (optional). 

{% alert important %}
It's important to keep your credentials file up to date; if your connector's credentials expire, the connector will stop sending events. If this persists for more than **48 hours**, the connector's events will be dropped, and data will be permanently lost.
{% endalert %}

![The Google Cloud Storage Currents page in Braze. On this page exist fields for integration name, contact email, GCS JSON credential, GCS bucket name, and prefix.]({% image_buster /assets/img/gcs6.png %})

Finally, scroll to the bottom of the page and select which message engagement events or customer behavior events you would like to export. When completed, launch your Current.

### Step 4: Set up Google Cloud Storage exports

To set up Google Cloud Storage (GCS) exports, go to **Technology Partners** > **Google Cloud Storage**, enter your GCS credentials, and select **Make this the default data export destination**.

Keep in mind that the organization and contents of any exported files will be identical across AWS S3, Microsoft Azure, and Google Cloud Storage integrations.

{% alert important %}
Be sure to input the full JSON value that's [generated by Google Cloud](https://cloud.google.com/iam/docs/keys-create-delete).
{% endalert %}

![The Google Cloud Storage page in the Braze dashboard.]({% image_buster /assets/img/gcs7.png %}){: style="max-width:70%;"}

### Step 5: Test your service account credentials (optional)

Your Google Cloud IAM service account must have the following permissions:

- `storage.objects.create`
- `storage.objects.delete`
- `storage.objects.list`
- `storage.objects.get`
- `storage.buckets.get`

To verify these permissions in the Braze dashboard, go to the **Google Cloud Storage** page, then select **Test Credentials**.

![The Google Cloud Storage credentials section in the Braze dashboard.]({% image_buster /assets/img/gcs8.png %}){: style="max-width:70%;"}

## Export behavior

Users that have integrated a cloud data storage solution, and are trying to export APIs, dashboard reports, or CSV reports will experience the following:

- All API exports will not return a download URL in the response body and must be retrieved through data storage.
- All dashboard reports and CSV reports will be sent to the users email for download (no storage permissions required) and backed up on Data Storage.

## Troubleshooting

### Google Cloud Storage Credentials are invalid

If you receive the following error when attempting enter your credentials:

```
Google Cloud Storage Credentials are invalid. Please ensure that your credentials string, bucket name, and prefix are valid. You do not have read permission.
```

Ensure that your Google Cloud IAM service account has the following permissions:

- `storage.objects.create`
- `storage.objects.delete`
- `storage.objects.list`
- `storage.objects.get`
- `storage.buckets.get`

After verifying, you can [test your credentials in the Braze dashboard](#step-5-test-your-service-account-credentials-optional).
