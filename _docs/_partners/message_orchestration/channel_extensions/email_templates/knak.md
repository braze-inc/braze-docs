---
nav_title: Knak
article_title: Knak
alias: /partners/knak/
description: "This article outlines the partnership between Braze and Knak, a campaign creation platform that allows you to create fully responsive emails in minutes or hours instead of days or weeks, and export them as ready-to-use Braze templates."
page_type: partner
search_tag: Knak

---

# Knak

> [Knak][1] is the first campaign creation platform built for enterprise marketing teams to use in-house. Their drag-and-drop platform lets anyone create beautiful, on-brand emails and landing pages in minutes, with no coding or outside help required.

The Braze and Knak integration allows you to create fully responsive emails in minutes or hours instead of days or weeks and export them as ready-to-use Braze templates. Knak is built for marketers who want to level up their email creation for campaigns managed in Braze, without the need for outside agencies or hand-coding. 

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Knak account | A Knak account is required to take advantage of this partnership. |
| Braze REST API key | A Braze REST API key with full **Templates** permissions. <br><br>This can be created within the **Braze Dashboard > Developer Console > REST API Key > Create New API Key**. |
| Braze REST endpoint | [Your REST endpoint URL][2]. Your endpoint will depend on the Braze URL for your instance. |
{: .reset-td-br-1 .reset-td-br-2}

## Use cases

Knak is built for marketers who want to level up their email creation, with no coding or outside help required. It's great for those who:
- Currently use simple templates for emails and want to up their game
- Rely on outside agencies or developers to build emails for Braze
- Want to take back creative control over asset creation and get to market considerably faster

## Integration

### Step 1: Configure your integration

In Knak, navigate to **Integrations > Platforms > + Add New Integration**.

![Add integration button][5]

Next, select the **Braze** platform and provide the Braze API key and REST endpoint. Click on **Create New Integration** to complete your integration. 

![Create new integration][6]

### Step 2: Sync your Knak templates

In Knak, locate an email you would like to sync to Braze and select **Publish** and then **Sync**.

![Knak integration 1][8]

Next, verify the email name and click **Sync**.

![Knak integration 2][9]

## Using the Integration

You can find your uploaded Knak emails in Braze under **Engagement > Templates & Media**. They'll be beautiful, on-brand, and fully responsive. The only limit is your own creativity!

[1]: https://knak.com/
[2]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[5]: {% image_buster /assets/img/knak/integration-setup-step-2-add-new-integration.png %}
[6]: {% image_buster /assets/img/knak/integration-setup-step-4-add-api-key.png %}
[8]: {% image_buster /assets/img/knak/integration-post-step-1-sync.png %}
[9]: {% image_buster /assets/img/knak/integration-post-step-2-asset-name.png %}