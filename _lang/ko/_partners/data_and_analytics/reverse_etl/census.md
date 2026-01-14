---
nav_title: Census
article_title: Census
description: "This reference article outlines the partnership between Braze and Census, a data integration platform that allows you to dynamically create targeted user segments with data from your cloud warehouse."
alias: /partners/census/
page_type: partner
search_tag: Partner

---

# Census

> [Census](https://www.getcensus.com/) is a data activation platform that connects cloud data warehouses like Snowflake and BigQuery to Braze. Marketing teams can unlock the power of their first-party data to build dynamic audience segments, sync customer attributes to personalize campaigns, and keep all their data in Braze up-to-date. It's easier than ever to take action with trusted, actionable data — no CSV uploads or engineering favors required.

The Braze and Census integration allows you to dynamically import audiences or product data into Braze to send personalized campaigns. For example, you can create a cohort in Braze for "Newsletter subscribers with CLV > 1000" to target high-value customers or "Users Active in the Last 30 Days" to target specific users to test an upcoming beta feature.

## Prerequisites

| Requirement | Description |
| --- | --- |
| Census account | A [Census account](https://www.getcensus.com/) is required to take advantage of this partnership. |
| Braze REST API key | A Braze REST API key with all user data permissions (except for `users.delete`) and `segments.list` permissions. The permissions set may change as Census adds support for more Braze objects, so you may either want to grant more permissions now or plan to update these permissions in the future. <br><br> This can be created in the Braze dashboard from **Settings** > **API Keys**. |
| Braze REST endpoint  | Your REST endpoint URL. Your endpoint will depend on the [Braze URL for your instance]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). |
| Data warehouse and data model | Before beginning the integration, you must have a data warehouse set up in Census and define a model of the subset of data you want to sync to Braze. Visit [Census documentation](https://docs.getcensus.com/destinations/braze) for a list of available data sources and guidance on model creation. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Integration

### Step 1: Create Braze service connection

To integrate Census in the Census platform, navigate to the **Connections** tab and select **New Destination** to create a new Braze service connection.

In the prompt that appears, name this connection, and provide your Braze endpoint URL and Braze REST API key (and, optionally, your data import key to sync cohorts).

![]({% image_buster /assets/img/census/add_service.png %}){: style="max-width:60%;"}

### Step 2: Create a Census sync

To sync customers to Braze, you must build a sync. Here, you will define where to sync data and how you would like fields mapped across the two platforms.

1. Navigate to the **Syncs** tab and select **New Sync**.<br><br> 
2. In the composer, select the source data model from your data warehouse.<br><br>
3. Configure where the model will be synced to. Select **Braze** as the destination and the [supported object type](#supported-objects) to sync.<br>![In the "Select a Destination" prompt, "Braze" is selected as the connection, and various objects are listed.]({% image_buster /assets/img/census/census_2.png %}){: style="max-width:80%;"}<br><br>
4. Select what synchronization rule you want to apply (**Update or Create** is the most common choice, but you can choose more advanced rules to handle deleting data, for example).<br><br>
5. Next, for record matching purposes, choose a sync key to [map](#supported-objects) your Braze object to a model field.<br>![In the "Select a Sync Key" prompt, "External User ID" from Braze is matched to "user_id" in the source.]({% image_buster /assets/img/census/census_1.png %}){: style="max-width:80%;"}<br><br>
6. Lastly, map the Census data fields to the equivalent Braze fields.<br>![Census mapping]({% image_buster /assets/img/census/census_3.png %}){: style="max-width:80%;"}<br><br>
7. Confirm details and create the sync. 

After the sync runs, you will find the user data in Braze. You can now create and add a Braze segment to future Braze campaigns and Canvases to target these users. 

{% alert note %}
When using the Census and Braze integration, Census will only send the deltas (changing data) on each sync to Braze.
{% endalert %}

## Supported objects

Census currently supports syncing of the following Braze objects:

| Object name | Sync Behaviors |
| --- | --- |
| User | Update, Create, Mirror, Delete |
| Cohort | Update, Create, Mirror | 
| Catalog | Update, Create, Mirror |
| Subscription Group Membership | Mirror |
| Event | Append |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Additionally, Census supports sending [structured data](https://docs.getcensus.com/destinations/braze#supported-objects) to Braze: 
- User push tokens: To send push tokens, your data should be structured as an array of objects with 2-3 values: `app_id`, `token`, and an optional `device_id`.
- Nested custom attributes: Both objects and arrays are supported. As of April 2022, this feature is still in early access. You may need to contact your Braze account manager for access.

