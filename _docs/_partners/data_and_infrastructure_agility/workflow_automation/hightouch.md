---
nav_title: Hightouch
article_title: Hightouch
description: "This article outlines the partnership between Braze and Hightouch, a platform to sync your customer data from your warehouse to business tools."
alias: /partners/hightouch/
page_type: partner
search_tag: Partner

---

# Hightouch

> [Hightouch][1] is a modern data integration platform that enables you to sync customer, product, or proprietary data from your warehouse or data lake to any app of your choice, all without assistance from your IT or engineering teams.

The Braze and Hightouch integration allows you to build better campaigns on Braze with up-to-date customer data from your data warehouse. By automatically syncing customer data into Braze, you no longer need to worry about data consistency and can focus on building world-class customer experiences. 

## Prerequisites

| Requirement | Description |
|---|---|
| Hightouch account | A Hightouch account is required to take advantage of this partnership.
| Braze REST API key | A Braze REST API key with `users.track` permissions. <br><br> This can be created within the **Braze Dashboard > Developer Console > REST API Key > Create New API Key**. |
| Braze REST endpoint  | Your REST Endpoint URL. Your endpoint will depend on the [Braze URL for your instance][2].<br><br>Hightouch requires everything after "https://rest." to specify your endpoint. For example, if your Braze endpoint is `https://rest.iad-01.braze.com`, you will only need `iad-01.braze.com`.|
{: .reset-td-br-1 .reset-td-br-2}

## Use cases

* Sync data about users and accounts into Braze to build hyper-personalized campaigns.
* Automatically update your Braze segments with fresh data from your warehouse.
* Deliver better experiences by bringing data from other customer touchpoints into Braze.

## Integration

### Step 1: Create your Hightouch Braze destination

1. On the Hightouch platform, in the **Destinations** section, click **Add destination**.
2. Select **Braze** from the list of available destinations.
3. Provide your Braze REST endpoint (excluding "https://rest.") and your Braze REST API Key.<br><br>![Add destination][3]

### Step 2: Object and event syncing

Hightouch supports syncing to both user objects and events.

| Destination | Description | Supported modes |
|---|---|---|
| Object | Syncs records to objects such as users or organizations in your destination.| Upsert or update |
| Events | Syncs records as events to your destination; this is often in the form of a track call. | Track event or track purchase |

#### Syncing Braze objects

You can sync Hightouch objects (user fields) to the equivalent Braze default or custom fields. You can also perform record matching to help unify data across the two platforms.

#### Syncing Braze events

Hightouch allows you to track event and purchase data and sync it Braze. Several options can be set in Hightouch that will affect the syncing behavior, such as setting up tracking data and defining non-existent user behavior.

{% alert important %}
Further instructions on object and event syncing can be found in [Hightouch documentation](https://hightouch.io/docs/destinations/braze/).
{% endalert %}


[1]: https://hightouch.io
[2]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)
[3]: {% image_buster /assets/img/hightouch/hightouch_braze_setup.png %}
[4]: https://hightouch.io/docs/destinations/braze/