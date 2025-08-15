---
nav_title: Snowflake Data Sharing
hidden: true
---

# Snowflake data sharing integration

> When Snowflake Data Share is used as an integration method, Braze will provision a share to your Snowflake instance on behalf of the customer. This share will automatically include all message engagement and user behavior events.

Shares are provisioned on a per-customer basis after the customer has purchased a Snowflake Data Share entitlement. When a customer requests a data share, Braze will add a share to the customer's workspace, and the customer can use the self-service UI to add the relevant partner Snowflake account data.

![]({% image_buster /assets/img/snowflake.png %})

Once the share is provisioned, all data is immediately accessible from within the Snowflake instance as an incoming data share.

![]({% image_buster /assets/img/snowflake2.png %})

Within your Snowflake instance, you will see one share per region. Each table has a column, `app_group_id`, which is effectively a tenant key for Braze. As new customers are added to a share within the same region, it will appear as different `app_group_ids` within the existing tables.

{% alert important %}
Braze currently hosts all user-level data in the Snowflake AWS US East-1 and EU-Central (Frankfurt) regions. Although Braze can share cross-region, it is most cost-effective for the customers if we share with `US-EAST-1` and/or `EU-CENTRAL-1`. 
{% endalert %}

{% alert tip %}
Download the [raw table schemas]({{site.baseurl}}/assets/download_file/data-sharing-raw-table-schemas.txt?ffbc5f5ca7092bc9ae26268aa0e711df) here or use this set of [sample event data](https://app.snowflake.com/marketplace/listing/GZT0Z5I4XY0/braze-braze-user-event-demo-dataset) available in the Snowflake marketplace to familiarize yourself with the events shared.
{% endalert %}

## Handling duplicate events

Duplicates are expected, but all events have a unique identifier, the ID column. Duplicates can be removed by doing `select distinct(id)`.

## Breaking versus non-breaking changes

### Non-breaking changes

Non-breaking changes can happen at any time and generally provide additional functionality. Examples of non-breaking changes:
- Adding a new table or view
- Adding a column to an existing table or view

{% alert important %}
Because new columns are considered non-breaking, Braze strongly recommends explicitly listing the columns of interest in each query instead of using `SELECT *` queries. Alternatively, you might want to create views that explicitly name columns and then query those views instead of the tables directly.
{% endalert %}

### Breaking changes

When possible, breaking changes will be preceded by an announcement and a migration period. Examples of breaking changes include:
- Removing a table or view
- Removing a column from an existing table or view
- Changing the type or nullability of an existing column

## General Data Protection Regulation (GDPR) compliance

Nearly every event record Braze stores includes a few fields representing users’ personally identifiable information (PII). Some events may include email address, phone number, device ID, language, gender, and location information. If a user’s request to be forgotten is submitted to Braze, we will null out those PII fields for any event belonging to those users. This way, we’re not removing the historical record of the event, but now the event can never be tied back to a specific individual.
