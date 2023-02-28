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

> This reference article covers the necessary steps involved in creating, maintaining, and testing a Canvas. Follow this guide, or check out our [Canvas Braze Learning course](https://learning.braze.com/quick-overview-canvas-setup)!

{% alert important %}
As of February 28, 2023, you will no longer be able to create or duplicate Canvases using the original Canvas experience. Braze recommends that customers who use the original Canvas experience move to Canvas Flow. It's an improved editing experience to better build and manage Canvases. Learn more about [cloning your Canvases to Canvas Flow]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/cloning_canvases/).
{% endalert %}

## Step 1: Create a new Canvas 

Go to the **Canvas** page, located under the **Engagement** section, then click **Create Canvas**.

## Step 2: Use the entry wizard to set up your Canvas

The Entry Wizard will guide you through setting up your Canvas—everything from naming it to setting conversion events and bringing the right users into your customer journey. Click on each of the following tabs to see what settings you can adjust in each of the Entry Wizard steps.

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
    Here, you will decide how your users will enter your Canvas:
    - Scheduled: This is a time-based Canvas entry
    - Action-Based: Your user will enter your Canvas after they perform a defined action
    - API-Triggered: Use an API request to enter users into your Canvas

    Learn more about the [Entry Schedule step](#step-2b-set-your-canvas-entry-schedule).
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
{% endtabs %}

### Step 2a: Set up your Canvas basics

Here, you'll name your Canvas, assign [Teams]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/teams/#teams), and create or add [Tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/#tags). You can also assign conversion events for the Canvas.

{% alert tip %}
Tag your Canvases so they're easy to find and build reports out of. For instance, when using [Report Builder]({{site.baseurl}}/user_guide/data_and_analytics/reporting/report_builder/), you can filter by particular tags.
{% endalert %}

![][51]

#### Choose conversion events

Choose your Conversion Event Type, then select the conversions you would like to record. We will use the [Conversion Event]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/) that you set from this screen to measure the efficiency of your Canvas. 

![Primary Conversion Event A with the Makes Purchase conversion event type to record conversations for users who make any purchase within a three day conversion deadline.][52]{: style="max-width:75%;"}

If your Canvas has multiple variants or a Control Group, Braze will use this conversion event to determine the best variation for achieving this conversion goal. Using the same logic, you can create multiple conversion events.

### Step 2b: Set your Canvas entry schedule

You can choose one of three ways in which users can enter your Canvas.

#### Entry schedule types

{% tabs local %}
  {% tab Scheduled Delivery %}
    With scheduled delivery, users will enter on a time schedule, similarly to how you would schedule a campaign. You can enroll users in a Canvas as soon as it is launched, or enter them into your journey at some point in the future, or on a recurring basis.

    ![Canvas Scheduled Delivery]({% image_buster /assets/img_archive/Canvas_Scheduled_Delivery.png %})
  {% endtab %}
  {% tab Action-Based Delivery %}
    With action-based delivery, you can choose to enter users into a Canvas when they perform certain triggers. Users will enter your Canvas and begin receiving messages when they take particular actions, such as opening your app, making a purchase, or triggering a custom event. <br><br>Note that action-based delivery is unavailable for Canvas components with in-app messages.

    ![Canvas Action-Based Delivery]({% image_buster /assets/img_archive/Canvas_Action_Based_Delivery.png %})

    You can control other aspects of your Canvas' behavior from the **Entry Audience** window, including rules for re-eligibility and frequency capping settings.
  {% endtab %}
  {% tab API-Triggered Delivery %}
    With API-triggered deliver, you can choose to enter users into a Canvas via an API request. In the dashboard, you can find an example cURL request that does this as well as assign optional [`canvas_entry_properties`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/) using the [`Canvas Entry Properties Object`]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/). <br><br>Users will enter your Canvas and begin receiving messages once they have been added using the [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/) endpoint via the API.

    ![Canvas API-Triggered Delivery]({% image_buster /assets/img_archive/Canvas_API_Triggered_Delivery.png %})

    API-Triggered Delivery Endpoints:
    - [POST: Send Canvas Messages via API-Triggered Delivery]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)
    - [POST: Schedule API-Triggered Canvases]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases/)
    - [POST: Update Scheduled API-Triggered Canvases]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases/)

  {% endtab %}
{% endtabs %}

<!--Tag allows alert to be linked to-->
<a id="important-edge-case"></a>

