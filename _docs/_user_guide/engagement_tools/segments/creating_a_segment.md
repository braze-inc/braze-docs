---
nav_title: Creating a Segment
article_title: Creating a Segment
page_order: 1
page_type: tutorial
description: "This how-to article will walk you through how to set up and create a segment using Braze."
tool: Segments
search_rank: 3
---

# [![Braze Learning course]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/segmentation-course){: style="float:right;width:120px;border:0;" class="noimgborder"}Creating a segment

> Segmentation allows you to target users based upon their demographic, behavioral, or technical characteristics and actions. Creative and intelligent use of segmentation and messaging automation enables you to seamlessly move your users from first touch to long-term customer. Segments update in real-time as data changes, and you can create as many segments as needed for your targeting and messaging purposes.

## Step 1: Navigate to the segments section

Go to **Audience** > **Segments**.

## Step 2: Name your segment

Select **Create Segment** to begin building your segment. Name your segment by describing the type of user you intend to filter for. This will help you identify the segment when you want to target it for your campaigns or Canvases. Vague segment titles can be confusing.

Optionally, you can do the following:
- Add a description to the segment to provide more details about the intention of this audience and leave notes for other team members to refer back to.
- Add a [team]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) to your segment.
- Add [tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) to your segment for further organization.

![Create Segment modal where the segment is named "Lapsed Users" with the Segment Description as "This is our main Lapsed User segment to target non-actives within the past fourteen days." with two buttons: Cancel and Create Segment.][2]{: style="max-width:70%;"}

## Step 3: Choose your app or platform

Choose which apps or platforms you'd like to target by selecting **Users from all apps** (default), or **Users from specific apps**. If you choose **Users from all apps**, the segment includes all users regardless of any session or app data. If you choose **Users from specific apps**, you can then select which apps or platforms you want to include in your segment.

For example, if you'd like to send an in-app message to only iOS devices, select your iOS app. This will ensure that users who might use both an iOS and an Android device will only receive the message on their iOS device. In the list of specific apps, the option **Users from no apps** allows you to include users with no sessions and no app data (typically created via user import or REST API).

![Segment Details panel with the "Users from all apps" option selected in the Apps Used section.][5]{: style="max-width:70%;"}

## Step 4: Add filters to your segment

Add at least one filter to your segment. You can combine as many filters as you want to make your segmentation more specific.

{% alert note %}
Braze doesn't generate profiles for users until they've used the app for the first time, so you can't target users who haven't opened your app yet.
{% endalert %}

#### Filter groups

Filters are organized into filter groups. Every filter must be part of a filter group that has a minimum of one filter. A segment can have multiple filter groups. To add one, select **Add filter group**. Edit the filter group name by selecting the icon that appears when you hover next to it.

![Filter group with an editing icon next to its name.][14]{: style="max-width:70%;"}

Select the icons next to each filter to collapse the filter editor, duplicate the filter, or remove the filter. After duplicating a filter, you can adjust its values within each dropdown.

You can also use the icon within each filter group to duplicate that filter group and the filters within it, or delete that filter group from your segment.

#### Segmentation logic using AND and OR

Within a filter group, filters can be joined by either "AND" or "OR". Between filter groups, groups can be joined by either "AND" or "OR". When using filter groups, you can create segmentation logic such as:
- (A AND B AND C) OR (C AND E AND F)
- (A OR B OR C) AND (C OR D OR F)

Selecting "OR" for your filters means that your segment will contain users satisfying any combination of one, some, or all of those filters. Selecting "AND" means that users who do not pass that filter will not be included in your segment.

