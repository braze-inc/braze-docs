---
nav_title: User Data Collection Best Practices
article_title: User Data Collection Best Practices
page_order: 4
page_type: reference
description: ""

---

# User data collection best practices

> Knowing when and how to collect user data for known and unknown users can be challenging to navigate when envisioning the user profile lifecycle of your customers. The following article will help clarify different methods and best practices for collecting new and existing user data.

## Overview

The example below comprises an email collection use case, but the logic applies to many different data collection scenarios. In this example, we assume you have already integrated a sign-up form or way to collect user information. 

Once a user provides information for you to log, we recommend you verify if the data already exists in your database and create a user-alias profile or update the existing user profile, as necessary. 

If an unknown user were to view your site and then at a later date create an account or identify themselves via email sign-up, profile merging must be handled carefully. Based on the method you merge, alias-only user info or anonymous data may be overwritten.

## Capturing user data through a webform

### Step 1: Check if user exists

When a user enters content through a web form, check if a user with that email already exists within your database. This can be done in one of two ways:
- Client checks internally (Recommended) - If you have an external record or database containing the provided user information that exists outside of Braze, reference this at the time of email submission to ensure the email has not already been captured.
- [/users/export/id](https://www.braze.com/docs/api/endpoints/export/user_data/post_users_identifier/) endpoint - check to see if the returned users array is empty or contains a value. It is not recommended to heavily leverage this endpoint when querying a single user; we apply a rate limit of 2,500 requests per minute to this endpoint ([all rate limits here for reference](https://www.braze.com/docs/api/api_limits/#rate-limits-by-request-type)).

### Step 2: Log or update user

- If a user exists:
  - Do not create a new profile.
  - Log a custom attribute (e.g., `newsletter_subscribed: true`) on the user's profile to indicate that the user has submitted their email via newsletter subscription.
Note: if multiple user profiles in Braze exist with the same email address, all profiles will be exported.<br><br>
- If a user does not exist:
  - Create an alias-only profile via Braze's [/users/track](https://www.braze.com/docs/api/endpoints/user_data/post_user_track/) endpoint. This endpoint will accept a [user alias object](https://www.braze.com/docs/api/objects_filters/user_alias_object/) and create an alias-only profile when `update_existing_only` is set to `false`. Set the user's email as the user alias to reference that user in the future (as the user won't have an `external_id`).

![User profile process][3]{: style="max-width:90%;"}

## Capturing user data when alias-only user info is already present

When a user creates an account or identifies themselves via email sign-up, there are two options are merging the profiles depending on which data should be retained:

### Option 1: Overwrite alias-only data and maintain anonymous data

Call `changeUser()` before making an API request to the `/users/identify` endpoint. Braze will merge anonymous user data (for example, if the user downloaded the app and logged various custom data before signing in) to the identified User Profile. Then, set the user alias.

Only push tokens and message history associated with the user alias profile are retained. Once merged, any attributes, events, or purchases will be "orphaned" and unavailable on the identifier user (`external_id` profile).

By calling `changeUser()` before making a request to the `/users/identify` endpoint, you will preserve any anonymous data but lose all data associated with the alias-only profile.

![User profile process][1]{: style="max-width:90%;"}

#### Keep user alias profile information
If you have events or attributes that you want to keep when you merge user profiles, you can export aliased user data before identification using the `/users/export/ids` endpoint, then re-associate the attributes, events, and purchases with the identified user.

### Option 2: Overwrite anonymous data and maintain the alias-only profile

Make a Braze API request to the `/users/identify` endpoint to identify any users that match a given user alias. If any exist, Braze will migrate the user alias data to the identified user profile.

Calling `changeUser()` after hitting the `/users/identify` endpoint will result in losing the anonymous data but maintaining all data associated with the alias-only profile.

![User profile process][2]{: style="max-width:90%;"}

## Additional resources
Check out our article on the Braze [user profile lifecycle](https://www.braze.com/docs/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/) for additional context.

Info on setting user IDs and calling change user method for [Android](https://www.braze.com/docs/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/), [iOS](https://www.braze.com/docs/developer_guide/platform_integration_guides/ios/analytics/setting_user_ids/#suggested-user-id-naming-convention), and [Web](https://www.braze.com/docs/developer_guide/platform_integration_guides/web/analytics/setting_user_ids/).

[1]: {% image_buster /assets/img/user_profile_process.png %}
[2]: {% image_buster /assets/img/user_profile_process2.png %}
[3]: {% image_buster /assets/img/user_profile_process3.png %}
