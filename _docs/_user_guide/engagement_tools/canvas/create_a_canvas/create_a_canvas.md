---
nav_title: Creating a Canvas
article_title: Creating a Canvas
page_order: 0
page_type: reference
description: "This reference article covers the necessary steps involved in creating, maintaining, and testing a Canvas."
tool: Canvas
search_rank: 1
---

# Creating a Canvas

> This reference article covers the necessary steps involved in creating, maintaining, and testing a Canvas. Follow this guide, or check out our [Canvas Braze Learning course](https://learning.braze.com/quick-overview-canvas-setup).

{% details Original Canvas editor %}
You can no longer create or duplicate Canvases using the original Canvas experience. Braze recommends [cloning your Canvases]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/cloning_canvases/) to the most current editor.
{% enddetails %}

## Creating a Canvas

### Step 1: Set up a new Canvas 

First, go to **Messaging** > **Canvas**, then select **Create Canvas**.

The Canvas builder will guide you step-by-step through setting up your Canvas—everything from naming it to setting conversion events and bringing the right users into your customer journey. Select each of the following tabs to view which settings you can adjust for each builder step.

{% tabs local %}
  {% tab Basics %}
    Here, you will set up the basics of your Canvas:
    - Name your Canvas
    - Add teams
    - Add tags
    - Assign conversion events, and choose their event types and deadlines

    Learn more about the [Basics step](#step-2a-set-up-your-canvas-basics).
  {% endtab %}
  {% tab Entry Schedule %}
    Here, you will decide how and when your users will enter your Canvas:
    - Scheduled: This is a time-based Canvas entry
    - Action-Based: Your user will enter your Canvas after they perform a defined action
    - API-Triggered: Use an API request to enter users into your Canvas

    Learn more about the [Entry Schedule step](#step-2b-determine-your-canvas-entry-schedule).
  {% endtab %}
  {% tab Target Audience %}
    Here, you will select your target audience:
    - Create your audience by adding segments and filters
    - Fine-tune Canvas re-entry and entry limits
    - See a summary of your target audience

    Learn more about the [Target Audience step](#step-2c-set-your-target-entry-audience).
  {% endtab %}
  {% tab Send Settings %}
    Here, you will select your Canvas Send Settings:
    - Select your subscription settings
    - Set a send rate limit for your Canvas messages
    - Enable and set Quiet Hours

    Learn more about the [Send Settings step](#step-2d-select-your-send-settings).
  {% endtab %}
  {% tab Build Canvas %}
    Here, you will build your Canvas.

    Learn how to [build your Canvas](#step-3-build-your-canvas) using the Canvas builder.
  {% endtab %}
  {% tab Summary %}
    Here, you will find the summary of your Canvas details. If you have the [Canvas approval workflow]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals/) turned on, you can approve the listed Canvas details before launching.

  {% endtab %}
{% endtabs %}

#### Step 1.1: Start with your Canvas basics

Here, you'll name your Canvas, assign [Teams]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/teams/#teams), and create or add [Tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/#tags). You can also assign conversion events for the Canvas.

{% alert tip %}
Tag your Canvases so they're easy to find and build reports out of. For instance, when using [Report Builder]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/), you can filter by particular tags.
{% endalert %}

![The Canvas details page, with fields for the Canvas name, description, location, and tags.]({% image_buster /assets/img/canvas_details.png %}){: style="max-width:70%;"}

##### Choose conversion events

Choose your conversion event type, then select the conversions to record. These [conversion events]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/) will measure the efficiency of your Canvas. 

![Primary Conversion Event A with the Makes Purchase conversion event type to record conversations for users who make any purchase within a three day conversion deadline.]({% image_buster /assets/img/add_canvas_conversions.png %})

If your Canvas has multiple variants or a control group, Braze will use this conversion event to determine the best variation for achieving this conversion goal. Using the same logic, you can create multiple conversion events.

#### Step 1.2: Determine your Canvas entry schedule

You can choose one of three ways in which users can enter your Canvas. 

##### Entry schedule types

{% tabs local %}
  {% tab Scheduled Delivery %}
    With scheduled delivery, users will enter on a time schedule, similarly to how you would schedule a campaign. You can enroll users in a Canvas as soon as it is launched, enter them into your journey at some point in the future, or on a recurring basis (daily, weekly, or monthly). 

    In this example, based on the time-based options, users will enter this Canvas every Tuesday at 12 pm in their local time zone every week, beginning November 14, 2025 until December 31, 2025.

    ![The "Entry Schedule" page with the type set to "Scheduled". Due to the selection, time-based options are shown, including frequency, start time, recurrence, days, and more.]({% image_buster /assets/img_archive/Canvas_Scheduled_Delivery.png %})
  {% endtab %}
  {% tab Action-Based Delivery %}
    With action-based delivery, users will enter the Canvas and begin receiving messages when they take particular actions, such as opening your app, making a purchase, or triggering a custom event.

    You can control other aspects of the Canvas behavior from the **Entry Audience** window, including rules for re-eligibility and frequency capping settings. Note that action-based delivery is unavailable for Canvas components with in-app messages.

    ![An example of action-based delivery. Users will enter the Canvas if they make a purchase with an entry window beginning at 1:30 pm on June 10, 2025.]({% image_buster /assets/img_archive/Canvas_Action_Based_Delivery.png %})

  {% endtab %}
  {% tab API-Triggered Delivery %}
    With API-triggered delivery, users will enter your Canvas and begin receiving messages after they have been added using the [`/canvas/trigger/send` endpoint]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/) via the API. In the dashboard, you can find an example cURL request that does this as well as assign optional [`canvas_entry_properties`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/) using the [Canvas entry properties object]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/). 

    ![An example of API-triggered delivery with a Canvas ID and an example of a cURL request.]({% image_buster /assets/img_archive/Canvas_API_Triggered_Delivery.png %})

    You can use the following endpoints for API-triggered delivery:
    - [POST: Send Canvas Messages via API-Triggered Delivery]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)
    - [POST: Schedule API-Triggered Canvases]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases/)
    - [POST: Update Scheduled API-Triggered Canvases]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases/)

  {% endtab %}
{% endtabs %}

