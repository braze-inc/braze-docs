---
nav_title: "Recipients Object"
article_title: API Recipients Object
page_order: 9
page_type: reference
description: "This article explains the different components of the Braze Recipients object."
---

# Recipients object specification

The Recipients Object allows you to request or write information in our endpoints.

Either `external_user_id` or `user_alias` is required in this object. __Requests must specify only one.__

The Recipients object allows you to combine the [User Alias object]({{site.baseurl}}/api/objects_filters/user_alias_object/), the [Trigger Properties object]({{site.baseurl}}/api/objects_filters/trigger_properties_object/), and the [Canvas Entry Properties object]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/).

## Object body

```json
[{
  "user_alias": (optional, User Alias Object) User Alias of user to receive message,
  "external_user_id": (optional, string) see External User Id,
  "trigger_properties": (optional, object) personalization key-value pairs for this user when sending a Campaign or message; see Trigger Properties,
  "canvas_entry_properties": (optional, object) personalization key-value pairs for this user when triggering a Canvas; see Canvas Entry Properties
}]
```

## Recipient object deduping

When making an API call with the Recipient Object, __if there exists a duplicated recipient targeting the same address (ie email, push), the user will be deduped__, meaning identical users will be removed, leaving one.

For example, if the same `external_user_id` is used, then only 1 message will be received. Consider making multiple API calls if you need a work-around for this behavior.

```json
{"campaign_id":"#####","recipients":[
{"external_user_id":"userid1","trigger_properties":{"name":"Beth Test 1"}},
{"external_user_id":"userid1","trigger_properties":{"name":"Beth Test 2"}} 
]}
```