---
nav_title: Race conditions
article_title: Race Conditions
alias: /race_conditions/
page_order: 9
page_type: reference
description: "This article covers best practices to avoid race conditions from affecting your messaging campaigns."
toc_headers: h2
---

# Race conditions

> A race condition occurs when an outcome depends on the sequence or timing of multiple events. For example, if the desired sequence of events is “Event A” then “Event B”, but sometimes “Event A” comes first, and other times “Event B” comes first—that is known as a race condition. This can lead to unexpected results or errors because these events compete to access shared resources or data.

{% multi_lang_include video.html id="LyJaxDoMtMs" align="right" %}

In Braze, race conditions can occur when multiple actions are triggered at the same time based on user data or events. For example, if a user triggers multiple campaigns (like signing up for a newsletter or making a purchase), they may not receive the messages in the correct order.

## Types of race conditions

The most common types of race conditions may occur when you’re doing the following:

- Targeting new users
- Using multiple API endpoints
- Matching action-based trigger and audience filters. 

Consider the following scenarios and implement best practices to avoid these race conditions.

## Scenario 1: Targeting new users

In Braze, one of the most common race conditions occurs with messages that target newly created users. The expected order of events is:

1. A user gets created;
2. The same user is immediately targeted for a message, performs a custom event, or logs a custom attribute.

However, in some cases, the second event triggers first. This means a message is attempting to be sent to a user that doesn’t exist yet. As a result, the user never receives it. This also applies to events or attributes, where the event or attribute attempts to be logged to a user profile that hasn’t been created yet.

### Best practices

#### Introduce delays

After a new user is created, you can add a delay before sending any targeted campaigns or Canvases. This timing delay allows the user profile to be created and for any relevant attributes to be updated that may determine their eligibility for receiving the message.

For example, after a user registers for your app, you can send a promotional offer after 24 hours. Or, if you're creating a user or logging a custom attribute, you can add a one-minute delay before proceeding in your process to avoid this race condition.

You can also add this delay in the [Braze SDK]({{site.baseurl}}/developer_guide/sdk_integration) for the specific custom event that triggers a new user to enter a Canvas. 

## Scenario 2: Using multiple API endpoints

{% alert important %}
We use asynchronous processing to maximize speed and flexibility. This means that when API calls are sent to us separately, we cannot guarantee that they are processed in the order they were sent.
{% endalert %}

There are a few scenarios where multiple API endpoints can also result in this race condition, such as when:

- Using separate API endpoints to create users and trigger Canvases or campaigns
- Making multiple separate calls to the `/users/track` endpoint to update custom attributes, events, or purchases

When user information is sent to Braze using the [`/users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track), it may occasionally take a few seconds to process. This means when requests are simultaneously made to the `/users/track` and Messaging endpoints like `/campaign/trigger/send`, there’s no guarantee that the user information is updated before a message is sent.

{% alert note %}
If user attributes and events are sent in the same request (either from `/users/track` or from the SDK), then Braze processes attributes before events or attempting to send any message.
{% endalert %}

### Best practices

#### When using multiple endpoints, send your requests one at a time

If you’re using multiple endpoints, you can try staggering your requests so that each request is completed before the next one starts. This can reduce the chance of a race condition. For example, if you need to update user attributes and send a message, first wait for the user profile to be updated completely before sending a message using an endpoint.

If you're sending a scheduled message API request, these requests must be separate, and a user must be created before sending the scheduled API request.

#### Include key data with the trigger

Instead of using multiple endpoints, you can include the [user attributes]({{site.baseurl}}/api/objects_filters/user_attributes_object#object-body) and [trigger properties]({{site.baseurl}}/api/objects_filters/trigger_properties_object) in a single API call using the [`campaign/trigger/send` endpoint]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns). 

When these objects are included with the trigger, the attributes are processed first, before the message is triggered, eliminating potential race conditions. Note that trigger properties don't update the user profile, but are used in the context of the message only.

#### Use the POST: Track users (sync) endpoint

Use the [`/users/track/sync/` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track_synchronous) to record custom events and purchases and update user profile attributes synchronously. Using this endpoint to update user profiles at the same time and in a single call can help prevent potential race conditions.

{% alert important %}
This endpoint is currently in beta. Contact your Braze account manager if you’re interested in participating in the beta.
{% endalert %}

## Scenario 3: Matching action-based triggers and audience filters

Another common race condition may occur if you configure an action-based campaign or Canvas with the same trigger as the audience filter (such as a changed attribute or performed a custom event). The user may not be in the audience at the time they perform the trigger event, which means they won’t receive the campaign or enter the Canvas.

### Best practices

#### Check your audience after a delay

To avoid using audience filters that contain the trigger criteria, we recommend checking your audience before delivery. For example, you can [use delivery validations]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/#edit-delivery-settings) in Canvas Message steps as an additional check to confirm your audience meets the delivery criteria at message send. You can also leverage exit criteria for Canvas to exit any users at any point during the user journey if they meet your criteria.

For campaigns, you can use exit events to allow campaigns with a trigger event to abort messages to users who perform the exit event while in the delay.

#### Use unique filters with the trigger event

As you configure your filters, you may want to add a redundant filter “just in case”. However, this redundancy may lead to more issues. Instead, avoid using any filter that contains the trigger when possible. This is the safest route to avoid a race condition.

For example, if your campaign trigger is “Has made a purchase” and your audience filter is “Has made any purchase”, this redundancy can cause a race condition. 

#### Avoid audience filters that assume the trigger event has been updated

This best practice is similar to avoiding redundant filters with the trigger event. Usually, a filter that assumes the trigger event is updated to the user profile fails.

#### Use Liquid aborts (attributes only)

In campaigns and Canvas steps, use Liquid aborts to avoid using audience filters that contain the trigger attributes at the entry schedule. For example, let’s say you have an array attribute “favorite colors” and want to target any user who updates the attribute array with any value, and also has the color “blue” in the array after the update has completed. If you use the audience filters in this example, you’ll encounter a race condition and miss users adding “blue” in the array for the first time.

In this case, you can implement a trigger delay in a campaign or use a Delay step in Canvas to allow the user profile to update for a period of time, then use the following Liquid abort logic:

{% raw %}
```liquid
{%assign colors={{custom_attribute.$(Favorite Color)|split:”,”}}%}
{%unless colors contains ‘Blue’%}
{%abort_message(Blue not present)%}
{%endunless%}
```
{% endraw %}

#### Confirm how user data is being managed

If there is a race condition during the Canvas entry evaluation, users may enter a Canvas that they weren't meant to enter. For example, the user's profile could be set to be included in the audience and subsequently updated after the Canvas has enqueued the users to no longer be eligible in the audience. 

If a user triggers the Canvas entry event multiple times within the same second, Braze allows only one entry for that second (even if re-entry is enabled). This prevents duplicate entries, so the total number of Canvas entries may be lower than the total trigger events.

We recommend confirming how user data is managed and updated, specifically when and how specific attributes are updated, such as by SDK, API, batch API, and other methods. This can help identify and clarify why a user has entered a campaign or Canvas versus when a user's profile was updated.
