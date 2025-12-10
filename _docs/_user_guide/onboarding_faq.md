---
article_title: FAQ
hidden: true
permalink: /onboarding_faq/
excerpt_separator: ""
page_type: glossary
layout: onboarding_faq
description: "This page contains a collection of frequently asked questions, outlined by category."

---

{% multi_lang_include video.html id="keAZAlBR9zc" source="youtube" %}


<!--- Users --->

{% api %}

### How do I handle anonymous user data?

{% apitags %}
Users
{% endapitags %}

Initially, when a user profile is recognized via the SDK, Braze creates an anonymous user profile with an associated `braze_id`: a unique user identifier that is set by Braze.

To further keep track of anonymous users, you can implement [user aliases]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle#user-aliases) that allow you to tag anonymous users with an identifier. These users can then be exported using their aliases, or referenced by the API.

If an anonymous user profile with an alias is later recognized with an `external_id`, they will be treated as a normal identified user profile, but will retain their existing alias and can still be referenced by that alias.

For alias users that you want to merge with identified users, you can merge any fields that are pertinent to the actual profile that you want to keep. You would have to export that data before deleting it from the alias profile using our [Export user profile by identifier endpoint]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/). You can then use our [Track users endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) to post these events to the profile you kept. This will preserve any data you want to keep such as attributes that were previously recorded on one profile, but not the other.

For a full breakdown of different methods for collecting new and existing user data in Braze, check out [data collection best practices]({{site.baseurl}}/user_guide/data/user_data_collection/best_practices/).

{% endapi %}
{% api %}

### How can I import users I have already collected and identified outside of Braze?

{% apitags %}
Users
{% endapitags %}

To import previously identified users, you can upload a CSV to Braze, or send data through the API.

#### CSV

You can upload and update user profiles via CSV files from **Audience** > **Import Users**. When importing your customer data, you'll need to specify each customer's unique identifier, also known as `external_id`.

Before starting your CSV import, it's important to understand from your engineering team how users will be identified in Braze. Typically this would be a database ID used internally. This should align with how users will be identified by the Braze SDK on mobile and web, so that each customer will have a single user profile within Braze across their devices. Learn more about the Braze [user profile lifecycle]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/).

When you provide an `external_id` in your import, Braze will update any existing user with the same `external_id` or create a newly identified user with that `external_id` set if one is not found.

For more information and to download CSV import templates, refer to [user import]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv).

#### API

To upload users via API, you can use our [Track users endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) to import them into Braze.

If you are unsure whether the user already exists in Braze, you can implement our [Export user profile by identifier endpoint]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) to verify. If you identify that the user already exists in Braze, you can use our `/users/track` endpoint to post the new data you'd like to add to the user profile that already exists in Braze.

{% alert note %}
Keep the following nuances in mind when using the `/users/track` endpoint:

- When creating alias-only users through this endpoint, you must explicitly set the `_update_existing_only` flag to false.
- Updating the subscription status with this endpoint will both update the user specified by their external ID (such as User1) and update the subscription status of any users with the same email as that user (User1).
{% endalert %}

{% endapi %}
{% api %}

### What's the difference between the push subscription statuses?

{% apitags %}
Users
{% endapitags %}

There are three push subscription state options: subscribed, opted-in, and unsubscribed.

By default, for your user to receive your messages through push, their push subscription state must be either subscribed or opted-in, and they must be push enabled. You can override this setting if needed when composing a message.

|Opt-in State|Description|
|---|---|
|Subscribed| Default push subscription state when a user profile is created in Braze. |
|Opted-In| A user has explicitly expressed a preference to receive push notifications. Braze will automatically move a user's opt-in state to `Opted-In` if a user accepts an OS-level push prompt.<br><br>This does not apply to users on Android 12 or below.|
|Unsubscribed| A user explicitly unsubscribed from push through your application or other methods your brand provides. By default, Braze push campaigns only target users that are `Subscribed` or `Opted-in` for push.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
{% api %}

### What if I've identified duplicated users?

{% apitags %}
Users
{% endapitags %}

If you have identified duplicate users, you will need to clean up those user profiles. You can do so through the following steps:

