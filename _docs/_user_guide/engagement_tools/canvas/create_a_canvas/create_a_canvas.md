---
nav_title: Create a Canvas
platform: Canvas
subplatform: Create a Canvas
page_order: 0
description: "This reference article covers the neccesary steps involved in creating, maintaining, and testing a Canvas."
---

# Creating a Canvas

Follow this guide, or check out our [LAB course](http://lab.braze.com/quick-overview-canvas-setup)!

## Step 1: Navigate to the Canvas Page and Create a New Canvas ![Canvas][1]{: style="float:right;max-width:15%;margin-left:10px;margin-top:10px;margin-bottom:10px;"}

Click on the "Canvas" link on the Dashboard's side navigation located underneath the "Campaigns" link, then click __Create a New Canvas__.

## Step 2: Use the Entry Wizard to Set Up Your Canvas

The Entry Wizard will guide you through setting up your Canvas - everything from naming it to setting conversion events and bringing the right users into your customer journey. Click on each of the tabs below to see what settings you can adjust in each of the Entry Wizard steps.

{% tabs local %}
  {% tab Basics %}
    Here, you will set up the basics of your Canvas:
    - Name Your Canvas
    - Add Teams to Your Canvas
    - Add Tags to Your Canvas
    - Assign Conversion Events and Choose Their Event Types and Deadlines

    [Learn more about the Basics step.](#set-up-your-canvas-basics)
  {% endtab %}
  {% tab Entry Schedule %}
    Here, you will decide how your users will enter your Canvas:
    - Scheduled: This is a time-based Canvas entry
    - Action-Based: Your user will enter your Canvas after they perform a defined action
    - API Triggered: Use an API request to enter users into your Canvas

    [Learn more about the Entry Schedule step.](#set-your-canvas-entry-schedule)
  {% endtab %}
  {% tab Entry Audience %}
    Here, you will select your Canvas Entry Audience:
    - Create Your Audience by Adding Segments and Filters
    - Fine-tune Canvas Re-Entry and Entry Limits
    - See a Summary of Your Target Audience

    [Learn more about the Entry Audience step.](#set-your-target-entry-audience)
  {% endtab %}
  {% tab Send Settings %}
    Here, you will select your Canvas Send Settings:
    - Select Your Subscription Settings
    - Set a Send Rate Limit for Your Canvas Messages
    - Enable and Set Quiet Hours

    [Learn more about the Send Settings step.](#select-your-send-settings)
  {% endtab %}
  {% tab Build Canvas %}
    Here you will build your Canvas.

    [Learn how to build your Canvas using the Canvas builder.](#step-3-build-your-canvas)
  {% endtab %}
{% endtabs %}


### Set Up Your Canvas Basics

Here, you'll name your Canvas, assign [Teams]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/teams/#teams), and create or add [Tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/#tags). Here, you'll also assign conversion events for the Canvas.

![Basics][51]

#### Choose Conversion Events

Choose your Conversion Event Type, then select the conversions you would like to record.

![Conversion][52]

We will use the Conversion Event that you set from this screen to measure the efficiency of your Canvas. If your Canvas has multiple variants or a Control Group, Braze will use this Conversion Event to determine the best variation
for achieving this Conversion goal. Using the same logic, you can create multiple Conversion Events.


### Set Your Canvas Entry Schedule

There are three ways in which users can enter your Canvas - a scheduled entry, an action-based delivery, or an API-Triggered delivery. After you choose which you'll use, adjust those settings appropriately, and move on to setting your target audience.

![Entry Schedule][53]

#### Entry Schedule Types


{% tabs local %}
  {% tab Scheduled Delivery %}
    __Scheduled Delivery__<br>
    With scheduled delivery, users will enter on a time schedule, similarly to how you would schedule a Campaign. You can enroll users in a Canvas as soon as it is launched, or enter them into your journey at some point in the future, or on a recurring basis.

    ![Canvas Scheduled Delivery]({% image_buster /assets/img_archive/Canvas_Scheduled_Delivery.png %})
  {% endtab %}
  {% tab Action-Based Delivery %}
    __Action-Based Delivery__<br>
    Additionally, you can choose to enter users into a Canvas when they perform certain triggers using Action-Based Delivery. Users will enter your Canvas and begin receiving messages when they take particular actions, such as opening your app, making a purchase, or triggering a custom event. Note that action-based delivery is unavailable for Canvas steps with in-app messages.

    ![Canvas Action-Based Delivery]({% image_buster /assets/img_archive/Canvas_Action_Based_Delivery.png %})

    You can control other aspects of your Canvas' behavior from the Entry Audience window, including rules for re-eligibility and frequency capping settings.
  {% endtab %}
  {% tab API-Triggered Delivery %}
    __API-Triggered Delivery__<br>
    You may also choose to enter users into a Canvas via an API request. In the Dashboard, you can find an example cURL request that does this as well as assign optional [`canvas_entry_properties`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/) using the [`Canvas Entry Properties Object`]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/). Users will enter your Canvas and begin receiving messages once they have been added using the [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/) endpoint via the API.

    ![Canvas API-Triggered Delivery]({% image_buster /assets/img_archive/Canvas_API_Triggered_Delivery.png %})

    API-Triggered Delivery Endpoints:
    - [POST: Send Canvas Messages via API Triggered Delivery]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)
    - [POST: Schedule API Triggered Canvases]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases/)
    - [POST: Update Scheduled API Triggered Canvases]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases/)

  {% endtab %}
{% endtabs %}

{% alert important %}
Should the window of re-eligibility be less than the maximum duration of the Canvas, a user will be allowed to re-enter and receive more than one step's messages. In the edge case where a user's re-entry reaches the same step as its previous entry, Braze will deduplicate that step's messages. In the event where a user re-enters the Canvas, reaches the same step as their previous entry, and is eligible for an in-app message for each entry, the user will get the message twice (depending on in-app message priority) as long as they re-open a session two times.
{% endalert %}

### Set Your Target Entry Audience

You can set the target audience for your Canvas here. Only the users who match your defined criteria can enter the journey.

![Canvas Target Audience][54]

If you want to limit a particular journey to users who first used your app less than 3 weeks ago. You can also control settings such as whether messages should be sent to users who are subscribed or opted-in to your notifications.

### Select Your Send Settings

Click "Send Settings" to select your Subscription Settings, turn on rate limiting, and to enable Quiet Hours.

![Send Settings][55]

By turning on rate-limiting or Frequency Capping you can ease the marketing pressure placed on your users and ensure you aren't over messaging them. To learn more about the benefits of rate-limiting and Frequency Capping click [here][6b].

{% alert important %}
Visit your __Global Campaign Settings__ page in your Braze account to manage your Frequency Capping rules.
{% endalert %}

Then, specify Quiet Hours (the time during which your messages will not send) for Canvas. Check "Enable Quiet Hours" in your __Send Settings__. Select your Quiet Hours in your user's local time and what action will follow if the message triggers inside of those Quiet Hours.

![quiethours][50]


## Step 3: Build Your Canvas

### Add a Variant
![Canvas Add Variant][11]{: style="float:right;max-width:20%;margin-left:15px;"}

Click the "Add Variant" button and select the option to add a new variant to your Canvas. Variants represent a journey that your users will take.

You can add additional variants by pressing the + button. When you add new variants, you'll be able to adjust how your users will be distributed between them so that you can cross-compare and analyze the efficacy of different engagement strategies:

![Canvas Multiple Variants][12]

### Editing a Step

Click anywhere on a Step, and Braze will open the Step editing interface. Steps can be configured to send messages after either a fixed delay (maximum of 31 days) or when a user performs a particular action. For example, you can use Canvas to configure a Day 1, Day 3, Day 7 onboarding Campaign with time delays between messages:

![Canvas One Day][13]

Or you can set a group of messages to be sent after your users take a particular action, with a configurable window, delay, and [exception events][56]:

![Canvas Exception Events][14]

You can also apply Filters to each Step of a Canvas. Use this to add additional control flow logic, such as dropping users out of a journey when they're not likely to need additional engagement encouragement:

![Canvas Additional Engagement][15]

#### Messages in Canvas

Edit the Messages in a Canvas Step to control messages that a particular Step will send. Canvas can send Email, Mobile & Web Push messages, and Webhooks to integrate with other systems.

Similar to Campaign messages, you may use certain Liquid templating.<br>
__Please see Canvas and Custom Event Properties below for limitations.__

![Canvas Message Edit][16]

Select desired advancement behavior. Learn more about options [here]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/).

![Canvas Advancement Behavior][20]

Press the "Done" button once you've finished configuring your Step.

{% tabs local %}
{% tab Canvas Entry Properties %}
Canvas Entry Properties are the properties mapped by you when triggering or scheduling a canvas via the API.
{% raw %}
- For example, a request with `\"canvas_entry_properties\" : {\"product_name\" : \"shoes\", \"product_price\" : 79.99}` could add the word \"shoes\" to a message by adding the Liquid `{{canvas_entry_properties.${product_name}}}`.

__Canvas Entry Properties can be referenced in the first step of a Canvas - but only the first step__! 

For more information on the Canvas Entry Object and Properties, check out our [Documentation]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/#canvas-entry-properties-object).
{% endraw %}
{% endtab %}
{% tab Custom Event Properties %}
Custom Event Properties are the properties set by you on custom events and purchases, used mainly in Action-Based Delivery campaigns. These properties are ephemeral and can only be used at the time when they happen. Event properties __don’t persist__ so if you are scheduling a canvas step, rather than using action-based delivery, you wouldn’t be able to use an event property as we don’t store that data. You can't reference the event property for an event that’s already happened.

__Custom Event Properties can be referenced in the first step of a canvas - but only the first step__! 

For more information on Custom Event Properties, check out our [Documentation]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties).

