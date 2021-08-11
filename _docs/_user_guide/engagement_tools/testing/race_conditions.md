---
nav_title: Race Conditions
page_order: 9

page_type: reference
description: "This article covers best practices to avoid race conditions from affecting your messaging campaigns."
tool:
- Campaigns
- Canvas
no_index: true
---

# Race Conditions

A **race condition** is a concept where an outcome is dependent on the sequence or timing of other events. For example, if the desired sequence of events is "Event A" and then "Event B", but sometimes "Event A" comes first and other times "Event B" comes first—that is known as a race condition.

{% include video.html id="LyJaxDoMtMs" align="right" %}

## Targeting New Users

In the Braze platform, one of the most common race conditions occurs with messages that target newly created users. Here, the expected order of events is: 

1. A user gets created; 
2. The same user is immediately targeted for a message. 

However, in some cases, the second event will trigger first. This means that a message is attempting to be sent to a user that has not been created yet, and as a result, the user never receives it.

## Using Multiple API Endpoints

If you're using separate API endpoints to create users and trigger Canvases/campaigns, this can also result in this race condition. When user information is sent to Braze via the `users/track` endpoint, it may occasionally take a few seconds to process. As a result, when requests are made to the `users/track` and [messaging endpoints][4] at the same time, there is no guarantee that the user information will be updated before a message is sent. If these requests are made in the same API call, there should be no issue. Please note that if you are sending a scheduled message API call, these requests __must__ be separate, and a user must be created before sending the schdeuled API call.

{% alert note %}
If user attributes are sent via SDK or in the same user/track call as the event, then Braze will automatically process those first before attempting to send any message.
{% endalert %}

One way to avoid this race condition is by adding a delay—around a minute or so—between the creation of a user, and the targeting of that user by your Canvas or campaign. 

Similarly, you can use the [`Attributes`][1] object to add/create/update a user, and then target them using either the [`canvas/trigger/send`][2] or [`campaign/trigger/send`][3] endpoint. This API call will process the `Attributes` object before targeting the users.

Attributes that are included in this object will be processed before Braze begins to send the campaign. If the `send_to_existing_only` flag is set to false, and an `external_user_id` does not exist in Braze’s database, Braze will create a user profile for the `external_user_id` and process the associated attributes to the user profile before Braze begins to send the campaign. Also note, if the `send_to_existing_only` flag is set to false, then the attributes object must be included in order to create the user.

## Matching Action-Based Triggers and Audience Filters

Another common race condition may occur if you configure an action-based campaign or Canvas with the same trigger as the audience filter (i.e., a changed attribute or performed a custom event). The user may not be in the audience at the time they perform the trigger event, which means they won't receive the campaign or enter the Canvas. In this case, Braze recommends you avoid configuring your trigger to match your audience filter.


[1]: {{site.baseurl}}/api/objects_filters/user_attributes_object/
[2]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/
[3]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/
[4]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/