1. Export the user profiles using our `/users/export/ids` endpoint.
2. Identify correct user profile (ultimately, your team will need to decide on the correct information) and either:
    - Merge any fields that are pertinent to the actual profile that you want to keep using the `/user/track` endpoint.
    - Delete the duplicate, non-useful profile without merging any data using the users/delete endpoint. After you delete a user profile, **there is no way to retrieve the information**.

{% alert important %}
We recommend that you first import the new user profiles with the correct `external_id` and corresponding custom attributes and events. After user profiles are deleted, they can't be retrieved, so deleting should be the very last step.
{% endalert %}

Some additional things to note:

- Any engagement data (such as campaigns or Canvases received) on duplicate user profiles will be lost. The only way to retain the historical engagement context is by adding it as a custom attribute (such as an array custom attribute of all campaigns or Canvases received).
- When migrating user profiles, it's also up to your team to decide which user profile of the duplicates will be kept. Braze can't decide or provide you a list of profiles to delete.  
- Ultimately, it will be important for your team to assess the sign-up process from your users' experience and make sure that you're only calling the `changeUser()` method when a user becomes identified.

{% endapi %}
{% api %}

<!-- Segments -->

### How do I create a segment when I import a group of users through CSV?

{% apitags %}
Segments
{% endapitags %}

To import your CSV file, navigate to the **User Import** page under the Users section. The **Recent Imports** table lists up to twenty of your most recent imports, their file names, number of lines in the file, number of lines successfully imported, total lines in each file, and the status of each import.

The **Import CSV** panel contains importing directions and a button to begin your import. Click **Select CSV File** and select your file of interest. Then, before clicking **Start Import**, you have the option to let Braze know what to do with this list under "What do you want us to do with the users in this CSV".

Select **Import Users in this CSV and also make it possible to retarget this specific batch of users as a group**, and then select **Automatically generate a segment from the users who are imported from this CSV**. After you click **Start Import**, Braze will upload your file, check the column headers and the data types of each column, and create a segment.

To download a CSV template, refer to [user import]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv).

{% endapi %}
{% api %}

### What types of filters can I use when creating a segment?

{% apitags %}
Segments
{% endapitags %}

The Braze SDK provides you with a powerful arsenal of filters to segment and target your users based on specific features and attributes. You can use the [Segmentation Filters]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters) glossary to search or narrow these filters by Filter Category (Custom Data, User Activity, Retargeting, Marketing Activity, User Attributes, Install Attribution, Social Activity, Testing, Other).

{% endapi %}
{% api %}

### How do I set up location targeting so that I can segment users by their most recent location and use it in my location-based campaigns and strategies?

{% apitags %}
Segments
{% endapitags %}

Navigate to the **Segments** page, under Engagement, to view all of your current user segments. On this page, you can create and name new segments. To get started, click **Create Segment** and give your segment a name.

Once you have created your segment, add a `Most Recent Location` filter to target users by the last place that they used your app. You can either highlight users in a standard circular region or create a custom polygonal region.

- For circular regions, you can move the origin and adjust the location radius for your segmentation.
- For polygonal regions, you can more specifically designate which areas you wish to be included in your segment.

{% alert tip %}
Interested in taking advantage of location targeting with the help of a Braze partner? Check out our available Braze [contextual location partners]({{site.baseurl}}/partners/message_personalization/).
{% endalert %}

{% endapi %}
{% api %}

### How can I target precise lists of users based on their custom event and purchase behavior in the past 365 days?

{% apitags %}
Segments
{% endapitags %}

You can use [Segment Extensions]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/)! Segment Extensions enable you to target a more precise list of users than you otherwise could with a regular segment.

You can create up to 10 Segment Extensions per workspace. After these extension lists are generated, they can then be included or excluded as a filter in your segments. When creating a Segment Extension, you can also specify that the list be regenerated once every 24 hours.

1. Under Engagements, expand **Segments** and click **Segment Extension**.
2. From the Segment Extensions table, click **+ Create New Extension**.
3. Name your Segment Extension by describing the type of users you intend to filter for. This will ensure that this extension can be easily and accurately discovered when applying it as a filter in your segment.
4. Select between a purchase or custom event criteria for targeting.
5. Choose which purchased item or specific custom event you'd like to target for your user list. 
6. Choose how many times (more than, less than, or equal to) the user would need to have completed the event, and how many days to look back, up to 365 days.

To increase targeting precision, you can select **Add Property Filters** and segment based on the specific properties of your purchase or custom event. Braze supports event property segmentation based on string, numeric, boolean, and time objects.

We also support segmentation based on [nested event properties]({{site.baseurl}}/user_guide/data/custom_data/custom_events/nested_objects/).

Segment Extensions rely on long term storage of event properties and don't have the 30-day custom event property storage capacity. This means you can look back on event properties tracked within the past year, and tracking doesn't wait until the extension has been set up first.

{% alert note %}
Using event properties within Segment Extensions does not impact data point usage.
{% endalert %}

{% endapi %}
{% api %}

#### Keeping Segment Extensions up to date

{% apitags %}
Segments
{% endapitags %}

You can specify whether you want this extension to represent a single snapshot in time, or whether you want this extension to regenerate on a daily basis. Your extension will always begin processing after the initial save. If you would like the extension to be regenerated daily, select **Regenerate Extension Daily** and the regeneration will begin processing at around midnight each day in your company's time zone.

When you're done, click **Save**. Your extension will begin processing. The length of time it takes to generate your extension depends on how many users you have, how many custom events or purchase events you're capturing, and how many days you're looking back in history.

Finally, after you've created an extension, you can use it as a filter when creating a segment or defining an audience for a campaign or Canvas. Start by choosing `Braze Segment Extension` from the filter list under the **User Attributes** section. From the Braze Segment Extension filter list, choose the extension you wish to include or exclude in this segment. To view the extension criteria, click **View Extension Details**. Now you can proceed as usual with creating your segment.

{% endapi %}
{% api %}

<!-- Campaigns -->

### How do you create a multichannel campaign?

{% apitags %}
Campaigns
{% endapitags %}

To create a multichannel campaign, go to the **Campaigns** page, select **Create Campaign**, then select **Multichannel Campaign**. When inside a multichannel campaign, select **Add Messaging Channel** from the compose tab to add your desired channels. Click the channel icons that appear to toggle through different messaging composers as you build your campaign copy for the different channels.

{% endapi %}
{% api %}

### What are some ways I can start testing and optimizing campaigns?

{% apitags %}
Campaigns
{% endapitags %}

Creating multivariate campaigns and running Canvases with multiple variants are a great way to start! For example, you can run a [multivariate campaign]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) to test out one message that has different copies or subject lines. Canvases with multiple variants are helpful for testing entire workflows.

{% endapi %}
{% api %}

### Why is there a difference between the number of unique recipients and the number of sends for a given campaign or Canvas?

{% apitags %}
Campaigns
{% endapitags %}

One potential explanation for this difference could be due to the campaign or Canvas having re-eligibility turned on. By having this on, users who qualify for the segment and delivery settings will be able to receive the message more than once. If re-eligibility is not turned on, then the probable explanation for the difference between sends and unique recipients may be due to users having multiple devices across platforms associated with their profiles.

For example, should you have a Canvas that has both iOS and web push notifications, a given user with both mobile and desktop devices could receive more than one message.

{% endapi %}
{% api %}

### What does local time zone delivery offer?

{% apitags %}
Campaigns
{% endapitags %}

Local time zone delivery allows you to deliver messaging campaigns to a segment based on a user's individual time zone. Without local time zone delivery, campaigns will be scheduled based on your company's time zone settings in Braze.

For example, a London-based company sending a campaign at 12 pm will reach users on the west coast of America at 4 am. If your app is only available in certain countries, this may not be a risk for you, otherwise, we highly recommend avoiding sending early morning push notifications to your user base!

{% endapi %}
{% api %}

### How does Braze recognize a user's time zone?

{% apitags %}
Campaigns
{% endapitags %}

Braze will automatically determine a user's time zone from their device. This is designed to support time zone accuracy and full coverage of your users. Users created through the User API or otherwise without a time zone will have your company's time zone as their default time zone until they are recognized in your app by the SDK.

You can check your company's time zone in your [company settings]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/).

{% endapi %}
{% api %}

### How do I schedule a local time zone campaign?

{% apitags %}
Campaigns
{% endapitags %}

When scheduling a campaign, you need to choose to send it at a designated time, and then select **Send campaign to users in their local time zone**.

Braze highly recommends that all local time zone campaigns are scheduled 24 hours in advance. Since such a campaign needs to send over the course of an entire day, scheduling them 24 hours in advance allows your message reach your entire segment. However, you can schedule these campaigns less than 24 hours in advance if necessary. Keep in mind that Braze will not send messages to any users that have missed the send time by more than 1 hour.

For example, if it's 1 pm and you schedule a local time zone campaign for 3 pm, then the campaign will immediately send to all users whose local time is 3–4 pm, but not to users whose local time is 5 pm. In addition, the send time you choose for your campaign needs to have not yet occurred in your company's time zone.

Editing a local time zone campaign that is scheduled less than 24 hours in advance will not alter the message's schedule. If you decide to edit a local time zone campaign to send at a later time (for instance, 7 pm instead of 6 pm), users who were in the targeted segment when the original send time was chosen will still receive the message at the original time (6 pm). If you edit a local time zone to send at an earlier time (for instance, 4 pm instead of 5 pm), then the campaign will still send to all segment members at the original time (5 pm).

{% alert note %}
For Canvas steps, users do not need to be in the step for 24 hours to receive the next step for local time zone delivery.
{% endalert %}

If you have allowed users to become re-eligible for the campaign, then they will receive it again at the original time (5 pm). For all subsequent occurrences of your campaign, however, your messages only send at your updated time.

{% endapi %}
{% api %}

### When do changes to local time zone campaigns take effect?

{% apitags %}
Campaigns
{% endapitags %}

Target segments for local time zone campaigns should include at least a 48-hour window for any time-based filters to guarantee delivery to the entire segment. For example, consider a segment targeting users on their second day with the following filters:

- First used app more than 1 day ago
- First used app less than 2 days ago

Local time zone delivery may miss users in this segment based on the delivery time and the users' local time zone. This is because a user can leave the segment by the time their time zone triggers delivery.

{% endapi %}
{% api %}

### What changes can I make to scheduled campaigns ahead of launch?

{% apitags %}
Campaigns
{% endapitags %}

When the campaign is scheduled, edits to anything other than the message composition need to be made before we queue the messages to send. As per all campaigns, you can't edit conversion events after the campaign is launched.

{% endapi %}
{% api %}

### What is the "safe zone" before messages on a scheduled campaign are queued?

{% apitags %}
Campaigns
{% endapitags %}

- One-time scheduled campaigns can be edited up until the scheduled send time.
- Recurring scheduled campaigns can be edited up until the scheduled send time.
- Local send time campaigns can be edited up to 24 hours prior to the scheduled send time.
- Optimal send time campaigns can be edited up to 24 hours prior to the day the campaign is scheduled to send on.

{% endapi %}
{% api %}

### What if I make an edit within the "safe zone"?

{% apitags %}
Campaigns
{% endapitags %}

Changing the send time on campaigns within this time can lead to undesired behavior, for example:

- Braze will not send messages to any users that have missed the send time by more than one hour.
- Messages that were already queued may still send at the originally queued time, rather than the adjusted time.

{% endapi %}
{% api %}

### What should I do if the "safe zone" has already passed?

{% apitags %}
Campaigns
{% endapitags %}

To ensure campaigns operate as desired, we recommend stopping the current campaign (this will stop any queued messages). You can then duplicate the campaign, making the changes as necessary and launch the new campaign. You may need to exclude users from this campaign who have already received the first campaign.

Make sure to re-adjust campaign schedule times to allow for time zone sending.

{% endapi %}
{% api %}

### When does Braze evaluate users for local time zone delivery?

{% apitags %}
Campaigns
{% endapitags %}

For local time zone delivery, Braze evaluates users for their entry eligibility during these two instances:

- At Samoa time (UTC+13) of the scheduled day
- At local time of the scheduled day

For a user to be eligible for entry, they must be eligible for both checks. For example, if a Canvas is scheduled to launch on August 7, 2021 at 2 pm local time zone, then targeting a user located in New York would require the following checks for eligibility:

- New York on August 6, 2021 at 9 pm
- New York on August 7, 2021 at 2 pm

The user needs to be in the segment for 24 hours prior to the launch. If the user is not eligible in the first check, then Braze will not attempt the second check.

{% endapi %}
{% api %}

### Why does the number of users entering a campaign not match the expected number?

{% apitags %}
Campaigns
{% endapitags %}

The number of users entering a campaign may differ from your expected number because of how audiences and triggers are evaluated. In Braze, an audience is evaluated before the trigger (unless using a [change in attribute trigger]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/attribute_triggers#change-custom-attribute-value)). This will cause users to drop out of the campaign if they aren't initially part of your selected audience before any trigger actions are evaluated.

{% endapi %}
{% api %}

<!-- Canvases -->

### What happens if the audience and send time are identical for a Canvas that has one variant, but multiple branches?

{% apitags %}
Canvases
{% endapitags %}

We queue a job for each step—they run at around the same time, and one of them "wins". In practice, this may be sorted somewhat evenly, but it's likely to have at least a slight bias toward the step that was created first.

Moreover, we can't make any guarantees about exactly what that distribution will look like. If you want to ensure an even split, add a [random bucket number]({{site.baseurl}}/user_guide/engagement_tools/testing/random_bucket_numbers/) filter.

{% endapi %}
{% api %}

### What happens when you stop a Canvas?

{% apitags %}
Canvases
{% endapitags %}

When you stop a Canvas, the following applies:

- Users will be prevented from entering the Canvas.
- No further messages will be sent out, despite where a user is in the flow.
    - **Exception:** Email Canvases won't immediately stop. After the send requests go to SendGrid, there is nothing we can do to stop them from being delivered to the user.

{% alert note %}
Stopping a Canvas will not exit users who are waiting in a step. If you re-enable the Canvas and the users are still waiting, they will complete the step and move onto the next component. However, if the time that the user should've progressed to the next component has passed, they will instead exit the Canvas.
{% endalert %}

{% endapi %}
{% api %}

### When does an exception event trigger?

{% apitags %}
Canvases
{% endapitags %}

Exception events only trigger while the user is waiting to receive the Canvas component it's associated with. If a user performs an action in advance, the exception event will not trigger.

If you want to except users who have performed a certain event in advance, use [filters]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/) instead.

{% endapi %}
{% api %}

### How does editing a Canvas affect users already in the Canvas?

{% apitags %}
Canvases
{% endapitags %}

If you edit some of the steps of a multi-step Canvas, users who were already in the audience but have not received the steps will receive the updated version of the message. Note that this will only happen if they haven't been evaluated for the step yet.

For more information on what you can or can't edit after launch, check out [Changing Your Canvas After Launch]({{site.baseurl}}/post-launch_edits/).

{% endapi %}
{% api %}

### How are user conversions tracked in a Canvas?

{% apitags %}
Canvases
{% endapitags %}

A user can only convert once per Canvas entry.

Conversions are assigned to the most recent message received by the user for that entry. The summary block at the beginning of a Canvas reflects all conversions performed by users within that path, whether or not they received a message. Each subsequent step will only show conversions that happened while that was the most recent step the user received.

{% details Use cases %}

#### Use case 1

There is a Canvas path with 10 push notifications and the conversion event is "session start" ("Opens App"):

- User A opens the app after entering but before receiving the first message.
- User B opens the app after each push notification.

**Result:**
The summary will show two conversion while the individual steps will show a conversion of one on the first step and zero for all subsequent steps.

{% alert note %}
If Quiet Hours is active when the conversion event happens, the same rules apply.
{% endalert %}

#### Use case 2

There is a one-step Canvas with Quiet Hours:

1. User enters the Canvas.
2. First step has no delay, but is within Quiet Hours, so the message is suppressed.
3. User performs the conversion event.

**Result:**
The user will count as converted in the overall Canvas variant, but not the step since they didn't receive the step.

{% enddetails %}

{% endapi %}
{% api %}

### When looking at the number of unique users, is Canvas analytics or the segmenter more accurate?

{% apitags %}
Canvases
{% endapitags %}

The segmenter is a more accurate statistic for unique user data versus Canvas or campaign stats. This is because Canvas and campaign statistics are numbers that Braze increments when something happens—which means there are variables which could result in this number being different than that of the segmenter. For example, users can convert more than once for a Canvas or campaign.  

{% endapi %}
{% api %}

### Why does the number of users entering a Canvas not match the expected number?

{% apitags %}
Canvases
{% endapitags %}

The number of users entering a Canvas may differ from your expected number because of how audiences and triggers are evaluated. In Braze, an audience is evaluated before the trigger (unless using a [change in attribute]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/attribute_triggers/#change-custom-attribute-value) trigger). This will cause users to drop out of the Canvas if not part of your selected audience before any trigger actions are evaluated.

{% endapi %}
{% api %}

<!-- Analytics -->

### What metrics does Braze measure?

{% apitags %}
Analytics
{% endapitags %}

Depending on the channel, Braze measures a variety of metrics to enable you to determine a campaign's success and inform future ones. You can find a comprehensive list in our [report metrics glossary]({{site.baseurl}}/user_guide/data/report_metrics/).

{% endapi %}
{% api %}

### How is revenue calculated in Braze?

{% apitags %}
Analytics
{% endapitags %}

On the **Revenue** page, you can view data on revenue or purchases over specific periods of time, for a specific product, or your app's total revenue or purchases. These revenue numbers are generated from the purchases made from campaign recipients within a certain conversion period.

That being said, it's important to note that Braze is a marketing tool and not a revenue management tool. Our [purchase object]({{site.baseurl}}/api/objects_filters/purchase_object/) doesn't support refunds and cancellations, so you may see discrepancies when comparing data with other tools.

{% endapi %}
{% api %}

### What reporting capabilities does Currents enable?

{% apitags %}
Analytics
{% endapitags %}

Our Currents tool continuously streams both messaging engagement and customer behavior data to one of our many data partners, empowering you to use the unique and valuable data Braze creates to power your business intelligence and analytics efforts in other best-in-class partners.

This data goes beyond messaging engagement metrics, and can also includes more complex numbers such as custom attribute and event performance. For more details, review our [currents events glossary]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/).

{% endapi %}
{% api %}

### How can I schedule a recurring engagement report?

{% apitags %}
Analytics
{% endapitags %}

To schedule a recurring engagement report, do the following:

1. In your dashboard account, navigate to **Engagement Reports**, under **Data**.
2. Click **+ Create New Report**.
3. Add the [campaigns and Canvas messages]({{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/#manually-select-campaigns-or-canvases) (individually or [by tag]({{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/#automatically-select-campaigns-or-canvases)) that you would like to compile in your report.
4. [Add statistics]({{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/#add-statistics-to-your-report) to your report.
5. Select the compression and deliminator for your report.
6. Enter the email addresses of Braze users who should receive this report.
7. Select the [time frame]({{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/#time-frame) from which you would like your report to run data.
8. Select the [intervals (daily, weekly, etc.)]({{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/#data-display) at which would like to see the breakdown of your data.
9. Schedule your report to [send immediately]({{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/#send-immediately) or at a [future, specified time]({{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/#send-at-designated-time).
10. Run the report, then open it in your email when it arrives!

{% endapi %}
{% api %}

### What's the difference between Engagement Reports and the Report Builder?

{% apitags %}
Analytics
{% endapitags %}

Engagement Reports provide you with CSVs of engagement statistics for specific messages from campaigns and Canvases via a triggered email. Certain data is aggregated at the campaign or Canvas level versus at the individual variant or step level. Reports are not saved in the dashboard, and re-running the report can result in updated statistics.

The Report Builder allows you to compare the results of multiple campaigns or Canvases in a single view so that you can easily determine which engagement strategies most impacted your key metrics. For both campaigns and Canvases, you're able to export your data and save your report to view in the future.

For more information on the uses of reports and analytics in Braze, refer to [reports overview]({{site.baseurl}}/user_guide/analytics/reporting/reports_overview/).

{% endapi %}
