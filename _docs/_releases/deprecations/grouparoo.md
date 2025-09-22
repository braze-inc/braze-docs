---
nav_title: Grouparoo
page_order: 1
description: "This article outlines the partnership between Braze and Grouparoo, a open-source reverse ETL tool that makes it easy to power your Marketing, Sales, and Support tools using the data in your data warehouse."
page_type: update

---

# Grouparoo

{% alert update %}
Support for Grouparoo has been discontinued as of April 2022.
{% endalert %}

> [Grouparoo](https://www.grouparoo.com/) is an open-source reverse ETL tool that makes it easy to power your marketing, sales, and support tools using the data in your warehouse. Configuration is done in a model-centric UI, making it possible for non-technical team members to configure and schedule data syncs in support of operations.

The Braze and Grouparoo integration makes it easy to operationalize data stored in a warehouse by sending it to Braze. When you set up automatic sync schedules, you can consistently enhance customer communications with up-to-date information.

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Grouparoo account and project | A Grouparoo account and project are required to take advantage of this partnership.<br><br>This integration is possible to use with the free community edition and enterprise solutions provided by Grouparoo. Setup will take place in the Grouparoo configuration user interface. |
| Braze REST API key | A Braze REST API key with users and track permissions. <br><br> This can be created in the Braze dashboard from **Settings** > **API Keys**. |
| Braze REST endpoint | [Your REST endpoint URL](https://www.grouparoo.com/). Your endpoint will depend on the Braze URL for your instance. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Step 1: Create a Braze app in Grouparoo

In Grouparoo, navigate to **Apps** and select **Braze** to create a new Braze app. In the modal that appears, provide your Braze API key and REST endpoint.

![]({% image_buster /assets/img/grouparoo/add-app.png %})

### Step 2: Set up a model and data source

This integration requires that you have an existing model and data source set up before continuing to the next step. If you do not have this set up, visit the Grouparoo documentation to learn how to set up a [model](https://www.grouparoo.com/docs/config/models) and [data source](https://www.grouparoo.com/docs/config/sources).

### Step 3: Create a Braze destination in Grouparoo

#### Select sync mode

In Grouparoo, select your model from the navigation bar. Next, scroll to the **Destinations** section and click **Add new Destination**.

Next, select the **Braze** app you made, name the destination, and select your desired sync mode from the following:
- **Sync**: Add, update, and remove Braze users as needed. This option looks for new records, changes to existing records, and deletions.
- **Additive**: Add and update Braze users as needed, but do not remove anybody. This option looks for new users to add to Braze and changes to existing Braze users but does not keep track of deletions.
- **Enrich**: Only update those users that already exist in Braze. Do not add or remove Users. This option will only update existing users in Braze.

#### Property field mapping

Next, you must map Grouparoo property fields to Braze property fields. 

![Example property mapping fields. Grouparoo userID is set to map to external_id. email, firstName, and lastName are set as equivalent "email", "first_name", and "last_name" grouparoo fields.]({% image_buster /assets/img/grouparoo/mapping.png %}){: style="max-width:80%;"}

Make sure the Braze `external_id` field is mapped to the primary key in your source table. Map the rest of the fields as necessary for your use case.

**Send Record Properties** section: A list of preset user profile fields available to map data. Any of these can be synced to from Grouparoo properties.

**Optional Braze User Profile Fields** section: Create optional custom Braze user profile fields. If you click **Add New Braze User Profile Field**, you will see all the available properties you can map to Braze. The name of any new field you create will be the same as the Grouparoo property but can be renamed.

#### Grouparoo groups

In addition to mapping, you may also choose to add Grouparoo groups to Braze subscription groups. 

![Under "Braze Subscription Groups" in the Grouparoo destination configuration window, the "High value with recent automotive purchase" Grouparoo group will be added to the "High value with recent automotive purchase" Braze subscription group.]({% image_buster /assets/img/grouparoo/lists.png %}){: style="max-width:80%;"}

{% alert important %}
Further details and updates on this integration can be found in [Grouparoo's documentation](https://www.grouparoo.com/docs/integrations/grouparoo-braze).
{% endalert %}

