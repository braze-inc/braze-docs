---  
nav_title: MAILIZIO  
article_title: MAILIZIO  
description: "This reference article outlines the partnership between Braze and MAILIZIO."  
alias: /partners/MAILIZIO/  
page_type: partner  
search_tag: Partner  
---

# Mailizio

> **Mailizio** is an email creation and management platform that makes it easy to design reusable, brand-safe content using an intuitive visual editor. With the **Braze integration**, you can export your content blocks and email marketing, then automatically generate in-app messages from those same assets, enabling fast and fully controlled campaign deployment

*This integration is maintained by Mailizio*

## About this integration  
With the Mailizio - Braze integration, you can design dynamic email marketing using Mailizio’s powerful editor, leverage Liquid variables as used in your Braze configurations, and automatically push them to Braze for streamlined campaign execution.

## Use cases  
* Push ready-to-send email marketing directly into Braze for campaigns and transactional messages.  
* Build reusable content modules (headers, footers, promotions, etc.) to streamline production across multiple campaigns and channels.  
* Generate in-app messages from emails: Thanks to Ai, Mailizio identifies the most relevant sections of your email marketing, letting you export the HTML and drop it straight into your in-app campaigns.  
* Personalize at scale with Braze-compatible Liquid variables, usable in both emails and in-app messages.  
* Keep your branding consistent by managing all creative assets in Mailizio and updating them in Braze with a single export.

## Prerequisites  
| Prerequisite       | Description |                          
|-----------------------|-----------------|  
| Mailizio account   | A Mailizio account is required to take advantage of this partnership.  |  
| Braze REST API key  | A Braze REST API key with full **Templates** permissions.<br><br>This can be created in the Braze dashboard from **Settings** > **API Keys**. |  
| A Braze REST endpoint | [Your REST endpoint URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Your endpoint depends on the Braze URL for your instance.  |  
{: .reset-td-br-1 .reset-td-br-2 role=“presentation”}

## Integration  
Provide your Braze REST API key and cluster instance to the Mailizio customer success manager. The team will then set up the initial integration for you.

{% alert important %}  
This is a one-time setup and any exports in the future will automatically use this API key.  
{% endalert %}

### Step 1: Create a email in Mailizio

In Mailizio, use our drag-and-drop editor to easily build an email that reflects your brand identity, and click ‘Save’ to preserve your work.

![drag-and-drop editor screenshot]({% image_buster /assets/img/mailizio/screenshot_1.png %})

### Step 2: Export your email marketing to Braze

Once ready, click ‘Export Newsletter’, in the popup, select ’Braze-email’, and choose whether you want to export it.

If you update your content later, simply re-export from Mailizio to refresh it in Braze.

![export modal screenshot]({% image_buster /assets/img/mailizio/screenshot_2.png %})

{% alert important %}  
You can create and export content blocks the same way using Mailizio’s ‘Module’ editor.  
{% endalert %}

## Usage  
Find your uploaded email in your Braze account’s Templates & Media > Email Templates section. You can now use this email marketing to start sending engaging email messages to your customers!