# Banners: Frequently Asked Questions

> These are answers to frequently asked questions about Banners in Braze. For more general information, see [About Banners]({% if include.section == "user" %}{{site.baseurl}}/user_guide/message_building_by_channel/banners{% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/banners{% endif %}).

## When do Banner updates appear for users?

Banners are refreshed with their latest data whenever you call the refresh method&#8212;there's no need to resend or update your Banner campaign.

## How many placements can I request in a session?

In a single refresh request, you can request a maximum of 10 placements. For each one you request, Braze will return the highest-priority Banner a user is eligible for. Additional requests will return an error.

For more information, see [Placement requests]({% if include.section == "user" %}{{site.baseurl}}/user_guide/message_building_by_channel/banners#requests{% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/banners#requests{% endif %}).

## How many Banner campaigns can be active simultaneously?

Each workspace can support up to 200 active Banner campaigns. If this limit is reached, you'll need to [archive or deactivate]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/about_statuses/#changing-the-status) an existing campaign before creating a new one.

## For campaigns sharing a placement, which Banner is displayed first?

If a user qualifies for multiple Banner campaigns that share the same placement, the Banner with the highest priority will be displayed. For more information, see [Banner priority]({% if include.section == "user" %}{{site.baseurl}}/user_guide/message_building_by_channel/banners/#priority{% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/banners#priority{% endif %}).

## Can I use Banners in my existing Content Card feed?

Banners are different from Content Cards, meaning you can’t use Banners and Content Cards in the same feed. To replace existing Content Card feeds with Banners, you’ll need to [create placements in your app or website]({{site.baseurl}}/developer_guide/banners/placements/).

## Can I trigger a banner based on user actions?

While Banners do not support [action-based delivery]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery), you can target users based on their past actions using segmentation and priority.

For example, to show a special Banner only to users who have completed a `purchase` event:
1. **Targeting:** In your campaign, target a segment of users who have performed the custom event `purchase` at least once.
2. **Priority:** If you have a general Banner for all users and this specific Banner for purchasers targeting the same placement, set the specific Banner's priority to **High** and the general Banner to **Medium** or **Low**.

When the user starts a new session or refreshes Banners after performing the action, Braze evaluates their eligibility. If they match the "Purchase" segment, the high-priority Banner will be displayed.


## Can users manually dismiss a Banner?

No. Users cannot manually dismiss Banners. However, you can control Banner visibility by managing user segment eligibility. When a user no longer meets the targeting criteria for a Banner campaign, they won't see it again on their next session.

For example, if you display a promotional Banner until a user makes a purchase, logging an event such as `purchase_completed` can remove that user from the targeted segment, effectively hiding the Banner in subsequent sessions.

## Can I export Banners campaign analytics using the Braze API?

Yes. You can use the [`/campaigns/data_series` endpoint]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/) to get data on how many Banner campaigns were viewed, clicked, or converted.

## When are users segmented?

Users are segmented at the beginning of the session. If a campaign's targeted segments depend on custom attributes, custom events, or other targeting attributes, they must be present on the user at the beginning of the session.

## How can I compose Banners to ensure the lowest latency?

The simpler the messaging in your Banner, the faster it will render. It’s best to test your Banner campaign against the expected latency for your use case. For example, be sure to test Liquid attributes like `catalog_items`.

## Are all Liquid tags supported?

No. However, most Liquid tags are supported for Banner messages, except for `catalog_items` that are re-rendered using the [`:rerender` tag]({{site.baseurl}}/user_guide/data/activation/catalogs/using_catalogs/#using-liquid).

## Can I capture click events?

Click events are only captured if an on-click action is set on a `logClick` element and is called using the [JS bridge]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/html_in-app_messages/#javascript-bridge).
