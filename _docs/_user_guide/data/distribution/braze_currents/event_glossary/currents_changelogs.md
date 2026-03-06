---
nav_title: Currents event changelogs
article_title: Currents event changelogs
page_order: 3
description: "Track schema changes across Currents releases, including new event types and field additions for storage and data sharing."
tool: Currents
---

# Currents changelog

> Track schema changes across Currents releases. Each version lists new event types and field additions for both storage and data sharing.

## Changes in Version 6 (release date 2026-03-04)

### Changes for storage

* Field changes to event type `agentconsole.AgentExecuted`:
    * Added new `string` field `error`: Description of error

* Field changes to event type `agentconsole.ToolInvocation`:
    * Added new `string` field `request_id`: unique id for this overall LLM request and complete execution

* Field changes to event type `users.messages.rcs.InboundReceive`:
    * Added new `string` field `canvas_variation_name`: Name of the Canvas variation this user received

### Changes for data sharing

* Field changes to event type `agentconsole.AgentExecuted`:
    * Added new `string` field `canvas_name`: Name of the Canvas
    * Added new `string` field `canvas_variation_name`: Name of the Canvas variation this user received
    * Added new `string` field `canvas_step_name`: Name of the Canvas step
    * Added new `string` field `error`: Error name

* Field changes to event type `agentconsole.ToolInvocation`:
    * Added new `string` field `request_id`: unique id for this overall LLM request and complete execution

* Field changes to event type `users.behaviors.subscription.GlobalStateChange`:
    * Added new `string` field `campaign_name`: Name of the campaign
    * Added new `string` field `message_variation_name`: Name of the message variation
    * Added new `string` field `canvas_name`: Name of the Canvas
    * Added new `string` field `canvas_variation_name`: Name of the Canvas variation this user received
    * Added new `string` field `canvas_step_name`: Name of the Canvas step

* Field changes to event type `users.behaviors.subscriptiongroup.StateChange`:
    * Added new `string` field `campaign_name`: Name of the campaign
    * Added new `string` field `message_variation_name`: Name of the message variation
    * Added new `string` field `canvas_name`: Name of the Canvas
    * Added new `string` field `canvas_variation_name`: Name of the Canvas variation this user received
    * Added new `string` field `canvas_step_name`: Name of the Canvas step

* Field changes to event type `users.campaigns.Conversion`:
    * Added new `string` field `campaign_name`: Name of the campaign
    * Added new `string` field `message_variation_name`: Name of the message variation
    * Added new `string` field `conversion_behavior`: JSON-encoded string describing the conversion behavior

* Field changes to event type `users.campaigns.EnrollInControl`:
    * Added new `string` field `campaign_name`: Name of the campaign
    * Added new `string` field `message_variation_name`: Name of the message variation

* Field changes to event type `users.canvas.Conversion`:
    * Added new `string` field `canvas_name`: Name of the Canvas
    * Added new `string` field `canvas_variation_name`: Name of the Canvas variation this user received
    * Added new `string` field `canvas_step_name`: Name of the Canvas step
    * Added new `string` field `conversion_behavior`: JSON-encoded string describing the conversion behavior

* Field changes to event type `users.canvas.Entry`:
    * Added new `string` field `canvas_name`: Name of the Canvas
    * Added new `string` field `canvas_variation_name`: Name of the Canvas variation this user received
    * Added new `string` field `canvas_step_name`: Name of the Canvas step

* Field changes to event type `users.canvas.exit.MatchedAudience`:
    * Added new `string` field `canvas_name`: Name of the Canvas
    * Added new `string` field `canvas_variation_name`: Name of the Canvas variation this user received
    * Added new `string` field `canvas_step_name`: Name of the Canvas step

* Field changes to event type `users.canvas.exit.PerformedEvent`:
    * Added new `string` field `canvas_name`: Name of the Canvas
    * Added new `string` field `canvas_variation_name`: Name of the Canvas variation this user received
    * Added new `string` field `canvas_step_name`: Name of the Canvas step

* Field changes to event type `users.canvas.experimentstep.Conversion`:
    * Added new `string` field `canvas_name`: Name of the Canvas
    * Added new `string` field `canvas_variation_name`: Name of the Canvas variation this user received
    * Added new `string` field `canvas_step_name`: Name of the Canvas step
    * Added new `string` field `experiment_split_name`: Name of the experiment split
    * Added new `string` field `conversion_behavior`: JSON-encoded string describing the conversion behavior

* Field changes to event type `users.canvas.experimentstep.SplitEntry`:
    * Added new `string` field `canvas_name`: Name of the Canvas
    * Added new `string` field `canvas_variation_name`: Name of the Canvas variation this user received
    * Added new `string` field `canvas_step_name`: Name of the Canvas step
    * Added new `string` field `experiment_split_name`: Name of the experiment split

* Field changes to event type `users.canvasstep.Progression`:
    * Added new `string` field `canvas_name`: Name of the Canvas
    * Added new `string` field `canvas_variation_name`: Name of the Canvas variation this user received
    * Added new `string` field `canvas_step_name`: Name of the Canvas step

* Field changes to event type `users.messages.banner.Abort`:
    * Added new `string` field `campaign_name`: Name of the campaign
    * Added new `string` field `message_variation_name`: Name of the message variation

* Field changes to event type `users.messages.banner.Click`:
    * Added new `string` field `campaign_name`: Name of the campaign
    * Added new `string` field `message_variation_name`: Name of the message variation

* Field changes to event type `users.messages.banner.Impression`:
    * Added new `string` field `campaign_name`: Name of the campaign
    * Added new `string` field `message_variation_name`: Name of the message variation

