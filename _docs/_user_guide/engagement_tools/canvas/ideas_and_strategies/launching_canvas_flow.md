---
nav_title: Launching with Canvas Flow
article_title: Launching with Canvas Flow
page_order: 3
description: "This reference article covers how to prepare and test a Canvas built with Canvas Flow before launch."
page_type: reference
tool: Canvas
---

# Launching with Canvas Flow

> This reference article covers how to prepare and test a Canvas built using Canvas Flow before launch. This includes identifying important Canvas checkpoints such as Canvas entry conditions, audience summaries, and user segments.

As you prepare to launch your Canvas, Braze recommends that you check your Canvas at each stage of the Canvas builder, including:
* [Race conditions](#race-conditions)
* [Delivery times](#delivery-times)
* [User segments](#segment-users)

## Race conditions 

Consider the [race conditions]({{site.baseurl}}/user_guide/engagement_tools/testing/race_conditions/) that may be occur before launching your Canvas. 

To enter your Canvas, users must be in the **Entry Audience** before the entry schedule occurs (whether that be scheduled at a specific time, or triggered by action-based or API-triggered event). Note that users who qualify for your entry audience after will not enter for Canvases that are action-based, API-triggered, or one-time-send Canvases.

### Review entry audience filters

In general, avoid configuring an action-based or API-triggered Canvas with the same trigger as the audience filter. For example, after a Canvas is launched, users who perform a specific action will be included in the Entry Audience, so there's no need to add the event as an audience filter. 

### Batch multiple API requests

Make your requests in the same API call, rather than multiple calls, to confirm that the user profile is created or updated first. Check out [Using multiple endpoints]({{site.baseurl}}/user_guide/engagement_tools/testing/race_conditions/#using-multiple-api-endpoints) for more examples.

### Add a delay

Another option to avoid race conditions is to use the Delay step (ideally set for 5 minutes) as the first step of your Canvas. This allows time for attributes, email addresses, and push tokenbs to be processed to new user profiles before they're targeted for the following Canvas steps. Without this Delay step, it's possible for an email to be sent to a user whose email hasn't updated yet.

## Delivery times

By setting a Canvas delivery time in real time, this can lead to increasing engagement and conversion rates. Take note of which delivery time you've set for your Canvas. To increase engagement and conversion rates, it's best to have Canvases trigger in real time as opposed to a scheduled, recurring basis.

## Segment users

Before oversaturating your Canvas Flow user journey with components, consider how you might keep a user journey simple. Use the simplified view in the Canvas editor to get a better idea of how your user journey branches. 

There are four main components you can use to segment your users in a simple, effective manner:

* Audience Paths
* Decision Split
* Action Paths
* Experiement Paths

Use the Action Paths step to segment users within the Canvas based on custom attributes, custom events, and previous message engagement data from user profiles.

The Decision Split step creates a point in your user journey where you can evaluate your users with a polar question to determine which path to send the user to, depending on their answer.

Actions Paths focus on segmenting users based on real-time behaviors such as custom events, purcahse events, and custom attribute changes.

Similar to Action Paths, you can leverage Experiment Paths steps in your Canvas to test multiple Canvas paths against each other, along with a control group. This tracks path performance, allowing you to make informed decisions when building your Canvas journey. 

## Testing before launch

Check out [Sending test Canvases]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/sending_test_canvases/) for different methods you can leverage to test your Canvas.

## Troubleshooting

{% details Why are my users not receiving my Canvas messages? %}
- Check that their push subscription state is "subscribed" or "opted-in" **and** that their **Push Enabled** status is set to "true". If you added these as Canvas entry rules, it's possible that the users were unsubscribed between entering your Canvas and receiving the Message step.
- If global frequency capping is enabled for your Canvas, depending on your specific rules, this can limit how many times each user should receive a message from a specific channel. 
- If Quiet Hours are enabled, this can impact your message send time, meaning that your message may send a the next available time (when the Quiet Hours end) or cancel the message entirely.
{% enddetails %}
