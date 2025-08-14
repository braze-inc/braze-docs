---
nav_title: Segment Extensions
article_title: Segment Extensions
page_order: 6
page_type: reference
description: "This how-to article will walk you through how to set up and use a Segment Extension to enhance your segmentation capabilities."
tool: Segments
---

# Segment Extensions

> Segment Extensions allow you to build very precise segments over an extended period of a user's history. For example, using Segment Extensions you can target users who have purchased a particular product in the last sixteen months or have spent a certain amount of money with your service. Refine this audience by using event properties to make targeting even more granular.

Braze segmentation allows you to target users based on custom event or purchase behavior. Segment Extensions enhances this capacity, letting you draw on historic data saved on the user profile. Using Segment Extensions, you can identify and reach users who have completed any custom event or purchase event any number of times in the past two years (730 days). 

## Why use Segment Extensions?

Braze segments give you powerful targeting tools to create dynamic groups of users. For most use cases, this is enough to reach your audience effectively. Segment Extensions are designed for advanced use cases where you need to analyze behaviors from up to two years ago or apply complex logic—without compromising data retention or system performance. You can use [SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments) queries (SQL Segment Extensions) or data from your own [data warehouse]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/cdi_segments) to refine your audience further.

For example, Braze default segmentation will find users that fit specific criteria you define, such as identifying a user who recently purchased one of your products. Segment Extensions let you go deeper—like identifying users who bought a particular color of a specific product at least twice between 18 to 24 months ago. Segment Extensions are an enhancement, not a requirement. If you need more advanced filters or a longer lookback window, they're a great tool to help while keeping your data usage optimized.

{% alert note %}
There is a default allotment of 25 active Segment Extensions per workspace at a particular time. If you need to increase this limit, contact your Braze customer success manager to discuss your use case.
{% endalert %}

### SQL credit usage

The following Segment Extension types consume SQL credits:

- SQL Segment Extensions (both incremental and full refresh)
- Catalog Segments
- CDI Segments 
    - Credits are consumed within your own data warehouse

## Creating a Segment Extension

To create a Segment Extension, you will create a filter to refine a segment of your users based on custom event properties. When creating a Segment Extension, you will choose whether the segment will be static or dynamically refreshed at a set interval.

### Step 1: Navigate to Segment Extensions

Go to **Audience** > **Segment Extensions**.

From the Segment Extensions table, select  **Create New Extension**, then select your Segment Extension creation experience:

- **Simple extension:** Create a Segment Extension focused on a single event by using a guided form.
Best for when you don't want to use SQL.
- **Start with a template:** Create a SQL segment with a customizable template using Snowflake data.
- **Incremental refresh:** Write a Snowflake SQL segment that automatically refreshes the last 2 days of data or manually refresh as needed. Best for balancing accuracy and cost-efficiency.
- **Full refresh:** Write a Snowflake SQL segment that recalculates the entire audience upon manual refresh. Best for when you need a complete, up-to-date view of your audience.

![Table with different Segment Extension creation experiences to select from.]({% image_buster /assets/img/segment/segment_extension_modal.png %}){: style="max-width:50%"}

If you select an experience that uses SQL, see [SQL Segment Extensions]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/) for further information.

If you select **Simple extension**, continue to the steps below.

### Step 2: Name your Segment Extension

Name your Segment Extension by describing the type of users you intend to filter for. This will ensure that this extension can be easily and accurately discovered when applying it as a filter in your segment.

![Segment Extension named "Online Shoppers Extension - 90 Days".]({% image_buster /assets/img/segment/segment_extension2.png %})

### Step 3: Choose your criteria

Select between purchase, message engagement, or custom event criteria for targeting. After you've selected the desired event type criteria, choose which purchased item, message interaction, or specific custom event you'd like to target for your user list. Then choose how many times (more than, less than, or equal to) the user would need to have completed the event, and the time period—for Segment Extensions specifically, you can go back up to the past 730 days (2 years).

Segmentation based on event data from more than 730 days can be done using other filters located in **Segments**. When choosing your time period, you can specify a relative date range to select the past X number of days, a start date, an end date, or an exact date range (date A to date B).

![Segmentation criteria for users who performed a custom event more than 2 times in the date range of March 1st, 2025 through March 31st, 2025.]({% image_buster /assets/img/segment/segment_extension1.png %})

#### Event property segmentation

To increase targeting precision, select the **Add Property Filters** checkbox. This will enable you to drill down based on the specific properties of your purchase or custom event. We support event property segmentation based on string, numeric, boolean, and time objects.

For string properties, you can enter in multiple values at once. In the example below, this filter looks for users with a status equal to any of the following: gold, silver, or bronze.

![Segmenting based on string properties.]({% image_buster /assets/img/segment/property5.png %})

![Segmenting based on numeric properties.]({% image_buster /assets/img/segment/property2.png %})

![Segmenting based on boolean properties.]({% image_buster /assets/img/segment/property3.png %})

![Segmenting based on datetime objects.]({% image_buster /assets/img/segment/property4.png %})

We also support segmentation based on [nested event properties]({{site.baseurl}}/user_guide/data/custom_data/custom_events/nested_objects/).

![Segmenting based on nested event properties.]({% image_buster /assets/img/segment/nested_segment_extensions.png %})

Segment Extensions rely on long term storage of event properties and don't have a time-stamped property storage limit. You can look back on event properties tracked within the past two years. Using event properties within Segment Extensions does not impact data point usage.

{% alert note %}
You don't need Segment Extensions to use event properties or nested custom attributes in your segment. Segment Extensions just extend the historic window used to create a default segment. You can create a real-time default [segment]({{site.baseurl}}/user_guide/engagement_tools/segments/) that uses event properties from the past 30 days or uses nested custom attributes. Similarly, you can [schedule your message]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/) to trigger in real time based on an event property—no Segment Extension required. 
{% endalert %}

### Step 4: Designate refresh settings (optional)

{% multi_lang_include segments.md section='Refresh settings' %}

### Step 5: Save your Segment Extension

After you select **Save**, your Segment Extension will begin processing. The length of time it takes to generate your Segment Extension depends on how many users you have, how many custom events or purchase events you're capturing, and how many days you're looking back in history.

While your Segment Extension is processing, you will see a small animation next to the name of the Segment Extension, and the word "Processing" in the **Last Processed** column on the Segment Extension list. Note that you will not be able to edit a Segment Extension while it is processing.

!["Segment Extensions" page with two active extensions.]({% image_buster /assets/img/segment/segment_extension5.png %})

When a Segment Extension is processing, Braze will continue to use the version history of the default segment from before the processing began for audience segmentation purposes. Processing takes place each time a save or refresh occurs, and involves querying and updating user profiles—in other words, your default segment's membership does not update instantaneously. This means that unless a user's action is performed before the refresh begins processing, we can't guarantee that the user will be included in the Segment Extension once that particular refresh is complete. Conversely, users who were in the Segment Extension before the refresh that no longer meet the criteria will continue to match your deafult segment until the refresh process is complete and updates are applied.

### Step 6: Use your extension in a segment

After you have created a Segment Extension, you can use it as a filter when creating a segment or defining an audience for a campaign or Canvas. Start by choosing **Braze Segment Extension** from the filter list under the **User Attributes** section.

!["Filters" section with a filter dropdown showing "Braze Segment Extensions".]({% image_buster /assets/img/segment/segment_extension7.png %})

From the Braze Segment Extension filter list, choose the Segment Extension you wish to include or exclude in this segment.

![A "Braze Segment Extensions" filter that includes a segment "1 email click in the last 56 days".]({% image_buster /assets/img/segment/segment_extension6.png %})

To view the Segment Extension criteria, select **View Extension Details** to show the details in a new window.

![Extension for "1 email click in the last 56 days".]({% image_buster /assets/img/segment/segment_extension8.png %}){: style="max-width:70%;"}

Now you can proceed as usual with [creating your segment]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/).

## Frequently asked questions

### Can I create a Segment Extension that uses multiple custom events?

Yes. You can add multiple events or reference multiple Snowflake tables when using [SQL Segment Extensions]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/). 

When using **Simple extension** Segment Extensions, you can select one custom event, one purchase event, or one channel interaction. However, you can combine multiple Segment Extensions with an AND or OR when creating the default segment.

### Can I archive Segment Extensions if they exist in an active campaign?

No. Before you can archive a Segment Extension, you need to remove it from all active messaging.

### Can I use arrays in Segment Extensions?

Yes. To use arrays, append brackets (`[]`) to your property name. If your property is `location_code`,  you would enter `location_code[]`. 

Braze uses `[]` to traverse arrays and check if any item in the traversed array matches the event property. For example, you could create a Segment Extension of users who match at least one value of an array property.

### How does Braze calculate the time period for a relative time period of "last __ days"?

When Segment Extensions calculates the relative time period ("last X days"), the start time is set to midnight UTC. For example, for a Segment Extension that refreshes at 2024-09-16 21:00 UTC and specifies 10 days, the start time is set to 2024-09-06 00:00 UTC, not 2024-09-06 21:00 UTC. 

However, you can specify the time zones by using SQL segments to identify users who performed the custom event 10 days ago based on midnight in company time, or users who performed the event 10 days ago based on the current time.

