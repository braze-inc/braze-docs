---
page_order: 4.2
nav_title: Set Customer Context
article_title: Set Customer Context
description: "Learn how to configure customer context for Decisioning Studio Pro agents, including audience definition and customer data."
---

# Set Customer Context

> The first step to creating the self-learning AI cycle is configuring customer data. This includes both selecting the audience for your campaign and configuring customer data to be sent to the agents.

The first step to creating the self-learning AI cycle is configuring customer data. This includes both selecting the audience for your campaign and configuring customer data to be sent to the agents.

## Step 1: Define the audience

The first step is configuring the audience for your customer engagement.

As the agent ingests the audience, it separates customers into treatment groups in order to conduct randomized controlled trials. These treatment groups will include, at minimum, a Decisioning Studio group and a Random Control.

It may also include a Business-as-Usual group which allows you to test agent performance against the current marketing journey, and/or a Holdout group, to test how customers perform when they receive no communications from the campaign at all.

## Step 2: Send additional customer data to Decisioning Studio

The second step is to configure customer data to be sent to Decisioning Studio. In order to effectively personalize customer engagement, agents need to understand as much as possible about your customers.

Here are some examples of customer data that is especially helpful.

{% alert important %}
Note that conversions are engagement data required in order to set up the self-learning feedback loop for agents and are especially important. For more information on how to properly validate, consider the [Create the Feedback Loop]({{site.baseurl}}/user_guide/brazeai/decisioning_studio_pro/create_feedback_loop/) section.
{% endalert %}

* **[Required]** Conversions – needed to train AI models and calculate the success metric. Should include the value of each conversion (e.g., revenue) if relevant.

* **[Required]** Activation and engagement data – what was actually sent through each channel based on Decisioning Studio's recommendations and any subsequent customer actions associated with the triggered marketing event (e.g. send, open, click).

* **Customer profile** – years as customer; geography, if allowed in this industry; acquisition channel (e.g., web, phone); satisfaction level; model scores (e.g., churn propensity); lifetime value estimate

* **Customer behavior** – account logins; device type and operating system used for logins; customer service interactions (e.g., number of calls, topics); product usage (e.g., hours used per day, features accessed, categories viewed)

* **Other transactions** – products purchased by date (including product attributes); transaction amounts; transaction channels (e.g., in-store, online); payment methods

* **Other marketing engagement** – outbound communications sent (e.g., emails, SMS); email engagement (e.g., opens, clicks); survey responses (e.g., NPS, engagement); web and mobile app activity (e.g., pages browsed/products viewed)

### Best practices

* Customer data should have descriptive column names
* Incremental snapshots are preferable, vs. the whole customer history every day
* Include customer data on any insights that would be particularly important to your business (e.g., Do you want to see who self-learning AI treats your loyalty customers differently? Make sure it's in the customer data!)

## Integration patterns

### Braze Segment and Braze Data Platform (best case scenario)

The simplest and best approach is to choose a Braze segment for your agent. Provide the following information to the AI Decisioning Services team:

#### To define the audience:

* Create a segment for the audience that you would like to target
* Provide the Segment ID to your AI Decisioning Services team.

#### To send customer data from Braze:

In general, BrazeAI Decisioning Studio can use all data that you are already sending to the Braze Data Platform.

If there is customer data that you would want to use for Decisioning Studio that is not currently stored in the Customer Profile or Custom Attributes, make sure to use [Braze Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion) to ingest data from other sources.

CDI supports any of direct integrations, including:

* Snowflake
* Redshift
* BigQuery
* Databricks
* Microsoft Fabric

Once you are satisfied with the data you are sending into the Braze Data Platform, contact your AI Decisioning Services team to discuss which fields on the Customer Profile and Custom Attributes should be used for AI Decisioning.

To streamline this process, please create a list of Braze user profile attributes that you think best represent your customers' behaviors that should be used in Decisioning Studio (see the [list of available fields]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/#fields-to-export)). Your services team can also help you conduct discovery sessions with you to decide which fields are most appropriate for AI Decisioning.

### Salesforce Marketing Cloud (SFMC)

Decisioning Studio is able to accept an SFMC data extension as the audience as well. Decisioning Studio uses the available REST and SOAP API interfaces provided by SFMC to interact with the platform.

#### To define the audience:

In order to do this, take the following steps:

* Configure an SFMC data extension(s) for your audience and provide the data extension ID
* Set up SFMC Installed Package for API integration with the appropriate permissions required by Decisioning Studio
* Ensure that this data extension must be refreshed daily, as Decisioning Studio will pull from the the latest incremental data available

Provide the extension ID and API key to the Braze services team. They will assist with next steps.

#### To send customer data:

Send via the data extension, use [Braze Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion), or push to Google Cloud Storage.

CDI is the best-supported solution, and supports any of direct integrations, including:

* Snowflake
* Redshift
* BigQuery
* Databricks
* Microsoft Fabric

{% alert note %}
This may require mapping identifier fields from non-Braze sources to the Braze user identifiers, so that customer data can be associated with the correct Braze user profile.
{% endalert %}

### Klaviyo

#### To define the audience

Decisioning Studio is also able to accept Klaviyo segments. To configure Klaviyo integration:

* Create an audience segment
* Generate a private API key and provide this to the Braze AI Decisioning team
* Provide the segment ID and API key to the Braze services team

See the [Klaviyo documentation](https://help.klaviyo.com/hc/en-us/articles/115005237908) for more information on how to take these steps.

#### To send customer data:

Send via the audience segment, use [Braze Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion), or push to Google Cloud Storage.

CDI is the best-supported solution, and supports any of direct integrations, including:

* Snowflake
* Redshift
* BigQuery
* Databricks
* Microsoft Fabric

### Other - Cloud Solutions (Google Cloud Storage, Azure, and AWS)

Finally, if the audience is not currently stored in Braze, SFMC, or Klaviyo, then the next best step is to configure an automated export directly to a Braze-controlled Google Cloud Services bucket. We can also support export to AWS or Azure (although GCS is preferable).

To determine whether this is feasible, refer to the documentation for your Martech platform. For example, mParticle offers a [native integration with Google Cloud Storage](https://www.mparticle.com/integration/google-cloud-storage/). If this is the case, we can provide a GCS bucket to export audience data to. There are similar pages for [Twilio Segment](https://www.twilio.com/docs/segment/connections/storage/catalog/google-cloud-storage), [Treasure Data](https://docs.treasuredata.com/int/google-cloud-storage-export-integration), [ActionIQ](https://info.actioniq.com/hubfs/ActionIQ%20Industry%20Brief%20Solutions/ActionIQ_Integrations_Brief.pdf), and [Adobe Experience Platform](https://experienceleague.adobe.com/en/docs/experience-platform/destinations/catalog/cloud-storage/google-cloud-storage).

#### To send customer data

If customer data cannot be sent to the Braze data platform or via the CEP, then it should be sent directly to Google Cloud Storage bucket.

Finally, other options or completely custom audience builds are possible. These may require additional Services work or Engineering work from your team. To determine what is feasible and optimal, work with the AI Decisioning Services team.

