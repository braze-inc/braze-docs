---
nav_title: Abandoned cart
article_title: Abandoned Cart
page_order: 1
page_type: reference
description: "This article describes how to use a Braze Canvas template to engage with users in real-time to encourage them to complete their purchases."
tool: Canvas
---

# Abandoned cart

> Engage with users in real-time to encourage them to complete their purchases. Use this template to create a user journey that focuses on sending timely, personalized messages that remind users of their abandoned carts by highlighting product benefits and offering incentives, such as discount codes.

In this article, we'll walk you through a use case for the **Abandoned Intent** template, which is intended for the consideration stage of the user lifecycle. After this article, you'll have customized a user journey that encourages purchases from users who haven't made purchases after adding items to their carts.

## Prerequisites

To successfully use this template, you'll need the following:

- A separate post-purchase user journey Canvas since making a purchase in this Canvas will cause users to exit the Canvas.
- A configured [Braze Audience Sync]({{site.baseurl}}/partners/canvas_audience_sync/) with the partners and audiences you use.

## Tailoring the template to your needs

Let's say we work at Kitchenerie, a retail brand specializing in kitchenware, and our goal is to reengage users who have added the latest product "Enormous Paper Plate" to their carts but haven't made their purchases.

Before creating the Canvas, we set up the [Braze Audience Sync to Facebook]({{site.baseurl}}/partners/canvas_audience_sync/facebook_audience_sync/) integration so that we can add user data from Braze to Facebook Audiences to send advertisements based on behavioral triggers, segmentation, and more.

To access the abandoned intent template, when creating a new Canvas, select **Use a Canvas template** > **Braze templates**. Then, next to **Abandoned Intent**, select **Apply Template**. Now, we can go through the template to fit it for our needs.

### Step 1: Set up the details

Let’s adjust the Canvas details to reflect our goal.

1. Select **Edit** next to the template name.

![The current title and description of the Canvas.]({% image_buster /assets/img/canvas_templates/abandoned_intent_old_name_description.png %}){: style="max-width:60%;"}

{:start="2"}
2. Update the Canvas name to specify that the Canvas is for targeting users with abandoned carts.
3. Update the description to specify that the Canvas is for encouraging users to complete purchases from the latest seasonal kitchenware launch.
4. Add the tag **Abandon Cart** so we can filter for it on the Canvas home page.

![The new name, description, and tag for the Canvas.]({% image_buster /assets/img/canvas_templates/abandoned_intent_new_name_description.png %}){: style="max-width:60%;"}

### Step 2: Assign your conversion events

Next, let's assign our conversion event. Because our focus is on our "Enormous Paper Plate" product, we will do the following for **Primary Conversion Event A**:

1. For the **Conversion event type**, select **Makes Purchase**.
2. Select **Make a specific purchase**. This allows us to select a specific product name.
3. Select **Enormous Paper Plate**.

![Primary Conversion Event - A with the conversion type "Makes Purchase" with the product name "Enormous Paper Plate". There is a 3-day conversion deadline.]({% image_buster /assets/img/canvas_templates/abandoned_intent1.png %})

### Step 3: Set an entry schedule

While this template's entry schedule is set to **API-Triggered**, our use case will benefit more by having an action-based entry for this Canvas since we want to focus on users who have abandoned their cart (which is an action).

1. Select **Action-Based** as the entry schedule type.
2. Select **Abandoned Cart** as the trigger.
3. For the entry window, select the start time date.
4. Select the option to allow users to enter in their local time zone. This can keep our messaging relevant and lead to higher engagement if messages are sent at optimal times.

![An action-based Canvas that targets users who have abandoned their cart, with the entry window October 15, 2024 3:20 pm at the users' local time zone.]({% image_buster /assets/img/canvas_templates/abandoned_intent2.png %})

### Step 4: Determine who enters the Canvas

Next, let's define our target audience as users who have shopped exclusively online with us in the past 90 days. This helps us narrow our audience down to users we know are engaged with our products. 

!["Online Shoppers Segment - 90 Days" as the segment of users to target for this Canvas.]({% image_buster /assets/img/canvas_templates/abandoned_intent3.png %})

We'll leave the entry controls as is, so users aren't allowed to re-enter this Canvas and there's no limit to the number of people who can potentially enter this Canvas.

For the exit criteria, users will exit the Canvas if they have purchased the "Enormous Paper Plate". This way they won't receive further messages about an item they've already purchased.

![Exit criteria that determines users who make a specific purchase for the enormous paper plate will exit the Canvas.]({% image_buster /assets/img/canvas_templates/abandoned_intent4.png %})

### Step 5: Select your send settings

We’ll keep the default subscription settings, so we only send to users who have subscribed or opted into receiving messages or notifications, and leave the other settings as is.

### Step 6: Customize your Canvas

Now, we’ll build our Canvas by customizing the templated steps:

1. Select the Action Paths step, then select the **Made purchase** action group name.
2. For **Make Purchase**, select **Make A Specific Purchase** and choose **Enormous Paper Plate** for the product. Similar to the exit criteria, users who purchase this product will exit the Canvas.

!["Made purchase" action group that will exit the Canvas if the user purchases the enormous paper plate.]({% image_buster /assets/img/canvas_templates/abandoned_intent5.png %})

{: start="3"}
3. For the Message step, select **Edit message** to customize the email that will be sent to our users, notifying them of the items in their abandoned cart.
4. Keep the Delay step as is.
5. In the Message steps subsequent to the Audience Path step, we'll customize the email and SMS message that our users will receive. This is where we want to encourage our users to purchase products with personalized messaging.

![A preview of the SMS message that users will receive: "Hi there, you left the enormous paper plate behind in your cart! Complete your purchase now and step up your hosting game. Use code MYPLATE at checkout for 20 percent off your order!"]({% image_buster /assets/img/canvas_templates/abandoned_intent6.png %})

{: start="6"}
6. In the next Action Paths step, select the **Made purchase** action group. Then, select **Make a specific purchase** and choose **Enormous Paper Plate** for the product. This step will mirror the first Action Paths step by exiting users who have purchased our product so they won't receive further messaging.
7. Make sure our Audience Sync step is set up to sync to Facebook. This will further help with ad retargeting.

{% alert tip %}
You can use [Canvas entry properties]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/) to customize the messages in your Canvas based on which product you're referring to.
{% endalert %}

### Step 7: Test and launch the Canvas

After testing and reviewing our Canvas to make sure it works as expected, select **Launch Canvas** to launch the Canvas. Now, we can mindfully target users with a personalized user journey to encourage them to checkout the product they've added to their carts!

{% alert tip %}
Check out our [Pre and post-launch checklist]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch) for things to consider before and after you launch a Canvas.
{% endalert %}

