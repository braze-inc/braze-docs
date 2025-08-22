---
nav_title: User management
article_title: LINE User Management
page_order: 0
description: "This article covers the LINE user ID and how to set it."
page_type: reference
channel:
 - LINE
alias: /line/user_management/
---

# LINE user management

> The LINE user ID is stored on the user profile attribute called `native_line_id`, which is used to send messages to a user on the LINE channel. This article covers how to set and find the `native_line_id` attribute.

Customer user data is represented in a [Braze user profile]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/). A user profile stores information and attributes about a company’s users, such as first names and email addresses. 

When you send LINE messages through Braze, Braze uses the `native_line_id` attribute to identify what users to send the message. When LINE sends Braze webhook events, such as when a user follows a channel or replies to a message, the `native_line_id` is used to look up the corresponding user profile.

{% alert note %}
LINE user IDs are distinct by LINE provider. A specific user will have different LINE user IDs for each provider they follow. Users are unlikely to know their LINE ID (unlike their email or phone number), as they change for each brand they follow. 
{% endalert %}

## Setting the `native_line_id` attibute

There are a number of scenarios where `native_line_id` is set on the user profile, which are outlined below.

| Scenario | Whether user profile exists with `native_line_id` | Outcome |
| --- | --- | --- |
|A user follows a LINE channel | No| An anonymous user profile is created (merging will be required):<br> - `native_line_id` is set to the user’s LINE ID <br>- `line_id` user alias is set to the user’s LINE ID<br>- The user is subscribed to the channel’s Braze subscription group |
|A user follows a LINE channel| Yes | All user profiles with the `native_line_id`:<br>- Are subscribed to the channel’s Braze subscription group|
|Company uses user CSV upload with a n`ative_line_id` column| No| If no user profile exists for the specified `external_id` or user alias:<br>- `native_line_id` is set to the specified value<br> - All other attributes specified in the CSV are set on the user profile|
|Company uses user CSV upload with a `native_line_id` column | Yes | If a user profile exists for the specified `external_id` or user alias:<br>- `native_line_id` is set to the specified value<br>- All other attributes specified in the CSV are set on the user profile<br>- Multiple profiles have the same `native_line_id` |
| Company uses `/users/track` endpoint and specifies `native_line_id` attribute | No | If no user profile exists for the specified user ([specified by `external_id`, `user_alias`, `braze_id` or `email`]({{site.baseurl}}/api/objects_filters/user_attributes_object/)):<br>- `native_line_id` is set to the specified value<br>- All other attributes specified in request are set on the user profile |
| Company uses `/users/track` endpoint and specifies `native_line_id` attribute | Yes | If a user profile exists for the specified user ([specified by `external_id`, `user_alias`, `braze_id` or `email`]({{site.baseurl}}/api/objects_filters/user_attributes_object/)):<br>- `native_line_id` is set to the specified value<br>- All other attributes specified in request are set on the user profile<br>- Multiple profiles have the same `native_line_id` |
| Company requests Braze run the subscription status syncer | No | If a user LINE ID is returned from LINE that doesn't have a corresponding user profile in Braze, then an anonymous user profile is created:<br>- `native_line_id` is set to the user’s LINE ID<br>- `line_id` user alias is set to the user’s LINE ID<br>- The user is subscribed to the channel’s Braze subscription group<br><br>Note that if a user with the same LINE ID  is later created, there will be duplicate users, but both will have the correct LINE subscription status. User merging can clean up your user base in these cases. |
| Company requests Braze run the subscription status syncer | Yes | If a user LINE ID is returned from LINE that has a corresponding user profile in Braze:<br>- The user is subscribed to the channel’s Braze subscription group |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 }

## Finding the `native_line_id`

When viewing a user profile in the Braze dashboard, you can see whether it has the `native_line_id` attribute set by going to the **Engagement** tab > **Contact Settings** section > **LINE** section.

If the `native_line_id` has been set, it will be shown under **LINE User ID**. Otherwise, it won't appear.

![Line Contact Settings in the Engagment tab.]({% image_buster /assets/img/line/line_contact_settings.png %}){: style="max-width:50%;"}