After selecting your delivery method, adjust the settings to match your use case, then continue to setting your target audience.

{% details Deduplicate behavior for Canvases using the original editor %}
Should the window of re-eligibility be less than the maximum duration of the Canvas, a user will be allowed to re-enter and receive more than one component's messages. In the edge case where a user's re-entry reaches the same component as its previous entry, Braze will deduplicate that component's messages. 

If a user re-enters the Canvas, reaches the same component as their previous entry, and is eligible for an in-app message for each entry, the user will get the message twice (depending on in-app message priority) as long as they re-open a session two times.
{% enddetails %}

#### Step 1.3: Set your target entry audience

Only the users who match your defined criteria can enter the journey in the **Target Audience** step, meaning Braze evaluates the target audience for eligibility first **before** users enter the Canvas journey. For example, if you want to target new users, you can select a segment of users who first used your app less than a week ago.

In **Entry Controls**, you can limit the number of users every time the Canvas is scheduled to run. For API trigger-based and action-based Canvases, this limit occurs at every UTC hour. 

{% alert important %}
Avoid configuring an action-based campaign or Canvas with the same trigger as the audience filter (such as a changed attribute or performed a custom event). A [race condition]({{site.baseurl}}/user_guide/engagement_tools/testing/race_conditions) may occur in which the user is not in the audience at the time they perform the trigger event, which means they won't receive the campaign or enter the Canvas.
{% endalert %}

##### Testing your audience

After adding segments and filters to your target audience, you can test if your audience is set up as expected by [looking up a user]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/) to confirm if they match the audience criteria.

![The "User Lookup" field, which allows you to search by external user ID or Braze ID.]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:100%;"}{: style="max-width:80%;"}

##### Selecting entry controls

Entry controls determine if users are allowed to re-enter a Canvas. You can also limit the number of people who would potentially enter this Canvas by a selected cadence (daily, lifetime of the Canvas, or every time the Canvas is scheduled). 

For example, if you select **Limit entrance volume** and set the **Maximum entries** field to 5,000 users with **Daily** as the limit cadence, then the Canvas will only send to 5,000 users per day.

![The "Entry Controls" page displaying checkboxes for "Allow users to re-enter Canvas" and "Limit entrance volume". The latter allowing you to set the maximum entries and whether you'd like to limit daily, lifetime of the Canvas, or every time the Canvas is scheduled.]({% image_buster /assets/img_archive/entry_controls.png %})

{% alert tip %}
Braze doesn't recommend using the **Every time the Canvas is scheduled** feature for IP warming as this may lead to increased send volumes.
{% endalert %}

##### Setting exit criteria

Setting the [exit criteria]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exit_criteria) determines which users you want to exit a Canvas. If a user performs the exception event or matches the segments and filters, they won't receive any further messages.

