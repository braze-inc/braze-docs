---
nav_title: FAQs
article_title: Canvas FAQs
page_order: 8
alias: "/canvas_v2_101/"
description: "This article provides answers to frequently asked questions about Canvas and Canvas Flow."
tool: Canvas

---

# Canvas FAQs

> This article provides answers to some frequently asked questions about Canvas and [Canvas Flow](#canvas-flow).

## General

### What happens if the audience and send time are identical for a Canvas that has one variant, but multiple branches?

We enqueue a job for each step—they run at around the same time, and one of them "wins". In practice, this may be sorted somewhat evenly, but it's likely to have at least a slight bias toward the step that was created first. 

Moreover, we can't make any guarantees about exactly what that distribution will look like. If you want to ensure an even split, add a [Random Bucket Number]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/ab_testing_with_random_buckets/) filter to ensure it.

### What happens when you stop a Canvas?

When you stop a Canvas, the following applies:

- Users will be prevented from entering the Canvas.
- No further messages will be sent out, despite where a user is in the flow.
- **Exception:** Email Canvases will not immediately stop. Once the send requests go to SendGrid, there is nothing we can do to stop them from being delivered to the user.

{% alert note %}
Stopping a Canvas won't cause users who are waiting to receive messages to exit the user journey. If you re-enable the Canvas and users are still waiting for the message, they will receive it (unless the time they should've been sent the message has passed, then they won't receive it).
{% endalert %}

### When does an exception event trigger?

[Exception events]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exception_events/) only trigger while the user is waiting to receive the Canvas component it's associated with. If a user performs an action in advance, the exception event will not trigger.

If you want to except users who have performed a certain event in advance, use [filters]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/) instead.

### How does editing a Canvas affect users already in the Canvas?

If you edit some of the steps of a multi-step Canvas, users who were already in the audience but have not received the steps will receive the updated version of the message. Note that this will only happen if they haven't been evaluated for the step yet.

For more information on what you can or can't edit after launch, check out [Changing Your Canvas After Launch]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/change_your_canvas_after_launch/).

### How are user conversions tracked in a Canvas?

A user can only convert once per Canvas entry. Conversions are assigned to the most recent message received by the user for that entry. The summary block at the beginning of a Canvas reflects all conversions performed by users within that path, whether or not they received a message. Each subsequent step will only show conversions that happened while that was the most recent step the user received.

{% details Examples %}

**Example 1**

There is a Canvas path with 10 push notifications and the conversion event is "session start" ("Opens App"):

- User A opens the app after entering but before receiving the first message.
- User B opens the app after each push notification.

**Result:** The summary will show two conversion while the individual steps will show a conversion of one on the first step and zero for all subsequent steps.

{% alert note %}
If Quiet Hours is active when the conversion event happens, the same rules apply.
{% endalert %}

**Example 2**

There is a one-step Canvas with Quiet Hours enabled:

1. User enters the Canvas.
2. The first step doesn't have a delay, but is within the set Quiet Hours, so the message is suppressed.
3. User performs the conversion event.

**Result:** The user will count as converted in the overall Canvas variant, but not the step since they didn't receive the step.

{% enddetails %}

### What is the difference between the different conversion rate types?

- Total canvas conversions reflects how many unique users completed a conversion event, not how many conversions they each completed. 
- Variant conversion rate or summary block at the beginning of a Canvas reflects all conversions performed by users within that path, whether or not they received a message, as an aggregate total. 
- Step conversion rate reflects how many individuals received that message step and completed any of the outlined conversion events.

### How can I view analytics for each of my Canvas components?

To view the analytics of a Canvas component, go to your Canvas and scroll down the **Canvas Details** page. Here, you can view each component's analytics. Check out [Canvas analytics]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/) for more details.

### When looking at the number of unique users, is Canvas analytics or the segmenter more accurate?

The segmenter is a more accurate statistic for unique user data versus Canvas or campaign stats. This is because Canvas and campaign statistics are numbers that Braze increments when something happens—which means there are variables which could result in this number being different than that of the segmenter. For example, users can convert more than once for a Canvas or campaign.

### Why does the number of users entering a Canvas not match the expected number?

The number of users entering a Canvas may differ from your expected number because of how audiences and triggers are evaluated. In Braze, an audience is evaluated before the trigger (unless using a [change in attribute]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/attribute_triggers/#change-custom-attribute-value) trigger). This will cause users to drop out of the Canvas if not part of your selected audience before any trigger actions are evaluated.

### Why is my Canvas step conversion rate not equal to my Canvas variant total conversion rate?

It’s common for a Canvas variant’s conversion total to be greater than the sum of its step total. This occurs because a user can perform a conversion event for a variant as soon as they enter the variant. However, this same conversion event doesn't count toward a Canvas step. So, any user who enters the Canvas, and performs the conversion event before receiving the first Canvas step, will be counted towards the variant conversion total, and not towards the step total. The same is true for a user who enters the Canvas but exits the Canvas before receiving any step.

### How are Canvas audiences evaluated? 

By default, filters and segments for full steps in the Canvas are checked at send time. For Canvas Flow, the Decision Split component performs an evaluation right after receiving a previous step (or before a delay).

## Canvas Flow

### What is Canvas Flow?

Canvas Flow is the new and improved editing experience that simplifies how marketers can build and manage their Canvas user journeys. You can expect to easily view and use Canvas components in the Canvas builder. You also have access to more post-launch edit capabilities to edit connections between steps, delete steps and variants, and redirect users to different steps.

### How can I use Canvas Flow?

To use the Canvas Flow workflow, go to **Canvas** under the **Engagement** tab. Click <i class="fas fa-plus"></i> **Create Canvas**. Next, you'll have the option of building with Canvas Flow or the original Canvas experience. Select **Canvas Flow Workflow** and begin building your Canvas as you normally would!

### What's the difference between a component and a step?

A [component]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components) is an individual part of your Canvas that you can use to determine the effectiveness of your Canvas. Components can include actions such as splitting your user journey, adding a delay, and even testing multiple Canvas paths. A step in Canvas refers to the personalized user journey in your Canvas branches. Essentially, your Canvas is made of individual components that create steps for your user journey.

