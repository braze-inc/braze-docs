---
nav_title: Creating a Segment
article_title: Creating a Segment
page_order: 1
page_type: tutorial
description: "This how-to article will walk you through how to set up and create a segment using Braze."
tool: Segments
---

# Creating a segment

> This article will walk you through the steps of creating a segment, filtering your target audience, and segment navigation and archival.

Your developers have integrated the SDK, and the data from your users have begun pouring in. Now what? It's time to start segmenting your users. Follow the guide below or check out [our LAB Segmentation course](https://lab.braze.com/segmentation-course)!

Segmentation allows you to target users based upon their demographic, behavioral, social, or technical characteristics and actions. Creative and intelligent use of segmentation and messaging automation enables you to seamlessly move your users from first touch to long-term customer. Segments update in real-time as data changes, and you can create as many segments as needed for your targeting and messaging purposes.

## Step 1: Navigating to the segments section

!\[Segments Menu\]\[1\]{: style="float:right;max-width:20%;"}

From the left-hand side of the Dashboard under Engagement, click **Segments**.

## Step 2: Name your segment

Name your segment by describing the type of user you intend to filter for. This will ensure that this segment can accurately be the target of multiple campaigns or Canvases to come. Vague segment titles can cause confusion down the line.

Optionally, you can add a description to the segment to provide more details about the intention of this audience and leave notes for other team members to refer back to.

!\[Create a Segment\]\[2\]{: style="max-width:70%;"}

## Step 3: Choose your app or platform

Choose which apps or platforms you'd like to target by either selecting **Include users from all apps** (default), or by clearing the checkbox. If you clear this option, you can then select which apps or platforms you want to include in your segment. For example, if you'd like to send an in-app message to only iOS devices, select your iOS app. This will ensure that users who might use both an iOS and an Android device will only receive the message on their iOS device.

For more information on this option, refer to the section [Segment Membership Calculation](#segment-membership-calculation).

!\[Segment App Selection\]\[5\]

## Step 4: Add filters to your segment

Add at least one filter to your segment as depicted in the image below. You can combine as many filters as you want in order to make your segmentation more specific.

{% alert note %}
Braze doesn't generate profiles for users until they've used the app for the first time, so you can't target users who haven't opened your app yet.
{% endalert %}

!\[Segment Filters\]\[3\]

Choosing "OR" for your filters means that your segment will contain users satisfying any combination of one, some, or all of those filters, while "AND" means that users who do not pass that filter will not be included in your segment. This logic can be combined, so that you can segment users who pass one filter "AND" either one of two other filters.

Notice that the statistics on your segment are changing in real-time as you add and subtract filters. Keep in mind that these statistics are estimates (+/- 1%) and that the exact segment membership is always calculated before a segment is affected by a message sent in a campaign or Canvas.

{% alert important %}
Segments already using the Segment Membership Filter cannot be further included/nested into other segments.
{% endalert %}

### Single-user segments

You can create single user segments (or segments of a handful of users) using unique attributes that identify users, like a user name or a user ID.

However, the segmentation stats or preview may not show this individual user because segment stats are calculated based on a random sample with a 95% confidence interval that the result is within +/- 1%. The larger your user base is, the more likely it is that the size of your segment is a rough estimate. To ensure that your segment contains the single user you are targeting, click **Calculate Exact Statistics** on the **Segment Details** page. This will calculate the exact number of users in your segment, without any rounding.

Braze has testing filters to target specific users by user ID or email address.

## Step 5: Save your segment

Once you've clicked "Save" you're ready to start sending messages to your users!

## Segment membership calculation {#segment-membership-calculation}

Braze updates the user’s segment membership as data is sent back to our servers and processed, typically instantaneously. A user’s segment membership will not change until that session has been processed. For example, a user who falls into a lapsed user segment when the session first starts will be immediately moved out of the lapsed user segment when the session is processed.

Additionally, segment membership is calculated differently when **Include users from all apps** is selected, or when an app group has only one app. In these scenarios, segment membership includes all users—both those who have sessions logged, as well as users with no sessions and no app data (typically created via user import or REST API).

If **Include users from all apps** is cleared and you have more than one app in your app group, segment membership will only include users with sessions logged in the selected apps, and excludes users with no sessions or app data. Therefore the total of individual segments with one app selected will not equal a segment with **Include users from all apps** selected.

## Archiving segments

If you no longer need or wish to retire a specific segment, you can archive it by going to the __Segments__ page, clicking on the appropriate gear, then selecting "Archive" from the drop-down that appears.

{% alert warning %}
When you archive a segment, any campaigns or Canvases (even if the segment is only used in a single Canvas step) using it will __also be archived__. You will get a warning listing which Campaigns and Canvases are about to be archived by archiving the associated segment.
{% endalert %}

You can unarchive the segment by navigating to it within Segments, then selecting Unarchive from the top right corner of its page.
[1]: {% image_buster /assets/img_archive/Segment1.png %} [2]: {% image_buster /assets/img_archive/Segment2.png %} [3]: {% image_buster /assets/img_archive/segment_step4.png %} [5]: {% image_buster /assets/img_archive/segment_app_selection.png %}
