---
nav_title: Lexer
article_title: Lexer
page_order: 1

description: "Lexer and Braze put customer data in the hands of marketers to inspire the experiences that drive sales."
alias: /partners/lexer/

page_type: partner
search_tag: Partner
hidden: true
---

# Lexer

> Built for retail from the beginning, we know that the fastest path to customer centricity is making data accessible to all teams. So we combine powerful data enrichment with the most intuitive tools and expert advisory, making understanding and delighting your customers at every interaction a reality today. www.lexer.io

Lexer and Braze are changing retail by unlocking one of the most vital business assets: customer data. Together helping marketers know their customers, inspiring them to create the experiences that grow sales.

Lexer's segmentation, insights and audience activation and measurement capabilities streamline and optimise Braze’s orchestration and automation capabilities.


## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Partner account | A Lexer account is required to take advantage of this partnership. |
| Braze REST API key | "A Braze REST API Key with users.track permissions (except for user.delete) and segment.list permissions.The permission set may change as Lexer adds support for more Braze objects, so you may either want to grant more permissions now or plan to update these permissions in the future. This can be created within the Braze Dashboard -> Developer Console -> REST API Key -> Create New API Key" |
| Braze REST endpoint | [Your REST Endpoint URL][1]. Your endpoint will depend on the Braze URL for your instance. |
| Amazon AWS S3 Bucket and credentials | Before beginning the integration, you must have access credentials for an AWS S3 bucket connected to your Lexer hub (this may be a bucket you create, or one that Lexer creates and manages for you). Visit Lexer documentation <link to our s3 help article> for guidance on this requirement. |
{: .reset-td-br-1 .reset-td-br-2}

## Use cases

Use a persistently maintained operation single view of customer to deliver personalisation across all your consumer touchpoint including email, SMS, in-App and on domain.

## Integration

Select the Braze tile, and click **Integrate Braze**, then enter all the requested details and hit **Save Integration**.

![Integrating Braze in Lexer][1]

### What do I need to provide?
1. Your braze API key and URL
    - For information on how to obtain your API key and URL, read [here][2]
2. Your AWS S3 Bucket credentials and details
    - You won't need to provide this info if using a Lexer-managed s3 bucket
    - For more info on creating the access key credentials, read [here][3]
    - Learn more about AWS S3 bucket regions [here][4]
    - The path should match the path you specified when [connecting your S3 bucket to Braze][5] (this can be blank if you did not specify anything in Braze)
3. The ID of the segment you have created in Braze containing all users you wish to export to Lexer
    - More info on working with Braze segments can be found below, and the segment ID may be found via the tab for segment editing on Braze
    - The segment you specify lets Lexer know which users to export - if there are users you do not wish to export to Lexer, you may choose to exclude them from the segment you created in Braze

### Choosing which AWS S3 option to go with - Lexer-managed vs self-managed
Using a Lexer-managed bucket is the preferred way of connecting Braze to your Lexer hub, and will reduce the amount of set-up required by you! We'll provide the details you'll need to provide in Braze in the once-off configuration to be made. 

If you have already connected an S3 bucket to Braze and are using it for other purposes, then you will need to instead provide Lexer access to this self-managed bucket by following the steps above.

This integration works by providing Lexer with your existing API token and secrets, and allowing Lexer to make these exports on your behalf. It also imports your Braze data into Lexer using these credentials and your s3 configuration, so that your data on both platforms is automatically kept synchronised.

[1]: {% image_buster /assets/img/lexer/braze_integrate_screen.png %}
[2]: https://www.braze.com/docs/api/basics/#company-secret-explanation
[3]: https://aws.amazon.com/premiumsupport/knowledge-center/create-access-key/
[4]: https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingBucket.html
[5]: https://www.braze.com/docs/partners/data_and_infrastructure_agility/cloud_storage/amazon_s3/
