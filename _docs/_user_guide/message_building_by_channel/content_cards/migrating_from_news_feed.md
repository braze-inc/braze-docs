---
hidden: true
---

# Migrating From News Feed to Content Cards

## Features and Functionality

Content Cards offers many capabilities that are not supported by Braze's current News Feed such as additional delivery options like action-based, API delivery, and enhanced analytics like conversion tracking.

As you plan your migration from the News Feed to Content Cards, it will be important to note the main differences between Content Cards and the News Feed:

- Content Cards segmentation is evaluated at the time messages are sent, News Feed segmentation is evaluated at the time that News Feed Cards are viewed
- Content Cards personalization is templated at the time messages are sent, News Feed card personalization is templated at the time that News Feed Cards are viewed

## Implementation

- Content Cards and the News Feed are separate products so a simple integration in your apps or website is necessary in order to use Content Cards
- If desired, existing News Feed Cards will need to be manually migrated to Content Card Campaigns when you switch from News Feed to Content Cards
- Content Cards is not intended to be used at the same time as the News Feed as it's a replacement for the News Feed
- Content Cards does not currently support categories, use cases for categories can be achieved via customization and key value pairs
