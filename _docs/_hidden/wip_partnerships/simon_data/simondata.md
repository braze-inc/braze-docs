---
nav_title: Simon Data
article_title: Simon Data
page_order: 1

description: "Use the Braze and Simon Data integration to create and sync sophisticated audiences to Braze for orchestration, in real-time and without code."
alias: /partners/simon_data/

page_type: partner
search_tag: Partner
hidden: true
layout: dev_guide
---

# Simon Data

> [Simon Data][1] is a customer data platform (CDP) friendly to marketers and trusted by data teams. By transforming your data warehouse into a marketing powerhouse, Simon drives business results and a superior customer experience.
>
> Use the Braze and Simon Data integration to create and sync sophisticated audiences to Braze for orchestration, in real-time and without code. 
>
> With this integration you can leverage the best of Simon's campaign prioritization capabilities, Identity matching capabilities, complex aggregate support and more to elevate your Braze campaigns downstream. 

## Prerequisites

To get started, you need to authenticate your Braze account within your Simon Data account. 

| Requirement         | Description                                                                                                                                                               |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Simon Data          | You must have an existing Simon Data account to leverage the Braze integration from within Simon Data.                                                                    |
| Braze REST API key  | A Braze REST API key with `users.track`, `campaigns.trigger.schedule.create`, and `campaigns.trigger.send` permissions. <br><br> This can be created within the **Braze Dashboard > Developer Console > REST API Key > Create New API Key**. |
| Braze Dashboard URL | [Your REST endpoint URL][1]. Your endpoint will depend on the Braze URL for your instance.                                                                                |

{: .reset-td-br-1 .reset-td-br-2}

## Use cases

- Trigger a canvas or email  
- Pass and Maintain Segment Properties 
- Sync Traits and Contact Properties 

{% alert note %}  
When using the Simon and Braze integration, Simon only sends the changing data on each sync to Braze avoiding costs for irrelevant data. You choose which traits you want to sync, then only the values that have changed for those traits are sent during your pipe refresh; see **Sync Traits and Contact Properties** below.
{% endalert %}

## Integration

### Authenticate your Braze account in Simon

To use the Braze integration first authenticate your Braze account in Simon:

1. From the left navigation, click **Integrations** then scroll to Braze.
2. Enter your Braze [REST API Key][2] and your [Dashboard URL][3].
3. Click **Save Changes**. A successful connection displays **Connected** in the window.

![step_one][8]

### Trigger a canvas or email and/or Pass and Maintain Segment Properties

Once you've authenticated your Braze account in Simon you can add Braze actions to [Flows][4] and [Journeys][5]. Three actions are available:

![BrazeAuthentication][9]

- **Sync Simon Segment Attribute**: sync your segment details with a new or existing custom attribute in Braze.
- **Trigger a Braze Canvas**: trigger a Braze canvas that leverages your Simon segment data.
- **Send a Braze Campaign**: launch an entire Braze campaign from Simon.

Note, some actions are available for only specific Flow types or Journeys alone. Learn more at [docs.simondata.com][6].

### Sync Traits and Contact Properties

Choose specific traits to sync by default so you're only sending relevant data points to Braze and avoid charges for the fields you don't need updated (rather than updating every field for every customer in a segment every time, even if just one of their data points changed). 

To get started with trait syncing, submit a request in the [Simon Support Center][7]. Your account manager will let you know when you can proceed with the following steps. 

Once Contact Traits is activated by your account manager:

1. From the left navigation expand Admin Center then click **Sync Contact Traits**.
2. Choose **Braze**. Contact properties are displayed here, nested by dataset.
3. Check any fields you want synced when you use the Simon and Braze integration:
   1. **Number or traits** indicates how many traits are available to choose from in that dataset. You can choose all, or just individual fields.
   2. Edit the **Downstream name** if you want the field names to appear differently when they arrive in Braze.
   3. Click **Backfill all contacts** if this is your first time integrating with Braze from Simon. Backfilling sends all the data points to Braze the first time you use an action in a flow or journey (step three below) to be sure all your data is fully in sync, then on subsequent syncs only the traits you choose in this screen are sent to Braze (ensure you're only charged for the data you need).

Traits and Contact Properties will re-sync every time the pipe refreshes, based on your selections here. If you don't choose any traits, Simon sends all the data points by default.

![SyncTraits][10]


[1]: https://www.simondata.com

[2]: https://www.braze.com/docs/api/home?redirected=true#creating-and-managing-rest-api-keys

[3]: https://www.braze.com/docs/api/basics#api-definitions

[4]: https://docs.simondata.com/docs/campaigns-flows

[5]: https://docs.simondata.com/docs/campaigns-journeys-two

[6]: https://docs.simondata.com

[7]: https://docs.simondata.com/docs/support-center

[8]: {% image_buster /assets/img/simon_data/ConnecttoBraze.png %}  
[9]: {% image_buster /assets/img/simon_data/BrazeActions.png %}  
[10]: {% image_buster /assets/img/simon_data/BrazeTraitSyncing.png %}
