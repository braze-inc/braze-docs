---
nav_title: Canvas V2 101
permalink: /canvas_v2_101/
description: "This article describes what to expect during your Canvas V2 experience, such as differences between Canvas V1 and V2."
hidden: true
---

# Canvas V2 101

## What is Canvas V2?

The Canvas V2 workflow is the new and improved editing experience that simplifies how marketers can build and manage their Canvas user journeys. With Canvas V2, you can expect to easily view and use [Canvas components]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components) in the Canvas builder. 

{% alert important %}
Canvas V2 is currently in beta. Please contact your Braze account manager if you are interested in participating in the beta.
{% endalert %}

## What can I expect?

When using Canvas V2, you can expect the following:
* Full Steps to be replaced by lightweight Canvas components
* [Persistent entry properties]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_persistent_entry_properties/) to be available for message personalization throughout a user journey
* More post-launch edit capabilities to change connections between steps, delete steps and variants, and redirect users to different steps
* A new Canvas toolbar that shows all Canvas components
* A cloning feature that allows you to clone existing, stopped Canvases into Canvas V2. Your existing Canvases in V1 will not be altered or deleted.
* **Coming soon:** A new way to zoom in and out between full and icon views in Canvas

To use the Canvas V2 workflow, go to **Canvas** under the **Engagement** tab. Click <i class="fas fa-plus"></i> **Create Canvas**. Next, you'll have the option of building with Canvas V2 or the original Canvas experience. Select **Canvas V2 Workflow** and begin building your Canvas as you normally would!

![][1]{: style="max-width:85%"}

As you’re building or editing your Canvas, if you ever want to switch back to Canvas V1, click **Switch to Canvas V1 Workflow** at the bottom of the Canvas composer or at the top of the Canvas builder. 

{% alert note %}
Switching from Canvas V2 to V1 is allowed only if you do not use Canvas V2 features. Switching from Canvas V1 to V2 will only work if there are no Full Steps in your V1 Canvas.
{% endalert %}

## What will happen to my Canvases that I created using Canvas V1?

All of your existing Canvases and the current version of Canvas (Canvas V1) will continue to exist and be supported by Braze. Customers who choose to join Canvas V2 for early access will have the option of creating a Canvas using either the Canvas V1 or V2 workflow.

## What are the main differences between Canvas V2 and Canvas V1?

### Canvas Step Toolbar

Previously with the Canvas V1 workflow, a Full Step was added by default whenever you created any step in your user journey. Now with Canvas V2, these Full Steps are replaced by different Canvas components, which gives you the benefit of increased visibility and customization for your editing experience. You can immediately see all your Canvas components from the Canvas Step Toolbar.

### Branching

Steps in Canvas V2 can [branch]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/branching/), or split into multiple steps, only using path steps such as [Audience Paths]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths/) or [Action Paths]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/). These steps have a maximum branch size of seven groups and an Everyone Else group. For more than seven groups, simply create another path step connected to the Everyone Else path.

### Step behavior

Previously with the Canvas V1 workflow, each Full Step included delay and schedule settings, exception events, audience filters, message configuration, and message advancement options all in one step. Moving forward, these settings will be separate, which makes your Canvas step building experience more customizable and also introduces some differences in functionality.

### Message Step advancement

[Message Steps]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) advance all users who enter the step. There is no more requirement to specify message advancement behavior, making configuring the step simpler. This does mean that if you want to implement the **Advance when message sent** option, you would need to use a separate Audience Paths Step.

### Delay "in" behavior

[Delay Steps]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/) will wait the entire delay time before proceeding to the next step. 

Let's say on April 12 we have a Delay Step where the delay is set to send your user to the next step in one day at 2pm. A user enters the step at 2:01pm on April 13. 
- For Canvas V1, the user would proceed to the next step at 2pm on April 14, which is less than one day from the entry time. 
- For Canvas V2, the user would proceed to the next step at 2pm on April 15. Note that this is the same time, but more than one day from the entry time. 

### Intelligent Timing behavior

Since [Intelligent Timing]({{site.baseurl}}/user_guide/intelligence/intelligent_timing/) is stored in the Message Step, delays will be applied prior to Intelligent Timing calculations. 

Let's say on April 12, we have a Delay Step set to send a user to the next step after one day using Intelligent Timing. A user enters the step at 2:01pm on April 13, and Intelligent Timing for the given message channel is 2pm. 
- For Canvas V1, the user would receive the message at 2pm on April 14, which is less than one day from the entry time. 
- For Canvas V2, the user would receive the message at 2pm on April 15 instead, which is more than one day from the entry time.

### Exception events

#### Quiet Hours

Exception event functionality in Canvas V2 is applied using Action Paths, which are separate from Message Steps. Quiet Hours are enforced in the Message Step. This means that if a user already passed the Action Path Step (and was not excluded with the exception event there), then hit quiet hours when they got to the Message Step, and had their Canvas configured such that the message re-sends after the Quiet Hours period, the exception event will no longer be applied. This use case is not common.

For Segments and filters, the Canvas V2 Message Step has a new feature called Delivery Validations that allows users to configure additional Segments and filters that are validated at send-time. This prevents the aforementioned Quiet Hours edge case.

#### "In" or "On the next" schedule setting

Exception events in Canvas V2 are created using Action Paths. Action Paths only support “after a X time window” and not “in X time” or “on the next X time".

## I'm interested! How do I access Canvas V2?

Support for Canvas V2 is currently in early access. Contact your Braze account manager if you're interested in participating in the early access!

[1]: {% image_buster /assets/img_archive/canvas_v2_experience.png %}
