---
nav_title: "SMS Object"
page_order: 10

page_type: reference

channel: SMS
platform:
  - API
tool:
  - Campaigns
  - Canvas

description: "This article explains the different components of Braze's SMS Object."
---
# SMS Object Specification

```json
{
  "sms": (optional, SMS Object),
  {  
    "subscription_group_id": (required, string) the id of your subscription group,
    "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under,
    "body": (required, string),
    "app_id": (required, string) see App Identifier above
    "media_items" :(optional, array) if you are using MMS with Braze, you can pass an image URL to this field to send the image with your message.    
  }
}
```
