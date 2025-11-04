---
nav_title: Data models
article_title: Creating a B2B Data Model
page_order: 0
page_type: reference
description: "Learn how to use Braze data tools to create B2B models."
---

# Creating a B2B data model

> This use case demonstrates how you can use Braze data tools to create an effective and efficient B2B data model that helps you target, trigger, personalize, and send messages to your business users. 

{% alert note %}
These recommendations may change over time as Braze builds out our B2B capabilities.
{% endalert %}

Before we get into how you can set up your B2B data model, let’s go over several concepts and terms you should know.

There are four primary B2B objects that you need to execute B2B campaigns.

| Object | Description |
| --- | --- |
| Leads | A record of potential customers who have shown interest in a product or service but haven't yet been qualified as an opportunity. |
| Contacts | Typically, individuals who have been qualified and converted from a lead to a contact to pursue a sales opportunity. |
| Opportunities | A record that tracks the details of a potential sale or deal in progress
| Accounts | A record of an organization that is a qualified potential customer, an existing customer, a partner, or a competitor who has a relationship of similar significance. |
{: .reset-td-br-1 .reset-td-br-2 }

Within Braze, these four objects are combined and reduced into two objects: user profiles and business objects.

| Braze B2B object | Description | Original B2B objects  |
| --- | --- | --- |
| User profiles | These map directly to leads and contacts in your sales CRM system. Because leads are captured by Braze, they are automatically created as leads in your sales CRM system. As they are converted to contacts, the contact IDs and details sync back to Braze. |Leads<br> Contacts |
| Business objects | These map to any non-user objects in your sales CRM system. This includes your sales specific objects, such as account objects and opportunity objects. | Accounts<br> Opportunities |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Step 1: Create your business objects in Braze

Business objects are any non-user centric dataset. In a B2B context, these include your account and opportunity data, and any other pertinent non-user centric dataset that your company tracks.

There are two methods to create and manage your business objects in Braze, catalogs and connected sources. 

| Method | Description |
| --- | --- |
| [Catalogs]({{site.baseurl}}/user_guide/data/activation/catalogs) | These are independent data objects (supplemental data objects) on the primary user profile in Braze. In a B2B context, you would likely have catalogs for your accounts and opportunities. |
| [Connected sources]({{site.baseurl}}/user_guide/data/cloud_ingestion/connected_sources/) | These allow Braze to directly query your data warehouse. You're likely already syncing your lead, contact, opportunity, and account objects to your data warehouse on a regular basis, so you can point Braze segmentation directly to that warehouse and activate it in a zero-copy environment. |
{: .reset-td-br-1 .reset-td-br-2 }

{% tabs %}
{% tab Catalogs %}

### Option 1: Use catalogs for accounts and opportunities

Catalogs are data tables that are hosted and managed in Braze. While account and opportunity data originates from your sales CRM system of choice, you would be duplicating these in Braze to be used for marketing purposes: account-based segmentation, account-based marketing, lead management, and more.

For this option, we recommend creating one catalog for your accounts and one for your opportunities, and updating them frequently by sending Braze updates through our [catalogs API]({{site.baseurl}}/api/endpoints/catalogs/) or [catalogs Cloud Data Ingestion (CDI)]({{site.baseurl}}/user_guide/data/cloud_ingestion/sync_catalogs_data/). When creating these catalogs, make sure the `id` (first column) of your catalog matches the `id` in your sales CRM system.

#### Map over your CRM fields

The tables below include a few examples of fields you can map over from your CRM’s account and opportunity objects.

{% subtabs %}
{% subtab Account catalog %}

In this use case, Salesforce is the example CRM system. You can map over any field that is included in your CRM's objects.

<table border="1">
  <tr>
    <th><b>Braze object</b></th>
    <th><b>Braze field</b></th>
    <th><b>CRM object (Salesforce)</b></th>
    <th><b>CRM field (Salesforce)</b></th>
  </tr>
  <tr>
    <td rowspan="4">Catalog &gt; Account catalog</td>
    <td><code>id</code></td>
    <td><code>account</code></td>
    <td><code>id</code></td>
  </tr>
  <tr>
    <td><code>AccountName</code></td>
    <td><code>account</code></td>
    <td><code>Account Name</code></td>
  </tr>
  <tr>
    <td><code>Type</code></td>
    <td><code>account</code></td>
    <td><code>Type</code></td>
  </tr>
  <tr>
    <td><code>OTHER_FIELDS</code></td>
    <td><code>account</code></td>
    <td><code>OTHER_FIELDS</code></td>
  </tr>
</table>

##### Example table of mapped account fields

![Table of Salesforce accounts with respective information, such as billing address and account owner.]({% image_buster /assets/img/b2b/sf_accounts.png %})

{% endsubtab %}
{% subtab Opportunity catalog %}

In this use case, Salesforce is the example CRM system. You can map over any field that is included in your CRM's objects.

<table border="1">
  <tr>
    <th><b>Braze object</b></th>
    <th><b>Braze field</b></th>
    <th><b>CRM object (Salesforce)</b></th>
    <th><b>CRM field (Salesforce)</b></th>
  </tr>
  <tr>
    <td rowspan="4">Catalog &gt; Opportunity catalog</td>
    <td><code>id</code></td>
    <td><code>opportunity</code></td>
    <td><code>id</code></td>
  </tr>
  <tr>
    <td><code>OpportunityName</code></td>
    <td><code>opportunity</code></td>
    <td><code>Opportunity Name</code></td>
  </tr>
  <tr>
    <td><code>Territory</code></td>
    <td><code>opportunity</code></td>
    <td><code>Territory</code></td>
  <tr>
    <td><code>OTHER_FIELDS</code></td>
    <td><code>opportunity</code></td>
    <td><code>OTHER_FIELDS</code></td>
  </tr>
  </tr>
</table>

##### Example table of mapped opportunity fields

![Table of Salesforce opportunities with respective information, such as billing address and account owner.]({% image_buster /assets/img/b2b/sf_opportunities.png %})

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Connected sources %}

### Option 2: Use connected sources for accounts and opportunities

Connected sources are data tables that are hosted by you in your own data warehouse and queried by Braze [CDI Segment Extensions]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/cdi_segments/). Unlike catalogs, instead of duplicating your business objects (accounts and opportunities) in Braze, you’d be keeping them in your data warehouse and using your warehouse as the source of truth.

To set up connected sources, refer to [Integrating connected sources]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/connected_sources#integrating-connected-sources).

{% endtab %}
{% endtabs %}

## Step 2: Relate your business objects to user profiles

User profiles are the primary object in Braze, which power the majority of your demographic segmentation, triggering and personalization. User profiles include [default user data]({{site.baseurl}}/user_guide/data/user_data_collection/) collected by our SDK and other sources, including [custom data]({{site.baseurl}}/user_guide/data/custom_data/), which takes the form of either attributes (demographic data), events (behavioral data) or purchases (transactional data).

### Step 2.1: Map sales CRM IDs to Braze

First, make sure Braze and your CRM of choice have a common identifier to share data to. We suggest using the following table to map your sales CRM ID fields back to the Braze user object. The table below has Salesforce as the CRM system, but this can be done with any CRM.

#### Braze object: User

| Braze field | CRM object (Salesforce) | CRM field (Salesforce) | Additional information |
| --- | --- | --- | --- |
| `Aliases.salesforce_lead_id` | Lead | `id` |  - User alias label: `salesforce_lead_id` <br>- User alias name: `lead_id`|
| `Aliases.salesforce_contact_id` | Contact | `id` | - User alias label: `salesforce_contact_id` <br>- User alias name: `contact_id` |
| `AccountId` | Contact | `AccountId` | 
| `OpportunityId` (optional, scalar) <br>or<br> `Opportunities` (optional, array) | Opportunity | `id` | 
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 }

{% alert note %}
We recommend using [aliases]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases) instead of `external_id` to map Salesforce lead and contact identifiers back to Braze. This is because it reduces the amount of lookups required when identifying and running your product-led growth style initiatives.
{% endalert %}

After you have your IDs in sync, you need to relate your Braze user profiles with your business objects. 

### Step 2.2: Create a relationship between user profiles and your business objects

{% tabs %}
{% tab Catalogs %}

#### Option 1: When using catalogs

Now that your opportunity and account details are accounted for as Braze catalogs, you need to create a relationship between those catalogs and the user profiles you want to send messages to. Currently, this requires two steps:

1. Include the account (such as `account_id (string)`), opportunity ID (such as `opportunity_ids (array)`), or both on the user profile as attributes.
2. Log an event (such as `account_linked`) that includes the account ID as an event property.

```json
{
  "attributes" : [
    {
      "external_id" : "user1",
      "accountId" : "001J7000004K7AF",
      "opportunityIds" : [
"0064J000004EU59",
"0064J000004EU5G"
]
    }
  ],
  "events" : [
    {
      "external_id" : "user1",
      "name" : "account_linked",
      "time" : "2013-07-16T19:20:45+01:00",
      "properties": {
        "account_id": "001J7000004K7AF"
      }
    }
  ]
}
```

{% endtab %}
{% tab Connected sources %}

#### Option 2: When using connected sources

One of your connected source’s tables should include a `user_id` that matches the `external_user_id` set in Braze for your users. The user profile setup above uses your lead and `contact_ids` as your `external_id`, so you should ensure your lead/contact tables include these IDs.

In addition to ensuring the IDs match, we recommend writing basic account-level data such as `account_id`, `opportunity_id`, and even common firmographic attributes such as `industry` to the user profiles for efficient segmentation and personalization.

{% endtab %}
{% endtabs %}