---
nav_title: Conversion events
article_title: Conversion Events
page_order: 4
page_type: reference
description: "This reference article defines conversion events, how to use them to define your success metrics in Braze, and how to use these events to see how engaged your users are."
tool:
    - Campaigns
    - Canvas
---

# Conversion events

> A conversion event is a type of success metric that tracks whether a recipient of your messaging performs a high-value action in a set amount of time after receiving your engagement. Use these events to make sure you're collecting relevant, useful information that you can later use to gain insight for your campaign or Canvas.

## How it works

Let's say you're creating a personalized holiday campaign for active users, a conversion event of **Start a Session** within two or three days may be appropriate since it will allow you to gather a sense of user engagement from receiving your message. Additional events like **Make Purchase**, **Upgrade App**, or any of your custom events can be selected as conversion events.

{% alert tip %}
For more on conversions, check out our [Braze Learning course](https://learning.braze.com/campaign-setup-delivery-targeting-conversions) on campaign setup.
{% endalert %}

### Conversion tracking rules

Conversion events allow you to attribute user action back to a point of engagement. That said, there are a few things to note regarding how Braze handles multiple conversions. Check out the following scenarios to understand how Braze tracks these conversions:

- Conversions occur on a per-user basis, not a per-device basis. This means a user can only convert once, even if a message is sent to multiple devices. As another example, assume a campaign has only one conversion event which is "Makes any purchase". If a user who receives this campaign makes two separate purchases within the conversion deadline, then only one conversion will be counted.
- If a user performs one conversion event within the conversion deadlines of two separate campaigns or Canvases that they received, then the conversion will register on both.
- A user will count as converted if they performed the specific conversion event in the window even if they did not open or click the message.
- For Canvases, conversion tracking works based on the final conversion deadline that begins when a user enters the Canvas, not individual message timing. This means conversions can be counted even during delay periods between messages in Canvas.

### Primary conversion event

The primary conversion event is the first event added during the campaign or Canvas creation. This event has the most bearing on your engagement and reporting. Your primary conversion event is used to:

- Compute the winning message variation in [multivariate]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/#multivariate-and-ab-testing) campaigns or Canvases.
- Determine the window when revenue is calculated for the campaign or Canvas.
- Adjust message distributions for campaigns and Canvases using [Intelligent Selection]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/).

The primary conversion event count is calculated by dividing the number of users who performed the primary conversion action by the number of unique recipients. A user is considered a recipient once they are sent or shown the message, depending on the channel. For example, in push or email, a user becomes a recipient after the message is sent. For in-app messages or Content Cards, the user must view the message to be considered a recipient.

{% alert note %}
If messages are aborted using the Liquid `abort` tag, only the users who go through variants are potentially aborted. This means the messages to users who go through the control group won't be aborted, which may lead to skewed conversion percentages across variants and control groups. As a workaround, use [segmentation]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment) to target your users at campaign and Canvas entry.
{% endalert %}

## Creating a campaign with conversion tracking

### Step 1: Set up your campaign

[Create a campaign]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/creating_campaign) for your desired messaging channel. After setting up your campaign's messages and schedule, you'll have the option to add up to four conversion events for tracking.

We recommend using as many conversion events as you feel is necessary because the addition of a second (or third) conversion event can significantly enrich your reporting. For instance, let's say you have a campaign that targets lapsing users. In this case, adding a secondary conversion event and the primary **Starts Session** conversion event can further your understanding of how effective your campaign is in ushering your users back into your application. 

### Step 2: Add the conversion events

First, select the general type of event you'd like to use:

| Conversion Event Type         | Description                                                                                                                                                                                                                                                                                                                                 |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Starts Session**      | A user is counted as having converted when they open any one of the apps that you specify (defaults to all apps in the workspace).                                                                                                                                                                                                         |
| **Makes Purchase**      | A user is counted as having converted when they purchase the product you specify (defaults to any product).                                                                                                                                                                                                                                 |
| **Performs Custom Event** | A user is counted as having converted when they perform one of your existing custom events (no default, you must specify the event).                                                                                                                                                                                                        |
| **Upgrade App**         | A user is counted as having converted when they upgrade the app version on any one of the apps that you specify (defaults to all apps in the workspace). Braze performs a best-efforts numerical comparison to determine if the change was an upgrade. Non-numeric versions are counted as conversions if the version changes.              |
| **Opens email**         | A user is counted as having converted when they open the email (only for email campaigns).                                                                                                                                                                                                                                                 |
| **Clicks email**        | A user is counted as having converted when they click a link within the email (only for email campaigns).                                                                                                                                                                                                                                  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Set your conversion deadline. This is the maximum amount of time that may pass to consider a conversion. You have the option of allowing up to a 30-day window during which the conversion will be counted if the user takes the specified action.

![The "Makes Purchase" conversion event type as an example to record conversions for users who make any purchase. This has a conversion deadline of 12 hours.]({% image_buster /assets/img_archive/conversion_event_selection.png %})

After you've selected your conversion events, continue the campaign creation process and begin sending your campaign.

### Step 3: View your results

Go to the **Details** page to view the details for each conversion event associated with the campaign you just created. Regardless of your selected conversion events, you can also see the total revenue that can be attributed to this specific campaign, as well as specific variants, during the window of the primary conversion event.

{% alert note %}
If there are no conversion events selected during campaign creation, the time defaults to three days. 
{% endalert %}

Additionally, for multivariate messages, you can see the number of conversions and conversion percentages for your control group and each variant.

![Four conversion events that track conversions based on when a purchase was made within three hours, made a purchase within two hours, started a session within 30 minutes, and started a session within 25 minutes.]({% image_buster /assets/img_archive/conversion_event_details.png %})


