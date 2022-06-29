---
nav_title: Canvas Flow 101
permalink: /canvas_v2_101/
description: "This article describes what to expect during your Canvas Flow experience, such as differences between the original Canvas editor and Canvas Flow."
hidden: true
---

# Canvas Flow 101

## What is Canvas Flow?

Canvas Flow is the new and improved editing experience that simplifies how marketers can build and manage their Canvas user journeys. With Canvas Flow, you can expect to easily view and use [Canvas components]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components) in the Canvas builder. 

{% alert important %}
Canvas Flow is currently in early access. Please contact your Braze account manager if you are interested in participating in the early access.
{% endalert %}

## What can I expect?

When using Canvas Flow, you can expect the following:
* Full Steps to be replaced by lightweight Canvas components
* [Persistent entry properties]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_persistent_entry_properties/) to be available for message personalization throughout a user journey
* More post-launch edit capabilities to change connections between steps, delete steps and variants, and redirect users to different steps
* A new Canvas toolbar that shows all Canvas components
* A [cloning tool]({{site.baseurl}}/cloning_canvases/) that allows you to clone your stopped Canvases to Canvas Flow. The existing Canvases in V1 will not be altered or deleted.
* **Coming soon:** A new way to zoom in and out between full and icon views in Canvas

To use the Canvas Flow workflow, go to **Canvas** under the **Engagement** tab. Click <i class="fas fa-plus"></i> **Create Canvas**. Next, you'll have the option of building with Canvas Flow or the original Canvas experience. Select **Canvas Flow Workflow** and begin building your Canvas as you normally would!

![][1]{: style="max-width:85%"}

As you’re building or editing your Canvas, if you ever want to switch back to Canvas V1, click **Switch to Canvas V1 Workflow** at the bottom of the Canvas composer or at the top of the Canvas builder. 

{% alert note %}
Switching from Canvas Flow to the original Canvas editor is allowed only if you do not use Canvas Flow features, and will only work if there are no Full Steps in your Canvas.
{% endalert %}

## What will happen to my Canvases that I created using Canvas V1?

All of your existing Canvases and the current version of Canvas (Canvas V1) will continue to exist and be supported by Braze. Customers who choose to join Canvas Flow for early access will have the option of creating a Canvas using either the Canvas V1 or Flow workflow.

## What are the main differences between Canvas Flow and Canvas V1?

### Canvas Component Toolbar

Previously with the original Canvas editor, a Full Step was added by default whenever you created any step in your user journey. Now with Canvas Flow, these Full Steps are replaced by different Canvas components, which gives you the benefit of increased visibility and customization for your editing experience. You can immediately see all your Canvas components from the Canvas Step Toolbar.

### Branching

Steps in Canvas Flow can [branch]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/branching/), or split into multiple steps, only using path steps such as [Audience Paths]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths/) or [Action Paths]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/). These steps have a maximum branch size of seven groups and an Everyone Else group. For more than seven groups, simply create another path step connected to the Everyone Else path.

### Step behavior

Previously with the Canvas V1 workflow, each Full Step included information such as delay and schedule settings, exception events, audience filters, message configuration, and message advancement options all in one component. Moving forward, these settings will be separate. This makes your Canvas component building experience more customizable and also introduces some differences in functionality.

### Message Step advancement

[Message Steps]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) advance all users who enter the step. There is no requirement to specify message advancement behavior, making configuring the step simpler. If you want to implement the **Advance when message sent** option, add a separate Audience Paths Step to filter users that didn't receive the previous step.  

### Delay "in" behavior

[Delay components]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/) will wait the entire delay time before proceeding to the next step. 

Let's say on April 12 we have a Delay component where the delay is set to send your user to the next component in one day at 2pm. A user enters the component at 2:01pm on April 13. 
- For Canvas V1, the user would proceed to the next component at 2pm on April 14, which is less than one day from the entry time. 
- For Canvas Flow, the user would proceed to the next component at 2pm on April 15. Note that this is the same time, but more than one day from the entry time. 

### Intelligent Timing behavior

Since [Intelligent Timing]({{site.baseurl}}/user_guide/intelligence/intelligent_timing/) is stored in the Message component, delays will be applied prior to Intelligent Timing calculations. This means that, depending on when a user enters the component, they may receive the message later than they would in a Canvas built with the original Canvas editor.

If you set a delay for two days and use Intelligent Timing, it would look as follows:

- **Canvas V1:** 
Full Step - Delay 1 full day (24 hours). On the second day, send at the intelligent time (e.g. 11am) within day 2
- **Canvas Flow:** 
Delay Step - Delay 2 full days (48 hours)
Message Step - After the delay is up, send at the intelligent time (e.g. 11am) as soon as possible

For Canvas Flow, the Delay component will first delay the message for the number of days you choose. Then, as soon as the number of days has passed, the user would start receiving messages at the set Intelligent Timing. For example, if your delay is set for two days and you use Intelligent Timing, then it will take 48 hours for Intelligent Timing to apply and for messages to begin sending. For Canvas V1, if the Full Step includes a one day delay, then the message would send on the second day at the set Intelligent Timing. 

As an example, let's say on April 12, we have a Delay component set to send a user to the next component after one day using Intelligent Timing. A user enters the component at 2:01pm on April 13, and Intelligent Timing for the given message channel is 2pm. 
- For Canvas V1, the user would receive the message at 2pm on April 14, which is less than one day from the entry time. 
- For Canvas Flow, the user would receive the message at 2pm on April 15 instead, which is more than one day from the entry time.

Note that if Intelligent Timing is turned on, the message will be sent within 24 hours of the user entering the Message component at the intelligent time identified (even if no Delay step is involved).

### Exception events

#### Quiet Hours

Exception event functionality in Canvas Flow is applied using Action Paths, which are separate from Message Steps. Quiet Hours are enforced in the Message component. This means that if a user already passed the Action Path (and was not excluded with the exception event there), then hit quiet hours when they got to the Message component, and had their Canvas configured such that the message re-sends after the Quiet Hours period, the exception event will no longer be applied. Note that this use case is not common.

For Segments and filters, the Canvas Flow Message component has a new feature called Delivery Validations that allows users to configure additional Segments and filters that are validated at send-time. This prevents the aforementioned Quiet Hours edge case.

#### "In" or "On the next" schedule setting

Exception events in Canvas Flow are created using Action Paths. Action Paths only support “after a X time window” and not “in X time” or “on the next X time".


[1]: {% image_buster /assets/img_archive/canvas_v2_experience.png %}
