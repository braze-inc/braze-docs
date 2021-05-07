---
nav_title: Crowdin
page_order: 1
description: "Crowdin helps you automate the translation of your email templates and content blocks in Braze. Send your campaigns in multiple languages."
alias: /partners/crowdin/
---

# Crowdin

> Crowdin is a cloud-based software for localization management. Braze integration with Crowdin allows you to translate email templates and content blocks. You can synchronize content from your Braze account to your Crowdin project and add translations back to Braze.

Using Crowdin, you can translate your Android and iOS apps, website, store screenshots, and other content. Use features for improving translation quality, adding translation context, team cooperation, translation memory, workflow automation, integrations and plugins, and much more. You can translate your content with your in-house team, a translation agency, or using machine translation engines.

## Pre-Requisites

To connect your Braze account with <a href="https://accounts.crowdin.com/register" target="_blank">Crowdin</a> or <a href="https://accounts.crowdin.com/register" target="_blank">Crowdin Enterprise</a>, you’ll first need to sign up and create your translation project.

## Generate your credentials in Braze

To connect your Braze account with Crowdin, you need to provide two authorization elements: 
* Braze REST API Key 
* Braze REST Endpoint

### Create Braze REST API Key

To create a new Braze REST API Key in your Braze account, follow these steps:

1. In your Braze Dashboard, navigate to __Developer Console__ under __Settings__.
2. Click __Create New API Key__ in the REST API Keys section.
3. Specify your API Key Name and select the following permissions:
- Templates
- Content Blocks<br>
These permissions represent the content types you’ll be able to transfer to Crowdin for localization.<br>
4. Click __Save API key__.

After this, you’ll see your new REST API Key in the REST API Keys section list. Copy your new REST API Key from the Identifier column.<br><br>![Copy REST API Key Identifier][1]

### Copy Braze REST Endpoint

Depending on the instance your Braze account is provisioned to, copy the respective Braze REST Endpoint from the <a href="https://www.braze.com/docs/api/basics/#endpoints" target="_blank">Endpoints table</a>.

For example, if your Braze account is provisioned to the instance **US-01**, your Braze REST Endpoint is the following:<br> `rest.iad-01.braze.com`

## Set up Braze app in Crowdin/Crowdin Enterprise
{% tabs %}
{% tab Crowdin %}
To set up the Braze app in Crowdin, follow these steps:

1. Go to the <a href="https://crowdin.com/resources#marketplace/braze" target="_blank">Braze app in the marketplace</a>.
2. Click **Install** to add it to your account.
3. Open the project you created for your Braze content localization.
4. Go to **Settings > Integrations** tab.
5. In the **Applications** section, click on the Braze app.
6. In the appeared dialog, provide your Braze credentials (Braze REST API Key and Braze REST Endpoint).
7. Click **Log in with Braze Connector**. 
{% endtab %}

{% tab Crodwin Enterprise %}
To set up the Braze app in Crowdin Enterprise, follow these steps:

1. Go to the **Workspace** home page > **Marketplace**.
2. Click **Install** on the Braze app to add it to your organization.
3. Open the project you created for your Braze content localization.
4. Go to **Applications > Custom**.
5. Click on the Braze app.
6. In the appeared dialog, provide your Braze credentials (Braze REST API Key and Braze REST Endpoint).
7. Click **Log in with Braze Connector**.
{% endtab %}
{% endtabs %}

## Add your content to Crowdin/Crowdin Enterprise

Once you provide your Braze credentials, you’ll see two panels. To sync the files for translation from your Braze account, select the needed content on the right panel, and click **Sync to Crowdin**.

In the Editor mode in Crowdin, the content synced from your Braze account can be displayed to your translators as a string list or as a file preview.

   ![Crowdin Editor Email Preview][2]

## Add Translations to Braze

As soon as translations are completed, open the Braze app in Crowdin, select the translated files (for each file, you can choose either all target languages or only specific ones) on the left panel, and click **Sync to Braze**.

   ![Sync Translations to Braze][3]

[1]: {% image_buster /assets/img/crowdin/copy_api_key_identifier.png %}
[2]: {% image_buster /assets/img/crowdin/crowdin_editor_email_preview.png %}
[3]: {% image_buster /assets/img/crowdin/sync_translations.png %}
