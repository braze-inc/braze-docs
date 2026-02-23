---
nav_title: Approvals
article_title: Approvals
page_order: 1
page_type: reference
description: "This reference article gives an overview of the various statuses a campaign and Canvas can have and what they mean."
tool:
    - Campaigns
    - Canvas
---

# Approvals for campaigns and Canvases

> Use approvals to add a final checkpoint to your campaigns and Canvases before launch. With this workflow, you can verify and approve the content in all required sections of your message.

## How it works

You can review the details of your Campaign or Canvas in the final step of editing. 

For both Canvases and Campaigns, you must save all changes before approving, even if they're your own changes. A user with the appropriate permissions must approve each section of the summary before the message can launch. The default status for each section is **Pending Approval**.

{% tabs %}
{% tab campaign %}
To launch a Campaign, you must approve these components:

- **Messages:** This is the Campaign message.
- **Delivery:** This is the delivery type and determines when users receive the Campaign.
- **Target Audience:** This determines who will receive the Campaign.
- **Conversion Events:** This is the metric you're tracking for engagement and reporting purposes.
{% endtab %}

{% tab canvas %}
To launch a Canvas, you must approve these key components:

- **Conversion Events:** This is the metric you're tracking for engagement and reporting purposes.
- **Entry Schedule:** This includes the type of entry schedule and when users enter the Canvas.
- **Target Audience:** This determines who will enter this Canvas.
- **Send Settings:** These are the sending options for all steps in the Canvas. 
- **Build Canvas:** This is the Canvas user journey.
{% endtab %}
{% endtabs %}

## Turning on the approval workflow

By default, the approval workflow setting is off for Campaigns and Canvases. To turn on this feature, go to **Settings** > **Approval Workflow** and select the applicable toggle:

- **Use approval workflow for all Campaigns in [your workspace]**
- **Use approval workflow for all Canvases in [your workspace]**

{% alert important %}
Campaign approval is not supported for [API campaigns]({{site.baseurl}}/api/api_campaigns) and [Transactional Email campaigns]({{site.baseurl}}/user_guide/message_building_by_channel/email/transactional_message_api_campaign).
{% endalert %}

## Setting user permissions

After you turn on the approval workflow, you must set user permissions so your company users can approve or deny Campaigns and Canvases. Both permissions can also be applied to Workspaces or [Teams]({{site.baseurl}}/user_guide/administer/global/user_management/teams/) or added to a [permission set]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/#permission-sets).

{% tabs %}
{% tab campaign %}
You must have the ["Approve and Deny Campaigns" permission]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/#managing-limited-and-team-role-permissions). This permission controls who can update the approval status of a campaign. With this permission, you can do the following:

- Self-approve the Campaign
- Approve and launch the Campaign
- Approve but not launch the Campaign (a different user with the "Send Campaigns, Canvases" permission can launch the Campaign)
- Neither approve nor launch the Campaign

After approval statuses are set on the **Summary** step, any subsequent changes made to the Campaign reset all approval statuses when saved. This applies to any changes made either in a draft Campaign or a post-launch campaign. For example, if you only make changes to the Target Audience, the **Summary** step reverts approval statuses for all sections back to the default state, **Pending Approval**.

{% endtab %}

{% tab canvas %}
You must have the ["Approve and Deny Canvases" permission]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/#managing-limited-and-team-role-permissions). This permission controls who can update the approval status of a Canvas. With this permission, you can do the following:

- Self-approve the Canvas
- Approve and launch the Canvas
- Approve but not launch the Canvas (a different user with the "Send Campaigns, Canvases" permission can launch the Canvas)
- Neither approve nor launch the Canvas

After approval statuses are set on the **Summary** step, any subsequent changes made to the Canvas reset all approval statuses when saved. This applies to any changes made either in a draft Canvas or a post-launch Canvas. For example, if you only make changes to the target audience, the **Summary** step reverts approval statuses for all sections back to the default state, **Pending Approval**.

{% alert note %}
**Approval status and saving**

- When you click **Approve** for a section on the **Summary** step, that approval is saved immediately.
- The **Save** button saves changes to the Canvas content and settings, not the approval status.

To avoid losing approvals:

1. Make any Canvas edits you need, then click **Save**.
2. After the Canvas finishes saving, approve the relevant sections on the **Summary** step.
3. Click **Save** again only if you make additional Canvas changes after approval. If you change the Canvas and save, all approval statuses reset to **Pending Approval**.
{% endalert %}
{% endtab %}
{% endtabs %}

{% alert important %}
To edit a live Campaign, you need the "Approve and Deny Campaigns" permission. A user must approve their changes because a draft version of Campaigns is not yet available. This is not the case for Canvases as a user can make changes and save as a draft, and another user can approve and launch the Canvas.
{% endalert %}