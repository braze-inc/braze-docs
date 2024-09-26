---
nav_title: B2B Data Models
article_title: Creating a B2B Data Model
description: "Learn how to use Braze data tools to create B2B models."
---

# Creating a B2B data model

> This collection of use cases demonstrates how you can use Braze data tools to create an effective and efficient B2B data model that helps you target, trigger, personalize, and send messages to your business users. 

Some use cases include:

- Mapping sales customer relationship management (CRM) IDs to Braze
- Using Braze catalogs and catalogs API or catalogs Cloud Data Ingestion (CDI) to frequently update information about your accounts and opportunities
- Using Connected Content and Braze CDI segments to directly query your data warehouse for data about accounts and opportunities 

Before we cover the use cases, let's go over several concepts and terms you should know.

There are four primary B2B objects that you need to execute B2B campaigns.

| Object | Description |
| --- | --- |
| Leads | A record of potential customers who have shown interest in a product or service but haven't yet been qualified as an opportunity. |
| Contacts | Typically, individuals who have been qualified and converted from a lead to a contact to pursue a sales opportunity. |
| Opportunities | A record that tracks the details of a potential sale or deal in progress
| Accounts | A record of an organization that is a qualified potential customer, an existing customer, a partner, or a competitor who has a relationship of similar significance. |
{: .reset-td-br-1 .reset-td-br-2 }

Within Braze, we think of these as two buckets.

| Bucket | Description |
| --- | --- |
| User profiles | These map directly to leads and contacts in your sales CRM system. Because leads are captured by Braze, they are automatically created as leads in your sales CRM system. As they are converted to contacts, that contact’s ID and details sync back to Braze. |
| Business objects | These map to any non-user objects in your sales CRM system. This includes your sales specific objects, such as account objects and opportunity objects. |
{: .reset-td-br-1 .reset-td-br-2 }

## Use cases for user profiles

User profiles are the primary object in Braze, which power the majority of your demographic segmentation, triggering and personalization. User profiles include [default user data]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/) collected by our SDK and other sources, including [custom data]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/), which takes the form of either attributes (demographic data), events (behavioral data) or purchases (transactional data).

### Mapping sales CRM IDs to Braze

The following table is how we suggest you map your sales CRM ID fields back to the Braze user object.

#### Braze object: User

| CRM field | CRM object (Salesforce) | Braze field |
| --- | --- | --- |
| `Aliases.salesforce_lead_id` | Lead | `id` |
| `Aliases.salesforce_contact_id` | Contact | `id` |
| `AccountId` | Contact | `AccountId` |
| `OpportunityId` (optional, scalar) <br>or<br> `Opportunities` (optional, array) | Opportunity | `id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 }

{% alert note %}
We recommendd using [aliases]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases) instead of `external_id` to map Salesforce lead and contact identifiers back to Braze. This is because most of our users will create their own (non-CRM specific) UUID for their own users when they log into their profiles to access their platform. This UUID is typically the preferred `external_id` in Braze because it reduces the amount of lookups required when identifying and running product-led growth style initiatives.
{% endalert %}

## Use cases for business objects

Business objects are any non-user centric dataset. In a B2B context, these include your account and opportunity data, and any other pertinent non-user centric dataset that your company tracks. 

There are two methods to create and manage your business objects in Braze. 

| Method | Description |
| --- | --- |
| [Catalogs]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs) | These are independent data objects (supplemental data objects) on the primary user profile in Braze. In a B2B context, you would likely have catalogs for your accounts and opportunities. |
| [Connected sources]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/connected_sources/) | These allow Braze to directly query your data warehouse. You're likely already syncing your lead, contact, opportunity, and account objects to your data warehouse on a regular basis, so you can point Braze segmentation directly to that warehouse and activate it in a zero-copy environment. |
{: .reset-td-br-1 .reset-td-br-2 }

### Using catalogs for accounts and opportunities

[Catalogs]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/) are data tables that are hosted and managed in Braze. While account and opportunity data originates from your sales CRM system of choice, you would be duplicating these in Braze to be used for marketing purposes: account-based segmentation, account-based marketing, lead management, and more. 

We recommend creating one catalog for your accounts and one for your opportunities, and updating them frequently by sending Braze updates through our catalogs API or catalogs Cloud Data Ingestion (CDI). When creating these catalogs, make sure the `id` (first column) of your catalog matches the `id` in your sales CRM system. 

#### Braze object: Catalog > Account catalog

| CRM field | CRM object (Salesforce) | Braze field |
| --- | --- | --- |
| `id` | Account | `id` |
| `AccountName` | Account | `AccountName` |
| `Type` | Account | `Type` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 }

#### Braze object: Catalog > Opportunity catalog

| CRM field | CRM object (Salesforce) | Braze field |
| --- | --- | --- |
| `id` | Opportunity | `id` | 
| `OpportunityName` | Opportunity | `OpportunityName` |
| `Territory` | Opportunity | `Territory` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 }

#### Relating business objects to user profiles

Now that your opportunity and account details are ccounted for as Braze catalogs, you need to create a relationship between those catalogs and the user profiles you want to send messages to. Currently, this requires two steps:

1. Include the account, opportunity ID, or both on the user profile as attributes. We recommend you use these name formats:
    - For accounts: `[ AcctId1, AcctId2 ]`
    - For opportunities: `OppId`
2. Log an event (such as `account_linked`) which includes the account ID as an event property.

```json
{
  "events" : [
    {
      "external_id" : "user1",
      "name" : "account_linked",
      "time" : "2013-07-16T19:20:45+01:00",
      "properties": {
        "account_id": "xyz123
      }
    }
  ]
}
```

### Using Connected Content for accounts and opportunities

Connected sources are data tables that are hosted by you in your own data warehouse and queried by Braze CDI segments. Unlike catalogs, instead of replicating your business objects (accounts and opportunities) in Braze, you're keeping them in your data warehouse and using your warehouse as the source of truth. 

To set up connected sources, refer to [Integrating connected sources]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/connected_sources#integrating-connected-sources).

#### Relating business objects to user profiles

One of your connected source’s tables should include a `user_id` that matches the `external_user_id` set in Braze for your users. The user profile setup above will use your lead and `contact_id`s as your `external_id`, so you should ensure your `lead/contact` tables include these IDs. 