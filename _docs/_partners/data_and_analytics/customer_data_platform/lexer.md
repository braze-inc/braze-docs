---
nav_title: Lexer
article_title: Lexer
description: "This reference article outlines the partnership between Braze and Lexer, a customer data platform that puts customer data in the hands of marketers to inspire experiences that drive sales."
alias: /partners/lexer/
page_type: partner
search_tag: Partner
---

# Lexer

> [Lexer](https://lexer.io/), a customer data platform built for retail, helps brands drive incremental sales through improved customer experiences combining robust data enrichment with the most intuitive tools and expert advisory.

_This integration is maintained by Lexer._

## About the integration

The Braze and Lexer integration allows you to sync data across the two platforms. Use your Lexer data to create valuable Braze segments or import your existing ones to Lexer to unlock insights. 

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Partner account | A Lexer account is required to take advantage of this partnership. |
| Braze REST API key | A Braze REST API key with all `user` permissions (excluding `user.delete`) and `segment.list` permissions. The permission set may change as Lexer adds support for more Braze objects, so you may either want to grant more permissions now or plan to update these permissions in the future.<br><br> This can be created in the Braze dashboard from **Settings** > **API Keys**. |
| Braze REST endpoint | Your [REST endpoint URL]({{site.baseurl}}/api/basics/#endpoints). Your endpoint will depend on the Braze URL for your instance. |
| Amazon AWS S3 bucket and credentials | Before beginning the integration, you must have access credentials for an AWS S3 bucket connected to your Lexer hub (this may be a bucket you create or one that Lexer creates and manages for you). Visit [Lexer](https://learn.lexer.io/docs/amazon-s3) for guidance on this requirement. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

In Lexer, navigate to **Manage > Integration**, select the **Braze** tile, and click **Integrate Braze**. Provide the following information:
- **Braze REST endpoint**
- **Braze REST API key**
- **AWS Credentials**
  - **AWS S3 bucket name**
  - **AWS S3 [bucket region](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingBucket.html)**
  - **AWS S3 bucket path**: This path should match the path you specified when [connecting your S3 bucket to Braze]({{site.baseurl}}/partners/data_and_infrastructure_agility/cloud_storage/amazon_s3/). This should be blank if you did not specify anything to Braze.
  - **AWS S3 secret access key**: Visit Amazon for information on [creating an access key](https://aws.amazon.com/premiumsupport/knowledge-center/create-access-key/).
- **Braze export segment ID**: The ID for the segment you have created in Braze containing all users you wish to export to Lexer. If there are users you do not want to export to Lexer, you may exclude them from the segment you created in Braze. To find your segment identifier, click into your desired segment in Braze and locate the **Segment API Identifier**.

![]({% image_buster /assets/img/lexer/braze_integrate_screen.png %})

### Choosing an AWS S3 option (Lexer-managed or self-managed)
Using a Lexer-managed bucket is the preferred way of connecting Braze to your Lexer hub and will reduce the amount of setup needed. Lexer will provide the one-off details you will need to configure Braze.

If you have already connected an S3 bucket to Braze and are using it for other purposes, you will need to instead provide Lexer access to this self-managed bucket by following the preceding steps.

This integration works by providing Lexer with your existing API token and secrets, allowing Lexer to make these exports on your behalf. It also imports your Braze data into Lexer using these credentials and your S3 configuration to sync your data on both platforms automatically.

## Sending segments to Braze

### Step 1: Create activation

Lexer Activate will automatically update your Braze profiles, adding or removing attributes as customers enter and leave your segment.

1. In Lexer, in **Lexer Activations**, click **ACTIVATE NEW AUDIENCE**.
2. Select the appropriate Braze activation for this campaign.
3. Add your segment.
4. Update your audience name; this will become your attribute value in Braze.
5. This is the custom attribute we'll be updating in Braze. Contact [Lexer support](support@lexer.io) to update.
6. Check the appropriate list action—in most cases, you'll want to maintain your list.
7. Review the terms and conditions, and click **SEND AUDIENCE**.

![]({% image_buster /assets/img/lexer/lexer.png %})

### Step 2: Verify activation

Once your activation has been confirmed as sent in Activate, you will see records begin to update in Braze. Your profiles won't be fully updated in Braze until after receiving a confirmation email from Lexer.

### Step 3: Create your Braze segment

In Braze, you will see your audience name in Lexer is now a value in your `lexer_audience` custom attribute. Braze has a limit of 100 values per attribute.

To create your segment, navigate to **Segment > + Create Segment** and select **Custom Attribute** as the filter. Next, select `lexer_audience` as your attribute and your desired Lexer audience name. When completed, **Save** your audience.

You can now add this newly created segment to future Braze campaigns and Canvases to target these end-users.


