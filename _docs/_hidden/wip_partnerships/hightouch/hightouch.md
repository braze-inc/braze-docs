---
nav_title: Hightouch
page_order: 1

description: "This article details the partnership between Braze and Hightouch, a platform to sync your customer data from your warehouse to business tools."
alias: /partners/hightouch/
page_type: partner

---

# Hightouch

> [Hightouch][1] is a modern data integration platform that enables you to sync customer, product, or proprietary data from your warehouse or data lake to any app of your choice, all without assistance from your IT or engineering teams.

The Braze and Hightouch integration allows you to build better campaigns on Braze with up-to-date customer data from your data warehouse. You want to provide relevant, timely interactions to your customers, and doing so heavily relies on data in your Braze account to be accurate and fresh. By automatically syncing customer data from your data warehouse into Braze, you no longer need to worry about data consistency, and you can focus on building world-class customer experiences.

## Requirements

| Requirement | Origin | Access | Description |
|---|---|---|---|
| Braze API Key | Braze | You will need to create a new API key.<br><br>This can be created in the __Developer Console -> API Settings -> Create New API Key__ with __users.track__ permissions. | You will use your Braze API key to authenticate using Hightouch. |
| Braze REST Endpoint | Braze | [Braze REST endpoint list][2]. | Your REST endpoint URL.  |
| Hightouch Account | Hightouch | Your Hightouch Workspace. | An active Hightouch account. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Braze and Hightouch Integration

### Step 1: Obtain Braze Credentials

#### Create a Braze API Key

1. Within Braze, navigate to __Settings__ at the bottom of the left navigation bar and click __Developer Console__.
2. In the __API Settings__ tab, under __Rest API Keys__, click __+ Create New API Key__.
3. Name this API key, and select all User Data permissions relevant to this integration.  Next, select __Save API Key__.
4. Lastly, copy the API Key found under __Identifier__ to use when creating your Hightouch connection. 

#### Find your Braze API Endpoint

You will need to locate your Braze REST API endpoint. You will need this when creating your Hightouch destination with Braze. Your endpoint will depend on the Braze URL for your instance; you can find a full list of all Braze endpoints [here][2]. 

Hightouch only requires everything after "https://rest." to specify your endpoint. For example, if your Braze endpoint is https://rest.iad-01.braze.com, you will only need `iad-01.braze.com`.

### Step 2: Create your Hightouch Braze Destination

1. In the __Destinations__ section of Hightouch, click __Add destination__.
2. Select __Braze__ in the list of destinations listed.
3. Provide the Braze endpoint (excluding https://rest.) and your API Key.<br><br>![add_destination][3]

## Supported Objects and Sync Modes

Hightouch supports syncing to both user objects and events.

| Destination | Description | Supported Modes |
|---|---|---|
| Object | Syncs records to objects such as users or organizations in your destination.| Upsert or Update |
| Events | Syncs records as events to your destination; this is often in the form of a track call. | Track Event or Track Purchase |

## Use Cases

* Sync data about users and accounts into Braze to build hyper-personalized campaigns.
* Automatically update your Braze segments with fresh data from your warehouse.
* Deliver better experiences by bringing in data from other customer touchpoints into Braze.

## Additional Information

For more information on the Braze and Hightouch integration regarding field mapping and user and event syncing, visit the [Hightouch docs](https://hightouch.io/docs/destinations/braze/
).

[1]: https://hightouch.io
[2]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)
[3]: {% image_buster /assets/img/hightouch/hightouch_braze_setup.png %}
[4]: https://hightouch.io/docs/destinations/braze/