* Field changes to event type `users.messages.contentcard.Abort`:
    * Added new `string` field `campaign_name`: Name of the campaign
    * Added new `string` field `message_variation_name`: Name of the message variation
    * Added new `string` field `canvas_name`: Name of the Canvas
    * Added new `string` field `canvas_variation_name`: Name of the Canvas variation this user received
    * Added new `string` field `canvas_step_name`: Name of the Canvas step

* Field changes to event type `users.messages.contentcard.Click`:
    * Added new `string` field `campaign_name`: Name of the campaign
    * Added new `string` field `message_variation_name`: Name of the message variation
    * Added new `string` field `canvas_name`: Name of the Canvas
    * Added new `string` field `canvas_variation_name`: Name of the Canvas variation this user received
    * Added new `string` field `canvas_step_name`: Name of the Canvas step

* Field changes to event type `users.messages.contentcard.Dismiss`:
    * Added new `string` field `campaign_name`: Name of the campaign
    * Added new `string` field `message_variation_name`: Name of the message variation
    * Added new `string` field `canvas_name`: Name of the Canvas
    * Added new `string` field `canvas_variation_name`: Name of the Canvas variation this user received
    * Added new `string` field `canvas_step_name`: Name of the Canvas step

* Field changes to event type `users.messages.contentcard.Impression`:
    * Added new `string` field `campaign_name`: Name of the campaign
    * Added new `string` field `message_variation_name`: Name of the message variation
    * Added new `string` field `canvas_name`: Name of the Canvas
    * Added new `string` field `canvas_variation_name`: Name of the Canvas variation this user received
    * Added new `string` field `canvas_step_name`: Name of the Canvas step

* Field changes to event type `users.messages.contentcard.Send`:
    * Added new `string` field `campaign_name`: Name of the campaign
    * Added new `string` field `message_variation_name`: Name of the message variation
    * Added new `string` field `canvas_name`: Name of the Canvas
    * Added new `string` field `canvas_variation_name`: Name of the Canvas variation this user received
    * Added new `string` field `canvas_step_name`: Name of the Canvas step

* Field changes to event type `users.messages.email.Abort`:
    * Added new `string` field `campaign_name`: Name of the campaign
    * Added new `string` field `message_variation_name`: Name of the message variation
    * Added new `string` field `canvas_name`: Name of the Canvas
    * Added new `string` field `canvas_variation_name`: Name of the Canvas variation this user received
    * Added new `string` field `canvas_step_name`: Name of the Canvas step

* Field changes to event type `users.messages.email.Bounce`:
    * Added new `string` field `campaign_name`: Name of the campaign
    * Added new `string` field `message_variation_name`: Name of the message variation
    * Added new `string` field `canvas_name`: Name of the Canvas
    * Added new `string` field `canvas_variation_name`: Name of the Canvas variation this user received
    * Added new `string` field `canvas_step_name`: Name of the Canvas step

* Field changes to event type `users.messages.email.Click`:
    * Added new `string` field `campaign_name`: Name of the campaign
    * Added new `string` field `message_variation_name`: Name of the message variation
    * Added new `string` field `canvas_name`: Name of the Canvas
    * Added new `string` field `canvas_variation_name`: Name of the Canvas variation this user received
    * Added new `string` field `canvas_step_name`: Name of the Canvas step

* Field changes to event type `users.messages.email.Deferral`:
    * Added new `string` field `campaign_name`: Name of the campaign
    * Added new `string` field `message_variation_name`: Name of the message variation
    * Added new `string` field `canvas_name`: Name of the Canvas
    * Added new `string` field `canvas_variation_name`: Name of the Canvas variation this user received
    * Added new `string` field `canvas_step_name`: Name of the Canvas step

* Field changes to event type `users.messages.email.Delivery`:
    * Added new `string` field `campaign_name`: Name of the campaign
    * Added new `string` field `message_variation_name`: Name of the message variation
    * Added new `string` field `canvas_name`: Name of the Canvas
    * Added new `string` field `canvas_variation_name`: Name of the Canvas variation this user received
    * Added new `string` field `canvas_step_name`: Name of the Canvas step

* Field changes to event type `users.messages.email.MarkAsSpam`:
    * Added new `string` field `campaign_name`: Name of the campaign
    * Added new `string` field `message_variation_name`: Name of the message variation
    * Added new `string` field `canvas_name`: Name of the Canvas
    * Added new `string` field `canvas_variation_name`: Name of the Canvas variation this user received
    * Added new `string` field `canvas_step_name`: Name of the Canvas step

* Field changes to event type `users.messages.email.Open`:
    * Added new `string` field `campaign_name`: Name of the campaign
    * Added new `string` field `message_variation_name`: Name of the message variation
    * Added new `string` field `canvas_name`: Name of the Canvas
    * Added new `string` field `canvas_variation_name`: Name of the Canvas variation this user received
    * Added new `string` field `canvas_step_name`: Name of the Canvas step

* Field changes to event type `users.messages.email.Retry`:
    * Added new `string` field `campaign_name`: Name of the campaign
    * Added new `string` field `message_variation_name`: Name of the message variation
    * Added new `string` field `canvas_name`: Name of the Canvas
    * Added new `string` field `canvas_variation_name`: Name of the Canvas variation this user received
    * Added new `string` field `canvas_step_name`: Name of the Canvas step

* Field changes to event type `users.messages.email.Send`:
    * Added new `string` field `campaign_name`: Name of the campaign
    * Added new `string` field `message_variation_name`: Name of the message variation
    * Added new `string` field `canvas_name`: Name of the Canvas
    * Added new `string` field `canvas_variation_name`: Name of the Canvas variation this user received
    * Added new `string` field `canvas_step_name`: Name of the Canvas step

