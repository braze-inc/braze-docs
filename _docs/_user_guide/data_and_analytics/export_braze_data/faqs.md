---
nav_title: FAQs
article_title: Export FAQs
page_order: 11
page_type: FAQ
description: "This  article covers some frequently asked questions for API and CSV exports."

---

# Export faqs

> This page provides answers to some commonly asked questions about API and CSV exports.

### Can you make certain exports appear in a customer’s s3 bucket, and certain exports not?

No. If you have provided S3 credentials, all your exports will appear in your S3 bucket; otherwise, if no credentials are provided, all exports will appear in an S3 bucket belonging to Braze.

### Do i have to add s3 credentials to braze to export data?

No. Customers who do not add S3 credentials will have all of their exports appear in an S3 bucket belonging to Braze.

### What happens if you set up s3 credentials in the dashboard, but don't check “make this the default data export destination?”

That checkbox will impact whether exports go to S3 or Azure, assuming you've added credentials for both.

### Why did i receive multiple files when exporting user profiles to s3?

This is expected behavior for app groups with a lot of users. We split your export into multiple files, based on the number of users in your app group. Generally, there is one file output per 5,000 users. Note that if you are exporting a small segment within a large app group, you may still receive multiple files.

### Why do i see duplicates when i export users by segment via rest api?

This is a very rare edge case caused by the underlying architecture of the database provider. Duplicates are cleaned out every week; however, most weeks, there are no duplicates cleared.
