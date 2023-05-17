---
nav_title: Smartling
article_title: Smartling
page_order: 1

description: "This reference article outlines the partnership between Braze and Smartling, a cloud-based software for localization. This integration allows you to translate email templates and content blocks in Braze."
alias: /partners/smartling/

page_type: partner
search_tag: Partner
hidden: true
layout: dev_guide
---

# Smartling

An end-to-end cloud translation management software for customers looking to automate the translation of websites, applications, and customer experiences.

The Braze and Smartling integration allows you to translate email templates and content blocks. Smartling provides linguists with the benefit of visual context during the translation process, which reduces errors and maintains quality.

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Smartling account | A [Smartling account][2] is required to take advantage of this partnership. |
| Smartling translation project | To connect your Braze account with Smartling, you will first need to sign up and [create a translation project][3]. |
| Braze REST API key | A Braze REST API key with all templates and content blocks permissions. <br><br> This can be created within the **Braze Dashboard > Developer Console > REST API Key > Create New API Key**. |
| Braze REST endpoint | [Your REST endpoint URL][1]. Your endpoint will depend on the Braze URL for your instance. |
{: .reset-td-br-1 .reset-td-br-2}

## Integration

### Step 1: Set up the Braze project in Smartling TMS

#### Connecting Braze to Smartling

1. Log into [Smartling][2].
2. Create a [**Braze Connector**][6] project type in your Smartling Account.
    * Ensure all required target languages are added to the project.
3. From within this project, click **Settings > Braze Settings**.
4. Click **Connect to Braze**.
5. Insert your [Braze API URL][1].
    * E.g.: `https://rest.iad-01.braze.com`.
    * You need to use your Braze login URL to find API URL in the endpoints table.
6. Insert your **Braze API Key**.
    * In Braze, go to the Developer Console and click Create New API Key
        ![api key][4]
    * API Key should have **all permissions for templates emails** and **content blocks**
        ![permissions][5]
7. Click Save

#### Complete Braze connector configuration

Please check the full [connector configuration documentation here][3].

Select how you want automation of prior requests for translation.

Configure the source and target languages in **Language Configuration**. It will be used by the connector for ingesting content into Smartling TMS and delivering translations back to Braze.

![Connector language configuration][8]

### Step 2: Send content to Smartling

Once the Braze Connector has been connected and set up, you will find Braze content in the Braze tab in your Smartling project. Please see the full [documentation here][7].

Smartling provides advanced features to search and select content by:
* Keyword Search
* Braze Content Type
* Braze tagging

![Content blocks list][9]

### Step 3: Add translations to Braze

As translations are completed in the Smartling Platform, they are automatically sent to Braze. No need to manual sync content between Smartling and Braze, everything is fully automated!

[1]: {{site.baseurl}}/api/basics/#endpoints
[2]: https://dashboard.smartling.com/
[3]: https://help.smartling.com/hc/en-us/articles/13248549217435
[4]: https://help.smartling.com/hc/article_attachments/13347533624347
[5]: https://help.smartling.com/hc/article_attachments/13946813331739
[6]: https://help.smartling.com/hc/en-us/articles/115003074093
[7]: https://help.smartling.com/hc/en-us/articles/13248577069979
[8]: {% image_buster /assets/img/smartling/smartling-braze-settings.png %}
[9]: {% image_buster /assets/img/smartling/smartling-content-blocks-list.png %}
