---
nav_title: Security events export with S3
article_title: Security Settings Export with S3
page_order: 1
page_type: reference
description: "This reference article covers how to automatically export security events every day at midnight UTC to Amazon S3."
---

# Security events export with Amazon S3

> You can automatically export Security Events to Amazon S3, a cloud storage provider, with a daily job that runs at midnight UTC. Once set up, you don't need to manually export Security Events from the dashboard. The job will export the security events for the past 24 hours in CSV format to your configured S3 storage. It will be in the same structure as the manual downloaded report.

Braze supports two different S3 authentication and authorization methods for setting up Amazon S3 export:

- AWS secret access key method
- AWS role ARN method

## AWS secret access key method

This method generates a secret key and an access key ID that allows Braze to authenticate as a user on your AWS account to write data to your bucket.

### Step 1: Create an in-app message user

To retrieve your secret access key and access key ID, you’ll need to create an in-app message user, following the instructions in [Setting up your AWS account](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started-account-iam.html#create-an-admin).

### Step 2: Get credentials

1. After creating a new user, generate the access key and download your access key ID and secret access key.

![A summary page for a role called "liyu-chen-test".]({% image_buster /assets/img/security_export/credentials1.png %})

{: start="2"}
2. Take note of these credentials somewhere or download the credential files, because you’ll need to input these into Braze later on.

![Fields containing the access key and secret access key.]({% image_buster /assets/img/security_export/retrieve_access_keys.png %})

### Step 3: Create policy

1. Go to **IAM** > **Policies** > **Create Policy** to add permissions for your user. 
2. Select **Create Your Own Policy**, which gives limited permissions so Braze can only access the specified buckets.
3. Specify a policy name of your choice.
4. Input the following code snippet into the **Policy Document** section. Be sure to replace "INSERTBUCKETNAME" with your bucket name. Without these permissions, the integration will fail a credentials check and not be created.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:GetBucketLocation"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME"]
        },
        {
            "Effect": "Allow",
            "Action": ["s3:GetObject", "s3:PutObject", "s3:DeleteObject"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME*", "arn:aws:s3:::INSERTBUCKETNAME/", "arn:aws:s3:::INSERTBUCKETNAME"]
        }
    ]
}
```

### Step 4: Attach policy

1. After creating a new policy, go to **Users** and select your specific user. 
2. In the **Permissions** tab, select **Add Permissions**, directly attach the policy, and then select that policy. 

Now, you’re ready to link your AWS credentials to your Braze account!

### Step 5: Link Braze to AWS

1. In Braze, go to **Settings** > **Company Settings** > **Admin Settings** > **Security Settings** and scroll to the **Security Event Download** section.
2. Toggle on **Export to AWS S3** under **Export to cloud storage** and select **AWS secret access key**, which enables the S3 export. 
3. Input the following:
- AWS access key ID
- AWS secret access key
    - When inputting this key, first select **Test Credentials** to confirm your credentials work.
- AWS bucket name 

![The "Security Event Download" page with populated Braze account and Braze external IDs.]({% image_buster /assets/img/security_export/security_event_download1.png %})

{: start="4"}
4. Select **Save Changes**. 

!["Save changes" button.]({% image_buster /assets/img/security_export/save_changes_button.png %}){: style="max-width:50%;"}

You’ve integrated AWS S3 into your Braze account!

## AWS role ARN method

The AWS role ARN method generates a role Amazon Resource Name (ARN) that allows the Braze Amazon account to authenticate as a member of that role.

### Step 1: Create policy

1. Sign in to the AWS management console as an account administrator. 
2. In the AWS console, go to the **IAM** section > **Policies**, and then select **Create Policy**.

![A page with a list of policies and button to "Create policy".]({% image_buster /assets/img/security_export/policies.png %})

{: start="3"}
3. Open the **JSON** tab and input the following code snippet into the **Policy Document** section. Be sure to replace `INSERTBUCKETNAME` with your bucket name. 

```json
  {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:GetBucketLocation"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME"]
        },
        {
            "Effect": "Allow",
            "Action": ["s3:PutObject", "s3:GetObject","s3:DeleteObject"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME/*"]
        }
    ]
}
```

{: start="4"}
4. Select **Next** after reviewing the policy.

![A page that allows you to review your policy and optionally add permissions.]({% image_buster /assets/img/security_export/specify_permissions.png %})

{: start="5"}
5. Give the policy a name and description, and then select **Create Policy**.

![A page to review and create your policy.]({% image_buster /assets/img/security_export/review_and_create.png %})

### Step 2: Create role

1. In Braze, go to **Settings** > **Company Settings** > **Admin Settings** > **Security Settings** and scroll to the **Security Event Download** section. 
2. Select **AWS Role ARN**. 
3. Take note of the identifiers, Braze account ID, and Braze external ID needed to create your role.

![The "Security Event Download" page with populated Braze account and Braze external IDs.]({% image_buster /assets/img/security_export/security_event_download2.png %})

4. In the AWS console, go to the **IAM** section > **Roles** > **Create Role**. 
5. Select **Another AWS Account** as the trusted entity selector type. 
6. Provide your Braze account ID, check the **Require external ID** box, and then enter your Braze external ID. 
7. Select **Next** when complete.

![A page with options to select a trusted entity type and provide information about your AWS account.]({% image_buster /assets/img/security_export/select_trusted_entity.png %})

### Step 3: Attach policy

1. Search for the policy you created earlier in the search bar, and then place a checkmark next to the policy to attach it. 
2. Select **Next**.

![A list of policies with columns for their type and description.]({% image_buster /assets/img/security_export/add_permissions.png %})

{: start="3"}
3. Give the role a name and a description, and select **Create Role**.

![Fields to provide role details, such as the name, description, trust policy, permissions, and tags.]({% image_buster /assets/img/security_export/name_review_create.png %})

Your newly created role will appear in the list!

### Step 4: Link to Braze AWS

1. In the AWS Console, find your newly created role in the list. Select the name to open up the details of that role, and take note of the **ARN**.

![The summary page for a role called "security-event-export-olaf".]({% image_buster /assets/img/security_export/credentials2.png %})

{: start="2"}
2. In Braze, go to **Settings** > **Company Settings** > **Admin Settings** > **Security Settings** and scroll to the **Security Event Download** section.

!["Security Event Download" section with a toggle turned on for "Export to AWS S3".]({% image_buster /assets/img/security_export/security_event_download3.png %})

{: start="3"}
3. Make sure **AWS role ARN** is selected, then input your role ARN and AWS S3 bucket name in the designated fields. 
4. Select **Test Credentials** to confirm your credentials work properly.
5. Select **Save Changes**. 

!["Save changes" button.]({% image_buster /assets/img/security_export/save_changes_button.png %}){: style="max-width:40%;"}

You’ve integrated AWS S3 into your Braze account!