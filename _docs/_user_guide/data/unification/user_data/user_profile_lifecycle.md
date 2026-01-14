---
nav_title: User profile lifecycle
article_title: User Profile Lifecycle
page_order: 2
page_type: reference
description: "This reference article describes the Braze user profile lifecycle, and the various ways a user profile can be identified and referenced."

---

# User profile lifecycle

> This article describes the Braze user profile lifecycle and the various ways to identify and reference a user profile. If you're looking to better understand your customer lifecycle, check out our Braze Learning course on [Mapping User Lifecycles](https://learning.braze.com/mapping-customer-lifecycles) instead.

All persistent data associated with a user is stored in their user profile. After a user profile is created, either through the API or after a user is recognized by the SDK, you can assign a number of parameters to that profile to identify and reference that user. 

These parameters include:

* `braze_id` (assigned by Braze)
* `external_id`
* `email`
* `phone`
* Any number of custom user aliases that you set

## Anonymous user profiles

Any user without a designated `external_id` is called an [anonymous user]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/anonymous_users/). For example, these could be users who visited your website but didn't sign up, or users who downloaded your mobile app but didn't create a profile.

Initially, when a user is recognized by the SDK, an anonymous user profile is created with an associated `braze_id`: a unique identifier that is automatically assigned by Braze, cannot be edited, and is device-specific. This identifier can be used to update the user profile through the [API]({{site.baseurl}}/api/endpoints/user_data/).

## Identified user profiles

After a user is recognizable in your app (by providing a form of user ID or email address), we suggest assigning an `external_id` to that user's profile using the `changeUser` method ([web](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser), [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/changeuser(userid:sdkauthsignature:fileid:line:)), [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/change-user.html)). An `external_id` allows you to identify the same user profile across multiple devices.

Additional benefits of using an `external_id` include the following: 

- Provide a consistent user experience across multiple devices and platforms (for example, not sending lapsing user notifications to a user's Android tablet when they are a loyal user of the iPhone app).
- Improve the accuracy of your analytics by confirming users aren't creating a new user profile every time they uninstall and reinstall, or install the app on a different device.
- Enable import of user data from sources outside the app using the [User Data endpoints]({{site.baseurl}}/api/endpoints/user_data/) and target users with transactional messages using our [messaging endpoints]({{site.baseurl}}/api/endpoints/messaging/).
- Search for individual users using our "Testing" [filters]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/) within the segmenter, and on the [**Search Users**]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/) page.

### Considerations for external IDs

{% alert warning %}
Don't assign an `external_id` to a user profile before you can uniquely identify them. After you identify a user, you can't revert them to anonymous.
<br><br>
An `external_id` can be updated using the [`/users/external_ids/rename` endpoint]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_rename/). However, any attempt to set a different `external_id` during a user's session will create a new user profile with the new `external_id` associated with it. No data will be passed between the two profiles.
{% endalert %} 

#### Risk of using an email or hashed email as an external ID

Using an email address or a hashed email address as your Braze external ID can simplify identity management across your data sources; however, it's important to consider the potential risks to user privacy and data security.

- **Guessable information:** Email addresses are easily guessable, making them vulnerable to attacks.
- **Risk of exploitation:** If a malicious user alters their web browser to send someone else's email address as their external ID, they could potentially access sensitive messages or account information.

### What happens when you identify anonymous users

One of two scenarios can occur when you identify anonymous users:

1) **An anonymous user becomes a new identified user:** <br>If the `external_id` doesn't yet exist in Braze, the anonymous user becomes a new identified user and retains all the same attributes and history of the anonymous user. 

2) **An anonymous user is identified as an already existing user:** <br>If the `external_id` already exists in Braze, then this user was previously identified as a user in the system in some other way, such as through another device (like a tablet) or imported user data. 

In other words, you already have a user profile for this user. In this instance, Braze will do the following:
1. Orphan the anonymous user
2. Merge [specific user profile fields]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge_updates-behavior) that don't already exist on the identified user profile from the anonymous profile
3. Remove the anonymous profile from your user base so the user counts aren't inflated

