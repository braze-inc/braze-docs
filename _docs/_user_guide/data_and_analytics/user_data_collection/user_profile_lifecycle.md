---
nav_title: User Profile Lifecycle
page_order: 2
description: "All persistent data associated with a user will be stored against a user profile. Once a user profile is created, either following a user being recognized by the SDK or created via API, there are a number of identifiers that can be assigned to a profile to identify or reference that user."
---

# User Profile Lifecycle

All persistent data associated with a user will be stored against a user profile.

Once a user profile is created, either following a user being recognized by the SDK or created via API, there are a number of identifiers that can be assigned to a profile to identify or reference that user. These are the:

* `braze_id`
* `external_ id`
* Any number of aliases that you choose to set for your user base

## Anonymous User Profiles

Initially, when a user profile is recognized via the SDK an 'anonymous' user profile is created with an associated `braze_id`: a unique user identifier that is set by Braze. This identifier can be used to delete users through the REST API.

The `braze_id` is automatically assigned by Braze, cannot be edited and will be device-specific.

## Identified User Profiles

Once a user is recognizable in your app (by providing a form of user ID or email address) we suggest [assigning an external_id][23] to that user's profile. The purpose of this is to recognize the same user across multiple devices to a single user profile.

{% alert warning %}
Do not assign an `external_id` to a user profile before you are able to uniquely identify them. Once you identify a user, you cannot revert them to anonymous.
{% endalert %} 

Setting an `external_id` will merge any relevant user profile data from the anonymous user profile with the existing identified user profile data and orphan/remove the remaining, irrelevant parts of the previously anonymous profile data from our database. This method can prevent an orphaned user from receiving a campaign that has already been received or opened by your identified user or prevent various errors that can occur when there are duplicates of your users in Braze. These orphaned users are not considered in your user counts and will not be messaged.

On the first instance of assigning an `external_id` to an unknown user profile all, existing user profile data will be migrated to the new user profile.

{% alert warning %}
An `external_id` is unchangeable once it has been set against a user profile. Any attempt to set a different `external_id` during a user's session will create a new user profile with the new `external_id` associated with it. No data will be passed between the two profiles.
{% endalert %}

For further information on how to set an `external_id` against a user profile please see our documentation ([iOS][24], [Android][30], [Web][31]).

## User Aliases

To allow for customers to refer to users by multiple other identifiers, rather than only the Braze external_id, clients can also set user aliases against a user profile. Any alias set against a user profile will act in addition to the user's `braze_id` or `external_id` as opposed to replacing it. There is not a limit as to the number of aliases that you can set against a user profile.

Each alias consists of two parts: a label, which defines the key of the alias, and a name, which defines the value. An alias name for any single label must be unique across the user base. If you attempt to update a second user profile with a pre-existing label and name combination the user profile will not be updated.

Unlike an external_id, once an alias is set for a user this can be updated with a new name for a given label. This is possible either via the [New User Alias endpoint][32] or if you pass a new name via the SDK. Upon setting a user alias these will be visible when exporting that user's data.

![Alias_Label_Diagram][29]

User aliases also allow customers to tag anonymous users with an identifier. These users can then be exported using their aliases or referenced by the API.

If an anonymous user profile with an alias is later recognized with an external_id, they will be treated as a normal identified user profile but will retain and can be referenced by their existing alias.

A user alias can also be set on a known user profile to reference a known user by another externally known ID eg. a user may have an Amplitude ID and a different BI tool ID that you wish to reference within Braze.

For information on how to set a user alias please see our [documentation][25] for each platform.

![User_Profile_Lifecycle][26]

## Advanced Use Case Information

You can set a new user alias for existing identified user profiles via the SDK and [the API][27]. User aliases cannot be set via the API on an unknown user profile.  For more information on how to reference a user via the API please refer to our documentation.

If you attempt to set a pre-existing `external_id` on an anonymous user profile which share a matching alias name but with different labels, only the alias label on the pre-existing known user profile will be maintained.

Uninstalling and reinstalling an app will cause a new anonymous user ID to be generated for that user.

## How to Troubleshoot with Braze's IDs

Aside from acting as a mechanism to organize user data and reference user profiles, all `braze_id`'s can be used to find and identify users within your dashboard for testing. To find your user in the Braze dashboard please see our [Adding Test Users][28] section.

{% alert important %}
Braze will ban or block users ("dummy users") with over 5 million sessions and no longer ingest their SDK events because they are usually the result of misintegration. If you find that this has happened for a legitimate user, please reach out to your Braze account manager.
{% endalert %}

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
