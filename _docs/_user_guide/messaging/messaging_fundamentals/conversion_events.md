---
nav_title: Conversion events
article_title: Conversion Events
page_order: 3
page_type: reference
description: "This reference article defines conversion events, how to use them to define your success metrics in Braze, and how to use these events to see how engaged your users are."
tool:
    - Campaigns
    - Canvas
---

# Conversion events

> A conversion event is a type of success metric that tracks whether a recipient of your messaging performs a high-value action in a set amount of time after receiving your engagement. Use these events to make sure you're collecting relevant, useful information that you can later use to gain insight for your campaign or Canvas.

## How it works

For a personalized holiday campaign targeting active users, a conversion event of **Start a Session** within two or three days may be appropriate because it allows you to gather a sense of user engagement from receiving your message. You can also select additional events like **Places Order**, **Upgrade App**, or any of your custom events as conversion events.

{% alert tip %}
For more on conversions, check out our [Braze Learning course](https://learning.braze.com/campaign-setup-delivery-targeting-conversions) on campaign setup.
{% endalert %}

### Conversion tracking rules

Conversion events attribute user actions back to a point of engagement. Note the following about how Braze handles multiple conversions:

- **Single-channel campaigns**: Conversions occur on a per-user basis, not a per-device basis. Within a single channel, a user converts only once per conversion event, even if a message is sent to multiple devices. For example, if a campaign has only one conversion event set to "Makes any purchase" and a user makes two separate purchases within the conversion deadline, Braze counts only one conversion.
- **Multichannel campaigns**: For multichannel campaigns, each channel has its own conversion opportunity. A user can convert once per channel after receiving a message on that channel. This means if a user receives messages on multiple channels (for example, both email and push) and performs the conversion action, Braze counts one conversion for each channel, which can result in conversion rates exceeding 100%.
- If a user performs one conversion event within the conversion deadlines of two separate campaigns or Canvases that they received, the conversion registers on both.
- A user counts as converted if they performed the specific conversion event in the window, even if they did not open or click the message.
- For Canvases, conversion tracking works based on the final conversion deadline that begins when a user enters the Canvas, not individual message timing. Braze counts conversions even during delay periods between messages in Canvas.

### Primary conversion event

The primary conversion event is the first event you add during campaign or Canvas creation. This event has the most bearing on your engagement and reporting. Braze uses your primary conversion event to:

- Compute the winning message variation in [multivariate]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/#multivariate-and-ab-testing) campaigns or Canvases.
- Determine the window when revenue is calculated for the campaign or Canvas.
- Adjust message distributions for campaigns and Canvases using [Intelligent Selection]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/).

The primary conversion event count is the number of conversion events that occurred. For multichannel campaigns, Braze counts conversions per channel (as described in [Conversion tracking rules](#conversion-tracking-rules)), which means the conversion count can exceed the number of unique users and result in conversion rates greater than 100%. Braze calculates the primary conversion event rate by dividing this count by the number of unique recipients. Braze considers a user a recipient when the message is sent or shown, depending on the channel. For example, in push or email, a user becomes a recipient after Braze sends the message. For in-app messages or Content Cards, the user must view the message to be considered a recipient.

{% alert note %}
If you abort messages using the Liquid `abort` tag, Braze aborts messages only for users who go through variants. Messages to users in the control group are not aborted, which can lead to skewed conversion percentages across variants and control groups. As a workaround, use [segmentation]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment) to target your users at campaign and Canvas entry.
{% endalert %}

## Creating a campaign with conversion tracking

### Step 1: Set up your campaign

[Create a campaign]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/creating_campaign) for your desired messaging channel. After setting up your campaign's messages and schedule, you can add up to four conversion events for tracking.

Use as many conversion events as necessary. Adding a second or third conversion event significantly enriches your reporting. For example, for a campaign targeting lapsing users, adding a secondary conversion event along with the primary **Starts Session** conversion event helps you understand how effective your campaign is at bringing users back into your application. 

### Step 2: Add the conversion events

First, select the general type of event you'd like to use:

| Conversion Event Type   | Description                |
|-------------------------|----------------------------|
| **Starts Session**      | A user is counted as having converted when they open any one of the apps that you specify (defaults to all apps in the workspace).|
| **Makes Purchase**      | A user is counted as having converted when they record a [Purchase event]({{site.baseurl}}/api/objects_filters/purchase_object/). This tracks any purchase by default, or you can specify a particular product.|
| **Places Order**        | A user is counted as having converted when they trigger the [Order Placed eCommerce recommended event]({{site.baseurl}}/user_guide/data/activation/custom_data/recommended_events/ecommerce_events?tab=ecommerce.order_placed#ecommerce-recommended-events). This tracks any order by default, or you can filter by a specific product.|
| **Performs Custom Event**| A user is counted as having converted when they perform one of your existing custom events (no default, you must specify the event).|
| **Upgrade App**         | A user is counted as having converted when they upgrade the app version on any one of the apps that you specify (defaults to all apps in the workspace). Braze performs a best-efforts numerical comparison to determine if the change was an upgrade. Non-numeric versions are counted as conversions if the version changes.|
| **Opens email**         | A user is counted as having converted when they open the email (only for email campaigns).|
| **Clicks email**        | A user is counted as having converted when they click a link within the email (only for email campaigns).|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert important %}
**Nested properties are not supported in conversion events**. You cannot use nested properties in conversion events. For example, if `product_code` or `product_name` are nested properties within a `products` array (such as `products[].product_code`), you cannot use them to check if a specific product purchase has been made in a conversion event.
{% endalert %}

Set your conversion deadline. This is the maximum amount of time that can pass before Braze considers a conversion. You can set a window of up to 30 days during which Braze counts the conversion if the user takes the specified action.

![The "Makes Purchase" conversion event type as an example to record conversions for users who make any purchase. This has a conversion deadline of 12 hours.]({% image_buster /assets/img_archive/conversion_event_selection.png %})

After you've selected your conversion events, continue the campaign creation process and begin sending your campaign.

### Step 3: View your results

Go to the **Details** page to view the details for each conversion event associated with the campaign you created. Regardless of your selected conversion events, you can also see the total revenue attributed to this specific campaign, as well as specific variants, during the window of the primary conversion event.

{% alert note %}
If you don't select any conversion events during campaign creation, the time defaults to three days. 
{% endalert %}

Additionally, for multivariate messages, you can see the number of conversions and conversion percentages for your control group and each variant.

![Four conversion events that track conversions based on when a purchase was made within three hours, made a purchase within two hours, started a session within 30 minutes, and started a session within 25 minutes.]({% image_buster /assets/img_archive/conversion_event_details.png %})