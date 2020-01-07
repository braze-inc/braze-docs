---
nav_title: "Recipient Object"
page_order: 9

page_type: reference

platform:
  - API
tool:
  - Campaigns
  - Canvas
  - Segments

description: "This article explains the different components of the Braze Recipient object."
---

# Recipient Object

The recipient object allows you to request or write information in our endpoints.

Either `external_user_id` or `user_alias` is required in this object. Requests must specify only one.

The Recipient object allows you to combine the [User Alias object]({{ site.baseurl }}/api/objects_filters/user_alias_object/), the [Trigger Properties object]({{ site.baseurl }}/api/objects_filters/trigger_properties_object/), and the [Canvas Entry Properties object]({{ site.baseurl }}/api/objects_filters/canvas_entry_properties_object/).

## Object Body
```json
{
  "user_alias": (optional, User Alias Object) User Alias of user to receive message,
  "external_user_id": (optional, string) see External User Id,
  "trigger_properties": (optional, object) personalization key-value pairs for this user when sending a Campaign or message; see Trigger Properties,
  "canvas_entry_properties": (optional, object) personalization key-value pairs for this user when triggering a Canvas; see Canvas Entry Properties
}
```
