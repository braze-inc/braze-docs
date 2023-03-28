---
nav_title: Difference Between Blocklisting and Deletion
article_title: Difference Between Blocklisting and Deletion
page_order: 0

page_type: solution
description: "This help article walks you through the difference between attribute blocklisting and deletion."
---

# Difference between blocklisting and deleting

The difference between blocklisting and deletion are as follows:
- Blocklisting: If custom attributes, events, or purchases are blocklisted, they will remain on the user profile, but no new requests for the attribute will be processed.
- Deletion: If custom attributes, events, or purchases are deleted, the data will be removed, but Braze will still accept new incoming requests for that attribute if it is still tracked via the SDK or uploaded via the API or CSV. 

## Which should I do?

To accomplish blocklisting, Braze will have to send the blocklisting info down to each user's device, and it will be a data-intensive operation, which we ideally try to avoid. Also, if the list is too large (>100 attributes, events, or purchases), your app can begin to slow down. If you are not planning to send attributes to Braze anymore, the deletion route would be the recommended approach.

Regardless of your route, the custom attributes, events, and purchases you wish to remove will no longer appear on the **Manage Workspace** page, which removes them as segment filters. User-level data will remain on the profiles. 

