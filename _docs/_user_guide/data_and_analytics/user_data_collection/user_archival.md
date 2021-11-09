---
nav_title: User Archival Definitions
article_title: User Archival
page_order: 0
page_type: reference
description: "This reference article covers user archival definitions."

---
# User archival definitions

Each week, Braze runs a process to remove Inactive Users and Dormant Users from the Braze Services.

This process ensures that Braze provides accurate statistics regarding campaign reachable audiences. It also serves in accordance with two key concepts of [GDPR][1]:

1. The storage limitation principle - personal data processed and stored should be kept for no longer than is necessary
2. Having a legitimate business purpose to process personal data.

That is, personal data processed and stored should be kept for no longer than is necessary and personal data should only be processed for legitimate business purposes. Archived users will also have their unsubscribe status deleted in compliance with GDPR.

If you have a user profile in danger of being archived under these policies which needs to be retained, then register a single data point through our REST API for that user profile at least once every six months.

## Inactive users

"Inactive Users" are users that are unreachable and have likely churned. Inactive Users are those that meet all of these criteria:

- Can't receive email. For example, they do not have an email address or they are unsubscribed from all email lists.
- Can't receive SMS. For example, they do not have a valid phone number or they are unsubscribed from all SMS subscription groups.
- Can't receive push. For example, they have uninstalled the app or disabled push permissions.
- Haven't used any mobile app or visited a website in an app group in more than six months.
- Haven't received any messages from an app group in more than six months.
- Braze hasn't processed any data points for this user profile in more than six months.

In this case, these users cannot be messaged and are not engaging with your brand. These users have effectively churned.

## Dormant users

"Dormant Users" are users who have had no activity in the last twelve months and:

- Haven't used any mobile app or visited a website in an app group in more than 12 months.
- Haven't received any messages from an app group in more than 12 months.
- Braze hasn't processed any data points for this user profile in more than 12 months.

## Spam blocking

Braze blocks individual users with over 5 million sessions ("dummy users"), and no longer ingests their SDK events, because they are usually the result of an incorrect integration. If you find that this has happened for a legitimate user, please file a ticket with Braze [support]({{site.baseurl}}/braze_support/).

To find your dashboard's dummy users, perform the following steps:

1. Create a [segment]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/).
2. Select the filter `Session Count` and set it to `more than 5,000,000`.
3. Export the segment via CSV.

If necessary, you can delete the users via the [Users Delete]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/) API endpoint.

[1]: {{site.baseurl}}/help/dp-technical-assistance/#the-right-to-erasure
