---
nav_title: Census
article_title: Census Cohort Import
description: "This reference article outlines the cohort import functionality of Census, a data integration platform that allows you to dynamically create targeted user segments with data from your cloud warehouse."
page_type: partner
search_tag: Partner

---

# Census cohort import

> This article describes how to import user cohorts from [Census][1] to Braze. For more information on integrating Census, see the main [Census article]({{site.baseurl}}/partners/data_and_infrastructure_agility/workflow_automation/census/).

## Cohort import integration

### Step 1: Create Braze service connection

To integrate Census in the Census platform, navigate to the **Connections** tab and select **New Destination** to create a new Braze service connection.

In the prompt that appears, name this connection, and provide your Braze endpoint URL and Braze REST API key (and, optionally, your data import key to sync cohorts).

![][8]{: style="max-width:60%;"}

### Step 2: Create a Census sync

To sync customers to Braze, you must build a sync. Here, you will define where to sync data and how you would like fields mapped across the two platforms.

1. Navigate to the **Syncs** tab and select **New Sync**.<br><br> 
2. In the composer, select the source data model from your data warehouse.<br><br>
3. Configure where the model will be synced to. Select **Braze** as the destination and **User & Cohort** to sync.<br>![In the "Select a Destination" prompt, "Braze" is selected as the connection, and various objects are listed.][10]{: style="max-width:80%;"}<br><br>
4. Select the **Source Column** that identifies the users to add to a cohort, and select **External User ID** as the **Identifier Type**.<br><br>
5. In the **Cohort Name** dropdown, select a cohort, create a cohort, or select a Source Column to populate the cohort name.<br><br>
6. Use the **When a record is removed from source data** dropdown to select what happens to users when they're removed from the source dataset, such as **Do nothing** or **Remove matching record from cohort**.<br><br>
7. Lastly, map the Census data fields to the equivalent Braze fields.<br>![Census mapping][11]{: style="max-width:80%;"}<br><br>
8. Confirm details and create the sync. 

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
{: .reset-td-br-1 .reset-td-br-2}

Additionally, Census supports sending [structured data](https://docs.getcensus.com/destinations/braze#supported-objects) to Braze: 
- User push tokens: To send push tokens, your data should be structured as an array of objects with 2-3 values: `app_id`, `token`, and an optional `device_id`.
- Nested custom attributes: Both objects and arrays are supported. As of April 2022, this feature is still in early access. You may need to contact your Braze account manager for access.

[1]: https://www.getcensus.com/
[8]: {% image_buster /assets/img/census/add_service.png %}
[10]: {% image_buster /assets/img/census/census_2.png %}
[11]: {% image_buster /assets/img/census/census_3.png %}