##### Calculating target population

In the **Target Population** section, you can view a summary of your audience, such as your selected segments and additional filters, and a breakdown of how many users are reachable per messaging channel. To calculate the exact number of reachable users in your target audience instead of the default estimation, select [Calculate exact statistics]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment#calculating-exact-statistics).

Note that:

- Calculating exact statistics can take a few minutes to run. This function only calculates the exact statistics at the segment level, not at the filter or filter group level.
- For large segments, it is normal to see slight variation even when calculating exact statistics. The accuracy of this feature is expected to be 99.999% or greater.

To view additional statistics, such as the average lifetime revenue for targeted users, select **Show Additional Statistics**.

![Target Population breakdown with option to calculate exact statistics.]({% image_buster /assets/img_archive/canvas_exact_stats.png %})

##### Why the target audience count could differ from the reachable users count

{% multi_lang_include segments.md section='Differing audience size' %}

#### Step 1.4: Select your send settings

Select **Send Settings** to edit your subscription settings, turn on rate limiting, and to turn on Quiet Hours. By turning on [rate limiting]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#rate-limiting-and-canvas-components) or [frequency capping]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting#frequency-capping), you can ease the marketing pressure placed on your users and ensure you aren't over messaging them.

For Canvases targeting email and push channels, you may want to limit your Canvas so that only the users who are explicitly opted in will receive the message (excluding subscribed or unsubscribed users). For example, say you have three users of different opt-in status:

- **User A** is subscribed to email and is push enabled. This user doesn't receive the email but will receive the push.
- **User B** is opted-in to email but is not push enabled. This user will receive the email but doesn't receive the push.
- **User C** is opted-in to email and is push enabled. This user will receive both the email and the push.

To do so, set the **Subscription Settings** to send this Canvas to "opted-in users only". This option will ensure that only opted-in users will receive your email, and Braze will only send your push to users who are push enabled by default. 

These subscription settings are applied on a per-step basis, meaning that there is no effect on the entry audience. So, this setting is used to evaluate a user's eligibility to receive each Canvas step.

{% alert important %}
With this configuration, don't include any filters in the **Target Audience** step that limits the audience to a single channel (for example, `Foreground Push Enabled = True` or `Email Subscription = Opted-In`).
{% endalert %}

If desired, specify Quiet Hours (the time during which your messages will not be sent) for your Canvas. Check **Enable Quiet Hours** in your **Send Settings**. Then, select your Quiet Hours in your user's local time and what action will follow if the message triggers inside of those Quiet Hours.

![The "Quiet Hours" page displaying a checkbox for enabling quiet hours. If enabled, the start time, end time, and fallback behavior can be set.]({% image_buster /assets/img/quiet_hours.png %})

### Step 2: Build your Canvas

{% alert tip %}
Save time and streamline your Canvas creation by using [Braze Canvas templates]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_templates/#available-braze-templates)! Browse our library of pre-built templates to find one that fits your use case and customize it to meet your specific needs.
{% endalert %}

#### Step 2.1: Add a variant

![The "Add Variant" button selected to show a context menu with the option to "Add Variant".]({% image_buster /assets/img_archive/canvas_add_variant.gif %}){: style="float:right;max-width:40%;margin-left:15px;"}

Select **Add Variant**, then add a new variant to your Canvas. Variants represent a journey that your users will take and can contain multiple steps and branches.

You can add additional variants by selecting the <i class="fas fa-plus-circle"></i> plus button. When you add new variants, you'll be able to adjust how your users will be distributed between them so that you can cross-compare and analyze the efficacy of different engagement strategies.

![Two example variants in a Braze Canvas.]({% image_buster /assets/img_archive/Canvas_Multiple_Variants.png %})

{% alert tip %}
By default, the Canvas variant assignment is locked in when users enter the Canvas, meaning that if a user first enters a variant, that will be their variant every time they re-enter the Canvas. However, there are ways to circumvent this behavior. <br><br>To do so, you can create a random number generator using Liquid, run it at the beginning of each user's Canvas entry, store the value as a custom attribute, and then use that attribute to randomly divide users.

{% details Expand for steps %}

1. Create a custom attribute to store your random number. Name it something easy to locate, like "lottery_number" or "random_assignment". You can create the attribute either [in your dashboard]({{site.baseurl}}/user_guide/data/custom_data/managing_custom_data/), or through API calls to our [`/users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/).<br><br>
2. Create a webhook campaign at the beginning of your Canvas. This campaign will be the medium in which you create your random number and store it as a custom attribute. Refer to [Creating a webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#step-1-set-up-a-webhook) for more. Set the URL to our `/users/track` endpoint.<br><br>
3. Create the random number generator. You can do so with the code [ outlined here](https://community.shopify.com/c/technical-q-a/is-there-any-way-to-generate-random-number-with-liquid-shopify/m-p/1595486), which takes advantage of each user's unique time of entry to create a random number. Set the resulting number as a Liquid variable within your webhook campaign.<br><br>
4. Format the `/users/track` call on your webhook campaign so that it sets the custom attribute you created in step 1 to the random number you've generated on your current user's profile. When this step runs, you will have successfully made a random number that changes each time a user enters your campaign.<br><br>
5. Adjust the branches of your Canvas so that, instead of being divided by randomly chosen variants, they are divided based on audience rules. In the audience rules of each branch, set the audience filter according to your custom attribute. <br><br>For example, one branch may have "lottery_number is less than 3" as an audience filter, while another branch may have "lottery_number is more than 3 and less than 6" as an audience filter.

{% enddetails %}
{% endalert %}

#### Step 2.2: Add Canvas steps

You can add more steps to your Canvas workflow by dragging and dropping components from the **Components** sidebar. Or, select the <i class="fas fa-plus-circle"></i> plus button to add a component with the popover menu.

{% alert tip %}
As you begin to add more steps, you can switch up the zoom level to focus in on details or take in the entire user journey. Zoom in with <kbd>Shift</kbd> + <kbd>+</kbd> or zoom out with <kbd>Shift</kbd> + <kbd>-</kbd>.
{% endalert %}

![The component search window adding a delay step to the Braze Canvas.]({% image_buster /assets/img_archive/add_components_flow.png %}){: style="max-width:80%;"}

{% alert important %}
You can add up to 200 steps in a Canvas. If your Canvas exceeds 200 steps, loading issues may occur.
{% endalert %}

##### Maximum duration

As your Canvas journey increases in steps, the maximum duration is the longest possible time a user can take to complete this Canvas. This is calculated by adding the delays and trigger windows of each step for each variant for the longest path. For example, if your Canvas has a Delay step with a delay of 3 days and a Message step, the maximum duration of your Canvas will be 3 days.

##### Editing a step

Looking to edit a step in your user journey? Check out how to do this depending on your Canvas workflow!

You can edit any step in your Canvas workflow by selecting any of the components. For example, let's say you want to edit your first step, a [Delay]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/) component, in your workflow to a specific day. Select the step to view its settings and adjust your delay to March 1. This means on March 1, your users will move to the next step in your Canvas.

![An example "Delay" step with the delay set to "Until a specific day."]({% image_buster /assets/img_archive/edit_delay_flow.png %})

Or you can quickly edit and adjust the **Action Settings** of your [Action Paths]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) step to hold users for a window of time. This prioritizes their next path based on the actions during this evaluation period.

![The second step in the canvas, "Action Settings", with an evaluation window set to 1 day.]({% image_buster /assets/img_archive/action_paths_flow.png %})

The lightweight components in Canvas allow for a simple editing experience, so adjusting the finer details of your Canvas is made easier. 

##### Messages in Canvas

Edit the messages in a Canvas component to control messages that a particular step will send. Canvas can send email, mobile, and web push messages, and webhooks to integrate with other systems. Similar to campaigns, you can use certain [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/) templating to personalize your messages.

{% alert tip %}
Did you know you can include Canvas component names in your messages and link templates?<br>
Use the `campaign.${name}` Liquid tag in Canvas to display the current Canvas component name.
{% endalert %}

The Message component manages the messages sent to users. You can select your **Messaging Channels** and adjust **Delivery Settings** to optimize your Canvas messaging. For more details on this component, check out [Message]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/).

![The "Set up Messages" step, with "Messaging Channels" selected which displays the list of available messaging channels, such as android push, content cards, email, and more.]({% image_buster /assets/img_archive/message_setup_settings_flow.png %})

Select **Done** after you've finished configuring your Canvas component.

{% tabs local %}
{% tab Canvas Entry Properties %}

The `canvas_entry_properties` are configured in the Entry Schedule step of creating a Canvas and indicate the trigger that enters a user into a Canvas. These properties can also access the properties of entry payloads in API-triggered Canvases. Note that the `canvas_entry_properties` object can be up to 50 KB. 

Use the following Liquid when referencing these entry properties: {% raw %} ``canvas_entry_properties.${property_name}`` {% endraw %}. Note that the events must be custom events or purchase events to be used this way.

{% raw %}
For example, consider the following request: `\"canvas_entry_properties\" : {\"product_name\" : \"shoes\", \"product_price\" : 79.99}`. You could add the word "shoes" to a message with this Liquid ``{{canvas_entry_properties.${product_name}}}``.
{% endraw %}

{% endtab %}

{% tab Event Properties %}
Event properties are the properties set by you on custom events and purchases. These `event_properties` can be used in campaigns with action-based delivery as well as Canvases. 

In Canvas, custom event and purchase event properties can be used in Liquid in any Message step that follows an Action Paths step. Use this Liquid {% raw %} ``{{event_properties.${property_name}}}`` {% endraw %} when referencing these `event_properties`. These events must be custom events or purchase events to be used this way in the Message component.

In the first Message step following an Action Path, you can use `event_properties` related to the event referenced in that Action Path. You can have other steps (that are not another Action Paths or Message step) in between this Action Paths step and the Message step. Note that you'll only have access to `event_properties` if your Message step can be traced back to a non-Everyone Else path in an Action Path step

{% endtab %}
{% endtabs %}

#### Step 2.3: Edit connections

To move a connection between steps, select the arrow connecting the two components and select a different component. To remove the connection, select the arrow followed by **Cancel Connection** in the footer of the Canvas composer.

### Step 3: Add a control group

You can add a control group to your Canvas by selecting the <i class="fas fa-plus-circle"></i> plus button to add a new variant. 

Braze will track the conversions for users who are placed into the control group, although they will not receive any messages. To preserve an accurate test, we will track the number of conversions for your variants and the control group for exactly the same amount of time, as shown on the conversion event selection screen. 

You can adjust the distribution between your messages by double-clicking the **Variant Name** headers.

In this example, we have our Canvas divided into two variants. Variant 1 has 70% of the users. The second variant is a control group with the remaining 30% of users.

![An example variant in a Braze Canvas, where 70% go to "Variant 1", which delays for 1 day in the first step, then sends a message in the second step. The other 30% go to a "Control" that does not have any follow-up steps.]({% image_buster /assets/img_archive/Canvas_Multivariate_Flow.png %})

#### Intelligent Selection for Canvas

Intelligent Selection capabilities are now available within multivariate Canvases. Similar to the [Intelligent Selection]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/) feature for multivariate Campaigns, Intelligent Selection for Canvas analyzes the performance of each Canvas variant and adjusts the percentage of users being funneled through each variant. This distribution is based on each variant's performance metrics to maximize the total expected number of conversions.

