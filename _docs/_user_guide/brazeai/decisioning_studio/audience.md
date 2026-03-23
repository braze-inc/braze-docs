---
nav_title: Define your audience
article_title: Define your audience
page_order: 3
page_type: reference
description: "Learn how to define and configure the audience for your BrazeAI Decisioning Studio agent, including treatment groups and platform-specific setup steps."
---

# Define your audience

> Use case audiences are typically defined in a Customer Engagement Platform (such as Braze or Salesforce Marketing Cloud), then sent to the Decisioning Studio agent. The agent then divides customers into treatment groups in order to conduct randomized controlled trials.

## Treatment groups

| Group | Description |
|-------|-------------|
| **Decisioning Studio** | Customers who receive AI-optimized recommendations |
| **Random Control** | Customers who receive randomly selected options (baseline comparison) |
| **Business-as-Usual (optional)** | Customers who receive the current marketing journey (for comparing against existing performance) |
| **Holdout (optional)** | Customers who receive no communications (to measure overall campaign impact) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Configure your audience

{% tabs %}
{% tab Braze %}

1. Create a segment for your audience that you would like to target.
2. Provide the Segment ID to your AI Decisioning Services team.

{% alert note %}
For Braze, we can ingest multiple segments and combine them to create the audience. Decisioning Studio can ingest a segment for a Business-as-Usual comparator campaign. All of these patterns are acceptable.
{% endalert %}

{% endtab %}
{% tab Salesforce Marketing Cloud %}

1. Configure an SFMC Data Extension(s) for your audience and provide the data extension ID
2. Set up SFMC Installed Package for API integration with the appropriate permissions required by Decisioning Studio
3. Ensure that this data extension is refreshed daily, as Decisioning Studio will pull from the latest incremental data available

Provide the extension ID and API key to the Braze services team. They will assist with next steps in ingesting customer data.

{% endtab %}
{% tab Other Platforms %}

### Google Cloud Storage

If the audience is not currently stored in Braze or Salesforce Marketing Cloud, then the next best step is to configure an automated export directly to a Braze-controlled Google Cloud Services bucket.

To determine whether this is feasible, refer to the documentation for your Martech platform. For example, mParticle offers a [native integration with Google Cloud Storage](https://www.mparticle.com/integration/google-cloud-storage/). If this is the case, we can provide a GCS bucket to export audience data to.

There are similar pages for:
- [Twilio Segment](https://www.twilio.com/docs/segment/connections/storage/catalog/google-cloud-storage)
- [Treasure Data](https://docs.treasuredata.com/int/google-cloud-storage-export-integration)
- [ActionIQ](https://info.actioniq.com/hubfs/ActionIQ%20Industry%20Brief%20Solutions/ActionIQ_Integrations_Brief.pdf)
- [Adobe Experience Platform](https://experienceleague.adobe.com/en/docs/experience-platform/destinations/catalog/cloud-storage/google-cloud-storage)

{% endtab %}
{% endtabs %}

## Next steps

After defining your audience, proceed to set up orchestration:

- [Set up orchestration]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/orchestration_setup/)