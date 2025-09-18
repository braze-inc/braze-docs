---
nav_title: Dyspatch
article_title: Dyspatch
alias: /partners/dyspatch
description: "This reference article outlines the partnership between Braze and Dyspatch, a drag-and-drop email builder that allows you to create beautiful, responsive, and engaging emails without the need to write code."
page_type: partner
search_tag: Partner

---

# Dyspatch

> [Dyspatch](https://www.dyspatch.io) offers an intuitive drag-and-drop email builder used to create beautiful, responsive, and engaging emails without needing to write code. Collaborate with your team to create and approve emails within Dyspatch and then export them to Braze, all in a few steps! 

_This integration is maintained by Dyspatch._

## About the integration

The Dyspatch and Braze integration allow you to simplify your email creation lifecycle by exporting Dyspatch email templates directly to Braze.

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Dyspatch account | A [Dyspatch account](https://www.dyspatch.io/login/) with an [owner or admin role](https://docs.dyspatch.io/administration/dyspatch_roles/) is required to take advantage of this partnership. |
| Braze REST API key | A Braze REST API key with full **Templates** permissions. <br><br> This can be created in the Braze dashboard from **Settings** > **API Keys**. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Integration

The Braze and Dyspatch integration lets you export Dyspatch email templates directly into your Braze media library or download your template and manually upload it. 

### Step 1: Create the Braze integration

In the Dyspatch administration portal, open your username dropdown menu and select **Integrations**. Create a new integration, select **Braze**, and enter your Braze API key.

In the **Localize Exports By** field, you can choose how you would like to manage localization. This field allows you to [localize your email templates](https://docs.dyspatch.io/localization/localizing_a_template/) and export them to Braze to easily send emails personalized by language or locale. 

![Dyspatch Export Template]({% image_buster /assets/img/dyspatch/dyspatch_integration_create.png %}){: style="max-width:50%;"}

### Step 2: Export template to Braze

After completing an email in Dyspatch, to send your template to Braze, view the published email template and click **Download/Export** and then **Export to Integration**.

If you want to upload your template manually, view the published email template and  click **Download/Export** and then **Download HTML**. Next, in the **Templates & Media > Email Templates** section of your Braze account, select **From File** to upload your template.

![Dyspatch Export Template]({% image_buster /assets/img/dyspatch/dyspatch_export.gif %})

{% alert important %}
Do not select **Inline CSS** in the **Sending Info** section for any Dyspatch email template in Braze. Dyspatch takes care of this by making sure your emails are robust, responsive, and ready to send.
{% endalert %}

### Usage

Find your uploaded Dyspatch template in your Braze account's **Templates & Media > Email Templates** section. You can now use this email template to start sending engaging email messages to your customers!


