---
nav_title: Zendesk
article_title: Zendesk
description: "This reference article outlines the partnership between Braze and Zendesk, a popular support suite that allows you to utilize Braze webhooks that can sync support data between the two platforms."
alias: /partners/zendesk/
page_type: partner
search_tag: Partner

---

# Zendesk

> [Zendesk Support Suite](https://www.zendesk.com/support-suite/) (ZSS) offers businesses the ability to have natural conversations with their customers through omnichannel support using email, webchat, voice, or social messaging apps. Zendesk offers a streamlined ticketing system that values tracking and prioritizing interactions, allowing businesses to have a unified historical view of their customers.

The Braze and Zendesk server-to-server integration allows you to utilize: 
- Braze webhooks to automate the creation of support tickets in Zendesk due to message engagement in user journeys in Braze. For example, after successfully implementing and testing an integration, Braze can create a support ticket from a user answering negatively to an "Enjoying our App?" in-app message, allowing your support team to follow up with the customer.
- Zendesk webhooks to support bi-directional use cases like updating the user profile in Braze due to activity in Zendesk. For example, after a ticket is solved, log an event to the user profile in Braze.

## Prerequisites

| Requirement | Description |
|---|---|
| Zendesk account | A [Zendesk admin account](https://`<your-zendesk-instance>`.zendesk.com/agent/admin) is required to take advantage of this partnership. |
| Zendesk API token | A Zendesk [API token](https://support.zendesk.com/hc/en-us/articles/226022787-Generating-a-new-API-token-) is required to send requests from Braze to the Zendesk ticket endpoint. |
| Common identifier (recommended) | A [common identifier](#common-identifier) between Braze and Zendesk is recommended. |
| Braze API key | A Braze API key is required to send requests from Zendesk to a Braze endpoint. Ensure that the API key you use has the correct permissions for the Braze endpoint your Zendesk webhook is using. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Braze to Zendesk integration

### Step 1: Create your Braze webhook

To create a webhook:

- **Campaigns:** Go to the **Campaigns** page in the Braze dashboard. Click **Create Campaign** and select **Webhook**.
- **Canvas:** From a new or existing Canvas, create a full or message step in the Canvas builder. Next, click **Messages** and select **Webhook** from the message options.

In your webhook, fill out the following fields:
- **Webhook URL**: `<your-zendesk-instance>.zendesk.com/api/v2/tickets.json`
- **Request Body**: Raw Text

Further use cases can be handled through [Zendesk support APIs](https://developer.zendesk.com/rest_api/docs/support/introduction), which would change the `/api/v2/` endpoint accordingly at the end of the webhook URL.

#### Request header and method

Zendesk requires an HTTP header for authorization and an HTTP method. In the **Settings** tab, replace the <email_address> with your Zendesk admin email and <api_token> with your Zendesk API token.

- **HTTP Method**: POST
- **Request Headers**:
  - **Authorization**: Basic {% raw %} `{{ '<email_address>/token:<api_token>' | base64_encode }}` {% endraw %}
  - **Content-Type**: application/json

![]({% image_buster /assets/img_archive/zendesk_step1.gif %}){: style="max-width:70%;"}

#### Request body

Define the ticket details like type, subject, and status in your webhook payload. Ticket details are extensible and customized based on the [Zendesk ticket API](https://developer.zendesk.com/rest_api/docs/support/tickets#create-ticket). Use the following example to help structure your payload and enter your desired fields.

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

Your raw text will automatically highlight if it's an applicable Braze tag.

Preview your request in the **Preview** panel or navigate to the **Test** tab, where you can select a random user or an existing user or customize your own to test your webhook.

Lastly, check if the ticket has been created on the Zendesk side.

## Common identifier

If you have a common identifier between Braze and Zendesk, it is recommended to utilize this as the `requester_id`. This will help unify the two sets of users. Alternatively, if this is not the case, we recommend passing a set of identifying attributes such as name, email address, phone number, or others.

## Zendesk to Braze integration

### Step 1: Create a webhook

1. In the [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click **Apps and integrations** in the sidebar, then select **Webhooks > Webhooks**.<br><br>
2. Click **Create webhook**.<br><br>
3. Select **Trigger** or **Automation** and click **Next**.<br>![]({% image_buster /assets/img_archive/zendesk2.png %}){: style="max-width:70%;"}<br><br>
4. Provide the following information in your webhook:
- Enter a name and description for the webhook.
- Enter the Braze endpoint URL your webhook will use. {% raw %}Our example will use `https://{{instance_url}}/users/track`.{% endraw %}
- Select POST as the webhook's request method and set the request format to JSON.
- Select the bearer token authentication method for the webhook and provide your [Braze API key]({{site.baseurl}}/api/basics/#creating-and-managing-rest-api-keys).
  - Make sure that the API key you are using has the [correct permissions]({{site.baseurl}}/api/basics/#rest-api-key-permissions) for the Braze endpoint your webhook is using.<br><br>
5. (Recommended) Test the webhook to check it's working properly.<br><br>
6. For trigger and automation webhooks, you must connect the webhook to a trigger or automation before finishing the setup. Refer to the following step for our example of creating a trigger for the webhook. After the trigger is created, you can return to this page and select **Finish setup**.

### Step 2: Create a trigger or automation

[Follow Zendesk’s instructions](https://support.zendesk.com/hc/en-us/articles/4408839108378#topic_bwm_1tv_dpb) on how to connect your webhook to a trigger or automation.

Our example below will use a trigger to invoke the webhook when a support case status has been changed to "Solved" or "Closed". 

1. In the **Admin Center**, click **Objects and rules** in the sidebar, then select **Business rules > Triggers**.<br><br>
2. Select **Add trigger**.<br><br>
3. Name your trigger and select a category.<br><br>
4. Select **Add condition** to set up which conditions should trigger the webhook. For example, "Status category changed to closed" or "Status category changed to solved".![]({% image_buster /assets/img_archive/zendesk1.png %}){: style="max-width:70%;"}<br><br>
5. Select **Add action**, choose **Notify active webhook**, and select from the dropdown the webhook created in the previous step.<br><br>
6. Define the JSON body to conform to your Braze endpoint, using Zendesk variable placeholders to dynamically populate the relevant fields.<br>![]({% image_buster /assets/img_archive/zendesk3.png %}){: style="max-width:70%;"}<br><br>
7. Select **Create**.<br><br>
8. Return to your webhook and click **Finish setup**.


