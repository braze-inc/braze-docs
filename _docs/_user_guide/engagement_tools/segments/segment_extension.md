---
nav_title: Segment Extensions
article_title: Segment Extensions
page_order: 3.1

page_type: tutorial
description: "This how-to article will walk you through how to set up and use a Segment Extension to enhance your segmentation capabilities."
tool: Segments
---

# Segment Extensions

> Braze segmentation allows you to target users based on custom event or purchase behavior stored for the lifetime of that user profile. Examples include finding users who have or not have performed a particular custom event since a specific time, or segmenting users based on which products they have ever purchased or how much money they have spent with your service.

Segment Extensions are audience definitions which allow you to use nested event properties or create windowed aggregations of custom event and purchase event properties in the past 2 years (730 days). For example, Braze segmentation allows you to find users who have purchased a specific product in their lifetime. With Segment Extensions, you can further refine that audience to users who have purchased a specific color of a specific product at least twice in the past 2 years. When creating a Segment Extension, you can also specify that the audience be static or regenerated daily.

The use of nested event properties for [action-based delivery][19] does not require Segment Extensions, as event processing occurs in real-time. Nested custom attributes similarly do not require the use of Segment Extensions.

{% alert important %}
There is a default allotment of 25 active Segment Extensions per workspace at a particular time. If you need to increase this limit, contact your Braze customer success manager to discuss your use case.
{% endalert %}

## Step 1: Navigate to Segment Extensions

Go to **Audience** > **Segment Extensions**.

{% alert note %}
If you are using the [older navigation]({{site.baseurl}}/navigation), you can find this page at **Engagement** > **Segments** > **Segment Extensions**.
{% endalert %}

From the Segment Extensions table, click **Create New Extension**, then select your Segment Extension creation experience:

- **Simple extension:** Create a Segment Extension focused on a single event by using a guided form.
Best for when you don't want to use SQL.
- **Start with a template:** Create a SQL segment with a customizable template using Snowflake data.
- **Incremental refresh:** Write a Snowflake SQL segment that automatically refreshes the last 2 days of data or manually refresh as needed. Best for balancing accuracy and cost-efficiency.
- **Full refresh:** Write a Snowflake SQL segment that recalculates the entire audience upon manual refresh. Best for when you need a complete, up-to-date view of your audience.

![][20]{: style="max-width:50%"}

If you select an experience that uses SQL, see [SQL Segment Extensions]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/) for further information.

If you select **Simple extension**, continue to the steps below.

## Step 2: Name your Segment Extension

Name your Segment Extension by describing the type of users you intend to filter for. This will ensure that this extension can be easily and accurately discovered when applying it as a filter in your segment.

![Segment Extension named "Online Shoppers Extension - 90 Days" with the checkbox "Regenerate Extension Daily" selected.][2]

## Step 3: Choose your criteria

Select between purchase, message engagement, or custom event criteria for targeting. After you've selected the desired event type criteria, choose which purchased item, message interaction, or specific custom event you'd like to target for your user list. Then choose how many times (more than, less than, or equal to) the user would need to have completed the event, and the time period—for Segment Extensions specifically, you can go back up to the past 730 days (2 years).

Segmentation based on event data from more than 730 days can be done using other filters located in **Segments**. When choosing your time period, you can specify a relative date range (such as past X days), a start date, an end date, or an exact date range (date A to date B).

![][3]

### Event property segmentation

To increase targeting precision, select the **Add Property Filters** checkbox. This will enable you to drill down based on the specific properties of your purchase or custom event. We support event property segmentation based on string, numeric, boolean, and time objects.

For string properties, you can enter in multiple values at once. In the example below, this filter looks for users with a status equal to any of the following: gold, silver, or bronze.

![Segmenting based on string properties.][13.5]

![Segmenting based on numeric properties.][13]

![Segmenting based on boolean properties.][14]

![Segmenting based on datetime objects.][15]

We also support segmentation based on [nested event properties]({{site.baseurl}}/user_guide/data/custom_data/custom_events/nested_objects/).

![Segmenting based on nested event properties.][18]

Segment Extensions rely on long term storage of event properties and don't have a time-stamped property storage limit. You can look back on event properties tracked within the past two years.

{% alert note %}
Using event properties within Segment Extensions does not impact data point usage.
{% endalert %}

## Step 4: Designate refresh settings (optional)

If you don't need your extension to refresh on a regular schedule, you can save it without using refresh settings, and Braze will default to generating your Segment Extension based on your user membership at that moment. Use the default behavior if you only want to generate the audience once and then target it with a one-off campaign.

