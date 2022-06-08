---
nav_title: Crowdin
article_title: Crowdin
page_order: 1
description: "This article outlines the partnership between Braze and Crowdin, a cloud-based software platform that allows you to automate the translation of your email templates and content blocks in Braze."
alias: /partners/crowdin/
page_type: partner
search_tag: Partner

---

# Crowdin

> Crowdin is a cloud-based software for localization management. Using Crowdin, you can translate your Android and iOS apps, website, store screenshots, and other content. Translation can be done through your in-house team, a translation agency, or using machine translation engines.

The Braze and Crowdin integration allows you to translate email templates and content blocks. You can also synchronize content from your Braze account to your Crowdin project and add translations back to Braze.

## Prerequisites

| Requirement| Description|
| ---| ---|
| Crowdin account | A [Crowdin account](https://accounts.crowdin.com/register) is required to take advantage of this partnership. |
| Crowdin translation project | To connect your Braze account with Crowdin or Crowdin Enterprise, you will first need to sign up and create a translation project. |
| Braze REST API key | A Braze REST API key with all templates and content blocks permissions. <br><br> This can be created within the **Braze Dashboard > Developer Console > REST API Key > Create New API Key**. |
| Braze SDK endpoint | Your SDK endpoint URL will depend on the Braze URL for [your instance]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Integration

### Step 1: Set up the Braze app in Crowdin/Crowdin Enterprise

#### Crowdin
To set up the Braze app in Crowdin, follow these steps:

1. Go to the [Braze app in the marketplace](https://crowdin.com/resources#marketplace/braze).
2. Click **Install** to add it to your account.
3. Open the project you created for your Braze content localization.
4. Go to **Settings > Integrations** tab.
5. In the **Applications** section, click on the Braze app.
6. In the dialog, provide your Braze credentials (Braze REST API Key and Braze SDK Endpoint).
7. Click **Log in with Braze Connector**. 

#### Crowdin Enterprise
To set up the Braze app in Crowdin Enterprise, follow these steps:

1. Go to the **Workspace** home page > **Marketplace**.
2. Click **Install** on the Braze app to add it to your organization.
3. Open the project you created for your Braze content localization.
4. Go to **Applications > Custom**.
5. Click on the Braze app.
6. In the dialog, provide your Braze credentials (Braze REST API Key and Braze SDK Endpoint).
7. Click **Log in with Braze Connector**.

### Step 2: Add your content to Crowdin/Crowdin Enterprise

Once you provide your Braze credentials, you'll see two panels. Select the desired content to sync the files for translation from your Braze account and click **Sync to Crowdin**.

In the Editor mode in Crowdin, the content synced from your Braze account can be displayed to your translators as a string list or as a file preview.

![An image of what the Crowdin Editor email composer looks like with some basic translations added.][2]

### Step 3: Add translations to Braze

As soon as translations are complete, open the Braze app in Crowdin, select the translated files (for each file, you can choose either all target languages or only specific ones) on the left panel, and click **Sync to Braze**.

![An image of a user selecting their translation files and syncing them to Braze.][3]

[1]: {% image_buster /assets/img/crowdin/copy_api_key_identifier.png %}
[2]: {% image_buster /assets/img/crowdin/crowdin_editor_email_preview.png %}
[3]: {% image_buster /assets/img/crowdin/sync_translations.png %}