{% alert tip %}
When selecting "OR" for filters that include a negative filter (such as "is not" in a subscription group), remember that users only need to fulfill one of the "OR" filters to be included in the segment. To apply the negative filter regardless of the other filters, use an [exclusion group](#exclusion).
{% endalert %}

#### Filter operators

Depending on the specific filter you select, you will have different operators for identifying filter values. To dive deeper into the operators available for different types of custom attributes, see [Custom attribute storage]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#setting-custom-attributes). Note that when using the “is any of” operator, the maximum number of items you can include in that field is 256.

{% alert note %}
Braze doesn't generate profiles for users until they've used the app for the first time, so you can't target users who haven't opened your app yet.
{% endalert %}

![Segmenter filter groups with the AND operator.][9]{: style="max-width:70%;"}

{% alert important %}
Segments already using the **Segment Membership** filter cannot be further included or nested into other segments. This prevents a cycle where Segment A includes Segment B, which then tries to include Segment A again. If that happened, the segment would keep referencing itself, making it impossible to calculate who actually belongs in it.

Also, nesting segments like this adds complexity and can slow things down. Instead, recreate the segment you're trying to include using the same filters.
{% endalert %}

#### Exclusion groups (optional) {#exclusion}

When building a segment, you can apply one or multiple exclusion groups. Exclusion groups contain criteria that identify users to exclude from your segment, and will always be connected to your filter groups with an "AND NOT" operator.

Exclusion groups override segment criteria. If a user falls into your exclusion group criteria, they will not be part of your segment, even if they meet the criteria within your filter groups.

Create an exclusion group by adding filters like you would for filter groups. The _Estimated Reachable Users_ statistic in an exclusion group shows the estimated number of users remaining in your segment after the exclusion criteria is applied.

Excluded users will not be counted as part of your segment’s _Total reachable users_ statistic.

![An exclusion group with two filters.][12]{: style="max-width:70%;"}

#### Testing segments

After adding apps and filters to your segment, you can test if your segment is set up as expected by looking up a user to confirm if they match the segment criteria. To do so, search for a user’s `external_id` or `braze_id` in the **User Lookup** section.

![User Lookup section with a search field.][6]{: style="max-width:80%;"}

User lookup is available when:
- Creating a segment
- Setting up a campaign or Canvas audience
- Setting up an Audience Paths step

When a user matches the segment, filter, and app criteria, an alert will state so.

![A user lookup of "user007" triggers an alert stating, "user007 matches all of the segments, filters, and apps.][7]{: style=" max-width:80%;"}

When a user doesn’t match part or all of the segment, filter, or app criteria, the missing criteria is listed for troubleshooting purposes.

![A user lookup of "user1234" triggers an alert stating, "user1234 does not match the following targeting criteria:" and displays two missing criteria: a tenure greater than one year and today being an anniversary.][8]{: style=" max-width:80%;"}

#### Single-user segments

You can create single user segments (or segments of a handful of users) using unique attributes that identify users, like a user name or a user ID.

However, the segmentation stats or preview may not show this individual user because segment stats are calculated based on a random sample with a 95% confidence interval that the result is within +/- 1%. The larger your user base is, the more likely it is that the size of your segment is a rough estimate. To make sure that your segment contains the single user you are targeting, select **Calculate exact statistics**. This will calculate the exact number of users in your segment with greater than 99.999% accuracy.

Braze has testing filters to target specific users by user ID or email address.

## Step 5: Save your segment

Select **Save**. Now you're ready to start sending messages to your users!

## Measuring segment size

To learn about monitoring your segment’s membership and size, refer to [Measuring segment size]({{site.baseurl}}/user_guide/engagement_tools/segments/measuring_segment_size/).

## Archiving segments

If you no longer need or wish to retire a specific segment, you can archive it by going to the **Segments** page and selecting **Archive** from the menu in that segment's row.

{% alert warning %}
When you archive a segment, any campaigns or Canvases using it (even if the segment is only used in a single Canvas component) will also be archived. This also includes nested segments where both segments and any campaigns or Canvases using them will also be archived.
<br><br>
You will get a warning listing which campaigns and Canvases are about to be archived by archiving the associated segment.
{% endalert %}

You can unarchive the segment by navigating to it within the **Segments** page, then selecting **Unarchive**.

## Targeting behavior when users have multiple devices

Users have more than one device if they log into the same account on multiple devices. You can check for multiple devices in the **Recent Devices** section of a [user profile]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/).

When segmenting with device-dependent filters (device model, device OS, and app version), your segment will contain all users that match your filter criteria. These users will be sent a message on all their devices, including ones that may not meet your filter criteria. For example, let's say User A has two devices: Device 1 is OS 13.0, and Device 2 is OS 10.0. If a segment targets users with OS 10.0, this user will be part of that segment and receive messages on both of their devices.

### Push notifications

You can specify that only one push notification is sent to each user. When [composing your message]({{ssite.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message#step-4-compose-your-push-message), select **Only send to the user’s last used device** under **Additional Settings**.

![][13]{: style="max-width:60%;"}

### Considerations

- **Messages sent can exceed audience size.** When some users have more than one device, each device can receive a message. This causes a higher number of message sends than users in your segment.
- **A user's segment membership might not look how you'd expect.**
    - A user may be targeted on their current device based on attributes associated with a different device. If you didn't expect a user to receive a message, check their user profile for multiple devices.
    - A user may have been in your target segment at send time, but due to behaviors associated with any of their devices, may not be part of that segment afterward. This may result in a user receiving a campaign or Canvas even though they currently don’t match the filter criteria. <br><br>For example, a user could receive a message targeting users with a most recent app version of OS 10.0 even though they currently have OS 13.0. In this case, the user had OS 10.0 when the message was sent and then upgraded to OS 13.0 afterward.<br><br> Similarly, if a user later uses a device with a different app version, their user profile will update with a new most recent app version. This might make it seem that the user shouldn't have qualified for the message, even though they qualified when it was sent.


[1]: {% image_buster /assets/img_archive/Segment1.png %}
[2]: {% image_buster /assets/img_archive/Segment2.png %}
[3]: {% image_buster /assets/img_archive/segment_step4.png %}
[5]: {% image_buster /assets/img_archive/segment_app_selection.png %}
[6]: {% image_buster /assets/img_archive/user_lookup.png %}
[7]: {% image_buster /assets/img_archive/user_lookup_match.png %}
[8]: {% image_buster /assets/img_archive/user_lookup_nomatch.png %}
[9]: {% image_buster /assets/img_archive/segmenter_filter_groups.png %}
[11]: {% image_buster /assets/img_archive/segmenter_and_or.png %}
[12]: {% image_buster /assets/img_archive/segmenter_exclusion_groups.png %}
[13]: {% image_buster /assets/img_archive/send_to_last_device.png %}
[14]: {% image_buster /assets/img_archive/edit_filter_group_name.png %}