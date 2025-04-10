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

## Setting up exit criteria

In the **Target Audience** step of the Canvas builder, you can set up exit criteria to identify which users you want to exit your Canvas. 

The exit criteria includes an exception event, which is the specific action that can cause users to exit the Canvas.

![The exit criteria set up to re-engage users who have browsed products but haven't added them to their cart or placed an order yet.][1]{: style="max-width:90%;"}

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

### Using segments and filters

You can also add segments and filters in the exit criteria. This means users who match the segment or filter will exit the Canvas and won't receive any further messaging. 

For example, if the first step in a Canvas is a Delay step with a five-day delay, then the exit criteria will apply at the end of this step. So, if a user meets the exit criteria, they will exit at the end of the five days.

{% alert note %}
Array attributes aren’t currently supported as exit criteria on exception events.
{% endalert %}

## Example

Let's say we want to target users who haven't made any purchases at our backpack supply company yet. To set up the exit criteria, we would:

1. Select **Make Purchase** as the exception event.
2. Select **Add Trigger**. 
3. For **Segments**, select **Used in last day** so that when our Canvas launches, the audience will exclude users who have made any purchases.
4. For **Filters**, select **Purchase behavior** > **Number of purchases** > **Purchased product**.
5. Set the filter group to `backpack-example exactly 1`. This means that users who have purchased our backpack product would exit the Canvas.

![Exit Criteria settings with "Makes Any Purchase" as the exception event, so if a user makes any purchase, then they will exit this Canvas.][2]{: style="max-width:80%;"}


[1]: {% image_buster /assets/img/exit_criteria.png %}
[2]: {% image_buster /assets/img_archive/exit_criteria_example.png %}
