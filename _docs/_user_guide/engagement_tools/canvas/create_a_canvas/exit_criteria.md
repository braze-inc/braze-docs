---
nav_title: Exit Criteria 
article_title: Exit Criteria 
page_order: 4.1
alias: /exit_criteria/
page_type: reference
description: "This reference article covers exit criteria and how users can exit your Canvas based on the selected criteria."
tool: Canvas
---

# Exit criteria

> By adding exception events directly to your Canvas entry rules, your users can exit your Canvas as soon as the event happens at the end of the step. This helps achieve a more targeted approach to Canvas messaging with your audience.

### How users exit

After performing the exit event, users are exited from the Canvas as soon as the step they're currently in has been exited. For example, if a user is in a Delay step for 30 days and they perform the exit event on the first day of the Delay step, the user won't exit the Canvas for another 29 days.

Let's consider another example when using time-based exit criteria. A user enters a Delay step set to 24 hours on July 1 at 12 am. In this delay period, they perform the exit event "Last made purchase less than 1 hour ago" at 3 am. This user will be evaluated for the exit criteria on July 2 at 12 am, which is the conclusion of the Delay step's duration. Because 21 hours have passed since their purchase on July 1 at 3 am, they won't exit the Canvas because they didn't make a purchase within the one hour of exiting the Delay step on July 2. This impacts the "Total Exits by Exit Criteria" in your Canvas analytics, which are only updated after a user has fully exited the Canvas.

## Setting up exit criteria

In the **Target Audience** step of the Canvas builder, you can set up exit criteria to identify which users you want to exit your Canvas. 

The exit criteria includes an exception event, which is the specific action that can cause users to exit the Canvas.

![The exit criteria set up to re-engage users who have browsed products but haven't added them to their cart or placed an order yet.]({% image_buster /assets/img/exit_criteria.png %}){: style="max-width:90%;"}

### Selecting exception events {#exception-events}

When a user performs the exception event, they will exit the Canvas. Note that exception events will only trigger exits when a user is in the Canvas and advancing through the user journey.

Let's say you have a Canvas set up to promote a new product. In this case, the purchase of the product would be the exception event. This way, after a user makes the purchase, they won't receive more messages about a product they already purchased. Exception events keep your messaging relevant and personalized.

Additional exception events include:

- Making a purchase
- Starting a session
- Performing a custom event
- Performing a conversion event
- Adding an email address
- Changing a custom attribute value
- Updating a subscription status
- Updating a subscription group status
- Interacting with a campaign
- Entering a location
- Triggering a geofence
- Sending an SMS inbound message
- Sending a WhatsApp inbound message
- Sending a LINE inbound message
- Performing a cart updated event
- Performing a checkout completed event
- Performing a checkout started event

#### Scheduled steps

If a Canvas step is scheduled, the user will drop out immediately from the Canvas after the exception event occurs. Let's say a user enters a Canvas where the first step has a one-week delay and an exception event. If the user performs the exception event on day 5, they would exit immediately after performing the exception event (on day 5). 
 
#### Triggered steps

If a Canvas step is triggered by an event, the last scheduled send enqueued from that trigger will be canceled, but the user will remain inside the canvas for the duration of the window. That means the user can still be sent the step if they perform the trigger event again within the window. After the window passes, the user will then exit the Canvas.

### Using segments and filters

You can also add segments and filters in the exit criteria. This means users who match the segment and filter will exit the Canvas and won't receive any further messaging. 

For example, if the first step in a Canvas is a Delay step with a five-day delay, then the exit criteria will apply at the end of this step. So, if a user meets the exit criteria, they will exit at the end of the five days.

{% alert note %}
Array attributes aren’t currently supported as exit criteria on exception events.
{% endalert %}

### Having the same exit event and conversion event

When the exit event and conversion event are the same, both the conversion and exit events will be accounted for. For example, if a Canvas has a Delay step and a user performs the exit criteria while in that Delay step, the exit event will increment as soon as the user exits the Delay step. The conversion will also increment as soon as the event is logged on the user profile.

Conversions are tracked even after the Canvas ends, but exits are not tracked once the user exits the Canvas. The conversion window extends to three days beyond the maximum duration of the Canvas. This means conversions will continue to be tracked after exits stop being tracked. 

The minimum time for a conversion window is five minutes. Set the conversion windows to five minutes for your conversion events to get as close as possible to parity with exit events. We also recommend setting the conversion window to at least match the longest path in the Canvas.

Consider the following example on how analytics are calculated:

1. Ten users go through the Canvas.
2. Three users perform the conversion event within five minutes (the number of exit events is three, and the number of conversion events is three).
3. Another five users exit the Canvas after five minutes but perform the conversion event after two days (the number of exit events remains the same, but the conversion event increases to eight).
4. The last two users exit the Canvas after five minutes but don't perform the conversion event, or perform it after three days and five minutes (they aren't counted in either exit events or conversion events metrics).

## Example

Let's say we want to target users who haven't made any purchases at our backpack supply company yet. To set up the exit criteria, we would:

1. Select **Make Purchase** as the exception event.
2. Select **Add Trigger**. 
3. For **Segments**, select **Used in last day** so that when our Canvas launches, the audience will exclude users who have made any purchases.
4. For **Filters**, select **Purchase behavior** > **Number of purchases** > **Purchased product**.
5. Set the filter group to `backpack-example exactly 1`. This means that users who have purchased our backpack product would exit the Canvas.

![Exit Criteria settings with "Makes Any Purchase" as the exception event, so if a user makes any purchase, then they will exit this Canvas.]({% image_buster /assets/img_archive/exit_criteria_example.png %}){: style="max-width:80%;"}


