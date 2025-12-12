---
nav_title: Launching with Canvas flow
article_title: Launching with Canvas Flow
page_order: 3
description: "This reference article covers how to prepare and test a Canvas built with Canvas Flow before launch."
page_type: reference
tool: Canvas
---

# Launching with Canvas Flow

> This reference article covers how to prepare and test a Canvas built using Canvas Flow before launch. This includes identifying important Canvas checkpoints such as Canvas entry conditions, audience summaries, and user segments.

As you prepare to launch your Canvas, Braze recommends that you check your Canvas at each stage of the Canvas builder for settings that can impact your message sending, including:
* [Race conditions](#race-conditions)
* [Delivery times](#delivery-times)
* [User segments](#segment-users)

## Race conditions 

Consider the [race conditions]({{site.baseurl}}/user_guide/engagement_tools/testing/race_conditions/) that may be occur before launching your Canvas. 

To enter a Canvas, users must be in the entry audience before the entry schedule occurs regardless of whether the Canvas is scheduled, action-based, or API-triggered. 

![An Action-Based Canvas that enters users when they make any purchase during a user's local time from April 30, 2025 at 12 pm to May 7, 2025 at 12 pm.]({% image_buster /assets/img_archive/launch_with_canvas_flow_example.png %}){: style="max-width:75%;"}

Note that users who qualify for your entry audience after the Canvas launches will not enter the Canvas.

{% alert tip %}
Check out [Entry schedule types]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-2b-set-your-canvas-entry-schedule) for guidance and details for when to use scheduled, action-based, or API-triggered delivery for your Canvas!
{% endalert %}

### Review entry audience filters

In general, avoid configuring an action-based or API-triggered Canvas with the same trigger as the audience filter. For example, after a Canvas is launched, users who perform a specific action will be included in the entry audience, so there's no need to add the event as an audience filter. 

For more details on available segmentation filters to target your audience, see [Segmentation Filters]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters).

### Batch multiple API requests

Make your requests in the same API call, rather than multiple calls, to confirm that the user profile is created or updated first. Refer to [Using multiple endpoints]({{site.baseurl}}/user_guide/engagement_tools/testing/race_conditions/#using-multiple-api-endpoints) for more examples.

### Add a delay

Another option to avoid race conditions is to use the Delay step (ideally set for 5 minutes) as the first step of your Canvas. 

This allows time for attributes, email addresses, and push tokens to be processed to new user profiles before they're targeted for the following Canvas steps. Without this Delay step, it's possible for an email to be sent to a user whose email hasn't been updated yet.

## Delivery times

Setting a Canvas delivery time in real-time can lead to increasing engagement and conversion rates. Take note of which delivery time you've set for your Canvas. To help increase engagement and conversion rates, it's best to trigger Canvases in real-time instead of on a scheduled, recurring basis.

If you selected a scheduled delivery for your Canvas, Braze recommends scheduling your Canvas at least 24 hours before you want it to launch to allow for any adjustments to your Canvas.

## User segments

Before oversaturating your Canvas Flow user journey with components, consider how you might keep a user journey simple. Use the simplified view in the Canvas editor to get a better idea of how your user journey branches. 

There are four main components you can use to segment your users in a simple, effective manner:

* [Audience Paths](#audience-paths)
* [Decision Split](#decision-split)
* [Action Paths](#action-paths)
* [Experiment Paths](#experiment-paths)

### Audience Paths

Use [Audience Paths]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths/) steps to segment users within the Canvas based on custom attributes, custom events, and previous message engagement data from user profiles.

### Decision Split

The [Decision Split]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split/) step allows you to send your users to different user journey paths based on their answers to a polar question.

### Action Paths

[Action Paths]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) focus on segmenting users based on real-time behaviors such as custom events, purchase events, and custom attribute changes. 

### Experiment Paths

Similar to Action Paths, you can leverage [Experiment Paths]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/) steps in your Canvas to test multiple Canvas paths against each other, along with a control group. This tracks path performance, allowing you to make informed decisions when building your Canvas journey. 

## Testing before launch

After reviewing the finer details of your Canvas, check out [Sending test Canvases]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/sending_test_canvases/) for different methods you can leverage to test your Canvas with test users.

## Launch checklist

### Check user availability

- Make sure your users meet your segmentation criteria.
- Confirm their subscription state is “subscribed” or “opted-in” and their Push token exists. If you added these as Canvas entry rules, it’s possible that the users were unsubscribed between entering your Canvas and receiving the Message step.
- Confirm they match your Canvas send settings. (If users are “subscribed” but the settings are “Opted-in”, users won’t be enabled for the channel.)
- If global frequency capping is enabled for your Canvas, check if your rules are limiting how many times each user can receive a message from a specific channel.
- If Quiet Hours are enabled, your message send time could be affected, meaning that your message may be sent at the next available time (when the Quiet Hours end) or cancelled entirely.
- Check user availability for additional filters in your Canvas step.

### Confirm that they performed the prerequisite custom event or purchase

- Check if there’s a race condition, which impacts the messages users receive if they trigger multiple actions at the same time.
- Make sure there aren’t specific filters in the step that could have blocked users from receiving the message.
- Search for conflicts between different steps within the same Canvas. For example, users who didn’t receive the message might be stopped by a filter that requires the completion of another step on a different branch.
- Confirm that users meet additional validation rules.
- Confirm that the Canvas step was connected to the preceding step at the time of send.

### Confirm your Canvas saves correctly and all steps are valid

If your Canvas isn't loading and won't progress, this can be caused when a previous version of the Canvas wasn't saved properly and contains invalid steps. You can duplicate the Canvas from the dashboard. If the issue persists, open a [support ticket]({{site.baseurl}}/braze_support/).

## Troubleshooting

{% details Why are my users not receiving my Canvas messages? %}
**Check user availability**
- Make sure they meet your segmentation criteria.
- Confirm their push subscription state is "subscribed" or "opted-in" **and** their **Push Enabled** status is set to "true". If you added these as Canvas entry rules, it's possible that the users were unsubscribed between entering your Canvas and receiving the Message step.
- Confirm they match your Canvas send settings. (If users are "subscribed" but the settings are "Opted-in", users won't be enabled for the channel.)
- If global frequency capping is enabled for your Canvas, check if your rules are limiting how many times each user can receive a message from a specific channel. 
- If Quiet Hours are enabled, your message send time could be affected, meaning that your message may be sent at the next available time (when the Quiet Hours end) or cancelled entirely.

**Check user availability for additional filters in your Canvas step**
- Confirm that they performed the prerequisite custom event or purchase.
- Check if there's a [race condition]({{site.baseurl}}/user_guide/engagement_tools/testing/race_conditions/), which impacts the messages users receive if they trigger multiple actions at the same time.
- Make sure there aren't specific filters in the step that could have blocked users from receiving the message.
- Search for conflicts between different steps within the same Canvas. For example, users who didn't receive the message might be stopped by a filter that requires the completion of another step on a different branch.
- Confirm that users meet additional validation rules.
- Confirm that the Canvas step was connected to the preceding step at the time of send.
{% enddetails %}