* Field changes to event type `users.messages.email.SoftBounce`:
    * Added new `string` field `campaign_name`: Name of the campaign
    * Added new `string` field `message_variation_name`: Name of the message variation
    * Added new `string` field `canvas_name`: Name of the Canvas
    * Added new `string` field `canvas_variation_name`: Name of the Canvas variation this user received
    * Added new `string` field `canvas_step_name`: Name of the Canvas step

* Field changes to event type `users.messages.email.Unsubscribe`:
    * Added new `string` field `campaign_name`: Name of the campaign
    * Added new `string` field `message_variation_name`: Name of the message variation
    * Added new `string` field `canvas_name`: Name of the Canvas
    * Added new `string` field `canvas_variation_name`: Name of the Canvas variation this user received
    * Added new `string` field `canvas_step_name`: Name of the Canvas step

* Field changes to event type `users.messages.featureflag.Impression`:
    * Added new `string` field `campaign_name`: Name of the campaign
    * Added new `string` field `canvas_name`: Name of the Canvas
    * Added new `string` field `canvas_step_name`: Name of the Canvas step
    * Added new `string` field `canvas_variation_name`: Name of the Canvas variation this user received
    * Added new `string` field `message_variation_name`: Name of the message variation

* Field changes to event type `users.messages.inappmessage.Abort`:
    * Added new `string` field `campaign_name`: Name of the campaign
    * Added new `string` field `message_variation_name`: Name of the message variation
    * Added new `string` field `canvas_name`: Name of the Canvas
    * Added new `string` field `canvas_variation_name`: Name of the Canvas variation this user received
    * Added new `string` field `canvas_step_name`: Name of the Canvas step

* Field changes to event type `users.messages.inappmessage.Click`:
    * Added new `string` field `campaign_name`: Name of the campaign
    * Added new `string` field `message_variation_name`: Name of the message variation
    * Added new `string` field `canvas_name`: Name of the Canvas
    * Added new `string` field `canvas_variation_name`: Name of the Canvas variation this user received
    * Added new `string` field `canvas_step_name`: Name of the Canvas step

* Field changes to event type `users.messages.inappmessage.Impression`:
    * Added new `string` field `campaign_name`: Name of the campaign
    * Added new `string` field `message_variation_name`: Name of the message variation
    * Added new `string` field `canvas_name`: Name of the Canvas
    * Added new `string` field `canvas_variation_name`: Name of the Canvas variation this user received
    * Added new `string` field `canvas_step_name`: Name of the Canvas step

* Field changes to event type `users.messages.line.Retry`:
    * Added new `string` field `campaign_name`: Name of the campaign
    * Added new `string` field `canvas_step_name`: Name of the Canvas step

* Field changes to event type `users.messages.pushnotification.Abort`:
    * Added new `string` field `campaign_name`: Name of the campaign
    * Added new `string` field `message_variation_name`: Name of the message variation
    * Added new `string` field `canvas_name`: Name of the Canvas
    * Added new `string` field `canvas_variation_name`: Name of the Canvas variation this user received
    * Added new `string` field `canvas_step_name`: Name of the Canvas step

* Field changes to event type `users.messages.pushnotification.Bounce`:
    * Added new `string` field `campaign_name`: Name of the campaign
    * Added new `string` field `message_variation_name`: Name of the message variation
    * Added new `string` field `canvas_name`: Name of the Canvas
    * Added new `string` field `canvas_variation_name`: Name of the Canvas variation this user received
    * Added new `string` field `canvas_step_name`: Name of the Canvas step

* Field changes to event type `users.messages.pushnotification.InfluencedOpen`:
    * Added new `string` field `campaign_name`: Name of the campaign
    * Added new `string` field `message_variation_name`: Name of the message variation
    * Added new `string` field `canvas_name`: Name of the Canvas
    * Added new `string` field `canvas_variation_name`: Name of the Canvas variation this user received
    * Added new `string` field `canvas_step_name`: Name of the Canvas step

* Field changes to event type `users.messages.pushnotification.IosForeground`:
    * Added new `string` field `campaign_name`: Name of the campaign
    * Added new `string` field `message_variation_name`: Name of the message variation
    * Added new `string` field `canvas_name`: Name of the Canvas
    * Added new `string` field `canvas_variation_name`: Name of the Canvas variation this user received
    * Added new `string` field `canvas_step_name`: Name of the Canvas step

* Field changes to event type `users.messages.pushnotification.Open`:
    * Added new `string` field `campaign_name`: Name of the campaign
    * Added new `string` field `message_variation_name`: Name of the message variation
    * Added new `string` field `canvas_name`: Name of the Canvas
    * Added new `string` field `canvas_variation_name`: Name of the Canvas variation this user received
    * Added new `string` field `canvas_step_name`: Name of the Canvas step

* Field changes to event type `users.messages.pushnotification.Retry`:
    * Added new `string` field `campaign_name`: Name of the campaign
    * Added new `string` field `message_variation_name`: Name of the message variation
    * Added new `string` field `canvas_name`: Name of the Canvas
    * Added new `string` field `canvas_variation_name`: Name of the Canvas variation this user received
    * Added new `string` field `canvas_step_name`: Name of the Canvas step

* Field changes to event type `users.messages.pushnotification.Send`:
    * Added new `string` field `campaign_name`: Name of the campaign
    * Added new `string` field `message_variation_name`: Name of the message variation
    * Added new `string` field `canvas_name`: Name of the Canvas
    * Added new `string` field `canvas_variation_name`: Name of the Canvas variation this user received
    * Added new `string` field `canvas_step_name`: Name of the Canvas step

