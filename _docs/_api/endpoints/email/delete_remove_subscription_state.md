---
nav_title: "DELETE: Delete subscription state by email address or phone number"
article_title: "DELETE: Delete Subscription State by Email Address or Phone Number"
search_tag: Endpoint
page_order: 0
hidden: true
layout: api_page
page_type: reference
description: "This article outlines the details about the Delete subscription state by email address or phone number Braze endpoint."

---

{% api %}
# Delete subscription state by email address or phone number
{% apimethod delete %}
/users/subscription
{% endapimethod %}

> Use this endpoint to delete the subscription state value based on an email address or phone number.

## Request parameters

| Parameter | Required | Data Type | Description |
| --- | --- | --- | --- |
| `email` | Yes | String | The email address of the user (must include at least one address and at most 50 addresses). |
| `phone` | Yes | String | The phone number of the user (must include at least one phone number and at most 50 phone numbers). We recommend providing this in E.164 format. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Example request

```json
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
{
  {phone: "+12125551212"},
  {email: "dont.spam@me.com"},
  {phone: "+17185551212"}
}
```

## Response

```json
{
  "status": "The emails and/or phone numbers have been queued for deletion",
  "message": "success"
}
```

{% endapi %}
