---
nav_title: Zendesk
article_title: Zendesk
page_order: 9
description: "This article outlines the partnership between Braze and Zendesk, a popular support suite that allows you to utilize Braze webhooks that can sync support data between the two platforms."
alias: /partners/zendesk/
page_type: partner
search_tag: Partner
---

# Zendesk

> [Zendesk Support Suite](https://www.zendesk.com/support-suite/) (ZSS) offers businesses the ability to have natural conversations with their customers through omnichannel support using email, webchat, voice, or social messaging apps. ZSS values customer support through tracking and prioritizing interactions, allowing businesses to have a unified historical view of their customers. Powerful tools such as a streamlined ticketing system allow businesses to reach out directly to customers with a personalized approach.

Braze offers a server-to-server integration with Zendesk, allowing you to utilize the Braze webhooks that can sync support ticket data between Braze and Zendesk.

## Requirements

| Requirement                                               | Origin  | Access                                                          | Description                                                                                                                                                                                                                    |
| --------------------------------------------------------- | ------- | --------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Zendesk Account & Account Information                     | Zendesk | https://`<your-zendesk-instance>`.zendesk.com/agent/admin | An active Zendesk Account __with admin privileges__ is required to utilize the Braze integration.<br><br>The Zendesk API token is necessary to be able to send requests from Braze to the Zendesk Ticket endpoint. |
| Common Identifier between Braze and Zendesk (Recommended) | Braze   | For more information, see our [User Profile Lifecycle][1] docs. | A [common identifier](#common-identifier) between Braze and Zendesk is recommended.                                                                                                                                            |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Braze and Zendesk integration
#### Create Zendesk tickets from Braze campaigns/Canvases

The Braze and Zendesk integration allows you to automate the creation of support tickets in Zendesk as a result of message engagement in user journeys in Braze. For example, after successfully implementing and testing the integration, Braze can create a support ticket from a user answering negatively to an in-app message with the question "Enjoying our App?", allowing your support team to reach out and offer assistance to the customer.

Complete the following steps to utilize the Braze webhook channel to send data to Zendesk.

### Step 1: Create a webhook campaign or Canvas
<br>
{% tabs %}
{% tab Campaign %}

To create a webhook, go to the **Campaigns** page on the Braze dashboard, under **Engagement**. <br>From the **Create Campaign** drop-down, select **Webhook** and name your campaign.

{% endtab %}
{% tab Canvas %}

To create a webhook, from a new or existing Canvas, create a full step or message step in the Canvas Builder. Next, click the green message icon that appears and then **Webhook** from the message options.

{% endtab %}
{% endtabs %}

### Step 2: Webhook settings
To set up the webhook, first, set the content type to JSON to communicate with Zendesk, as well as add in your Authorization information:

1. Create a key/value pair. Set `Content-Type` as the key and its value to `application/json`.<br><br>
2. Set `Authorization` as another key/value pair and its value as: <br />
{% raw %} `Basic {{ '<email_address>/token:<api_token>' | base64_encode }}` {% endraw %}<br><br>Replace `<email_address>` with your Zendesk Admin email and `<api_token>` with the API token generated following <a href="https://support.zendesk.com/hc/en-us/articles/226022787-Generating-a-new-API-token-\" f-id=">these instructions</a>. Please note that you must use Liquid syntax, therefore the __email address and API token should be in curly brackets__ as shown below. <br><br>!\[zendesk_step1\]\[3\]{: style="max-width:70%;"}

### Step 3: Webhook URL

Next, tell Braze where to send the webhook. For this ticket use case, the Webhook URL would be:

`<your-zendesk-instance>.zendesk.com/api/v2/tickets.json`.

Further use cases can be handled through [Zendesk Support APIs][4], which would change the `/api/v2/` endpoint accordingly at the end of the Webhook URL.

!\[zendesk_step2\]\[5\]{: style="max-width:70%;"}

### Step 4: Webhook payload
Next, define the ticket details like type, subject, and status in your webhook payload. Ticket details are extensible and can be customized based on the [Zendesk Ticket API][6]. To start filling out your payload, set the request body to `Raw Text`, then enter your desired fields. Please see below for an example:

{% raw %}
```
{% assign ticket_type = 'question/incident/task/problem' %} << Choose one >>
{% assign ticket_subject = '' %}
{% capture ticket_body %}
<< Your message here >>
{% endcapture %}
{% assign ticket_subject_tag = '' %}
{% assign ticket_status = 'New' %}

{
"ticket": {
"requester_id": "{{${user_id}}}", 
"requester": { "name": "{{${first_name}}} {{${last_name}}}", "email": "{{${email_address}}}", "phone": "{{${phone_number}}}"},
"type": "{{ ticket_type }}",
"subject":  "{{ticket_subject}}",
"comment":  { "body": "{{ticket_body}}" },
"priority": "urgent",
"status": "{{ ticket_status }}"
  }
}
```
{% endraw %}

In the example, you can see that the first part of this payload assigns the necessary variables, as well as the ticket type for the rest of the payload. The second part carries the specific information for the ticket.

### Step 5: Test your integration

In order to test your webhook, navigate to the Preview tab, and hit `Send Test`. You will then see if the call has been successful. Lastly, check if the ticket has been created on the Zendesk side.

!\[zdfinal\]\[7\]

## Common identifier

Should you have a common identifier between Braze and Zendesk, it would be best practice to utilize this as the `requester_id`. Alternatively, if this is not the case, pass on a set of identifying attributes such as name, email address, phone number, or others.
[3]: {% image_buster /assets/img_archive/zendesk_step1.gif %} [5]: {% image_buster /assets/img_archive/zendesk_step2.png %} [7]: {% image_buster /assets/img_archive/zdfinal.gif %}

[1]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/
[4]: https://developer.zendesk.com/rest_api/docs/support/introduction
[6]: https://developer.zendesk.com/rest_api/docs/support/tickets#create-ticket