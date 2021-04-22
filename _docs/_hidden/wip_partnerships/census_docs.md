---
nav_title: Census
page_order: 1

description: "Use the Braze and Census integration to dynamically create targeted user segments with data from your cloud warehouse."
alias: /partners/census/

page_type: partner
hidden: true
---

# Census

> [Census][1] is the data integration platform that enables you to sync customer and product data from your cloud warehouse to the sales and marketing apps of your choice. 

With Census, keeping your customer success, sales, and marketing teams on the same page has never been easier. As Braze's technology partner, Census keeps your customer data in sync, without ongoing help from your engineering department.

## Requirements

In order to use Braze with Census, you'll need:

| Requirement | Origin | Access | Description |
|---|---|---|---|
| Braze API Key | Braze | You will need to create a new API Key.<br><br>This can be created in the __Developer Console -> API Settings -> Create New API Key__ with __users.track__ permissions. | This description should tell you what to do with the Braze API Key. |
| Braze REST Endpoint | Braze | [Braze REST Endpoint List][2] | Your REST Endpoint URL. Your endpoint will depend on the Braze URL for your instance. |
| Census Account | Census | Your Census Instance | An active Census account with an active Braze service connection. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Braze and Census Integration

The Braze and Census integration allows you to use your product data to dynamically create targeted user segments in Braze. For example, after successfully testing and implementing the integration, Braze can create a user segment of 'Users Active in the Last 30 Days' to target users that have used your product in the last 30 days, to ask them to test an upcoming beta feature.

Complete the steps below to get started:

### Step 1: Create a Braze API Key

Braze allows you create multiple API keys, each with their own set of permissions. In most cases, the recommended practice is to create new API key for Census rather than reusing an existing one.

__1.__ Within Braze, navigate to __App Settings__ in the bottom of the left navigation bar and click __Developer Console__.

![app_settings][3]

__2.__ In the __API Settings__ tab, under __Rest API Keys__, click __+ Create New API Key__.

![new_key][4]

__3.__ Provide a name you'll recognize (for example, "Census") and select the permissions shown below. Currently, you only need to select all the User Data permissions, except for users.delete. This permission set may change as Census adds support for more Braze objects, so you may either want to grant more permissions now or plan to update these permissions in the future. Scroll down and click __Save API Key__.

![save_key][5]

__4.__ Finally, copy the long code you see under __Identifier__ to use in Step 3.

![identifier][6]

### Step 2: Select your Braze API Endpoint

Braze requires a slightly different URL to access your account depending on where it has been set up - you can find the the full list of all [Braze API Endpoints here][2]. Generally, you need the number from the URL you see in your browser when you're signed into Braze.

For example, if your Braze URL is https://dashboard- 03.braze.com/, then your API Endpoint will be https://rest.iad-03.braze.com.

### Step 3: Create the Census Connection

Let's pull it all together!

__1.__ In the __Settings__ tab, create a new Braze Service Connection in Census.

![settings][7]

__2.__ You can provide whatever name you like.

__3.__ Provide the appropriate Braze Endpoint URL.

__4.__ Copy and paste your new Braze API key.

![add_service][8]


## Supported Sync Behaviors in Census

As of September 2020, Census supports syncing your data to the __User__ object in Braze. 

[1]: https://www.getcensus.com/
[2]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)
[3]: {% image_buster /assets/img/census/app_settings.png %}
[4]: {% image_buster /assets/img/census/new_key.png %}
[5]: {% image_buster /assets/img/census/save_key.png %}
[6]: {% image_buster /assets/img/census/identifier.png %}
[7]: {% image_buster /assets/img/census/settings.png %}
[8]: {% image_buster /assets/img/census/add_service.png %}
