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

That is, personal data processed and stored should be kept for no longer than is necessary and personal data should only be processed for legitimate business purposes. Please note, archived users will also have their unsubscribe status deleted in compliance with GDPR.

If you have a user profile in danger of being archived under these policies which needs to be retained, just register a single data point through our REST API for that user profile at least once every six months.

## Inactive users

"Inactive Users" are users that are unreachable and have likely churned. Inactive Users are those that meet all of these criteria:

- Cannot be sent email. For example, they do not have an email address or they are unsubscribed from all email lists.
- Cannot be sent SMS. For example, they do not have a valid phone number or they are unsubscribed from all SMS subscription groups.
- Cannot be sent push. For example, they have uninstalled the app or disabled push permissions.
- Have not used any mobile app or visited a website in an app group in more than six months.
- Have not received any messages from an app group in more than six months.
- Braze has not processed any data points for this user profile in more than six months.

In this case, these users cannot be messaged and are not engaging with your brand. These users have effectively churned.

## Dormant users

"Dormant Users" are users who have had no activity in the last twelve months and:

- Have not used any mobile app or visited a website in an app group in more than twelve months.
- Have not received any messages from an app group in more than twelve months.
- Braze has not processed any data points for this user profile in more than twelve months.

## Spam blocking
Braze blocks individual users with over 5 million sessions, and no longer ingests their SDK events, because they are usually the result of an incorrect integration. If you find that this has happened for a legitimate user, please file a ticket with Braze Support.

[1]: {{site.baseurl}}/help/dp-technical-assistance/#the-right-to-erasure
