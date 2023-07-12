---
nav_title: Creating a Segment
article_title: Creating a Segment
page_order: 1
page_type: tutorial
description: "This how-to article will walk you through how to set up and create a segment using Braze."
tool: Segments
search_rank: 3
---

# [![Braze Learning course]({% image_buster /assets/img/bl_icon2.png %})](https://learning.braze.com/segmentation-course){: style="float:right;width:120px;border:0;" class="noimgborder"}Creating a segment

> Segmentation allows you to target users based upon their demographic, behavioral, or technical characteristics and actions. Creative and intelligent use of segmentation and messaging automation enables you to seamlessly move your users from first touch to long-term customer. Segments update in real-time as data changes, and you can create as many segments as needed for your targeting and messaging purposes.

## Step 1: Navigate to the segments section

Go to **Audience** > **Segments**.

{% alert note %}
If you are using the [older navigation]({{site.baseurl}}/navigation), you can find **Segments** under **Engagement**.
{% endalert %}

## Step 2: Name your segment

Click <i class="fas fa-plus"></i> **Create Segment** to begin building your segment. Name your segment by describing the type of user you intend to filter for. This will ensure that this segment can accurately be the target of multiple campaigns or Canvases to come. Vague segment titles can cause confusion down the line.

Optionally, you can add a description to the segment to provide more details about the intention of this audience and leave notes for other team members to refer back to.

![Create Segment modal where the segment is named "Lapsed Users" with the Segment Description as "This is our main Lapsed User segment to target non-actives within the past fourteen days." with two buttons: Cancel and Create Segment.][2]{: style="max-width:70%;"}

## Step 3: Choose your app or platform

Choose which apps or platforms you'd like to target by selecting **Users from all apps** (default), or **Users from specific apps**. If you choose **Users from all apps**, the segment includes all users regardless of any session or app data. If you choose **Users from specific apps**, you can then select which apps or platforms you want to include in your segment.

For example, if you'd like to send an in-app message to only iOS devices, select your iOS app. This will ensure that users who might use both an iOS and an Android device will only receive the message on their iOS device. In the list of specific apps, the option **Users from no apps** allows you to include users with no sessions and no app data (typically created via user import or REST API).

![Segment Details panel with the "Users from all apps" option selected in the Apps Used section.][5]

## Step 4: Add filters to your segment

Add at least one filter to your segment as depicted in the following image. You can combine as many filters as you want in order to make your segmentation more specific.

{% alert note %}
Braze doesn't generate profiles for users until they've used the app for the first time, so you can't target users who haven't opened your app yet.
{% endalert %}

![Segment filters with the "OR" selected.][3]

Choosing "OR" for your filters means that your segment will contain users satisfying any combination of one, some, or all of those filters, while "AND" means that users who do not pass that filter will not be included in your segment. This logic can be combined so that you can segment users who pass one filter "AND" either one of two other filters.

Notice that the statistics on your segment are changing in real-time as you add and subtract filters. Keep in mind that these statistics are estimates (+/- 1%) and that the exact segment membership is always calculated before a segment is affected by a message sent in a campaign or Canvas. Note that you will see an error appear if the segment you are referencing in one of your nested segments is archived.

{% alert important %}
Segments already using the Segment Membership Filter cannot be further included or nested into other segments.
{% endalert %}

### Testing segments

After adding apps and filters to your segment, you can test if your segment is set up as expected by [looking up a user]({{site.baseurl}}/user_guide/engagement_tools/segments/user_lookup/) to confirm if they match the segment criteria.

![]({% image_buster /assets/img_archive/user_lookup.png %})

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

![A table displaying 9,100 total reachable users, 8,899 reachable users by email, 6,720 reachable users by web push, 4,521 reachable users by Android push, and 5,122 reachable users by iOS push.][4]

For a user to be listed as reachable through a certain channel, the user must have both:
* A valid email address/push token associated with their profile; and
* Opted in or subscribed to your app.

A single user may belong to different reachable user groups. For example, a user might have both a valid email address and valid Android push token and be opted in to both, but have no associated iOS push token. The gap between the total reachable users and the sum of the different channels are the number of users who qualified for the segment but they are not reachable via those communication channels.

#### Calculating exact statistics
The larger your user base is, the more likely the **Reachable Users** amount is a rough estimate. This allows us to quickly provide you estimates in real-time as you add filters, rather than searching your entire user base every time.

To calculate the exact amount of reachable users, click **Calculate Exact Statistics**. For large segments, it is normal to see slight variation even when calculating exact statistics. The accuracy of this feature is expected to be 99.999% or greater.

## Archiving segments

If you no longer need or wish to retire a specific segment, you can archive it by going to the **Segments** page, clicking on the gear, then selecting **Archive** from the dropdown.

{% alert warning %}
When you archive a segment, any campaigns or Canvases using it (even if the segment is only used in a single Canvas component) will also be archived. This also includes nested segments where both segments and any campaigns or Canvases using them will also be archived.
<br><br>
You will get a warning listing which campaigns and Canvases are about to be archived by archiving the associated segment.
{% endalert %}

You can unarchive the segment by navigating to it within the **Segments** page, then selecting **Unarchive**.

[1]: {% image_buster /assets/img_archive/Segment1.png %}
[2]: {% image_buster /assets/img_archive/Segment2.png %}
[3]: {% image_buster /assets/img_archive/segment_step4.png %}
[4]: {% image_buster /assets/img_archive/reachable_users.png %}
[5]: {% image_buster /assets/img_archive/segment_app_selection.png %}
