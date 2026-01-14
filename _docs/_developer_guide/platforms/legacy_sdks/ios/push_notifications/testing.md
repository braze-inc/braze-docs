---
nav_title: Testing
article_title: Push Notification Testing for iOS
platform: iOS
page_order: 29
description: "This reference article covers command line push testing for your iOS push notifications."
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Testing {#push-testing}

If you'd like to test in-app and push notifications via the command line, you can send a single notification through the terminal via CURL and the [messaging API]({{site.baseurl}}/api/endpoints/messaging/). You will need to replace the following fields with the correct values for your test case:

Required fields:

- `YOUR-API-KEY-HERE` - available at **Settings** > **API Keys**. Ensure the key is authorized to send messages via the `/messages/send` REST API endpoint. 
- `EXTERNAL_USER_ID` - available on the **Search Users** page.
- `REST_API_ENDPOINT_URL` - listed on the Braze [Instances]({{site.baseurl}}/api/basics/#endpoints. Ensure using the endpoint corresponds to the Braze instance your workspace is on.

Optional fields:
- `YOUR_KEY1` (optional)
- `YOUR_VALUE1` (optional)

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer YOUR-API-KEY-HERE" -d '{
  "external_user_ids":["EXTERNAL_USER_ID"],
  "messages": {
    "apple_push": {
      "alert":"Test push",
      "extra": {
        "YOUR_KEY1":"YOUR_VALUE1"
      }
    }
  }
}' https://{REST_API_ENDPOINT_URL}/messages/send 
```
