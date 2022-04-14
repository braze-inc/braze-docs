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

> [Zendesk Support Suite](https://www.zendesk.com/support-suite/) (ZSS) offers businesses the ability to have natural conversations with their customers through omnichannel support using email, webchat, voice, or social messaging apps. Zendesk offers a streamlined ticketing system that values tracking and prioritizing interactions, allowing businesses to have a unified historical view of their customers.

The Braze and Zendesk server-to-server integration allows you to utilize Braze webhooks to automate the creation of support tickets in Zendesk as a result of message engagement in user journeys in Braze. For example, after successfully implementing and testing an integration, Braze can create a support ticket from a user answering negatively to an "Enjoying our App?" in-app message, allowing your support team to follow up with the customer.  

## Prerequisites

| Requirement | Description |
|---|---|
| Zendesk account | A [Zendesk admin account](https://`<your-zendesk-instance>`.zendesk.com/agent/admin) is required to take advantage of this partnership. |
| Zendesk API token | A Zendesk [API token][2] is required to send requests from Braze to the Zendesk ticket endpoint. |
| Common identifier (recommended) | A [common identifier](#common-identifier) between Braze and Zendesk is recommended. |
{: .reset-td-br-1 .reset-td-br-2}

## Integration

### Step 1: Create your Braze webhook
<br>
**Campaign**<br>To create a webhook, go to the **Campaigns** page in the Braze dashboard, under **Engagement**. From the **Create Campaign** drop-down, select **Webhook** and name your campaign.<br>
**Canvas**<br>To create a webhook, from a new or existing Canvas, create a full or message step in the Canvas builder. Next, click **Messages** and then select **Webhook** from the message options.

In your Webhook, fill out the following fields:
- **Webhook URL**: `<your-zendesk-instance>.zendesk.com/api/v2/tickets.json`
- **Request Body**: Raw Text

Further use cases can be handled through [Zendesk support APIs][4], which would change the `/api/v2/` endpoint accordingly at the end of the Webhook URL.

#### Request header and method

Zendesk requires an HTTP Header for authorization and an HTTP method. In the **Settings** tab, replace the <email_address> with your Zendesk admin email and <api_token> with your Zendesk API token.

- **HTTP Method**: POST
- **Request Headers**:
  - **Authorization**: Basic {% raw %} `{{ '<email_address>/token:<api_token>' | base64_encode }}` {% endraw %}
  - **Content-Type**: application/json

![][3]{: style="max-width:70%;"}

#### Request body

Define the ticket details like type, subject, and status in your webhook payload. Ticket details are extensible and customized based on the [Zendesk ticket API][6]. Use the following example to help structure your payload and enter your desired fields.

{% raw %}
```json
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

### Step 2: Preview your request

Your raw text will automatically highlight if it is an applicable Braze tag.

Preview your request in the left-hand panel or navigate to the **Test** tab, where you can select a random user, an existing user or customize your own to test your webhook.

Lastly, check if the ticket has been created on the Zendesk side.

## Common identifier

If you have a common identifier between Braze and Zendesk, it is recommended to utilize this as the `requester_id`, this will help unify the two sets of users. Alternatively, if this is not the case, we recommend passing a set of identifying attributes such as name, email address, phone number, or others.

[1]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/
[2]: https://support.zendesk.com/hc/en-us/articles/226022787-Generating-a-new-API-token-\
[3]: {% image_buster /assets/img_archive/zendesk_step1.gif %}
[4]: https://developer.zendesk.com/rest_api/docs/support/introduction
[5]: {% image_buster /assets/img_archive/zendesk_step2.png %}
[6]: https://developer.zendesk.com/rest_api/docs/support/tickets#create-ticket
[7]: {% image_buster /assets/img_archive/zdfinal.gif %}