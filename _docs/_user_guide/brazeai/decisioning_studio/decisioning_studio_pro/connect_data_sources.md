---
nav_title: Connect data sources
article_title: Connect data sources
page_order: 1
description: "Learn how to connect customer data sources to BrazeAI Decisioning Studio Pro for personalized AI decisioning."
---

# Connect data sources

> BrazeAI Decisioning Studio™ Pro agents need to fully understand customer context in order to make effective decisions. This article explains how to connect customer data sources to Decisioning Studio Pro.

{% alert tip %}
Your AI Decisioning Services team will support you in configuring data connections for optimal performance.
{% endalert %}

## Supported integration patterns

Decisioning Studio Pro supports multiple integration patterns for connecting customer data:

| Integration pattern | Best for | Setup complexity |
|---------------------|----------|------------------|
| **Braze Data Platform** | Customers already using Braze | Low |
| **Braze Cloud Data Ingestion (CDI)** | Connecting external data warehouses | Medium |
| **Cloud Storage (GCS, AWS, Azure)** | Direct data exports from other platforms | Medium |
| **CEP integrations** | SFMC, Klaviyo data extensions | Medium |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

## Customer data types

The following customer data assets help agents personalize more effectively:

| Data type | Description | Examples |
|-----------|-------------|----------|
| **Customer profile** | Static and slowly-changing attributes | Years as customer, geography, acquisition channel, satisfaction level, lifetime value estimate |
| **Customer behavior** | Activity and engagement patterns | Account logins, device type, customer service interactions, product usage |
| **Transaction history** | Purchase and conversion data | Products purchased, transaction amounts, payment methods, purchase channels |
| **Marketing engagement** | Responses to communications | Email opens/clicks, SMS engagement, web and mobile activity, survey responses |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

{% alert tip %}
The more information agents have about your customers, the better they will perform. Consider including data on any insights that would be particularly important to your business (for example, do you want to see how AI treats your loyalty customers differently? Make sure loyalty status is in the customer data).
{% endalert %}

## Connecting data by platform

{% tabs %}
{% tab Braze %}

### Send customer data through Braze

BrazeAI Decisioning Studio can use all data that you are already sending to the Braze Data Platform.

If there is customer data that you want to use for Decisioning Studio that is not currently stored in the user profile or custom attributes, the recommended approach is to use [Braze Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion) to ingest data from other sources.

CDI supports direct integrations with:

- Snowflake
- Redshift
- BigQuery
- Databricks
- Microsoft Fabric
- AWS S3

For the full list of supported sources, see [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion).

Once you are satisfied with the data you are sending into the Braze Data Platform, contact your AI Decisioning Services team to discuss which fields on the user profile or custom attributes should be used for AI Decisioning.

To streamline this process, create a list of Braze user profile attributes that you think best represent your customers' behaviors that should be used in Decisioning Studio (see the [list of available fields]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/#fields-to-export)). Your services team can also help you conduct discovery sessions to decide which fields are most appropriate for AI Decisioning.

Other options for sending data include:

- Sending Braze custom events via the SDK
- Sending events using the REST endpoint ([`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track))

These patterns require more engineering effort, but are sometimes preferable depending on your current Braze configuration. Reach out to the AI Decisioning Services team to learn more.

{% endtab %}
{% tab SFMC %}

### Send customer data through SFMC

For Salesforce Marketing Cloud integrations:

1. Configure SFMC Data Extension(s) for your customer data
2. Set up SFMC Installed Package for API integration with the appropriate permissions required by Decisioning Studio
3. Ensure that data extensions are refreshed daily, as Decisioning Studio will pull from the latest incremental data available

Provide the extension ID and API key to your AI Decisioning Services team. They will assist with next steps in ingesting customer data.

{% endtab %}
{% tab Klaviyo %}

### Send customer data through Klaviyo

For Klaviyo integrations:

1. Confirm customer profile data is available in Klaviyo profiles
2. Generate a private API key with Full Access to Profiles
3. Provide the API key to your AI Decisioning Services team

See the [Klaviyo documentation](https://help.klaviyo.com/hc/en-us/articles/115005237908) for more information on API key setup.

{% endtab %}
{% tab Cloud Storage %}

### Other cloud solutions (Google Cloud Storage, Azure, AWS)

If customer data is not currently stored in Braze, SFMC, or Klaviyo, the next best step is to configure an automated export directly to a Braze-controlled Google Cloud Storage bucket. We can also support export to AWS or Azure (although GCS is preferable). For these platforms, export to their internal cloud storage in those cloud platforms and Braze can then pull that data.

To determine whether this is feasible, refer to the documentation for your Martech platform. For example:

- mParticle offers a [native integration with Google Cloud Storage](https://www.mparticle.com/integration/google-cloud-storage/)
- [Twilio Segment](https://www.twilio.com/docs/segment/connections/storage/catalog/google-cloud-storage)
- [Treasure Data](https://docs.treasuredata.com/int/google-cloud-storage-export-integration)
- [ActionIQ](https://info.actioniq.com/hubfs/ActionIQ%20Industry%20Brief%20Solutions/ActionIQ_Integrations_Brief.pdf)
- [Adobe Experience Platform](https://experienceleague.adobe.com/en/docs/experience-platform/destinations/catalog/cloud-storage/google-cloud-storage)

If this is feasible, we can provide a GCS bucket to export customer data to that is isolated to Decisioning Studio.

{% endtab %}
{% endtabs %}

## Best practices

- **Descriptive column names**: Customer data should have clear, descriptive column names. Ideally, a data dictionary should be provided.
- **Incremental updates**: Incremental files are preferable versus snapshots of the whole customer history every day
- **Consistent identifiers**: Each record must contain a unique customer identifier that is consistent across all data assets
- **Include timestamps**: Records should have associated timestamps for accurate attribution and agent training

## Custom integrations

Other options or completely custom data pipelines are possible. These may require additional Services work or Engineering work from your team. To determine what is feasible and optimal, work with your AI Decisioning Services team.

{% alert important %}
This guide explains the most common integration patterns. Information Security will still need to vet all connection points and Solutions Consultants will be available to advise on the implementation.
{% endalert %}

## Next steps

After connecting your data sources, proceed to set up orchestration:

- [Set up orchestration]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_pro/set_up_orchestration/)

