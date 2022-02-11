---
nav_title: "Webhook Object"
article_title: Webhook Messaging Object
page_order: 13
page_type: reference
channel: 
  - webhook
description: "This article outlines the Braze Webhook Object."

---

# Webhook object specification

The following outlines the Braze webhook object. 

As a best practice, Braze recommends that you supply an explicit value for `Content-Type` in the `request_headers` field to ensure consistent and predictable behavior, as senders and servers may change over time. If a value is not specified for the `Content-Type` header, one will be inferred from the request body.

```json
{
  "url": (required, string),
  "request_method": (required, string) one of "POST", "PUT", "DELETE", or "GET",
  "request_headers": (optional, Hash) key-value pairs to use as request headers,
  "body": (optional, string) if you want to include a JSON object, make sure to escape quotes and backslashes,
  "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under
}
```
