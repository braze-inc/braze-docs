---
nav_title: Collection Best Practices
article_title: Collection Best Practices
page_order: 3.1
page_type: reference
description: "The following article will help clarify different methods and best practices for collecting new and existing user data."

---

# Data collection best practices

> Knowing when and how to collect user data for known and unknown users can be challenging to navigate when envisioning the user profile lifecycle of your customers. The following article will help clarify different methods and best practices for collecting new and existing user data.

## Overview

The example below comprises an email collection use case, but the logic applies to many different data collection scenarios. In this example, we assume you have already integrated a sign-up form or way to collect user information. 

Once a user provides information for you to log, we recommend you verify if the data already exists in your database and create a user-alias profile or update the existing user profile, as necessary. 

If an unknown user were to view your site and then, at a later date, create an account or identify themselves via email sign-up, profile merging must be handled carefully. Based on the method in which you merge, alias-only user info or anonymous data may be overwritten.

## Capturing user data through a web form

### Step 1: Check if the user exists

When a user enters content through a web form, check if a user with that email already exists within your database. This can be done in one of two ways:
- **Client checks internally (recommended)**<br>If you have an external record or database containing the provided user information that exists outside of Braze, reference this at the time of email submission to ensure the email has not already been captured.<br><br>
- **[/users/export/id]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) endpoint**<br>Check to see if the returned users array is empty or contains a value. It is not recommended to heavily leverage this endpoint when querying a single user; we apply a rate limit of 2,500 requests per minute to this endpoint. For more information on endpoint rate limits, refer to [Rate limits by request type]({{site.baseurl}}/api/api_limits/#rate-limits-by-request-type).

### Step 2: Log or update user

- **If a user exists:**
  - Do not create a new profile.
  - Log a custom attribute (e.g., `newsletter_subscribed: true`) on the user's profile to indicate that the user has submitted their email via newsletter subscription. If multiple user profiles in Braze exist with the same email address, all profiles will be exported.<br><br>
- **If a user does not exist:**
  - Create an alias-only profile via Braze's [/users/track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) endpoint. This endpoint will accept a [user alias object]({{site.baseurl}}/api/objects_filters/user_alias_object/) and create an alias-only profile when `update_existing_only` is set to `false`. Set the user's email as the user alias to reference that user in the future (as the user won't have an `external_id`).

![Diagram showing the process to update an alias-only user profile. A user submits their email address and a custom attribute, their zip code, on a marketing landing page. An arrow pointing from the landing page collection to an alias-only user profile shows a Braze API request to the user track endpoint, with the request body containing the user's alias name, alias label, email, and zip code. The profile has the label "Alias Only user created in Braze" with the attributes from the request body to show the data being reflected on the newly-created profile.][3]{: style="max-width:90%;"}

## Capturing user data when alias-only user info is already present

When a user creates an account or identifies themselves via email sign-up, there are two options are merging the profiles depending on which data should be retained:

### Option 1: Overwrite alias-only data and maintain anonymous data

Call `changeUser()` before making an API request to the [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/) endpoint, then, set the user alias. 

By calling `changeUser()` before the request, Braze will merge and preserve anonymous user data (for example, if the user downloaded the app and logged custom data before signing in) to the identified user profile but "orphan" all data associated with the alias-only profile (attributes, events, purchases, etc.).

![Diagram showing the process to overwrite alias-only data and maintain anonymous data when identifying a user. The process starts with an anonymous user and their Braze ID. Then the user creates an account, and anonymous user data is migrated to an identified user profile when changeUser is called. The identified user now has a Braze ID and external ID. An arrow pointing from the identified user to an identified user with an alias shows a Braze API request to the users identify endpoint with the user's external ID, alias name, and alias label. During this step, the user data associated with that alias-only user is lost. The final step shows the identified user with a Braze ID, external ID, alias name, and alias label, but none of the custom attributes associated with the alias-only profile before they merged.][1]{: style="max-width:90%;"}

#### Keep user alias profile information
If you have events or attributes that you want to keep when you merge user profiles, you can export aliased user data before identification using the [`/users/export/ids`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) endpoint, then re-associate the attributes, events, and purchases with the identified user.

### Option 2: Overwrite anonymous data and maintain the alias-only profile

Make a Braze API request to the [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/) endpoint to identify any users that match a given user alias. If any exist, Braze will migrate the user alias data to the identified user profile. Next, call `changeUser()`.

By calling `changeUser()` after hitting the `/users/identify` endpoint, Braze will merge and preserve all data associated with the alias-only profile but "orphan" any anonymous user data.

![Diagram showing the process to overwrite anonymous data and maintain the alias-only profile. The process starts with an anonymous user and their Braze ID. Then the user creates an account. An arrow pointing from the account creation step to the identified user profile shows a Braze API request to the users identify endpoint with the user's external ID, alias name, and alias label. A box above the arrow shows that this alias-only user already exists in Braze, and has custom attributes associated with the alias user. Those custom attributes are preserved and written to the identified user profile. The last step shows changeUser being called, after which the anonymous user data is lost.][2]{: style="max-width:90%;"}

## Additional resources
- Check out our article on the Braze [user profile lifecycle]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/) for additional context.<br>
- Documentation on setting user IDs and calling the `changeUser()` method for [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/), [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/setting_user_ids/#suggested-user-id-naming-convention), and [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids/).

[1]: {% image_buster /assets/img/user_profile_process.png %}
[2]: {% image_buster /assets/img/user_profile_process2.png %}
[3]: {% image_buster /assets/img/user_profile_process3.png %}
