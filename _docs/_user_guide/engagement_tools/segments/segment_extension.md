---
nav_title: Segment Extensions
article_title: Segment Extensions
page_order: 3.1

page_type: tutorial
description: "This how-to article will walk you through how to use a Segment Extension with Braze Segments."
tool: Segments
---

# Segment Extensions

> This article will walk you through how to use a Segment Extension to enhance your segmentation capabilities

Braze Segmentation allows you to target users based on custom event or purchase behavior stored for the lifetime of that user profile. Examples include finding users who have or not have performed a particular custom event since a specific time, or segmenting users based on which products they have ever purchased or how much money they have spent with your service.

Segment Extensions are audience definitions which allow you to use nested event properties or create windowed aggregations of custom event and purchase event properties in the past 2 years (730 days). By means of example, Braze segmentation allows you to find users who have purchased a specific product in their lifetime. With Segment Extensions, you can further refine that audience to users who have purchased a specific color of a specific product at least twice in the past 2 years. When creating a Segment Extension, you can also specify that the audience be static or regenerated daily.

The use of nested event properties for [Action-Based Delivery][19] does not require Segment Extensions, as event processing occurs in real-time. Nested custom attributes similarly do not require the use of Segment Extensions.

{% alert important %}
Out of the box, there is a limit of 25 active Segment Extensions per app group at a particular time. If you need to increase this limit, contact your Braze customer success manager to discuss your use case.
{% endalert %}

## Step 1: Navigate to Segment Extensions

Under **Engagements**, expand **Segments** and click **Segment Extension**. From the Segment Extensions table, click <i class="fas fa-plus"></i> **Create New Extension**.

## Step 2: Name your Segment Extension

Name your Segment Extension by describing the type of users you intend to filter for. This will ensure that this extension can be easily and accurately discovered when applying it as a filter in your segment.

![Segment Extension named "Online Shoppers Extension - 90 Days" with the checkbox "Regenerate Extension Daily" selected.][2]

## Step 3: Choose your criteria

Select between purchase, message engagement, or custom event criteria for targeting. Once you’ve selected the desired event type criteria, choose which purchased item, message interaction, or specific custom event you’d like to target for your user list. Then choose how many times (more than, less than, or equal to) the user would need to have completed the event, and how many days to look back, up to 730 days (2 years). Segmentation based on event data from more than 730 days can be done using other filters located in **Segments**.

![][3]

### Event property segmentation

To increase targeting precision, select the **Add Property Filters** checkbox. This will enable you to drill down based on the specific properties of your purchase or custom event. We support event property segmentation based on string, numeric, boolean, and time objects.

![Segmenting based on numeric properties.][13]

![Segmenting based on boolean properties.][14]

![Segmenting based on datetime objects.][15]

We also support segmentation based on [nested event properties]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#nested-objects).

![Segmenting based on nested event properties.][18]

Segment Extensions rely on long term storage of event properties and don’t have a time-stamped property storage limit. You can look back on event properties tracked within the past two years.

{% alert note %}
Using event properties within Segment Extensions does not impact data point usage.
{% endalert %}

### Extension regeneration

You can specify whether you want this extension to represent a single snapshot in time, or whether you want this extension to regenerate on a daily basis. Your extension will always begin processing after the initial save. If you would like the extension to be regenerated daily, select the **Regenerate Extension Daily** checkbox and the regeneration will begin processing at around midnight each day in your company’s time zone.

{% alert important %}
The setting to regenerate extensions daily is automatically turned off for unused Segment Extensions. Braze defines unused extensions as ones that meet the following criteria:

- Not used in any active campaigns, Canvases, or segments
- Not used in any inactive (draft, stopped, archived) campaigns, Canvases, or segments
- Have not been modified in over 7 days

Braze will notify the company contact and creator of the extension when this setting is turned off. The option to regenerate extensions daily can be turned on again at any time.
{% endalert %}

## Step 4: Save your segment extension

Once you click **Save**, your extension will begin processing. The length of time it takes to generate your extension depends on how many users you have, how many custom events or purchase events you're capturing, and how many days you're looking back in history.

While your extension is processing, you will see a small animation next to the name of the extension, and the word "Processing" in the **Last Processed** column on the extension list. Note that you will not be able to edit an extension while it is processing.

![][5]

## Step 5: Use your extension in a segment

Once you have created an extension, you can use it as a filter when creating a segment or defining an audience for a campaign or Canvas. Start by choosing **Braze Segment Extension** from the filter list under the **User Attributes** section.

![][6]

From the Braze Segment Extension filter list, choose the extension you wish to include or exclude in this segment.

![][7]

To view the extension criteria, click **View Extension Details** to show the details in a modal popup.

![][8]{: style="max-width:70%;"}

Now you can proceed as usual with [creating your segment][11].

[2]: {% image_buster /assets/img/segment/segment_extension2.png %}
[3]: {% image_buster /assets/img/segment/segment_extension3.png %}
[5]: {% image_buster /assets/img/segment/segment_extension5.png %}
[6]: {% image_buster /assets/img/segment/segment_extension7.png %}
[7]: {% image_buster /assets/img/segment/segment_extension6.png %}
[8]: {% image_buster /assets/img/segment/segment_extension8.png %}
[10]: {{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/
[11]: {{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/
[12]: {% image_buster /assets/img/segment/property1.png %}
[13]: {% image_buster /assets/img/segment/property2.png %}
[14]: {% image_buster /assets/img/segment/property3.png %}
[15]: {% image_buster /assets/img/segment/property4.png %}
[16]: {% image_buster /assets/img/Shopify/arrow.jpeg %}
[17]: {% image_buster /assets/img/segment/segment_extension9.png %}
[18]: {% image_buster /assets/img/segment/nested_segment_extensions.png %}
[19]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/triggered_delivery/
