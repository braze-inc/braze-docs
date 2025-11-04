---
nav_title: Removing users via API
article_title: Removing Users via API
page_order: 0

page_type: reference
description: "This help article describes the implications of removing a user profile via the Braze REST API."
tool: Dashboard
platform: API
---

# Removing users via API

When you [remove a user via the Braze REST API]({{site.baseurl}}/api/endpoints/user_data/#user-delete-endpoint/), the following data is deleted (nulled):
- Any attributes that the user had
- Email address
- Phone number
- External user ID 
- Gender
- Country
- Language

When you [remove a user via the Braze REST API]({{site.baseurl}}/api/endpoints/user_data/#user-delete-endpoint/), the following events occur:
- The user profile is deleted (nulled).
- The [Lifetime Users]({{site.baseurl}}/user_guide/data_and_analytics/analytics/understanding_your_app_usage_data/#lifetime-users) count will be updated to account for the newly removed users.	
- The removed user will still count toward the aggregated conversion percentage. Custom event counts and purchase counts will not be updated for removed users.

## Multiple profiles with a shared email address

Let's say you want to merge multiple user profiles that share the same email address. 

To merge these user profiles:

 1. Identify any users with duplicate email addresses. 
 2. Export all the attributes of a single profile. 
 3. Import those attributes to the user profile either via API or CSV. 
 4. Remove the users via API, essentially deleting these duplicate users and the data outlined above.

_Last updated on September 13, 2023_

