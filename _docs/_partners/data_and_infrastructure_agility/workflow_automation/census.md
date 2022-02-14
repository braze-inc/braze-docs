---
nav_title: Census
article_title: Census
page_order: 9
description: "This article outlines the partnership between Braze and Census, a data integration platform that allows you to dynamically create targeted user segments with data from your cloud warehouse."
alias: /partners/census/
page_type: partner
search_tag: Partner

---

# Census

> [Census][1] is the data integration platform that enables you to sync customer and product data from your cloud warehouse to the sales and marketing apps of your choice, all without ongoing help from your engineering department. 

The Braze and Census integration allows you to dynamically import your Census product data into Braze to create targeted user segments. For example, after successfully testing and implementing the integration, Braze can create a user segment from the new data of 'Users Active in the Last 30 Days' to target specific users to ask them to test an upcoming beta feature.

## Prerequisites

| Requirement | Description |
| --- | --- |
| Census account | A [Census account][1] is required to take advantage of this partnership. |
| Braze REST API key | A Braze REST API key with all user data permissions(except for `users.delete`) and `segments.list` permissions. The permissions set may change as Census adds support for more Braze objects, so you may either want to grant more permissions now or plan to update these permissions in the future. <br><br> This can be created within the **Braze Dashboard > Developer Console > REST API Key > Create New API Key**. |
| Braze REST endpoint  | Your REST Endpoint URL. Your endpoint will depend on the [Braze URL for your instance][2]. |
| Data warehouse and data model | Before beginning the integration, you must have a data warehouse set up in Census and define a model of the subset of data you want to sync to Braze. Visit [Census documentation](https://docs.getcensus.com/destinations/braze) for a list of available data sources and guidance on model creation. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## Integration

### Step 1: Create Braze service connection

To integrate Census, in the Census platform, navigate to the **Settings** tab, and select **Add Service** to create a new Braze service connection.

In the prompt that appears, name this connection, and provide your Braze endpoint URL and Braze REST API key.

![Add service][8]{: style="max-width:60%;"}

### Step 2: Create a Census sync

To sync customers to Braze, you must build a sync. Here, you will define where to sync data and how you would like fields mapped across the two platforms.

1. Navigate to the **Syncs** tab and select **Add Sync**. 
2. In the prompt that appears, under **Connection**, select your desired data warehouse.
3. Next, select the source. This is the data model built from your data warehouse data.
4. Configure where the model will be synced to. Select **Braze** as the connection, and the [supported object type](#supported-objects) to sync.<br>![Census sync][10]{: style="max-width:80%;"}<br><br>
5. Make sure **Update or Create** is selected as a syncing rule.
6. Next, for record matching purposes, choose your desired [Braze user identifier](#supported-objects) for your Braze object type and associated model field.<br>![Census sync][9]{: style="max-width:80%;"}<br><br>
7. Lastly, map the Census data fields to the equivalent Braze fields.<br>![Census mapping][11]{: style="max-width:80%;"}<br><br>
8. Confirm details and create the sync. 

Once the sync is created, you will find the user data already in Braze. You can now create a Braze segment and add it to future Braze campaigns and Canvases to target these end-users. 

{% alert note %}
When using the Census and Braze integration, Census will only send the deltas (changing data) on each sync to Braze. 
{% endalert %}

## Supported objects

Census currently supports syncing of the following Braze objects:

| Object name | Identifiers |
| --- | --- |
| User | External user ID |
| Event | Event ID |

[1]: https://www.getcensus.com/
[2]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[8]: {% image_buster /assets/img/census/add_service.png %}
[9]: {% image_buster /assets/img/census/census_1.png %}
[10]: {% image_buster /assets/img/census/census_2.png %}
[11]: {% image_buster /assets/img/census/census_3.png %}