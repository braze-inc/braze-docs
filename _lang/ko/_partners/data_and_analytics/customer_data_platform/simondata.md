---
nav_title: Simon Data
article_title: Simon Data
description: "Use the Braze and Simon Data integration to create and sync sophisticated audiences to Braze for orchestration, in real-time and without code."
alias: /partners/simon_data/
page_type: partner
search_tag: Partner
---

# Simon Data

> [Simon Data](https://www.simondata.com) is a customer data platform (CDP) friendly to marketers and trusted by data teams. By transforming your data warehouse into a marketing powerhouse, Simon drives business results and a superior customer experience.

Use the Braze and Simon Data integration to create and sync sophisticated audiences to Braze for orchestration, in real-time and without code. With this integration you can leverage the best of Simon's campaign prioritization and Identity matching capabilities, complex aggregate support, and more to elevate your Braze campaigns downstream.

## Prerequisites

To get started, you need to authenticate your Braze account within your Simon Data account.

| Requirement         | Description                                                                                                                                                               |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Simon Data          | You must have an existing Simon Data account to leverage the Braze integration from within Simon Data.                                                                    |
| Braze REST API key  | A Braze REST API key with `users.track`, `campaigns.trigger.schedule.create`, and `campaigns.trigger.send` permissions. <br><br> This can be created in the Braze dashboard from **Settings** > **API Keys**. |
| Braze Dashboard URL | [Your REST endpoint URL]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints). Your endpoint will depend on the Braze URL for your instance.                                                                                |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Use cases

- Trigger a Braze Canvas or email  
- Pass and maintain Segment Properties
- Sync Traits and Contact Properties

{% alert note %}  
When using the Simon and Braze integration, Simon only sends deltas on each sync to Braze avoiding costs for irrelevant data. See [Sync Traits and Contact Properties](#sync-traits-and-contact-properties) for more.
{% endalert %}

## Integration

### Authenticate your Braze account in Simon

To use the Braze integration, first authenticate your Braze account in Simon:

1. From the left navigation, click **Integrations** then scroll to Braze.
2. Enter your Braze [REST API key]({{site.baseurl}}/api/basics/#creating-and-managing-rest-api-keys) and your [dashboard URL]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints).
3. Click **Save Changes**.

A successful connection displays **Connected** in the window.

![Integration screen in Simon Data]({% image_buster /assets/img/simon_data/ConnecttoBraze.png %}){: style="max-width:70%"}

### Add Braze actions to Flows or Journeys in Simon

After you've authenticated your Braze account in Simon you can add Braze actions to [Flows](https://docs.simondata.com/docs/campaigns-flows) and [Journeys](https://docs.simondata.com/docs/campaigns-journeys-two).

Three actions are available:

- **Sync Simon segment attribute**: Sync your segment details with a new or existing custom attribute in Braze.
- **Trigger a Braze Canvas**: Trigger a Braze Canvas that leverages your Simon segment data.
- **Send a Braze campaign**: Launch an entire Braze campaign from Simon.

![Dropdown showing list of available Braze actions in Simon Data.]({% image_buster /assets/img/simon_data/BrazeActions.png %}){: style="max-width:60%"}

Some actions are only available for specific Flow types or Journeys alone. Learn more at [docs.simondata.com](https://docs.simondata.com).

### Sync traits and contact properties

To minimize data consumption, you can choose specific traits to sync by default, rather than updating every field for all customers in a segment.

{% alert note %}
To get started with trait syncing, submit a request in the [Simon Support Center](https://docs.simondata.com/docs/support-center). Your account manager will let you know when you can proceed with the following steps.
{% endalert %}

After Contact Traits is activated by your account manager:

1. In Simon, expand **Admin Center** in the left navigation and select **Sync Contact Traits**.
2. Choose **Braze**. Contact properties are displayed here, nested by dataset.
3. Select any fields you want synced when you use the Simon and Braze integration:
   1. **Number or traits** indicates how many traits are available to choose from in that dataset. You can choose all or expand the row to select individual fields.
   2. Edit the **Downstream name** if you want the field names to appear differently when they arrive in Braze.
   3. If this is your first time integrating with Braze from Simon, click **Backfill all contacts**. Backfilling sends all the data points to Braze the first time you use an action in a flow or journey to be sure all your data is fully in sync. Then on subsequent syncs, only the traits you choose in this screen are sent to Braze. This helps to make sure you're only charged for the data you need.

![Selecting sync traits in Simon Data.]({% image_buster /assets/img/simon_data/BrazeTraitSyncing.png %})





