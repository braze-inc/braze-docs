---
nav_title: Mention Me
article_title: Mention Me
description: Mention Me Integration Setup Guide
alias: /partners/mention-me/
page_type: partner
search_tag: Partner
---

# Mention Me

<!-- In most cases, the ARTICLE_TITLE will be your company name. If your tool requires several separate pages on Braze Docs, you can add a relevant page descriptor to your title, such as "MyCompany Analytics." -->

<!-- The description starts with a '>' character and contains an introduction to your company, a link to your main site, and a concise overview of your integration. In a following paragraph, highlight the the relationship between your company and Braze and how this partnership helps your customers. -->
> Together, [Mention Me](https://www.mention-me.com/) and Braze is your gateway to attracting premium customers and fostering unwavering brand loyalty. 
By seamlessly integrating first-party referral data into Braze, you can deliver highly personalised omnichannel experiences targeted at your brand fans.

_This integration is maintained by Mention Me._

<!-- Most partner integrations will require the following prerequisites. However, you may add additional prerequisites as needed. -->
## Prerequisites

Before you start, you'll need the following:

| Prerequisite          | Description                                                                                                                                |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| A Mention Me account   | A [Mention Me](https://mention-me.com/login) account is required to take advantage of this partnership.                                                                     |
| A Braze REST API key  | A Braze REST API key with `users.track` and `campaignstemplates.email.create` permissions. <br><br> This can be created in the Braze dashboard from **Settings** > **API Keys**. |
| A Braze REST endpoint | [Your REST endpoint URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Your endpoint will depend on the Braze URL for your instance.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

<!-- An optional section you can use to outline the typical or atypical use cases for your integration. -->
## Use cases

* Send contact data and opt-ins from Mention Me referred customers to Braze in real time
* Use referral data to create coupon email reminders
* Enhance the performance of other marketing channels by using referral data to segment and target high value customers


<!-- Create step-by-step instructions for integrating your tool with Braze. It's important to be concise and only outline the minimum necessary steps. -->
## Integrating Mention Me

Connecting Mention Me to Braze takes just a few minutes, just follow these simple steps to get connected. 

### Connect Mention Me to Braze

1. Create a Braze API Key with `users.track` and `campaignstemplates.email.create` permissions.
2. On the [Mention Me Braze Integration Page](https://mention-me.com/merchant/~/integrations/braze), click **Connect**
3. Enter the API Key and select your Braze Instance
4. Select the countries you want to sync with

More details on the setup process can be found [here](https://help.mention-me.com/hc/en-gb/articles/26151756257693-How-to-setup-Braze-with-Mention-Me)
### What data is sent from Mention Me to Braze

During the setup of the Braze integration, Mention Me will take care of creating the customer attributes and events, so you won't need to do this beforehand.

The events and custom attributes linked to customers in Braze are based on their email addresses. Mention Me will send events and contact profile attributes for any prospect or existing customer (regardless of their opt-in status) who has triggered an event via Mention Me.

More details on the different contact profle attributes and events can be found [here](https://help.mention-me.com/hc/en-gb/articles/26677937177501-What-Mention-Me-data-is-sent-to-Braze)
