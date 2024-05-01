---
nav_title: Race Conditions
article_title: Race Conditions
alias: /race_conditions/
page_order: 9
page_type: reference
description: "This article covers best practices to avoid race conditions from affecting your messaging campaigns."

---

# Race conditions

> A race condition is a concept where an outcome is dependent on the sequence or timing of other events. 

For example, if the desired sequence of events is "Event A" and then "Event B", but sometimes "Event A" comes first and other times "Event B" comes first—that is known as a race condition.

{% multi_lang_include video.html id="LyJaxDoMtMs" align="right" %}

## Targeting new users

In Braze, one of the most common race conditions occurs with messages that target newly created users. Here, the expected order of events is:

1. A user gets created;
2. The same user is immediately targeted for a message, performs a custom event, or logs a custom attribute.

However, in some cases, the second event will trigger first. This means that a message is attempting to be sent to a user that has not been created yet, and as a result, the user never receives it. The same applies for events or attributes, where the event or attribute is attempting to be logged to a user profile that doesn't exist yet.

## Using multiple API endpoints

There are a few scenarios where multiple API endpoints can also result in this race condition, such as when:

- Using separate API endpoints to create users and trigger Canvases or campaigns
- Making multiple separate calls to the `/users/track` endpoint to update custom attributes, events, or purchases

When user information is sent to Braze via the `/users/track` endpoint, it may occasionally take a few seconds to process. As a result, when requests are made to the `/users/track` and [Messaging endpoints][4] at the same time, there is currently no guarantee that the user information will be updated before a message is sent.

For both of the preceding scenarios, if these requests are made in the same API request, there will be no issue.

{% alert note %}
If user attributes and events are sent in the same request (either from `/users/track` or from the SDK), then Braze will process attributes before events or attempting to send any message.
{% endalert %}

Note that if you are sending a scheduled message API request, these requests must be separate, and a user must be created before sending the scheduled API request.

### Avoiding the race condition

One way to avoid this race condition is by adding a delay—around a minute or so—between the creation of a user, and the targeting of that user by your Canvas or campaign, or attempting to log an attribute or event to that user profile.

Similarly, you can use the [`Attributes`][1] object to add, create, or update a user, and then target them using either the [`/canvas/trigger/send` endpoint][2] or [`/campaign/trigger/send` endpoint][3]. This API request will process the `attributes` object before targeting the users.

Attributes that are included in this object will be processed before Braze begins to send the campaign. If the `send_to_existing_only` flag is set to false, and an `external_user_id` does not exist in the Braze database, we will create a user profile for the `external_user_id` and process the associated attributes to the user profile before Braze begins to send the campaign. Also note, if the `send_to_existing_only` flag is set to false, then the attributes object must be included in order to create the user. The `send_to_existing_only` flag can't be used with user aliases.

## Matching action-based triggers and audience filters

Another common race condition may occur if you configure an action-based campaign or Canvas with the same trigger as the audience filter (such as a changed attribute or performed a custom event). The user may not be in the audience at the time they perform the trigger event, which means they won't receive the campaign or enter the Canvas. In this case, Braze recommends you avoid configuring your trigger to match your audience filter. 

### Avoiding the race condition

One way to avoid this race condition can be to add a delay of more than one minute to allow users enough time to enter the Canvas.

[1]: {{site.baseurl}}/api/objects_filters/user_attributes_object/
[2]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/
[3]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/
[4]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/
