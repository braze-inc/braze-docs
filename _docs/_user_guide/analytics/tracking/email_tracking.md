---
nav_title: Email open pixel and click tracking
article_title: Email Open Pixel and Click Tracking
page_order: 1
page_type: reference
description: "This reference article covers how to implement open pixel and click tracking."

---

# Email open pixel and click tracking

> [Open pixel tracking]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#changing-location-of-tracking-pixel) and click tracking can be turned on or off for each user profile. This flexibility helps you follow regional privacy laws, where an individual user profile might indicate they no longer want to be tracked.

## Turning on open pixel or click tracking

When either importing or updating a user profile via [API]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields) or [CSV]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv), two fields are available for you to modify:

- `email_open_tracking_disabled`: Accepts `true` or `false`. Set to `false` to add the open tracking pixel to all future emails sent to this user. Available for SparkPost and SendGrid only.
- `email_click_tracking_disabled`: Accepts `true` or `false`. Set to `false` to add click tracking to all links within a future email, sent to this user. Available for SparkPost and SendGrid only.

For reference, this information is reflected on the user profile in the email **Contact Settings**, located in the **Engagement** tab.

![Email open and click tracking pixel fields on the Engagement tab of a user's profile]({% image_buster /assets/img_archive/open_click_user_profile.png %}){: style="max-width:60%;"}

