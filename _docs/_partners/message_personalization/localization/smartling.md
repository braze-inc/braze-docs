---
nav_title: Smartling
article_title: Smartling
description: "This reference article outlines the partnership between Braze and Smartling, a cloud-based software for localization. The Braze Connector supports the translation of HTML email templates, Content Blocks, Canvases, and campaign email messages."
alias: /partners/smartling/
page_type: partner
search_tag: Partner
---

# Smartling

> [Smartling](https://www.smartling.com/) is an end-to-end cloud translation management software for customers looking to automate the translation of websites, applications, and customer experiences.

_This integration is maintained by Smartling._

## About the integration

The Braze Connector supports translations for Campaigns and Canvases ([Email](https://www.braze.com/docs/user_guide/message_building_by_channel/email/using_locales/#prerequisites), [Push](https://www.braze.com/docs/user_guide/message_building_by_channel/push/using_locales/#prerequisites), and [IAM](https://www.braze.com/docs/user_guide/message_building_by_channel/in-app_messages/using_locales)), Email Templates, and Content Blocks. Translations are supported in both HTML and Drag-and-Drop editors where supported. 

{% alert note %}
Depending on your use case, you can manage translations for Content Blocks or Email Templates using either the legacy translation workflow or the updated one. In the updated workflow, using Braze's multi-language support and locales in messages, translation tags are added to the Content Block or Email Template. However, Smartling executes translations at the message level. The content is translated only once it’s included in a Campaign or Canvas and the target locale is set. Please see the **Managing translations for Content Blocks and Email Templates** section for more information.
{% endalert %}

## Prerequisites

| Requirement                   | Description                                                                                                                                                         |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Smartling account             | A [Smartling account](https://dashboard.smartling.com/) is required to take advantage of this partnership.                                                          |
| Smartling translation project | To connect your Braze account with Smartling, you must first sign in and [create a translation project](https://help.smartling.com/hc/en-us/articles/115003074093). |
| Braze REST API key            | A Braze REST API key with the following permissions: <br>- campaigns.translations.get<br>- campaigns.translations.update<br>- campaigns.list<br>- campaigns.details<br>- canvas.translations.get<br>- canvas.translations.update<br>- campaigns.list<br>- campaigns.list<br>- campaigns.details<br>- templates.email.create<br>- templates.email.update<br>- templates.email.list<br>- templates.email.info<br>- templates.translations.get<br>- templates.translations.update<br>- content_blocks.info<br>- content_blocks.list<br>- content_blocks.create<br>- content_blocks.update<br><br> This can be created in the Braze dashboard from **Settings > API Keys**. |
| Braze REST endpoint           | [Your REST endpoint URL](https://www.braze.com/docs/api/basics/#endpoints). Your endpoint will depend on the Braze URL for your instance.             |
| Braze Multi Language Settings | [Complete Multi Language Settings in Braze](https://www.braze.com/docs/user_guide/administrative/app_settings/multi_language_settings/#prerequisites) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Step 1: Set up multi-language settings in Braze

Refer to the [instructions](https://www.braze.com/docs/user_guide/administrative/app_settings/multi_language_settings/#prerequisites) for setting up locales in Braze.

### Step 2: Set up the Braze project in Smartling TMS

Refer to Smartling [documentation](https://help.smartling.com/hc/en-us/articles/13248549217435) for details on connector configuration.

### Connecting Braze to Smartling

1. In [Smartling](https://dashboard.smartling.com/), create a [Braze Connector](https://help.smartling.com/hc/en-us/articles/115003074093) project type in your Smartling account.

![Braze connection in Smartling.]({% image_buster /assets/img/smartling/image1_Connecting_Braze_to_Smartling.png %})

{: start="2"}
2. In this project, select **Settings** > **Braze Settings** > **Connect to Braze**.
3. Enter the required fields like API URL and API Key. If the Test Connection is successful, save Connection. If the test is not successful, double check you’ve inputted the correct API URL and API Key.

![Braze connection in Smartling API settings.]({% image_buster /assets/img/smartling/image2_API.png %})

{: start="4"}
4. Add additional project languages.

![Braze connection in Smartling Project Languages.]({% image_buster /assets/img/smartling/image3_project_languages.png %}) assets/img/smartling/image3_project_languages.png

{: start="5"}
5. In Braze Settings, verify that the values in the Target Language (Braze) column match the locales configured in Braze multi-language settings. The locale naming convention must match exactly.







#### Complete Braze connector configuration

Refer to Smartling [documentation](https://help.smartling.com/hc/en-us/articles/13248549217435) for details on connector configuration.

1. Select how you want automation of prior requests for translation.
2. Configure the source and target languages in **Language Configuration**. The connector will use it to ingest content into Smartling TMS and deliver translations back to Braze.

![Connector language configuration.]({% image_buster /assets/img/smartling/smartling-braze-settings.png %})

### Step 2: Send content to Smartling

Once the Braze connector has been connected and set up, you will find Braze content in the **Braze** tab in your Smartling project. Refer to Smartling [documentation](https://help.smartling.com/hc/en-us/articles/13248577069979) to learn more.

Smartling provides advanced features to search and select content by:

* Keyword search
* Braze content type
* Braze tagging

![Content blocks list.]({% image_buster /assets/img/smartling/smartling-content-blocks-list.png %})

### Step 3: Add translations to Braze

As translations are completed in the Smartling platform, they are automatically sent to Braze—no need to manually sync content between Smartling and Braze.


