---
nav_title: Email Templates
page_order: 1
search_rank: 3
---

# Email Templates

Use the Email Template REST APIs to programmatically manage the email templates that you have stored on the Braze dashboard, on the Templates & Media page. Braze provides two endpoints for creating and updating your email templates.

## Creating Email Templates

Use the endpoints below to create email templates on the Braze dashboard. These templates will be available on the Templates and Media page. The response from this endpoint will include a field for `email_template_id`, which can be used to update the template in subsequent API calls.

Instance  | REST Endpoint
----------|------------------------------------------------
US-01 | `https://rest.iad-01.braze.com/templates/email/create`
US-02 | `https://rest.iad-02.braze.com/templates/email/create`
US-03 | `https://rest.iad-03.braze.com/templates/email/create`
US-04 | `https://rest.iad-04.braze.com/templates/email/create`
US-06 | `https://rest.iad-06.braze.com/templates/email/create`
EU-01 | `https://rest.fra-01.braze.eu/templates/email/create`

```yaml
POST https://YOUR_REST_API_URL/templates/email/create
  
  endpoint: create email template
  endpoint_url: /templates/email/create
  method: post
  description: use to create email templates in your Braze account.
  response_details: response from this endpoint will include a field for email_template_id, which can be used to update the template in subsequent API calls.
  query_parameters:
    template_name: (required, string) the name of your email template,
    subject: (required, string) the email template subject line,
    body: (required, string) the email template body that may include HTML,
    plaintext_body: (optional, string) a plaintext version of the email template body,
    preheader: (optional, string) the email preheader used to generate previews in some clients 
  query_example: 'https://rest.iad-01.braze.com/templates/email/info?api_key=123abc-def5-3729-owod-23f9f3j30& email_template_id=759c2ad9-eefc-4af1-bde4-602630644935'
  response_body_parameters: 
    email_template_id: (string) your email template's API Identifier,
    template_name: (string) the name of your email template,
    subject: (string) the email template subject line,
    preheader: (optional, string) the email preheader used to generate previews in some clients),
    body: (optional, string) the email template body that may include HTML,
    plaintext_body: (optional, string) a plaintext version of the email template body,
    tags: (string) tag names,
    created_at: (string, in ISO 8601),
    updated_at: (string, in ISO 8601),
  link_to_swagger: 'https://www.braze.com/docs/api/interactive/#/operations/Email%20Templates/CreateEmailTemplate'
  errors:
  glossary_tags: email, post_method


  

```

## Updating Email Templates

Use the endpoints below to update email templates on the Braze dashboard. You can access an email template's `email_template_id` by navigating to it on the Templates and Media page. The email template creation API endpoint will also return an `email_template_id` reference.

All fields other than the `api_key` and `email_template_id` are optional, but you must specify at least one field to update.

Instance  | REST Endpoint
----------|------------------------------------------------
US-01 | `https://rest.iad-01.braze.com/templates/email/update`
US-02 | `https://rest.iad-02.braze.com/templates/email/update`
US-03 | `https://rest.iad-03.braze.com/templates/email/update`
US-04 | `https://rest.iad-04.braze.com/templates/email/update`
US-06 | `https://rest.iad-06.braze.com/templates/email/update`
EU-01 | `https://rest.fra-01.braze.eu/templates/email/update`


```yaml
POST https://YOUR_REST_API_URL/templates/email/update

endpoint: update email templates
endpoint_url: /templates/email/update
method: post
description: use to update email templates on the Braze dashboard.
response_details: will return updated email template.

query_parameters:
  api_key: (required, string) your App Group REST API Key,
  email_template_id: (required, string) your email template's API Identifier,
  template_name: (optional, string) the name of your email template,
  subject: (optional, string) the email template subject line,
  body: (optional, string) the email template body that may include HTML,
  plaintext_body: (optional, string) a plaintext version of the email template body,
  preheader: (optional, string) the email preheader used to generate previews in some clients

query_example: https://rest.iad-01.braze.com/templates/email/update?api_key=123abc-def5-3729-owod-23f9f3j30& email_template_id=759c2ad9-eefc-4af1-bde4-602630644935

response_body_parameters:
link_to_swagger: https://www.braze.com/docs/api/interactive/#/operations/Email%20Templates/UpdateEmailTemplate
errors: 401
glossary_tags: email

```



