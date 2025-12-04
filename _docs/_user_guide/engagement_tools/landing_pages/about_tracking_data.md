---
nav_title: About tracking data
article_title: About landing page tracking data
description: "Learn about tracking and anonymized data for landing pages in Braze."
page_order: 10
alias: /landing_pages/data_tracking/
---

# About landing page tracking data

> Learn about tracking and anonymized data for landing pages in Braze.

## Tracking methods

### Web SDK

The Braze web SDK is initialized only when a user submits a form on the landing page. Prior to form submission, no personal data is collected and the SDK doesn't actively track users. After initialization is completed, the SDK doesn't store any data in the browser (such as cookies, local storage, or others).

When a form is submitted, the SDK will collect the following data:

- Form submission event (name of event and time of submission)
- Data specified by your team in the form (such as name, email, and phone number)
- Session start time
- Device ID (a unique ID that is generated, but not stored, for the device)
- Country determined by IP address

### Anonymized data

Before a user submits a form, the data tracked on a landing page consists only of anonymized, non-identifiable information. This consists of standard website aggregate metrics like the number of page views (impressions) and clicks that a landing page receives.

Because this data isn't linked to identifiable users, it can't be used to retarget or track individual user behavior.

## Merging duplicate user profiles

Braze doesn't automatically merge users based on attributes, such as email or phone, when a landing page form is submitted. If a form is submitted with an email or phone number that matches an existing user profile, Braze creates a separate user profile.

To merge duplicate user profiles, you can:

- Trigger the [`/users/merge` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/) when a landing page form is submitted to merge the new profile with an existing profile.
- Schedule [bulk merging]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users/#bulk-merging) to periodically merge duplicate profiles based on matching identifiers.

