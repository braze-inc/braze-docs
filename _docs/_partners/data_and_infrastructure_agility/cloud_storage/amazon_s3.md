---
nav_title: Amazon S3
article_title: Amazon S3
alias: /partners/amazon_s3/
page_order: 1
description: "This article outlines the partnership between Braze and Amazon S3, a highly scalable storage system offered by Amazon Web Services."
page_type: partner
search_tag: Partner

---

# Amazon S3 Integration

> [Amazon S3](https://aws.amazon.com/s3/) is a highly scalable storage system offered by Amazon Web Services.

Braze has two different integration strategies with Amazon S3 - one for [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/) and one for all Dashboard data exports (CSV exports, Engagement Reports, etc.) Both integrations support two different authentication/authorization methods:

-   [AWS Secret Access Key method](#aws-secret-key-auth-method)
-   [AWS Role ARN method](#aws-role-arn-auth-method)

Follow the instructions on this page to get started with your AWS S3 integration. If you already have an S3 bucket, we still recommend creating a new bucket **specifically for Braze** so you can limit permissions.

1.  To create a bucket for your app, open the [Amazon S3 console](https://console.aws.amazon.com/s3/) and follow the instructions to **Sign in** or **Create an Account with AWS**.
2.  Once signed in, select "S3" from the "Storage & Content Delivery" category.
3.  Select "Create Bucket" on the next screen and you"ll be prompted to create your bucket and select a region.

## AWS Secret Key Auth Method

This authentication method generates a **Secret Key** and an **Access Key ID** that enables Braze to authenticate as a user on your AWS account for the purposes of writing data to your bucket.

### Step 1 - Create User {#secret-key-1}

To retrieve your **Access Key ID** and **Secret Access Key**, you’ll need to [create an **IAM User** and **Administrators Group** in AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html).

### Step 2 - Get Credentials {#secret-key-2}

Once a user has been created, click "Show User Security Credentials" so your **Access Key ID** and **Secret Access Key** will be revealed. Next, either note these credentials somewhere or click the blue "Download Credentials" button as you will need to input these into the Braze dashboard later on.

![Secret Key][11]

### Step 3 - Create Policy {#secret-key-3}

Now, navigate to the **Policies** tab in the navigation bar and select "Get Started" then "Create Policy". This will allow you to add permissions for your user. Select "Create Your Own Policy". This will give limited permissions so we only have the ability to access the bucket that you specify.

![Policy][12]

Input the code below when creating your own policy. (Note that there are different policies required for "Currents" vs. "Dashboard Data Export".) Specify a "Policy Name" of your choice, and input the code below into the "Policy Document" section. Be sure to replace `INSERTBUCKETNAME` with your own bucket name.

{% tabs %}
{% tab Braze Currents %}

```json
{
  "Version": "2012-10-17",
  "Statement": [
    { "Effect": "Allow",
      "Action": ["s3:GetBucketLocation"],
      "Resource": ["arn:aws:s3:::INSERTBUCKETNAME"]
    }
    ,
    { "Effect": "Allow",
      "Action": ["s3:PutObject", "s3:ListBucket"],
      "Resource": ["arn:aws:s3:::INSERTBUCKETNAME*", "arn:aws:s3:::INSERTBUCKETNAME/", "arn:aws:s3:::INSERTBUCKETNAME"]
    }
  ]
}
```

{% endtab %}
{% tab Dashboard Data Export %}

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

{% endtab %}
{% endtabs %}

### Step 4 - Attach Policy {#secret-key-4}

Once your policy has been created, navigate to "Users" and then click into your specific user so you can attach this new policy. On the "Permissions" tab, click "Attach Policy".

![Attach User][13]

Search for the new policy that you created and click to attach.

You are now ready to link your AWS credentials to your Braze account.

### Step 5 - Link Braze to AWS {#secret-key-5}

{% tabs %}
{% tab Braze Currents %}

Navigate to the "Currents" page on the Braze Dashboard under the "Integrations" section, click the "Create Current" dropdown, and select "Amazon S3 Data Export".

![AWS Creds]({{site.baseurl}}/assets/img/currents-s3-example.png)

Give your Current a name. Then, in the **Credentials** section, make sure the "AWS Secret Access Key" radio button is selected, then input your **AWS Access ID**, **AWS Secret Access Key**, and **AWS S3 Bucket Name** in the designated fields.

{% alert warning %}
Keep your AWS Access Key ID and AWS Secret Access Key up to date. If your connector's credentials expire, the connector will stop sending events. If this persists for more than **48 hours**, the connector's events will be dropped and data will be permanently lost.
{% endalert %}

You can also add the following customizations, based on your needs:

-   Folder Path (defaults to `currents`) 
-   Server-Side, At-Rest AES-256 Encryption (defaults to OFF) - Includes the "x-amz-server-side-encryption" header

Click "Launch Current" to continue.

A notification will inform you whether your credentials have been successfully validated. AWS S3 should now be set up for Braze Currents.

{% endtab %}
{% tab Dashboard Data Export %}

Navigate to the "Technology Partners" page on the Braze Dashboard under the "Integrations" section and click on "Amazon S3".

![AWS Creds]({{site.baseurl}}/assets/img/s3_tech_partners.png)

On the AWS Credentials page, make sure the "AWS Secret Access Key" radio button is selected, then input your AWS Access ID, AWS Secret Access Key, and AWS S3 Bucket Name in the designated fields. When inputting your secret key, click "Test Credentials" first to ensure your credentials work, then "Save" once this is successful.

{% alert tip %}
You can always retrieve new credentials by navigating to your user and clicking "Create Access Key" on the Security Credentials tab within the AWS Console.
{% endalert %}

A notification will inform you whether your credentials have been successfully validated. AWS S3 should now be integrated into your Braze account.

{% endtab %}
{% endtabs %}

## AWS Role ARN Auth Method

This authentication method generates a Role ARN (Amazon Resource Name) that enables Braze's Amazon account to authenticate as a member of the Role you created for the purposes of writing data to your bucket.

### Step 1 - Create Policy {#role-arn-1}

To get started, sign in to the AWS Management Console as an administrator of the account. Navigate to the IAM section of the AWS Console, click "Policies" in the navigation bar, and click "Create Policy".

![Role ARN]({{site.baseurl}}/assets/img/create_policy_1_list.png)

Open the "JSON" tab and input the code below into the “Policy Document” section. Be sure to replace INSERTBUCKETNAME with your own bucket name. Click "Review Policy" when you're finished.

{% tabs %}
{% tab Braze Currents %}

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
            "Action": ["s3:PutObject", "s3:GetObject"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME/*"]
        }
    ]
}
```

{% endtab %}
{% tab Dashboard Data Export %}

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
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME/*"]
        }
    ]
}
```

{% endtab %}
{% endtabs %}

Next, give the policy a name and a description and click "Create Policy".

![Role ARN]({{site.baseurl}}/assets/img/create_policy_3_name.png)

![Role ARN]({{site.baseurl}}/assets/img/create_policy_4_created.png)

### Step 2 - Create Role {#role-arn-2}

Now, still within the IAM section of the AWS Console, click "Roles" in the navigation bar and click "Create Role".

![Role ARN]({{site.baseurl}}/assets/img/create_role_1_list.png)

Retrieve your **Braze Account ID** and **External ID** from your Braze account.

{% tabs %}
{% tab Braze Currents %}

Navigate to the "Currents" page in your Braze account under the "Integrations" section, click the "Create Current" dropdown, and select "Amazon S3 Data Export".

![AWS Creds]({{site.baseurl}}/assets/img/currents-role-arn.png)

{% endtab %}
{% tab Dashboard Data Export %}

Navigate to the "Technology Partners" page in your Braze account under the "Integrations" section and click on "Amazon S3".

![AWS Creds]({{site.baseurl}}/assets/img/data-export-role-arn.png)

{% endtab %}
{% endtabs %}

Back on the AWS Console, select "Another AWS Account" from the type of trusted entity selector. Enter the **Braze Account ID**, check "Require external ID", and enter the **Braze External ID**. Click "Next" when complete.

![Role ARN]({{site.baseurl}}/assets/img/create_role_2_another.png)

### Step 3 - Attach Policy {#role-arn-3}

Next, attach the Policy you created earlier to the Role. Search for the policy in the search bar, and place a checkmark next to the policy to attach it. Click "Next" when complete.

![Role ARN]({{site.baseurl}}/assets/img/create_role_3_attach.png)

Give the Role a name and a description, and click "Create Role".

![Role ARN]({{site.baseurl}}/assets/img/create_role_4_name.png)

You should now see your newly created Role on the list.

### Step 4 - Link to Braze AWS {#role-arn-4}

Still on the AWS Console, find your newly created Role in the list. Click the name to open up the details of that Role.

![Role ARN]({{site.baseurl}}/assets/img/create_role_5_created.png)

Take note of the "Role ARN" at the top of the summary (click the icon to copy to the clipboard.)

![Role ARN]({{site.baseurl}}/assets/img/create_role_6_summary.png)

Return to your Braze account and copy the Role ARN into the field provided.

{% tabs %}
{% tab Braze Currents %}

Navigate to the "Currents" page in your Braze account under the "Integrations" section, click the "Create Current" dropdown, and select "Amazon S3 Data Export".

![AWS Creds]({{site.baseurl}}/assets/img/currents-role-arn.png)

Give your Current a name. Then, in the Credentials section, make sure the "AWS Role ARN" radio button is selected, then input your Role ARN, and AWS S3 Bucket Name in the designated fields.

You can also add the following customizations, based on your needs:

-   Folder Path (defaults to `currents`)
-   Server-Side, At-Rest AES-256 Encryption (defaults to OFF) - Includes the "x-amz-server-side-encryption" header

Click "Launch Current" to continue.

A notification will inform you whether your credentials have been successfully validated. AWS S3 should now be set up for Braze Currents.

{% alert important %}
If you receive a “S3 credentials are invalid” error, this may be due to integrating too quickly after creating a role in AWS. Please wait and try again. 
{% endalert %}

{% endtab %}
{% tab Dashboard Data Export %}

Navigate to the "Technology Partners" page in your Braze account under the "Integrations" section and click on "Amazon S3".

![AWS Creds]({{site.baseurl}}/assets/img/data-export-role-arn.png)

On the **AWS Credentials** page, make sure the "AWS Role ARN" radio button is selected, then input your Role ARN, and **AWS S3 Bucket Name** in the designated fields. Click "Test Credentials" first to ensure your credentials work properly, then "Save" once this is successful.

{% alert tip %}
You can always retrieve new credentials by navigating to your user and clicking "Create Access Key" on the Security Credentials tab within the AWS Console.
{% endalert %}

A notification will inform you whether your credentials have been successfully validated. AWS S3 should now be integrated into your Braze account.

{% endtab %}
{% endtabs %}


[11]: {% image_buster /assets/img_archive/S3_Credentials.png %}
[12]: {% image_buster /assets/img_archive/S3_CreatePolicy.png %}
[13]: {% image_buster /assets/img_archive/S3_AttachPolicy.png %}
