---
nav_title: Smartling
article_title: Smartling
description: "This reference article outlines the partnership between Braze and Smartling, a cloud-based software for localization. This integration allows you to translate email templates and content blocks in Braze."
alias: /partners/smartling/
page_type: partner
search_tag: Partner
---

# Smartling

> [Smartling][2], is an end-to-end cloud translation management software for customers looking to automate the translation of websites, applications, and customer experiences.

The Braze and Smartling integration allows you to translate email templates and content blocks. Smartling provides linguists with the benefit of visual context during translation, which reduces errors and maintains quality.

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Smartling account | A [Smartling account][2] is required to take advantage of this partnership. |
| Smartling translation project | To connect your Braze account with Smartling, you must first sign up and [create a translation project][3]. |
| Braze REST API key | A Braze REST API key with all templates and Content Blocks permissions. <br><br> This can be created within the **Braze Dashboard > Developer Console > REST API Key > Create New API Key**. |
| Braze REST endpoint | [Your REST endpoint URL][1]. Your endpoint will depend on the Braze URL for your instance. |
{: .reset-td-br-1 .reset-td-br-2}

## Integration

### Step 1: Set up the Braze project in Smartling TMS

#### Connecting Braze to Smartling

1. In [Smartling][2], create a [Braze Connector][6] project type in your Smartling account. 
  - Ensure all required target languages are added to the project.
2. From within this project, click **Settings** > **Braze Settings** > **Connect to Braze**.
3. Enter your Braze API URL and Braze API key.
4. Click **Save**.

#### Complete Braze connector configuration

Refer to Smartling [documentation][3] for details on connector configuration.

Select how you want automation of prior requests for translation.

Configure the source and target languages in **Language Configuration**. It will be used by the connector for ingesting content into Smartling TMS and delivering translations back to Braze.

![][8]

### Step 2: Send content to Smartling

Once the Braze connector has been connected and set up, you will find Braze content in the **Braze** tab in your Smartling project. Refer to Smartling [documentation][7] to learn more.

Smartling provides advanced features to search and select content by:
* Keyword search
* Braze Content type
* Braze tagging

![][9]

### Step 3: Add translations to Braze

As translations are completed in the Smartling platform, they are automatically sent to Braze. No need to manually sync content between Smartling and Braze.

[1]: {{site.baseurl}}/api/basics/#endpoints
[2]: https://dashboard.smartling.com/
[3]: https://help.smartling.com/hc/en-us/articles/13248549217435
[4]: https://help.smartling.com/hc/article_attachments/13347533624347
[5]: https://help.smartling.com/hc/article_attachments/13946813331739
[6]: https://help.smartling.com/hc/en-us/articles/115003074093
[7]: https://help.smartling.com/hc/en-us/articles/13248577069979
[8]: {% image_buster /assets/img/smartling/smartling-braze-settings.png %}
[9]: {% image_buster /assets/img/smartling/smartling-content-blocks-list.png %}