---
nav_title: "Recipients object"
article_title: API Recipients Object
page_order: 9
page_type: reference
description: "This reference article explains the different components of the Braze recipients object."

---

# Recipients object

> The recipients object allows you to request or write information in our endpoints.

You must include one of `external_user_id`, `user_alias`, `braze_id`, or `email` in this object. **Requests must specify only one.**

The recipients object allows you to combine the [user alias object]({{site.baseurl}}/api/objects_filters/user_alias_object/), the [trigger properties object]({{site.baseurl}}/api/objects_filters/trigger_properties_object/), the [Canvas entry properties object]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/), and the [user attributes object]({{site.baseurl}}/api/objects_filters/user_attributes_object/).

## Object body

```json
[{
  "user_alias": (optional, User Alias Object) User alias of user to receive message,
  "external_user_id": (optional, string) see External user ID,
  "braze_id": (optional, string) see Braze ID,
  "email": (optional, string) email address of user to receive message,
  "prioritization": (optional, array) see Prioritization; required when using email,
  "trigger_properties": (optional, object) personalization key-value pairs for this user when sending a campaign or message; see Trigger Properties,
  "context": (optional, object) personalization key-value pairs for this user when triggering a Canvas; see Canvas Entry Properties
  "send_to_existing_only": (optional, boolean) defaults to true; cannot be used with user aliases,
  "attributes": (optional, object) fields in the attributes object create or update an attribute of that name with the given value on the specified user profile before the message is sent and existing values are overwritten
}]
```

When `send_to_existing_only` is `true`, Braze only sends the message to existing users. However, you cannot use this flag with user aliases. When `send_to_existing_only` is `false`, you must include an attribute. Braze creates a user with the `id` and attributes before sending the message.

- [Braze ID]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/)
- [User aliases]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases)
- [External user ID]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields)
- [Prioritization]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/#identifying-users-by-email)
- [User attributes object]({{site.baseurl}}/api/objects_filters/user_attributes_object/)

## Recipient object deduping

When making an API call with the recipient object, **if there exists a duplicated recipient targeting the same address (that is, email, push), Braze dedupes the user**, meaning Braze removes identical users, leaving one.

For example, if you use the same `external_user_id`, then the user receives only one message. Consider making multiple API calls if you need a workaround for this behavior.

```json
{"campaign_id":"#####","recipients":[
{"external_user_id":"userid1","trigger_properties":{"name":"Beth Test 1"}},
{"external_user_id":"userid1","trigger_properties":{"name":"Beth Test 2"}}
]}
```
