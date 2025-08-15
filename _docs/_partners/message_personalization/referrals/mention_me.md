---
nav_title: Mention me
article_title: Integrating Mention Me with Braze
description: Mention Me Integration Setup Guide
alias: /partners/mention_me/
page_type: partner
search_tag: Partner
---

# Mention Me

> Together, [Mention Me](https://www.mention-me.com/) and Braze can be your gateway to attracting premium customers and fostering unwavering brand loyalty. By seamlessly integrating first-party referral data into Braze, you can deliver highly-personalized omnichannel experiences targeted at your brand fans.

_This integration is maintained by Mention Me._

## Prerequisites

Before you start, you'll need the following:

| Prerequisite          | Description                                                                                                                                |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| A Mention Me account   | A [Mention Me](https://mention-me.com/login) account is required to take advantage of this partnership.                                                                     |
| A Braze REST API key  | A Braze REST API key with `users.track` and `templates.email.create` permissions. <br><br> This can be created in the Braze dashboard from **Settings** > **API Keys**. |
| A Braze REST endpoint | [Your REST endpoint URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Your endpoint will depend on the Braze URL for your instance.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Use cases

* Send contact data and opt-ins from Mention Me referred customers to Braze in real time
* Use referral data to create coupon email reminders
* Enhance the performance of other marketing channels by using referral data to segment and target high value customers

## What data is sent from Mention Me to Braze?

When you set up this integration, Mention Me will automatically create your customer attributes and events&#8212;so no need to do this beforehand.

Your customer's email addresses in Braze will be used to link relevant events and custom attributes. Mention Me will send events and contact profile attributes for any prospect or existing customer who triggers this event via Mention Me, regardless of their opt-in status.

For more details, refer to [Contact profile attributes and events](https://help.mention-me.com/hc/en-gb/articles/26677937177501-What-Mention-Me-data-is-sent-to-Braze).

## Integrating Mention Me

{% alert tip %}
For a full step-by-step walkthrough, refer to [Mention Me's Braze setup documentation](https://help.mention-me.com/hc/en-gb/articles/26151773368221-How-to-setup-Braze-with-Mention-Me).
{% endalert %}

To integrate Mention Me with Braze:

1. In Mention Me, go to the [Braze integration](https://mention-me.com/merchant/~/integrations/braze) page, then select **Connect**.
2. Select **Create New Authorization**, then add the [API key you previously created](#prerequisites) and select your Braze instance.
3. Choose one or more countries you'd like to sync with.
4. When you're finished, select **Connect**.