Keep in mind that multivariate Canvases allow you to test more than copy, but timing and channels as well. Through Intelligent Selection, you can test Canvases more efficiently and have confidence that your users will be sent on the best possible Canvas journey.

![The "Intelligent Selection" option is enabled in the "Edit Variant Distribution" page. As it analyzes and optimizes the Canvas, it displays a horizontal bar across the page that's split into several sections, each varying in color and size. This is only a visual representation and does not correlate to any specific analytics.]({% image_buster /assets/img_archive/canvas_intelligent_selection.png %})

Intelligent Selection for Canvas optimizes your Canvas results by making gradual real-time adjustments to the distribution of users sorted into each variant. When the statistical algorithm determines a decisive winner among your variants, it will rule out the underperforming variants and slot all future eligible recipients of the Canvas into the Winning Variants. 

For this reason, Intelligent Selection works best on Canvases that have new users entering frequently.

### Step 4: Save and launch

After you're done creating your Canvas, select **Launch Canvas** to save and launch your Canvas. After you've launched your Canvas, you'll be able to view analytics for your journey as they come in on the **Canvas Details** page. 

You can also save your Canvas as a draft if you need to come back to it.

![An example Canvas in Braze.]({% image_buster /assets/img_archive/Canvas_Analytics.png %})

{% alert tip %}
Need to make edits to your Canvas after launch? Well, you can! Check out [Editing Canvases after launch]({{site.baseurl}}/post-launch_edits/) for more information.
{% endalert %}

