---
nav_title: Personalize.AI
article_title: Personalize.AI
description: "This reference article outlines the partnership between Braze and Personalize.AI, an AI-based SaaS business platform that drives revenue growth from personalized recommendations."
alias: /partners/personalize/
page_type: partner
search_tag: Partner
---

# Personalize.AI

> [Personalize.AI](https://www.zs.com/solutions/artificial-intelligence-and-analytics/personalize-ai/) partners with Braze to improve customer revenue by delivering personalized messages and offers sent through Braze. Use this integration to export data from Personalize.AI into the Braze platform.

## Prerequisites

| Requirement             | Description                                                                                                                                                     |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Personalize.AI instance | A Personalize.AI instance is required to take advantage of this partnership.                                                                                    |
| Braze REST API key      | A Braze REST API key with all permissions. <br><br>This can be created within the **Braze Dashboard > Developer Console > REST API Key > Create New API Key**. |
| Braze REST endpoint     | Your REST endpoint URL. Your endpoint will depend on the [Braze URL for your instance][1].                                                                      |
{: .reset-td-br-1 .reset-td-br-2}

## Use cases

* Deploy testing, including flexible stratification, to drive results from customer feedback
* Provide personalized recommendations for items and offers, including treatment, timing, and content
* Identify prioritized objectives and target your optimal audience through Braze
* Identify opportunities to re-engage lapsed users
* Leverage geo-location data to find the right audience for newly-opened locations
* Use lookalike modeling to build on limited available data for newer users, matchings them with the most relevant recommendations
* Identify the right ways to engage customers throughout their lifecycle 
* Proactively assess customers for likelihood to churn and assign a risk score to find early indicators of churn
* Target customers with personalized interventions to prevent them from becoming inactive

## Integration

### Configure a connection with Braze in Personalize.AI

1. Navigate to the **Integrations** tab, located under **Operationalization**, in your Personalize.AI instance.
2. Click on **Braze**. 
3. Configure your integration with Braze.

* **Connection Name:** Name your connection. This is how your integration will be referred to in Personalize.AI.
* **Sync Frequency:** The sync frequency controls how often Personalize.AI exports data to Braze. Select **Daily**, **Weekly**, or **Monthly**. 
* **API Key:** Add your Braze API key.
* **API URL:** Add your Braze REST endpoint URL.

4. Click **EXPORT** to export data to Braze.

Once your data has been exported, Personalize.AI will continue to pass data to Braze at the intervals determined by the sync frequency that you set during integration.

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints