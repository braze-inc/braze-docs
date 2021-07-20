---
nav_title: Census
page_order: 9
description: "This article outlines the partnership between Braze and Census, a data intgration platform that allows you to dynamically create targeted user segments with data from your cloud warehouse."
alias: /partners/census/
page_type: partner
---

# Census

> [Census][1] is the data integration platform that enables you to sync customer and product data from your cloud warehouse to the sales and marketing apps of your choice. 

With Census, keeping your customer success, sales, and marketing teams on the same page has never been easier. As Braze's technology partner, Census keeps your customer data in sync, without ongoing help from your engineering department.

## Requirements

| Requirement | Origin | Access | Description |
|---|---|---|---|
| Braze API Key | Braze | You will need to create a new API Key.<br><br>This can be created in the __Developer Console -> API Settings -> Create New API Key__ with __users.track__ permissions. | This description should tell you what to do with the Braze API Key. |
| Braze REST Endpoint | Braze | [Braze REST Endpoint List][2] | Your REST Endpoint URL. Your endpoint will depend on the Braze URL for your instance. |
| Census Account | Census | Your Census Instance | An active Census account with an active Braze service connection. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Braze and Census Integration

The Braze and Census integration allows you to use your product data to dynamically create targeted user segments in Braze. For example, after successfully testing and implementing the integration, Braze can create a user segment of 'Users Active in the Last 30 Days' to target specific users to ask them to test an upcoming beta feature.

### Step 1: Create a Braze API Key

Braze allows you to create multiple API keys, each with its own set of permissions. In most cases, the recommended practice is to create a new API key for Census rather than reusing an existing one.

1. Within Braze, navigate to __Settings__ at the bottom of the left navigation bar and click __Developer Console__.
2. In the __API Settings__ tab, under __Rest API Keys__, click __+ Create New API Key__.
3. Name this API key, and select all User Data permissions, except for `users.delete`. The permissions set may change as Census adds support for more Braze objects, so you may either want to grant more permissions now or plan to update these permissions in the future. Next, select __Save API Key__.
4. Lastly, copy API Key found under __Identifier__ to use when creating your Census connection. 

### Step 2: Select your Braze API Endpoint

Locate and note your Braze REST API endpoint, this will be needed when creating your Census connection with Braze. Your endpoint will depend on the Braze URL for your instance, find a full list of all Braze API Endpoints [here][2]. 

### Step 3: Create the Census Connection

1. In the __Settings__ tab, create a new __Braze Service Connection__ under __Add Service__ in Census.
2. Name this connection and provide the Braze Endpoint URL and API Key.<br><br>![add_service][8]{: style="max-width:60%;"}

## Supported Sync Behaviors in Census

Census supports syncing your data to both the user and event object in Braze. To learn more about this integration and Census syncing behaviors, visit the following [Census documentation](https://docs.getcensus.com/destinations/braze).


[1]: https://www.getcensus.com/
[2]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)
[8]: {% image_buster /assets/img/census/add_service.png %}
