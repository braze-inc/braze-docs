# Banners: Frequently Asked Questions

> These are answers to frequently asked questions about Banners in Braze. For more general information, see [About Banners]({% if include.section == "user" %}{{site.baseurl}}/user_guide/message_building_by_channel/banners{% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/banners{% endif %}).

## When do Banner updates appear for users?

Banners are automatically refreshed at the start of each new user session with their latest data&#8212;there's no need to resend or update your Banner campaign.

## How many placements can be requested in a session?

Up to 10 placements can be returned per session. Each placement will include the highest priority Banner a user is eligible for.

For example, if you've created three placements (such as a homepage-promo, cart-abandonment, and seasonal-offer), you can request all three within a single session. For each placement, Braze will return the [highest priority]({{site.baseurl}}/user_guide/message_building_by_channel/banners/#priority) Banner matching that user's targeting criteria. If you request more than 10 placements in a single session, only the first 10 will be evaluated and returned.

## For campaigns sharing a placement, which Banner is displayed first?

If a user qualifies for multiple Banner campaigns that share the same placement, the Banner with the highest priority will be displayed. For more information, refer to [Banner priority]({{site.baseurl}}/user_guide/message_building_by_channel/banners/#priority).

## Can I use Banners in my existing Content Card feed?

Banners are different from Content Cards, meaning you can’t use Banners and Content Cards in the same feed. To replace existing Content Card feeds with Banners, you’ll need to [create placements in your app or website]({{site.baseurl}}/developer_guide/banners/creating_placements/).

## Can users dismiss a Banner?

No. Users cannot manually dismiss Banners. However, you can control Banner visibility by managing user segment eligibility. When a user no longer meets the targeting criteria for a Banner campaign, they won't see it again on their next session.

For example, if you display a promotional Banner until a user makes a purchase, logging an event such as `purchase_completed` can remove that user from the targeted segment, effectively hiding the Banner in subsequent sessions.

## Can I export Banners campaign analytics using the Braze API?

Yes. You can use the [`/campaigns/data_series` endpoint]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/) to get data on how many Banner campaigns were viewed, clicked, or converted.

## When are users segmented?

Users are segmented at the beginning of the session. If a campaign's targeted segments depend on custom attributes, custom events, or other targeting attributes, they must be present on the user at the beginning of the session.

## How can I compose Banners to ensure the lowest latency?

The simpler the messaging in your Banner, the faster it will render. It’s best to test your Banner campaign against the expected latency for your use case. For example, be sure to test Liquid attributes like `catalog_items`.

## Are all Liquid tags supported?

No. However, most Liquid tags are supported for Banner messages, except for `catalog_items` that are re-rendered using the [`:rerender` tag]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/using_catalogs/#using-liquid).

## Can I capture click events?

Click events are only captured if an on-click action is set on a `logClick` element and is called using the [JS bridge]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/html_in-app_messages/#javascript-bridge).
