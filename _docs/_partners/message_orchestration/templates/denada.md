---
nav_title: Denada
article_title: Denada
alias: /partners/denada/
description: "This reference article outlines the partnership between Braze and Denada, an AI-powered marketing creative platform that lets you create on-brand email templates through natural conversation and export them directly to Braze."
page_type: partner
search_tag: Partner
---

# Denada

> [Denada](https://heydenada.com) is an AI-powered marketing creative platform that lets subject matter experts create on-brand marketing materials through natural conversation. With Denada, teams can go from ideation to finished email content without needing design expertise.

_This integration is maintained by Denada._

## About the integration

The Braze and Denada integration allows you to export email templates created in Denada directly into Braze, including automatic image upload to the Braze media library. This streamlines the process of moving from creative ideation to campaign execution.

## Prerequisites

The following are required to use this integration:

| Requirement | Description |
| ----------- | ----------- |
| Denada account | A [Denada account](https://app.heydenada.com) is required to use this integration. |
| Braze REST API key | A Braze REST API key with full **Templates** permissions. <br><br>This can be created in the Braze dashboard from **Settings** > **API Keys**. |
| Braze REST endpoint | [Your REST endpoint URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Your endpoint depends on the Braze URL for your instance. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Use cases

Denada is built for marketers and subject matter experts who want to create on-brand email content without design or coding skills. It's great for those who:
- Want to use conversational AI to rapidly generate email templates and push them directly to Braze
- Need to iterate on existing Braze email templates by re-exporting from Denada with conflict detection and overwrite support
- Want automatic image upload and management in the Braze media library during export

## Integration

### Step 1: Configure your integration

In Denada, click your company name in the lower left corner and select **Team settings**, then click **Add integration**.

Select **Braze** as the integration, then enter your Braze **API key** and select your **REST API endpoint** from the list of available regions.

{% alert note %}
This is a one-time setup. When your credentials are validated, your configuration is saved for all future exports.
{% endalert %}

### Step 2: Export a template to Braze

In Denada, open an email template in the editor and select **Export** > **Braze**.

Enter a **template name** and **subject line** for the email. Choose your image handling preference:
- **Upload new:** Upload all images to the Braze media library.
- **Use existing:** Reuse previously uploaded images when available.

If a template with the same name already exists in Braze, Denada detects the conflict and prompts you to confirm whether to overwrite or create a new template.

Click **Export**. Denada renders the template to HTML, uploads images to Braze, and creates or updates the email template in your Braze account.

## Using the integration

You can find your uploaded Denada emails in Braze under **Templates & Media > Email Templates**. In older navigation, go to **Engagement** > **Templates & Media**. They're ready to use in any Braze campaign or Canvas.

Denada tracks previous exports, so subsequent exports of the same template can update the existing Braze template rather than creating duplicates.
