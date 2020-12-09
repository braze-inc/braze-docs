---
nav_title: Zendesk
page_order: 9

description: "Braze and Zendesk integration through webhooks. Send custom data from Braze to create a ticket in Zendesk Support Suite"
alias: /partners/zendesk/

page_type: partner
hidden: false
---

# Zendesk

[Zendesk Support Suite](https://www.zendesk.com/support-suite/) (ZSS) offers businesses the ability to have natural conversations with their customers through omnichannel support, using email, web chat, voice or social messaging apps. ZSS values customer support through tracking and prioritising interactions, allowing businesses to have a unified historical view of the customer. Powerful tools such as a streamlined ticketing system allow businesses to reach out directly to customers with a personalised approach. 

Braze offers capacity for a bi-directional server-to-server integration, utilising webhooks to sync support ticket data between Braze and Zendesk.



## Requirements

| Requirement | Origin | Access | Description |
|---|---|---|---|
| Zendesk Account & Account Information | Zendesk | https://`<your-zendesk-instance>`.zendesk.com/agent/admin | An active Zendesk Account (with administrator privileges) is required to utilise the Braze integration. The Zendesk API token is necessary to be able to send requests from Braze to the Zendesk Ticket endpoint. |
| Common Identifier between Braze and Zendesk | Braze | For more information, see our [User Profile Lifecycle] [1] docs | A matching identifier is required. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Braze → Zendesk Integration
### Create tickets in Zendesk directly from Braze Campaign/Canvas

This process will allow you to automate the creation of support tickets in Zendesk as a result of message engagement in user journeys from Braze. For example, creating a support ticket from a user answering negatively to an in-app message with the question “Enjoying our app?”, allowing your support team to reach out and offer assistance to the customer.

Here, you will utilise the Braze webhook channel to send data to Zendesk.

### Step 1: Create a Campaign/Canvas Step using the webhook channel  
<br />

![zd11] [8]

### Step 2: Webhook Settings
In order to setup the webhook, first you set the language as JSON to communicate with Zendesk, as well as add in our authentication:

1. Create a key/value pair. Set “Content-Type” as the key and its value to “application/json”.

2. Set "Authorization" as another key and its value as: <br /> 
{% raw %} `Basic {{ '<email_address>/token:<api_token>' | base64_encode }}` {% endraw %}

Email address is your Zendesk Admin email and api_token is the API generated following [these instructions] [2]. Please note that we are using Liquid syntax, therefore the email address and API token should be in curly brackets as shown below. 

![zendesk_step1] [3]

### Step 3: Webhook URL

Next, you need to tell Braze where to send the webhook. For this use case of creating a ticket, the Webhook URL would be:

`<your-zendesk-instance>.zendesk.com/api/v2/tickets.json`. 

Further use cases can be handled through [Zendesk Support APIs] [4], which would change the /api/v2/ endpoint accordingly at the end of the Webhook URL.

![zendesk_step2] [5]

### Step 4: Webhook Payload
Now define the details about the ticket created in Zendesk, such as ticket type, subject and status. To do this, keep the request body as ‘Raw Text’, then you start filling your payload. Please see below for an example: 

Keeping Request Body as Raw Text, you can start filling in your payload. We have already set up a Webhook Template called Zendesk: Create Ticket with some predefined fields:

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

The first part of this request is assigning the variables, as well as the ticket type for the main part of the payload. The remainder carries the specific information for the ticket. 

Please note the above fields of the payload are extensible and can be customised based on the [Zendesk Ticket API] [6]. 

### Step 5: Test

In order to test your webhook, navigate to the Preview tab and hit ‘Send Test’. You will then see if the call has been successful. Now, check if the ticket has been created on the Zendesk side.


![zdfinal] [7]

## Common Identifier

Should you have a common identifier between Braze and Zendesk, it would be best practice to utilise this as the ‘requester_id’. Alternatively, if this is not the case, pass on a set of identifying attributes such as name, email address, phone number or others.


[1]: https://www.braze.com/docs/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/
[2]: https://support.zendesk.com/hc/en-us/articles/226022787-Generating-a-new-API-token-\
[3]: {% image_buster /assets/img_archive/zendesk_step1.gif %}
[4]: https://developer.zendesk.com/rest_api/docs/support/introduction
[5]: {% image_buster /assets/img_archive/zendesk_step2.png %}
[6]: https://developer.zendesk.com/rest_api/docs/support/tickets#create-ticket
[7]: {% image_buster /assets/img_archive/zdfinal.gif %}
[8]: {% image_buster /assets/img_archive/zd11.gif %}
