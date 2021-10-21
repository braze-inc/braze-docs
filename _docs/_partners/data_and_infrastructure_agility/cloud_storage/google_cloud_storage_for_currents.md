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

# Google cloud storage

> [Google Cloud Storage](https://cloud.google.com/storage/) is massively scalable object storage for unstructured data offered by Google as part of the Cloud Computing product suite.

After streaming data into Google Cloud Storage Storage, you can use ETL processes (Extract, Transform, Load) to transfer your data to other locations, such as Google Bigquery.

## Integration

integration with google cloud storage requires credentials that allow braze to get information about the storage bucket being written to (`storage.buckets.get`) as well as the ability to create objects within that bucket (`storage.objects.create`). in order to grant those permissions in the google cloud platform iam & admin section, you need to create a custom role and then create a service account that uses that role. doing this will generate a downloadable key that you can then upload into braze so that currents events can be written to your gcs bucket.

### Step 1 - create role

Create a new Role in the **Roles** subsection of the **IAM & admin** section of your **Google Cloud Platform** console

![google_cloud_storage][2]

### Step 2 - grant role permissions

Give the Role a name, add the `storage.buckets.get` and `storage.objects.create` permissions to the Role, and click Create.

![google_cloud_storage][3]

### Step 3 - create a service account

Create a new **Service Account** for your project within the **IAM & admin** section of your **Google Cloud Platform** console.

![google_cloud_storage][4]

### Step 4 - grant access

Give the Service Account a name, and grant it access as your newly created custom Role.

![google_cloud_storage][5]

### Step 5 - create key

Create a key using the JSON format. Once created, this key will download to your machine.

![google_cloud_storage][6]

### Step 6 - upload key

On the **Braze Currents** integration page, upload that JSON key file as your **Credentials File**.

{% alert important %}
It's important to keep your Credentials File up to date; if your connector's credentials expire, the connector will stop sending events. If this persists for more than **48 hours**, the connector's events will be dropped and data will be permanently lost.
{% endalert %}

### Step 7 - finish up

Include your GCS bucket name in the appropriate field so we know where to stream Currents data.

## Customizations

you can also add the following customizations, based on your needs:

-   Prefix (defaults to `currents`)

Add this information to the Google Cloud Storage Currents page in Braze, and press **Save**.

![google_cloud_storage][1]

[1]: {% image_buster /assets/img/google_cloud_storage.png %}
[2]: {% image_buster /assets/img/gcs1.png %}
[3]: {% image_buster /assets/img/gcs2.png %}
[4]: {% image_buster /assets/img/gcs3.png %}
[5]: {% image_buster /assets/img/gcs4.png %}
[6]: {% image_buster /assets/img/gcs5.png %}