## List Email Templates Available

Use the endpoints below to get a list of available templates.

Instance  | REST Endpoint
----------|------------------------------------------------
US-01 | `https://rest.iad-01.braze.com/templates/email/list`
US-02 | `https://rest.iad-02.braze.com/templates/email/list`
US-03 | `https://rest.iad-03.braze.com/templates/email/list`
US-04 | `https://rest.iad-04.braze.com/templates/email/list`
US-06 | `https://rest.iad-06.braze.com/templates/email/list`
EU-01 | `https://rest.fra-01.braze.eu/templates/email/list`


### Request Parameters

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `api_key`  | Yes | String | Your App Group REST API Key. |
| `modified_after`  | No | String in ISO 8601 | Retrieve only templates updated at or after the given time. |
| `modified_before`  |  No | String in ISO 8601 | Retrieve only templates updated at or before the given time. |
| `limit` | No | Positive Number | Maximum number of templates to retrieve, default to 100 if not provided, maximum acceptable value is 1000. |
| `offset`  |  No | Positive Number | Number of templates to skip before returning rest of the templates that fit the search criteria. |


```yaml
GET https://YOUR_REST_API_URL/templates/email/list

endpoint: list email templates
endpoint_url: /templates/email/list
method: get
description: use to get a list of available templates.

parameters:
  api_key: (required, string) your App Group REST API Key
  modified_after: (string, in ISO 8601) retrieve only templates updated at or after the given time. 
  modified_before: (string, in ISO 8601) retrieve only templates updated at or before the given time.
  limit: (positive integer) maximum number of templates to retrieve, default to 100 if not provided, max 1000.
  offset: (positive integer) number of templates to skip before returning rest of the templates that fit the search criteria.
  
request_body_example: https://rest.iad-01.braze.com/templates/email/list?api_key=123abc-def5-3729-owod-23f9f3j30
response_body_parameters: 
  count: number of templates returned
  templates:
    email_template_id: (string) your email template's API Identifier,
    template_name: (string) the name of your email template,
    created_at: (string, in ISO 8601),
    updated_at: (string, in ISO 8601)
link_to_swagger: https://www.braze.com/docs/api/interactive/#/operations/Email%20Templates/ListEmailTemplates
errors:
glossary_tags: email

```



## See Email Template Information

Use the endpoints below to get information on your email templates.

Instance  | REST Endpoint
----------|------------------------------------------------
US-01 | `https://rest.iad-01.braze.com/templates/email/info`
US-02 | `https://rest.iad-02.braze.com/templates/email/info`
US-03 | `https://rest.iad-03.braze.com/templates/email/info`
US-04 | `https://rest.iad-04.braze.com/templates/email/info`
US-06 | `https://rest.iad-06.braze.com/templates/email/info`
EU-01 | `https://rest.fra-01.braze.eu/templates/email/info`

### Request Parameters

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `api_key`  | Yes | String | Your App Group REST API Key. |
| `email_template_id`  | Yes | String | Your email template’s API Identifier. |


https://rest.iad-01.braze.com/templates/email/info?api_key=123abc-def5-3729-owod-23f9f3j30& email_template_id=759c2ad9-eefc-4af1-bde4-602630644935


```yaml
GET https://YOUR_REST_API_URL/templates/email/info

endpoint: see email information
endpoint_url: /templates/email/info
method: get
description: to get information on your email templates.

parameters:
  api_key: (required, string) your App Group REST API key as found in your Developer Console.
  email_template_id: (required, string) the ID of your already existing email template.
  
request_body_example: https://rest.iad-01.braze.com/templates/email/info?api_key=123abc-def5-3729-owod-23f9f3j30& email_template_id=759c2ad9-eefc-4af1-bde4-602630644935

response_body_parameters:

link_to_swagger: https://www.braze.com/docs/api/interactive/#/operations/Email%20Templates/SeeEmailTemplateInformation
errors:
glossary_tags: email

```

Images in this response will show in the "body" variable as HTML.
