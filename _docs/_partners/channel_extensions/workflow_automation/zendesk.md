---
nav_title: Zendesk
page_order: 1

description: "Braze and Zendesk integration through webhooks. Send custom data from Braze to create a ticket in Zendesk Support Suite"
alias: /partners/zendesk/

page_type: partner
hidden: false
---

# Zendesk

[Zendesk Support Suite](https://www.zendesk.com/support-suite/) (ZSS) offers businesses to have natural conversations with their customers through an omnichannel support, whether it’s email, chat, voice or social messaging apps. ZSS values customer support through tracking and prioritising interactions, allowing businesses to have a unified view of the customer through pulling in previous history too. Powerful tools such as a streamlined ticketing system allows businesses to reach out directly to customers with a personalised approach. 

Braze offers capacity for a bi-directional server-to-server integration, utilising webhooks to sync support ticket data between Braze and Zendesk.

## Requirements

| Requirement | Origin | Access | Description |
|---|---|---|---|
| Zendesk Account & Account Information | Zendesk | https://`<your-zendesk-instance>`.zendesk.com/agent/admin | An active Zendesk Account (with administrator privileges) is required to utilise the Braze integration. The Zendesk API token is necessary to be able to send requests from Braze to the Zendesk Ticket endpoint. |
| Common Identifier between Braze and Zendesk | Braze | For more information, see our [User Profile Lifecycle] [1] docs | A matching identifier is required. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Braze → Zendesk Integration
### Create tickets in Zendesk directly from Braze Campaign/Canvas

This process will allow you to automate the creation of support tickets in Zendesk as a result of message engagement of user journeys within Braze. For example, creating a support ticket from a user answering negatively to an in-app message with the question “Enjoying our app?”, allowing your support team to reach out and offer assistance to the customer.

Here, we utilise the Braze webhook channel to send data to Zendesk.

Using this webhook template, customers can easily automate the creation of support tickets as a result of a user’s journey or message engagement within Braze. For example, you may want to automatically create a support ticket when a user receives a Braze in-app message that asks “Do you like our app?” and the user clicks “No”, so that your support team can reach out and offer help to satisfy the customer. 

### Step 1: Webhook Channel Settings
#### 1a

Create a key/value pair. Setting “Content-Type” as the key and its value to “application/json”.

####  1b

Set Authorization as another key and its value as 
{% raw %} `Basic {{ '<email_address>/token:<api_token>' | base64_encode }}` {% endraw %}, where email address is your Zendesk Admin email and api_token is the API generated following [these instructions] [2]. Please note that we are using Liquid syntax, therefore the email address and API token should be in curly brackets as shown below. 

![zendesk_step1] [3]


### Step 2: Webhook URL

For this use case of creating a ticket, the Webhook URL would be:

`<your-zendesk-instance>.zendesk.com/api/v2/tickets.json`. 

Further use cases can be handled through [Zendesk Support APIs] [4], which would change the /api/v2/ endpoint accordingly at the end of the Webhook URL.

![zendesk_step2] [5]

### Step 3: Webhook Payload

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
"type": "{{ ticket_type }}",
"subject":  "{{ticket_subject}}",
"comment":  { "body": "{{ticket_body}}" },
"priority": "low/normal/high/urgent",
"status": "{{ ticket_status }}"
  }
}
```
{% endraw %}

Please note the above fields of the payload are extensible and can be customised based on the [Zendesk Ticket API] [6]. 

### Step 4: Test

In the Test section you can ‘Send Test’ to preview if the ticket has been created on the Zendesk side.

![zendesk_test] [7]

## User ID

In this case, as we know that our unique identifier matches between Braze and Zendesk, we have set the ‘requester_id’ field to be the Braze external_id {% raw %} `({{${user_id}}}` {% endraw %} field). Other standard attributes can be used, such as {% raw %} `{{${email_address}}}`  {% endraw %} or {% raw %} `{{${phone}}}`  {% endraw %} .

We realise that user_id, email or phone numbers may not be the optimal solution for all customers to have a common identifier between Braze and Zendesk. An alternative method could utilise a custom attribute in the Braze profile to hold the unique_id of the Zendesk user, with that value called as the requester_id each time.


[1]: https://www.braze.com/docs/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/
[2]: https://support.zendesk.com/hc/en-us/articles/226022787-Generating-a-new-API-token-\
[3]: {% image_buster /assets/img_archive/zendesk_step1.gif %}
[4]: https://developer.zendesk.com/rest_api/docs/support/introduction
[5]: {% image_buster /assets/img_archive/zendesk_step2.png %}
[6]: https://developer.zendesk.com/rest_api/docs/support/tickets#create-ticket
[7]: {% image_buster /assets/img_archive/zendesk_test.gif %}
