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

> [Census][1] is the data integration platform that enables you to sync customer and product data from your cloud warehouse to the sales and marketing apps of your choice.

With Census, keeping your customer success, sales, and marketing teams on the same page has never been easier. As Braze's technology partner, Census keeps your customer data in sync without ongoing help from your engineering department.

## Prerequisites

| Requirement         | Description                                                                                                                                                                        |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Braze API Key       | You will need to create a new API Key.<br><br>This can be created in the **Developer Console -> API Settings -> Create New API Key** with **users.track** permissions. |
| Braze REST Endpoint | Your REST [Endpoint URL][2]. Your endpoint will depend on the Braze URL for your instance.                                                                                         |
| Census Account      | An active Census account is required to take advantage of this Braze integration.                                                                                                  |
{: .reset-td-br-1 .reset-td-br-2}

## Braze and Census integration

The Braze and Census integration allows you to use your product data to dynamically create targeted user segments in Braze. For example, after successfully testing and implementing the integration, Braze can create a user segment of 'Users Active in the Last 30 Days' to target specific users to ask them to test an upcoming beta feature.

### Step 1: Create a Braze API key

Braze allows you to create multiple API keys, each with its own set of permissions. In most cases, the recommended practice is to create a new API key for Census rather than reusing an existing one.

1. Within Braze, navigate to **Settings** at the bottom of the left navigation bar and click **Developer Console**.
2. In the **API Settings** tab, under **Rest API Keys**, click **+ Create New API Key**.
3. Name this API key, and select all User Data permissions, except for `users.delete`. The permissions set may change as Census adds support for more Braze objects, so you may either want to grant more permissions now or plan to update these permissions in the future. Next, select **Save API Key**.
4. Lastly, copy API Key found under **Identifier** to use when creating your Census connection.

### Step 2: Select your Braze API endpoint

Locate and note your Braze REST API endpoint; this will be needed when creating your Census connection with Braze. Your endpoint will depend on the [Braze URL][2] for your instance.

### Step 3: Create the Census connection

1. In the Census **Settings** tab, select **Add Service** and create a new **Braze Service Connection**.
2. Name this connection and provide your Braze endpoint URL and API key.<br><br>!\[add_service\]\[8\]{: style="max-width:60%;"}

## Syncing in Census

When using the Census and Braze integration, Census will only send the deltas (changing data) on each sync to Braze.

### Supported sync behaviors

Census supports syncing your data to both the user and event object in Braze. Visit the following [Census documentation](https://docs.getcensus.com/destinations/braze) to learn more about this integration and Census syncing behaviors.
[8]: {% image_buster /assets/img/census/add_service.png %}

[1]: https://www.getcensus.com/
[2]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints