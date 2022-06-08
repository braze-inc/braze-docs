---
nav_title: User Profile Lifecycle
article_title: User Profile Lifecycle
page_order: 2
page_type: reference
description: "This reference article describes the user profile lifecycle in Braze, and the various ways a user profile can be identified and referenced."

---

# User profile lifecycle

> This article describes the user profile lifecycle in Braze, and the various ways a user profile can be identified and referenced. If you're looking to better understand your customer lifecycle, check out our Braze Learning course on [Mapping User Lifecycles](https://learning.braze.com/mapping-customer-lifecycles) instead.

All persistent data associated with a user will be stored against a user profile.

Once a user profile is created, either after a user is recognized by the SDK or created via API, there are a number of identifiers that can be assigned to a profile to identify or reference that user. 

These identifiers are the following:

* `braze_id`
* `external_id`
* Any number of aliases that you choose to set for your user base.

## Anonymous user profiles

Initially, when a user profile is recognized via the SDK an anonymous user profile is created with an associated `braze_id`: a unique user identifier that is set by Braze. This identifier can be used to delete users through the REST API.

The `braze_id` is automatically assigned by Braze, cannot be edited, and is device-specific.

## Identified user profiles

Once a user is recognizable in your app (by providing a form of user ID or email address) we suggest [assigning an external_id][23] to that user's profile. The purpose of this is to recognize the same user across multiple devices to a single user profile.

More benefits of user IDs include the following: 

- Provide a consistent user experience across multiple devices and platforms (e.g., not sending lapsing user notifications to a user’s Android tablet when they are a loyal user of the app on the iPhone).
- Improve the accuracy of your analytics by ensuring users aren’t creating a new user profile every time they uninstall and reinstall, or install the app on a different device.
- Enable import of user data from sources outside the app using our [User API]({{site.baseurl}}/api/endpoints/user_data/), and target users with transactional messages using our [Messaging API]({{site.baseurl}}/api/endpoints/messaging/).
- Search for individual users using our “Testing” [filters]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/) within the segmenter, and on the [User Search]({{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/) page.

{% alert warning %}
Do not assign an `external_id` to a user profile before you are able to uniquely identify them. Once you identify a user, you cannot revert them to anonymous.
{% endalert %} 

Setting an `external_id` will merge any relevant user profile data from the anonymous user profile with the existing identified user profile data and remove the remaining, irrelevant parts of the previously anonymous profile data from our database. This method can prevent an orphaned user from receiving a campaign that has already been received or opened by your identified user or prevent various errors that can occur when there are duplicates of your users in Braze. These orphaned users are not considered in your user counts and will not be messaged.

On the first instance of assigning an `external_id` to an unknown user profile, all existing user profile data will be migrated to the new user profile.

{% alert warning %}
An `external_id` is unchangeable once it has been set against a user profile. Any attempt to set a different `external_id` during a user's session will create a new user profile with the new `external_id` associated with it. No data will be passed between the two profiles.
{% endalert %}

For further information on how to set an `external_id` against a user profile see our documentation ([iOS][24], [Android][30], [Web][31]).

## User aliases

To allow referring to users by multiple other identifiers rather than only the Braze `external_id`, you can also set user aliases against a user profile. Any alias set against a user profile will act in addition to the user's `braze_id` or `external_id` as opposed to replacing it. There's no limit to the number of aliases that you can set against a user profile.

Each alias consists of two parts: a label, which defines the key of the alias, and a name, which defines the value. An alias name for any single label must be unique across the user base. If you attempt to update a second user profile with a pre-existing label and name combination, the user profile will not be updated.

Unlike an `external_id`, an alias can be updated with a new name for a given label once set. You can do so either via the [New User Alias Endpoint][32], or if you pass a new name via the SDK. The user alias will then be visible when exporting that user's data.

![Two different user profiles for separate users with the same user alias label but different alias values][29]

User aliases also allow you to tag anonymous users with an identifier. These users can then be exported using their aliases, or referenced by the API.

If an anonymous user profile with an alias is later recognized with an `external_id`, they will be treated as a normal identified user profile, but will retain their existing alias and can still be referenced by that alias.

A user alias can also be set on a known user profile to reference a known user by another externally known ID. For example, a user may have an Amplitude ID and a different BI tool ID that you wish to reference within Braze.

For information on how to set a user alias, see our documentation for each platform ([iOS][1], [Android][2], [Web][3]).

![A flow chart of a user profile's lifecycle in Braze. When changeUser() is called for an anonymous user, that user becomes an Identified User and data is migrated to their identified user profile. The Identified User has a Braze ID and external ID. At this point, if a second anonymous user has changeUser() called, their anonymous user data will be orphaned. If the Identified User has an alias added to their existing user profile, no data will be affected but they will become an Identified User with alias. If a third anonymous user with the same alias label as the identified user but a different alias name then has changeUser() called, the existing data is discarded and only the alias label on the identified user profile is maintained.][26]

{% alert tip %}
Having trouble picturing how this may look for the user profile lifecycle of your customers? Visit [Best practices]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/best_practices/) to view user data collection best practices.
{% endalert %}

## Advanced use case information

You can set a new user alias for existing identified user profiles via our SDK and our API using the [new user alias endpoint][27]. However, user aliases can't be set via the API on an unknown user profile.

If you attempt to set a pre-existing `external_id` on an anonymous user profile which share a matching alias name, but have different labels, only the alias label on the pre-existing known user profile will be maintained.

Uninstalling and reinstalling an app will cause a new anonymous user ID to be generated for that user.

## How to troubleshoot with Braze's IDs

Aside from acting as a mechanism to organize user data and reference user profiles, all `braze_id`'s can be used to find and identify users within your dashboard for testing. To find your user in the Braze dashboard, refer to [Adding Test Users][28].

{% alert important %}
Braze will ban or block users with over 5 million sessions ("dummy users") and no longer ingest their SDK events, as these users are generally the result of misintegration. If you find that this has happened to a legitimate user, reach out to your Braze account manager.
{% endalert %}

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/setting_user_ids/#aliasing-users
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/#aliasing-users
[3]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids/#aliasing-users

[23]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/setting_user_ids/#assigning-a-user-id
[24]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/setting_user_ids/
[25]: {{site.baseurl}}/developer_guide/home/
[26]: {% image_buster /assets/img_archive/Braze_User_flowchart.png %}
[27]: {{site.baseurl}}/developer_guide/rest_api/user_data/#new-user-alias-endpoint
[28]: {{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#adding-test-users
[29]: {% image_buster /assets/img_archive/Braze_User_aliases.png %}
[30]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/
[31]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids/
[32]: {{site.baseurl}}/developer_guide/rest_api/user_data/#new-user-alias-endpoint
