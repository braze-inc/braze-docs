---
nav_title: Amazon S3 for Currents
page_order: 1
alias: /partners/amazon_s3_for_currents/
---

# Amazon S3

[Amazon S3](https://aws.amazon.com/s3/) is a highly scalable storage system offered by Amazon Web Services. After transporting data into S3, you can use ETL processes (Extract, Transform, Load) to transfer your data to other locations.

If you're looking for information on the API integration with AWS S3, [click here]({{ site.baseurl }}/partners/technology_partners/data_and_infrastructure_agility/data_warehouses/amazon_s3/).

To get started, create a new S3 bucket for this integration. Then, create an IAM user in your AWS account that has the `s3:PutObject`, `s3:GetBucketLocation` and `s3:ListObject` permissions for the new S3 bucket. Gather the following information from the bucket and IAM user:

-   Access Key ID for user
-   Secret Access Key for user
-   Bucket Name

You can also add the following customizations, based on your needs:

-   Folder Path (defaults to `currents`)
-   AES-256 Encryption (defaults to OFF)

Add this information to the Amazon S3 Currents page on the dashboard, and press save.

![S3]({% image_buster /assets/img_archive/currents-s3-edit.png %})
