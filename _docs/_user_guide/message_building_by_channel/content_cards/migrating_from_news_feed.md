---
nav_title: Migrating from News Feed
article_title: Migrating from News Feed
page_order: 10
description: "This reference article provides guidance on migrating from News Feed to Braze Content Cards."
channel:
  - content cards
  - news feed
  
---

# Migrating from News Feed to Content Cards

{% alert note %}
News Feed is being deprecated. Braze recommends that customers who use our News Feed tool move over to our Content Cards messaging channel—it's more flexible, customizable, and reliable.
{% endalert %}

> Moving from News Feed to Content Cards takes time, but it is an easy adoption! You can't automatically migrate content from News Feed to Content Cards—you must integrate Content Cards from scratch. However, with the new flexibility of Content Cards, we don't think you'll miss it or mind.

Reach out to your Braze account manager for more details.

## Features and functionality

Content Cards offers many capabilities that are not supported by News Feed, such as additional delivery options like action-based and API delivery, and enhanced analytics like conversion tracking.

As you plan your migration from the News Feed to Content Cards, it will be important to note the main differences between Content Cards and the News Feed:

- **Segmentation:** Content Cards segmentation can be evaluated at the time messages are sent or at the time the card is first viewed. News Feed segmentation is evaluated at the time that News Feed Cards are viewed.
- **Personalization:** Content Cards personalization can be templated at the time messages are sent or at the time the card is first viewed. News Feed card personalization is templated at the time that News Feed Cards are viewed.

The following table further outlines the difference in supported features between News Feed and Content Cards:

| Feature | News Feed | Content Cards |
|---|---|---|
| Multivariate and multichannel campaigns | <i class="fas fa-times" title="Not supported"></i> | <i class="fas fa-check" title="Supported"></i> |
| Scheduled, action-based, and API-based delivery | <i class="fas fa-times" title="Not supported"></i> | <i class="fas fa-check" title="Supported"></i> |
| API-created messages | <i class="fas fa-times" title="Not supported"></i> | <i class="fas fa-check" title="Supported"></i> |
| A/B testing | <i class="fas fa-times" title="Not supported"></i> | <i class="fas fa-check" title="Supported"></i> |
| [Dismissing and pinning cards][4] | <i class="fas fa-times" title="Not supported"></i> | <i class="fas fa-check" title="Supported"></i> |
| [Rich analytics][3] (for example, conversion tracking) | <i class="fas fa-times" title="Not supported"></i> | <i class="fas fa-check" title="Supported"></i> |
| [Available in Canvas][2] | <i class="fas fa-times" title="Not supported"></i> | <i class="fas fa-check" title="Supported"></i> |
| [Connected Content][5] | <i class="fas fa-times" title="Not supported"></i> | <i class="fas fa-check" title="Supported"></i> |
| Personalization and segmentation | Templated at impression | Templated at send or first impression |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Implementation

- Content Cards and the News Feed are separate products, so a simple integration for your app or website is necessary in order to use Content Cards.
- If desired, existing News Feed Cards will need to be manually migrated to Content Card campaigns when you switch.
- Content Cards is not intended to be used at the same time as the News Feed, as it is a replacement for the News Feed.
- Content Cards does not currently support categories. Categories can be achieved via [customization and key-value pairs][1].


[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/multiple_feeds/
[2]: {{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/content-cards_in_canvas/
[3]: {{site.baseurl}}/user_guide/message_building_by_channel/content_cards/reporting/
[4]: {{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/#step-2-compose-a-content-card
[5]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/