{% alert important %}
Should the window of re-eligibility be less than the maximum duration of the Canvas, a user will be allowed to re-enter and receive more than one component's messages. In the edge case where a user's re-entry reaches the same component as its previous entry, Braze will deduplicate that component's messages. <br><br>In the event where a user re-enters the Canvas, reaches the same component as their previous entry, and is eligible for an in-app message for each entry, the user will get the message twice (depending on in-app message priority) as long as they re-open a session two times.
{% endalert %}

After you choose your delivery method, adjust those settings appropriately, and move on to setting your target audience.

### Step 2c: Set your target entry audience

You can set the target audience for your Canvas on the **Target Audience** step. Only the users who match your defined criteria can enter the journey.

For example, if you want to target new users, you can limit a particular journey to users who first used your app less than 3 weeks ago. You can also control settings such as whether messages should be sent to users who are subscribed or opted-in to your notifications.

{% alert warning %}
Avoid configuring an action-based campaign or Canvas with the same trigger as the audience filter (i.e., a changed attribute or performed a custom event). A race condition may occur in which the user is not in the audience at the time they perform the trigger event, which means they won't receive the campaign or enter the Canvas.  
{% endalert %}

#### Testing your audience

After adding segments and filters to your target audience, you can test if your audience is set up as expected by [looking up a user]({{site.baseurl}}/user_guide/engagement_tools/segments/user_lookup/) to confirm if they match the audience criteria.

![]({% image_buster /assets/img_archive/user_lookup.png %})

### Step 2d: Select your send settings

Click **Send Settings** to select your subscription settings, turn on rate limiting, and to enable Quiet Hours. 

By turning on [rate limiting][6b] or [frequency capping][6c], you can ease the marketing pressure placed on your users and ensure you aren't over messaging them. To manage your frequency capping rules, go  to your **Global Message Settings** page in your Braze account.

For Canvases targeting email and push channels, you may want to limit your Canvas so that only the users who are explicitly opted in will receive the message (excluding subscribed or unsubscribed users). For example, say you have three users of different opt-in status:

- **User A** is subscribed to email and is push enabled. This user doesn't receive the email but will receive the push.
- **User B** is opted-in to email but is not push enabled. This user will receive the email but doesn't receive the push.
- **User C** is opted-in to email and is push enabled. This user will receive both the email and the push.

To do so, set the **Subscription Settings** to send this Canvas to "opted-in users only". This option will ensure that only opted-in users will receive your email, and Braze will only send your push to users who are push enabled by default. 

These subscription settings are applied on a per-step basis, meaning that there is no effect on the entry audience. So this setting is used to evaluate a user's eligibility to receive each Canvas step.

{% alert important %}
With this configuration, don't include any filters in the **Target Users** step that limit the audience to a single channel (e.g., `Push Enabled = True` or `Email Subscription = Opted-In`).
{% endalert %}

If desired, specify Quiet Hours (the time during which your messages will not send) for your Canvas. Check **Enable Quiet Hours** in your **Send Settings**. Then, select your Quiet Hours in your user's local time and what action will follow if the message triggers inside of those Quiet Hours.

![][50]

## Step 3: Build your Canvas

### Adding a variant

![][11]{: style="float:right;max-width:35%;margin-left:15px;"}

Click **Add Variant** and select the option to add a new variant to your Canvas. Variants represent a journey that your users will take, and can contain multiple steps and branches.

You can add additional variants by pressing the <i class="fas fa-plus-circle"></i> plus button. When you add new variants, you'll be able to adjust how your users will be distributed between them so that you can cross-compare and analyze the efficacy of different engagement strategies.

![][12]

{% alert tip %}
By default, Canvas variant assignment is locked in when users enter the Canvas, meaning that if a user first enters a variant, that will be their variant every time they re-enter the Canvas. However, there are ways to circumvent this behavior. <br><br>To do so, you can create a random number generator using Liquid, run it at the beginning of each user's Canvas entry, store the value as a custom attribute, and then use that attribute to randomly divide users.

{% details Expand for steps %}

