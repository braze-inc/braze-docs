---
nav_title: Mozart Data
article_title: Mozart Data
page_order: 1

description: "This document outlines Braze's partnership and integration steps with Mozart Data, an all-in-one modern data platform."
alias: /partners/your_partner_name/

page_type: partner
search_tag: Partner
hidden: true

---
{% multi_lang_include video.html id="HU6dSOClcQ0" align="right" %}

# Mozart Data

> [Mozart Data](https://mozartdata.com/) is an all-in-one modern data platform powered by Fivetran, Portable, and Snowflake. We empower customers to centralize, clean, and analyze their data in all one place.


The Braze integration with Mozart Data allows you to:
- Use Fivetran to import Braze data into Snowflake cloud data warehouse in minutes
- Create transforms by coming the Braze data with the data from all of your other applications and effectively analyze user behaviors
- Import data from the Snowflake data warehouse into Braze to create new customer engagement opportunities based
- Combine Braze data with the data from all of your other applications to gain a more holistic understanding of user behaviors
- Integrate with a business intelligence tool to further explore the data that is stored in Snowflake data warehous

## Prerequisites


{% alert important %}
The following requirements listed are typical requirements you might need from Braze. We recommend using the attributed titling and phrasing listed in the following chart. Be sure to adjust the descriptions and tailor them to your partnership integration. 
{% endalert %}

| Requirement | Description |
| ----------- | ----------- |
| Mozart Data account | A Mozart Data account is required to take advantage of this partnership. |
| (Option 1) | During the Mozart Data account creation process, select the **Create a New Snowflake Account** option. Mozart Data will provision a new Snowflake account for you |
| [Option 2] Snowflake (ACCOUNTADMIN) | If your organization already has a Snowflake account, you will need to involve a user with account-level permissions |
{: .reset-td-br-1 .reset-td-br-2}

## Use cases

Use cases can be a critical part of your documentation. Although optional, this is a good place to outline typical or even novel use cases for the integration. This can be used as a way to sell or upsell the relationship - it provides context, ideas, and most importantly, a way to visualize the capabilities of the integration.

## Integration

This is where you break down the integration into steps. Do not just write endless paragraphs - these are technical documents that will be used by marketers and developers alike to get the integration up and running. Your main goal is to write descriptive documentation that helps the Braze user get the job done. 

Optionally, you can also provide details on if this is a side-by-side, server-to-server, or basic integration. This enables you to have multiple integration sections if more than one way to integrate exists.

### Step 1: Short description of step one 

Provide a short description for each step, including any code, as necessary. Remember that you can offer several different code sets - there's no need to only provide one way to integrate.

### Step 2: Short description of step two 

You also can add images to your documentation. We recommend including images of key integration steps as images do a great job of confirming what users should be seeing as they progress through the various steps.

### Step 3: Short description of step three 

Outline thorough integration usage, especially if it includes inserting Liquid into our message composer. If your integration leverages a Braze webhook, we recommend including the following webhook formatting steps into your partner page.

{% details Webhook formatting %}
```
### Step 2: Create a [Partner] webhook in Braze
To create a [Partner] webhook template to use in future campaigns or Canvases, navigate to the **Templates & Media** section in the Braze platform. If you would like to create a one-off [Partner] webhook campaign or use an existing template, select **Webhook** in Braze when creating a new campaign.
Once you have selected the [Partner] webhook template, you should see the following:
- **Webhook URL**: [Partner Webhook URL]
- **Request Body**: Raw Text
#### Request headers and method
[Partner] requires an `HTTP Header` for authorization. The following will already be included within the template as key-value pairs.
{% raw %}
- **HTTP Method**: POST
- **Request Header**:
  - **Authorization**: Bearer [PARTNER_AUTHORIZATION_HEADER]
  - **Request Body**: application/json
{% endraw %}
#### Request body
Include code of your webhook request body. 
### Step 3: Preview your request
Preview your request in the **Preview** panel or navigate to the `Test` tab, where you can select a random user, an existing user or customize your own to test your webhook.
{% alert important %}
Remember to save your template before leaving the page! <br>Updated webhook templates can be found in the **Saved Webhook Templates** list when creating a new [webhook campaign]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/). 
{% endalert %}
```
{% enddetails %}

## Customization

Customization is an **optional** section. Here, you could outline specific ways to customize your integration between the two partners.

## Using this integration

This section should describe how to use the integration in Braze. Let users know how to access the data (if any) provided to Braze through the integration and how to leverage it in Braze messaging.

### Step 1: Short description of step one 

This set of steps will walk your users through how to use this integration in Braze.

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
