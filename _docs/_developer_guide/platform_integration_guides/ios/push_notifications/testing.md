---
nav_title: Testing
article_title: Push Notification Testing for iOS
platform: iOS
page_order: 29
description: "This article covers command line push testing for your iOS push notifications."
channel:
  - push

---

# Testing {#push-testing}

If you'd like to test in-app and push notifications via the command line, you can send a single notification through the terminal via CURL and the [messaging API][29]. You will need to replace the following fields with the correct values for your test case:

- `YOUR_API_KEY` - available on the [Developer Console][30] page.
- `YOUR_EXTERNAL_USER_ID` - available on the [user profile search page][31]. See [assigning user IDs][32] for more information.
- `YOUR_KEY1` (optional)
- `YOUR_VALUE1` (optional)

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {{YOUR_API_KEY}}" -d '{
  "external_user_ids":["YOUR_EXTERNAL_USER_ID"],
  "messages": {
    "apple_push": {
      "alert":"Test push",
      "extra": {
        "YOUR_KEY1":"YOUR_VALUE1"
      }
    }
  }
}' https://rest.iad-01.braze.com/messages/send
```
The preceding example is for customers on the `US-01` instance. If you are not on this instance, refer to our [API documentation][66] to see which endpoint to make requests to.

[29]: {{site.baseurl}}/api/endpoints/messaging/
[30]: https://dashboard-01.braze.com/app_settings/api_settings/
[31]: https://dashboard-01.braze.com/users/user_search/user-search/
[32]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/setting_user_ids/#assigning-a-user-id
[66]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/
