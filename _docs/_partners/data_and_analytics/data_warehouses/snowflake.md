---
nav_title: Snowflake
article_title: Snowflake
alias: /partners/snowflake/
description: "This article outlines the partnership between Braze and Snowflake, covering both Data Sharing (Braze to Snowflake) and Cloud Data Ingestion (Snowflake to Braze)."
page_type: partner
search_tag: Partner

---

# Snowflake

> [Snowflake](https://docs.snowflake.net/manuals/user-guide/intro-key-concepts.html) is a purpose-built SQL cloud data warehouse provided as Software-as-a-Service (SaaS). Snowflake provides a data warehouse that is faster, easier to use, and far more flexible than traditional data warehouse offerings. With Snowflake's unique and patented architecture, it's easy to amass all of your data, enable rapid analytics, and derive data-driven insights for all of your users.

Braze offers two integrations with Snowflake. Together, they provide a complete, bidirectional data pipeline between your Braze and Snowflake environments.

## Choosing an integration

### Data Sharing (Braze to Snowflake)

Snowflake [Secure Data Sharing]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/data_sharing/) gives you secure, real-time access to Braze engagement and campaign data directly in your Snowflake instance. No data is copied or transferred between accounts—all sharing is accomplished through Snowflake's unique services layer and metadata store.

**Use Data Sharing when you want to:**
- Query Braze event and campaign data using Snowflake SQL
- Create complex reports and perform attribution modeling
- Join Braze data with other data in your Snowflake warehouse
- Benchmark your engagement data across channels, industries, and device platforms

For setup instructions, see [Snowflake Data Sharing]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/data_sharing/).

### Cloud Data Ingestion (Snowflake to Braze)

[Cloud Data Ingestion (CDI)]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/) lets you sync data from your Snowflake instance directly into Braze. This allows you to keep user attributes, events, and purchases in Braze up to date with your source-of-truth data warehouse.

**Use Cloud Data Ingestion when you want to:**
- Sync user attributes from Snowflake to Braze user profiles
- Send event or purchase data from Snowflake into Braze
- Keep Braze in sync with data transformations happening in your warehouse
- Avoid building and maintaining custom ETL pipelines from Snowflake to Braze

For setup instructions, see [Cloud Data Ingestion: Data warehouse integrations]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/).
