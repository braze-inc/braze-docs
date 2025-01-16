---
nav_title: Setting User IDs
article_title: Setting User IDs for Roku
platform: Roku
page_order: 0
page_type: reference
description: "This reference article covers methods to identify and set user IDs for Roku, as well as best practices and important considerations."
 
---

# Setting user IDs

> This reference article covers methods to identify and set user IDs for Roku, as well as best practices and important considerations.

{% multi_lang_include archive/setting_user_ids/setting_user_ids.md %}

You should make the following call as soon as the user is identified (generally after logging in) in order to set the user ID:

```brightscript
m.Braze.setUserId(YOUR_USER_ID_STRING)
```

## Suggested user ID naming convention

{% multi_lang_include archive/setting_user_ids/naming_convention.md %}

## User ID integration best practices and notes

{% multi_lang_include archive/setting_user_ids/best_practices.md %}

