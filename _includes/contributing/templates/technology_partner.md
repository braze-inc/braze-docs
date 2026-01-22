You can use this template to create technology partner documentation. For an example, see [Scuba Analytics]({{site.baseurl}}/partners/data_and_analytics/business_intelligence/scuba/).

{% details Show template %}
{% raw %}
`````markdown
---
nav_title: PARTNER_NAME
article_title: PARTNER_NAME
description: "This reference article outlines the partnership between Braze and PARTNER_NAME."
alias: /partners/PARTNER_NAME/
page_type: partner
search_tag: Partner
---

# ARTICLE_TITLE
<!-- In most cases, the ARTICLE_TITLE will be your company name. If your tool requires several separate pages on Braze Docs, you can add a relevant page descriptor to those pages’ titles, such as "MyCompany Analytics." -->

> DESCRIPTION.
<!-- The description starts with a '>' character and contains an introduction to your company, a link to your main site, and a concise overview of your integration.-->

<-- Only include the following line if the partner manages the integration. If Braze manages the integration, don’t include it. -->
*This integration is maintained by PARTNER_NAME*

## About this integration
<-- Highlight the relationship between your company and Braze and how this partnership helps your customers. -->

ADDITIONAL_INFORMATION.

## Use cases
<!--Though the ‘Use cases’ section is optional, this is a good place to outline typical or even novel use cases for the integration. Use this section as a way to sell or upsell your integration to customers and Braze account teams; it provides context, ideas, and most importantly, a way to visualize the capabilities of your integration.-->

CONTENT.

<!-- When including screenshots, use the following format to specify where each screenshot should be placed. PARTNER_NAME and IMAGE_NAME should be all lowercase. -->
![ALT_TEXT]({% image_buster /assets/img/PARTNER_NAME/IMAGE_NAME.png %})

## Prerequisites
<!-- Most partner integrations require the following prerequisites. However, you may add additional prerequisites as needed. -->

Before you start, you need the following:

| Prerequisite       | Description |                        
|-----------------------|-----------------|
| A PARTNER_NAME account   | A PARTNER_NAME account is required to take advantage of this partnership.  |
| A Braze REST API key  | A Braze REST API key with `users.track` permissions. <br><br> Create this key in the Braze dashboard from **Settings** > **API Keys**. |
| A Braze REST endpoint | [Your REST endpoint URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Your endpoint depends on the Braze URL for your instance.  |
{: .reset-td-br-1 .reset-td-br-2 role=“presentation”}

## Integrating TOOL_NAME
<!-- Create step-by-step instructions for integrating your tool with Braze. It's important to be concise and outline the minimum necessary steps. -->

### Step 1: ACTION_TO_COMPLETE

CONTENT.

### Step 2: Make a POST request
<!-- Use the "Make a POST request", "Default behavior," and "Rate limit" sections to outline how users can make a POST request. If this information isn't required for your integration, you can remove these sections. -->

{% alert important %}
The following request uses cURL. For better API request management, we recommend using an API client, such as Postman.
{% endalert %}

To upload your PARTNER_NAME data to Braze, make a POST request to `PARTNER_POST_URL` using the `application/json` content-type:

```bash
curl -X POST "PARTNER_POST_URL" \
-H "content-type: application/json" \
-d '{"braze_host":"BRAZE_API_ENDPOINT", \
"braze_api_key":"BRAZE_API_KEY", \
"PARTNER_host":"HOSTNAME", \
"PARTNER_token":"PARTNER_NAME_API_TOKEN"}'
```

Replace the following:

| Placeholder     | Description      |
|---------------------|---------------------|
| `BRAZE_API_ENDPOINT`    | The Braze REST endpoint URL of your current Braze instance. For more information, see [Rest API keys]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/#rest-api-keys). |
| `BRAZE_API_KEY`         | Your Braze REST API key with the `users.track` permission. |                                                                                                                                    | `HOSTNAME`                  | The hostname of your current PARTNER_NAME instance.  |                                                                                                                         
| `PARTNER_NAME_API_TOKEN`       | Your PARTNER_NAME API token.  |                                                                                                                                        {: .reset-td-br-1 .reset-td-br-2 role=“presentation”}

#### Default behavior

CONTENT.

#### Rate limit

CONTENT.

## Customizing TOOL_NAME
<!-- An optional section you can use to outline additional customization steps. It's important to be concise and outline the minimum necessary steps. -->

### Step 1: ACTION_TO_COMPLETE

CONTENT.

### Step 2: ACTION_TO_COMPLETE

CONTENT.

## Using TOOL_NAME with Braze / USE_CASE
<!-- A section outlining how to use your integration with Braze. For example, how to access the data sent to Braze, how to leverage your integration with Braze messaging, or how to complete a certain use case from the “Use cases” section. -->

### Step 1: ACTION_TO_COMPLETE

CONTENT.

### Step 2: ACTION_TO_COMPLETE

CONTENT.

## Considerations
<!-- An optional section listing additional information that may impact how users interact with your integration. -->

### CONSIDERATION_ITEM

CONTENT.

## Troubleshooting
<!-- An optional section guiding users through issues they may encounter while setting up your integration. You can also direct users to your documentation site with hyperlinks. -->

### TROUBLESHOOTING_ITEM

CONTENT.
`````
{% endraw %}
{% enddetails %}
