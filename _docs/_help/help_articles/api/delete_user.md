---
nav_title: Delete User via API
page_order: 0

page_type: reference
description: "This article describes the implications of deleting a user profile via the Braze REST API."
tool: Dashboard
platform: API
noindex: true
---

# What happens when a user profile is deleted via the REST API?	

When you [delete a user via the Braze API]({{site.baseurl}}/api/endpoints/user_data/#user-delete-endpoint)...	

- The Lifetime Users count (i.e. "Users") will be updated to account for the newly deleted users.	
- The __entire user profile__ will be deleted.	
- The deleted user __will still count__ towards the aggregated conversion percentage.	

However...	
- Custom event counts __will not be updated__ for deleted users.	
- Purchase counts __will not be updated__ for deleted users.	
