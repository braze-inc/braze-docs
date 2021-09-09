---
nav_title: Migrating from News Feed
article_title: Migrating from News Feed
page_order: 10
description: "Content Cards offer many more capabilities that are not supported by Braze's News Feed. This article covers the differences between the two and guidance on migration and adoption."
channel:
  - content cards
  - news feed
  
---

# Migrating From News Feed to Content Cards

Moving from News Feed to Content Cards takes time, but it is an easy adoption! You cannot automatically migrate content from News Feed to Content Cards - you must integrate Content Cards from scratch. However, with the new flexibility of Content Cards, we don't think you'll miss it or mind.

Reach out to your Braze account manager for more details.

## Features and Functionality

Content Cards offers many capabilities that are not supported by Braze's current News Feed, such as additional delivery options like action-based, API delivery, and enhanced analytics like conversion tracking.

As you plan your migration from the News Feed to Content Cards, it will be important to note the main differences between Content Cards and the News Feed:

- Content Cards segmentation is evaluated at the time messages are sent, News Feed segmentation is evaluated at the time that News Feed Cards are viewed.
- Content Cards personalization is templated at the time messages are sent, News Feed card personalization is templated at the time that News Feed Cards are viewed.

| Feature | News Feed | Content Cards |
|---|---|---|
| Transactional and 1:1 Messaging | <i class="fas fa-times"></i> | <i class="fas fa-check"></i> |
| Multivariate and Multi-Channel Campaigns | <i class="fas fa-times"></i> | <i class="fas fa-check"></i> |
| Scheduled, Action-Based, and API-Based Delivery | <i class="fas fa-times"></i> | <i class="fas fa-check"></i> |
| API-Created Messages | <i class="fas fa-times"></i> | <i class="fas fa-check"></i> |
| A/B Testing | <i class="fas fa-times"></i> | <i class="fas fa-check"></i> |
| [Dismissing and Pinning Cards][4] | <i class="fas fa-times"></i> | <i class="fas fa-check"></i> |
| [Rich Analytics][3] | <i class="fas fa-times"></i> | <i class="fas fa-check"></i> |
| [Available in Canvas][2] | <i class="fas fa-times"></i> | <i class="fas fa-check"></i> |
| [Connected Content][5] | <i class="fas fa-times"></i> | <i class="fas fa-check"></i> |
| Personalization and Segmentation | Templated at Impression | Templated at Send |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3} 

## Implementation

- Content Cards and the News Feed are separate products, so a simple integration for your app or website is necessary in order to use Content Cards.
- If desired, existing News Feed Cards will need to be manually migrated to Content Card campaigns when you switch.
- Content Cards is not intended to be used at the same time as the News Feed, as it is a replacement for the News Feed.
- Content Cards does not currently support categories - categories can be achieved via [customization and key-value pairs][1].


[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/multiple_feeds/
[2]: {{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/content-cards_in_canvas/
[3]: {{site.baseurl}}/user_guide/message_building_by_channel/content_cards/reporting/
[4]: {{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/#step-2-compose-a-content-card
[5]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/
