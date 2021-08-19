---
nav_title: "Webhook Object"
article_title: Webhook Object
page_order: 13
page_type: reference
channel: 
  - webhook
description: "This article outlines the Braze Webhook Object."

---

# Webhook Object Specification

```json
{
  "url": (required, string),
  "request_method": (required, string) one of "POST", "PUT", "DELETE", or "GET",
  "request_headers": (optional, Hash) key-value pairs to use as request headers,
  "body": (optional, string) if you want to include a JSON object, make sure to escape quotes and backslashes,
  "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under
}
```
