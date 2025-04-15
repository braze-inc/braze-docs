---
nav_title: Smartling
article_title: Smartling
description: "This reference article outlines the partnership between Braze and Smartling, a cloud-based software for localization. The Braze Connector supports the translation of HTML email templates, Content Blocks, Canvases, and campaign email messages."
alias: /partners/smartling/
page_type: partner
search_tag: Partner
---

# Smartling

> [Smartling][5] is an end-to-end cloud translation management software for customers looking to automate the translation of websites, applications, and customer experiences.

_This integration is maintained by Smartling._

## About the integration

The Braze Connector supports the translation of HTML email templates, Content Blocks, Canvases, and campaign email messages. Translations are requested from Smartling, and translated content is automatically sent to Braze.

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Smartling account | A [Smartling account][2] is required to take advantage of this partnership. |
| Smartling translation project | To connect your Braze account with Smartling, you must first sign in and [create a translation project][6]. |
| Braze REST API key | A Braze REST API key with all templates and Content Blocks permissions. <br><br> This can be created in the Braze dashboard from **Settings** > **API Keys**. |
| Braze REST endpoint | [Your REST endpoint URL][1]. Your endpoint will depend on the Braze URL for your instance. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

The Smartling Braze integration allows you to translate HTML email templates, Content Blocks, Canvases, and campaign email messages. Note the following details depending on what you're translating:

**Email templates**
* Only HTML email templates are supported.
* You will need to decide on how your translated emails are delivered to Braze by the connector:
  * **One Email for All Languages:** The connector delivers all languages in the same email as the source.
  * **One Email per Language:** The connector creates a new email for each language in Braze.

**Content Blocks**
* All Content Blocks are supported.
* The Content Blocks contain both the original and translated versions.
* Liquid script determines the correct language for display based on the recipient's language preference.

**Campaigns and Canvases**
* Make sure you've added your target languages under **Multi-Language Support** settings in Braze.
* Refer to [Smartling documentation][3] for details on connector configuration.

## Integration

### Step 1: Set up the Braze project in Smartling TMS

#### Connecting Braze to Smartling

1. In [Smartling][2], create a [Braze Connector][6] project type in your Smartling account.
  - Make sure all required target languages are added to the project.
2. In this project, select **Settings** > **Braze Settings** > **Connect to Braze**.
3. Enter your Braze API URL and Braze API key.
4. Select **Save**.

#### Complete Braze connector configuration

Refer to Smartling [documentation][3] for details on connector configuration.

1. Select how you want automation of prior requests for translation.
2. Configure the source and target languages in **Language Configuration**. The connector will use it to ingest content into Smartling TMS and deliver translations back to Braze.

![Connector language configuration.][8]

### Step 2: Send content to Smartling

Once the Braze connector has been connected and set up, you will find Braze content in the **Braze** tab in your Smartling project. Refer to Smartling [documentation][7] to learn more.

Smartling provides advanced features to search and select content by:

* Keyword search
* Braze content type
* Braze tagging

![Content blocks list.][9]

### Step 3: Add translations to Braze

As translations are completed in the Smartling platform, they are automatically sent to Braze—no need to manually sync content between Smartling and Braze.


[1]: {{site.baseurl}}/api/basics/#endpoints
[2]: https://dashboard.smartling.com/
[3]: https://help.smartling.com/hc/en-us/articles/13248549217435
[4]: https://help.smartling.com/hc/article_attachments/13347533624347
[5]: https://www.smartling.com/
[6]: https://help.smartling.com/hc/en-us/articles/115003074093
[7]: https://help.smartling.com/hc/en-us/articles/13248577069979
[8]: {% image_buster /assets/img/smartling/smartling-braze-settings.png %}
[9]: {% image_buster /assets/img/smartling/smartling-content-blocks-list.png %}