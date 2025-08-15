このテンプレートを使ってテクノロジーパートナードキュメントを作成できます。例としては、[Scuba Analytics]({{site.baseurl}}/partners/data_and_analytics/business_intelligence/scuba/) を参照してください。

{% details テンプレートを表示 %}
{% raw %}
`````markdown
---
nav_title: NAV_TITLE
article_title: ARTICLE_TITLE
description: "SHORT_DESCRIPTION."
alias: /partners/PARTNER_NAME/
page_type: partner
search_tag: Partner
---

<!-- In most cases, the ARTICLE_TITLE will be your company name. If your tool requires several separate pages on Braze Docs, you can add a relevant page descriptor to your title, such as "MyCompany Analytics." -->
# ARTICLE_TITLE

<!-- The description starts with a '>' character and contains an introduction to your company, a link to your main site, and a concise overview of your integration. In a following paragraph, highlight the the relationship between your company and Braze and how this partnership helps your customers. -->
> DESCRIPTION.

*This integration is maintained by PARTNER_NAME.*

## Overview

ADDITIONAL_INFORMATION.

<!-- Most partner integrations will require the following prerequisites. However, you may add additional prerequisites as needed. -->
## Prerequisites

Before you start, you'll need the following:

| Prerequisite          | Description                                                                                                                                |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| A PARTNER_NAME account   | A PARTNER_NAME account is required to take advantage of this partnership.                                                                     |
| A Braze REST API key  | A Braze REST API key with `users.track` permissions. <br><br> This can be created in the Braze dashboard from **Settings** > **API Keys**. |
| A Braze REST endpoint | [Your REST endpoint URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Your endpoint will depend on the Braze URL for your instance.                                                 |
{: .reset-td-br-1 .reset-td-br-2}

<!-- An optional section you can use to outline the typical or atypical use cases for your integration. -->
## Use cases

CONTENT.

<!-- Create step-by-step instructions for integrating your tool with Braze. It's important to be concise and only outline the minimum necessary steps. -->
## Integrating TOOL_NAME

CONTENT.

### Step 1: ACTION_TO_COMPLETE

CONTENT.

<!-- Use the "Make a post request", "Default behavior," and "Rate limit" sections to outline how users can make a POST request. If this information isn't required for your integration, you can remove these sections. -->
### Step 2: Make a post request

{% alert important %}
The following request uses curl. For better API request management, we recommend using an API client, such as Postman.
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

| Placeholder             | Description                                                                                                                                                                                     |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `BRAZE_API_ENDPOINT`    | The Braze REST endpoint URL of your current Braze instance. For more information, see [Rest API keys]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/#rest-api-keys). |
| `BRAZE_API_KEY`         | Your Braze REST API key with the `users.track` permission.                                                                                                                                      |
| `HOSTNAME`              | The hostname of your current PARTNER_NAME instance.                                                                                                                                                    |
| `PARTNER_NAME_API_TOKEN`       | Your PARTNER_NAME API token.                                                                                                                                                                           |
{: .reset-td-br-1 .reset-td-br-2}

#### Default behavior

CONTENT.

#### Rate limit

CONTENT.

<!-- An optional section you can use to outline additional customization steps. It's important to be concise and only outline the minimum necessary steps. -->
## Customizing TOOL_NAME

### Step 1: ACTION_TO_COMPLETE

CONTENT.

### Step 2: ACTION_TO_COMPLETE

CONTENT.

<!-- A section outlining how to use your integration with Braze. For example: how to access the data sent to Braze, or how to leverage your integration with Braze messaging. -->
## Using TOOL_NAME with Braze

### Step 1: ACTION_TO_COMPLETE

CONTENT.

### Step 2: ACTION_TO_COMPLETE

CONTENT.
`````
{% endraw %}
{% enddetails %}
