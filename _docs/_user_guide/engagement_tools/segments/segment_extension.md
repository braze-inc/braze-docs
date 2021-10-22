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

A Segment Extension expands our existing segmentation capabilities by enabling you to target more precise lists of users based on their custom event and purchase behavior in the past 365 days. You can create a maximum of 10 Segment Extensions per App Group. After these extension lists are generated, they can then be included or excluded as a [filter][10] in your segments. When creating a Segment Extension, you can also specify that the list be regenerated once every 24 hours.

## Step 1: Navigate to Segment Extensions

From the left-hand side of the Dashboard under Engagement, expand the Segments section, and click **Segment Extension**. From the Segment Extensions table, click **+ Create New Extension**.

![Segment Extension Nav][1]

## Step 2: Name your Segment Extension

Name your Segment Extension by describing the type of users you intend to filter for. This will ensure that this extension can be easily and accurately discovered when applying it as a filter in your segment.

![Segment Extension Name][2]

## Step 3: Choose your criteria

Select between a purchase or custom event criteria for targeting. Once you've selected the desired event type criteria, choose which purchased item or specific custom event you'd like to target for your user list. Then choose how many times (more than, less than, or equal to) the user would need to have completed the event, and how many days to look back, up to 365 days.

![Segment Extension Criteria][3]

### Event property segmentation

To increase targeting precision, select the **Add Property Filters** checkbox. This will enable you to drill down based on the specific properties of your purchase or custom event. We support event property segmentation based on string, numeric, boolean, and time objects. We also support segmentation based on [nested event properties]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/nested_object_support/).

![Event Property][12]

![Arrow][16]{: style="border:0;"}

![Event Property][13]{: style="max-width:85%;"}

![Event Property][14]{: style="max-width:85%;"}

![Event Property][15]{: style="max-width:85%;"}

Segment Extensions rely on long term storage of event properties and don't have the 30-day custom event property storage limit. This means you can look back on event properties tracked within the past year, and tracking doesn't wait until the extension has been set up first.

{% alert note %} Using event properties within Segment Extensions does not impact data point usage.  {% endalert %}

### Extension regeneration

You can specify whether you want this extension to represent a single snapshot in time, or whether you want this extension to regenerate on a daily basis. Your extension will always begin processing after the initial save. If you would like the extension to be regenerated daily, select the **Regenerate Extension Daily** checkbox and the regeneration will begin processing at around midnight each day in your company’s time zone.

{% alert important %}
Starting on November 29, 2021, the setting to regenerate extensions daily will be automatically turned off for unused Segment Extensions. Braze defines unused extensions as ones that meet the following criteria:

- Not used in any active campaigns, Canvases, or segments
- Not used in any inactive (draft, stopped, archived) campaigns, Canvases, or segments
- Have not been modified in over 7 days

Braze will notify the company contact and creator of the extension when this setting is turned off. The option to regenerate extensions daily can be turned on again at any time.
{% endalert %}

## Step 4: Save your segment extension

Once you click **Save**, your extension will begin processing. The length of time it takes to generate your extension depends on how many users you have, how many custom events or purchase events you're capturing, and how many days you're looking back in history.

While your extension is processing, you will see a small animation next to the name of the extension, and the word "Processing" in the **Last Processed** column on the extension list. Note that you will not be able to edit an extension while it is processing.

![Segment Extension Processing][5]

## Step 5: Use your extension in a segment

Once you have created an extension, you can use it as a filter when creating a segment or defining an audience for a campaign or Canvas. Start by choosing **Braze Segment Extension** from the filter list under the **User Attributes** section.

![Segment Extension as a Segment Filter][6]

From the Braze Segment Extension filter list, choose the extension you wish to include or exclude in this segment.

![Segment Extension as a Segment Filter][7]

To view the extension criteria, click **View Extension Details** to show the details in a modal popup.

![Segment Extension Details Modal][8]{: style="max-width:60%;"}

Now you can proceed as usual with [creating your segment][11].

[1]: {% image_buster /assets/img/segment/segment_extension1.png %}
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
