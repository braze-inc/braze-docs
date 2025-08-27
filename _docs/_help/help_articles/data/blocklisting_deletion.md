---
nav_title: Difference between blocklisting and deletion
article_title: Difference Between Blocklisting and Deletion
page_order: 2

page_type: solution
description: "This help article walks you through the difference between attribute blocklisting and deletion."
---

# Difference between blocklisting and deleting

To understand the difference between blocklisting an deleting attributes in Braze, let's review the results of each action:

- **Blocklisting:** If custom attributes, events, or purchases are blocklisted, they will remain on the user profile, but no new requests for the attribute will be processed.
- **Deletion:** If custom attributes, events, or purchases are deleted, the data will be removed. However, Braze will still accept new incoming requests for that attribute if it's still tracked via the SDK or uploaded via API or CSV.

## Which should I do?

To accomplish blocklisting, Braze will have to send the blocklisting information down to each user's device, and it will be a data-intensive operation, which we ideally try to avoid. Also, if the list is too large (> 100 attributes, events, or purchases), your app can begin to slow down. 

If you aren't planning to send attributes to Braze anymore, the deletion route would be the recommended approach.

Regardless of your route, the custom attributes, events, and purchases you wish to remove will no longer appear on the **Manage Workspace** page, which removes them as segment filters. User-level data will remain on the profiles. 