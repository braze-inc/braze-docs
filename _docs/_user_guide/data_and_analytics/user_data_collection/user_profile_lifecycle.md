---
nav_title: User Profile Lifecycle
article_title: User Profile Lifecycle
page_order: 2
page_type: reference
description: "This reference article describes the Braze user profile lifecycle, and the various ways a user profile can be identified and referenced."

---

# User profile lifecycle

> This article describes the user profile lifecycle in Braze, and the various ways a user profile can be identified and referenced. If you're looking to better understand your customer lifecycle, check out our Braze Learning course on [Mapping User Lifecycles](https://learning.braze.com/mapping-customer-lifecycles) instead.

All persistent data associated with a user is stored in their user profile.

Once a user profile is created, either after a user is recognized by the SDK or created via the API, there are a number of parameters that can be assigned to that profile to identify and reference that user. 

These parameters include:

* `braze_id`
* `external_id`
* Any number of custom user aliases that you set

## Anonymous user profiles

Any user without a designated `external_id` is called an anonymous user. For example, these could be users who have visited your website but not signed up or downloaded your mobile app but not created a profile.

Initially, when a user is recognized via the SDK, an anonymous user profile is created with an associated `braze_id`: a unique identifier that is set by Braze. This identifier can be used to update the user profile through the [API]({{site.baseurl}}/api/endpoints/user_data/).

The `braze_id` is automatically assigned by Braze, cannot be edited, and is device-specific.

## Identified user profiles

Once a user is recognizable in your app (by providing a form of user ID or email address), we suggest assigning an `external_id` to that user's profile using the `changeUser` method ([web](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser), [iOS](https://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#ac8b369b40e15860b0ec18c0f4b46ac69), [Android](https://braze-inc.github.io/braze-android-sdk/javadocs/com/appboy/Appboy.html#changeUser-java.lang.String-)). An `external_id` allows you to identify the same user profile across multiple devices. 

Additional benefits of using an `external_id` include the following: 

- Provide a consistent user experience across multiple devices and platforms (for example, not sending lapsing user notifications to a user's Android tablet when they are a loyal user of the app on the iPhone).
- Improve the accuracy of your analytics by confirming users aren't creating a new user profile every time they uninstall and reinstall, or install the app on a different device.
- Enable import of user data from sources outside the app using the [User Data endpoints]({{site.baseurl}}/api/endpoints/user_data/) and target users with transactional messages using our [Messaging endpoints]({{site.baseurl}}/api/endpoints/messaging/).
- Search for individual users using our "Testing" [filters]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/) within the segmenter, and on the [User Search]({{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/) page.

{% alert warning %}
Do not assign an `external_id` to a user profile before you are able to uniquely identify them. After you identify a user, you cannot revert them to anonymous.
<br><br>
Additionally, an `external_id` is unchangeable after it has been set against a user profile. Any attempt to set a different `external_id` during a user's session will create a new user profile with the new `external_id` associated with it. No data will be passed between the two profiles.
{% endalert %} 

There are two scenarios that occur when you identify anonymous users:

1) **An anonymous user becomes a new identified user:** <br>If the `external_id` does not yet exist in Braze, the anonymous user becomes a new identified user and retains all of the same attributes and history of the anonymous user. 

2) **An anonymous user is identified as an already existing user:** <br>If the `external_id` already exists in Braze, then this user was previously identified as a user in the system in some other way, such as via another device like a tablet or through imported user data. 

As such, you already have a user profile for this user. In this instance, Braze will do the following:
1. Orphan the anonymous user
2. Merge [specific user profile fields]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge_updates-behavior) that don't already exist on the identified user profile from the anonymous profile
3. Remove the anonymous profile from your user base so the user counts aren't inflated

If an anonymous user has a first name and the known user also has a first name set, the first name of the target is maintained. If the target user has a null value, and the anonymous user has a value, it's merged into the target user if it falls under these [specific user profile fields]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge_updates-behavior).

For information on how to set an `external_id` against a user profile, see our documentation ([iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/), [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids/)).

## User aliases