Your segment will always begin processing after the initial save. Whenever your segment refreshes, Braze will re-run the segment and update segment membership to reflect the users in your segment at the time of refresh. This can help your recurring campaigns reach the most relevant users.

### Setting up a recurring refresh

To set up a recurring schedule, select **Refresh Settings** in the upper right corner of your specific extension. The option to designate refresh settings is available for all types of Segment Extensions, including SQL segments, CDI segments, and simple form-based Segment Extensions.

{% alert important %}
Refresh settings are automatically turned off for unused Segment Extensions. Braze defines unused extensions as ones that meet the following criteria:

- Not used in any active campaigns, Canvases, or segments
- Not used in any inactive (draft, stopped, archived) campaigns, Canvases, or segments
- Have not been modified in over 7 days

Braze will notify the company contact and creator of the extension when this setting is turned off. The option to regenerate extensions daily can be turned on again at any time.
{% endalert %}

#### Selecting your refresh settings

![Refresh Interval Settings with a weekly refresh frequency, start time of 10 am, and Monday selected as a day.][21]{: style="max-width:60%;"}

Within the **Refresh Settings** panel, you can select the frequency at which this segment extension will refresh: hourly, daily, weekly, or monthly. You’ll also be required to select the specific time (which is in your company’s time zone) the refresh would occur, such as:

- If you have an email campaign that is sent every Monday at 11 am company time, and you want to ensure your segment is refreshed right before it's sent, you should choose a refresh schedule of weekly at 10 am on Mondays.
- If you’d like your segment to refresh every day, select the daily refresh frequency and then choose the time of day to refresh.

{% alert note %}
The ability to set an hourly refresh schedule isn't available for form-based Segment Extensions (but you can set daily, weekly, or monthly schedules). 
{% endalert %}

### Credit consumption and additional costs

Because refreshes re-run your segment’s query, each refresh for SQL segments will consume SQL segment credits, and each refresh for CDI segments will incur a cost within your third-party data warehouse.

{% alert note %}
Segments could require up to 60 minutes to refresh because of data processing times. Segments that are currently in the process of refreshing will have a “Processing” status within your Segment Extensions list. This has a couple of implications:

- To finish processing your segment before a specific time, choose a refresh time that is 60 minutes earlier. 
- Only one refresh can occur at a time for a specific Segment Extension. If there is a conflict where a new refresh is initiated when an existing refresh has already begun processing, Braze will cancel the new refresh request and continue the in-progress processing. 
{% endalert %}

## Step 5: Save your Segment Extension

Once you click **Save**, your extension will begin processing. The length of time it takes to generate your extension depends on how many users you have, how many custom events or purchase events you're capturing, and how many days you're looking back in history.

While your extension is processing, you will see a small animation next to the name of the extension, and the word "Processing" in the **Last Processed** column on the extension list. Note that you will not be able to edit an extension while it is processing.

![][5]

## Step 6: Use your extension in a segment

Once you have created an extension, you can use it as a filter when creating a segment or defining an audience for a campaign or Canvas. Start by choosing **Braze Segment Extension** from the filter list under the **User Attributes** section.

![][6]

From the Braze Segment Extension filter list, choose the extension you wish to include or exclude in this segment.

![][7]

To view the extension criteria, click **View Extension Details** to show the details in a modal popup.

![][8]{: style="max-width:70%;"}

Now you can proceed as usual with [creating your segment][11].

[2]: {% image_buster /assets/img/segment/segment_extension2.png %}
[3]: {% image_buster /assets/img/segment/segment_extension1.png %}
[5]: {% image_buster /assets/img/segment/segment_extension5.png %}
[6]: {% image_buster /assets/img/segment/segment_extension7.png %}
[7]: {% image_buster /assets/img/segment/segment_extension6.png %}
[8]: {% image_buster /assets/img/segment/segment_extension8.png %}
[10]: {{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/
[11]: {{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/
[12]: {% image_buster /assets/img/segment/property1.png %}
[13]: {% image_buster /assets/img/segment/property2.png %}
[13.5]: {% image_buster /assets/img/segment/property5.png %}
[14]: {% image_buster /assets/img/segment/property3.png %}
[15]: {% image_buster /assets/img/segment/property4.png %}
[16]: {% image_buster /assets/img/Shopify/arrow.jpeg %}
[17]: {% image_buster /assets/img/segment/segment_extension9.png %}
[18]: {% image_buster /assets/img/segment/nested_segment_extensions.png %}
[19]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/
[20]: {% image_buster /assets/img/segment/segment_extension_modal.png %}
[21]: {% image_buster /assets/img/segment/segment_interval_settings.png %}