* Field changes to event type `users.messages.rcs.InboundReceive`:
    * Added new `string` field `canvas_variation_name`: Name of the Canvas variation this user received

* Field changes to event type `users.messages.sms.Abort`:
    * Added new `string` field `campaign_name`: Name of the campaign
    * Added new `string` field `message_variation_name`: Name of the message variation
    * Added new `string` field `canvas_name`: Name of the Canvas
    * Added new `string` field `canvas_variation_name`: Name of the Canvas variation this user received
    * Added new `string` field `canvas_step_name`: Name of the Canvas step

* Field changes to event type `users.messages.sms.CarrierSend`:
    * Added new `string` field `campaign_name`: Name of the campaign
    * Added new `string` field `message_variation_name`: Name of the message variation
    * Added new `string` field `canvas_name`: Name of the Canvas
    * Added new `string` field `canvas_variation_name`: Name of the Canvas variation this user received
    * Added new `string` field `canvas_step_name`: Name of the Canvas step

* Field changes to event type `users.messages.sms.Delivery`:
    * Added new `string` field `campaign_name`: Name of the campaign
    * Added new `string` field `message_variation_name`: Name of the message variation
    * Added new `string` field `canvas_name`: Name of the Canvas
    * Added new `string` field `canvas_variation_name`: Name of the Canvas variation this user received
    * Added new `string` field `canvas_step_name`: Name of the Canvas step

* Field changes to event type `users.messages.sms.DeliveryFailure`:
    * Added new `string` field `campaign_name`: Name of the campaign
    * Added new `string` field `message_variation_name`: Name of the message variation
    * Added new `string` field `canvas_name`: Name of the Canvas
    * Added new `string` field `canvas_variation_name`: Name of the Canvas variation this user received
    * Added new `string` field `canvas_step_name`: Name of the Canvas step

* Field changes to event type `users.messages.sms.InboundReceive`:
    * Added new `string` field `campaign_name`: Name of the campaign
    * Added new `string` field `message_variation_name`: Name of the message variation
    * Added new `string` field `canvas_name`: Name of the Canvas
    * Added new `string` field `canvas_variation_name`: Name of the Canvas variation this user received
    * Added new `string` field `canvas_step_name`: Name of the Canvas step

* Field changes to event type `users.messages.sms.Rejection`:
    * Added new `string` field `campaign_name`: Name of the campaign
    * Added new `string` field `message_variation_name`: Name of the message variation
    * Added new `string` field `canvas_name`: Name of the Canvas
    * Added new `string` field `canvas_variation_name`: Name of the Canvas variation this user received
    * Added new `string` field `canvas_step_name`: Name of the Canvas step

* Field changes to event type `users.messages.sms.Retry`:
    * Added new `string` field `campaign_name`: Name of the campaign
    * Added new `string` field `message_variation_name`: Name of the message variation
    * Added new `string` field `canvas_name`: Name of the Canvas
    * Added new `string` field `canvas_variation_name`: Name of the Canvas variation this user received
    * Added new `string` field `canvas_step_name`: Name of the Canvas step

* Field changes to event type `users.messages.sms.Send`:
    * Added new `string` field `campaign_name`: Name of the campaign
    * Added new `string` field `message_variation_name`: Name of the message variation
    * Added new `string` field `canvas_name`: Name of the Canvas
    * Added new `string` field `canvas_variation_name`: Name of the Canvas variation this user received
    * Added new `string` field `canvas_step_name`: Name of the Canvas step

* Field changes to event type `users.messages.sms.ShortLinkClick`:
    * Added new `string` field `campaign_name`: Name of the campaign
    * Added new `string` field `message_variation_name`: Name of the message variation
    * Added new `string` field `canvas_name`: Name of the Canvas
    * Added new `string` field `canvas_variation_name`: Name of the Canvas variation this user received
    * Added new `string` field `canvas_step_name`: Name of the Canvas step

* Field changes to event type `users.messages.webhook.Abort`:
    * Added new `string` field `campaign_name`: Name of the campaign
    * Added new `string` field `message_variation_name`: Name of the message variation
    * Added new `string` field `canvas_name`: Name of the Canvas
    * Added new `string` field `canvas_variation_name`: Name of the Canvas variation this user received
    * Added new `string` field `canvas_step_name`: Name of the Canvas step

* Field changes to event type `users.messages.webhook.Failure`:
    * Added new `string` field `campaign_name`: Name of the campaign
    * Added new `string` field `canvas_name`: Name of the Canvas
    * Added new `string` field `canvas_step_name`: Name of the Canvas step
    * Added new `string` field `canvas_variation_name`: Name of the Canvas variation this user received
    * Added new `string` field `message_variation_name`: Name of the message variation

* Field changes to event type `users.messages.webhook.Retry`:
    * Added new `string` field `campaign_name`: Name of the campaign
    * Added new `string` field `message_variation_name`: Name of the message variation
    * Added new `string` field `canvas_name`: Name of the Canvas
    * Added new `string` field `canvas_variation_name`: Name of the Canvas variation this user received
    * Added new `string` field `canvas_step_name`: Name of the Canvas step

* Field changes to event type `users.messages.webhook.Send`:
    * Added new `string` field `campaign_name`: Name of the campaign
    * Added new `string` field `message_variation_name`: Name of the message variation
    * Added new `string` field `canvas_name`: Name of the Canvas
    * Added new `string` field `canvas_variation_name`: Name of the Canvas variation this user received
    * Added new `string` field `canvas_step_name`: Name of the Canvas step

* Field changes to event type `users.messages.whatsapp.Abort`:
    * Added new `string` field `campaign_name`: Name of the campaign
    * Added new `string` field `message_variation_name`: Name of the message variation
    * Added new `string` field `canvas_name`: Name of the Canvas
    * Added new `string` field `canvas_variation_name`: Name of the Canvas variation this user received
    * Added new `string` field `canvas_step_name`: Name of the Canvas step

