---
nav_title: "SMS object"
article_title: SMS Messaging Object
page_order: 10
page_type: reference
channel: SMS
description: "This reference article explains the different components of the Braze SMS object."

---
# SMS object

> The `sms` object allows you to modify or create SMS messages via our [messaging endpoints]({{site.baseurl}}/api/endpoints/messaging).

```json
{
    "subscription_group_id": (required, string) the ID of your subscription group,
    "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under,
    "body": (required, string),
    "app_id": (required, string) see App Identifier,
    "media_items" :(optional, array) use this field to pass an image URL in an MMS to send an image with your message,
    "link_shortening_enabled": (optional, boolean) use this field to turn on link shortening and campaign-level click tracking,
    "user_click_tracking_enabled": (optional, boolean) if link_shortening_enabled is true, use this field to turn on link shortening, and campaign-level and user-level click tracking.
}
```

- [App identifier]({{site.baseurl}}/api/identifier_types/)
  - Any valid `app_id` from an app configured in your workspace works for all users in your workspace, regardless of whether the user has the specific app on their profile or not.