---
nav_title: Octolis
article_title: Octolis
description: "Octolis is a data activation platform that allows you to integrate your data into Braze."
alias: /partners/octolis/
page_type: partner
search_tag: Octolis

---

# Octolis

> [Octolis][0] is a powerful data activation platform (or headless CDP). Sitting on top of a database you own, Octolis is an easy way to unify, prepare, score and sync data in your business tools.

The Braze and Octolis integration acts as middleware between your raw data sources and Braze, enabling you to retrieve and unify data from various sources, online and offline:
1. Unify and combine data from sources such as Eshop, CRM, POS system, etc.
2. Normalize and score
3. Real-time synchronization of computed fields and events to Braze

![][7]

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Octolis account | An Octolis account is required to take advantage of this partnership. |
| Braze REST API key | A Braze REST API key with [**users.track**][1] permissions. <br><br> This can be created within the **Braze Dashboard > Developer Console > REST API Key > Create New API Key**. |
| Braze REST endpoint | [Your REST endpoint URL][2]. Your endpoint will depend on the Braze URL for your instance. |
| Braze app key | Your app identifier key. This can be found within the **Braze Dashboard > Manage Settings > API Key**. |
{: .reset-td-br-1 .reset-td-br-2}

## Integration

Before beginning the integration, refer to the following sections on connections, sources, audiences, and syncs.

For more information, refer to the Octolis [Getting started][4] section.

### Step 1: Connect Octolis to your data sources

To send data to Braze, you must ensure that you have created at least one [audience][5]. An audience combines several data sources, applies them to preparation steps, and adds computed fields.

These audiences need to be built based on several data sources. A source can be any of the following:
- A Salesforce object (contacts, accounts, etc.)
- A Zendesk object (tickets)
- A file inside of an SFTP (CSV file containing some contacts, JSON file containing events...)
- A table/view of a database.
- One of your systems sends us records through webhooks or API calls.

### Step 2: Add Braze as a destination

Next, to set Braze as a new destination, select **+ Add more** at the top of your current destination within the main screen and select **Braze** from the available business tools.

![][9]

Once selected, provide the following:

- Your Braze's API key: This can be created within the **Braze Dashboard > Developer Console > REST API Key > Create New API Key**
- Time window: Octolis will apply the rate limiting in the given period.
- Request volume: Number of requests you can make within this time frame.
- Custom attributes: Specify here the new fields you will send to Braze, their format (string, integer, float), and tick the **Required for syncs** if you want one of them to be mandatory for a sync.

![][10]

Once configured, Braze will appear as a new destination on the home screen.

### Step 3: Create a new sync

From the menu, click **Syncs** and select **Add sync** at the top right. Select the audience you want to select from the audience you have previously created.
Next, select **Braze** as the destination and which entity you will send data to.

![][11]

### Step 4: Set output settings

By default, Braze creates all the attributes that you would send, but you must document the list of fields to be synchronized.

![][12]{: style="max-width:75%;"}

Here is a specific definition of settings fields.

| Field | Description |
| --- | --- |
| Where do you want to sync the audience to? | Braze's entity where you will create or update records. |
| Which field is used to identify a record? | The field will use Octolis to identify a record if it already exists in Braze. |
| How often do you want to send each record? | By default, the sync will be incremental for all integrations (API, database, FTP). This means that only new values since the last update will be updated. If necessary, you can also send whole tables at regular intervals. On initiation, Octolis will send the complete table. |
| Which fields should be synced? | Octolis to Braze fields mapping. The list of all available fields appears in the drop-down menu. To send a computed field to Braze, you must first ensure that you created the corresponding column within your Braze entity. |
| When do you want to sync the audience? | How the data will be sent to Braze: manually, in real-time, or programmed.  |
| Sync when record is... | Create: For opt-ins, it is important that the Braze table remains master. You don't want Octolis to trigger a sync when the field is updated.<br><br>Update: On the other hand, for a first name field, for example, you want to be able to update the field in your Braze table each time a customer gives you a new entry. |
{: .reset-td-br-1 .reset-td-br-2}

## Multi-keys deduplication

Deduplication is a major challenge when reconciling data from multiple sources, especially online and offline. Through Octolis's advanced no-code module, you can use multiple keys for [deduplication][3]. This module is available for each master table, meaning you can adapt the logic to each entity.

[0]: http://octolis.com
[1]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[2]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[3]: https://help.octolis.com/resources/faq/what-is-deduplication-and-how-does-it-work
[4]: https://help.octolis.com/
[5]: https://help.octolis.com/audiences/create-a-no-code-audience
[6]: {{site.baseurl}}/api/api_limits/
[7]: {% image_buster /assets/img/Octolis/Braze_scheme.png %}
[8]: {% image_buster /assets/img/Octolis/Braze_screen1.png %}
[9]: {% image_buster /assets/img/Octolis/Braze_screen2.png %}
[10]: {% image_buster /assets/img/Octolis/Braze_screen3.png %}
[11]: {% image_buster /assets/img/Octolis/Braze_screen4.png %}
[12]: {% image_buster /assets/img/Octolis/Braze_screen5.png %}