### Can I use Full Steps in Canvas Flow?

No. In Canvas Flow, Full Steps are replaced with lightweight [Canvas components]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components). You can also leverage [persistent entry properties]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_persistent_entry_properties/) for message personalization throughout a user journey.

### How do I convert an existing Canvas into Canvas Flow?

You can [clone your Canvas to Canvas Flow]({{site.baseurl}}/cloning_canvases/). This creates a copy of your original Canvas in the Canvas Flow workflow.

### Can I revert back to the original Canvas editor?

As you’re building or editing your Canvas, if you ever want to switch back to the original Canvas editor, click **Switch to original workflow** at the bottom of the Canvas composer or at the top of the Canvas builder. 

{% alert important %}
Switching from Canvas Flow to the original Canvas editor is allowed only if you do not use Canvas Flow features, and will only work if there are no full steps in your Canvas.
{% endalert %}

### What will happen to my Canvases that I created using the original editor?

All of your existing Canvases and the original Canvas editor will continue to exist and be supported by Braze. Customers who choose to join Canvas Flow for early access will have the option of creating a Canvas using either the original or Flow workflow.

### Is there a limit for how many steps I can include?

Yes. A Canvas built using Canvas Flow can contain up to 200 steps.

### Can I launch a Canvas with disconnected steps?

Yes! Canvas Flow allows you to launch your Canvas with disconnected steps. You can also save Canvases post-launch with disconnected steps. 

### Where do users go once they've reached a disconnected step?

If a user is in a disconnected step of your Canvas Flow workflow, they will advance to the subsequent step if there is one, and the step's setting will dictate how the user should advance. This is intended to allow users to make changes to steps without having to directly connect them to the rest of the Canvas. This also gives you some room for testing before going live immediately, effectively allowing for saving a draft.

We recommend checking the analytics view for users pending in a Canvas step before disconnecting a step.

### What are the main differences between Canvas Flow and the original Canvas editor?

#### Canvas Component Toolbar

Previously with the original Canvas editor, a full step was added by default whenever you created any step in your user journey. Now with Canvas Flow, these full steps are replaced by different Canvas components, which gives you the benefit of increased visibility and customization for your editing experience. You can immediately see all your Canvas components from the Canvas Step Toolbar.

#### Step behavior

Previously, each full step included information such as delay and schedule settings, exception events, audience filters, message configuration, and message advancement options all in one component. These are separate settings in Canvas Flow to make your Canvas building experience more customizable and introduces some differences in functionality.

#### Message component advancement

[Message components]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) advance all users who enter the step. There is no requirement to specify message advancement behavior, making configuring the overall step simpler. If you want to implement the **Advance when message sent** option, add a separate Audience Paths to filter users that didn't receive the previous step.  

#### Delay "in" behavior

[Delay components]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/) will wait the entire delay time before proceeding to the next step. 

Let's say on April 12 we have a Delay component where the delay is set to send your user to the next step in one day at 2 pm. A user enters the component at 2:01 pm on April 13. 
- For the original workflow, the user would proceed to the next step at 2 pm on April 14, which is less than one day from the entry time. 
- For Canvas Flow, the user would proceed to the next step at 2 pm on April 15. Note that this is the same time, but more than one day from the entry time. 

#### Intelligent Timing behavior

Since [Intelligent Timing]({{site.baseurl}}/user_guide/intelligence/intelligent_timing/) is stored in the Message component, delays will be applied prior to Intelligent Timing calculations. This means that, depending on when a user enters the component, they may receive the message later than they would in a Canvas built with the original Canvas workflow.

Let’s say your delay is set for 2 days, Intelligent Timing is turned on, and it has determined that the best time to send your message is 2 pm. A user enters the Delay step at 2:01 pm.
- **Canvas Flow:** It will take 48 hours for the delay to pass, so the user receives the message on the third day at 2 pm.
- **Original workflow:** The user receives the message on the second day at 2 pm.

Note that if Intelligent Timing is turned on, the message will be sent within 24 hours of the user entering the Message component at the intelligent time identified (even if no Delay component is involved).

#### Exception events

##### Quiet Hours

Exception event functionality in Canvas Flow is applied using Action Paths, which are separate from Message steps. Quiet Hours are enforced in the Message component. This means that if a user already passed the Action Path (and was not excluded with the exception event there), then hit Quiet Hours when they got to the Message component, and had their Canvas configured such that the message re-sends after the Quiet Hours period, the exception event will no longer be applied. Note that this use case is not common.

For segments and filters, the Canvas Flow Message component has a new feature called Delivery Validations that allows users to configure additional segments and filters that are validated at send-time. This prevents the aforementioned Quiet Hours edge case.

##### "In" or "On the next" schedule setting

Exception events in Canvas Flow are created using Action Paths. Action Paths only support “after a X time window” and not “in X time” or “on the next X time".
