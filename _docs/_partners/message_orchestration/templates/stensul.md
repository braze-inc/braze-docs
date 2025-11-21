---
nav_title: Stensul
article_title: Stensul
alias: /partners/stensul
description: "This reference article outlines the partnership between Braze and Stensul, an enterprise email platform for creating mobile-responsive email templates across channels."
page_type: partner
search_tag: Partner

---

# Stensul

> [Stensul](https://stensul.com/) provides email marketers tools to build mobile-responsive, on-brand emails in Stensul before sending them downstream to Braze in real time for campaign creation.

_This integration is maintained by Stensul._

## About the integration

The Braze and Stensul integration allows you to export your HTML-formatted Stensul emails and upload them as templates within Braze.

## Prerequisites

| Requirement | Description |
| ------------| ----------- |
| Stensul account | A Stensul account is required to take advantage of this partnership. |
| Braze REST API key | A Braze REST API key with full **Templates** permissions. <br><br> This can be created in the Braze dashboard from **Settings** > **API Keys**. |
| Cluster instance | Your Braze [cluster instance]({{site.baseurl}}/api/basics/#endpoints) aligns with your Braze dashboard and REST endpoint.  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Integration

Provide your Braze REST API key and cluster instance to your Stensul customer success team. The team will then set up the initial integration for you.

{% alert important %}
This is a one-time setup and any exports in the future will automatically utilize this API key.
{% endalert %}

### Step 1: Create Stensul email

Create a Stensul email in the Stensul platform and click **Complete**.

![Stensul Save Options]({% image_buster /assets/img_archive/stensul_save_options.png %})

### Step 2: Export template to Braze
In the new dialogue that appears on the completion page, select **Upload to ESP**.

![Stensul Upload Options]({% image_buster /assets/img_archive/stensul_upload_options.png %})

Next, enter the **template name**, **subject**, and **preheader** for your email and select **Upload**. You will then receive a confirmation that the upload was successful and a history of past uploads of the file, if applicable.

![Stensul Upload Success]({% image_buster /assets/img_archive/stensul_upload_success.png %})

## Usage

Find your uploaded Stensul template in your Braze account's **Templates & Media > Email Templates** section. You can now use this email template to start sending engaging email messages to your customers!


