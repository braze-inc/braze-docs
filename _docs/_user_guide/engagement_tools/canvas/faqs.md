---
nav_title: FAQ
article_title: Canvas FAQ
page_order: 8
alias: "/canvas_v2_101/"
description: "This article provides answers to frequently asked questions about Canvas."
tool: Canvas

---

# Frequently asked questions

> This article provides answers to some frequently asked questions about Canvas.

### How many steps I can include in a Canvas?

You can add up to 200 steps in a Canvas.

### What happens if the audience and send time are identical for a Canvas that has one variant, but multiple branches?

We enqueue a job for each step—they run at around the same time, and one of them "wins". In practice, this may be sorted somewhat evenly, but it's likely to have at least a slight bias toward the step that was created first. 

Moreover, we can't make any guarantees about exactly what that distribution will look like. If you want an even split, add a [Random Bucket Number]({{site.baseurl}}/user_guide/engagement_tools/testing/random_bucket_numbers/) filter.

### Can I launch a Canvas with disconnected steps?

Yes. You can also save Canvases post-launch with disconnected steps. 

### Where do users go when they've reached a disconnected step?

If a user is in a disconnected step of your Canvas workflow, they will advance to the subsequent step if there is one, and the step's setting will dictate how the user should advance. This is intended to allow users to make changes to steps without having to directly connect them to the rest of the Canvas. This also gives you some room for testing before going live immediately, effectively allowing for saving a draft.

We recommend checking the analytics view for users pending in a Canvas step before disconnecting a step.

### What happens when you stop a Canvas?

When you stop a Canvas, the following applies:

- Users will be prevented from entering the Canvas.
- No further messages will be sent out, despite where a user is in the flow.
- **Exception:** Canvases with emails will not immediately stop. After the send requests go to SendGrid, there is nothing we can do to stop them from being delivered to the user.

### Should I build one Canvas or separate Canvases per user lifecycle?

Depending on what you’re looking to accomplish with your Canvas, you may need different approaches in how you build your user journey. The flexibility of Canvas allows you to map user journeys for any stage of the user lifecycle. Check out our [Braze Canvas templates]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates) for several examples of streamlined approaches to creating effective user journeys.

### When are in-app messages in Canvas sent?

In-app messages are sent upon the next session start. This means if the user enters the Canvas step before the Canvas is stopped, they'll still receive the in-app message upon their next session start as long as the in-app message hasn't expired yet.

It's possible for a user to start a session before the Canvas is stopped, but not be shown the in-app message immediately. This can occur if the in-app message is triggered by a custom event or is delayed. This means it's possible for a user to log an in-app message impression and "receive" the in-app message after the Canvas is stopped. However, the user would have had to start the session before the Canvas was stopped, but **after** they received the Canvas step.

{% alert note %}
Stopping a Canvas won't cause users who are waiting to receive messages to exit the user journey. If you re-enable the Canvas and users are still waiting for the message, they'll receive it (unless the time they should've been sent the message has passed, then they won't receive it).
{% endalert %}

### When does an exception event trigger?

Exception events only trigger while the user is waiting to receive the Canvas component it's associated with. If a user performs an action in advance, the exception event will not trigger. If you want to exclude users who have performed a certain event in advance, use [filters]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/) instead.

### How does editing a Canvas affect users already in the Canvas?

If you edit some of the steps of a multi-step Canvas, users who were already in the audience but have not received the steps will receive the updated version of the message. Note that this will only happen if they haven't been evaluated for the step yet.

For more information on what you can edit after launch, refer to [Changing your Canvas after launch]({{site.baseurl}}/post-launch_edits/).

### How are user conversions tracked in a Canvas?

A user can only convert once per Canvas entry. Conversions are assigned to the most recent message received by the user for that entry. The summary block at the beginning of a Canvas reflects all conversions performed by users within that path, whether or not they received a message. Each subsequent step will only show conversions that happened while that was the most recent step the user received.

{% details Expand for examples %}

**Example 1**

There is a Canvas path with 10 push notifications and the conversion event is "session start" ("Opens App"):

- User A opens the app after entering but before receiving the first message.
- User B opens the app after each push notification.

**Result:** The summary will show two conversions while the individual steps will show a conversion of one on the first step and zero for all subsequent steps.

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

### What's the difference between the different conversion rate types?

- Total Canvas conversions reflect how many unique users completed a conversion event, not how many conversions they each completed. 
- Variant conversion rate or summary block at the beginning of a Canvas reflects all conversions performed by users within that path, whether or not they received a message, as an aggregate total. 
- Step conversion rate reflects how many individuals received that message step and completed any of the outlined conversion events.

### What's the difference between a component and a step?

A [component]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/about/) is an individual part of your Canvas that you can use to determine the effectiveness of your Canvas. Components can include actions such as splitting your user journey, adding a delay, and even testing multiple Canvas paths. A step in Canvas refers to the personalized user journey in your Canvas branches. Essentially, your Canvas is made of individual components that create steps for your user journey.

### How can I view analytics for each of my Canvas components?

To view the analytics of a Canvas component, go to your Canvas and scroll down the **Canvas Details** page. Here, you can view each component's analytics. Check out [Canvas analytics]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/) for more details.

### When looking at the number of unique users, is Canvas analytics or the segmenter more accurate?

