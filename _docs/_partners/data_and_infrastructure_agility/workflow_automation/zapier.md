---
nav_title: Zapier
article_title: Zapier
alias: /partners/zapier/
description: "This article outlines the partnership between Braze and Zapier, an automation web tool that allows you to share data between web apps, and use that information to automate actions."
page_type: partner
search_tag: Partner

---
# Zapier integration

> [Zapier][1] is an automation web tool that allows you to share data between web apps and then use that information to automate actions. 

The Braze and Zapier partnership leverages the Braze API and Braze [webhooks][3] to connect with third-party applications—such as Google Workplace, Slack, Salesforce, WordPress, etc. to automate various actions.

## Prerequisites

| Requirements | Description |
|---|---|
| Zapier account | A Zapier account is required to take advantage of this partnership. |
| Braze REST Endpoint | Your REST Endpoint URL. Your endpoint will depend on the [Braze URL for your instance][0]. |
{: .reset-td-br-1 .reset-td-br-2}

## Integration

In the Zapier example below, we will be sending information from WordPress to Braze using a POST webhook. This information can then be used to create a Braze campaign or Canvas.

### Step 1: Create a Zapier trigger

Using Zapier's terminology, a "zap" is an automated workflow that connects your apps and services. The first part of any zap is to designate a trigger. Once your zap is enabled, Zapier will automatically perform the respective actions whenever your trigger is detected.

Using our WordPress example, in the Zapier platform, we'll set up our zap to trigger when a new WordPress post gets added and select **Published** and **Posts** as **Post Status** and **Post Type**. 

![In the Zapier platform, within a zap, select the trigger to be a "new comment", "any webhook", or "new post". For this example, "new post" is selected. ] [5]

![In the Zapier platform, within a zap, configure the trigger by selecting the desired post status and post type. For this example, "Published", and "Posts" is selected.] [6]

### Step 3: Add an action webhook

Next, define the zap action. When your zap is enabled, and your trigger is detected, the action will automatically occur.

Continuing our example, we want to send a POST request as a JSON to a Braze endpoint. This can be done by selecting the **Webhooks** option under **Apps**.

![][7]

### Step 4: Set up Braze POST

First, choose **POST** as the webhook action type. Next, make sure to fill out the following fields using your Braze REST endpoint in the webhook URL:

- **Webhook URL**: `https://rest.iad-01.braze.com/campaigns/trigger/send`
- **Payload Type** : JSON
- **Data** : `trigger_properties**name`, `api_key`, and `campaign_id`
These data fields are key-value pairs that will be used for the data portion of the request.

![The data key-value pairs for this example are "app_group_id" set as "your-app-group-id", "campaign_id" set as "your-campaign-id", and "trigger_properties**name" set as "Post Name".][10]

### Step 5: Create a Braze campaign

![A Braze push campaign with Liquid that references the trigger properties name. This Liquid will template your name into the message.][12]

Once you've successfully set up your zap, you can customize your Braze campaigns or Canvases with Wordpress data by using Liquid formatting to display the information in your messages.

[0]: {{site.baseurl}}/api/basics/#api-definitions
[1]: https://zapier.com/
[3]: {{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#creating-a-webhook
[5]:{% image_buster /assets/img_archive/zapier1.png %}
[6]:{% image_buster /assets/img_archive/zapier2.png %}
[7]:{% image_buster /assets/img_archive/zapier3.png %}
[8]:{% image_buster /assets/img_archive/zapier4.png %}
[10]:{% image_buster /assets/img_archive/zapier5.png %}
[12]:{% image_buster /assets/img_archive/zapier6.png %}