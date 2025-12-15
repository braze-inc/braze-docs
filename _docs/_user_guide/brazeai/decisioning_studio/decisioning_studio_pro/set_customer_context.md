---
page_order: 4.2
nav_title: Set Customer Context
article_title: Set Customer Context
description: "Learn how to configure customer context for Decisioning Studio Pro agents, including audience definition and customer data."
---

# Set Customer Context

Decisioning Studio agents need to fully understand customer context in order to make decisions. Configuring this part of the pipeline includes both defining the audience and configuring customer data to be sent to the agents.

## Step 1: Define the audience

Use case audiences are typically defined in a Customer Engagement Platform (such as Braze or Salesforce Marketing Cloud), then sent to the Decisioning Studio agent. The agent then divides customers into treatment groups in order to conduct randomized controlled trials. These treatment groups will include, at minimum, a Decisioning Studio group and a Random Control. It may also include a Business-as-Usual group which allows you to test agent performance against the current marketing journey, and/or a Holdout group, to test how customers perform when they receive no communications from the campaign at all.

Specific instructions for audience configuration are included below, alongside instructions for sending customer data. 

## Step 2: Send additional customer data to Decisioning Studio

In order to effectively personalize customer engagement, agents need to understand as much as possible about your customers. This data should be sent along with the audience definition. 

The following customer data assets are important to consider: 

* **[Required]** Conversions – needed to train AI models and calculate the success metric. Should include the value of each conversion (e.g., revenue) if relevant. This is especially important for establsihing the self-learning feedback loop for agents. For more information on how to properly validate, consider the [Create the Feedback Loop]({{site.baseurl}}/user_guide/brazeai/decisioning_studio_pro/create_feedback_loop/) section.

* **[Required]** Activation and engagement data – what was actually sent through each channel based on Decisioning Studio's recommendations and any subsequent customer actions associated with the triggered marketing event (e.g. send, open, click).

* **Customer profile** – years as customer; geography, if allowed in this industry; acquisition channel (e.g., web, phone); satisfaction level; model scores (e.g., churn propensity); lifetime value estimate

* **Customer behavior** – account logins; device type and operating system used for logins; customer service interactions (e.g., number of calls, topics); product usage (e.g., hours used per day, features accessed, categories viewed)

* **Other transactions** – products purchased by date (including product attributes); transaction amounts; transaction channels (e.g., in-store, online); payment methods

* **Other marketing engagement** – outbound communications sent (e.g., emails, SMS); email engagement (e.g., opens, clicks); survey responses (e.g., NPS, engagement); web and mobile app activity (e.g., pages browsed/products viewed)

### Best practices

* Customer data should have descriptive column names
* Incremental files are preferable vs. to snapshots of the whole customer history every day
* Include customer data on any insights that would be particularly important to your business (e.g., Do you want to see who self-learning AI treats your loyalty customers differently? Make sure it's in the customer data!)

## Integration patterns



### Step 1: Configure your audience

{% tabs %}
{% tab Braze %}

**Configure audience in Braze**
1. Create a segment for your audience that you would like to target.
2. Provide the Segment ID to your AI Decisioning Services team.

Note: For Braze, multiple segments can be combined to create the audience, and Decisioning Studio can ingest on a segment for a Business-as-Usual comparator compaign. All of these patterns are acceptable. 

**Send customer data from Braze**

In general, BrazeAI Decisioning Studio can use all data that you are already sending to the Braze Data Platform.

If there is customer data that you would want to use for Decisioning Studio that is not currently stored in the Customer Profile or Custom Attributes, the recommended approach [Braze Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion) to ingest data from other sources.

CDI supports any of direct integrations, including:

* Snowflake
* Redshift
* BigQuery
* Databricks
* Microsoft Fabric
* AWS S3

Once you are satisfied with the data you are sending into the Braze Data Platform, contact your AI Decisioning Services team to discuss which fields on the Customer Profile and Custom Attributes should be used for AI Decisioning.

To streamline this process, please create a list of Braze user profile attributes that you think best represent your customers' behaviors that should be used in Decisioning Studio (see the [list of available fields]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/#fields-to-export)). Your services team can also help you conduct discovery sessions with you to decide which fields are most appropriate for AI Decisioning.

Other options for sending data include: 
• Sending Braze custom events via the SDK
• Sending events via REST endpoint (/users/track)

These patterns require more engineering effort, but are sometimes preferable, depending on the current Braze configuration. Talk with AI Decisioning Services to learn more. 

{% tab Salesforce Marketing Cloud (SFMC) %}

Decisioning Studio is able to accept an SFMC data extension as the audience as well. Decisioning Studio uses the available REST and SOAP API interfaces provided by SFMC to interact with the platform.

**Configure audience in SFMC**
1. Configure an SFMC data extension(s) for your audience and provide the data extension ID
2. Set up SFMC Installed Package for API integration with the appropriate permissions required by Decisioning Studio
3. Ensure that this data extension must be refreshed daily, as Decisioning Studio will pull from the the latest incremental data available

Provide the extension ID and API key to the Braze services team. They will assist with next steps in ingesting customer data.

{% tab Klaviyo %}

**To define the audience in Klaviyo:**

In order to do this, take the following steps:

* Configure an SFMC data extension(s) for your audience and provide the data extension ID
* Set up SFMC Installed Package for API integration with the appropriate permissions required by Decisioning Studio
* Ensure that this data extension must be refreshed daily, as Decisioning Studio will pull from the the latest incremental data available

Provide the extension ID and API key to the Braze services team. They will assist with next steps.

{% tab Other Cloud Solutions %}

** Other Cloud Solutions (Google Cloud Storage, Azure, and AWS)**

Finally, if the audience is not currently stored in Braze, SFMC, or Klaviyo, then the next best step is to configure an automated export directly to a Braze-controlled Google Cloud Services bucket. We can also support export to AWS or Azure (although GCS is preferable).

To determine whether this is feasible, refer to the documentation for your Martech platform. For example, mParticle offers a [native integration with Google Cloud Storage](https://www.mparticle.com/integration/google-cloud-storage/). If this is the case, we can provide a GCS bucket to export audience data to. There are similar pages for [Twilio Segment](https://www.twilio.com/docs/segment/connections/storage/catalog/google-cloud-storage), [Treasure Data](https://docs.treasuredata.com/int/google-cloud-storage-export-integration), [ActionIQ](https://info.actioniq.com/hubfs/ActionIQ%20Industry%20Brief%20Solutions/ActionIQ_Integrations_Brief.pdf), and [Adobe Experience Platform](https://experienceleague.adobe.com/en/docs/experience-platform/destinations/catalog/cloud-storage/google-cloud-storage).

If customer data cannot be sent to the Braze data platform or via the CEP, then it should be sent directly to Google Cloud Storage bucket.

Finally, other options or completely custom audience builds are possible. These may require additional Services work or Engineering work from your team. To determine what is feasible and optimal, work with the AI Decisioning Services team.