The segmenter is a more accurate statistic for unique user data versus Canvas or campaign stats. This is because Canvas and campaign statistics are numbers that Braze increments when something happens—which means there are variables that could result in this number being different than that of the segmenter. For example, users can convert more than once for a Canvas or campaign.

### Why does the number of users entering a Canvas not match the expected number?

The number of users entering a Canvas may differ from your expected number because of how audiences and triggers are evaluated. In Braze, an audience is evaluated before the trigger (unless using a [change in attribute]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/attribute_triggers/#change-custom-attribute-value) trigger). This will cause users to drop out of the Canvas if not part of your selected audience before any trigger actions are evaluated.

### What happens to anonymous users during their Canvas journey?

While anonymous users can enter and exit Canvases, their actions aren't associated with a specific user profile until they're identified, so their interactions may not be fully tracked in your analytics. You can use the [Query Builder]({{site.baseurl}}/user_guide/analytics/query_builder/) to generate a report of these metrics.

### Why is my Canvas step conversion rate not equal to my Canvas variant total conversion rate?

It's common for a Canvas variant's conversion total to be greater than the sum of its step total. This occurs because a user can perform a conversion event for a variant as soon as they enter the variant. However, this same conversion event doesn't count toward a Canvas step. So, any user who enters the Canvas, and performs the conversion event before receiving the first Canvas step, will be counted  the variant conversion total, and not toward the step total. The same is true for a user who enters the Canvas but exits the Canvas before receiving any step.

### How are Canvas audiences evaluated? 

By default, filters and segments for full steps in the Canvas are checked at send time. The Decision Split step performs an evaluation right after receiving a previous step (or before a delay).

{% alert tip %}
For further assistance with Canvas troubleshooting, be sure to contact Braze Support within 30 days of your issue's occurrence as we only have the last 30 days of diagnostic logs.
{% endalert %}

### What is the difference between "Has not entered Canvas variation" and "Is not in Canvas control group"?

Refer to [Segmentation Filters]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters) for full filter definitions.

#### Has not entered Canvas variation

The user never entered a variation path of a specific Canvas. All users who aren't in the control group are included, regardless of whether they have entered the Canvas. This includes users who entered another variation and users who haven't entered any variation. 

#### Is not in Canvas control group

The user entered the Canvas, but isn't in the control group and consequently received a variation. This only includes users who entered the Canvas.

Note that variation assignment occurs at Canvas entry. If a user hasn't entered a Canvas, they won't be assigned any variant. In other words, they won't be in the control group or a variant.

{% details Expand for original Canvas editor FAQs %}

### How do I convert an existing Canvas from the original editor to the current editor?

You can [clone your Canvas]({{site.baseurl}}/cloning_canvases/). This creates a copy of your original Canvas in the most current Canvas workflow.

### What are the main differences between the current and original Canvas editors?

#### Canvas component toolbar

Previously with the original Canvas editor, a full step was added by default whenever you created any step in your user journey. These full steps are replaced by different Canvas components, which gives you the benefit of increased visibility and customization for your editing experience. You can immediately see all your Canvas components from the Canvas Step Toolbar.

#### Step behavior

Previously, each full step included information such as delay and schedule settings, exception events, audience filters, message configuration, and message advancement options all in one component. These are separate settings in the current editor to make your Canvas building experience more customizable and introduces some differences in functionality.

#### Message component advancement

[Message components]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) advance all users who enter the step. There is no requirement to specify message advancement behavior, making configuring the overall step simpler. If you want to implement the **Advance when message sent** option, add a separate Audience Paths to filter users that didn't receive the previous step.  

#### Delay "in" behavior

[Delay components]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/) will wait the entire delay time before proceeding to the next step. 

Let's say on April 12 we have a Delay component where the delay is set to send your user to the next step in one day at 2 pm. A user enters the component at 2:01 pm on April 13. 
- For the original workflow, the user would proceed to the next step at 2 pm on April 14, which is less than one day from the entry time. 
- In the current editor, the user would proceed to the next step at 2 pm on April 15. Note that this is the same time, but more than one day from the entry time. 

#### Intelligent Timing behavior

Since [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/) is stored in the Message component, delays will be applied prior to Intelligent Timing calculations. This means that, depending on when a user enters the component, they may receive the message later than they would in a Canvas built with the original Canvas workflow.

Let's say your delay is set for 2 days, Intelligent Timing is turned on, and it has determined that the best time to send your message is 2 pm. A user enters the Delay step at 2:01 pm.
- **Current workflow:** It will take 48 hours for the delay to pass, so the user receives the message on the third day at 2 pm.
- **Original workflow:** The user receives the message on the second day at 2 pm.

Note that if Intelligent Timing is turned on, the message will be sent within 24 hours of the user entering the Message component at the intelligent time identified (even if no Delay component is involved).

#### Exception events

##### Quiet Hours

Exception event is applied using Action Paths, which are separate from Message steps. Quiet Hours are enforced in the Message component. This means that if a user already passed the Action Path (and wasn't excluded with the exception event), then encounters Quiet Hours when they got to the Message component, and had their Canvas configured such that the message re-sends after the Quiet Hours period, the exception event will no longer be applied. Note that this use case is not common.

For segments and filters, the Message step has delivery validations that allows users to configure additional segments and filters that are validated at send-time. This prevents the aforementioned Quiet Hours edge case.

##### "In" or "On the next" schedule setting

Exception events are created using Action Paths. Action Paths only support "after an X time window" and not "in X time" or "on the next X time".

{% enddetails %}