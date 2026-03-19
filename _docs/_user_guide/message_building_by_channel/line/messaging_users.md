---
nav_title: Messaging users
article_title: Message LINE Users
page_order: 2
description: "This reference article covers how chat with users by using templated campaigns and Canvases."
page_type: reference
channel:
 - LINE
alias: /line/messaging_users/
---

# Messaging LINE users

> LINE is a two-way communication channel. You can go beyond sending users messages and engage in conversations with users by using templated campaigns and Canvases. This article covers the details of messaging users, such as how to set trigger words for inbound messages and unrecognized responses.

There are various methods to converse with users through LINE, such as using LINE trigger words. You can also use calls-to-action (CTAs) to encourage user engagement with your LINE messaging.

## Action-based triggers

You can create campaigns and Canvases that start, branch, and have mid-journey changes when you receive an inbound LINE message (a message sent from a user) that contains a trigger word. Make sure you choose trigger words that match what you expect users to send.

### Campaign

Set your trigger words when scheduling an action-based delivery campaign.

![Action-based trigger of "Send this campaign to users who sent inbound LINE to subscription group where the message body is" and a blank field.]({% image_buster /assets/img/line/trigger_word_campaign.png %})

### Canvas

Set your trigger words within [action paths]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths) in your Canvas.

![Action path with a trigger of "Send this campaign to users who sent inbound LINE to subscription group where the message body is" and a blank field.]({% image_buster /assets/img/line/trigger_word_canvas.png %})

### Requirements

Each letter of your trigger word must be capitalized when building your campaign or Canvas, even though Braze doesn't require inbound trigger words to be capitalized. For example, if your trigger word is "JOIN2023", an inbound message of “jOin2023” will still trigger the Canvas or campaign.

If no trigger word is specified, the campaign or Canvas will run for *all* inbound LINE messages. This includes messages that have matched phrases across active campaigns and Canvases, in which case the user will receive two LINE messages.

## Unrecognized responses

You should include a trigger option for unrecognized responses on interactive Canvases. This informs users of the available prompts (or trigger words) and sets their expectations for the channel.

### Creating a trigger for unrecognized responses

After creating action groups for the custom filter phrases, add another action group to the action path for **Send LINE message**, and don't check **Where the message body**. This will catch all unrecognized user responses, similar to an “else” clause.

For this message, you should send a LINE message informing the user that this channel is not monitored by a human and, if needed, guide them to a support channel.

