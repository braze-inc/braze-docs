---
nav_title: "Aliases to Identify Object"
article_title: API Aliases to Identify Object
page_order: 11
page_type: reference
description: "This article explains the object needed to identify user aliases."

---

# Aliases to identify object specification

An API request with any fields in the Attributes Object will create or update an attribute of that name with the given value on the specified user profile. Use Braze User Profile Field names (listed below or any listed in the [User Profile Fields chart]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields)) to update those special values on the user profile in the dashboard or add your own custom attribute data to the user.

## Object body

```json
{
  "aliases_to_identify" : (required, array of Aliases to Identify Object)
  [
    {
      "external_id" : (required, string) see External User ID below,
      // external_ids for users that do not exist will return a non-fatal error.
      // See Server Responses for details.
      "user_alias" : {
        "alias_name" : (required, string),
        "alias_label" : (required, string)
      }
    }
  ]
}
```

For more information on `alias_name` and `alias_label`, check out our [User Aliases documentation]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases)
