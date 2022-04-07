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

- `YOUR_API_KEY` - available on the **Developer Console**
- `YOUR_EXTERNAL_USER_ID` - available on the **User Profile Search** page
- `YOUR_KEY1` (optional)
- `YOUR_VALUE1` (optional)

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {{YOUR_API_KEY}}" -d "{\"external_user_ids\":[\"YOUR_EXTERNAL_USER_ID\"],\"messages\":{\"android_push\":{\"title\":\"Test push title\",\"alert\":\"Test push\",\"extra\":{\"YOUR_KEY1\":\"YOUR_VALUE1\"}}}}" https://rest.iad-01.braze.com/messages/send
```

This example uses the `US-01` instance. If you are not on this instance, replace the `US-01` endpoint with [your endpoint][66].

[13]: {{site.baseurl}}/api/endpoints/messaging/
[14]: https://dashboard-01.braze.com/app_settings/api_settings/
[15]: https://dashboard-01.braze.com/users/user_search/user-search/
[66]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/