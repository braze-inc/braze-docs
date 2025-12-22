---
nav_title: "Aliases to identify object"
article_title: API Aliases to Identify Object
page_order: 11
page_type: reference
description: "This article explains aliases to identify object specification."

---

# Aliases to identify object

An API request with any fields in the attributes object creates or updates an attribute of that name with the given value on the specified user profile.

Use Braze user profile field names (listed as follows or any listed in the section for [Braze user profile fields]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields)) to update those special values on the user profile in the dashboard or add your own custom attribute data to the user.

## Object body

```json
{
  "aliases_to_identify" : (required, array of aliases to identify object)
  [
    {
      "external_id" : (required, string) see External user ID,
      // external_ids for users that do not exist return a non-fatal error.
      // See server responses for details.
      "user_alias" : {
        "alias_name" : (required, string) see User aliases,
        "alias_label" : (required, string) see User aliases
      }
    }
  ]
}
```

- [External user ID]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields)
- [User aliases]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases)