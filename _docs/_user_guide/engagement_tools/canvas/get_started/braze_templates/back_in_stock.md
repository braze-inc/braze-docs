---
nav_title: Back in stock
article_title: Back In Stock
page_order: 2
page_type: reference
description: "This article describes how to use a Braze Canvas template to drive purchases by notifying your users when an item is back in stock with personalized messaging."
tool: Canvas
---

# Back in stock

> Use the back-in-stock template to create messages that target users who have previously viewed or expressed interest in an item that was out of stock but is now available for purchase. This helps users obtain the products they want by engaging them at the critical moment when a product returns to availability.

This article will walk you through a use case for the **Back In Stock** template, which is designed for the conversion step of the user lifecycle. When you’re finished, you’ll have created a Canvas that sends a push (web or mobile), SMS, or email to users when an item is back in stock, and up to two reminders.

## Prerequisites

To successfully use this template, you'll need the following:

- A [catalog]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog) containing information about your item
- [Back-in-stock notifications]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications/#how-back-in-stock-notifications-work) must be set up for the item you want to message users about

## Tailoring the template to your needs

Let’s say we’re working for PantsLabyrinth, a direct-to-consumer clothing retailer that specializes in slacks, jeans, culottes, and many other types of pants. We can use the back in stock template to notify customers on various channels when a popular pair of jeans, the Classic Straight Leg, is back in stock.

Before creating the Canvas, we [set up a catalog]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog) that contains information about our straight leg pants inventory and [set up back-in-stock notifications]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications/#setting-up-back-in-stock-notifications) for the Classic Straight Leg jeans. We made it so that users will subscribe to notifications after they perform the custom event of favoriting the Classic Straight Leg jeans on the app.

To access the back-in-stock template, when creating a new Canvas, select **Use a Canvas template** > **Braze templates**. Then, next to **Back in Stock**, select **Apply Template**. Now, we can go through the template to fit it for our needs.

### Step 1: Set up the details

Let’s adjust the Canvas details to reflect our goal.

1. Select **Edit** next to the template name.

![The current title and description of the Canvas.]({% image_buster /assets/img/canvas_templates/back_in_stock_old_name_description.png %}){: style="max-width:45%;"}

{:start="2"}
2. Update the Canvas name to specify that the Canvas is for targeting users when our product Classic Straight Leg is back in stock.
3. Update the description to explain that this Canvas contains personalized messaging.
4. Add the tag **Back in Stock**, which is nested under the tag **Promotional**, so that we can filter for it on the Canvas home page. 

!["Set Up Canvas Details" step with a Canvas name of "Back in Stock - Classic Straight Leg" and a brief Canvas description.]({% image_buster /assets/img/canvas_templates/back_in_stock_1.png %})

### Step 2: Assign conversion events

Change the **Primary Conversion Event - A** to **Make a specific purchase** and select **Classic Straight Leg** for the product name.

!["Assign Conversion Events" section for the conversion event type of purchasing the Classic Straight Leg product with a conversion deadline of 7 days.]({% image_buster /assets/img/canvas_templates/back_in_stock_2.png %})

### Step 3: Tailor the entry schedule

Let’s keep the entry schedule as **Action-Based** so that users will enter our Canvas when they perform an action, which the template already has set to **Perform a Back in Stock Event**.

We’ll make two adjustments to this step:

1. Select the catalog that includes information about our Classic Straight Leg jeans, which we’ve named “Straight Leg Pants”. 

!["Entry Schedule" step for an action-based Canvas.]({% image_buster /assets/img/canvas_templates/back_in_stock_3.png %})

{: start="2"}
2. Set the **Start Time (Required)** to our desired start date and time.

!["Entry Window" section with a start time of January 2, 2025 at 12 am.]({% image_buster /assets/img/canvas_templates/back_in_stock_4.png %})

### Step 4: Select the target audience

We’ll define our target audience as users who we think are more likely to purchase the Classic Straight Leg jeans.

1. Select our target segment, “Favorited - Classic Straight Leg Jeans”, which consists of users who’ve favorited our Classic Straight Leg jeans on our app or website.
2. Select a filter to include users who have purchased “Jeans” more than “0” times.

!["Target Audience" step with the segment of "Favorited - Classic Straight Leg Jeans".]({% image_buster /assets/img/canvas_templates/back_in_stock_5.png %})

{: start="3"}
3. Adjust the entry controls to allow users to re-enter the Canvas after the Canvas’s maximum duration, to prevent the likelihood of users triggering the same step concurrently.

!["Entry Controls" section with a checkbox for allowing users to re-enter this Canvas with a maximum duration of the Canvas.]({% image_buster /assets/img/canvas_templates/back_in_stock_6.png %})

{: start="4"}
4. Adjust the exit criteria to remove users who performed the custom event of unfavoriting the Classic Straight Leg jeans.

!["Exit Criteria" section with a exception for users that perform the custom event of "Unfavorited".]({% image_buster /assets/img/canvas_templates/back_in_stock_7.png %})

### Step 5: Select your send settings

We’ll keep the default subscription settings, so we only send to users who have subscribed or opted into receiving messages or notifications, and skip the other settings (frequency capping, quiet hours, and seed groups).

!["Send Settings" step targeting users who are subscribed or opted in.]({% image_buster /assets/img/canvas_templates/back_in_stock_8.png %})

### Step 6: Customize your Canvas

Now, we’ll build our Canvas by customizing the channels and content that will send to users. Because we’re using all four of the template channels (mobile and web push, SMS, and email) and using the [Intelligent Channel]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_channel/) filter, we don’t need to add or remove any.

{% alert tip %}
You can use [Canvas entry properties]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/) to customize the messages in your Canvas based on which product you're referring to.
{% endalert %}

We’ll begin our customization by going through each Message step to update the content.

1. Replace `!!YOURCATALOGHERE!!` with our catalog name (“Straight_Leg_Pants”).
2. Replace `[0]` with the index number of the Classic Straight Leg jeans, which is “9” because the jeans are tenth item in the the `items` array of our catalog. (Arrays are zero-indexed in Liquid, so the first item is `0` and not `1`.)
3. Repeat steps 1 and 2 for all remaining Message steps, including:
    - The “In-Product Msg & Email” message that sends after the one-day delay
    - The “Push+Email Alert” messages that send to users who haven’t made a purchase
4. Update the Action Paths step by selecting the **Purchase** action group. Then, select **Make a specific purchase** and choose Classic Straight Leg jeans for the product.

![Mobile Push Canvas step with a message notifying users that a product is back in stock.]({% image_buster /assets/img/canvas_templates/back_in_stock_9.png %})

### Step 7: Test and launch your Canvas

After testing and reviewing our Canvas to make sure it works as expected, we’ll launch it by selecting **Launch Canvas**. Now our users who have favorited our Classic Straight Leg jeans and have subscribed to our messaging channels will receive notifications when they’re back in stock!

{% alert tip %}
Check out our [Pre and post-launch checklist]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch) for things to consider before and after you launch a Canvas.
{% endalert %}

