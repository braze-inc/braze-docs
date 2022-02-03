---
nav_title: Grouparoo
article_title: Grouparoo
page_order: 1

description: "Grouparoo is an open source Reverse ETL tool that makes it easy to power your Marketing, Sales, and Support tools using the data in your data warehouse."
alias: /partners/grouparoo/

page_type: partner
search_tag: Partner
hidden: true

---

# Grouparoo

> [Grouparoo][1] is an open source Reverse ETL tool that makes it easy to power your marketing, sales, and support tools using the data in your warehouse. Configuration is done in a Model-centric UI making it possible for non-technical team members to configure and schedule data syncs in support of operations.

<br />

The Braze and Grouparoo integration makes it easy to operationalize data stored in a warehouse by sending it to Braze. When you set up automatic sync schedules, you can consistently enhance customer communications with up to date information.

## Prerequisites

You will need a Braze account, a Braze API key, and Braze REST Endpoint to sync data to Braze using Grouparoo.

To find your API keys in the Braze dashboard, use the menu to navigate to __Braze Dashboard -> Developer Console -> REST API Key ->__. There, you will see a list of any existing API keys and have the option to create a New API key.

The API key you use to configure Grouparoo to connect with Braze needs to have Users and Campaigns permissions.


| Requirement | Description |
| ----------- | ----------- |
| Grouparoo Project | A Grouparoo project is required to take advantage of this partnership between Braze and Grouparoo. This integration is possible to use with the free community edition as well as enterprise solutions provided by Grouparoo. Setup will take place in the Grouparoo Configuration User Interface |
| Braze REST API key | A Braze REST API Key with `users.track` permissions as well as campaigns permissions. <br><br> This can be created within the __Braze Dashboard -> Developer Console -> REST API Key -> Create New API Key__ |
| Braze REST endpoint | [Your REST endpoint URL][1]. Your endpoint will depend on the Braze URL for your instance. |
{: .reset-td-br-1 .reset-td-br-2}


## Integration

To connect Grouparoo to Braze, you create an App in Grouparoo that details how to make the connection. This specifies account information used for Braze access.

### Step 1: Create a Braze App in Grouparoo

In Grouparoo, while creating an App for Braze, you must specify two options to connect to Braze.

![Add an App][2]{: style='max-width:60%;"}

| Option | Description |
| ----------- | ----------- |
| Braze API Key | Braze REST API key. It can be found under the Developer Console (bottom left side of the menu) on the Braze dashboard. Users and Campaigns permissions are needed.|
| Braze REST Endpoint | Braze REST Endpoint. It uses the same instance number as the dashboard (i.e. if the dashboard URL is dashboard-01.braze.com the REST endpoint will be rest.iad-01.braze.com)|

### Step 2: Create a Braze Destination in Grouparoo

Once you have a Model and data Source set up, you can set up Braze as a Destination.

You name the Destination and choose which sync mode you would like to use (Create, Update, and Delete are options available for syncing through Grouparoo)

- **Sync**: Add, update, and remove Braze Users as needed.This option looks for new records, changes to existing records, and deletions.
- **Additive**: Add and update Braze Users as needed, but do not remove anybody. This option looks for new Users to add to Braze and changes to existing Braze Users, but does not keep track of deletions.
- **Enrich**: Only update those Users that already exist in Braze. Do not add or remove Users. This option will only update existing Users in Braze.


Next, you'll need to map properties. The external_id Profile Field in Braze must be mapped to the primary key in your Source table.

![Property to Profile Field Mapping][3]{: style='max-width:60%;"}

After mapping this required field, Braze has a list of preset User Profile Fields available to map data. You can find these by scrolling through the dropdown menu in the Send Record Property portion of the form. Any of these can be synced to from Grouparoo Properties.

Below the Optional Braze User Profile Fields heading, you have the option to create custom Braze User Profile Fields. When you Click ‘Add New Braze User Profile Field’, you will see the properties available in Grouparoo to map to Braze. Choose one of these to create a new mapping and a new Field in Braze. The name of the Braze Profile Field you create is the same as the name of the Grouparoo Property you’ve chosen, by default, but can be edited.

In addition to mapping, during this step you may also choose to add Grouparoo Groups to Braze Subscription Groups. Braze’s Subscription Groups are segment filters used to narrow your audience that allow for more granular subscription options for end-users. An app group in Braze can have up to 25 Subscription Groups.

![Groups to Lists][4]{: style='max-width:60%;"}


{% alert important %}
Further details and updates on this integration can be found in [Grouparoo's documentation](https://www.grouparoo.com/docs/integrations/grouparoo-braze).
{% endalert %}

[1]: https://www.grouparoo.com/
[2]: {% image_buster /assets/img/grouparoo/add-app.png %}
[3]: {% image_buster /assets/img/grouparoo/mapping.png %}
[4]: {% image_buster /assets/img/grouparoo/lists.png %}
