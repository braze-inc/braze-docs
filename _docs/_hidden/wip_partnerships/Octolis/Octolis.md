---
nav_title: Octolis
article_title: Octolis
page_order: 1

description: "Everything you need to know about Braze integration with Octolis"
alias: /partners/Octolis/

page_type: partner
search_tag: Octolis
hidden: true

---

# Octolis

> [Octolis][0] is a powerful data activation platform (or headless CDP). Sitting on top of a database you own, Octolis is the easiest way to unify, prepare, score and sync data in your business tools.

The Braze and Octolis integration allows you easily integrate all your data into Braze’s data model. With Octolis, you are now able to transform data from several sources to feed Braze with contacts attributes or events, for example : 
- Unify online and offline data
- Normalize offline data
- Add computed fields or score
- Sync data to Braze as events or contacts attributes

![][7]

## Prerequisites

This section should list what you need to complete this partnership integration. The best way to deliver this information is with a quick instructional paragraph that describes any non-technically important details or "need to know" information, like whether or not your integration will be subject to additional security checks or clearances. Then, use a chart to describe the technical requirements of the integration.

{% alert important %}
The following requirements listed are typical requirements you might need from Braze. We recommend using the attributed titling and phrasing listed in the following chart. Be sure to adjust the descriptions and tailor them to your partnership integration. 
{% endalert %}

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Octolis account | An Octolis account is required to take advantage of this partnership. |
| Braze REST API key | A Braze REST API key with [*users.track*][1] permissions. <br><br> This can be created within the **Braze Dashboard > Developer Console > REST API Key > Create New API Key**. |
| Braze REST endpoint | [Your REST endpoint URL][2]. Your endpoint will depend on the Braze URL for your instance. |
| Braze app key | Your app identifier key. This can be found within the Braze Dashboard > Manage Settings > API Key. |
{: .reset-td-br-1 .reset-td-br-2}

## Getting started

### Introduction

Acting as a middleware between your raw data sources and Braze, Octolis will make you able to retrieve and unify data from various sources, online & offline.

Our approach is particularly relevant for omnichannel players : 

1. Unify & combine data from any sources: Eshop, CRM, POS system,…
2. Normalize & score 
3. Real-time synchronization of computed fields and events to Braze 

For instance, we enable KFC France to send offline transactional data from ERP to braze as events (new orders in the restaurant ABC, loyalty enrollment,..). Thus, KFC retrieves in Braze all of the offline touchpoints for each customer.

### Multi-keys deduplication
Deduplication is a major challenge when it comes to reconciling data from multiple sources and especially online and offline.
Depending on business reality and the quality/completeness of your data, you will need the flexibility to choose the most relevant key combination for deduplication.

For instance, you might want to define that "If two contacts have a different email but the same postal address + first/last name, then the two contacts should be deduplicated and merged.”
But it could be as well: Email x Phone x (Last name x First name x Zip code).

Through our advanced no-code module, you will be able to use multiple keys for deduplication. This module is available for each master table, meaning that you can adapt the logic to each entity.

{% alert note %} 
For further information about Octolis deduplication, please refer to [our specific help center section][3].
{% endalert %}

### Control over Braze attributes

By default, Braze creates all the attributes that you would send.

This generates two types of issues:

- The attribute's format created automatically by Braze will not match yours.
- You will pay for each additional attribute, even if you don’t use it afterward.

With Octolis, when you create a connection with Braze, you must document the list of fields to be synchronized. 

Thus, Octolis brings more control over the structure of the data entering into Braze and avoids the above-mentioned issues.

## Integration

### Getting started

Before taking advantage of the Octolis and Braze integration, take a few minutes to understand Octolis’ core concepts: Connections, Sources, Audiences, and Syncs.

{% alert note %} 
You will find all of this detailed within our Help Center > [Getting Started” section][4].
{% endalert %}

### Step 1 - Connect Octolis to your data sources

To start sending data to Braze, you first need to make sure that you have [created at least one Audience][5].
An Audience is an entity combining several data Sources, applying them to Preparation steps, and adding Computed fields.