1. Create a custom attribute to store your random number. Name it something easy to locate, like "lottery_number" or "random_assignment". You can create the attribute either [in your dashboard]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/custom_event_and_attribute_management/), or through API calls to our [User Track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) endpoint.<br><br>
2. Create a webhook campaign at the beginning of your Canvas. This campaign will be the medium in which you create your random number, and store it as a custom attribute. Refer to [Creating a Webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#step-1-set-up-a-webhook) for more. Set the URL to our User Track endpoint.<br><br>
3. Create the random number generator. You can do so with the code [outlined here](https://www.131-studio.com/blogs/shopify-conversion/generate-random-numbers-using-liquid-shopify), which takes advantage of each user's unique time of entry to create a random number. Set the resulting number as a Liquid variable within your webhook campaign.<br><br>
4. Format the `users/track` call on your webhook campaign so that it sets the custom attribute you created in step 1 to the random number you've generated on your current user's profile. When this step runs, you will have successfully made a random number that changes each time a user enters your campaign.<br><br>
5. Adjust the branches of your Canvas so that, instead of being divided by randomly chosen variants, they are divided based on audience rules. In the audience rules of each branch, set the audience filter according to your custom attribute. <br><br>For example, one branch may have "lottery_number is less than 3" as an audience filter, while another branch may have "lottery_number is more than 3 and less than 6" as an audience filter.

{% enddetails %}
{% endalert %}

### Adding steps

You can add more steps to your Canvas workflow by dragging and dropping components from the **Components** sidebar. Or, when you click the <i class="fas fa-plus-circle"></i> plus button, you can also add a component with the popover menu.

![]({% image_buster /assets/img_archive/add_components_flow.png %})

{% alert tip %}
As you begin to add more steps, you can view your entire Canvas using either the **Detailed View** or **Simplified View**. **Simplified View** shows just the component icons as a high-level visual of your user journey whereas **Detailed View** shows the expanded step details. Depending on your preferences, you can toggle between these views!
{% endalert %}

{% alert warning %}
A Canvas built using Canvas Flow can contain up to 200 steps. If your Canvas exceeds 200 steps, loading issues will occur.
{% endalert %}

### Editing a step

Looking to edit a step in your user journey? Check out how to do this depending on your Canvas workflow!

You can edit any step in your Canvas Flow workflow by clicking any of the components. For example, let's say you want to edit your first step, a [Delay]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/) component, in your workflow to a specific day. Click the step to view its settings and adjust your delay to March 1. This means on March 1, your users will move to the next step in your Canvas.

![]({% image_buster /assets/img_archive/edit_delay_flow.png %})

Or you can quickly edit and adjust the **Action Settings** of your [Action Paths]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) step to hold users for a window of time. This prioritizes their next path based on the actions during this evaluation period.

![]({% image_buster /assets/img_archive/action_paths_flow.png %})

The lightweight components in Canvas allow for a simple editing experience, so adjusting the finer details of your Canvas is made easier. 

#### Messages in Canvas

Edit the messages in a Canvas component to control messages that a particular step will send. Canvas can send email, mobile, and web push messages, and webhooks to integrate with other systems. Similar to campaign messages, you can use certain Liquid templating to personalize your messages.

{% alert tip %}
Did you know you can include Canvas component names in your messages and link templates?<br>
Use the `campaign.${name}` Liquid tag in Canvas to display the current Canvas component name.
{% endalert %}

The Message component manages the messages sent to users. You can select your **Messaging Channels** and adjust **Delivery Settings** to optimize your Canvas messaging. For more details on this component, check out [Message]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/).

![]({% image_buster /assets/img_archive/message_setup_settings_flow.png %})

Click **Done** once you've finished configuring your Canvas component.

{% tabs local %}
{% tab Canvas Entry Properties %}

The `canvas_entry_properties` are configured in the Entry Schedule step of creating a Canvas and will indicate the trigger that enters a user into a Canvas. These properties can also access the properties of entry payloads in API-triggered Canvases. Note that the `canvas_entry_properties` object has a maximum size limit of 50 KB. 

For Canvas Flow, entry properties can be used in Liquid in any Message step. Use the following Liquid when referencing these entry properties: {% raw %} ``canvas_entry_properties${property_name}`` {% endraw %}. Events must be custom events or purchase events to be used this way.

Use the following Liquid when referencing these entry properties: {% raw %} ``canvas_entry_properties${property_name}`` {% endraw %}. Note that the events must be custom events or purchase events to be used this way.

{% raw %}
For example, consider the following request: `\"canvas_entry_properties\" : {\"product_name\" : \"shoes\", \"product_price\" : 79.99}`. You could add the word "shoes" to a message with this Liquid ``{{canvas_entry_properties.${product_name}}}``.
{% endraw %}

{% endtab %}

{% tab Event Properties %}
Event properties are the properties set by you on custom events and purchases. These `event_properties` can be used in campaigns with action-based delivery as well as Canvases. 

