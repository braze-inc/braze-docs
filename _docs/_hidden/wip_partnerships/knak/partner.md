---
nav_title: Knak
article_title: Knak
page_order: 1

description: "The Knak integration allows you create fully-responsive emails in minutes or hours instead of days or weeks, and export them as ready-to-use Braze templates."
alias: /partners/knak/

page_type: partner
search_tag: Partner
hidden: true

---

# Knak

> [Knak][1] is the first campaign creation platform built for enterprise marketing teams to use in-house. Our drag-and-drop platform lets anyone create beautiful, on-brand emails and landing pages in minutes, with no coding or outside help required. Plus, it integrates seamlessly with Braze.

Knak is built for marketers who want to level-up their email creation for campaigns managed in Braze, without the need for outside agencies or hand-coding. It lets you create fully-responsive emails in minutes or hours instead of days or weeks, and export them as ready-to-use Braze templates.

## Prerequisites

In short, anybody with a Knak account and a Braze account can use Knak with Braze.

| Requirement | Description |
| ----------- | ----------- |
| Knak account | A Knak account is required to take advantage of this partnership. |
| Braze REST API key | A Braze REST API Key with full Templates permissions. <br><br>This can be created within the **Braze Dashboard -> Developer Console -> REST API Key -> Create New API Key** |
| Braze Environment URL | [Your REST endpoint URL][2]. Your endpoint will depend on the Braze URL for your instance. |
{: .reset-td-br-1 .reset-td-br-2}

## Use cases

Knak is built for marketers who want to level-up their email creation for campaigns managed in Braze, with no coding or outside help required. It’s great for those who:
- Currently use simple templates for emails, and want to up their game
- Rely on outside agencies or developers to build emails for Braze
- Want to take back creative control over asset creation, and get to market considerably faster

## Integration

Knak integrates seamlessly with Braze in a few easy steps.

### Step 1

On the left-side menu in Knak, go to **Integrations > Platforms**.

![integration_setup_step_1][1]

### Step 2

Click on **+ Add New Integration** on the top right hand side.

![integration_setup_step_2][2]

### Step 3

Select the **Braze** platform.

![integration_setup_step_3][3]

### Step 4

Enter an integration name, the API key, and the Braze Environment URL.

![integration_setup_step_4][4]

### Step 5

Click on **Create New Integration**.

![integration_setup_step_5][5]

## Using this integration

You can find your uploaded Knak emails in your Braze account’s Engagement > Templates & Media section. They’ll be beautiful, on-brand and fully responsive. The only limit is your own creativity!

### Step 1
Go to **Publish > Sync**

![integration_post_step_1][6]

### Step 2
Check the Asset name that you want to show in Braze and click on **Sync**.

![integration_post_step_2][7]

### Step 3
The email is now synced to Braze. The email can be found under **Engagement > Templates & Media** in Braze.

![integration_post_step_3][8]


[1]: https://knak.com/
[2]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints

[1]: {% image_buster /assets/img/knak/integration-setup-step-1-platforms.png %}
[2]: {% image_buster /assets/img/knak/integration-setup-step-2-add-new-integration.png %}
[3]: {% image_buster /assets/img/knak/integration-setup-step-3-select-braze.png %}
[4]: {% image_buster /assets/img/knak/integration-setup-step-4-add-api-key.png %}
[5]: {% image_buster /assets/img/knak/integration-setup-step-5-save.png %}
[6]: {% image_buster /assets/img/knak/integration-post-step-1-sync.png %}
[7]: {% image_buster /assets/img/knak/integration-post-step-2-asset-name.png %}
[8]: {% image_buster /assets/img/knak/integration-post-step-3-templates-media.png %}