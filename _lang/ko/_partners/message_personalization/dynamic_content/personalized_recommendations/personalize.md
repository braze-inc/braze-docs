---
nav_title: Personalize.AI
article_title: Personalize.AI
description: "This reference article outlines the partnership between Braze and Personalize.AI, an AI-based SaaS business platform that drives revenue growth from personalized recommendations."
alias: /partners/personalize_ai/
page_type: partner
search_tag: Partner
---

# Personalize.AI

> [Personalize.AI](https://www.zs.com/solutions/artificial-intelligence-and-analytics/personalize-ai/) partners with Braze to generate incremental revenue by delivering personalized messages and offers sent through Braze. 

The Braze and Personalize.AI integration allows you to export data from Personalize.AI into the Braze platform for message personalization and targeting.

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Personalize.AI instance | A Personalize.AI instance is required to take advantage of this partnership. |
| Braze REST API key | A Braze REST API key with all permissions. <br><br>This can be created in the Braze dashboard from **Settings** > **API Keys**. |
| Braze REST endpoint | Your REST endpoint URL. Your endpoint will depend on the [Braze URL for your instance]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Use cases

* Deploy testing, including flexible stratification, to drive results from customer feedback
* Provide personalized recommendations for items and offers, including treatment, timing, and content
* Identify prioritized objectives and target your optimal audience through Braze
* Identify opportunities to re-engage lapsed users
* Leverage geolocation data to find the right audience for newly opened locations
* Use lookalike modeling to build on limited available data for newer users, matching them with the most relevant recommendations
* Identify the right ways to engage customers throughout their lifecycle 
* Proactively assess customers for likelihood to churn and assign a risk score to find early indicators of churn
* Target customers with personalized interventions to prevent them from becoming inactive

## Integration

### Configure a connection with Braze in Personalize.AI

1. In Personalize.AI, navigate to the **Integrations** tab, located under **Operationalization**, in your Personalize.AI instance.
2. Click on **Braze**. 
3. Configure your integration with Braze.
    * **Connection Name:** Name your connection. This is how your integration will be referred to in Personalize.AI.
    * **Sync Frequency:** The sync frequency controls how often Personalize.AI exports data to Braze. Select **Daily**, **Weekly**, or **Monthly**. 
    * **API Key:** Add your Braze API key.
    * **API URL:** Add your Braze REST endpoint URL.
4. Click **EXPORT** to export data to Braze.

Once your data has been exported, Personalize.AI will continue to pass data to Braze at the intervals determined by the sync frequency you set during integration.

## Using this integration

Personalize.AI exports identifiers used for personalized targeting into Braze. These custom attributes indicate timing, content, treatment, and offers for each customer. Depending on the integration, fields can be passed as an event or pulled into the [Connected Content APIs]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/public_apis/) instead of stored on the customer's profile. Personalize.AI supports the use of `external_id` as an identifier.

The data attributes imported into Braze are intuitively named for use in Canvases, following consistent terminology. For example, the attribute `C402_Target_Variant` in Personalize.AI would be exported to Braze as `"P.AI_Model_Treatment"`. The attributes exported from Personalize.AI are designed to not interfere with any existing attributes or tracking your use. These attributes are validated continuously to confirm that you can reference them confidently. 

For example, here is a set of customer attributes as they relate to an example churn-focused Canvas.

| Personalize.AI attribute | Value |
| ----------- | ------------- | 
| `Customer_ID` | 12345 |
| `Target_Canvas` | C4 |
| `Target_Objective` |  "Churn_Mitigation" |
| `C4_Target_Date` | 3/1/2023 |
| `C4_Target_Variant` | Treatment |
| `C4_Treatment` | "P.AI_Model" |
| `C4_Offer_Value` | $3 |
| `C4_Item_Recom` | "Caesar Salad" |
| `C4_Subject_Line` | "We miss you" |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


