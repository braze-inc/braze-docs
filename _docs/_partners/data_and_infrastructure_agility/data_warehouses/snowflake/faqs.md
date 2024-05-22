---
nav_title: FAQ
article_title: Snowflake Data Sharing FAQ
page_order: 3
page_type: FAQ
description: "This article covers some frequently asked questions for Snowflake Data Sharing"

---

# Frequently Asked Questions

### Is it possible to obfuscate PII data via snowflake data sharing?
It is not supported as of now.

### Do I need same region data share or cross region share?
You would use same region data sharing under the following scenario:
- Your Snowflake account is in US-EAST-1 (AWS) and your braze dashboard region is in US.
- Or your Snowflake region is in EU-CENTRAL-1 and your braze dashboard region is in EU.
Otherwise cross region data sharing should be purchased. 

### What to do with my data share when I'm switching to a new snowflake account?
You can simply delete the old data share associated with your old Snowflake account, and create a new share for the new account. All historical data should be available in the recreated share. 

### I'm not seeing data in my data share.
One common issue is having the wrong Snowflake account ID when creating the data share. The Account ID on the data sharing dashboard must match the output of CURRENT_ACCOUNT() from your Snowflake account.

If it’s a cross region data share, data might not be immediately available. Depending on the your data volume it could take a few hours for data to get synced to your region.


