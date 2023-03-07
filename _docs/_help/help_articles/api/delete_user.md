---
nav_title: Deleting Users via API
article_title: Deleting Users via API
page_order: 0

page_type: reference
description: "This help article describes the implications of deleting a user profile via the Braze REST API."
tool: Dashboard
platform: API
---

# Deleting users via API

When you [delete a user via the Braze REST API][1], the following events occur:

- The [Lifetime Users][2] count will be updated to account for the newly deleted users.	
- The entire user profile will be deleted.	
- The deleted user will still count towards the aggregated conversion percentage. Custom event counts and purchase counts will not be updated for deleted users.

After a user is deleted, Braze does not keep any of the following data:
- Any attributes that the user had
- Email address
- Phone number
- External user ID 
- Gender
- Country
- Language
- Other similar data

## Multiple profiles with a shared email address

Let's say you want to merge multiple user profiles that share the same email address. 

To merge these user profiles:

 1. Identify any users with duplicate email addresses. 
 2. Export all the attributes of a single profile. 
 3. Import those attributes to the user profile either via API or CSV. 
 4. Delete the users via API, essentially deleting these duplicate users and the data outlined above.

_Last updated on October 24, 2022_

[1]: {{site.baseurl}}/api/endpoints/user_data/#user-delete-endpoint/
[2]: {{site.baseurl}}/user_guide/data_and_analytics/analytics/understanding_your_app_usage_data/#lifetime-users