---
article_title: FAQ
hidden: true
permalink: /onboarding_faq/
excerpt_separator: ""
page_type: glossary
layout: onboarding_faq
description: "This FAQ. . ."

---

{% api %}

## Users

{% apitags %}
Users
{% endapitags %}

### How do I handle anonymous user data?

Initially, when a user profile is recognized via the SDK, Braze creates an anonymous user profile with an associated `braze_id`: a unique user identifier that is set by Braze.

To further keep track of anonymous users, you can implement [user aliases]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle#user-aliases) that allow you to tag anonymous users with an identifier. These users can then be exported using their aliases, or referenced by the API.

If an anonymous user profile with an alias is later recognized with an `external_id`, they will be treated as a normal identified user profile, but will retain their existing alias and can still be referenced by that alias.

For alias users that you want to merge with identified users, you can merge any fields that are pertinent to the actual profile that you want to keep. You would have to export that data before deleting it from the alias profile using our [POST: User Profile Export by Identifier]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) endpoint. You can then use our [POST: User Track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) endpoint to post these events to the profile you kept. This will preserve any data you want to keep such as attributes that were previously recorded on one profile, but not the other.

For a full breakdown of different methods for collecting new and existing user data in Braze, check out [data collection best practices]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/best_practices/).

### How can I import users I have already collected and identified outside of Braze?

To import previously identified users, you can upload a CSV to Braze, or send data through the API.

#### CSV

You can upload and update user profiles via CSV files from the **User Import** page. When importing your customer data, you’ll need to specify each customer’s unique identifier, also known as `external_id`.

Before starting your CSV import, it’s important to understand from your engineering team how users will be identified in Braze. Typically this would be a database ID used internally. This should align with how users will be identified by the Braze SDK on mobile and web, and ensures that each customer will have a single user profile within Braze across their devices. Learn more about Braze’s [user profile lifecycle]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/).

When you provide an `external_id` in your import, Braze will update any existing user with the same `external_id` or create a newly identified user with that `external_id` set if one is not found.

For more information and to download CSV import templates, refer to [user import]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv).

#### API

To upload users via API, you can use our [POST: User Track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) endpoint to import them into Braze.

If you are unsure whether the user already exists in Braze, you can implement our [POST: User Profile Export by Identifier]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) endpoint to verify. If you identify that the user already exists in Braze, you can use our POST: User Track endpoint to post the new data you’d like to add to the user profile that already exists in Braze.

{% alert note %}
Keep the following nuances in mind when using the `/users/track` endpoint:

- When creating alias-only users through this endpoint, you must explicitly set the `_update_existing_only` flag to false.
- Updating the subscription status with this endpoint will both update the user specified by their `external_id` (such as User1) and update the subscription status of any users with the same email as that user (User1).
{% endalert %}

### What's the difference between the push subscription statuses?

There are three push subscription state options: subscribed, opted-in, and unsubscribed.

By default, for your user to receive your messages through push, their push subscription state must be either subscribed or opted-in, and they must be push enabled. You can override this setting if needed when composing a message.

|Opt-in State|Description|
|---|---|
|Subscribed| Default push subscription state when a user profile is created in Braze. |
|Opted-In| A user has explicitly expressed a preference to receive push notifications. Braze will automatically move a user's opt-in state to `Opted-In` if a user accepts an OS-level push prompt.<br><br>This does not apply to users on Android 12 or below.|
|Unsubscribed| A user explicitly unsubscribed from push through your application or other methods your brand provides. By default, Braze push campaigns only target users that are `Subscribed` or `Opted-in` for push.|
{: .reset-td-br-1 .reset-td-br-2}

### What if I've identified duplicated users?

If you have identified duplicate users, you will need to clean up those user profiles. You can do so through the following steps:

1. Export the user profiles using our users/export/ids endpoint API.
2. Identify correct user profile (ultimately, your team will need to decide on the correct information) and either:
    - Merge any fields that are pertinent to the actual profile that you want to keep using the user/track endpoint.
    - Delete the duplicate, non-useful profile without merging any data using the users/delete endpoint. Once you delete a user profile, **there is no way to retrieve the information**.

{% alert important %}
We recommend that you first import the new user profiles with the correct `external_id` and corresponding custom attributes and events. Once user profiles are deleted, they can't be retrieved, so deleting should be the very last step.
{% endalert %}

Some additional things to note:

- Any engagement data (such as campaigns or Canvases received) on duplicate user profiles will be lost. The only way to retain the historical engagement context is by adding it as a custom attribute (such as an array custom attribute of all campaigns or Canvases received).
- When migrating user profiles, it's also up to your team to decide which user profile of the duplicates will be kept. Braze can't decide or provide you a list of profiles to delete.  
- Ultimately, it will be important for your team to assess the signup process from your users’ experience and make sure that you're only calling the `changeUser()` method when a user becomes identified.

## Segments

{% apitags %}
Segments
{% endapitags %}

### How do I create a segment when I import a group of users through CSV?

To import your CSV file, navigate to the **User Import** page under the Users section. The **Recent Imports** table lists up to twenty of your most recent imports, their file names, number of lines in the file, number of lines successfully imported, total lines in each file, and the status of each import.

The **Import CSV** panel contains importing directions and a button to begin your import. Click **Select CSV File** and select your file of interest. Then, before clicking **Start Import**, you have the option to let Braze know what to do with this list under “What do you want us to do with the users in this CSV".

Select **Import Users in this CSV and also make it possible to retarget this specific batch of users as a group**, and then select **Automatically generate a segment from the users who are imported from this CSV**. Once you click **Start Import**, Braze will upload your file, check the column headers and the data types of each column, and create a segment.

To download a CSV template, refer to [user import]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv).

### What types of filters can I use when creating a segment?

Braze’s SDK provides you with a powerful arsenal of filters to segment and target your users based on specific features and attributes. You can use the [Segmentation Filters]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters) glossary to search or narrow these filters by Filter Category (Custom Data, User Activity, Retargeting, Marketing Activity, User Attributes, Install Attribution, Social Activity, Testing, Other).

### How do I set up location targeting so that I can segment users by their most recent location and use it in my location-based campaigns and strategies?

Navigate to the **Segments** page, under Engagement, to view all of your current user segments. On this page, you can create and name new segments. To get started, click **Create Segment** and give your segment a name.

Once you have created your segment, add a `Most Recent Location` filter to target users by the last place that they used your app. You can either highlight users in a standard circular region or create a custom polygonal region.

- For circular regions, you can move the origin and adjust the location radius for your segmentation.
- For polygonal regions, you can more specifically designate which areas you wish to be included in your segment.

{% alert tip %}
Interested in taking advantage of location targeting with the help of a Braze partner? Check out our available Braze [contextual location partners]({{site.baseurl}}/partners/message_personalization/location).

### How

{% endalert %}

## Campaigns

{% apitags %}
Campaigns
{% endapitags %}

## Canvases

{% apitags %}
Canvases
{% endapitags %}

## Analytics

{% apitags %}
Analytics
{% endapitags %}

{% endapi %}