* Field changes to event type `users.messages.whatsapp.Click`:
    * Added new `string` field `campaign_name`: Name of the campaign
    * Added new `string` field `message_variation_name`: Name of the message variation
    * Added new `string` field `canvas_name`: Name of the Canvas
    * Added new `string` field `canvas_variation_name`: Name of the Canvas variation this user received
    * Added new `string` field `canvas_step_name`: Name of the Canvas step

* Field changes to event type `users.messages.whatsapp.Delivery`:
    * Added new `string` field `campaign_name`: Name of the campaign
    * Added new `string` field `message_variation_name`: Name of the message variation
    * Added new `string` field `canvas_name`: Name of the Canvas
    * Added new `string` field `canvas_variation_name`: Name of the Canvas variation this user received
    * Added new `string` field `canvas_step_name`: Name of the Canvas step

* Field changes to event type `users.messages.whatsapp.Failure`:
    * Added new `string` field `campaign_name`: Name of the campaign
    * Added new `string` field `message_variation_name`: Name of the message variation
    * Added new `string` field `canvas_name`: Name of the Canvas
    * Added new `string` field `canvas_variation_name`: Name of the Canvas variation this user received
    * Added new `string` field `canvas_step_name`: Name of the Canvas step

* Field changes to event type `users.messages.whatsapp.InboundReceive`:
    * Added new `string` field `campaign_name`: Name of the campaign
    * Added new `string` field `canvas_name`: Name of the Canvas
    * Added new `string` field `canvas_step_name`: Name of the Canvas step
    * Added new `string` field `canvas_variation_name`: Name of the Canvas variation this user received
    * Added new `string` field `message_variation_name`: Name of the message variation

* Field changes to event type `users.messages.whatsapp.Read`:
    * Added new `string` field `campaign_name`: Name of the campaign
    * Added new `string` field `message_variation_name`: Name of the message variation
    * Added new `string` field `canvas_name`: Name of the Canvas
    * Added new `string` field `canvas_variation_name`: Name of the Canvas variation this user received
    * Added new `string` field `canvas_step_name`: Name of the Canvas step

* Field changes to event type `users.messages.whatsapp.Retry`:
    * Added new `string` field `campaign_name`: Name of the campaign
    * Added new `string` field `message_variation_name`: Name of the message variation
    * Added new `string` field `canvas_name`: Name of the Canvas
    * Added new `string` field `canvas_variation_name`: Name of the Canvas variation this user received
    * Added new `string` field `canvas_step_name`: Name of the Canvas step

* Field changes to event type `users.messages.whatsapp.Send`:
    * Added new `string` field `campaign_name`: Name of the campaign
    * Added new `string` field `canvas_name`: Name of the Canvas
    * Added new `string` field `canvas_step_name`: Name of the Canvas step
    * Added new `string` field `canvas_variation_name`: Name of the Canvas variation this user received
    * Added new `string` field `message_variation_name`: Name of the message variation

## Changes in Version 5 (release date 2026-02-04)

### Changes for storage

* Added new event type `agentconsole.AgentExecuted`.
* Added new event type `agentconsole.ToolInvocation`.
* Added new event type `users.messages.email.Retry`.
* Added new event type `users.messages.line.Retry`.
* Added new event type `users.messages.pushnotification.Retry`.
* Added new event type `users.messages.sms.Retry`.
* Added new event type `users.messages.webhook.Retry`.
* Added new event type `users.messages.whatsapp.Retry`.
* Field changes to event type `users.behaviors.pushnotification.TokenStateChange`:
    * Added new `long` field `time_ms`: Time in millisecond when the event happened

### Changes for data sharing

* Added new event type `agentconsole.AgentExecuted`.
* Added new event type `agentconsole.ToolInvocation`.
* Added new event type `users.messages.email.Retry`.
* Added new event type `users.messages.line.Retry`.
* Added new event type `users.messages.pushnotification.Retry`.
* Added new event type `users.messages.sms.Retry`.
* Added new event type `users.messages.webhook.Retry`.
* Added new event type `users.messages.whatsapp.Retry`.
* Field changes to event type `users.behaviors.pushnotification.TokenStateChange`:
    * Added new `long` field `time_ms`: Time in millisecond when the event happened

## Changes in Version 4 (release date 2026-01-07)

### Changes for storage

* Field changes to event type `users.behaviors.pushnotification.TokenStateChange`:
    * Added new `string` field `push_token`: Push token of the event

* Field changes to event type `users.messages.pushnotification.Bounce`:
    * Added new `string` field `push_token`: Push token of the event

* Field changes to event type `users.messages.pushnotification.Send`:
    * Added new `string` field `push_token`: Push token of the event

* Field changes to event type `users.messages.rcs.Click`:
    * Added new `string` field `canvas_variation_name`: Name of the Canvas variation this user received
    * Field `user_phone_number` is now *optional*.

* Field changes to event type `users.messages.rcs.InboundReceive`:
    * Field `user_id` is now *optional*.

* Field changes to event type `users.messages.rcs.Rejection`:
    * Added new `string` field `canvas_step_message_variation_id`: API ID of the Canvas step message variation this user received

### Changes for data sharing

* Field changes to event type `users.messages.rcs.Click`:
    * Added new `string` field `canvas_variation_name`: Name of the Canvas variation this user received
    * Field `user_phone_number` is now *optional*.

* Field changes to event type `users.messages.rcs.InboundReceive`:
    * Field `user_id` is now *optional*.

* Field changes to event type `users.messages.rcs.Rejection`:
    * Added new `string` field `canvas_step_message_variation_api_id`: API ID of the Canvas step message variation this user received

## Changes in Version 3 (release date 2025-10-08)

### Changes for storage

* Added new event type `users.messages.line.Abort`.
* Added new event type `users.messages.line.Click`.
* Added new event type `users.messages.line.InboundReceive`.
* Added new event type `users.messages.line.Send`.
* Added new event type `users.messages.rcs.Abort`.
* Added new event type `users.messages.rcs.Click`.
* Added new event type `users.messages.rcs.Delivery`.
* Added new event type `users.messages.rcs.InboundReceive`.
* Added new event type `users.messages.rcs.Read`.
* Added new event type `users.messages.rcs.Rejection`.
* Added new event type `users.messages.rcs.Send`.
* Field changes to event type `users.messages.sms.Delivery`:
    * Added new `boolean` field `is_sms_fallback`: Indicates that a SMS fallback message was sent due to a rejected RCS message. The message could result in delivery, delivery failure, or rejection. It can be linked to the RCS Rejection event via a send ID and dispatch ID

* Field changes to event type `users.messages.sms.DeliveryFailure`:
    * Added new `boolean` field `is_sms_fallback`: Indicates that a SMS fallback message was sent due to a rejected RCS message. The message could result in delivery, delivery failure, or rejection. It can be linked to the RCS Rejection event via a send ID and dispatch ID

* Field changes to event type `users.messages.sms.Rejection`:
    * Added new `boolean` field `is_sms_fallback`: Indicates that a SMS fallback message was sent due to a rejected RCS message. The message could result in delivery, delivery failure, or rejection. It can be linked to the RCS Rejection event via a send ID and dispatch ID It can be linked to the RCS Rejection event via a send ID and dispatch ID. (Event property)

* Field changes to event type `users.messages.whatsapp.Delivery`:
    * Added new `string` field `flow_id`: The unique ID of the Flow in the WhatsApp Manager. Present if the message includes a CTA to respond to a WhatsApp Flow
    * Added new `string` field `template_name`: [PII] Name of the template in the WhatsApp manager. Present if sending a Template Message
    * Added new `string` field `message_id`: The unique ID generated by Meta for this message

* Field changes to event type `users.messages.whatsapp.Failure`:
    * Added new `string` field `message_id`: The unique ID generated by Meta for this message
    * Added new `string` field `template_name`: [PII] Name of the template in the WhatsApp manager. Present if sending a Template Message
    * Added new `string` field `flow_id`: The unique ID of the Flow in the WhatsApp Manager. Present if the message includes a CTA to respond to a WhatsApp Flow

* Field changes to event type `users.messages.whatsapp.InboundReceive`:
    * Added new `string` field `catalog_id`: Catalog ID of a product if a product is referenced in the inbound message. Otherwise, empty.
    * Added new `string` field `product_id`: Product SKU if a product is referenced in the inbound message. Otherwise, empty.
    * Added new `string` field `flow_id`: The unique ID of the Flow in the WhatsApp Manager. Present if the user is responding to a WhatsApp Flow.
    * Added new `string` field `flow_response_json`: [PII] The form values the user responded with. Present if the user is responding to a WhatsApp Flow.
    * Added new `string` field `message_id`: The unique ID generated by Meta for this message
    * Added new `string` field `in_reply_to`: The message_id of the message this message was replying to

* Field changes to event type `users.messages.whatsapp.Read`:
    * Added new `string` field `template_name`: [PII] Name of the template in the WhatsApp manager. Present if sending a Template Message
    * Added new `string` field `message_id`: The unique ID generated by Meta for this message
    * Added new `string` field `flow_id`: The unique ID of the Flow in the WhatsApp Manager. Present if the message includes a CTA to respond to a WhatsApp Flow

* Field changes to event type `users.messages.whatsapp.Send`:
    * Added new `string` field `flow_id`: The unique ID of the Flow in the WhatsApp Manager. Present if the message includes a CTA to respond to a WhatsApp Flow
    * Added new `string` field `template_name`: [PII] Name of the template in the WhatsApp Manager. Present if sending a Template Message
    * Added new `string` field `message_id`: The unique ID generated by Meta for this message

### Changes for data sharing

* Added new event type `users.messages.line.Abort`.
* Added new event type `users.messages.line.Click`.
* Added new event type `users.messages.line.InboundReceive`.
* Added new event type `users.messages.line.Send`.
* Added new event type `users.messages.rcs.Abort`.
* Added new event type `users.messages.rcs.Click`.
* Added new event type `users.messages.rcs.Delivery`.
* Added new event type `users.messages.rcs.InboundReceive`.
* Added new event type `users.messages.rcs.Read`.
* Added new event type `users.messages.rcs.Rejection`.
* Added new event type `users.messages.rcs.Send`.
* Field changes to event type `users.messages.sms.Delivery`:
    * Added new `boolean` field `is_sms_fallback`: Indicates if SMS fallback was attempted for this rejected RCS message. It is linked/paired to the SMS Delivery event

* Field changes to event type `users.messages.sms.DeliveryFailure`:
    * Added new `boolean` field `is_sms_fallback`: Indicates if SMS fallback was attempted for this rejected RCS message. It is linked/paired to the SMS Delivery event

* Field changes to event type `users.messages.sms.Rejection`:
    * Added new `boolean` field `is_sms_fallback`: Indicates if SMS fallback was attempted for this rejected RCS message. It is linked/paired to the SMS Delivery event