To refer to users by identifiers other than only the Braze `external_id`, set user aliases against a user profile. Any alias set against a user profile will act in addition to the user's `braze_id` or `external_id` as opposed to replacing it. There's no limit to the number of aliases that you can set against a user profile.

Each alias functions as a key-value pair that consists of two parts: an `alias_label`, which defines the key of the alias, and an `alias_name`, which defines the value. An `alias_name` for any single label must be unique across the user base (just like with `external_id`). If you attempt to update a second user profile with a pre-existing label and name combination, the user profile will not be updated.

Unlike an `external_id`, an alias can be updated with a new name for a given label after it is set either via our [User Data endpoints]({{site.baseurl}}/developer_guide/rest_api/user_data/#new-user-alias-endpoint) or by passing a new name via the SDK. The user alias will then be visible when exporting that user's data.

![Two different user profiles for separate users with the same user alias label but different alias names]({% image_buster /assets/img_archive/Braze_User_aliases.png %})

User aliases also allow you to tag anonymous users with an identifier. For example, if a user provides your ecommerce site with their email address but hasn't yet signed up, the email address can be used as an alias for that anonymous user. These users can then be exported using their aliases or referenced by the API.

If an anonymous user profile with an alias is later recognized with an `external_id`, they will be treated as a normal identified user profile, but will retain their existing alias and can still be referenced by that alias.

A user alias can also be set on a known user profile to reference a known user by another externally known ID. For example, a user may have a business intelligence tool ID (like an Amplitude ID) that you wish to reference within Braze.

For information on how to set a user alias, see our documentation for each platform ([iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/#aliasing-users), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/#aliasing-users), [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids/#aliasing-users)).

![A flow chart of a user profile's lifecycle in Braze. When changeUser() is called for an anonymous user, that user becomes an Identified User and data is migrated to their identified user profile. The Identified User has a Braze ID and external ID. At this point, if a second anonymous user has changeUser() called, user data fields that do not already exist on the Identified User will be merged. If the Identified User has an alias added to their existing user profile, no data will be affected but they will become an Identified User with alias. If a third anonymous user with the same alias label as the Identified User but a different alias name then has changeUser() called, any fields that do not exist on the Identified User will be merged and the alias label on the Identified User profile is maintained.]({% image_buster /assets/img_archive/Braze_User_flowchart.png %})

{% alert tip %}
Having trouble picturing how this may look for the user profile lifecycle of your customers? Visit [Best practices]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/best_practices/) to view user data collection best practices.
{% endalert %}

## Advanced use case information

You can set a new user alias for existing identified user profiles via our SDK and our API using the [User Data endpoints]({{site.baseurl}}/developer_guide/rest_api/user_data/#new-user-alias-endpoint). However, user aliases can't be set via the API for an existing unknown user profile.

If you attempt to set a pre-existing `external_id` on an anonymous user profile which shares a matching alias name but has different labels, only the alias label on the pre-existing known user profile will be maintained.

Uninstalling and reinstalling an app will cause a new anonymous `braze_id` to be generated for that user.

### How to troubleshoot with user IDs

All user IDs can be used to find and identify users within your dashboard for testing. To find your user in the Braze dashboard, refer to [Adding Test Users]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#adding-test-users).

{% alert important %}
Braze will ban or block users with over 5 million sessions ("dummy users") and no longer ingest their SDK events, as these users are generally the result of misintegration. If you find that this has happened to a legitimate user, reach out to your Braze account manager.
{% endalert %}

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/#aliasing-users
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/#aliasing-users
[3]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids/#aliasing-users

[23]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/#assigning-a-user-id
[24]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/
[25]: {{site.baseurl}}/developer_guide/home/
[26]: {% image_buster /assets/img_archive/Braze_User_flowchart.png %}
[27]: {{site.baseurl}}/developer_guide/rest_api/user_data/#new-user-alias-endpoint
[28]: {{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#adding-test-users
[29]: {% image_buster /assets/img_archive/Braze_User_aliases.png %}
[30]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/
[31]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids/
[32]: {{site.baseurl}}/developer_guide/rest_api/user_data/#new-user-alias-endpoint
