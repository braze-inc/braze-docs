---
nav_title: Amazon S3
alias: /partners/amazon_s3/
page_order: 1
---

# Amazon S3 Integration

Follow the instructions on this page to get started with your AWS S3 integration. AWS S3 integration is required for advanced data export functionality.

If you're looking for information on the Currents integration with AWS S3, [click here]({{ site.baseurl }}/partners/technology_partners/data_and_infrastructure_agility/data_warehouses/amazon_s3_for_currents/).

## Obtaining Amazon S3 Credentials

If you already have an S3 bucket, we still recommend creating a new bucket for Braze so you can limit permissions.

#### Step 1 {#S3-1}

To create a bucket for your app, open the [Amazon S3 console][6] and follow the instructions to Sign in or Create an Account with AWS.

#### Step 2 {#S3-2}

Once signed in, select 'S3' from the 'Storage & Content Delivery' Category.

![S3 Creds][7]

#### Step 3 {#S3-3}

Select 'Create Bucket' on the next screen and you'll be prompted to create your bucket and select a region. [Click here][8] for information on Bucket Restrictions and Limitations, as well as naming conventions.

![Create Bucket][9]

#### Step 4 {#S3-4}

To retrieve your access ID and secret access key, you'll need to create your first IAM User and Administrators Group. Follow these [step-by-step instructions][10].

#### Step 5 {#S3-5}

Once a user has been created, please select 'Show User Security Credentials' so your Access Key ID and Secret Access Key will be revealed. Click the blue 'Download Credentials' button as you will need to input this into the Braze dashboard later on.

![Secret Key][11]

#### Step 6 {#S3-6}

Now, you'll need to navigate to the Policies tab in the navigation bar and select 'Get Started' then 'Create Policy' which will allow you to add permissions for your user. Select 'Create Your Own Policy'. This will give limited permissions so we only have the ability to access the bucket that you specify.

![Policy][12]

Below is the code you need to input when creating your own policy. You will have to specify a 'Policy Name' of your choice, and input the code below into the 'Policy Document' section. Be sure to replace 'INSERTBUCKETNAME' with your own bucket name.

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

#### Step 7 {#S3-7}

Once your policy has been created, you will need to select 'Users' and then click into your specifc user so you can attach this new policy. On the 'Permissions' tab, click 'Attach Policy'.

![Attach User][13]

Search for the new policy that you created and click to attach.

You are now ready to link your AWS credentials to your Braze account.

## Linking Braze to Amazon S3

#### Step 1 {#aws-1}

Navigate to the 'Technology Partners' page on the Braze Dashboard under the 'Integrations' section and click on 'Amazon S3'.

![AWS Creds][5]

#### Step 2 {#aws-2}

On the AWS Credentials page, input your AWS Access ID, AWS Secret Access Key, and AWS S3 Bucket Name in the designated fields. When inputting your secret key, click 'Test Credentials' first to ensure your credentials work, then 'Save' once this is successful.

> You can always retrieve new credentials by navigating to your user and clicking 'Create Access Key' on the Security Credentials Tab within the AWS Console.

## Integration Complete {#aws-3}

AWS S3 should now be integrated into your Braze account. A notification will inform you if your credentials have been successfully validated.

[3]: http://aws.amazon.com/
[4]: http://aws.amazon.com/

[5]: {% image_buster /assets/img/s3_tech_partners.png %} "AWS Creds"
[6]: https://console.aws.amazon.com/s3/
[7]: {% image_buster /assets/img_archive/S3_Category.png %}
[8]: https://docs.aws.amazon.com/AmazonS3/latest/dev/BucketRestrictions.html
[9]: {% image_buster /assets/img_archive/S3_CreateBucket.png %}
[10]: https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html
[11]: {% image_buster /assets/img_archive/S3_Credentials.png %}
[12]: {% image_buster /assets/img_archive/S3_CreatePolicy.png %}
[13]: {% image_buster /assets/img_archive/S3_AttachPolicy.png %}
[14]: {{ site.baseurl }}/developer_guide/platform_wide/app_group_configuration/#app-group-configuration
[15]: {{ site.baseurl }}/partners/technology_partners/data_and_infrastructure_agility/customer_data_platform/segment_integration/#getting-started