* Field changes to event type `users.messages.whatsapp.Delivery`:
    * Added new `string` field `flow_id`: The unique ID of the Flow in the WhatsApp Manager. Present if the user is responding to a WhatsApp Flow.
    * Added new `string` field `template_name`: [PII] Name of the template in the WhatsApp manager. Present if sending a Template Message
    * Added new `string` field `message_id`: The unique ID generated by Meta for this message

* Field changes to event type `users.messages.whatsapp.Failure`:
    * Added new `string` field `message_id`: The unique ID generated by Meta for this message
    * Added new `string` field `template_name`: [PII] Name of the template in the WhatsApp manager. Present if sending a Template Message
    * Added new `string` field `flow_id`: The unique ID of the Flow in the WhatsApp Manager. Present if the user is responding to a WhatsApp Flow.

* Field changes to event type `users.messages.whatsapp.InboundReceive`:
    * Added new `string` field `catalog_id`: Catalog ID of a product if a product is referenced in the inbound message. Otherwise, empty.
    * Added new `string` field `product_id`: ID of the product purchased
    * Added new `string` field `flow_id`: The unique ID of the Flow in the WhatsApp Manager. Present if the user is responding to a WhatsApp Flow.
    * Added new `string` field `flow_response_json`: [PII] The form values the user responded with. Present if the user is responding to a WhatsApp Flow.
    * Added new `string` field `message_id`: The unique ID generated by Meta for this message
    * Added new `string` field `in_reply_to`: The message_id of the message this message was replying to

* Field changes to event type `users.messages.whatsapp.Read`:
    * Added new `string` field `template_name`: [PII] Name of the template in the WhatsApp manager. Present if sending a Template Message
    * Added new `string` field `message_id`: The unique ID generated by Meta for this message
    * Added new `string` field `flow_id`: The unique ID of the Flow in the WhatsApp Manager. Present if the user is responding to a WhatsApp Flow.

* Field changes to event type `users.messages.whatsapp.Send`:
    * Added new `string` field `flow_id`: The unique ID of the Flow in the WhatsApp Manager. Present if the user is responding to a WhatsApp Flow.
    * Added new `string` field `template_name`: [PII] Name of the template in the WhatsApp manager. Present if sending a Template Message
    * Added new `string` field `message_id`: The unique ID generated by Meta for this message

## Changes in Version 2 (release date null)

### Changes for storage

* Added new event type `users.behaviors.app.FirstSession`.
* Added new event type `users.behaviors.app.SessionEnd`.
* Added new event type `users.behaviors.app.SessionStart`.
* Added new event type `users.behaviors.CustomEvent`.
* Added new event type `users.behaviors.InstallAttribution`.
* Added new event type `users.behaviors.liveactivity.PushToStartTokenChange`.
* Added new event type `users.behaviors.liveactivity.UpdateTokenChange`.
* Added new event type `users.behaviors.Location`.
* Added new event type `users.behaviors.Purchase`.
* Added new event type `users.behaviors.pushnotification.TokenStateChange`.
* Added new event type `users.behaviors.subscription.GlobalStateChange`.
* Added new event type `users.behaviors.subscriptiongroup.StateChange`.
* Added new event type `users.behaviors.Uninstall`.
* Added new event type `users.campaigns.Conversion`.
* Added new event type `users.campaigns.EnrollInControl`.
* Added new event type `users.canvas.Conversion`.
* Added new event type `users.canvas.Entry`.
* Added new event type `users.canvas.exit.MatchedAudience`.
* Added new event type `users.canvas.exit.PerformedEvent`.
* Added new event type `users.canvas.experimentstep.Conversion`.
* Added new event type `users.canvas.experimentstep.SplitEntry`.
* Added new event type `users.canvasstep.Progression`.
* Added new event type `users.messages.banner.Abort`.
* Added new event type `users.messages.banner.Click`.
* Added new event type `users.messages.banner.Impression`.
* Added new event type `users.messages.contentcard.Abort`.
* Added new event type `users.messages.contentcard.Click`.
* Added new event type `users.messages.contentcard.Dismiss`.
* Added new event type `users.messages.contentcard.Impression`.
* Added new event type `users.messages.contentcard.Send`.
* Added new event type `users.messages.email.Abort`.
* Added new event type `users.messages.email.Bounce`.
* Added new event type `users.messages.email.Click`.
* Added new event type `users.messages.email.Deferral`.
* Added new event type `users.messages.email.Delivery`.
* Added new event type `users.messages.email.MarkAsSpam`.
* Added new event type `users.messages.email.Open`.
* Added new event type `users.messages.email.Send`.
* Added new event type `users.messages.email.SoftBounce`.
* Added new event type `users.messages.email.Unsubscribe`.
* Added new event type `users.messages.featureflag.Impression`.
* Added new event type `users.messages.inappmessage.Abort`.
* Added new event type `users.messages.inappmessage.Click`.
* Added new event type `users.messages.inappmessage.Impression`.
* Added new event type `users.messages.liveactivity.Outcome`.
* Added new event type `users.messages.liveactivity.Send`.
* Added new event type `users.messages.pushnotification.Abort`.
* Added new event type `users.messages.pushnotification.Bounce`.
* Added new event type `users.messages.pushnotification.IosForeground`.
* Added new event type `users.messages.pushnotification.Open`.
* Added new event type `users.messages.pushnotification.Send`.
* Added new event type `users.messages.sms.Abort`.
* Added new event type `users.messages.sms.CarrierSend`.
* Added new event type `users.messages.sms.Delivery`.
* Added new event type `users.messages.sms.DeliveryFailure`.
* Added new event type `users.messages.sms.InboundReceive`.
* Added new event type `users.messages.sms.Rejection`.
* Added new event type `users.messages.sms.Send`.
* Added new event type `users.messages.sms.ShortLinkClick`.
* Added new event type `users.messages.webhook.Abort`.
* Added new event type `users.messages.webhook.Failure`.
* Added new event type `users.messages.webhook.Send`.
* Added new event type `users.messages.whatsapp.Abort`.
* Added new event type `users.messages.whatsapp.Click`.
* Added new event type `users.messages.whatsapp.Delivery`.
* Added new event type `users.messages.whatsapp.Failure`.
* Added new event type `users.messages.whatsapp.InboundReceive`.
* Added new event type `users.messages.whatsapp.Read`.
* Added new event type `users.messages.whatsapp.Send`.
* Added new event type `users.RandomBucketNumberUpdate`.

