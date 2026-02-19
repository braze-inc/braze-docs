---
nav_title: FAQ
article_title: Managing Custom Data FAQ
page_order: 1
page_type: FAQ
description: "This page provides answers to frequently asked questions about managing custom data in Braze."
---

# Frequently asked questions

> This page provides answers to some frequently asked questions about managing custom data.

### Why is my custom attribute detected as a different data type in production than in development?

Braze automatically detects the data type of a custom attribute based on the first value it receives. If your development environment sends a numeric value like `100` first, the attribute is stored as a number. If your production environment's first value arrives as a string (such as `"100"` wrapped in quotes), the attribute is stored as a string.

To prevent this, ensure your integration sends consistent data types across all environments. If the wrong type is already set, you can force the correct data type in **Data Settings** > **Custom Attributes** by using the [data type dropdown]({{site.baseurl}}/user_guide/data/activation/custom_data/managing_custom_data/#forcing-data-type-comparisons).

### If I force a data type change on a custom attribute, will existing data be converted?

No. Forcing a data type change only affects new data coming into Braze. Any data ingested before the type change continues to be stored as the old type and may not be segmentable with the new type's filters. A warning appears on the affected users' profiles.

If you need all existing user data to match the new type, you must re-send the attribute values for those users through the SDK, API, or a CSV import. There is no automatic bulk conversion for existing data.

### How can I avoid data type issues when using Cloud Data Ingestion (CDI)?

When using CDI to sync data from external sources (such as Databricks or Snowflake), ensure your source columns use the correct data types before syncing. Common issues include:

- **Timestamps stored as strings**: Make sure your date columns use a timestamp or datetime type in your source database, not a varchar or string.
- **Numbers stored as strings**: Cast numeric columns to integer or float types in your source query before syncing.
- **Inconsistent types across syncs**: If a column type changes between syncs, Braze may reject the new data. Verify your source schema remains consistent.
