---
nav_title: Segment Cohorts
page_order: 2

page_type: tutorial
channel:

hidden: true

description: "This how-to article will walk you through how to use Segment Cohorts with Braze Segments."
---
# Creating and Using a Segment Cohort

> This article will walk you through how to use Segment Cohorts to enhance your segmentation capabilities

Segment Cohorts expand our existing segmentation capabilities by enabling you to target more precise lists of users based on their custom event and purchase behavior in the past 365 days. Once these cohort lists are generated, they can then be included/excluded as a [filter][10] in your Segments. When creating a Segment Cohort, you can also specify that the list be regenerated once every 24 hours.

## Step 1: Navigating to the Segment Cohorts Section

From the left-hand side of the Dashboard under Engagement, expand the Segments section, and click on Segment Cohorts. From the Segment Cohorts table, click the "+ Create New Cohort" button at the top right of the table.

![Segment Cohorts Nav][1]

## Step 2: Name Your Segment Cohort

Name your Segment Cohort by describing the type of users you intend to filter for. This will ensure that this Cohort can be easily and accurately discovered when applying it as a filter in your segment.

![Segment Cohorts Name][2]

## Step 3: Choose Your Criteria

Select between a Purchase or Custom Event criteria for targeting. Once you've selected the desired event type criteria, choose which Purchased Item or specific Custom Event you'd like to target for your user list. Then choose how many times (more than, less than, or equal to) the user would need to have completed the event, and how many days to look back, up to 365 days.

![Segment Cohorts Criteria][3]

### Event Property Segmentation

To increase targeting precision, select the “Add Property Filters” checkbox. This will enable you to drill down based on the specific properties of your Purchase or Custom Event. We support event property segmentation based on string, numeric, boolean, and time objects. 

![Event Property][12]

![Arrow][16]{: style="border:0;"}

![Event Property][13]

![Event Property][14]

![Event Property][15]{: style="max-width:85%;"}

### Cohort Regeneration

You can specify whether you want this cohort to represent a single snapshot in time, or whether you want this cohort to regenerate on a daily basis. Your cohort will always begin processing after the initial save. If you would like the cohort to be regenerated daily, select the “Regenerate Cohort Daily” checkbox and the regeneration will begin processing at around midnight each day in your company’s time zone.

## Step 4: Save Your Segment Cohort

![Segment Cohort Save][4]

Once you click "Save", your cohort will begin processing. The length of time it takes to generate your cohort depends on how many users you have, how many Custom or Purchase events you're capturing, and how many days you're looking back in history.

While your cohort is processing, you will see a small animation next to the name of the cohort, and the word "Processing" in the "Last Processed" column on the cohort list. Note that you will not be able to edit a cohort while it is processing.

![Segment Cohort Processing][5]

## Step 5: Using Your Cohort in a Segment

Once you have created a cohort, you can use it as a filter when creating a segment or defining an audience for a Campaign or Canvas. Start by choosing "Braze Segment Cohort" from the filter list under the "User Attributes" section.

![Segment Cohort as a Segment Filter][6]

From the Braze Segment Cohort filter list, choose the cohort you wish to include/exclude in this Segment.

![Segment Cohort as a Segment Filter][7]

To view the cohort criteria, click the "View Cohort Details" link to show the details in a modal popup.

![Segment Cohort Details Modal][8]{: style="max-width:60%;"}

Now you can proceed as usual with [creating your segment][11].

[1]: {% image_buster /assets/img/cohort/segment_cohort_nav.png %}
[2]: {% image_buster /assets/img/cohort/segment_cohort_name.png %}
[3]: {% image_buster /assets/img/cohort/segment_cohort_criteria.png %}
[4]: {% image_buster /assets/img/cohort/segment_cohort_save.png %}
[5]: {% image_buster /assets/img/cohort/segment_cohort_list.png %}
[6]: {% image_buster /assets/img/cohort/segment_cohort_as_filter1.png %}
[7]: {% image_buster /assets/img/cohort/segment_cohort_as_filter2.png %}
[8]: {% image_buster /assets/img/cohort/segment_cohort_view.png %}
[10]: {{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/
[11]: {{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/
[12]: {% image_buster /assets/img/cohort/property1.png %}
[13]: {% image_buster /assets/img/cohort/property2.png %}
[14]: {% image_buster /assets/img/cohort/property3.png %}
[15]: {% image_buster /assets/img/cohort/property4.png %}
[16]: {% image_buster /assets/img/shopify/arrow.jpeg %}