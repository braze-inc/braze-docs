---
nav_title: Deleting users
article_title: Deleting users
page_order: 4.2
toc_headers: h2
description: "TODO" 
---

# Deleting users

> Learn how to delete one or more user profiles directly through the Braze dashboard.

{% alert important %}
This feature is currently in early access. Contact your customer success manager if you're interested in participating.
{% endalert %}

## Prerequisites

Before you can delete users, you'll need to be an admin or have **Delete User** permissions.

## About user deletion

User deletion lets you manage your database by removing profiles that are no longer needed, created in error, or required to be deleted for compliance (such as GDPR or CCPA).

| Consideration | Details |
|---------------|---------|
| Maximum size | You can delete up to 100 million user profiles in a bulk deletion. |
| Processing time | All bulk deletions require a 7-day waiting period plus the time it takes to process deletions. |
| Job limits | Only one bulk deletion can run at a time, which also includes the 7-day waiting period. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Deleting users

### Individual

To delete an individual user from Braze, go to **Audience** > **Search Users**, then search for and select a user. If you're deleting a duplicate user profile, verify that you've selected the right one.

![ALT_TEXT]()

{% alert warning %}
Single-user deletions are permanent—profiles cannot be recovered after they're deleted.  
{% endalert %}

On their profile page, select **More Actions** > **Delete User**. Keep in mind, it may take a few minutes for the user to be fully deleted in Braze.

![ALT_TEXT]()

### Bulk

If you haven't already, [create a segment]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment) containing the user profiles you want to delete. Be sure to include all user profiles if you're deleting duplicate users.

Next, go to **Audience** > **Manage Audience**, then select the **Delete Users** tab.

![ALT_TEXT]()

Choose the segment you want to delete, then select **Delete users**. Note that bulk user deletion may take a while&#8212;come back here to [check the status](#status).

When the segment is deleted, we'll email you to let you know.

![ALT_TEXT]()

{% alert note %}
To ensure that these exact users are deleted regardless of segment changes, a [segment filter]({{site.baseurl}}/user_guide/engagement_tools/segments/managing_segments/#filters) called **Pending Deletion** is automatically created.
{% endalert %}

## Canceling bulk deletions

You have 7 days to cancel bulk deletion requests. To cancel, go to **Audience** > **Manage Audience**, then select the **Delete Users** tab.

![ALT_TEXT]()

Next to a pending bulk deletion, select **Cancel**.

![ALT_TEXT]()

{% alert tip %}
When bulk user deletion is in progress, you can cancel it at any time. However, any users already deleted before the cancellation cannot be restored.
{% endalert %}

## Checking deletion status {#status}

To check the status of a deletion, use one of the following methods:

### Segment filters

When you delete a segment of users, a [segment filter]({{site.baseurl}}/user_guide/engagement_tools/segments/managing_segments/#filters) called **Pending Deletion** is automatically created. You can use it to:

- See the exact set of users tied to a specific deletion run date.
- Exclude those users from campaigns so they don’t receive messages before removal.
- Export the list if you need it for compliance or record-keeping.

### Manage audience

{% alert note %}
If your segment is dynamic, use the [Pending Deletion segment filter](#segment-filters) instead.
{% endalert %}

Go to **Audience** > **Manage Audience**, then select the **Delete Users** tab.

![ALT_TEXT]()

For each deletion request, you can check who initiated the deletion, the current status, and how many user profiles were deleted. Refer to the following table for more details:

| Field | Description |
|-------|-------------|
| Run Date | Shows the scheduled deletion date. Use it with the **Pending Deletion** filter to find all profiles marked for that run. |
| Segment Name | Shows the original segment used to generate the set of profiles marked for deletion. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Security event report

You can also check the status of previous deletions by downloading a security event report. For more information, see [Security settings]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/#security-event-report).

## Frequently asked questions {#faq}

### Can I delete segments with more than 100 million users?

No. You cannot delete segments with more than 100 million users. If you need help deleting a segment of this size, contact [support@braze.com](mailto:support@braze.com).

### Does automated user merging affect user deletion?

If a scheduled merge includes user profiles pending deletion, Braze skips those profiles and does not merge them. To merge these profiles, you must remove them from deletion.

### What happens to data sent to users pending deletion?

Data sent from external systems or SDKs is still accepted, but the users will be deleted as scheduled regardless of activity.

### Will Canvases and campaigns trigger for users pending deletion?

Yes. However, you can add a segment inclusion filter to exclude all users with the **Pending Deletion** [segment filter](#segment-filters).

### Can I recover deleted user profiles?

Deleting a single user is permanent.

You can [cancel pending bulk deletions](#canceling-bulk-deletions) up to 7 days after starting the request. However, any users already deleted before cancelling cannot be restored.