If both the anonymous user and known user have a first name, the first name of the known user is maintained. If the known user has a null value and the anonymous user has a value, the anonymous user's value is merged into the known user's profile if the value falls under these [specific user profile fields]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge-behavior).

For information on how to set an `external_id` against a user profile, see our documentation ([iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/?tab=swift), [Android]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/?tab=android), [Web]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/?tab=web)).

## User aliases

To refer to users by identifiers other than the Braze `external_id`, set user aliases against a user profile. Any alias set against a user profile will act in addition to the user's `braze_id` or `external_id` as opposed to replacing it. There's no limit to the number of aliases that you can set against a user profile.

Each alias functions as a key-value pair that consists of two parts: an `alias_label`, which defines the key of the alias, and an `alias_name`, which defines the value. An `alias_name` for any single label must be unique across your user base (just like with `external_id`). If you try to update a second user profile with a pre-existing label and name combination, the user profile won't be updated.

### Updating user aliases

An alias can be updated with a new name for a given label after it's set either by using our [User Data endpoints]({{site.baseurl}}/developer_guide/rest_api/user_data/#new-user-alias-endpoint) or passing a new name through the SDK. The user alias will then be visible when exporting that user's data.

![Two different user profiles for separate users with the same user alias label but different alias names]({% image_buster /assets/img_archive/Braze_User_aliases.png %})

### Tagging anonymous users

User aliases also allow you to tag anonymous users with an identifier. For example, if a user provides your eCommerce site with their email address but hasn't yet signed up, the email address can be used as an alias for that anonymous user. These users can then be exported using their aliases or referenced by the API.

### Behavior of aliases on anonymous user profiles

If an anonymous user profile with an alias is later recognized with an `external_id`, they will be treated as a normal identified user profile, but will retain their existing alias and can still be referenced by that alias.

### Setting aliases on known user profiles

A user alias can also be set on a known user profile to reference a known user by another externally known ID. For example, a user may have a business intelligence tool ID (like an Amplitude ID) that you wish to reference within Braze.

For information on how to set a user alias, see our documentation for each platform ([iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/#aliasing-users), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/#aliasing-users), [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids/#aliasing-users)).

![A flow chart of a user profile's lifecycle in Braze. When changeUser() is called for an anonymous user, that user becomes an Identified User and data is migrated to their identified user profile. The Identified User has a Braze ID and external ID. At this point, if a second anonymous user has changeUser() called, user data fields that do not already exist on the Identified User will be merged. If the Identified User has an alias added to their existing user profile, no data will be affected but they will become an Identified User with alias. If a third anonymous user with the same alias label as the Identified User but a different alias name then has changeUser() called, any fields that do not exist on the Identified User will be merged and the alias label on the Identified User profile is maintained.]({% image_buster /assets/img_archive/Braze_User_flowchart.png %})

{% alert tip %}
Having trouble picturing how this may look for the user profile lifecycle of your customers? Visit [Best practices]({{site.baseurl}}/user_guide/data/user_data_collection/best_practices/) to view user data collection best practices.
{% endalert %}

## Advanced use case

You can set a new user alias for existing identified user profiles through our SDK and our API using the [User Data endpoints]({{site.baseurl}}/developer_guide/rest_api/user_data/#new-user-alias-endpoint). However, user aliases can't be set through the API for an existing unknown user profile.

The user aliases are also merged in the process. However, if both the user to be orphaned and the target user have an alias with the same label, only the alias from the target user is maintained.

Uninstalling and reinstalling an app will generate a new anonymous `braze_id` for that user.

### Troubleshooting with user IDs

All user IDs can be used to find and identify users within your dashboard for testing. To find your user in the Braze dashboard, refer to [Adding Test Users]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#adding-test-users).

{% alert important %}
Braze will ban or block users with over 5,000,000 sessions ("dummy users") and will no longer ingest their SDK events, as these users are generally the result of misintegration. If you find that this has happened to a legitimate user, contact your Braze account manager.
{% endalert %}