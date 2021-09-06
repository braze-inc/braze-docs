---
nav_title: "SMS Object"
article_title: SMS Messaging Object
page_order: 10
page_type: reference
channel: SMS
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
    "media_items" :(optional, array) use this field to pass an image URL in an MMS to send an image with your message.    
  }
}
```