In Canvas Flow, custom event and purchase event properties can be used in Liquid in any Message step that follows an Action Paths step. Use this Liquid {% raw %} ``{{event_properties.${property_name}}}`` {% endraw %} when referencing these `event_properties`. These events must be custom events or purchase events to be used this way in the Message component.

In the first Message step following an Action Path, you can use `event_properties` related to the event referenced in that Action Path. You can have other steps (that are not another Action Paths or Message step) in between this Action Paths step and the Message step. Note that you'll only have access to `event_properties` if your Message step can be traced back to a non-Everyone Else path in an Action Path step

{% endtab %}
{% endtabs %}

### Editing connections

To move a connection between steps, click the arrow connecting the two components and select a different component. To break the connection, click the arrow and click **Cancel Connection** in the footer of the Canvas composer.

## Step 4: Use multivariate testing using Canvas

You can add a control group to your Canvas by clicking on the <i class="fas fa-plus-circle"></i> plus button to add a new variant. 

Braze will track the conversions for users who are placed into the control group, although they will not receive any messages. To preserve an accurate test, we will track the number of conversions for your variants and the control group for exactly the same amount of time, as shown on the conversion event selection screen. 

You can adjust the distribution between your messages by double-clicking the **Variant Name** headers.

In this example, we have our Canvas divided into two variants. Variant 1 has 70% of the users. The second variant is a control group with the remaining 30% of users.

![]({% image_buster /assets/img_archive/Canvas_Multivariate_Flow.png %})

### Intelligent Selection for Canvas

Intelligent Selection capabilities are now available within multivariate Canvases. Similar to the [Intelligent Selection][18a] feature for multivariate Campaigns, Intelligent Selection for Canvas analyzes the performance of each Canvas variant and adjusts the percentage of users being funneled through each variant. This distribution is based off each variant's performance metrics to maximize the total expected number of conversions.

Keep in mind that multivariate Canvases allow you to test more than copy, but timing and channels as well. Through Intelligent Selection, you can test Canvases more efficiently and have confidence that your users will be sent on the best possible Canvas journey.

![][18b]

Intelligent Selection for Canvas optimizes your Canvas's results by making gradual real-time adjustments to the distribution of users sorted into each variant. When the statistical algorithm determines a decisive winner among your variants it will rule out the underperforming variants and slot all future eligible recipients of the Canvas into the winning variants. 

For this reason, Intelligent Selection works best on Canvases that have new users entering frequently.

## Step 5: Save and launch your Canvas

Once you're done creating your Canvas, press **Launch Canvas** to save and launch your Canvas. You can also save your Canvas as a draft if you need to come back to it.

Once you've launched your Canvas, you'll be able to view analytics for your journey as they come in on the **Canvas Details** page.

![][19]

{% alert tip %}
Need to make edits to your Canvas after launch? Well, you can! Check out [Editing Canvases after launch]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/change_your_canvas_after_launch/) for more information.
{% endalert %}


[1]:{% image_buster /assets/img_archive/canvas_dropdown.png %}
[3]: {% image_buster /assets/img_archive/choose_canvas_experience.png %}
[6b]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#rate-limiting
[6c]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#frequency-capping
[11]:{% image_buster /assets/img_archive/canvas_add_variant.gif %}
[12]:{% image_buster /assets/img_archive/Canvas_Multiple_Variants.png %}
[13]:{% image_buster /assets/img_archive/Canvas_One_Day.png %}
[14]:{% image_buster /assets/img_archive/Canvas_Exception_Events.png %}
[15]:{% image_buster /assets/img_archive/Canvas_Additional_Engagement.png %}
[17]:{% image_buster /assets/img_archive/Canvas_More_Step.png %}
[18a]: {{site.baseurl}}/user_guide/intelligence/intelligent_selection/
[18b]: {% image_buster /assets/img_archive/canvas_intelligent_selection.png %}
[19]:{% image_buster /assets/img_archive/Canvas_Analytics.png %}
[50]: {% image_buster /assets/img/quiet_hours.png %}
[51]: {% image_buster /assets/img/Basics1.gif %}
[52]: {% image_buster /assets/img/add_canvas_conversions.png %}
[53]: {% image_buster /assets/img/entry-schedule-canvas-1.gif %}
[54]: {% image_buster /assets/img/entry-audience-canvas-1.gif %}
[55]: {% image_buster /assets/img/canvas-send-settings-1.gif %}