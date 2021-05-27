---
nav_title: FAQs
title: Export FAQs
page_order: 11

page_type: FAQ
description: "This  article covers some frequently asked questions for API and CSV exports."
---

# Export FAQs

> This page provides answers to some commonly asked questions about API and CSV exports.

### Can you make certain exports appear in a customer’s S3 bucket, and certain exports not?

No. If you have provided S3 credentials, all your exports will appear in your S3 bucket; otherwise, if no credentials are provided, all exports will appear in an S3 bucket belonging to Braze.

### Do I have to add S3 credentials to Braze to export data?

No. Customers who do not add S3 credentials will have all of their exports appear in an S3 bucket belonging to Braze.

### What happens if you set up S3 credentials in the dashboard, but don't check “make this the default data export destination?”

That checkbox will impact whether exports go to S3 or Azure, assuming you've added credentials for both.

### Why did I receive multiple files when exporting user profiles to S3?

This is expected behavior for app groups with a lot of users. We split your export into multiple files, based on the number of users in your app group. Generally, there is one file output per 5,000 users. Note that if you are exporting a small segment within a large app group, you may still receive multiple files.

### Why do I see duplicates when I export users by segment via REST API?

This is a very rare edge case caused by the underlying architecture of the database provider. Duplicates are cleaned out every week; however, most weeks, there are no duplicates cleared.
