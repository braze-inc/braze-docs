---
nav_title: Deleting Users via API
article_title: Deleting Users via API
page_order: 0

page_type: reference
description: "This article describes the implications of deleting a user profile via the Braze REST API."
tool: Dashboard
platform: API
---

# Deleting users via API

When you [delete a user via the Braze REST API]({{site.baseurl}}/api/endpoints/user_data/#user-delete-endpoint), the following occurs:

- The [Lifetime Users]({{site.baseurl}}/user_guide/data_and_analytics/your_reports/understanding_your_app_usage_data/#lifetime-users) count will be updated to account for the newly deleted users.	
- The entire user profile will be deleted.	
- The deleted user will still count towards the aggregated conversion percentage.	

Custom event counts and purchase counts will not be updated for deleted users.	

_Last updated on October 8, 2019_