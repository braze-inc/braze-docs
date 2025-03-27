---
nav_title: Approvals
article_title: Approvals
page_order: 2
page_type: reference
description: "This reference article gives an overview of the various statuses a campaign and Canvas can have and what they mean."
tool:
    - Campaigns
    - Canvas
---

# Approvals for campaigns and Canvases

> The approval process for campaigns and Canvases adds a review process to your workflow before launch. This way, you can check that each section in the final of the campaign or Canvas editor is approved in order to launch.

## How it works

You can review the details of your campaign or Canvas in the final step of your editor. For campaigns, this is **Review Summary**, and for Canvases, this is **Summary**. 

If your administrator has turned on the approval workflow, each section of the summary must be approved by a user with the appropriate permissions before the message can launch. The default status for each section is **Pending Approval**.

{% tabs %}
{% tab campaign %}
To launch a campaign, you must approve these key components:

- **Messages:** This is the campaign message.
- **Delivery:** This is the delivery type and determines when users will receive the campaign.
- **Target Audience:** This determines who will receive the campaign.
- **Conversion Events:** This is the metric you're tracking for engagement and reporting purposes.
{% endtab %}

{% tab canvas %}
To launch a Canvas, you must approve these key components:

- **Conversion Events:** This is the metric you're tracking for engagement and reporting purposes.
- **Entry Schedule:** This includes the type of entry schedule and when users should enter the Canvas.
- **Target Audience:** This determines who will enter this Canvas.
- **Send Settings:** These are the sending options for all steps in the Canvas. 
- **Build Canvas:** This is the Canvas user journey.
{% endtab %}
{% endtabs %}

## Turning on the approval workflow

By default, the approval workflow setting is turned off for campaigns and Canvases. To turn on this feature, go to **Settings** > **Approval Workflow** and select the applicable toggle:
- **Use approval workflow for all campaigns in [your workspace]**
- **Use approval workflow for all Canvases in [your workspace]**

{% alert important %}
Campaign approval is not supported in the building workflow for [API campaigns]({{site.baseurl}}/api/api_campaigns) and [Transactional Email campaigns]({{site.baseurl}}/user_guide/message_building_by_channel/email/transactional_message_api_campaign).
{% endalert %}

## Setting user permissions

After the approval workflow is turned on, you'll need to set user permissions so your dashboard users can approve or deny the campaigns and Canvases immediately. Both permissions can also be applied to workspaces or [teams]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) or added to a [permission set]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#permission-sets).

{% tabs %}
{% tab campaign %}
You must have the ["Approve and Deny Campaigns" permission]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#managing-limited-and-team-role-permissions). This permission controls who can update the approval status of a campaign. It's possible to self-approve components of a campaign.
{% endtab %}

{% tab canvas %}
You must have the ["Approve and Deny Canvases" permission]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#managing-limited-and-team-role-permissions). A user with this permission can do any of the following actions in the Canvas workflow:

- Approve but not launch the Canvas
- Launch but not approve the Canvas
- Approve and launch the Canvas
- Neither approve or launch the Canvas

After approval statuses are set on the **Summary** step, any subsequent changes made to the Canvas will reset all approval statuses when saved. This applies to any changes made either in a draft Canvas or a post-launch Canvas. For example, if you only make changes to the target audience, the **Summary** step will revert approval statuses for all sections back to the default state, pending.
{% endtab %}
{% endtabs %}

{% alert important %}
To edit a live campaign, you will need the "Approve and Deny Campaigns" permission. A user will need to approve their changes since a draft version of campaigns is not yet available. This is not the case for Canvases as a user can make changes and save as a draft, and another user can approve and launch the Canvas.
{% endalert %}
