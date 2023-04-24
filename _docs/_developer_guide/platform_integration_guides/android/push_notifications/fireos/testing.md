---
nav_title: Testing
article_title: Testing for FireOS
platform: FireOS
page_order: 19
page_type: reference
description: "This page provides information on testing FireOS in-app messages and push notifications via the command line."
channel: 
- push

---

# Testing from command line

If you'd like to test in-app and push notifications via the command-line, you can send a single notification through the terminal via cURL and the [messaging API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/). You will need to replace the following fields with the correct values for your test case:

Required fields:
- `YOUR-API-KEY-HERE` - available on the **Developer Console** page. Ensure the key is authorized to send messages via the `/messages/send` REST API endpoint. 
- `EXTERNAL_USER_ID` - available on the **User Profile Search** page.
- `REST_API_ENDPOINT_URL` - available on the Braze [Instances]({{site.baseurl}}/api/basics/#endpoints) page. Ensure using the endpoint corresponds to the Braze instance your app group is on.

Optional fields:
- `YOUR_KEY1` (optional)
- `YOUR_VALUE1` (optional)

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer YOUR-API-KEY-HERE" -d '{
  "external_user_ids":["EXTERNAL_USER_ID"],
  "messages": {
    "android_push": {
      "title":"Test push title",
      "alert":"Test push",
      "extra":{
        "YOUR_KEY1":"YOUR_VALUE1"
      }
    }
  }
}' https://{REST_API_ENDPOINT_URL}/messages/send 
```

[13]: {{site.baseurl}}/api/endpoints/messaging/
[66]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/