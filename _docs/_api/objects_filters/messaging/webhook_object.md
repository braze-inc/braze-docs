---
nav_title: "Webhook object"
article_title: Webhook Messaging Object
page_order: 13
page_type: reference
channel:
  - webhook
description: "This reference article outlines the Braze webhook object."

---

# Webhook object

> The `webhook` object allows you to modify or create webhook messages via our [messaging endpoints]({{site.baseurl}}/api/endpoints/messaging).

```json
{
  "url": (required, string),
  "request_method": (required, string) one of "POST", "PUT", "DELETE", or "GET",
  "request_headers": (optional, Hash) key-value pairs to use as request headers,
  "body": (optional, string) if you want to include a JSON object, make sure to escape quotes and backslashes,
  "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under
}
```

As a best practice, Braze recommends providing an explicit value for `Content-Type` in the `request_headers` field for consistent and predictable behavior, as senders and servers may change over time. If you don't specify a value for the `Content-Type` header, the system infers a value from the request body.
