---
nav_title: File storage integrations
article_title: File Storage Integrations
description: "This page covers Braze Cloud Data Ingestion and how to sync relevant data from S3 to Braze."
page_order: 3
page_type: reference

---

# File storage integrations

> This page covers how to set up Cloud Data Ingestion support and sync relevant data from S3 to Braze.

## How it works

You can use Cloud Data Ingestion (CDI) for S3 to directly integrate one or more S3 buckets in your AWS account with Braze. When new files are published to S3, a message is posted to SQS, and Braze Cloud Data Ingestion takes in those new files. 

Cloud Data Ingestion supports the following:

- JSON files
- CSV files
- Parquet files
- Attribute, custom event, purchase event, user delete, and catalog data

## Prerequisites

The integration requires the following resources:

 - S3 bucket for data storage 
 - SQS queue for new file notifications 
 - IAM role for Braze access  

### AWS definitions

First, define the terms used during this task.

| Term | Definition |
| --- | --- |
| Amazon Resource Name (ARN) | The ARN is a unique identifier for AWS resources. |
| Identity and Access Management (IAM) | IAM is a web service that lets you securely control access to AWS resources. In this tutorial, you will create an IAM policy and assign it to an IAM role to integrate your S3 bucket with Braze Cloud Data Ingestion. |
| Amazon Simple Queue Service (SQS) | SQS is a hosted queue that lets you integrate distributed software systems and components. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Setting up Cloud Data Ingestion in AWS

### Step 1: Create a source bucket

Create a general-purpose S3 bucket with default settings in your AWS account. S3 buckets can be reused across syncs as long as the folder is unique.

The default settings are:

- ACLs Disabled
- Block all public access
- Disable bucket versioning
- SSE-S3 encryption

Take note of the region you’ve created the bucket in, as you will create an SQS queue in the same region in the next step.

### Step 2: Create SQS queue

Create an SQS queue to track when objects are added to the bucket you’ve created. Use the default configuration settings for now. 

An SQS queue must be unique globally (for example, only one can be used for a CDI sync and cannot be reused in another workspace).

{% alert important %}
Be sure to create this SQS in the same region as the one you created the bucket in.
{% endalert %}

Make sure you take note of the ARN and the URL of the SQS as you’ll be using it frequently during this configuration.

![Selecting "Advanced" with an example JSON object to define who can access a queue.]({% image_buster /assets/img/cloud_ingestion/s3_ARN.png %})

### Step 3: Set up access policy

To set up the access policy, choose **Advanced options**. 

Append the following statement to the queue's access policy, being careful to replace `YOUR-BUCKET-NAME-HERE` with your bucket name, and `YOUR-SQS-ARN` with your SQS queue ARN, and `YOUR-AWS-ACCOUNT-ID` with your AWS account ID: 

``` json 
{
  "Sid": "braze-cdi-s3-sqs-publish",
  "Effect": "Allow",
  "Principal": {
    "Service": "s3.amazonaws.com"
  },
  "Action": "SQS:SendMessage",
  "Resource": "YOUR-SQS-ARN",
  "Condition": {
    "StringEquals": {
      "aws:SourceAccount": "YOUR-AWS-ACCOUNT-ID"
    },
    "ArnLike": {
      "aws:SourceArn": "arn:aws:s3:::YOUR-BUCKET-NAME-HERE"
    }
  }
} 
```

### Step 4: Add an event notification to the S3 bucket

1. In the bucket created in step 1, go to **Properties** > **Event notifications**.
2. Give the configuration a name. Optionally, specify a prefix or suffix to target if you only want a subset of files to be ingested by Braze.
3. Under **Destination**, select **SQS queue** and provide the ARN of the SQS you created in step 2.

{% alert note %}
If you upload your files to the root folder of an S3 bucket and then move some of the files to a specific folder in the bucket, you may encounter an unexpected error. Instead, you can change the event notifications to send for only the files in the prefix, avoid placing files in the S3 bucket outside that prefix, or update the integration with no prefix, which will then ingest all files.
{% endalert %}

### Step 5: Create an IAM policy

Create an IAM policy to allow Braze to interact with your source bucket. To get started, sign in to the AWS management console as an account administrator. 

1. Go to the IAM section of the AWS Console, select **Policies** in the navigation bar, then select **Create Policy**.<br><br>![The "Create policy" button in the AWS Console.]({% image_buster /assets/img/create_policy_1_list.png %})<br><br>

2. Open the **JSON** tab and input the following code snippet into the **Policy Document** section, taking care to replace `YOUR-BUCKET-NAME-HERE` with your bucket name, and `YOUR-SQS-ARN-HERE` with your SQS queue name: 

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:GetObjectAttributes", "s3:GetObject"],
            "Resource": ["arn:aws:s3:::YOUR-BUCKET-NAME-HERE"]
        },
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:GetObjectAttributes", "s3:GetObject"],
            "Resource": ["arn:aws:s3:::YOUR-BUCKET-NAME-HERE/*"]
        },
        {
            "Effect": "Allow",
            "Action": [
                "sqs:DeleteMessage",
                "sqs:GetQueueUrl",
                "sqs:ReceiveMessage",
                "sqs:GetQueueAttributes"
            ],
            "Resource": "YOUR-SQS-ARN-HERE"
        }
    ]
}

```  

{: start="3"}
3. Select **Review Policy** when you're finished.

4. Give the policy a name and description, then select **Create Policy**.  

![An example policy named "new-policy-name."]({% image_buster /assets/img/create_policy_3_name.png %})

![The description field for the policy.]({% image_buster /assets/img/create_policy_4_created.png %})

### Step 6: Create an IAM role

To complete the setup on AWS, you will create an IAM role and attach the IAM policy from step 4 to it. 

1. Within the same IAM section of the console where you created the IAM policy, go to **Roles** > **Create Role**. 

<br><br>![The "Create role" button.]({% image_buster /assets/img/create_role_1_list.png %})<br><br>

{: start="2"}
2. Copy the Braze AWS account ID from your Braze dashboard. Go to **Cloud Data Ingestion**, select **Create New Data Sync**, and select **S3 Import**.

3. In AWS, select **Another AWS Account** as the trusted entity selector type. Provide your Braze account ID. Select the **Require external ID** checkbox, and enter an external ID for Braze to use. This is the generated external ID from creating an S3 Currents connection in the **Credentials** section of your Currents connection in the Braze dashboard. Select **Next** when complete. 

<br><br> ![The S3 "Create Role" page. This page has fields for role name, role description, trusted entities, policies, and permissions boundary.]({% image_buster /assets/img/create_role_2_another.png %})<br><br>

{: start="4"}
4. Attach the policy created in step 4 to the role. Search for the policy in the search bar, and select a checkmark next to the policy to attach it. Select **Next** when complete.

<br><br>![Role ARN with the new-policy-name selected.]({% image_buster /assets/img/create_role_3_attach.png %})<br><br>

Give the role a name and a description, and select **Create Role**.

<br><br>![An example role named "new-role-name".]({% image_buster /assets/img/create_role_4_name.png %})<br><br>

{: start="5"}
5. Take note of the ARN of the role you created and the external ID you generated, because you need them to create the Cloud Data Ingestion integration.

## Setting up Cloud Data Ingestion in Braze

1. To create a new integration, go to **Data Settings** > **Cloud Data Ingestion**, select **Create New Data Sync**, and select **S3 Import** from the file sources section. 
2. Input the information from the AWS setup process to create a new sync. Specify the following:

  - Role ARN
  - External ID
  - SQS URL (must be unique for each new integration)
  - Bucket name
  - Folder path (optional, must be unique across syncs in a workspace)
  - Region

![Example security credentials as displayed in S3 to create a new import sync.]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_1.png %})

{: start="3"}
3. Name your integration, and select the data type for this integration. 

<br><br>![Setting up sync details for "cdi-s3-as-source-integration" with user attributes as the data type.]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_2.png %})<br><br>

{: start="4"}
4. Add a contact email for notifications if the sync breaks because of access or permissions issues. Optionally, turn on notifications for user-level errors and sync successes. 

<br><br> ![Setting up notification preferences for sync error notifications.]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_3.png %})<br><br>

{: start="5"}
5. Finally, test the connection and save the sync. 

<br><br>![An option to test the connection with a data preview.]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_4.png %})

## Required file formats

Cloud Data Ingestion supports JSON, CSV, and Parquet files. Each file must contain one or more of the supported identifier columns and a payload column as a JSON string.

Braze doesn’t enforce any additional filename requirements beyond what's enforced by AWS. Filenames should be unique. We recommend appending a timestamp for uniqueness.

### User identifiers

Your source file may contain one or more user identifier columns or keys. Each row should only contain one identifier, but a source file may have multiple identifier types.

| Identifier | Description |
| --- | --- |
| `EXTERNAL_ID` | This identifies the user you want to update. This should match the `external_id` value used in Braze. |
| `ALIAS_NAME` and `ALIAS_LABEL` | These two columns create a user alias object. `alias_name` should be a unique identifier, and `alias_label` specifies the type of alias. Users may have multiple aliases with different labels, but only one `alias_name` per `alias_label`. |
| `BRAZE_ID` | The Braze user identifier. This is generated by the Braze SDK, and new users cannot be created using a Braze ID through Cloud Data Ingestion. To create new users, specify an external user ID or user alias. |
| `EMAIL` | The user's email address. If multiple profiles with the same email address exist, the most recently updated profile will be prioritized for updates. If you include both email and phone, we will use the email as the primary identifier. |
| `PHONE` | The user's phone number. If multiple profiles with the same phone number exist, the most recently updated profile will be prioritized for updates. |
|`PAYLOAD` | This is a JSON string of the fields you want to sync to the user in Braze. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Unlike with data warehouse sources, the `UPDATED_AT` column is neither required nor supported. 
{% endalert %}

{% tabs %}
{% tab JSON Attributes %}
``` json  
{"external_id":"s3-qa-0","payload":"{\"name\": \"GT896\", \"age\": 74, \"subscriber\": true, \"retention\": {\"previous_purchases\": 21, \"vip\": false}, \"last_visit\": \"2023-08-08T16:03:26.600803\"}"}
{"external_id":"s3-qa-1","payload":"{\"name\": \"HSCJC\", \"age\": 86, \"subscriber\": false, \"retention\": {\"previous_purchases\": 0, \"vip\": false}, \"last_visit\": \"2023-08-08T16:03:26.600824\"}"}
{"external_id":"s3-qa-2","payload":"{\"name\": \"YTMQZ\", \"age\": 43, \"subscriber\": false, \"retention\": {\"previous_purchases\": 23, \"vip\": true}, \"last_visit\": \"2023-08-08T16:03:26.600831\"}"}
{"external_id":"s3-qa-3","payload":"{\"name\": \"5P44M\", \"age\": 15, \"subscriber\": true, \"retention\": {\"previous_purchases\": 7, \"vip\": true}, \"last_visit\": \"2023-08-08T16:03:26.600838\"}"}
{"external_id":"s3-qa-4","payload":"{\"name\": \"WMYS7\", \"age\": 11, \"subscriber\": true, \"retention\": {\"previous_purchases\": 0, \"vip\": false}, \"last_visit\": \"2023-08-08T16:03:26.600844\"}"}
{"external_id":"s3-qa-5","payload":"{\"name\": \"KCBLK\", \"age\": 47, \"subscriber\": true, \"retention\": {\"previous_purchases\": 11, \"vip\": true}, \"last_visit\": \"2023-08-08T16:03:26.600850\"}"}
{"external_id":"s3-qa-6","payload":"{\"name\": \"T93MJ\", \"age\": 47, \"subscriber\": true, \"retention\": {\"previous_purchases\": 10, \"vip\": false}, \"last_visit\": \"2023-08-08T16:03:26.600856\"}"}
```  
{% alert important %}
Every line in your source file must contain valid JSON, or the file will be skipped. 
{% endalert %}
{% endtab %}
{% tab JSON Custom Events %}
``` json  
{"external_id":"s3-qa-0","payload":"{\"app_id\": \"YOUR_APP_ID\", \"name\": \"view-206\", \"time\": \"2024-04-02T14:34:08\", \"properties\": {\"bool_value\": false, \"preceding_event\": \"unsubscribe\", \"important_number\": 206}}"}
{"external_id":"s3-qa-1","payload":"{\"app_id\": \"YOUR_APP_ID\", \"name\": \"view-206\", \"time\": \"2024-04-02T14:34:08\", \"properties\": {\"bool_value\": false, \"preceding_event\": \"unsubscribe\", \"important_number\": 206}}"}
```  
{% alert important %}
Every line in your source file must contain valid JSON, or the file will be skipped. 
{% endalert %}
{% endtab %}
{% tab JSON Purchase Events %}
``` json  
{"external_id":"s3-qa-0","payload":"{\"app_id\": \"YOUR_APP_ID\", \"product_id\": \"product-11\", \"currency\": \"BSD\", \"price\": 8.511527858335066, \"time\": \"2024-04-02T14:34:08\", \"quantity\": 19, \"properties\": {\"is_a_boolean\": true, \"important_number\": 40, \"preceding_event\": \"click\"}}"}
{"external_id":"s3-qa-1","payload":"{\"app_id\": \"YOUR_APP_ID\", \"product_id\": \"product-11\", \"currency\": \"BSD\", \"price\": 8.511527858335066, \"time\": \"2024-04-02T14:34:08\", \"quantity\": 19, \"properties\": {\"is_a_boolean\": true, \"important_number\": 40, \"preceding_event\": \"click\"}}"}
```  
{% alert important %}
Every line in your source file must contain valid JSON, or the file will be skipped.
{% endalert %}

{% endtab %}
{% tab CSV Attributes %}
```plaintext  
external_id,payload
s3-qa-load-0-d0daa196-cdf5-4a69-84ae-4797303aee75,"{""name"": ""SNXIM"", ""age"": 54, ""subscriber"": true, ""retention"": {""previous_purchases"": 19, ""vip"": true}, ""last_visit"": ""2023-08-08T16:03:26.598806""}"
s3-qa-load-1-d0daa196-cdf5-4a69-84ae-4797303aee75,"{""name"": ""0J747"", ""age"": 73, ""subscriber"": false, ""retention"": {""previous_purchases"": 22, ""vip"": false}, ""last_visit"": ""2023-08-08T16:03:26.598816""}"
s3-qa-load-2-d0daa196-cdf5-4a69-84ae-4797303aee75,"{""name"": ""EP1U0"", ""age"": 99, ""subscriber"": false, ""retention"": {""previous_purchases"": 23, ""vip"": false}, ""last_visit"": ""2023-08-08T16:03:26.598822""}"
```
{% endtab %}
{% tab CSV Catalogs  %}
```plaintext  
ID,PAYLOAD
85,"{""product_name"": ""Product 85"", ""price"": 85.85}" 
1,"{""product_name"": ""Product 1"", ""price"": 1.01}" 
```
{% endtab %}

{% endtabs %}  

For examples of all supported file types, refer to the sample files in [braze-examples](https://github.com/braze-inc/braze-examples/tree/main/cloud-data-ingestion/braze-examples/payloads/file_storage).  

## Things to know

- Files added to the S3 source bucket should not exceed 512&nbsp;MB. Files larger than 512&nbsp;MB will result in an error and won't be synced to Braze.
- While there is no additional limit on the number of rows per file, we recommend using smaller files to improve how fast your syncs run. For example, a 500&nbsp;MB file would take considerably longer to ingest than five separate 100&nbsp;MB files.
- There's no additional limit on the number of files uploaded in a given time.
- Ordering isn't supported in or between files. We recommend batching updates periodically if you're monitoring for any expected race conditions.

## Troubleshooting

### Uploading files and processing

CDI will only process files that are added after the sync is created. In this process, Braze looks for new files to be added, which triggers a new message to SQS. This will kick off a new sync to process the new file.

Existing files can be used to validate the data structure in the test connection, but they will not be synced to Braze. Any existing files that should be synced must be reuploaded to S3 to be processed by CDI.

### Handling unexpected file errors

If you're observing a high number of errors or failed files, you may have another process adding files to the S3 bucket in a folder other than the target folder for CDI.

When files are uploaded to the source bucket but not in the source folder, CDI will process the SQS notification, but it does not take any action on the file, so this may appear as an error.
