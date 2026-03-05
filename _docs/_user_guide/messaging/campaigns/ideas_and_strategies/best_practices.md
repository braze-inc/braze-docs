---
nav_title: Best practices
article_title: Campaign Best Practices
page_order: 0
description: "This article provides best practices for creating and customizing your campaigns."
tool: Campaign

---

# Campaign best practices

## Four T's of Braze

Braze recommends that you only send customer data that you intend to utilize on the Braze platform. Consider the philosophy of the "Four T's of Braze" to ensure you only send data that you will use to:

- **Target** your audiences by building [audience segments]({{site.baseurl}}/user_guide/engagement_tools/segments/).
- **Trigger** your messages with [action-based]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery#action-based-delivery) or [API-triggered]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/) delivery.
- **Template** and personalize your messages with [Liquid conditional logic]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid).
- **Track** the efficacy of your campaigns with [conversion tracking]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/).

This allows you to optimize the data you send to Braze and will streamline your ability to message your users while guaranteeing against tracking data points your team may not find helpful long-term. 

## User targeting

As you build out your campaigns over time, you may notice lapses in your audience. At this crucial point, you can target your [lapsing users]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/capturing_lapsing_users/) with a specialized campaign using segmentation. 

### Identify your audience

Leverage segments and filters to your advantage by defining your audience. Consider who your campaign and messages are targeting. With this key information, you can create [multichannel campaigns]({{site.baseurl}}/user_guide/engagement_tools/campaigns/faq/#how-do-you-create-a-multichannel-campaign) that offer the flexibility of building your messages in different channels to match your audience's notification preferences.

It's also important to understand your [active users]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/active_user_campaigns/) to show your appreciation to your consistent users.

## Multichannel campaigns

### Feature awareness

If your goal is to draw your users toward a new feature or app version, use a multichannel strategy with a focus on in-app channels. [In-app messages]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about/) and [Content Cards]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/) are generally less disruptive if a user doesn't wish to update immediately. 

Be sure to include [deep links]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/) to the appropriate app store.

Persuading users to update their app or change how they use your app can be difficult, so let them know about all the benefits of the new version or features and how it will improve their experience with your app. 

### Send timing

Timing is key! When your goal is to convince users to update their app, wait until they have a positive experience within the app to ask users. To keep your audience engaged, avoid repetitive messaging that may appear intrusive.

Over time, your users may forget certain features or not notice new features. When new features are added, be sure to let your users know with [in-app messages]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about/). If users aren't engaging with major features within the app, it may be best to remind them when they're engaging with your app and when this new feature would be of use. Our article on [data opt-in]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/) has more information on ensuring your request agrees with users' workflow expectations. 

## High ratings

Getting five-star ratings in the app store is on every mobile marketer's wish list. Achieving positive reviews, however, is no easy task because it requires extra work from your users. By applying our functionality in clever ways, we can help you increase your customer engagement.

### Targeting power users

Power users can be advocates for your app. Often, they interact with your app consistently and can provide feedback to improve your app. Although they differ from app to app, power users tend to have the following:

- Logged many sessions
- Used the app recently
- Spent money and made purchases

To ensure higher ratings, ask your power users to review your app in the app store, as they're more likely to have great things to say. For example, you could create a segment named "Power users" with these filters:
- Has used these apps more than 10 times in the last 14 days
- Has spent more than 50 dollars

![An example of a segment that targets power users of an app.]({% image_buster /assets/img_archive/ratings_power_users.png %})

Visiting the app store takes time on the part of your users. To maximize the likelihood that they will go through the extra effort, request a rating or review after they just had a positive experience with your app. For instance, ask them after they beat a game level or made a purchase using a discount code. Our article on [data opt-in]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-states) has more information on ways to ensure your request agrees with users' workflow expectations.

## Scheduling your campaigns

When editing campaign schedules or audiences, note the following best practices:

- **One-time schedule campaigns:** You can edit the campaign up until the scheduled send time.
- **Recurring scheduled campaigns:** You can edit the campaign up until the scheduled send time.
- **Local send time campaigns:** Don't make edits 24 hours before the scheduled send time.
- **Optimal send time campaigns:** Don't make edits 24 hours before midnight of the day the campaign is scheduled to be sent on.

{% alert note %}
Editing a live campaign and changing the delivery to **Local Send Time** will cause a new batch of messages to be enqueued, meaning your users will receive the message twice due to the message being enqueued twice. To prevent this, first stop the original campaign, then launch a duplicate after updating the schedule.
{% endalert %}

