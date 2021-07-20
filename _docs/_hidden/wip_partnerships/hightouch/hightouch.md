---
nav_title: Hightouch
page_order: 1

description: "This article details the partnership between Braze and Hightouch, a platform to sync your customer data from your warehouse to business tools."
alias: /partners/hightouch/

page_type: partner
hidden: true
---

# [Hightouch]

> [Hightouch][1] is a Reverse ETL platform that enables you to sync customer, product, or proprietary data from your warehouse or data lake to any app of your choice.

With Hightouch, you're able to own your data and keep it in sync everywhere in your technology stack. As Braze's technology partner, Hightouch keeps your customer data in sync, without the assistance from your IT or engineering teams.

## Requirements

| Requirement | Origin | Access | Description |
|---|---|---|---|
| Braze API Key | Braze | You will need to create a new API Key.<br><br>This can be created in the __Developer Console -> API Settings -> Create New API Key__ with __users.track__ permissions. | You will use your Braze API Key to authenticate using Hightouch. |
| Braze REST Endpoint | Braze | [Braze REST Endpoint List][1] | Your REST Endpoint URL.  |
| Hightouch Account | Hightouch | Your Hightouch Workspace | An active Hightouch account |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Braze and Hightouch Integration

Hightouch allows you to build better campaigns on Braze with up-to-date customer data from your data warehouse. You want to provide relevant, timely interactions to your customers, and doing so heavily relies on data in your Braze account to be accurate and fresh. By automatically syncing customer data from your data warehouse into Braze, you no longer need to worry about data consistency because data is no longer flowing in from multiple sources in different formats, and you can focus on building world-class customer experiences.

### Step 1: Create a Braze API Key

Braze allows you to create multiple API keys, each with its own set of permissions. In most cases, the recommended practice is to create a new API key for Hightouch rather than reusing an existing one. However, if this not a requirement, you can skip to step 2 if you already have your key.

1. Within Braze, navigate to __Settings__ at the bottom of the left navigation bar and click __Developer Console__.
2. In the __API Settings__ tab, under __Rest API Keys__, click __+ Create New API Key__.
3. Name this API key, and select all User Data permissions relevant to this integration.  Next, select __Save API Key__.
4. Lastly, copy API Key found under __Identifier__ to use when creating your Hightouch connection. 

### Step 2: Find your Braze API Endpoint

You will need to locate your Braze REST API endpoint. You will need this when creating your Hightouch destination with Braze. Your endpoint will depend on the Braze URL for your instance, you can find a full list of all Braze endpoints [here][2]. Hightouch only requires everything after "https://rest." to specify your endpoint. As an example, if your Braze endpoint is https://rest.iad-01.braze.com, you will only need iad-01.braze.com.

### Step 3: Create your Hightouch Braze Destination

1. In the _Destinations_ section of Hightouch, click "Add destination."
2. Select Braze in the list of destinations listed.
3. Provide the Braze Endpoint (except https://rest.) and your API Key.<br /><br />![add_destination][3]

## Supported Objects and Sync Modes

Hightouch supports syncing to the __User__ object and __Events__.

| Destination | Description | Supported Modes |
|---|---|---|
| Object | Syncs records to objects such as users or organizations in your destination.| Upsert or Update |
| Events | Syncs records as events to your destination, this is often in the form of a track call. | Track event or Track Purchase|

## Use Cases

* Sync data about users and accounts into Braze to build hyper-personalized campaigns
* Automatically update your Braze segments with fresh data from your warehouse
* Deliver better experiences by bringing in data from other customer touchpoints into Braze

[1]: https://hightouch.io
[2]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)
[3]: {% image_buster /assets/img/hightouch/hightouch_braze_setup.png %}
