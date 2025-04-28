---
nav_title: Kubit
article_title: Kubit
description: "This reference article outlines the partnership between Braze and Kubit, a no-code, self-service analytics platform that delivers instant product insights, allowing you to import Kubit user cohorts and target them in the Braze messaging."
alias: /partners/kubit/
page_type: partner
search_tag: Partner

---

# Kubit

> [Kubit](https://kubit.ai/) is a no-code, self-service analytics platform that delivers instant product insights. 

The Braze and Kubit integration allows you to [import Kubit user cohorts]({{site.baseurl}}/partners/data_and_analytics/cohort_import/kubit/) and target them in the Braze messaging. In addition, through the use of [Snowflake secure data sharing]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/), you can integrate the raw campaign and impression data from Braze with Kubit product analytics to measure the impact of these campaigns in real-time. This approach provides insights into the full lifecycle of your users without requiring any engineering efforts.

## Prerequisites

| Requirement | Description |
|---|---|
|Kubit enterprise account | A Kubit enterprise account is required to take advantage of this partnership. |
| Matching user IDs | Your customer data in Kubit and Braze must have matching user IDs across the two platforms. This also includes anonymous UUIDs. Visit our [documentation]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/?tab=android) to read about how Braze sets user IDs. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" } 

## Analyzing Braze data in Kubit

Take advantage of [Snowflake secure data sharing]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/) to share your Braze raw campaign and impression data with Kubit to incorporate them into Kubit's self-service analytics, providing you a full picture of users' lifecycle.

For reference, here are all the [Braze fields]({{site.baseurl}}/assets/download_file/data-sharing-raw-table-schemas.txt?ed79384e6ac6a97fe3b3d9f76852b7c2) which are available to be incorporated into Kubit analytics. The details of this step are very customer-specific and require special configurations. Talk to your Kubit account manager or [support@kubit.ai](support@kubit.ai) to learn more.