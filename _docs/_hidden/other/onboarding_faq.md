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

### How can I target precise lists of users based on their custom event and purchase behavior in the past 365 days?

You can use [Segment Extensions]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/)! Segment Extensions enable you to target a more precise list of users than you otherwise could with a regular segment.

You can create up to 10 Segment Extensions per app group. After these extension lists are generated, they can then be included or excluded as a filter in your segments. When creating a Segment Extension, you can also specify that the list be regenerated once every 24 hours.

1. Under Engagements, expand **Segments** and click **Segment Extension**.
2. From the Segment Extensions table, click **+ Create New Extension**.
3. Name your Segment Extension by describing the type of users you intend to filter for. This will ensure that this extension can be easily and accurately discovered when applying it as a filter in your segment.
4. Select between a purchase or custom event criteria for targeting.
5. Choose which purchased item or specific custom event you’d like to target for your user list. 
6. Choose how many times (more than, less than, or equal to) the user would need to have completed the event, and how many days to look back, up to 365 days.

To increase targeting precision, you can select **Add Property Filters** and segment based on the specific properties of your purchase or custom event. Braze supports event property segmentation based on string, numeric, boolean, and time objects.

We also support segmentation based on [nested event properties]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#nested-objects).

Segment Extensions rely on long term storage of event properties and don’t have the 30-day custom event property storage limit. This means you can look back on event properties tracked within the past year, and tracking doesn’t wait until the extension has been set up first.

{% alert note %}
Using event properties within Segment Extensions does not impact data point usage.
{% endalert %}

#### Keeping Segment Extensions up to date

You can specify whether you want this extension to represent a single snapshot in time, or whether you want this extension to regenerate on a daily basis. Your extension will always begin processing after the initial save. If you would like the extension to be regenerated daily, select **Regenerate Extension Daily** and the regeneration will begin processing at around midnight each day in your company’s time zone.

When you’re done, click **Save**. Your extension will begin processing. The length of time it takes to generate your extension depends on how many users you have, how many custom events or purchase events you’re capturing, and how many days you’re looking back in history.

Finally, after you've created an extension, you can use it as a filter when creating a segment or defining an audience for a campaign or Canvas. Start by choosing `Braze Segment Extension` from the filter list under the **User Attributes** section. From the Braze Segment Extension filter list, choose the extension you wish to include or exclude in this segment. To view the extension criteria, click **View Extension Details**. Now you can proceed as usual with creating your segment.

{% endalert %}

## Campaigns

{% apitags %}
Campaigns
{% endapitags %}

### How do you create a multichannel campaign?

To create a multichannel campaigns, go to the **Campaigns** page, select **Create Campaign**, then select **Multichannel Campaign**. Once in a multichannel campaign, select **Add Messaging Channel** from the compose tab to add your desired channels. Click the channel icons that appear to toggle through different messaging composers as you build your campaign copy for the different channels.

### What are some ways I can start testing and optimizing campaigns?

Creating multivariate campaigns and running Canvases with multiple variants are a great way to start! For example, you can run a [multivariate campaign]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) to test out one message that has different copies or subject lines. Canvases with multiple variants are helpful for testing entire workflows.

### Why is there a difference between the number of unique recipients and the number of sends for a given campaign or Canvas?

One potential explanation for this difference could be due to the campaign or Canvas having re-eligibility turned on. By having this on, users who qualify for the segment and delivery settings will be able to receive the message more than once. If re-eligibility is not turned on, then the probable explanation for the difference between sends and unique recipients may be due to users having multiple devices across platforms associated with their profiles.

For example, should you have a Canvas that has both iOS and web push notifications, a given user with both mobile and desktop devices could receive more than one message.

### What does local time zone delivery offer?

Local time zone delivery allows you to deliver messaging campaigns to a segment based on a user’s individual time zone. Without local time zone delivery, campaigns will be scheduled based on your company’s time zone settings in Braze.

For example, a London-based company sending a campaign at 12pm will reach users on the west coast of America at 4am. If your app is only available in certain countries, this may not be a risk for you, otherwise, we highly recommend avoiding sending early morning push notifications to your user base!

### How does Braze recognize a user's time zone?

Braze will automatically determine a user’s time zone from their device. This ensures time zone accuracy and full coverage of your users. Users created through the User API or otherwise without a time zone will have your company’s time zone as their default time zone until they are recognized in your app by the SDK.

You can check your company’s time zone in your [company settings]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/company-wide_settings_management/).

### How do I schedule a local time zone campaign?

When scheduling a campaign, you need to choose to send it at a designated time, and then select **Send campaign to users in their local time zone**.

Braze highly recommends that all local time zone campaigns are scheduled 24 hours in advance. Since such a campaign needs to send over the course of an entire day, scheduling them 24 hours in advance ensures that your message will reach your entire segment. However, you can schedule these campaigns less than 24 hours in advance if necessary. Keep in mind that Braze will not send messages to any users that have missed the send time by more than 1 hour.

For example, if it's 1 pm and you schedule a local time zone campaign for 3 pm, then the campaign will immediately send to all users whose local time is 3–4 pm, but not to users whose local time is 5 pm. In addition, the send time you choose for your campaign needs to have not yet occurred in your company’s time zone.

Editing a local time zone campaign that is scheduled less than 24 hours in advance will not alter the message’s schedule. If you decide to edit a local time zone campaign to send at a later time (for instance, 7 pm instead of 6 pm), users who were in the targeted segment when the original send time was chosen will still receive the message at the original time (6 pm). If you edit a local time zone to send at an earlier time (for instance, 4 pm instead of 5 pm), then the campaign will still send to all segment members at the original time (5 pm).

{% alert note %}
For Canvas steps, users do not need to be in the step for 24 hours to receive the next step for local time zone delivery.
{% endalert %}

If you have allowed users to become re-eligible for the campaign, then they will receive it again at the original time (5 pm). For all subsequent occurrences of your campaign, however, your messages only send at your updated time.

## Canvases

{% apitags %}
Canvases
{% endapitags %}

## Analytics

{% apitags %}
Analytics
{% endapitags %}

{% endapi %}
