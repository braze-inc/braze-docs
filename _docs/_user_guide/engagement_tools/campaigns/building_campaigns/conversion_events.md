---
nav_title: Conversion Events
article_title: Conversion Events
page_order: 5
page_type: tutorial
description: "This article defines conversion events, how to use them and define your success metrics within Braze, and how to use these tools to see how engaged your users are."
tool: Campaigns

---
# Conversion events

> This article defines conversion events, how to use them and define your success metrics within Braze, and how to use these tools to see how engaged your users are.
> <br>
> <br>
> By using conversion events, you can make sure you're collecting relevant, useful information that you can later use to gain insight for your campaign. 

In order to track engagement metrics and the necessary details regarding how messaging drives your KPIs, Braze allows you to set conversion events for each of your campaigns and Canvases.

A conversion event is a type of success metric that tracks whether a recipient of your messaging performs a high-value action within a set amount of time after receiving your engagement. With this, you can begin to attribute these valuable actions to the different points of engagement reaching the user. 

For example, if you're creating a personalized holiday campaign for active users, a conversion event of **Start a Session** within two or three days may be appropriate since it will allow you to gather a sense of user engagement from receiving your message. Additional events like **Make Purchase**, **Upgrade App**, or any of your custom events can be selected as conversion events.

For more on conversions, check out our [LAB course](http://lab.braze.com/campaign-setup-delivery-targeting-conversions) on campaign setup!

## Primary conversion event

The primary conversion event is the first event added during the campaign or Canvas creation. This event has the most bearing on your engagement and reporting. Your primary conversion event is used to:

- Compute the winning message variation in [multivariate][4] campaigns or Canvases.
- Determine the window when revenue is calculated for the campaign or Canvas.
- Adjust message distributions for campaigns and Canvases using [Intelligent Selection][5].

## Step 1: Create a campaign with conversion tracking

Navigate to the [Campaigns][1] page in your company dashboard and click **Create Campaign**, then select the type of campaign you'd like to create.

After setting up your campaign's messages and schedule, you'll have the option to add up to four conversion events for tracking. 

We highly recommend using as many conversion events that you feel is necessary since the addition of a second (or third) conversion event can significantly enrich your reporting. For instance, let's say you have a campaign that targets lapsing users. In this case, adding a secondary conversion event in addition to the primary **Starts Session** conversion event can further your understanding of how effective your campaign is in ushering your users back into your application. 

## Step 2: Add conversion events

For each conversion event you wish to track, select the event and conversion deadline.

1. Select the general type of event you'd like to use:
  - **Opens App**: A user is counted as having converted when they open any one of the apps that you specify (defaults to all apps in the app group).
  - **Makes Purchase**: A user is counted as having converted when they purchase the product you specify (defaults to any product).
  - **Performs Custom Event**: A user is counted as having converted when they perform one of your existing custom events (no default, you must specify the event).
  - **Upgrade App**: A user is counted as having converted when they upgrade the app version on any one of the apps that you specify (defaults to all apps in the app group). Braze will perform a best-efforts numerical comparison to determine if the version change was an upgrade. For example, a user would convert if they upgrade from version 1.2.3 to 1.3.0 of the application, but Braze wouldn't register a conversion if a user downgrades from 1.2.3 to 1.2.2. However, if the app's version name contain strings, such as "1.2.3-beta2", then Braze will not be able to determine if a version change was an upgrade. In this situation, Braze will count it as a conversion when the user's most recent app version changes.<br><br>
2. Set your conversion deadline. This is the maximum amount of time that may pass to consider a conversion. You have the option of allowing up to a 30-day window during which a conversion will be counted if the user takes the specified action.  

![The "Makes Purchase" conversion event type as an example to record conversions for users who make any purchase. This has a conversion deadline of 12 hours.][2]

Once you've selected your conversion events, continue the campaign creation process and begin sending your campaign.

## Step 3: View results

Navigate to the **Details** page to view the details for each conversion event associated with the campaign you just created. Regardless of your selected conversion events, you can also see the total revenue that can be attributed to this specific campaign, as well as specific variants, during the window of the primary conversion event.

{% alert note %}
If there are no conversion events selected during campaign creation, the time period defaults to three days. 
{% endalert %}

Additionally, for multivariate messages, you can see the number of conversions and conversion percentages for your control group and each variant.

![][3]

## Conversion tracking rules

Conversion events allow you to attribute user action back to a point of engagement. That said, there are a few things to note regarding how Braze handles multiple conversions. Check out the following scenarios to understand how Braze tracks these conversions:

- A user can only convert once on each conversion event for a campaign or Canvas. For instance, assume a campaign has only one conversion event which is "Makes any purchase." If a user who receives this campaign makes two separate purchases within the conversion deadline, then only one conversion will be counted.
- If a user performs one conversion event within the conversion deadlines of two separate campaigns or Canvases that they received, then the conversion will register on both.
- A user will count as converted if they performed the specific conversion event in the window even if they did not open or click the message.

[1]: https://dashboard-01.braze.com/engagement/campaigns/ "Campaigns Page"
[2]: {% image_buster /assets/img_archive/conversion_event_selection.png %}
[3]: {% image_buster /assets/img_archive/conversion_event_details.png %}
[4]: {{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/#multivariate-and-ab-testing
[5]: {{site.baseurl}}/user_guide/intelligence/intelligent_selection/#intelligent-selection