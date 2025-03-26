---
nav_title: Alpaco
article_title: Alpaco
alias: /partners/Alpaco
description: "The Braze and Alpaco integration leverages Alpaco's syntax to create and export data-driven email templates to Braze."
page_type: partner
search_tag: Partner

---

# Alpaco

> [Alpaco](https://alpaco.email/) is an online email marketing tool that offers a drag-and-drop email editor for a new level of control of design and output. The Braze and Alpaco integration allows you to export on-brand and data-driven emails to Braze. 

_This integration is maintained by Alpaco._

{% alert note %}
Alpaco supports [full Liquid](https://shopify.github.io/liquid/) variables, and as such also fully supports any Liquid variables used in your Braze configurations.
{% endalert %}

## Prerequisites

| Requirement | Description |
| ------------| ----------- |
| Alpaco account | An Alpaco account is required to take advantage of this partnership. |
| Braze REST API key | A Braze REST API key with full **Templates** permissions. <br><br> This can be created in the Braze dashboard from **Settings** > **API Keys**. |
| Cluster instance | Your Braze [cluster instance]({{site.baseurl}}/api/basics/#endpoints) aligns with your Braze dashboard and REST endpoint. <br><br> For example, if your dashboard URL is `https://dashboard-03.braze.com`, your endpoint will be `dashboard-03`.  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Integration

Provide your Braze REST API key and cluster instance to the Alpaco customer success team. The team will then set up the initial integration for you.

{% alert note %}
This is a one-time setup and any exports in the future will automatically use this API key.
{% endalert %}

## Exporting Alpaco emails to Braze

### Step 1: Create an email template in Alpaco

In the Alpaco platform, use the different settings and options to create a template that expresses your brand identity. Select **Save** when you're happy with your template.

![Alpaco Create template]({% image_buster /assets/img/alpaco/alpaco_1.png %})

### Step 2: Create an email

After the template is created, navigate to the lobby and create an email with the template. Select **Review** to make sure everything looks right.

![Alpaco Create email]({% image_buster /assets/img/alpaco/alpaco_2.png %})

### Step 3: Review and export email to Braze

Select **Export** and choose the Braze integration to export your email template to Braze. 

If you want to make changes to your email template, make those changes in Alpaco, and then export the email again to Braze. This will update the email in Braze with your changes.

![Alpaco Export email]({% image_buster /assets/img/alpaco/alpaco_3.png %})

## Using Alpaco email templates in Braze

Find your uploaded Alpaco email by navigating to **Templates & Media > Email Templates** in the Braze dashboard. You can now use this template to send on-brand and data-driven emails to your users.


[1]: {{site.baseurl}}/user_guide/message_building_by_channel/email/creating_an_email_template/
