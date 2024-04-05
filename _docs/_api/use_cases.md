---
nav_title: API Use Cases
article_title: API Use Cases
description: "Whether you’re a proficient developer or a marketer with minimal developer resources, this reference article is designed to help you understand how to leverage the power of the Braze REST API to accomplish various tasks and enhance your customer engagement strategy."
page_type: reference
page_order: 4.8
---

# Use cases

> The Braze REST API provides a wide range of endpoints designed to help manage and optimize your customer engagement strategy. In this article, we’ll explore several use cases for each endpoint category: catalogs, email lists and addresses, export, messages, preference center, SMS, subscription groups, templates, and user data.<br><br>Each section introduces a scenario with a step-by-step guide, code sample, and expected outcome. By the end of this guide, you’ll better understand how to use the Braze REST API to enhance your customer engagement efforts.

## Braze REST API collection

| Collection                                                                 | Purpose                                                                               |
|----------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| [Catalogs]({{site.baseurl}}/api/endpoints/catalogs/)                       | Create and manage catalogs and catalog items to reference in your Braze campaigns.    |
| [Cloud Data Ingestion]({{site.baseurl}}/api/endpoints/cdi/)                | Manage your data warehouse integrations and syncs.                                    |
| [Email lists and addresses]({{site.baseurl}}/api/endpoints/email/)         | Set up and manage bi-directional sync between Braze and your email systems.           |
| [Export]({{site.baseurl}}/api/endpoints/export/)                           | Access and export various details of your campaigns, Canvases, KPIs, and more.        |
| [Messages]({{site.baseurl}}/api/endpoints/messaging/)                      | Schedule, send, and manage your campaigns and Canvases.                               |
| [Preference center]({{site.baseurl}}/api/endpoints/preference_center/)     | Build your preference center and update the styling of it.                            |
| [SCIM]({{site.baseurl}}/api/endpoints/scim/)                               | Manage user identifies in cloud-based applications and services.                      |
| [SMS]({{site.baseurl}}/api/endpoints/sms/)                                 | Manage your users' phone numbers in your subscription groups.                         |
| [Subscription groups]({{site.baseurl}}/api/endpoints/subscription_groups/) | List and update both SMS and email subscription groups stored in the Braze dashboard. |
| [Templates]({{site.baseurl}}/api/endpoints/templates/)                     | Create and update templates for email messaging and Content Blocks.                   |
| [User data]({{site.baseurl}}/api/endpoints/user_data/)                     | Identify, track, and manage your users.                                               |
{: .reset-td-br-1 .reset-td-br-2}

## Updating multiple items in a catalog



## Removing emails from the Braze spam list

At MovieCanon, a streaming services company, the developer team is responsible for periodically auditing their email lists to identify and keep users who are subscribed to their email campaigns. As part of this audit, they want to remove this list of emails from their spam list:

- august.author.example.com
- betty.benson@example.com
- charlie.chase@example.com
- delilah.york@example.com
- evergreen.rebecca@example.com

To accomplish this task, you’ll need an API key with the `email.spam.remove` permission to use the `/email/spam/remove` endpoint. This endpoint removes email addresses from your Braze spam list and the spam list maintained by your email provider.

To send this request, you must have a string email address or an array of up to 50 email addresses to modify. Since MovieCanon’s list of emails is under 50, we can accomplish this task with the following request body:

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "email": ["august.author.example.com","betty.benson@example.com","charlie.chase@example.com","delilah.york@example.com","evergreen.rebecca@example.com"]
}
```

After sending this payload successfully, we’ll see this response that confirms the emails have been removed from MovieCanon’s spam list.

```json
{
  "message": "success"
}
```

## Auditing all Canvases

Siege Valley Health is a hospital system that includes 10 operating hospitals and research centers with thousands of patients. Their marketing team wants to compare the Canvases sent to their patients to remind them to schedule an appointment for their flu shots from their past 3 years of using Braze. Siege Valley Health’s marketing team also wants a quick and efficient way to see both the list of Canvases and the analytics summary.

Let’s dive into how we can accomplish these two tasks using a combination of endpoints rather than filtering through the Braze dashboard.

{% details Here’s the response that the Seige Valley Health marketing team would receive. %}

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "canvases" : [
  	{
  		"id" : (string) the Canvas API identifier,
  		"last_edited": (ISO 8601 string) the last edited time for the message,
  		"name" : (string) the Canvas name,
  		"tags" : (array) the tag names associated with the Canvas formatted as strings,
  	},
  	{
  		"id" : (string) the Canvas API identifier,
  		"last_edited": (ISO 8601 string) the last edited time for the message,
  		"name" : (string) the Canvas name,
  		"tags" : (array) the tag names associated with the Canvas formatted as strings,
  	},
    ... (more Canvases)
  ],
  "message": 'success'
}
```

{% enddetails %}

Let’s move on to the next task of viewing the analytics summary for the first Canvas from Seige Valley Health’s list of Canvases.

## Checking upcoming scheduled campaigns and Canvases

## Viewing an older preference center


## Removing invalid phone numbers

At CashBlastr, their primary goal is to streamline how people can send and receive quick payments. As a financial service company, they want to keep their list of phone numbers for their customers up-to-date and accurate. Their developer team has been tasked to remove the following list of phone numbers that have been marked as “invalid” so the marketing team’s SMS messages can reach the appropriate CashBlastr customers.

- 12223135467
- 12183095514
- 14235662245
- 14324567892

To send this request, the phone numbers must be in an array of strings in e.164 format, with up to 50 phone numbers per request. Because the list doesn’t exceed 50 phone numbers, here’s an example of the request body CashBlastr’s developer team would send:

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "phone_numbers": ["12183095514","14255551212"]
}
```

After sending this payload successfully, we’ll see this response that confirms the invalid phone numbers from CashBlastr have been removed from the Braze invalid list.

```json
{
  "message": "success"
}
```


## Viewing a user's subscription groups




## Updating an HTML template for email messaging

At WorkFriends, a social network for helping build connections between workers from different industries, their marketing team is responsible for sending email campaigns to their users. These campaigns often include reminders for local events, weekly newsletters, and profile activity highlights.

In this scenario, let’s say WorkFriends has historically used a singular HTML template with its legacy branding. In an effort to align their brand identity, they want to see if there’s any helpful information in this HTML template before transitioning to a new template.

{% details Here’s the response that the WorkFriends team would receive. %}

```json
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
{
  "email_template_id": (string) Your email template's API Identifier,
  "template_name": (string) The name of your email template,
  "description": (string) The email template description,
  "subject": (string) The email template subject line,
  "preheader": (optional, string) The email preheader used to generate previews in some clients),
  "body": (optional, string) The email template body that may include HTML,
  "plaintext_body": (optional, string) A plaintext version of the email template body,
  "should_inline_css": (optional, boolean) Whether there is inline CSS in the body of the template - defaults to the css inlining value for the workspace,
  "tags": (string) Tag names,
  "created_at": (string) The time the email was created at in ISO 8601,
  "updated_at": (string) The time the email was updated in ISO 8601
}
```

{% enddetails %}

After reviewing this template information, you can also use the `/templates/email/update` endpoint to update the email template via API. You’ll see the edits reflected in the Braze dashboard.