{% endtab %}
{% endtabs %}

{% alert tip %}
Did you know you can include Canvas step names in your messages and link templates?<br>
Use the `campaign.${name}` Liquid tag in Canvas to display the current Canvas step name.
{% endalert %}

### Add More Steps

Add more Steps by pressing the blue plus icon:

![Canvas More Step][17]{: style="max-width:75%;"}

## Step 4: Use Multivariate Testing Using Canvas

You can add a Control Group to your Canvas by clicking on the Plus icon to add a new variant. Braze will track the Conversions for users who are placed into the Control Group, although they will not receive any messages. To preserve an accurate test, we will track the number of Conversions for your variants and the Control Group for exactly the same amount of time, as shown on the Conversion Event selection screen. Adjust the distribution between your messages by double-clicking the variant Name headers.

![Canvas Multivariate][18]

### Intelligent Selection for Canvas
Intelligent Selection capabilities are now available within Multivariate Canvases. Similar to the [Intelligent Selection][18a] feature for multivariate Campaigns, Intelligent Selection for Canvas analyzes the performance of each Canvas variant and adjusts the percentage of users being funneled through each based off their performance metrics in such a way that the total expected number of conversions is maximized. Keep in mind that multivariate Canvases allow you to test more than copy, but timing and channels as well. Through Intelligent Selection you can test Canvases more efficiently and have confidence that your users will be sent on the best possible Canvas journey.

![Intelligent Selection][18b]

Intelligent Selection for Canvas optimizes your Canvas's results by making gradual real-time adjustments to the distribution of users sorted into each variant. When the statistical algorithm determines a decisive winner among your variants it will rule out the underperforming variants and slot all future eligible recipients of the Canvas into the winning variants. For this reason, Intelligent Selection works best on Canvases that have new users entering frequently.

## Step 5: Save & Launch Your Canvas

Once you're done, press the "Launch Canvas" button at the bottom right to save and launch your Canvas. You can also save your Canvas as a Draft if you need to come back to it.

Once you've launched your Canvas, you'll be able to view analytics for your journey as they come in:

![Canvas Analytics][19]


[1]:{% image_buster /assets/img_archive/Canvas_Dropdown.png %}
[6b]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#rate-limiting
[11]:{% image_buster /assets/img_archive/Canvas_Add_Variant.png %}
[12]:{% image_buster /assets/img_archive/Canvas_Multiple_Variants.png %}
[13]:{% image_buster /assets/img_archive/Canvas_One_Day.png %}
[14]:{% image_buster /assets/img_archive/Canvas_Exception_Events.png %}
[15]:{% image_buster /assets/img_archive/Canvas_Additional_Engagement.png %}
[16]:{% image_buster /assets/img_archive/Canvas_Message_Edit.png %}
[17]:{% image_buster /assets/img_archive/Canvas_More_Step.png %}
[18]:{% image_buster /assets/img_archive/Canvas_Multivariate.png %}
[18a]: {{site.baseurl}}/user_guide/intelligence/intelligent_selection/
[18b]: {% image_buster /assets/img_archive/canvas_intelligent_selection.png %}
[19]:{% image_buster /assets/img_archive/Canvas_Analytics.png %}
[20]:{% image_buster /assets/img_archive/Canvas_Advancement_Behavior.png %}
[link]: https://startupclass.co/courses/how-to-start-a-startup/lectures/64035
[21]:{% image_buster /assets/img_archive/Journey_2.png %}
[24]:{% image_buster /assets/img_archive/Journey_5.png %}
[25]:{% image_buster /assets/img_archive/Journey_6.png %}
[28]:{% image_buster /assets/img_archive/Journey_9.png %}
[29]:{% image_buster /assets/img_archive/Journey_10.png %}
[31]:{% image_buster /assets/img_archive/Canvas_Branch_1.png %}
[32]:{% image_buster /assets/img_archive/Canvas_Branch_2.png %}
[33]:{% image_buster /assets/img_archive/Canvas_Branch_3.png %}
[34]:{% image_buster /assets/img_archive/Canvas_Branch_4.png %}
[35]:{% image_buster /assets/img_archive/Canvas_Branch_5.png %}
[36]: https://www.braze.com/contact/
[37]: {{site.baseurl}}/help/webinars/webinar_signup/#canvas-entry-steps-and-conditions
[41]: {% image_buster /assets/img_archive/Journey_8-audience_options.png %}
[42]: {% image_buster /assets/img_archive/Journey_11-audience_options.png %}
[45]: {% image_buster /assets/img_archive/step_priority.png %}
[46]: {% image_buster /assets/img_archive/canvas_priority.png %}
[50]: {% image_buster /assets/img/quiet_hours.png %}
[51]: {% image_buster /assets/img/Basics1.gif %}
[52]: {% image_buster /assets/img/Conversions-canvas-1.gif %}
[53]: {% image_buster /assets/img/entry-schedule-canvas-1.gif %}
[54]: {% image_buster /assets/img/entry-audience-canvas-1.gif %}
[55]: {% image_buster /assets/img/canvas-send-settings-1.gif %}
[56]: {{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exception_events/