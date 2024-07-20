---
nav_title: Smartling
article_title: Smartling
description: "This reference article outlines the partnership between Braze and Smartling, a cloud-based software for localization. This integration allows you to translate email templates and Content Blocks in Braze."
alias: /partners/smartling/
page_type: partner
search_tag: Partner
---

# Smartling

> [Smartling](https://dashboard.smartling.com/) is an end-to-end cloud translation management software for customers looking to automate the translation of websites, applications, and customer experiences.

The Braze and Smartling integration allows you to translate email templates and Content Blocks. Smartling provides linguists with the benefit of visual context during translation, which reduces errors and maintains quality.

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Smartling account | A [Smartling account](https://dashboard.smartling.com/) is required to take advantage of this partnership. |
| Smartling translation project | To connect your Braze account with Smartling, you must first sign up and [create a translation project](https://help.smartling.com/hc/en-us/articles/13248549217435). |
| Braze REST API key | A Braze REST API key with all templates and Content Blocks permissions. <br><br> This can be created in the Braze dashboard from **Settings** > **API Keys**. |
| Braze REST endpoint | [Your REST endpoint URL]({{site.baseurl}}/api/basics/#endpoints). Your endpoint will depend on the Braze URL for your instance. |
{: .reset-td-br-1 .reset-td-br-2}

## Integration

The Smartling Braze integration will allow you to translate email templates and Content Blocks. 

Email templates: 
* Only HTML Editor Emails are supported. 
* Each translation will be stored as its own email template. 

Content Blocks: 
* All Content Blocks are supported. 
* The Content Blocks contain both the original and translated versions.
* Liquid script determines the correct language for display based on the recipient's language preference.

### Step 1: Set up the Braze project in Smartling TMS

#### Connecting Braze to Smartling

1. In [Smartling](https://dashboard.smartling.com/), create a [Braze Connector](https://help.smartling.com/hc/en-us/articles/115003074093) project type in your Smartling account. 
  - Ensure all required target languages are added to the project.
2. From within this project, click **Settings** > **Braze Settings** > **Connect to Braze**.
3. Enter your Braze API URL and Braze API key.
4. Click **Save**.

#### Complete Braze connector configuration

Refer to Smartling [documentation](https://help.smartling.com/hc/en-us/articles/13248549217435) for details on connector configuration.

Select how you want automation of prior requests for translation.

Configure the source and target languages in **Language Configuration**. It will be used by the connector for ingesting content into Smartling TMS and delivering translations back to Braze.

![]({% image_buster /assets/img/smartling/smartling-braze-settings.png %})

### Step 2: Send content to Smartling

Once the Braze connector has been connected and set up, you will find Braze content in the **Braze** tab in your Smartling project. Refer to Smartling [documentation](https://help.smartling.com/hc/en-us/articles/13248577069979) to learn more.

Smartling provides advanced features to search and select content by:
* Keyword search
* Braze content type
* Braze tagging

![]({% image_buster /assets/img/smartling/smartling-content-blocks-list.png %})

### Step 3: Add translations to Braze

As translations are completed in the Smartling platform, they are automatically sent to Braze—no need to manually sync content between Smartling and Braze.

