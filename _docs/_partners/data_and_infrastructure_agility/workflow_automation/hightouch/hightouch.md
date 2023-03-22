---
nav_title: Hightouch
article_title: Hightouch
description: "This reference article outlines the partnership between Braze and Hightouch, a platform to sync your customer data from your warehouse to business tools."
page_type: partner
search_tag: Partner

---

# Hightouch

{:.subintro}
[Hightouch][1] is a modern data integration platform that enables you to sync customer, product, or proprietary data from your warehouse or data lake to any app of your choice, all without assistance from your IT or engineering teams.

The Braze and Hightouch integration allows you to build better campaigns on Braze with up-to-date customer data from your data warehouse. By automatically syncing customer data into Braze, you no longer need to worry about data consistency and can focus on building world-class customer experiences. 

This integration also allows you to [import user cohorts to Braze](#data-import-integration), sending targeted campaigns based on data that may only exist in your warehouse.

## Prerequisites

| Requirement | Description |
|---|---|
| Hightouch account | A Hightouch account is required to take advantage of this partnership.
| Braze REST API key | A Braze REST API key with `users.track` and `users.export.ids` permissions. <br><br> This can be created within the **Braze Dashboard > Developer Console > REST API Key > Create New API Key**. |
| Braze REST endpoint  | Your REST Endpoint URL. Your endpoint will depend on the [Braze URL for your instance][2].<br><br>Hightouch requires the name of the cluster your Braze instance sits on. For example, if your Braze endpoint is `https://rest.iad-01.braze.com`, you only need `iad-01`.|
{: .reset-td-br-1 .reset-td-br-2}

## Use cases

* Sync data about users and accounts into Braze to build hyper-personalized campaigns.
* Automatically update your Braze segments with fresh data from your warehouse.
* Deliver better experiences by bringing data from other customer touchpoints into Braze.
* Import cohorts of users to Braze, allowing you to send targeted campaigns and Canvases. 

## Integration

### Step 1: Create your Hightouch Braze destination

1. On the Hightouch platform, in the **Destinations** section, click **Add destination**.
2. Select **Braze** from the list of available destinations.
3. Provide your Braze REST endpoint (excluding "https://rest.") and your Braze REST API Key.<br><br>![][3]

### Step 2: Object and event syncing

Hightouch supports syncing to both user objects and events.

| Destination | Description | Supported modes |
|---|---|---|
| Object | Syncs records to objects such as users or organizations in your destination.| Upsert or update |
| Events | Syncs records as events to your destination; this is often in the form of a track call. | Track event or track purchase |

{% alert note %}
Refer to [Hightouch](https://hightouch.com/docs/destinations/braze#syncing-and-data-point-consumption) for more information on how syncs affect your Braze data point consumption.
{% endalert %}

#### Syncing Braze objects

You can sync Hightouch objects (user fields) to the equivalent Braze default or custom fields. You can also perform record matching to help unify data across the two platforms.

#### Syncing Braze events

Hightouch allows you to track event and purchase data and sync it to Braze. Several options can be set in Hightouch that will affect the syncing behavior, such as setting up tracking data and defining non-existent user behavior.

{% alert important %}
Further instructions on object and event syncing can be found in [Hightouch documentation](https://hightouch.io/docs/destinations/braze/).
{% endalert %}

## Data import integration

### Step 1: Get the Braze data import Key
In Braze, navigate to **Technology Partners** and select **Hightouch**. Here, you will find your REST Endpoint and generate your Braze data import key. Once generated, you can create a new key or invalidate an existing one.<br><br>![][6]{: style="max-width:90%;"} 

### Step 2: Add Braze cohorts as a Destination in Hightouch
Navigate to the **Destination** page in your Hightouch workspace, search for **Braze Cohorts**, and click **Continue**. From there, take your REST endpoint and data import key and click **Continue**.<br><br>![][7]{: style="max-width:90%;"}

### Step 3: Sync a model (or audience) into Braze Cohorts
In Hightouch, using your created [model](https://hightouch.io/docs/getting-started/create-your-first-sync/#create-a-model) or [audience](https://hightouch.io/docs/audiences/usage/), create a new sync. Next, select the Braze Cohorts destination you created in the previous step. Lastly, in the Braze Cohorts destination configuration, select the identifier you want to match against and decide whether or not you want Hightouch to create a new Braze Cohort or update an existing one.<br><br>![][8]{: style="max-width:90%;"}

### Step 4: Create a Braze segment from the Hightouch custom audience
In Braze, navigate to **Segments**, create a new segment, and select **Hightouch Cohorts** as your filter. From here, you can choose which Hightouch cohort you wish to include. Once created, you can select your Hightouch cohort segment as an audience filter when creating a campaign or Canvas.<br><br>![][9]{: style="max-width:90%;"}

### Using this integration
To use your Hightouch segment, create a Braze campaign or Canvas and select the segment as your target audience.<br><br>![][10]{: style="max-width:90%;"}

## Integration demo

<div class="video-container">
    <iframe width="560" height="315" src="https://drive.google.com/file/d/1KQdCwZzV88hXMx7AMWgh8izqkldtNv5p/preview" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

[1]: https://hightouch.io
[2]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[3]: {% image_buster /assets/img/hightouch/hightouch_braze_setup.png %}
[4]: https://hightouch.io/docs/destinations/braze/
[6]: {% image_buster /assets/img/hightouch/data_import_key.png %} 
[7]: {% image_buster /assets/img/hightouch/cohort1.png %} 
[8]: {% image_buster /assets/img/hightouch/cohort2.png %}  
[9]: {% image_buster /assets/img/hightouch/cohort3.png %}  
[10]: {% image_buster /assets/img/hightouch/cohort4.png %}  
