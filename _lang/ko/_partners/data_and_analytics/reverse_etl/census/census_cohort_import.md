---
nav_title: Census
article_title: Census Cohort Import
description: "This reference article outlines the cohort import functionality of Census, a data integration platform that allows you to dynamically create targeted user segments with data from your cloud warehouse."
page_type: partner
search_tag: Partner

---

# Census cohort import

> This article describes how to import user cohorts from [Census](https://www.getcensus.com/) to Braze. For more information on integrating Census, see the main [Census article]({{site.baseurl}}/partners/data_and_analytics/reverse_etl/census/).

## Cohort import integration

### Step 1: Create Braze service connection

To integrate Census in the Census platform, navigate to the **Connections** tab and select **New Destination** to create a new Braze service connection.

In the prompt that appears, name this connection, and provide your Braze endpoint URL, Braze REST API key, and data import key. The data import key is required to sync cohorts and can be found in Braze by going to **Partner Integrations** > **Technology Partners** > **Census**.

![]({% image_buster /assets/img/census/add_service.png %}){: style="max-width:60%;"}

### Step 2: Create a Census sync

To sync customers to Braze, you must build a sync. Here, you will define where to sync data and how you would like fields mapped across the two platforms.

1. Navigate to the **Syncs** tab and select **New Sync**.<br><br> 
2. In the composer, select the source data model from your data warehouse.<br><br>
3. Configure where the model will be synced to. Select **Braze** as the destination and **User & Cohort** as the object to sync.<br>![In the "Select a Destination" prompt, "Braze" is selected as the connection, and various objects are listed.]({% image_buster /assets/img/census/census_2.png %}){: style="max-width:80%;"}<br><br>
4. Select the **Source Column** that identifies the users to add to a cohort, and select **External User ID** as the **Identifier Type**.<br><br>
5. In the **Cohort Name** dropdown, select a cohort, create a cohort, or select a Source Column to populate the cohort name.<br><br>
6. Use the **When a record is removed from source data** dropdown to select what happens to users when they're removed from the source dataset, such as **Do nothing** or **Remove matching record from cohort**.<br><br>
7. Lastly, map the Census data fields to the equivalent Braze fields.<br>![Census mapping]({% image_buster /assets/img/census/census_3.png %}){: style="max-width:80%;"}<br><br>
8. Confirm details and create the sync. 

Now you can run your sync!

During a sync, any fields that you map will first be synced to the user object to update what already exists in Braze. After that, the updated user will be added to the specified cohort.

After the sync, you can create and add a Braze segment with a Census cohort filter to future Braze campaigns and Canvases to target those users. 

{% alert note %}
When using the Census and Braze integration, Census will only send the deltas (changing data) on each sync to Braze.
{% endalert %}

{% alert important %}
Only users who already exist within Braze will be added or removed from a cohort. Cohort Import will not create new users in Braze.
{% endalert %}

## User Matching

Identified users can be matched by either their `external_id` or `alias`. Anonymous users can be matched by their `device_id`. Identified users who were originally created as anonymous users can't be identified by their `device_id`, and must be identified by their `external_id` or `alias`.

