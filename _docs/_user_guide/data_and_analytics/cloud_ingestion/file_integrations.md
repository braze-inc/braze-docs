---
nav_title: File Storage Integrations
article_title: File Storage Integrations
description: "This reference article covers Braze Cloud Data Ingestion and how to sync relevant data from S3 to Braze"
page_order: 3
page_type: reference

---

# File storage integrations

With Cloud Data Ingestion for S3, set up a direct integration from one or more S3 buckets in your AWS account to Braze. When new files are published to S3, a message is posted to SQS. Braze continuously checks for new files and they're picked up by Cloud Data Ingestion as soon as the file is published. Cloud Data Ingestion supports JSON, CSV, and parquet files and attributes, event, purchase and user delete data.


The integration requires the following resources:
 - S3 bucket for data storage 
 - SQS queue for new file notifications 
 - IAM role for Braze access  

{% alert important %}
Braze Cloud Data Ingestion support for S3 is currently in early access. Contact your Braze account manager if you are interested in participating in the early access. {% endalert %}


## Product setup - AWS

New Cloud Data Ingestion integrations require some setup in your AWS account. Follow these steps to set up the integration:


### Step 1: Create a source bucket
Create a general purpose S3 Bucket with default settings in your AWS account. 

Default settings are:
  - ACLs Disabled
  - Block all public access
  - Disable bucket versioning
  - SSE-S3 encryption

Take note of what region you’ve created the bucket in, as you will use the same region to create the SQS later on.


### Step 2: Create SQS resources
Create a new SQS queue in the same region you created the S3 bucket.  This queue will be used to track when objects are added to the bucket(s) you’ve created

The queue can be created with default configuration settings, until you reach the access policy step. When setting up the access policy, choose "Advanced" options. Append the following statement to the queue's access policy: 
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
1. Navigate to the bucket created in step 1 and 
2. Go to Properties -> Event notifications 
3. Give the configuration a name. Optionally, specify a prefix and/or suffix to target (if you only want a subset of files to be ingested by Braze)
4. Under destination pick SQS queue and provide the ARN of the SQS you created in Step 2

### Step 4: IAM Policy
Create an IAM policy to allow Braze to interact with your source bucket. To get started, sign in to the AWS management console as an account administrator. 

1. Navigate to the IAM section of the AWS Console, click **Policies** in the navigation bar, and click **Create Policy**.  

![]({{site.baseurl}}/assets/img/create_policy_1_list.png)

2. Open the **JSON** tab and input the following code snippet into the **Policy Document** section. Be sure to replace `YOUR-BUCKET-NAME-HERE` with your bucket name, and `YOUR-SQS-ARN-HERE` with your SQS queue name.  
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
3. Click **Review Policy** when you're finished.  

4. Give the policy a name and a description and click **Create Policy**.  

![]({{site.baseurl}}/assets/img/create_policy_3_name.png)

![]({{site.baseurl}}/assets/img/create_policy_4_created.png)

### Step 5: IAM Role
To complete the setup on AWS, you will create an IAM Role and attach the IAM Policy from Step 4 to it. 

1. Within the same IAM section of the console where you created the IAM policy, click **Roles > Create Role**.  

![]({{site.baseurl}}/assets/img/create_role_1_list.png)

2. Retrieve the Braze AWS account ID from your Braze dashboard: avigate to **Partner Integrations** > **Technology Partners** and click **Amazon S3**. Here you will find the Account ID needed to create your role.  

3. In AWS, select **Another AWS Account** as the trusted entity selector type. Provide your Braze account ID, check the **Require external ID** box, and enter an external ID for Braze to use. Click **Next** when complete.  

![The S3 "Create Role" page. This page has fields for role name, role description, trusted entities, policies, and permissions boundary.]({{site.baseurl}}/assets/img/create_role_2_another.png)

4. Attach the policy created in Step 4 to the role. Search for the policy in the search bar, and place a checkmark next to the policy to attach it. Click **Next** when complete.  

![Role ARN]({{site.baseurl}}/assets/img/create_role_3_attach.png)

Give the role a name and a description, and click **Create Role**.

![Role ARN]({{site.baseurl}}/assets/img/create_role_4_name.png)


5. Be sure to take note of the ARN of the Role you just created, and the external-id you generated as you’ll be using it to create the CDI Integration.  


## Product setup - Braze 

1. To create a new integration, navigate to Data Settings>Cloud Data Ingestion, click "Create New Data Sync", and select S3 Import from the file sources section.  
2. Input the information from the AWS setup process to create a new sync. You'll need to specify Role ARN, External ID, SQS URL, Bucket Name, Folder Path (optional), and Region. *The SQS URL must be unique for each new integration.*  
![]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_1.png %}) 
3. Give your integration a name, and select the data type for this integration. 
![]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_2.png %})  
4. Add a contact email for notifications if the sync breaks due to access or permissions issues. Optionally, turn on notifications for user-level errors and sync successes.  
![]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_3.png %})
5. Finally, test the connection and save the sync.  
![]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_4.png %})


