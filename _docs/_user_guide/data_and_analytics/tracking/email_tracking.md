---
nav_title: Email Open Pixel and Click Tracking
article_title: Email Open Pixel and Click Tracking
page_order: 1
page_type: reference
description: "This reference article covers how to disable open pixel and click tracking."

---

# Open pixel and click tracking overview

[Open pixel tracking][open_tracking] and click tracking can now be disabled per user profile. This flexibility helps customers support regional privacy laws, where an individual user profile might indicate they no longer want to be tracked.

## Implementation

when either importing or updating a user profile via [api][api_doc] or [csv][csv_doc], two new fields are now available for you to modify.

- email_open_tracking_disabled
- email_click_tracking_disabled

_For easy reference, this information is reflected on the user profile in the Email Contact Settings._

![open_click_user_profile][1]{: style="max-width:60%;"}

[open_tracking]: {{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/email_settings/#email-open-tracking-pixel
[api_doc]: {{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields
[csv_doc]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#standard-user-data-column-headers
[1]: {% image_buster /assets/img_archive/open_click_user_profile.png %}
