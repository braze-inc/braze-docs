---
nav_title: Personalize.AI
article_title: Personalize.AI
page_order: 1

description: "This is the Google Search and SEO description that will appear; try to make this informative and concise, yet brief."
alias: /partners/personalize/

page_type: partner
search_tag: Partner
hidden: true
layout: dev_guide
---

# Personalize.AI

Personalize.AI partners with Braze to unlock incremental value for Braze users by providing 1:1 personalization for messages and offers sent through Braze. P.AI has been used in conjunction with Braze with multiple clients during which we partnered to create impact from personalization and to drive double digit growth. With the value generated with the existing partnerships, there is significant value in partnering to go to new businesses with new capabilities and to provide additional value to existing clients. By making the existing integration deeper, Braze and P.AI can work in tandem to provide end to end marketing success. With P.AI’s robust data science and AI capabilities, we see opportunity in working together to codevelop feature and leveling up the offerings for businesses.

![Image1][2] ![Image3][3]

![Image4][4]

## Prerequisites

| Requirement             | Description                                                                                                                                                     |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Personalize.AI instance | A Personalize.AI instance is required to take advantage of this partnership.                                                                                    |
| Braze REST API key      | A Braze REST API key with all permissions. <br><br> This can be created within the **Braze Dashboard > Developer Console > REST API Key > Create New API Key**. |
| Braze REST endpoint     | Your REST endpoint URL. Your endpoint will depend on the [Braze URL for your instance][1].                                                                      |

{: .reset-td-br-1 .reset-td-br-2}

## Use cases

- Deploy sophisticated testing including flexible stratification to ensure maximized learnings and fair testing environment
- Serve 1:1 personalized recommendations of items and offers including treatment, timing, and content
- Identify prioritized objectives and deploy optimal audience and treatment to reach them
- For customers who are inactive, find customers most likely to reactivate and intervene with the lowest cost effective offers
- Leverage app session geo-location data to find the right audience for a newly opened business location while balancing cannibalization of nearby units
- Use lookalike modeling to build on limited available data for newer customers to identify and map customers with the most relevant recommendations
- Identify and serve optimal offers to engage customers throughout their lifecycle journey to influence each incremental action driving a higher ROI (at the lowest marketing spend)
- Proactively assess customers for likelihood to churn and assign a risk score leveraging ML model to find early indicators of churn
- Target customers with personalized interventions to prevent them from becoming inactive

## Integration

### Configure Braze Connection in Personalize.AI

When you log in to your Personalize.AI account, navigate to the **Integrations** tab, under Operationalization on right side menu.

Scroll until you can find Braze, and click on **Braze**.

A popup will appear to configure the integration with Braze.

- **Connection Name:** This is how the connection will be named and referred going forward
- **Sync Frequency:** Select Daily Weekly or Monthly; this will control how often Personalize.AI exports data to Braze
- **API Key:** Braze API Key created in the Requirements
- **API URL:** Braze REST endpoint URL as defined in the requirements

Click **EXPORT** to export data to Braze

### Post Export

Once your data has been exported, based on your Sync Frequency configured in connection, Personalize.AI will generate an updated version of data and send it to Braze.

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints

[2]: {% image_buster /assets/img/personalize/PAI1.png %}
[3]: {% image_buster /assets/img/personalize/PAI2.png %}
[4]: {% image_buster /assets/img/personalize/PAI3.png %}


