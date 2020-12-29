---
nav_title: Crowdin
page_order: 1

description: "Crowdin helps you automate the translation of your email templates and content blocks in Braze. Send your campaigns in multiple languages."
alias: /partners/crowdin/

page_type: crowdin
hidden: true
---

# About Crowdin

Crowdin is a cloud-based software for localization management. Braze integration with Crowdin allows you to translate email templates and content blocks. You can synchronize content from your Braze account to your Crowdin project and add translations back to Braze.

You can translate your Android and iOS apps, website, store screenshots, and other content in Crowdin as well. Use features for improving translation quality, adding translation context, team cooperation, translation memory, workflow automation, integrations and plugins, and many more. You can translate your content with your in-house team, a translation agency, or using machine translation engines.

## Pre-Requisites

To connect your Braze account with <a href="https://accounts.crowdin.com/register" target="_blank">Crowdin</a> or <a href="https://accounts.crowdin.com/register" target="_blank">Crowdin Enterprise</a>, you’ll first need to sign up and create your translation project.

## Generate your credentials in Braze

To connect your Braze account with Crowdin, you need to provide two authorization elements: 
* Rest API Key 
* SDK Endpoint of your Web app

### Create Web App

To create a Web app in your Braze account, follow these steps:

1. In your Braze Dashboard, navigate to **Manage App Group**.
2. Click **Add App**.
3. Specify your App Name and select the **Web** option from the **Platform** drop-down list.
4. Click **Add App**.

   ![Create Web App][1]

5. Copy the SDK Endpoint.

   ![Copy SDK Endpoint][2]

### Create Rest API Key

To create a new Rest API Key in your Braze account, follow these steps:

1. In your Braze Dashboard, navigate to Developer Console.
2. Click Create New API Key in the Rest API Keys section.

   ![Create API Key][3]

3. Specify your API Key Name and select the following permissions:

     * Templates
     * Content Blocks

    These permissions represent the content types you’ll be able to transfer to Crowdin for localization.
4. Click Save API key.

After this, you’ll see your new API Key in the Rest API Keys section list. Copy the Identifier of your new API Key.

   ![Copy API Key Identifier][4]

## Set up Braze app in Crowdin

To set up the Braze app in Crowdin, follow these steps:

1. Go to the <a href="https://crowdin.com/resources#marketplace/braze" target="_blank">Braze app in the marketplace</a>.
2. Click **Install** to add it to your account.
3. Open the project you created for your Braze content localization.
4. Go to **Settings > Integrations** tab.
5. In the **Applications** section, click on the Braze app.
6. In the appeared dialog, provide your Braze credentials (Braze API Key and SDK Endpoint).
7. Click **Log in with Braze Connector**. 

## Set up Braze app in Crowdin Enterprise

To set up the Braze app in Crowdin Enterprise, follow these steps:

1. Go to the **Workspace** home page > **Marketplace**.
2. Click **Install** on the Braze app to add it to your organization.
3. Open the project you created for your Braze content localization.
4. Go to **Applications > Custom**.
5. Click on the Braze app.
6. In the appeared dialog, provide your Braze credentials (Braze API Key and SDK Endpoint).
7. Click **Log in with Braze Connector**.

## Add your content to Crowdin/Crowdin Enterprise

Once you provide your Braze credentials, you’ll see two panels. To sync the files for translation from your Braze account, select the needed content on the right panel, and click **Sync to Crowdin**.

In the Editor mode in Crowdin, the content synced from your Braze account can be displayed to your translators as a string list or as a file preview.

   ![Crowdin Editor Email Preview][5]

## Add Translations to Braze

As soon as translations are completed, open the Braze app in Crowdin, select the translated files (for each file, you can choose either all target languages or only specific ones) on the left panel, and click **Sync to Braze**.

   ![Sync Translations to Braze][6]

[1]: {% image_buster /assets/img/crowdin/create_web_app.png %}
[2]: {% image_buster /assets/img/crowdin/copy_sdk_endpoint.png %}
[3]: {% image_buster /assets/img/crowdin/create_api_key.png %}
[4]: {% image_buster /assets/img/crowdin/copy_api_key_identifier.png %}
[5]: {% image_buster /assets/img/crowdin/crowdin_editor_email_preview.png %}
[6]: {% image_buster /assets/img/crowdin/sync_translations.png %}