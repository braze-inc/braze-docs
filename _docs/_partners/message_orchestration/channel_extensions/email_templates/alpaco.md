---
nav_title: Alpaco
article_title: Alpaco
alias: /partners/Alpaco
description: "This reference article outlines the partnership between Braze and Alpaco, an online email marketing tool that offers a drag-and-drop email editor with unparalleled level of control of design and output."
page_type: partner
search_tag: Partner

---

# Alpaco

> [Alpaco](https://alpaco.email/) is an online email marketing tool that offers a drag-and-drop email editor with unparalleled level of control of design and output. Alpaco offers a collaborative platform for marketers, copywriters, designers and developers for an optimal workflow, before exporting the email to Braze for campaign creation.

The Braze and Alpaco integration leverages Alpaco's syntax to create and export data-driven email templates to Braze.

## Prerequisites

| Requirement | Description |
| ------------| ----------- |
| Alpaco account | A Alpaco account is required to take advantage of this partnership. |
| Braze REST API key | A Braze REST API key with full **Templates** permissions. <br><br> This can be created in the Braze dashboard from **Settings** > **API Keys**. |
| Cluster instance | Your Braze [cluster instance]({{site.baseurl}}/api/basics/#endpoints) aligns with your Braze dashboard and REST endpoint. <br><br> For example, if your dashboard URL is `https://dashboard-03.braze.com`, your endpoint will be `dashboard-03`.  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Integration

Provide your Braze REST API key and cluster instance to the Alpaco customer success team. The team will then set up the initial integration for you.

{% alert important %}
This is a one-time setup and any exports in the future will automatically utilize this API key.
{% endalert %}

### Step 1: Create a email template in Alpaco

Create an email template in the Alpaco platform. Use the different settings and options to create an on-brand template to your liking. Click **Save** when you're happy with your template.<br>Alpaco supports [full Liquid](https://shopify.github.io/liquid/) variables, and as such also fully supports any Liquid variables used in your Braze configurations.

![Alpaco Create template]({% image_buster /assets/img/alpaco/alpaco_1.png %})

### Step 2: Export template to Braze
After the template is created, navigate to the lobby and create an email with the template and click **Review**.


![Alpaco Create email]({% image_buster /assets/img/alpaco/alpaco_2.png %})

### Step 3: Export template to Braze
Click **Export** and chose the recently created integration to your Braze enviroment, made by the Alpaco customer sucess team.<br>
Making changes to an email in Alpaco, and exporting it again will result in updating the email in Braze.

![Alpaco Export email]({% image_buster /assets/img/alpaco/alpaco_3.png %})

## Usage

Find your uploaded Alpaco email in your Braze account's **Templates & Media > Email Templates** section. You can now use this emails to start sending on-brand and full data-driven email messages to your customers!

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/email/creating_an_email_template/