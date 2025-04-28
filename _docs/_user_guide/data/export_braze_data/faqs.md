---
nav_title: FAQ
article_title: Export FAQ
page_order: 11
page_type: FAQ
description: "This article covers some frequently asked questions for API and CSV exports."

---

# Frequently asked questions

> This page provides answers to some commonly asked questions about API and CSV exports.

### Can you make certain exports appear in your S3 bucket and others not?

No. If you have provided S3 credentials, all your exports will appear in your S3 bucket; otherwise, if no credentials are provided, all exports will appear in an S3 bucket belonging to Braze.

### Do I have to add S3 credentials to Braze to export data?

No. If you don't add S3 credentials, your exports will appear in an S3 bucket belonging to Braze.

### What happens if you set up S3 credentials in the dashboard but don't select "Make this the default data export destination?"

The **Make this the default data export destination** checkbox impacts whether exports go to S3 or Azure, assuming you've added credentials for both.

### Why did I receive multiple files when exporting user profiles to S3?

This is expected behavior for workspaces with a lot of users. Braze will split your export into multiple files based on the number of users in your workspace. Generally, there is one file output per 5,000 users. Note that if you are exporting a small segment within a large workspace, you may still receive multiple files.

### Why do I see duplicates when I export users by segment through REST API?

This is a very rare occurrence caused by the underlying architecture of the database provider. Duplicates are cleaned out every week; however, most weeks, no duplicates are cleared.
