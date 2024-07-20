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

{% alert note %}
If you are using the [older navigation]({{site.baseurl}}/navigation), you can find **Segments** under **Engagement**.
{% endalert %}

## Step 2: Name your segment

Click <i class="fas fa-plus"></i> **Create Segment** to begin building your segment. Name your segment by describing the type of user you intend to filter for. This will ensure that this segment can accurately be the target of multiple campaigns or Canvases to come. Vague segment titles can cause confusion down the line.

Optionally, you can add a description to the segment to provide more details about the intention of this audience and leave notes for other team members to refer back to.

![Create Segment modal where the segment is named "Lapsed Users" with the Segment Description as "This is our main Lapsed User segment to target non-actives within the past fourteen days." with two buttons: Cancel and Create Segment.]({% image_buster /assets/img_archive/Segment2.png %}){: style="max-width:70%;"}

## Step 3: Choose your app or platform

Choose which apps or platforms you'd like to target by selecting **Users from all apps** (default), or **Users from specific apps**. If you choose **Users from all apps**, the segment includes all users regardless of any session or app data. If you choose **Users from specific apps**, you can then select which apps or platforms you want to include in your segment.

For example, if you'd like to send an in-app message to only iOS devices, select your iOS app. This will ensure that users who might use both an iOS and an Android device will only receive the message on their iOS device. In the list of specific apps, the option **Users from no apps** allows you to include users with no sessions and no app data (typically created via user import or REST API).

![Segment Details panel with the "Users from all apps" option selected in the Apps Used section.]({% image_buster /assets/img_archive/segment_app_selection.png %})

## Step 4: Add filters to your segment

Add at least one filter to your segment as depicted in the following image. You can combine as many filters as you want in order to make your segmentation more specific.

{% alert note %}
Braze doesn't generate profiles for users until they've used the app for the first time, so you can't target users who haven't opened your app yet.
{% endalert %}

![Segment filters with the "OR" selected.]({% image_buster /assets/img_archive/segment_step4.png %})

Choosing "OR" for your filters means that your segment will contain users satisfying any combination of one, some, or all of those filters, while "AND" means that users who do not pass that filter will not be included in your segment. This logic can be combined so that you can segment users who pass one filter "AND" either one of two other filters.

Notice that the statistics on your segment are changing in real-time as you add and subtract filters. Keep in mind that these statistics are estimates (+/- 1%) and that the exact segment membership is always calculated before a segment is affected by a message sent in a campaign or Canvas. Note that you will see an error appear if the segment you are referencing in one of your nested segments is archived.

{% alert important %}
Segments already using the Segment Membership Filter cannot be further included or nested into other segments.
{% endalert %}

### Testing segments

After adding apps and filters to your segment, you can test if your segment is set up as expected by looking up a user to confirm if they match the segment criteria. To do so, click **Lookup User** and search for a user’s `external_id` or `braze_id`.

![User Lookup section with a "Lookup User" button.]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:50%;"}

User lookup is available when:
- Creating a segment
- Setting up a campaign or Canvas audience
- Setting up an Audience Paths step

When a user matches the segment, filter, and app criteria, you see the following:

![A user lookup of "user007" triggers an alert stating, "user007 matches all of the segments, filters, and apps.]({% image_buster /assets/img_archive/user_lookup_match.png %}){: style=" max-width:60%;"}

When a user doesn’t match part or all of the segment, filter, or app criteria, the missing criteria is listed for troubleshooting purposes.

![A user lookup of "user1234" triggers an alert stating, "user1234 does not match the following targeting criteria:" and displays two missing criteria: a tenure greater than one year and today being an anniversary.]({% image_buster /assets/img_archive/user_lookup_nomatch.png %}){: style=" max-width:60%;"}

### Single-user segments

You can create single user segments (or segments of a handful of users) using unique attributes that identify users, like a user name or a user ID.

However, the segmentation stats or preview may not show this individual user because segment stats are calculated based on a random sample with a 95% confidence interval that the result is within +/- 1%. The larger your user base is, the more likely it is that the size of your segment is a rough estimate. To ensure that your segment contains the single user you are targeting, click **Calculate Exact Statistics** on the **Segment Details** page. This will calculate the exact number of users in your segment with greater than 99.999% accuracy.

Braze has testing filters to target specific users by user ID or email address.

## Step 5: Save your segment

Once you've clicked **Save**, you're ready to start sending messages to your users!

## Segment membership calculation {#segment-membership-calculation}

Braze updates the user's segment membership as data is sent back to our servers and processed, typically instantaneously. A user's segment membership will not change until that session has been processed. For example, a user who falls into a lapsed user segment when the session first starts will be immediately moved out of the lapsed user segment when the session is processed.

### Total reachable users calculation

Each segment displays the total number of users that are members of that segment. When filtering for **Users from all apps**, it also displays all of the different channels available to communicate with those users, such as web push or email. It is possible that the number of total users is different than the number of users reachable by each channel. Why is this?

![A table displaying 9,100 total reachable users, 8,899 reachable users by email, 6,720 reachable users by web push, 4,521 reachable users by Android push, and 5,122 reachable users by iOS push.]({% image_buster /assets/img_archive/reachable_users.png %})

For a user to be listed as reachable through a certain channel, the user must have both:
* A valid email address/push token associated with their profile; and
* Opted in or subscribed to your app.

A single user may belong to different reachable user groups. For example, a user might have both a valid email address and valid Android push token and be opted in to both, but have no associated iOS push token. The gap between the total reachable users and the sum of the different channels are the number of users who qualified for the segment but they are not reachable via those communication channels.

#### Calculating exact statistics

The larger your user base is, the more likely the **Reachable Users** amount is a rough estimate. This allows us to provide you estimates in real-time as you add filters, rather than taking longer to search your entire user base every time.

To calculate the exact amount of reachable users, click **Calculate Exact Statistics**. For large segments, it is normal to see slight variation even when calculating exact statistics. The accuracy of this feature is expected to be 99.999% or greater.

## Archiving segments

If you no longer need or wish to retire a specific segment, you can archive it by going to the **Segments** page, clicking on the gear, then selecting **Archive** from the dropdown.

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

![]({% image_buster /assets/img_archive/send_to_last_device.png %}){: style="max-width:60%;"}

### Considerations

- **Messages sent can exceed audience size.** When some users have more than one device, each device can receive a message. This causes a higher number of message sends than users in your segment.
- **A user's segment membership might not look how you'd expect.**
    - A user may be targeted on their current device based on attributes associated with a different device. If you didn't expect a user to receive a message, check their user profile for multiple devices.
    - A user may have been in your target segment at send time, but due to behaviors associated with any of their devices, may not be part of that segment afterward. This may result in a user receiving a campaign or Canvas even though they currently don’t match the filter criteria. <br><br>For example, a user could receive a message targeting users with a most recent app version of OS 10.0 even though they currently have OS 13.0. In this case, the user had OS 10.0 when the message was sent and then upgraded to OS 13.0 afterward.<br><br> Similarly, if a user later uses a device with a different app version, their user profile will update with a new most recent app version. This might make it seem that the user shouldn't have qualified for the message, even though they qualified when it was sent.

