---
nav_title: May
page_order: 8
noindex: true
page_type: update
description: "This article contains release notes for May 2019."
---

# May 2019

## Content Cards

Content Cards are persistent content that appear within customers' app and web experiences.

With Content Cards, you can send a highly targeted, dynamic stream of rich content to your customers right within the apps they love, without interrupting their experience. Or, you can pair Content Cards with other channels, like email or push notifications, to enable cohesive marketing strategies.

![Content Cards Feed]({% image_buster /assets/img/cc-feed.png %}){: height="50%" width="50%"}

In addition, Content Cards support more personalized features, including card pinning, card dismissal, API-based delivery, custom card expiration times, card analytics.

Use it to create notification centers, homepage feeds, and promotion feeds.

You will need to update to a supported Braze SDK version:
- iOS: 3.8.0 or later
- Android: 2.6.0 or later
- Web: 2.2.0 or later

[Learn more about Content Cards here!]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/)

{% alert update %}
Content Cards for Currents and our API documentation for Content Cards will be launched later this week. Stay tuned!
{% endalert %}

## Roku platform addition

Braze has added a new channel to our capabilities! By expanding into new channels, we can enable our customers to enrich their data by understanding viewing behavior or provide meaningful experiences to their consumers across all relevant channels.

You can now [retrieve data from Roku devices]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=roku) for data enrichment and custom event tracking.

## Notification preferences for Canvas or campaign updates

This [new notification]({{site.baseurl}}/user_guide/administrative/company_settings/notification_preferences/#notification-preferences) will alert you via email when a campaign or Canvas is activated, updated, reactivated, or deactivated. Activate this in **Notification Preferences** in your Braze account.

## Jampp technology partner documentation

Jampp is a performance marketing platform for acquiring and retargeting mobile customers. It combines behavioral data with predictive and programmatic technology to generate revenue for advertisers by showing personal, relevant ads that inspire consumers to purchase for the first time, or more often.

Braze customers can [integrate with Jampp]({{site.baseurl}}/partners/jampp/) by configuring the Braze webhook channel to stream events into Jampp. As a result, customers have the ability to add richer data sets to their retargeting initiatives with Jampp within the mobile advertising ecosystem.

## Platform picker for in-app messages

We've made it easier to select where your in-app messages are going and which platforms they're built for with our platform picker, which emphasizes this step in the campaign creation process.

![Platform Picker]({% image_buster /assets/img/iam_platforms.gif %})

## Dispatch ID Currents field for email

{% alert update %}
Behavior for `dispatch_id` differs between Canvas and campaigns because Braze treats Canvas steps (except for Entry Steps, which can be scheduled) as triggered events, even when they are "scheduled". Learn more about [`dispatch_id` behavior]({{site.baseurl}}/help/help_articles/data/dispatch_id/) in Canvas and campaigns.

_Update noted in August 2019._
{% endalert %}

In the effort to continue enhancing our Currents capabilities, we're adding `dispatch_id` as a field to Currents email events across all connector types.

The `dispatch_id` is the unique ID generated for each transmission ,or dispatch, sent from the Braze platform.

While all customers who are sent a scheduled message get the same `dispatch_id`, customers who receive either action-based or API-triggered messages will get a unique `dispatch_id` per message. The `dispatch_id` field enables you to identify which instance of a recurring campaign is responsible for conversion, thus equipping you with more insights and information on which types of campaigns are helping push the needle on your business goals.

## "Only Show Mine" campaign sorting feature

When a user checks the `Only Show Mine` checkbox on the campaign grid, the results will filter down to campaigns show only created by the logged-in user. Additionally, the user can use the search bar by inputting `created_by_me:true`.

Also, the campaign grid sidebar is now resizable!

## Delete users by alias

You can now use the `users/delete` endpoint to [delete users by alias]({{site.baseurl}}/api/endpoints/user_data/#user-delete-request)!

## Unique calculation for email clicks and opens

Unique Clicks and Unique Opens for email are now captured and displayed on a 7-day time frame per user and increment a count of 1 within that 7 day window, per each `dispatch_id`.

Using `dispatch_id` allows for recurring messages to reflect the true unique open or unique click count of each message. It will be easy for customers to match this data, now that the `dispatch_id` is available in Currents.

Any users also using Mailjet will see a spike in these numbers, since the previous uniqueness timeframe was over 30 days. You should have been made aware of this change three (3) weeks ago.  SendGrid customers should see no difference.

You can search for these updated terms in our [report metrics glossary]({{site.baseurl}}/user_guide/data/report_metrics/).

{% alert update %}
Behavior for `dispatch_id` differs between Canvas and campaigns because Braze treats Canvas steps (except for Entry Steps, which can be scheduled) as triggered events, even when they are "scheduled". [Learn more about [`dispatch_id` behavior]({{site.baseurl}}/help/help_articles/data/dispatch_id/) in Canvas and campaigns.

_Update noted in August 2019._
{% endalert %}


## Most engaged channel

{% alert update %}
As of the [November 2019 product release]({{site.baseurl}}/help/release_notes/2019/november/#intelligence-suite), "Most Engaged Channel" has been renamed to ["Intelligent Channel"]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_channel/).
{% endalert %}

The Most Engaged Channel filter selects the portion of your audience for whom the selected messaging channel is their "best" channel. In this case, "best" means "has the highest likelihood of engagement, given the user's history". You can select email, web push, or mobile push (which includes any available mobile OS or device) as a channel.

Check this new filter out in our [Segmentation Filters library]({{site.baseurl }}/user_guide/engagement_tools/segments/segmentation_filters/).

