---
nav_title: FAQs
article_title: Snowflake Data Sharing FAQs
page_order: 50
page_type: FAQ
description: "This article answers frequently asked questions about Snowflake data sharing."

---

# Frequently asked questions

### Is it possible to obfuscate PII data via Snowflake data sharing?
No, as of now that is not supported.

### Do I need data share for the same region or cross region?
Use data sharing for the same region in the following scenarios:
- Your Snowflake account is in US-EAST-1 (AWS) and your Braze dashboard region is in the US.
- Your Snowflake region is in EU-CENTRAL-1 and your Braze dashboard region is in the EU.

Otherwise, use data sharing for cross region. 

### What should I do with my data share when I switch to a new Snowflake account?
You can delete the old data share associated with your old Snowflake account and then create a new share for the new account. All historical data will be available in the new share. 

### Why don't I see data in my data share?
You might have used the wrong Snowflake account ID when creating your data share. The account ID on the data sharing dashboard must match the output of `CURRENT_ACCOUNT()` from your Snowflake account.

If your share is cross region, the data might not be immediately available. Depending on your data volume, it could take a few hours for data to sync to your region.

### Why am I receiving a HIPAA compliance error when creating a data share?

The specified account is either not HIPAA-compliant or on [Snowflake Editions](https://docs.snowflake.com/en/user-guide/intro-editions) lower than Business Critical. Your Snowflake account must be upgraded to the Business Critical Edition to be HIPAA-compliant for data sharing. Contact Snowflake support for further assistance with upgrading your account.

### Why can't I recreate a data share after deleting one?

The system may still be processing the deletion of your previous data share. Wait a few minutes for the deprovisioning process to complete, then try creating the new data share again.