Before sending any kind of data to Braze, you first need to build your first audience based on one or several data sources.

For instance, a *Source* can be one of the following:

- A Salesforce object (contacts, accounts...)
- A Zendesk object (tickets)
- A file inside of an SFTP (CSV file containing some contacts, JSON file containing events...)
- A table/view of a database.
- One of your systems sends us records through Webhooks/API calls.

### Step 2 - Add Braze as a new destination

Once Octolis connected to your data sources and your first Audience created, you are now able to add braze as a new destination.

Within the main screen, select “+ Add more” on top of your current destinations.

<img width="960" alt="Braze_screen1" src="https://user-images.githubusercontent.com/100789766/202801818-ff01da12-af44-4cba-893d-d418dcb7a07b.png">

Select Braze amongst available business tools.

<img width="960" alt="Braze_screen2" src="https://user-images.githubusercontent.com/100789766/202800839-f45ecb09-595b-49c3-a7de-db4a878e2695.png">

Once selected, you must provide :

- Your Braze’s API key. This can be created within the **Braze Dashboard > Developer Console > REST API Key > Create New API Key**
- Time window: The given period on which we will apply the rate limiting.
- Request Volume: Number of requests that you will be able to make within this time frame.
- Custom Attributes: Specify here the new fields that you will send to Braze, their format (String, Integer, float,..), and tick the “Required for syncs” if you want one of them to be mandatory for a sync.

{% alert note %} 
By default, [Braze’s API quota][6] for /users/track requests is 50 000 per minute.
{% endalert %}

<img width="960" alt="Braze_screen3" src="https://user-images.githubusercontent.com/100789766/202801879-6c81d052-e8c3-4c92-81ea-b1f4460300ae.png">

Once configured, Braze will appear as a new destination on the home screen.

### Step 3: Create a new sync

From the left Menu, click on “Syncs”, and select “Add sync” at the top right.
Select the Audience you want to sync amongst the Audiences you have previously created.

### Step 4: Configure your Destination

Select Braze as the Destination and which entity you will send data to.

<img width="963" alt="Braze_screen4" src="https://user-images.githubusercontent.com/100789766/202760588-b9adfbdc-e82e-40e0-b87f-e56fd0288f74.png">

### Step 5: Output settings

![Braze_screen5](https://user-images.githubusercontent.com/100789766/202750534-ce2f739c-090f-4ba1-8211-a38ec2a1eb8f.png)

Here is a specific definition of settings fields.

| Field | Description |
| --- | --- |
| Where do you want to sync the Audience to? | Braze’s entity where you will create or update records. |
| Which field is used to identify a record? | The field that will use Octolis to identify a record if it already exists in Braze. |
| How often do you want to send each record? | By default, for all types of integrations (API, database, ftp) the sync will be incremental. This means that only new values since the last update will be updated. If necessary, you can also send whole tables at regular intervals. On initiation, we will send the complete table. |
| Which fields should be synced? | Octolis to Braze fields mapping. The list of all available fields appears in the drop-down menu. If you want to send a computed field to Braze, you first have to make sure that you created the corresponding column within your Braze entity. |
| When do you want to sync the Audience? | How the data will be sent to Braze: manually, in real-time, or programmed.  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

{% alert note %} 
Why having to choose “Created or updated” for each field?

**Create**: For instance, for opt-ins, it is important that the Braze table remains master. You don't want Octolis to trigger a sync when the field is updated.

**Update**: On the other hand, for a first name field, for example, you want to be able to update the field in your Braze table each time a customer gives you a new entry.{% endalert %}

[0]: http://octolis.com 
[1]: https://www.braze.com/docs/api/endpoints/user_data/post_user_track/
[2]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[3]: https://help.octolis.com/resources/faq/what-is-deduplication-and-how-does-it-work
[4]: https://help.octolis.com/
[5]: https://help.octolis.com/audiences/create-a-no-code-audience
[6]: https://www.braze.com/docs/api/api_limits/
[7]: {% image_buster /assets/img/Octolis/Braze scheme.png %}
