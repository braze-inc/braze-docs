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
- Your Snowflake region is in AP-Southeast-2 (AWS) and your Braze dashboard region is in Australia.
- Your Snowflake region is in AP-Southeast-3 (AWS) and your Braze dashboard region is in Indonesia.

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

### How many times do I need to run `CREATE DATABASE` when I have multiple workspaces sharing data to the same Snowflake account?

You need to run `CREATE DATABASE <name> FROM SHARE <provider_account>.<share_name>` only once. When multiple data shares from different Braze workspaces are shared to the same Snowflake account, they are automatically combined into the same share. After you create the initial database, data from additional workspaces is automatically added to the existing database without requiring additional share requests or database creation steps.

For example, if you create a data share to Snowflake Account 123 from Workspace A, you accept the share request and create a database. When you later create a data share to the same Snowflake Account 123 from Workspace B, no new share request is sent—the data is immediately added to the existing share and becomes available in the previously created database.

### If I have multiple workspaces, does a single database contain data from all of them?

Yes. When you share data from multiple Braze workspaces to the same Snowflake account, all data is combined into a single share and available in the same database. You can filter the data by `app_group_id` to distinguish between workspaces.

As a best practice, always filter by `app_group_id` in your queries to future-proof them. This ensures your dashboards and reports remain accurate if you add additional workspaces in the future. Without this filter, your metrics may unexpectedly include data from newly added workspaces.

### What is the recommended approach for managing data from multiple workspaces in Snowflake?

Send all Braze data into the same database and filter by `app_group_id` to distinguish between workspaces. This approach simplifies data management and ensures consistent reporting across your organization.

### How many Snowflake Data Share Connectors do I need for multiple workspaces?

The number of Connectors you need depends on your specific configuration and entitlements. Contact your Braze account team to learn more about which entitlements are right for your use case.


