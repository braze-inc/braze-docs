---
nav_title: Your Partner Page
article_title: Your Partner Page
page_order: 1

description: "This is the Google Search and SEO description that will appear; try to make this informative and concise, yet brief."
alias: /partners/your_partner_name/

page_type: partner
search_tag: Partner
hidden: true

---

# [Partner Name]

> Welcome to the Braze partner template! Here, you'll find everything you need to create your partner page. In this first section, include a brief description of your company. Also, include a link to your main site. 

In this second paragraph, explore the relationship between your company and Braze. This paragraph should explain how Braze and your company partner together to tighten the bond between the Braze user and their customer. Explain the "elevation" that occurs when a Braze user integrates with or leverages your partnership and the services you offer.

## Prerequisites

This section should list what you need to complete this partnership integration. The best way to deliver this information is with a quick instructional paragraph that describes any non-technically important details or "need to know" information, like whether or not your integration will be subject to additional security checks or clearances. Then, use a chart to describe the technical requirements of the integration.

{% alert important %}
The requirements listed below are typical requirements you might need from Braze. We recommend using the attributed titling and phrasing listed in the chart below. Be sure to adjust the descriptions and tailor them to your partnership integration. 
{% endalert %}

| Requirement | Description |
| ----------- | ----------- |
| Partner account | A partner account is required to take advantage of this partnership. |
| Braze REST API key | A Braze REST API Key with `users.track` permissions. <br><br> This can be created within the __Braze Dashboard -> Developer Console -> REST API Key -> Create New API Key__ |
| Braze REST endpoint | [Your REST endpoint URL][1]. Your endpoint will depend on the Braze URL for your instance. |
{: .reset-td-br-1 .reset-td-br-2}

## Use cases

Use cases can be a critical part of your documentation. Although optional, this is a good place to outline typical or even novel use cases for the integration. This can be used as a way to sell or upsell the relationship - it provides context, ideas, and most importantly, a way to visualize the capabilities of the integration.

## Integration

This is where you break down the integration into steps. Do not just write endless paragraphs - these are technical documents that will be used by marketers and developers alike to get the integration up and running. Your main goal is to write descriptive documentation that helps the Braze user get the job done. 

Optionally, you can also provide details on if this is a side-by-side, server-to-server, or out-of-the-box integration. This enables you to have multiple integration sections if more than one way to integrate exists.

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

Preview your request in the left-hand panel or navigate to the `Test` tab, where you can select a random user, an existing user or customize your own to test your webhook.

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