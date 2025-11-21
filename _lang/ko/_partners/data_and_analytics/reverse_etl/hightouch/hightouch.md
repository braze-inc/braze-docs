---
nav_title: Hightouch
article_title: Hightouch
description: "This reference article outlines the partnership between Braze and Hightouch, a platform to sync your customer data from your warehouse to business tools."
page_type: partner
search_tag: Partner

---

# Hightouch

> [Hightouch](https://hightouch.io) is a modern data integration platform that enables you to sync customer, product, or proprietary data from your warehouse or data lake to any app of your choice, all without assistance from your IT or engineering teams.

The Braze and Hightouch integration allows you to build better campaigns on Braze with up-to-date customer data from your data warehouse. By automatically syncing customer data into Braze, you no longer need to worry about data consistency and can focus on building world-class customer experiences. 

This integration also allows you to [import user cohorts to Braze]({{site.baseurl}}/partners/data_and_analytics/reverse_etl/hightouch/hightouch_cohort_import/), sending targeted campaigns based on data that may only exist in your warehouse.

## Prerequisites

| Requirement | Description |
|---|---|
| Hightouch account | A Hightouch account is required to take advantage of this partnership.
| Braze REST API key | A Braze REST API key with `users.track` and `users.export.ids` permissions. <br><br> This can be created in the Braze dashboard from **Settings** > **API Keys**. |
| Braze REST endpoint  | Your REST endpoint URL. Your endpoint will depend on the [Braze URL for your instance]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints).<br><br>Hightouch requires the name of the cluster your Braze instance sits on. For example, if your Braze endpoint is `https://rest.iad-01.braze.com`, you only need `iad-01`.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Use cases

* Sync data about users and accounts into Braze to build hyper-personalized campaigns.
* Automatically update your Braze segments with fresh data from your warehouse.
* Deliver better experiences by bringing data from other customer touchpoints into Braze.
* Import cohorts of users to Braze, allowing you to send targeted campaigns and Canvases. 

## Integration

### Step 1: Create your Hightouch Braze destination

1. On the Hightouch platform, in the **Destinations** section, click **Add destination**.
2. Select **Braze** from the list of available destinations.
3. Provide your Braze REST endpoint (excluding "https://rest.") and your Braze REST API Key.<br><br>![]({% image_buster /assets/img/hightouch/hightouch_braze_setup.png %})

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



## Integration demo

<div class="video-container">
    <iframe width="560" height="315" src="https://drive.google.com/file/d/1KQdCwZzV88hXMx7AMWgh8izqkldtNv5p/preview" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>


