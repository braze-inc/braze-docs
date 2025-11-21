---
nav_title: Zapier
article_title: Zapier
alias: /partners/zapier/
description: "This reference article outlines the partnership between Braze and Zapier, an automation web tool that allows you to share data between web apps, and use that information to automate actions."
page_type: partner
search_tag: Partner

---
# Zapier integration

> [Zapier](https://zapier.com/) is an automation web tool that allows you to share data between web apps and then use that information to automate actions. 

The Braze and Zapier partnership leverages the Braze API and Braze [webhooks]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#creating-a-webhook) to connect with third-party applications—such as Google Workplace, Slack, Salesforce, WordPress, etc. to automate various actions.

## Prerequisites

| Requirements | Description |
|---|---|
| Zapier account | A Zapier account is required to take advantage of this partnership. |
| Braze REST endpoint | Your REST endpoint URL. Your endpoint will depend on the [Braze URL for your instance]({{site.baseurl}}/api/basics/#api-definitions). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

In the following Zapier example, we will be sending information from WordPress to Braze using a POST webhook. This information can then be used to create a Braze Canvas.

### Step 1: Create a Zapier trigger

Using Zapier's terminology, a "zap" is an automated workflow that connects your apps and services. The first part of any zap is to designate a trigger. After your zap is enabled, Zapier will automatically perform the respective actions whenever your trigger is detected.

Using our WordPress example, in the Zapier platform, we'll set up our zap to trigger when a new WordPress post gets added and select **Published** and **Posts** as **Post Status** and **Post Type**. 

![In the Zapier platform, within a zap, select the trigger to be a "new comment", "any webhook", or "new post". For this example, "new post" is selected. ] [5]

![In the Zapier platform, within a zap, configure the trigger by selecting the desired post status and post type. For this example, "Published", and "Posts" is selected.] [6]

### Step 2: Add an action webhook

Next, define the zap action. When your zap is enabled, and your trigger is detected, the action will automatically occur.

Continuing our example, we want to send a POST request as a JSON to a Braze endpoint. This can be done by selecting the **Webhooks** option under **Apps**.

![]({% image_buster /assets/img_archive/zapier3.png %})

### Step 3: Set up Braze POST

When setting up your webhook, use the following settings and provide your Braze REST endpoint in the webhook URL. When complete, select **Publish**.

- **Method** : POST
- **Webhook URL**: `https://rest.iad-01.braze.com/canvas/trigger/send`
- **Data Pass-Though**: False
- **Unflatten**: No
- **Request Header**:
  - **Content-Type**: application/json
  - **Authorization**: Bearer YOUR-API-KEY
- **Data**: 

```json
{
  "canvas_id": "your_canvas_identifier",
  "recipients": [
    {
      "external_user_id": "external_user_identifier",
      "canvas_entry_properties":{
        "string_property": "Your example string",
        "example_integer_property": 1
      }
    }
  ]
}
```

![]({% image_buster /assets/img/zapier.png %}){: style="max-width:70%;"}

### Step 4: Create a Braze campaign

Once you've successfully set up your zap, you can customize your Braze campaigns or Canvases with WordPress data by using Liquid formatting to display the information in your messages.

[5]: {% image_buster /assets/img_archive/zapier1.png %}
[6]: {% image_buster /assets/img_archive/zapier2.png %}
