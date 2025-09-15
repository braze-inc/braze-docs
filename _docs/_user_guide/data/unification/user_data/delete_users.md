---
nav_title: Deleting users
article_title: Deleting users
page_order: 4.2
toc_headers: h2
description: "Learn how to delete an individual user or a segment of users directly through the Braze dashboard." 
---

# Deleting users

> Learn how to delete an individual user or a segment of users directly through the Braze dashboard.

{% alert important %}
This feature is currently in early access. Contact your customer success manager if you're interested in participating.
{% endalert %}

## Prerequisites

To delete users, you'll need to be an admin or have **Delete User** permissions.

## About user deletion

User deletion lets you manage your database by removing profiles that are no longer needed, created in error, or required to be deleted for compliance (such as GDPR or CCPA).

| Consideration | Details |
|---------------|---------|
| Maximum size | You can delete up to 100 million user profiles when deleting a segment. |
| Waiting period | All segment deletions require a 7-day waiting period plus the time it takes to process deletions. |
| Job limits | Only one segment can be deleted at a single time, which includes the 7-day waiting period. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Deleting users

You can delete an [individual user](#delete-individual) or a [segment of users](#delete-segment) through the Braze dashboard:

### Deleting an individual {#delete-individual}

To delete an individual user from Braze, go to **Audience** > **Search Users**, then search for and select a user. If you're deleting a duplicate user profile, verify that you've selected the right one.

![The 'Search Users' page in Braze.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/search_user.png %}){: style="max-width:75%;"}

{% alert warning %}
Single-user deletions are permanent—profiles cannot be recovered after they're deleted.  
{% endalert %}

On their profile page, select <i class="fa-solid fa-ellipsis-vertical"></i> **Show options** > **Delete User**. Keep in mind, it may take a few minutes for the user to be fully deleted in Braze.

![A user in Braze with the vertical-ellipses menu open, showing the option to delete the user.]({% image_buster /assets/img/audience_management/deleting_users/delete_user.png %}){: style="max-width:85%;"}

### Deleting a segment {#delete-segment}

If you haven't already, [create a segment]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment) containing the user profiles you want to delete. Be sure to include all user profiles if you're deleting duplicate users.

In Braze, go to **Audience** > **Manage Audience**, then select the **Delete Users** tab.

![The 'Delete Users' tab in the 'Manage Audience' section of the Braze dashboard.]({% image_buster /assets/img/audience_management/deleting_users/delete_users_tab.png %}){: style="max-width:85%;"}

Select **Delete users**, choose the segment you want to delete, then select **Next**.

![A pop-up window with a segment chosen for deletion.]({% image_buster /assets/img/audience_management/deleting_users/choose_segment_to_delete.png %}){: style="max-width:75%;"}

Type **DELETE** to confirm your request, then select **Delete users**.

![The confirmation page with 'DELETE' typed in the confirmation box.]({% image_buster /assets/img/audience_management/deleting_users/confirm_segment_delete.png %}){: style="max-width:75%;"}

Your segment won't be deleted immediately. Instead, it will be marked as pending deletion for the next 7 days. After this time, your segment will be deleted and we'll email you to let you know.

{% alert tip %}
To ensure that these exact users are deleted regardless of segment changes, a segment filter called **Pending Deletion** is automatically created. You can [use this filter]({{site.baseurl}}/user_guide/engagement_tools/segments/managing_segments/#filters) to check the status of pending deletions.
{% endalert %}

## Canceling segment deletions {#cancel}

You have 7 days to cancel pending segment deletions. To cancel, go to **Audience** > **Manage Audience**, then select the **Delete Users** tab.

![The 'Delete Users' tab in the 'Manage Audience' section of the Braze dashboard.]({% image_buster /assets/img/audience_management/deleting_users/delete_users_tab.png %}){: style="max-width:85%;"}

Next to a pending segment deletion, select <i class="fa-solid fa-eye"></i> to open the deletion record details.

![A pending segment deletion on the 'Delete Users' tab.]({% image_buster /assets/img/audience_management/deleting_users/pending_deletion.png %})

In the deletion record details, select **Cancel deletion**.

![The 'Deletion Record Details' window on the 'Delete Users' tab.]({% image_buster /assets/img/audience_management/deleting_users/deletion_record_details.png %}){: style="max-width:55%;"}

{% alert tip %}
When bulk user deletion is in progress, you can cancel it at any time. However, any users already deleted before the cancellation cannot be restored.
{% endalert %}

## Checking deletion status {#status}

You can check the status of a deletion using [segment filters](#segment-filters), the [manage audience](#manage-audience) page, or [security event reports](#security-event-report).

### Segment filters

When you delete a segment of users, a [segment filter]({{site.baseurl}}/user_guide/engagement_tools/segments/managing_segments/#filters) called **Pending Deletion** is automatically created. You can use it to:

- See the exact set of users tied to a specific deletion run date.
- Exclude those users from campaigns so they don’t receive messages before removal.
- Export the list if you need it for compliance or record-keeping.

### Manage audience

{% alert note %}
To get the list of exact users that will be deleted, use the [Pending Deletion segment filter](#segment-filters) instead.
{% endalert %}

Go to **Audience** > **Manage Audience**, then select the **Delete Users** tab.

![The 'Delete Users' tab in the 'Manage Audience' section of the Braze dashboard.]({% image_buster /assets/img/audience_management/deleting_users/delete_users_tab.png %}){: style="max-width:85%;"}

On this page, you can find the following general information for all current and pending deletions:

| Field | Description |
|-------|-------------|
| Request Date | The date the request was originally made. Use it with the **Pending Deletion** filter to get the list of profiles pending deletion. |
| Requester | The user who initiated the deletion request. |
| Segment Name | The segment that will be deleted. |
| Status | Shows whether the deletion request is pending, in progress, or complete. |  
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

For more details about a specific request, select <i class="fa-solid fa-eye"></i> to show the deletion record details. Here you can also [cancel pending segment deletions](#cancel).

![A pending segment deletion on the 'Delete Users' tab.]({% image_buster /assets/img/audience_management/deleting_users/pending_deletion.png %})

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

Deleting individual users are permanent.

You can [cancel segment deletions](#cancel) within the first 7 days after. However, any users already deleted before cancelling cannot be restored.
