---
nav_title: Difference between blocklisting and deletion
article_title: Difference Between Blocklisting and Deletion
page_order: 2

page_type: solution
description: "This help article walks you through the difference between attribute blocklisting and deletion."
---

# Difference between blocklisting and deleting

To understand the difference between blocklisting and deleting custom data in Braze, review the results of each action:

- **Blocklisting:** If custom attributes, events, or purchases are blocklisted, they remain on user profiles, but Braze no longer processes new data for those objects.
- **Deletion:** If custom attributes, events, or purchases are deleted, Braze removes that data from user profiles. Deleted custom attributes and events move to `Trashed` for seven days, during which you can restore them. After seven days, Braze permanently deletes them. Deleting also doesn't prevent new incoming data, so make sure the data is no longer being sent through your SDK, API, or CSV imports before you delete it.

## Which should I do?

To accomplish blocklisting, Braze will have to send the blocklisting information down to each user's device, and it will be a data-intensive operation, which we ideally try to avoid. Also, if the list is too large (> 100 attributes, events, or purchases), your app can begin to slow down. 

If you aren't planning to send attributes to Braze anymore, the deletion route would be the recommended approach.

Regardless of your route, the custom attributes, events, and purchases you remove no longer appear on the **Manage Workspace** page, which removes them as segment filters. If you delete custom data, Braze removes that user-level data from profiles. 