### Changes for data sharing

* Added new event type `changelogs.GlobalControlGroup`.
* Added new event type `users.behaviors.app.FirstSession`.
* Added new event type `users.behaviors.app.NewsFeedImpression`.
* Added new event type `users.behaviors.app.SessionEnd`.
* Added new event type `users.behaviors.app.SessionStart`.
* Added new event type `users.behaviors.CustomEvent`.
* Added new event type `users.behaviors.geofence.DataEvent`.
* Added new event type `users.behaviors.geofence.RecordEvent`.
* Added new event type `users.behaviors.InstallAttribution`.
* Added new event type `users.behaviors.liveactivity.PushToStartTokenChange`.
* Added new event type `users.behaviors.liveactivity.UpdateTokenChange`.
* Added new event type `users.behaviors.Location`.
* Added new event type `users.behaviors.Purchase`.
* Added new event type `users.behaviors.pushnotification.TokenStateChange`.
* Added new event type `users.behaviors.subscription.GlobalStateChange`.
* Added new event type `users.behaviors.subscriptiongroup.StateChange`.
* Added new event type `users.behaviors.Uninstall`.
* Added new event type `users.behaviors.UpgradedApp`.
* Added new event type `users.campaigns.Conversion`.
* Added new event type `users.campaigns.EnrollInControl`.
* Added new event type `users.campaigns.FrequencyCap`.
* Added new event type `users.campaigns.Revenue`.
* Added new event type `users.canvas.Conversion`.
* Added new event type `users.canvas.Entry`.
* Added new event type `users.canvas.exit.MatchedAudience`.
* Added new event type `users.canvas.exit.PerformedEvent`.
* Added new event type `users.canvas.experimentstep.Conversion`.
* Added new event type `users.canvas.experimentstep.SplitEntry`.
* Added new event type `users.canvas.FrequencyCap`.
* Added new event type `users.canvas.Revenue`.
* Added new event type `users.canvasstep.Progression`.
* Added new event type `users.messages.banner.Abort`.
* Added new event type `users.messages.banner.Click`.
* Added new event type `users.messages.banner.Impression`.
* Added new event type `users.messages.contentcard.Abort`.
* Added new event type `users.messages.contentcard.Click`.
* Added new event type `users.messages.contentcard.Dismiss`.
* Added new event type `users.messages.contentcard.Impression`.
* Added new event type `users.messages.contentcard.Send`.
* Added new event type `users.messages.email.Abort`.
* Added new event type `users.messages.email.Bounce`.
* Added new event type `users.messages.email.Click`.
* Added new event type `users.messages.email.Deferral`.
* Added new event type `users.messages.email.Delivery`.
* Added new event type `users.messages.email.MarkAsSpam`.
* Added new event type `users.messages.email.Open`.
* Added new event type `users.messages.email.Send`.
* Added new event type `users.messages.email.SoftBounce`.
* Added new event type `users.messages.email.Unsubscribe`.
* Added new event type `users.messages.featureflag.Impression`.
* Added new event type `users.messages.inappmessage.Abort`.
* Added new event type `users.messages.inappmessage.Click`.
* Added new event type `users.messages.inappmessage.Impression`.
* Added new event type `users.messages.liveactivity.Outcome`.
* Added new event type `users.messages.liveactivity.Send`.
* Added new event type `users.messages.newsfeedcard.Abort`.
* Added new event type `users.messages.newsfeedcard.Click`.
* Added new event type `users.messages.newsfeedcard.Impression`.
* Added new event type `users.messages.pushnotification.Abort`.
* Added new event type `users.messages.pushnotification.Bounce`.
* Added new event type `users.messages.pushnotification.InfluencedOpen`.
* Added new event type `users.messages.pushnotification.IosForeground`.
* Added new event type `users.messages.pushnotification.Open`.
* Added new event type `users.messages.pushnotification.Send`.
* Added new event type `users.messages.sms.Abort`.
* Added new event type `users.messages.sms.CarrierSend`.
* Added new event type `users.messages.sms.Delivery`.
* Added new event type `users.messages.sms.DeliveryFailure`.
* Added new event type `users.messages.sms.InboundReceive`.
* Added new event type `users.messages.sms.Rejection`.
* Added new event type `users.messages.sms.Send`.
* Added new event type `users.messages.sms.ShortLinkClick`.
* Added new event type `users.messages.webhook.Abort`.
* Added new event type `users.messages.webhook.Failure`.
* Added new event type `users.messages.webhook.Send`.
* Added new event type `users.messages.whatsapp.Abort`.
* Added new event type `users.messages.whatsapp.Click`.
* Added new event type `users.messages.whatsapp.Delivery`.
* Added new event type `users.messages.whatsapp.Failure`.
* Added new event type `users.messages.whatsapp.InboundReceive`.
* Added new event type `users.messages.whatsapp.Read`.
* Added new event type `users.messages.whatsapp.Send`.
* Added new event type `users.RandomBucketNumberUpdate`.
* Added new event type `users.UserDeleteRequest`.
* Added new event type `users.UserOrphan`.
