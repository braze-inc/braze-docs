---
nav_title: Setting User IDs
article_title: Setting User IDs for Roku
platform: Roku
page_order: 0
page_type: reference
description: "This page covers methods to identify users, as well as best practices and important considerations."
 
---

# Setting User IDs

{% include archive/setting_user_ids/setting_user_ids.md %}

You should make the following call as soon as the user is identified (generally after logging in) in order to set the user ID:

```
m.Braze.setUserId(YOUR_USER_ID_STRING)
```

## Suggested User ID Naming Convention

{% include archive/setting_user_ids/naming_convention.md %}

## User ID Integration Best Practices & Notes

{% include archive/setting_user_ids/best_practices.md %}

> If you opt to use a hash of a unique identifier as your user ID take care to ensure that you're normalizing the input to your hashing function. For example, if you're going to use a hash of an email address, ensure that you're stripping leading and trailing whitespace from the input, and taking localization into account.

[1]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
[2]: {{site.baseurl}}/api/endpoints/messaging/
