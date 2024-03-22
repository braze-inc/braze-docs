---
nav_title: File Storage Integrations
article_title: File Storage Integrations
description: "This reference article covers Braze Cloud Data Ingestion and how to sync relevant data from S3 to Braze"
page_order: 3
page_type: reference

---

# File storage integrations

> This article covers how to set up Cloud Data Ingestion support and sync relevant data from S3 to Braze.

You can use Cloud Data Ingestion for S3 to directly integrate one or more S3 buckets in your AWS account with Braze. When new files are published to S3, a message is posted to SQS, and Braze Cloud Data Ingestion takes in those new files. 

Cloud Data Ingestion supports JSON, CSV, and Parquet files, and attributes, event, purchase, and user delete data.

The integration requires the following resources:
 - S3 bucket for data storage 
 - SQS queue for new file notifications 
 - IAM role for Braze access  

{% alert note %}
Braze Cloud Data Ingestion support for S3 is currently in early access. Contact your Braze account manager if you are interested in participating in the early access. 
{% endalert %}

## Setting up Cloud Data Ingest in AWS

Follow these steps to set up a Cloud Data Integest integration in your AWS account:

### Step 1: Create a source bucket

Create a general purpose S3 bucket with default settings in your AWS account. 

The default settings are:
  - ACLs Disabled
  - Block all public access
  - Disable bucket versioning
  - SSE-S3 encryption

Take note of the region you’ve created the bucket in, as you will create an SQS queue in the same region in the next step.

### Step 2: Create SQS resources

Create an SQS queue in the same region you created the S3 bucket. This queue will be used to track when objects are added to the bucket(s) you’ve created.

You can create this queue with default configuration settings until you reach the access policy step. When setting up the access policy, choose Advanced options. Append the following statement to the queue's access policy: 

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

### Step 3: Add an event notification to the S3 bucket

1. In the bucket created in Step 1, go to **Properties** > **Event notifications**.

2. Give the configuration a name. Optionally, specify a prefix or suffix to target if you only want a subset of files to be ingested by Braze.

3. Under **Destination** select **SQS queue** and provide the ARN of the SQS you created in Step 2.

### Step 4: Create an IAM policy

Create an IAM policy to allow Braze to interact with your source bucket. To get started, sign in to the AWS management console as an account administrator. 

1. Go to the IAM section of the AWS Console, select **Policies** in the navigation bar, then select **Create Policy**.<br><br>![]({{site.baseurl}}/assets/img/create_policy_1_list.png)<br><br>

2. Open the **JSON** tab and input the following code snippet into the **Policy Document** section. Replace `YOUR-BUCKET-NAME-HERE` with your bucket name, and `YOUR-SQS-ARN-HERE` with your SQS queue name.  

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

4. Give the policy a name and description and select **Create Policy**.  

![]({{site.baseurl}}/assets/img/create_policy_3_name.png)

![]({{site.baseurl}}/assets/img/create_policy_4_created.png)

### Step 5: IAM Role

To complete the setup on AWS, you will create an IAM role and attach the IAM policy from Step 4 to it. 

1. Within the same IAM section of the console where you created the IAM policy, go to **Roles** > **Create Role**. <br><br>![]({{site.baseurl}}/assets/img/create_role_1_list.png)<br><br>

2. Retrieve the Braze AWS account ID from your Braze dashboard. Go to **Partner Integrations** > **Technology Partners** and select **Amazon S3**. Here you will find the Account ID needed to create your role. 

3. In AWS, select **Another AWS Account** as the trusted entity selector type. Provide your Braze account ID, select the **Require external ID** checkbox, and enter an external ID for Braze to use. Select **Next** when complete. <br><br> ![The S3 "Create Role" page. This page has fields for role name, role description, trusted entities, policies, and permissions boundary.]({{site.baseurl}}/assets/img/create_role_2_another.png)

4. Attach the policy created in Step 4 to the role. Search for the policy in the search bar, and select a checkmark next to the policy to attach it. Select **Next** when complete.<br><br>![Role ARN]({{site.baseurl}}/assets/img/create_role_3_attach.png)<br><br>Give the role a name and a description, and click **Create Role**.<br><br>![Role ARN]({{site.baseurl}}/assets/img/create_role_4_name.png)<br><br>

{: start="5"}
5. Take note of the ARN of the role you just created and the external-id you generated, as you’ll use them to create the CDI Integration.  

## Setting up Cloud Data Ingest in Braze

1. To create a new integration, go to **Data Settings** > **Cloud Data Ingestion**, select **Create New Data Sync**, and select **S3 Import** from the file sources section. 

2. Input the information from the AWS setup process to create a new sync. Specify the following:
- Role ARN
- External ID
- SQS URL (must be unique for each new integration)
- Bucket Name
- Folder Path (optional)
- Region.  

![]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_1.png %})

{: start="3"}
3. Give your integration a name, and select the data type for this integration. <br><br>![]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_2.png %})<br><br>

4. Add a contact email for notifications if the sync breaks because of access or permissions issues. Optionally, turn on notifications for user-level errors and sync successes. <br><br> ![]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_3.png %})<br><br>

{: start ="5"}
5. Finally, test the connection and save the sync. <br><br>![]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_4.png %})