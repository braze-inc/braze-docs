---
nav_title: MyPostcard
article_title: MyPostcard
page_order: 1
description: "This reference article outlines the partnership between Braze and MyPostcard, which enables you to use direct mail as an additional channel for your CRM workflow."
alias: /partners/mypostcard/
page_type: partner
search_tag: Partner

---

# MyPostcard

> [MyPostcard][1], a leading global postcard app, empowers businesses to execute direct mail campaigns with ease, providing a seamless and profitable way to connect with customers. 

Use the MyPostcard and Braze integration to effortlessly send your customers print mailings.

## Prerequisites

| Requirement                      | Description                                                                                                             |
|----------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| MyPostcard B2B account           | Registering with MyPostcard is required to take advantage of this integration.                                          |
| B2B API key & Credentials        | You can find your API Key and the credentials in the MyPostcard B2B Admin Tool.                                         |
| Approved MyPostcard B2B Campaign | In order to take advantage of this integration, you need to set up a print mailing campaign in the MyPostcard B2B Tool. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Use cases

To elevate your direct mail campaigns, it’s crucial to move beyond traditional mass mailings and integrate this channel seamlessly into your workflows. This approach allows you to reach specific customers who have opted out of your email newsletters or whose emails are getting marked as spam. With MyPostcard, you can effortlessly send print mailing campaigns directly through Braze.
- Build intuitive workflows in Braze, incorporating print mail as a powerful new channel, all without any technical expertise.
- Unlock the potential of personalized print mailings with just a few simple steps.
- Benefit from fast & easy implementation, backed by personalized support from our dedicated team.

## Integration

To integrate with MyPostcard, Simply [sign up here][2] and create your first campaign to use it via [braze webhooks][3].

### Step 1: Create your Braze webhook template

To create an MyPostcard webhook template to use in future campaigns or Canvases, navigate to Templates > Webhook Templates in the Braze platform.

{% alert note %}
If you are using the [older navigation]({{site.baseurl}}/navigation), go to **Engagement** > **Templates & Media** > **Webhook Templates**.
{% endalert %}

If you would like to create a one-off MyPostcard webhook campaign or use an existing template, select **Webhook** in Braze when creating a new campaign.

In your new Webhook template, fill out the following fields:
- **Webhook URL**: The Webhook URL as shown in the B2B Admin Tool
- **Request Body**: Raw Text (JSON format to be found in the B2B Admin Tool)

#### Request headers and method

MyPostcard requires an HTTP Header for authorization and an HTTP method to be included in the template.

- **HTTP Method**: POST
- **Request Headers**:
  - **username**: {% raw %} `{{ '<username>' }}` {% endraw %}
  - **password**: {% raw %} `{{ '<password>' }}` {% endraw %}
  - **Content-Type**: application/json

#### Request body

Just copy the request body displayed in the B2B Admin, then fill in the placeholders with content using any Liquid personalization tags.

![Compose Tab showing the JSON body and webhook information.][4]

### Step 2: Preview your request

Next, preview your request in the **Preview** panel or go to the **Test** tab, where you can choose a random user, an existing user, or create a custom user to test your webhook. Don’t forget to save your template before leaving the page!

![Test Webhook Tab with different fields to validate the implementation.][5]

{% alert important %}
Remember to save your template before leaving the page! <br>Updated webhook templates can be found in the **Saved Webhook Templates** list when creating a new [webhook campaign]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/). 
{% endalert %}

[1]: https://www.mypostcard.com
[2]: https://www.mypostcard.com/b2b/admin/
[3]: https://www.braze.com/docs/user_guide/message_building_by_channel/webhooks
[4]: {% image_buster /assets/img/mypostcard/mypostcard_compose.jpg %}
[5]: {% image_buster /assets/img/mypostcard/mypostcard_test.jpg %}
