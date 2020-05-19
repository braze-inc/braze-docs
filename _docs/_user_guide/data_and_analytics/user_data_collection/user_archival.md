---
nav_title: User Archival Definitions
page_order: 0
description: "This reference article covers user archival definitions."
---
# User Archival Definitions

## Inactive Users

"Inactive Users" are users that are unreachable and have likely churned. Inactive Users are those that meet all of these criteria:

- Cannot be sent email. For example, they do not have an email address or they are unsubscribed from all email lists.
- Cannot be sent push. For example, they have uninstalled the app or disabled push permissions.
- Have not used any mobile app or visited a website in an app group in more than six months.
- Have not received any messages from an app group in more than six months.
- Braze has not processed any data points for this user profile in more than six months.

In this case, these users cannot be messaged and are not engaging with your brand. These users have effectively churned.

## Dormant Users

"Dormant Users" are users who have had no activity in the last twelve months and:

- Have not used any mobile app or visited a website in an app group in more than twelve months.
- Have not received any messages from an app group in more than twelve months.
- Braze has not processed any data points for this user profile in more than twelve months.

Each week, Braze runs a process to remove Inactive Users and Dormant Users from the Braze Services.

This process ensures that Braze provides accurate statistics regarding campaign reachable audiences. It also serves in accordance with two key concepts of [GDPR][1]:

1. The storage limitation principle - personal data processed and stored should be kept for no longer than is necessary
2. Having a legitimate business purpose to process personal data.

That is, personal data processed and stored should be kept for no longer than is necessary and personal data should only be processed for legitimate business purposes.

If you have a user that meets the above criteria that you do not want to become Inactive or Dormant, you may simply register a single data point for that profile once every six months.

{% alert important %}
Braze will ban or block individual users ("dummy users") with over 5 million sessions and no longer ingest their SDK events, because they are usually the result of an incorrect integration. If you find that this has happened for a legitimate user, please reach out to your Braze account manager.
{% endalert %}

[1]: {{site.baseurl}}/help/gdpr_compliance/#braze-recommendation
