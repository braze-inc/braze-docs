---
nav_title: Setting User IDs
article_title: Setting User IDs for Roku
platform: Roku
page_order: 0
page_type: reference
description: "This page covers methods to identify users, as well as best practices and important considerations."
 
---

# Setting user ids

{% include archive/setting_user_ids/setting_user_ids.md %}

You should make the following call as soon as the user is identified (generally after logging in) in order to set the user ID:

```
m.Braze.setUserId(YOUR_USER_ID_STRING)
```

## Suggested user id naming convention

{% include archive/setting_user_ids/naming_convention.md %}

## User id integration best practices & notes

{% include archive/setting_user_ids/best_practices.md %}

[1]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
[2]: {{site.baseurl}}/api/endpoints/messaging/
